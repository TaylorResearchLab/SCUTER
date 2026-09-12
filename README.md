# SCUTER

**Scientific Collaboration for User-directed, Traceable, Evidence-based Research**

*A portable Skill for scientist-directed AI collaboration.*

SCUTER helps scientists work with multiple AI assistants while directing the research and maintaining a rigorous scientific record. Its protocol connects questions, assignments, evidence, review, decisions, and handoffs to the files and methods behind the work. It is designed to support reproducibility and FAIR-oriented research practices using tools the scientist already has.

## Get started

**New to SCUTER? Start with the [60-second quick start](QUICKSTART.md).**

In the simplest case:

1. **Download the actual `.skill` file to your computer:** [download `scuter-v0.2.2-dev.skill`](https://raw.githubusercontent.com/TaylorResearchLab/SCUTER/951c46b63133dfc67dd5bdf3ac56dd62691fe613/dist/scuter-v0.2.2-dev.skill).
2. **Do not unzip or edit it.** If your AI application accepts `.skill` files as chat attachments, simply upload or drag that exact `.skill` file into the chat. The assistant can then recognize and use the Skill. If the application instead provides a dedicated **Add Skill**, **Install Skill**, **Upload Skill**, or equivalent control, use that interface to upload the same file.
3. Tell the assistant: **"Use SCUTER for this project. I am the User."**
4. Give it your project locations, first bounded task, and acceptance criteria.

If clicking the `.skill` link does not immediately download the file, use your browser's **Save Link As...** command and save it with the filename `scuter-v0.2.2-dev.skill`.

If the application does not support `.skill` files, use the [complete Markdown instructions](https://raw.githubusercontent.com/TaylorResearchLab/SCUTER/951c46b63133dfc67dd5bdf3ac56dd62691fe613/dist/scuter-v0.2.2-dev.md) through its supported project-instructions, persistent-instructions, or instruction-document interface.

For the fuller setup, read the [implementation guide](docs/implementation-guide.md). Establish your Project Overview and Collaboration Log, identify the participating assistants and project locations, and state the evidence required before you will accept a result. Then direct a bounded task, obtain review of the actual work, and record your decision before continuing.

The Markdown edition includes all companion instructions. You do not need to build the files to use them. Installation support, available integrations, and instruction following must be checked in the application you use.

## The scientist directs the work

The User defines and revises the scientific question, selects which assistant acts next, evaluates evidence, connects findings across workstreams, and decides what enters the accepted project record. AI participants implement, review, challenge, and repair within that direction.

The [protocol](protocol/01.work-contract.md) provides five directives: User authority, prior-art lineage, reference validation, collaborative practice, and the durable record. Adopt and adapt it to your project, record those choices, and provide the same adopted version to every participant.

## Materials

| Resource | Purpose |
| --- | --- |
| [Quick start](QUICKSTART.md) | Fastest path from download to a first SCUTER task |
| [Implementation guide](docs/implementation-guide.md) | Setup and the complete task-review-acceptance cycle |
| [Protocol and templates](protocol/01.work-contract.md) | Directives, provisions, worked examples, and project templates |
| [Notion setup](docs/notion-setup.md) | Shared-record structure and verification practices |
| [Record and review guidance](docs/record-and-review.md) | Evidence, review exposure, and session provenance |
| [Skill source](skills/scuter/SKILL.md) | Instructions and bundled companion files |
| [Distributions](dist/) | Skill package, complete Markdown edition, and checksums |

## Development

Current development version: **0.2.2-dev**. Packaging checks verify file integrity and consistency. They do not establish protocol adherence or effectiveness in a particular AI application. Record your actual application, setup, and test results when evaluating SCUTER.

Maintainers can build and verify all distributions offline using Python 3.10 or newer and this repository alone. See [development instructions](DEVELOPMENT.md).

## Companion paper

[*Beyond the Chat Window*](https://github.com/TaylorResearchLab/beyond-the-chat-window) is the companion paper to SCUTER.

## Attribution and licensing

SCUTER is developed by Deanne M. Taylor. See [LICENSE.md](LICENSE.md) and [LICENSE-CC0.md](LICENSE-CC0.md) for the repository's license notices.
