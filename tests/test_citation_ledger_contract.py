import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class CitationLedgerContractTests(unittest.TestCase):
    def test_protocol_is_two_level_and_claim_specific(self):
        text = (ROOT / "protocol/01.work-contract.md").read_text()
        self.assertIn("source-centric at the top level and proposition-centric at the evidence level", text)
        self.assertIn("Validation is not a source-wide property", text)
        self.assertIn("claim-evidence mapping table", text)
        self.assertIn("Validated support", text)

    def test_notion_schema_has_source_and_mapping_levels(self):
        text = (ROOT / "docs/notion-setup.md").read_text()
        self.assertIn("Do not use a source-level `Validated` field", text)
        self.assertIn("Complete primary text", text)
        self.assertIn("Exact project/manuscript proposition", text)
        self.assertIn("Evidence location", text)
        self.assertIn("Scope/caveat", text)
        self.assertIn("User acceptance", text)

    def test_skill_prevents_source_wide_validation(self):
        text = (ROOT / "skills/scuter/SKILL.md").read_text()
        self.assertIn("one source record per primary work", text)
        self.assertIn("Source-level access or support for one proposition never validates other claims", text)

if __name__ == "__main__":
    unittest.main()
