# SCUTER

**Scientific Collaboration for User-directed, Traceable, Evidence-based Research**

*A portable Skill for scientist-directed AI collaboration.*

SCUTER helps scientists work with multiple AI assistants while directing the research and maintaining a rigorous scientific record. Its protocol connects questions, assignments, evidence, review, decisions, and handoffs to the files and methods behind the work. It is designed to support reproducibility and FAIR-oriented research practices using tools the scientist already has.

## Get started

1. Read the [implementation guide](docs/implementation-guide.md) and choose a small first task.
2. Supply the [SCUTER Skill package](dist/scuter-v0.2.1-dev.skill?raw=true) to an application that supports Skill installation, or use the [complete Markdown instructions](dist/scuter-v0.2.1-dev.md?raw=true) through its supported instruction or document interface.
3. Establish your Project Overview and Collaboration Log. Identify the participating assistants, project locations, and evidence required to accept a result.
4. Direct a task, obtain a review of the actual work, and record your decision before continuing.

The Markdown edition includes all companion instructions. You do not need to build the files to use them. Installation support, available integrations, and instruction following must be checked in the application you use.

## The scientist directs the work

The User defines and revises the scientific question, selects which assistant acts next, evaluates evidence, connects findings across workstreams, and decides what enters the accepted project record. AI participants implement, review, challenge, and repair within that direction.

The [protocol](protocol/01.work-contract.md) provides five directives: User authority, prior-art lineage, reference validation, collaborative practice, and the durable record. Adopt and adapt it to your project, record those choices, and provide the same adopted version to every participant.

## Materials

| Resource | Purpose |
| --- | --- |
| [Implementation guide](docs/implementation-guide.md) | Setup and the complete task-review-acceptance cycle |
| [Protocol and templates](protocol/01.work-contract.md) | Directives, provisions, worked examples, and project templates |
| [Notion setup](docs/notion-setup.md) | Shared-record structure and verification practices |
| [Record and review guidance](docs/record-and-review.md) | Evidence, review exposure, and session provenance |
| [Skill source](skills/scuter/SKILL.md) | Instructions and bundled companion files |
| [Distributions](dist/) | Skill package, complete Markdown edition, and checksums |

## Development

Current development version: **0.2.1-dev**. Packaging checks verify file integrity and consistency. They do not establish protocol adherence or effectiveness in a particular AI application. Record your actual application, setup, and test results when evaluating SCUTER.

Maintainers can build and verify all distributions offline using Python 3.10 or newer and this repository alone. See [development instructions](DEVELOPMENT.md).

## Companion paper

[*Beyond the Chat Window*](https://github.com/TaylorResearchLab/beyond-the-chat-window) is the companion paper to SCUTER.

## Attribution and licensing

SCUTER is developed by Deanne M. Taylor. See [LICENSE.md](LICENSE.md) and [LICENSE-CC0.md](LICENSE-CC0.md) for the repository's license notices.
