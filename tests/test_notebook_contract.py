"""Document/schema regression checks, not tests of Agent compliance or Notion access."""
import importlib.util
import io
from pathlib import Path
import re
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('notebook_build', ROOT / 'tools/build.py')
BUILD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BUILD)

FIELDS = [
    'Entry', 'Created time', 'Last edited time', 'Date', 'Agent instance ID',
    'Owner', 'Assignment to', 'Needs Agent A Review', 'Needs Agent B Review',
    'Needs User Review', 'Approved by Agent A', 'Approved by Agent B',
    'Approved by User', 'Status', 'Source', 'Next Action', 'Summary', 'Topic',
    'Type', 'Reference posts', 'Reference links', 'Repository', 'Commit SHA',
    'Purpose', 'Subproject',
]


class NotebookContractTests(unittest.TestCase):
    def test_protocol_core_fields(self):
        protocol = (ROOT / 'protocol/01.work-contract.md').read_text(encoding='utf-8')
        block = protocol.split('The public template uses the following core field order:', 1)[1]
        block = block.split('\n\nAgent A and Agent B', 1)[0]
        self.assertEqual(re.findall(r'^\d+\. (.+)$', block, re.M), FIELDS)

    def test_notion_table_matches_core(self):
        text = (ROOT / 'docs/notion-setup.md').read_text(encoding='utf-8')
        block = text.split('| Field | Suggested type | Purpose |', 1)[1].split('\n\n', 1)[0]
        names = []
        for line in block.splitlines():
            if line.startswith('|') and not line.startswith('| ---'):
                names.extend(name.strip() for name in line.split('|')[1].split(';'))
        self.assertEqual(len(names), len(set(names)))
        self.assertEqual(set(names), set(FIELDS))
        self.assertIn('| Reference posts | Text |', text)
        self.assertIn('| Last edited time | Last edited time |', text)

    def test_notebook_terms_reach_all_instruction_editions(self):
        version = (ROOT / 'VERSION').read_text().strip()
        outputs = BUILD.expected_outputs(ROOT)
        with zipfile.ZipFile(io.BytesIO(outputs[f'dist/scuter-v{version}.skill'])) as archive:
            for member in ['SKILL.md', 'references/protocol.md',
                           'references/implementation-guide.md', 'references/notion-setup.md',
                           'references/record-and-review.md']:
                text = archive.read('scuter/' + member).decode('utf-8')
                for field in ['Reference posts', 'Agent instance ID', 'Last edited time']:
                    with self.subTest(member=member, field=field):
                        self.assertIn(field, text)
        md = outputs[f'dist/scuter-v{version}.md'].decode('utf-8')
        self.assertIn('faithful structured-row', md)
        self.assertIn('page ID', md)

    def test_rebuild_is_byte_identical_for_real_sources(self):
        self.assertEqual(BUILD.expected_outputs(ROOT), BUILD.expected_outputs(ROOT))


if __name__ == '__main__':
    unittest.main()
