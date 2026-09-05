#!/usr/bin/env python3
"""Build and check SCUTER distributions using only this checkout and Python 3.10+."""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import posixpath
from pathlib import Path
import re
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SOURCES = {
    "skills/scuter/SKILL.md": "SKILL.md",
    "protocol/01.work-contract.md": "references/protocol.md",
    "docs/implementation-guide.md": "references/implementation-guide.md",
    "docs/notion-setup.md": "references/notion-setup.md",
    "docs/record-and-review.md": "references/record-and-review.md",
    "LICENSE.md": "LICENSE.md",
}
STAMP = (2020, 1, 1, 0, 0, 0)


def read_file(root: Path, name: str) -> bytes:
    path = root / name
    if path.is_symlink() or not path.resolve().is_relative_to(root.resolve()):
        raise ValueError(f"Source escapes checkout: {name}")
    return path.read_bytes()


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def expected_outputs(root: Path) -> dict[str, bytes]:
    version = read_file(root, "VERSION").decode("ascii").strip()
    if not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+(?:-[a-z0-9.-]+)?", version):
        raise ValueError("Invalid VERSION")
    sources = {name: read_file(root, name) for name in SOURCES}
    members = {SOURCES[name]: data for name, data in sources.items()}
    members["references/implementation-guide.md"] = members["references/implementation-guide.md"].replace(b"../protocol/01.work-contract.md", b"protocol.md")
    entry = members["SKILL.md"].decode("utf-8")
    if not entry.startswith("---\n") or "\n---\n" not in entry[4:]:
        raise ValueError("Missing Skill frontmatter")
    frontmatter = entry.split("---\n", 2)[1]
    if not re.search(r"^name: scuter$", frontmatter, re.M):
        raise ValueError("Skill name must match directory scuter")
    description = re.search(r"^description: (.+)$", frontmatter, re.M)
    if not description or not 1 <= len(description[1]) <= 1024:
        raise ValueError("A single-line description of 1-1024 characters is required")
    if f'  version: "{version}"' not in frontmatter:
        raise ValueError("Skill metadata and VERSION disagree")
    for name, data in members.items():
        text = data.decode("utf-8")
        if not text.endswith("\n"):
            raise ValueError(f"Missing final newline: {name}")
    for target in re.findall(r"\]\((references/[^)#]+)(?:#[^)]*)?\)", entry):
        if target not in members:
            raise ValueError(f"Missing companion file: {target}")
    for name, data in members.items():
        for target in re.findall(r"\]\(([^)]+)\)", data.decode("utf-8")):
            target = target.split("#", 1)[0]
            if target and ":" not in target and target.endswith(".md"):
                resolved = posixpath.normpath(posixpath.join(posixpath.dirname(name), target))
                if resolved not in members:
                    raise ValueError(f"Missing local document: {name} -> {target}")
    protocol = members["references/protocol.md"].decode("utf-8")
    for directive in ("USER-AUTHORITY", "PRIOR-ART-LINEAGE", "REFERENCE-VALIDATION", "PRACTICE", "DURABLE-RECORD"):
        if directive not in protocol or directive not in entry:
            raise ValueError(f"Missing directive: {directive}")
    manifest = {
        "name": "scuter", "version": version, "status": "development",
        "protocol_source": {"path": "protocol/01.work-contract.md", "sha256": sha256(sources["protocol/01.work-contract.md"])},
        "source_files_sha256": {name: sha256(data) for name, data in sorted(sources.items())},
        "members_sha256": {name: sha256(data) for name, data in sorted(members.items())},
        "document_link_adjustment": "The bundled implementation guide links to references/protocol.md within the Skill.",
    }
    manifest_bytes = (json.dumps(manifest, indent=2) + "\n").encode("utf-8")
    members["MANIFEST.json"] = manifest_bytes
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w", compression=zipfile.ZIP_STORED) as archive:
        for name, data in sorted(members.items()):
            item = zipfile.ZipInfo("scuter/" + name, STAMP)
            item.create_system = 3
            item.external_attr = 0o100644 << 16
            item.compress_type = zipfile.ZIP_STORED
            archive.writestr(item, data)
    archive_bytes = stream.getvalue()
    # Read every member back, including CRC validation, and reject unexpected entries.
    with zipfile.ZipFile(io.BytesIO(archive_bytes)) as archive:
        if set(archive.namelist()) != {"scuter/" + name for name in members}:
            raise ValueError("Unexpected archive member set")
        for name, data in members.items():
            if archive.read("scuter/" + name) != data:
                raise ValueError(f"Archive member mismatch: {name}")
    markdown = [f"# SCUTER {version}\n\nScientific Collaboration for User-directed, Traceable, Evidence-based Research.\n\nThis complete instruction edition includes the entry instructions and all companion text below. References to named files refer to the corresponding sections in this document. The User supplies project locations, permissions, roles, and acceptance criteria.\n"]
    for name, data in members.items():
        if name == "MANIFEST.json":
            continue
        markdown.append(f"\n---\n\n## Included file: {name}\n\n" + data.decode("utf-8"))
    markdown.append("\n---\n\n## Content manifest\n\n```json\n" + manifest_bytes.decode("utf-8") + "```\n")
    md_bytes = "".join(markdown).encode("utf-8")
    outputs = {"skills/scuter/" + name: data for name, data in members.items() if name != "SKILL.md"}
    outputs[f"dist/scuter-v{version}.skill"] = archive_bytes
    outputs[f"dist/scuter-v{version}.md"] = md_bytes
    sums = "".join(f"{sha256(data)}  {Path(name).name}\n" for name, data in sorted(outputs.items()) if name.startswith("dist/"))
    outputs["dist/SHA256SUMS"] = sums.encode("ascii")
    return outputs


def build(root: Path, check: bool = False) -> int:
    outputs = expected_outputs(root)
    expected_members = {str(Path(path).relative_to("skills/scuter")) for path in outputs if path.startswith("skills/scuter/")} | {"SKILL.md"}
    actual_members = {str(path.relative_to(root / "skills/scuter")) for path in (root / "skills/scuter").rglob("*") if path.is_file()}
    if actual_members - expected_members:
        raise ValueError(f"Unexpected Skill files: {sorted(actual_members - expected_members)}")
    for name, data in outputs.items():
        path = root / name
        if path.is_symlink() or not path.resolve().is_relative_to(root.resolve()):
            raise ValueError(f"Output escapes checkout: {name}")
        if check:
            if not path.is_file() or path.read_bytes() != data:
                raise ValueError(f"Missing or stale generated artifact: {name}")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
    print(f"PASS: {len(outputs)} generated artifacts {'verified' if check else 'built'}; source and archive agree")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Verify without writing")
    args = parser.parse_args()
    try:
        return build(ROOT, args.check)
    except (OSError, ValueError, KeyError, zipfile.BadZipFile, UnicodeError) as error:
        print(f"SCUTER build failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
