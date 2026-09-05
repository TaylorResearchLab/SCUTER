# Repository separation and provenance

## Origin

The reusable SCUTER artifacts were imported from `TaylorResearchLab/beyond-the-chat-window` at commit `32be4c53532074e7a1be46f7706fc7e0c5701657`, the manuscript work branch's verified state on September 5, 2026. [Source snapshot](https://github.com/TaylorResearchLab/beyond-the-chat-window/tree/32be4c53532074e7a1be46f7706fc7e0c5701657).

The imported files are exactly those listed in `provenance/import-plan.json`. Each entry contains the original path, destination path, and expected Git blob SHA. The import report records SHA-256 values, sizes, runtime identity, and package/source verification. The existing destination README was expanded; no preexisting destination content was removed.

## Scope

The complete five-file Skill source directory and its `.skill` archive retain their original paths and bytes. The current protocol is copied from `supplement/01.work-contract.md` to `protocol/01.work-contract.md`. The implementation guide and interpretation notes move to `docs/`. Both existing license notices are preserved.

The manuscript, paper figure, citation ledger, bibliography, document-build infrastructure, internal project records, and unrelated research material are not imported. The historical Git history remains accessible in the paper repository. This is an attributed snapshot import, not a claim that the original commit history was transferred into this repository.

## One maintained protocol

After verified import and paper-side cutover, `protocol/01.work-contract.md` in SCUTER is the maintenance source for subsequent protocol development. The paper retains the supplementary version it describes. That retained snapshot is not a second independently maintained protocol. Changes to the paper's snapshot must be deliberate, version-pinned updates.

The imported v0.1.0 Skill manifest correctly records its older origin at `47ad152`. Its reference to the paper supplement describes that historical generation source. It does not make the paper repository the ongoing maintenance location after cutover. The gap between that package snapshot and the imported current protocol predates migration and remains explicit.

A new SCUTER-named package must be generated and checked from an adopted protocol revision in a separate change. Do not rename or overwrite the historical v0.1.0 archive and imply that its contents changed. A self-contained Markdown edition and additional platform tests are not part of this byte-preserving import.

## Verification

The import utility downloads only allowlisted public raw-file URLs at the complete source commit. It validates every Git blob identity before writing, refuses to overwrite different existing files, validates the Skill manifest's member checksums, and compares every archive file with the source directory. It does not extract or execute archived code.

At the initial import commit, repeat the checks without network access:

```bash
python3 tools/import_from_paper.py --check
```

This command verifies the original snapshot and is not intended to assert that later intentional protocol revisions remain byte-identical to the import. For initial import reproduction in a clean checkout containing only the bootstrap files, run the same command without `--check`. The utility never commits or pushes changes itself.

The temporary bootstrap workflow is limited to importing the allowlisted files and pushing one non-forced commit to this repository. It is removed after successful migration. No source-repository deletion happens in that job. The paper-side cutover is a separate reviewed-branch change made after destination verification.

Migration and checksum verification establish artifact identity, not protocol efficacy, platform compatibility, independent review, or readiness for release. No tag, formal release, manuscript merge, or publication is created by this operation.
