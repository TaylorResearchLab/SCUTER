#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SOURCE_FILES = [
    "skills/scuter/SKILL.md",
    "protocol/01.work-contract.md",
    "docs/implementation-guide.md",
    "docs/notion-setup.md",
    "docs/record-and-review.md",
]

for rel in SOURCE_FILES:
    path = ROOT / rel
    text = path.read_text()
    text = text.replace("HYPOTHESIS ONLY — not source-supported", "HYPOTHESIS ONLY: not source-supported")
    text = text.replace("EVIDENCE SUPPORTED — [specific proposition]", "EVIDENCE SUPPORTED: [specific proposition]")
    path.write_text(text)

version_path = ROOT / "VERSION"
if version_path.read_text().strip() != "0.2.1-dev":
    raise RuntimeError("Expected VERSION 0.2.1-dev")
version_path.write_text("0.2.2-dev\n")

skill_path = ROOT / "skills/scuter/SKILL.md"
skill = skill_path.read_text()
old = '  version: "0.2.1-dev"'
new = '  version: "0.2.2-dev"'
if skill.count(old) != 1:
    raise RuntimeError("Expected one 0.2.1-dev Skill metadata version")
skill_path.write_text(skill.replace(old, new, 1))

print("Updated source to SCUTER 0.2.2-dev and colon-form evidence-state labels")
