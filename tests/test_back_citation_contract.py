import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class BackCitationContractTests(unittest.TestCase):
    def test_protocol_requires_back_citation_exploration(self):
        text = (ROOT / "protocol/01.work-contract.md").read_text()
        self.assertIn("back-citation exploration", text)
        self.assertIn("citation inheritance", text)
        self.assertIn("discovery path, not evidence", text)
        self.assertIn("material citation paths", text)

    def test_skill_preserves_primary_text_boundary(self):
        text = (ROOT / "skills/scuter/SKILL.md").read_text()
        self.assertIn("back-citation exploration", text)
        self.assertIn("discovery route", text)
        self.assertIn("validated from its own pinned complete primary text", text)

    def test_guidance_pairs_backward_and_forward_chaining(self):
        impl = (ROOT / "docs/implementation-guide.md").read_text()
        review = (ROOT / "docs/record-and-review.md").read_text()
        self.assertIn("forward citation chaining", impl)
        self.assertIn("recorded citation path", review)
        self.assertIn("Repeated citation", review)

if __name__ == "__main__":
    unittest.main()
