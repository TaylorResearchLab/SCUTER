# Worked example and reusable templates (verbatim)

Source: same file and commit as references/protocol.md, sections S4–S8. S5 is the initial assignment text a User can issue to any AI participant. S6 is the canonical Collaboration Log record shape. S7 is the structured handoff. S8 is the compact per-project adaptation template.

# S4. Completed synthetic example

The directives in S2 and the provisions in S3 are general. This section applies them to one synthetic project.

## S4.1 Project definition

| Field | Synthetic example |
| --- | --- |
| Project | Reproducible reanalysis of a public benchmark dataset |
| Scientific objective | Implement and validate a versioned analysis pipeline and produce an auditable methods summary |
| User | Scientific leader, project manager, operator of the final computing environment, adjudicator, and release authority |
| Agent A | Initial implementation and test lead |
| Agent B | Reciprocal reviewer, second-participant checker, and repair lead when assigned |
| Shared record | Project Overview page, structured Collaboration Log, and numbered notebooks |
| Versioned file store | Repository with a protected default branch and pull-request review |
| Final computing environment | User-controlled environment |
| Public-release boundary | Code, configuration, synthetic examples, and manuscript text approved by the User |

## S4.2 Required deliverables

The synthetic project requires:

- versioned source code and tests;
- an environment specification;
- an explicit run configuration;
- an identifier crosswalk when required;
- quality-control outputs;
- a machine-readable results table;
- a concise methods and limitations summary;
- a citation-validation and prior-art ledger;
- a final handoff identifying the accepted commit and final run.

## S4.3 Acceptance criteria

For the synthetic project, a result is accepted only when:

- code and configuration are committed;
- automated tests pass;
- the User completes the final run;
- quality-control outputs are recorded;
- the reciprocal reviewer inspects the files and evidence;
- **the User reviews the code and validation, and the configuration that produced the result, and evaluates the result versus the project goals and the scientific question**;
- material objections are resolved or retained explicitly as limitations;
- citations are validated under `REFERENCE-VALIDATION`;
- claims and the underlying assumptions on which they depend are checked under `PRIOR-ART-LINEAGE`;
- the User marks the result accepted.

# S5. Example initial assignment

> Work under the project collaboration protocol. Apply the reference-validation directive: only cite validated articles. A resolved identifier, derivative citation, or generated reference is not validation. Record the primary validation source and date, and obtain a second participant's check before merge. Apply the prior-art lineage directive: before asserting that a contribution is novel, or relying on an assumption that carries a finding, search the literature and record what you searched and found. Do not certify the originality of your own contribution. The User retains authority and responsibility for the scientific questions, methods, scope, privacy, final execution, acceptance, merge, and release. Use the Collaboration Log as the durable record and the repository as the versioned file store. Before starting, read the Project Overview page and the specific upstream records or artifacts identified for this task; do not assume that available context has already been incorporated. Agent A will implement the first pipeline version. Agent B will review the code, tests, configuration, and quality-control plan rather than merely edit the prose. Ask for clarification when material ambiguity is detected. Record every material decision, run, correction, citation validation, prior-art search, file location, and next action. Store code, commands, inputs, configuration, and outputs together. Verify every Notion and repository write by reading it back. After completing a review, record the result, update status and next action, clear your own review field, and set your approval only when you endorse the current version. Create a structured handoff before transferring the lead role.
# S6. Example Collaboration Log record

| Field | Example value |
| --- | --- |
| Entry | Initial pipeline implementation completed in sandbox |
| Source | Agent A; Code/Run |
| Owner | Agent A |
| Type | Implementation |
| Topic | Analysis |
| Status | Needs Review |
| Assignment to | Agent B; User |
| Needs Agent B Review | Yes |
| Needs User Review | Yes |
| Approved by Agent A | Yes |
| Approved by Agent B | No |
| Approved by User | No |
| Purpose | Produce a testable first implementation of the agreed analysis specification |
| Summary | Pipeline executes on synthetic input; final data have not been run |
| Repository | `organization/project-x` |
| Branch / PR | `agent/initial-pipeline`, PR 4 |
| Commit SHA | `0123456789abcdef...` |
| Command | `python -m project_x.run --config config/example.yaml` |
| Inputs | Synthetic fixture `tests/data/example.tsv` |
| Outputs | `artifacts/example_run/` |
| Evidence | Sandbox evidence only |
| Citations | No new citations |
| Read-back | Commit and output path fetched and verified |
| Uncertainty | Performance and identifier coverage have not been tested on final inputs |
| Next action | Agent B reviews the diff, tests, and acceptance criteria; User schedules the final run after review |

# S7. Example structured handoff

## Current accepted state

The analysis specification is accepted. The implementation at commit `0123456` is provisional and has passed synthetic tests only.

## Work completed

- Agent A implemented the pipeline and unit tests.
- Agent B identified two identifier-normalization defects.
- Agent A repaired both defects at commit `89abcde`.
- The User confirmed that all public references in the methods note appear in the citation-validation ledger.
- A second participant checked the recorded validation sources.

## Current files

- Specification: Notebook 03, accepted.
- Repository: `organization/project-x`.
- Branch: `agent/initial-pipeline`.
- Current commit: `89abcde`.
- Configuration: `config/authoritative.yaml`.
- Quality-control plan: `docs/qc-plan.md`.

## Execution evidence

Synthetic tests pass. No final run has been performed. The sandbox environment and exact command are recorded in the latest implementation record. The repository write and artifact path were read back and verified.

## Open questions

- Whether the final dataset contains unmapped identifiers.
- Whether memory use remains within the protected environment allocation.

## Superseded work

Commit `0123456` is superseded because of identifier-normalization defects.

## Known limitations

The current evidence does not establish validity on final inputs.

## Next action

The User runs commit `89abcde` with `config/authoritative.yaml` in the final computing environment. Acceptance requires completion of the run, review of the quality-control outputs, and an accepted run-result record.

# S8. Reusable compact template

| Protocol element | Project-specific value |
| --- | --- |
| Project objective and scientific questions | `[DEFINE]` |
| User authority and responsibility | `[SCOPE, METHODS, PRIVACY, EXECUTION, ACCEPTANCE, RELEASE]` |
| Named agent roles | `[LEAD]`, `[REVIEWER]`, `[OPTIONAL ADDITIONAL SESSIONS]` |
| Participants and platforms | `[PLATFORMS, MODEL VERSIONS, AVAILABLE INTEGRATIONS]` |
| `REFERENCE-VALIDATION` ledger and second check | `[LOCATION AND REVIEWER]` |
| `PRIOR-ART-LINEAGE` searches and searcher | `[DATABASES, TERMS, WHO SEARCHED]` |
| Shared record | `[DATABASE / LOG / NOTEBOOK LOCATION]` |
| Current accepted-state page | `[LOCATION]` |
| Repository | `[REPOSITORY]` |
| Final computing environment | `[USER-CONTROLLED LOCATION]` |
| Required deliverables | `[LIST]` |
| Evidence classes | `[PROPOSAL, SANDBOX, COMMIT, FINAL RUN]` |
| Acceptance criteria | `[LIST]` |
| Review and approval fields | `[ROUTING, ENDORSEMENT, USER ACCEPTANCE]` |
| Deliberation | `[WHEN USED]` |
| Required log fields | `[LIST]` |
| Write read-back | `[HOW VERIFIED]` |
| Handoff trigger | `[WHEN]` |
| Context reorientation | `[CURRENT STATE AND TASK-RELEVANT UPSTREAM DEPENDENCIES]` |
| Privacy boundary | `[WHAT MUST NOT BE DISCLOSED]` |
| External-collaborator disclosure | `[WHO MUST BE INFORMED]` |
| AI-use disclosure | `[WHAT THE VENUE REQUIRES, WHERE STATED]` |
| Release requirements | `[BUILD, CITATIONS, LINKS, PRIOR-ART SEARCHES, ASSUMPTION LINEAGE, CHECKSUMS, USER APPROVAL]` |

The template should be shortened or expanded according to project risk, duration, and regulatory requirements. It does not replace institutional security, data-governance, authorship, or responsible-conduct policies.

