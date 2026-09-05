#!/usr/bin/env python3
"""Import a pinned, allowlisted public source snapshot without rewriting bytes.

This one-time migration utility has no credentials or repository-write logic.
The bootstrap workflow separately commits only the explicit destination paths.
After migration, --check verifies a checkout against the initial import plan.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import platform
import sys
import urllib.request
import zipfile

MAX_BYTES = 5 * 1024 * 1024


def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()


def safe_path(value: str) -> PurePosixPath:
    path = PurePosixPath(value)
    if not value or path.is_absolute() or ".." in path.parts or "\\" in value:
        raise ValueError(f"Unsafe relative path: {value!r}")
    return path


def check_blob(data: bytes, expected: str, path: str) -> None:
    actual = git_blob_sha(data)
    if actual != expected:
        raise ValueError(f"Blob mismatch for {path}: expected {expected}, found {actual}")


def check_package(files: dict[str, bytes], skill_dir: str, archive: str) -> dict:
    """Compare every archived file with its source, and validate member hashes."""
    prefix = skill_dir.rstrip("/") + "/"
    source = {p[len(prefix):]: b for p, b in files.items() if p.startswith(prefix)}
    if "SKILL.md" not in source or "MANIFEST.json" not in source:
        raise ValueError("Missing Skill entry point or manifest")
    manifest = json.loads(source["MANIFEST.json"])
    expected_members = manifest["members_sha256"]
    if set(expected_members) != set(source) - {"MANIFEST.json"}:
        raise ValueError("Manifest member list and source file set disagree")
    for name, expected in expected_members.items():
        safe_path(name)
        if hashlib.sha256(source[name]).hexdigest() != expected:
            raise ValueError(f"Source manifest checksum mismatch: {name}")
    with zipfile.ZipFile(io.BytesIO(files[archive])) as zf:
        entries = [x for x in zf.infolist() if not x.is_dir()]
        names = [x.filename for x in entries]
        if len(names) != len(set(names)):
            raise ValueError("Duplicate archive members")
        if sum(x.file_size for x in entries) > MAX_BYTES:
            raise ValueError("Uncompressed archive exceeds migration limit")
        for name in names:
            safe_path(name)
        entry_points = [n for n in names if PurePosixPath(n).name == "SKILL.md"]
        if len(entry_points) != 1:
            raise ValueError("Expected exactly one SKILL.md in archive")
        root = entry_points[0][:-len("SKILL.md")]
        if any(not n.startswith(root) for n in names):
            raise ValueError("Archive files outside Skill root")
        relative = {n[len(root):]: n for n in names}
        if set(relative) != set(source):
            raise ValueError(f"Archive/source member sets differ: {set(relative) ^ set(source)}")
        for rel, name in relative.items():
            if zf.read(name) != source[rel]:
                raise ValueError(f"Archive/source byte mismatch: {rel}")
    return {"status": "passed", "source_file_count": len(source),
            "manifest_hashed_members": len(expected_members), "archive_root": root,
            "version": manifest["version"],
            "protocol_snapshot": manifest["protocol_source"]["commit"]}


def collect(plan: dict, root: Path, fetch: bool) -> dict[str, bytes]:
    repository = plan["source_repository"]
    commit = plan["source_commit"]
    if repository != "TaylorResearchLab/beyond-the-chat-window":
        raise ValueError("Unexpected source repository")
    if len(commit) != 40 or any(c not in "0123456789abcdef" for c in commit):
        raise ValueError("A complete source commit SHA is required")
    files: dict[str, bytes] = {}
    for item in plan["files"]:
        src = str(safe_path(item["source_path"]))
        dst = str(safe_path(item["destination_path"]))
        if dst in files:
            raise ValueError(f"Duplicate destination: {dst}")
        target = root / dst
        if target.is_symlink() or not target.resolve().is_relative_to(root.resolve()):
            raise ValueError(f"Destination escapes checkout: {dst}")
        if fetch:
            url = f"https://raw.githubusercontent.com/{repository}/{commit}/{src}"
            request = urllib.request.Request(url, headers={"User-Agent": "SCUTER-snapshot-import"})
            with urllib.request.urlopen(request, timeout=30) as response:
                data = response.read(MAX_BYTES + 1)
            if len(data) > MAX_BYTES:
                raise ValueError(f"Source file exceeds size limit: {src}")
        else:
            data = target.read_bytes()
        check_blob(data, item["git_blob_sha"], src)
        if target.exists() and target.read_bytes() != data:
            raise ValueError(f"Refusing to overwrite a modified destination: {dst}")
        files[dst] = data
    return files


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Verify existing files without downloading or writing")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    plan_bytes = (root / "provenance/import-plan.json").read_bytes()
    plan = json.loads(plan_bytes)
    files = collect(plan, root, fetch=not args.check)
    package = check_package(files, plan["skill_directory"], plan["package_path"])
    if not args.check:
        # Validate every source and the complete archive before writing any imported file.
        for rel, data in files.items():
            target = root / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            if not target.exists():
                with target.open("xb") as stream:
                    stream.write(data)
        report = {
            "schema_version": 1,
            "source_repository": plan["source_repository"],
            "source_commit": plan["source_commit"],
            "import_plan_sha256": hashlib.sha256(plan_bytes).hexdigest(),
            "workflow_run_id": os.environ.get("GITHUB_RUN_ID"),
            "bootstrap_commit": os.environ.get("GITHUB_SHA"),
            "python": platform.python_version(),
            "checks": {"source_git_blobs": "passed", "archive_source_agreement": package},
            "files": [{**item, "bytes": len(files[item["destination_path"]]),
                       "sha256": hashlib.sha256(files[item["destination_path"]]).hexdigest()}
                      for item in plan["files"]],
        }
        report_path = root / "provenance/import-report.json"
        if not report_path.exists():
            report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"status": "passed", "imported_files": len(files),
                      "mode": "check" if args.check else "import", "package": package}, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, KeyError, zipfile.BadZipFile) as error:
        print(f"Migration failed: {error}", file=sys.stderr)
        raise SystemExit(1)
