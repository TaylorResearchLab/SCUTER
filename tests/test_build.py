"""Offline checks of deterministic packaging and failure detection."""
from contextlib import redirect_stdout
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
import zipfile

SPEC = importlib.util.spec_from_file_location("scuter_build", Path(__file__).resolve().parents[1] / "tools/build.py")
BUILD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BUILD)


class PackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in BUILD.SOURCES:
            p = self.root / name
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text("Example documentation.\n", encoding="utf-8")
        (self.root / "VERSION").write_text("0.2.0\n", encoding="ascii")
        rules = "USER-AUTHORITY PRIOR-ART-LINEAGE REFERENCE-VALIDATION PRACTICE DURABLE-RECORD\n"
        (self.root / "protocol/01.work-contract.md").write_text(rules)
        (self.root / "skills/scuter/SKILL.md").write_text('---\nname: scuter\ndescription: Coordinate scientific work with a User-directed record.\nmetadata:\n  version: "0.2.0"\n---\n\n' + rules + "[Protocol](references/protocol.md)\n")

    def run_build(self, check=False):
        with redirect_stdout(io.StringIO()):
            return BUILD.build(self.root, check)

    def test_reproducible_build_and_offline_check(self):
        first = BUILD.expected_outputs(self.root)
        second = BUILD.expected_outputs(self.root)
        self.assertEqual(first, second)
        self.run_build()
        self.assertEqual(self.run_build(check=True), 0)

    def test_archive_members_and_manifest(self):
        outputs = BUILD.expected_outputs(self.root)
        with zipfile.ZipFile(io.BytesIO(outputs["dist/scuter-v0.2.0.skill"])) as archive:
            manifest = json.loads(archive.read("scuter/MANIFEST.json"))
            for name, checksum in manifest["members_sha256"].items():
                self.assertEqual(BUILD.sha256(archive.read("scuter/" + name)), checksum)

    def test_tampered_package_is_rejected(self):
        self.run_build()
        (self.root / "dist/scuter-v0.2.0.skill").write_bytes(b"tampered")
        with self.assertRaises(ValueError):
            self.run_build(check=True)

    def test_changed_protocol_requires_rebuild(self):
        self.run_build()
        path = self.root / "protocol/01.work-contract.md"
        path.write_text(path.read_text() + "New requirement.\n")
        with self.assertRaises(ValueError):
            self.run_build(check=True)

    def test_version_mismatch_is_rejected(self):
        (self.root / "VERSION").write_text("0.3.0\n")
        with self.assertRaises(ValueError):
            BUILD.expected_outputs(self.root)

    def test_missing_companion_is_rejected(self):
        path = self.root / "skills/scuter/SKILL.md"
        path.write_text(path.read_text() + "[Absent](references/absent.md)\n")
        with self.assertRaises(ValueError):
            BUILD.expected_outputs(self.root)

    def test_unexpected_skill_file_is_rejected(self):
        (self.root / "skills/scuter/unexpected.txt").write_text("Unexpected file.\n")
        with self.assertRaises(ValueError):
            self.run_build()

    def test_symlink_source_is_rejected(self):
        path = self.root / "LICENSE.md"
        path.unlink()
        path.symlink_to(self.root / "VERSION")
        with self.assertRaises(ValueError):
            BUILD.expected_outputs(self.root)

    def test_standalone_contains_all_companion_text(self):
        outputs = BUILD.expected_outputs(self.root)
        md = outputs["dist/scuter-v0.2.0.md"].decode("utf-8")
        for source, member in BUILD.SOURCES.items():
            self.assertIn("## Included file: " + member, md)
            self.assertIn((self.root / source).read_text(), md)


if __name__ == "__main__":
    unittest.main()
