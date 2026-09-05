# SCUTER

**Scientific Collaboration for User-directed, Traceable, Evidence-based Research**

A portable Skill for scientist-directed AI collaboration.

SCUTER provides a collaboration protocol, participant instructions, and templates for using AI assistants while the scientist directs the research. Its practices connect assignments, review, decisions, and handoffs to a durable scientific record and versioned artifacts.

## Start here

Read the [implementation guide](docs/implementation-guide.md) for setup and a complete work cycle. Adopt and adapt the [current protocol](protocol/01.work-contract.md) for your project. The [provenance and interpretation notes](docs/provenance-and-interpretation.md) distinguish historical observations from later protocol refinements.

The existing development package and its complete source are available here:

- [Download the v0.1.0 Skill package](skills/user-mediated-collaboration-v0.1.0.skill?raw=true).
- [Inspect the Skill entry point and companion files](skills/user-mediated-collaboration/).

**Version note:** this repository initially preserves the existing `user-mediated-collaboration` v0.1.0 package byte-for-byte, including its original filename and embedded protocol snapshot `47ad152`. The current protocol includes later revisions. Moving these materials here does not make that older package equivalent to the current protocol. Reconciliation, regeneration under the SCUTER package name, and platform testing remain development work. Do not load only `SKILL.md` without its referenced companion files.

## What is here

| Location | Purpose |
| --- | --- |
| `protocol/01.work-contract.md` | Maintained protocol source, including directives, provisions, worked examples, and reusable templates |
| `docs/implementation-guide.md` | Setup, assignments, review, acceptance, handoffs, and troubleshooting |
| `docs/provenance-and-interpretation.md` | Scope and interpretation of the supporting experience |
| `skills/` | Existing development Skill source, manifest, and matching installable archive |
| `provenance/` | Exact source commit, original-to-new path mapping, content hashes, and import verification |
| `tools/import_from_paper.py` | Reproducible, allowlisted snapshot-import and verification utility |

The instructions do not create service connections or confer permissions. Installation and behavior depend on the host application and project setup. No additional platform compatibility is claimed by this repository migration.

## Relationship to the paper

SCUTER was developed in [Beyond the Chat Window](https://github.com/TaylorResearchLab/beyond-the-chat-window). That repository holds the manuscript, its study record, and a version-pinned supplementary snapshot. This repository is the maintenance home for the reusable protocol and Skill materials. The initial import comes from paper commit `32be4c53532074e7a1be46f7706fc7e0c5701657`.

See [MIGRATION.md](MIGRATION.md) for the source-of-record boundary and exact migration scope. The initial import preserves source wording and section numbering, including references to the paper supplement. Subsequent changes should be made here and recorded as revisions, not independently edited into both repositories.

## Development status and attribution

The protocol was developed by Deanne M. Taylor through the work described in the companion paper. These materials are a development snapshot, not a new formal release or evidence of effectiveness across investigators. Review and release decisions remain separate from repository migration.

The original [CC BY 4.0 license](LICENSE.md) and [CC0 notice](LICENSE-CC0.md) are retained from the source repository. Migration preserves the existing notices; it does not relicense imported material.
