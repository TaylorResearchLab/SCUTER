# S1. Purpose and scope

SCUTER provides a User-directed collaboration protocol for research conducted across AI platforms. The worked examples are synthetic and illustrate the protocol and its reusable record structures.

The protocol defines human authority, evidence requirements, reference validation, prior-art obligations, review and approval, record keeping, file custody, handoffs, privacy, and release. It is intended for adoption at the start of a project or major work phase, and can be adapted for different providers or for multiple named sessions from one provider.

S2 states the directives. S3 states the provisions that implement them. S4 applies both to a synthetic project. S5 through S8 provide worked examples of the required artifacts.

## Data type and disposition

Whether a project will involve private or protected data, and whether a protected environment is required, is established by the User at setup, before the shared record is created. Where protected data is involved: protected data does not leave its environment; any shared-record tool in the data path, including Notion or any other notebooking application, must itself qualify as a protected environment; and this workflow has not been designed or validated to satisfy protected-data requirements, so a User adopting it for such a project does so at the User's own risk. Content supplied to commercial AI platforms leaves the User's institutional environment and is subject to provider handling, retention, and terms that the User does not control. Responsibility for compliant handling remains with the User. The provisions below reflect this constraint rather than establishing it.

## Status of this example

The directives recorded here are not rules in any binding sense. Many were developed over time in response to needs that recurred across different projects. These directives are provided so that other users can start from concrete examples rather than re-learning the same limitations.

Adopters should expect to modify them. Some directives will not fit a given project. Others that a project requires will be absent here, because we did not encounter the need that would have prompted them.

The order and structure of these protocols have not been compared against any other alternative and is not presented as best practice. The order of the directives was itself a design decision. The User is first established as the accountable authority, together with the expectations placed on the collaboration. The requirement to establish prior-art lineage and attribution over project content follows, then requirements for validating external references, then collaborative practice, and finally the maintenance of the durable record.

## Revision and scope of application

The protocol records how the User has organized the work. The User maintains it and may revise it at any time. Its function is to make changes and departures visible against a stated baseline. Revision is expected; unrecorded revision is a departure from the protocol.

Provider terms are separate from this protocol and unaffected by it. Provider terms govern all use, and prevail where the two differ. Responsibility for compliant use remains with the User.

# S2. Protocol directives

## S2.0 Precedence and directive classes

Directives are ordered by precedence. Where two conflict, the earlier directive prevails. `USER-AUTHORITY` prevails over all others.

Each directive carries a stable semantic identifier in addition to a display number. References elsewhere use the identifier, so that reordering does not alter the meaning of a citation.

Directives are of two classes.

**Release requirements** are satisfied before merge and release. `PRIOR-ART-LINEAGE` and `REFERENCE-VALIDATION` are release requirements. An AI participant may not set one aside, may not certify its own satisfaction of one, and records an unmet requirement as blocking. An unmet requirement is reported to the User, who may proceed without it. Proceeding does not satisfy the requirement: it remains recorded as unmet, and a release made without it is outside the validated pathway and is described as such in any account of how the work was produced. The decision to proceed and its stated reason are recorded.

The User's authority under this protocol does not extend to law, institutional policy, funder or journal requirements, collaborator agreements, provider terms, or factual accuracy.

**Standing requirements** apply continuously and are not discharged.

## S2.1 User authority  `USER-AUTHORITY`

*Display number: DIRECTIVE ONE. Standing requirement. Prevails over all others.*

1. The User defines the research question, scope, methods, project direction, privacy boundary, final computing environment, acceptance criteria, and release decision.
2. The User is the author of the work and accepts responsibility for released scientific content and artifacts. AI participants are assistants and are not authors. An implementation with more than one actively participating human investigator may designate User(s) and define which humans share authority and responsibility; collaborators outside the operating workflow are not thereby designated Users.
3. Final judgment rests with the User. No AI participant overrides a User decision.
4. AI participants may propose, implement, test, review, challenge, and repair. No AI participant accepts its own result into accepted state.
5. The User selects which participant acts next and determines whether a contribution is accepted, rejected, returned for revision, parked, or superseded.
6. A routing instruction from the User directs attention and does not transfer project management.
7. The User may stop, redirect, narrow, or end a workstream without agreement from any AI participant.
8. The User is responsible for determining and satisfying any required AI-use disclosures.
9. Material concerns regarding conflicts with scholarly or scientific standards are reported to the User immediately.

## S2.2 Prior-art lineage  `PRIOR-ART-LINEAGE`

*Display number: DIRECTIVE TWO. Release requirement.*

Claims in this project are supported by citation to the published record. Prior work is assumed to exist.

Citation credits the researchers whose work is used, places the claim within the scientific record, and states which prior results the work uses for support, so that a reader can establish the inherited background and assumptions. Three classes of statement are distinguished. **Assertions of fact** are statements presented as established, including definitions, standard results, derivations, parameter values, and methods. **Claims of novelty** are statements that a contribution is original. **Underlying assumptions** are premises on which conclusions depend, included because they are not stated as claims and would otherwise escape a search directed at novelty.

The classes for which recorded searches are required are a coverage declaration the User makes at adoption and records in the project record. The declaration reflects the state of the field and the risk the project carries: a project in a young or fast-moving field may require the widest coverage, while a project resting on well-established background may confine searches to its original contributions. Example coverage levels: **FULL** requires recorded searches for all three classes, with results that are standard, widely known, or presented in textbooks not exempt. **CLAIMS** requires recorded searches for claims of novelty and for the underlying assumptions on which principal results depend, the same set enumerated under `PRACTICE` item 9; other statements are supported by validated citation under `REFERENCE-VALIDATION` without a search record. **CITATION** requires no recorded searches, with all sources governed by `REFERENCE-VALIDATION` alone; because an absence of prior art is supported only by searches actually conducted, a claim of novelty released under this level is released outside the validated pathway and is described as such in any account of how the work was produced. The User may revise the declaration, and the revision is recorded.

For this directive, the unit of work is the proposition; the output is a search record. The search record is an internal project resource and is not prepared for external review. It distinguishes a search that returned nothing from a search that was not conducted, establishes the date on which an absence was determined, and prevents repetition of searches already found unproductive. Maintaining it is a substantial ongoing effort.

1. Each statement requiring support is reduced to its constituent propositions. Searches address one proposition at a time rather than a general topic, so that the proposition each search addressed is identifiable.
2. Prior art exploration typically utilizes Google Scholar, PubMed, arXiv, bioRxiv and other scholarly resources related to a topic. Useful strategies include keyword and synonym searches, backward citation tracking, and forward citation chaining.
3. Abstracts are used to screen results for relevance to the proposition.
4. Search terms, databases, dates, and results are entered in the search record and attributed to the participant who conducted the search.
5. A search returning no relevant results is repeated with alternative terms before absence is recorded. No claim of novelty rests on a single unsuccessful search.
6. **Searches returning nothing relevant are retained with the same detail as searches that return candidates**: date, databases queried, the exact terms used, and the strategy followed. An absence of prior art is supported only by the searches actually conducted, and only as of the dates on which they were conducted. A null result obtained well before submission is repeated before the claim it supports is released.
7. The participant that introduced a statement does not conduct the search establishing its lineage. Searches are conducted by a different participant.
8. Each candidate is recorded as retained, screened out with a reason, or inaccessible. A second participant reviews the search record.
9. The statement is then narrowed, defended, or withdrawn in light of what the search returned.
10. Candidates retained are passed to `REFERENCE-VALIDATION` for admission as references.
11. A statement within the declared coverage released without a recorded search blocks merge and release.

## S2.3 Reference validation  `REFERENCE-VALIDATION`

*Display number: DIRECTIVE THREE. Release requirement.*

For this directive, the unit of work is the reference; the output is a citation ledger entry.

Supporting references are admitted with the following protocol:

1. A participant proposes the resource by creating an entry in the citation ledger, marked `Provisional`.
2. The proposing participant opens a primary publication or authoritative source record and confirms that the resource exists, recording title, authors or responsible organization, publication year or release date, persistent identifier or stable URL, date accessed, and relevant source location.
3. The participant indicates whether the cited source's content can sufficiently support the specific assertion or claim. Bibliographic identity is not sufficient.
4. A second-participant check covers both bibliographic identity and claim-source correspondence. Disagreements, corrections, and uncertainties are recorded. This check is designated independent only where exposure was prospectively controlled and recorded; otherwise it is recorded as a second check following exposure.
5. Each reviewer records approval, clarification or objection to a source citation. The User determines whether the source citation is accepted into the project record.
6. An unresolved, broken, mismatched, inaccessible, or unvalidated reference blocks merge and release.

### Citation requirements

The following rules determine when a scientific statement requires an external citation. Describing a statement as "common knowledge," "standard," "well known," or similar does not by itself exempt it from citation.

1. **Current-project hypothesis, assumption, derivation, or result.** An external citation is not required when the statement genuinely originates in the current project. It is clearly identified as a hypothesis, assumption, derivation, observation, or result of the present work and linked to the relevant project evidence or derivation. Any external premise on which it depends remains subject to citation.
2. **Pure mathematical identity or explicit definition.** A citation is generally not required for an identity derived directly from mathematics or for a definition introduced explicitly by the present work. A named theorem, established method, conventional definition, or result with an identifiable scholarly origin is cited when that origin is relevant.
3. **Claim derived from outside work.** Any empirical, theoretical, methodological, mechanistic, or interpretive claim originating outside the current project is cited to an appropriate source.
4. **Standard scientific fact.** A scientific statement is not exempt from citation merely because it is described as standard or commonly known. If there is any plausible alternate convention, scope, interpretation, population, experimental context, or domain of validity, an appropriate source is cited.
5. **Quantitative statement.** A numerical value, range, rate, threshold, effect size, prevalence, parameter, or other quantitative scientific statement is cited unless it is directly calculated, measured, or derived in the current work. Internally derived quantities are linked to the corresponding method, data, calculation, or result.
6. **Novelty or priority statement.** A claim that a method, result, observation, interpretation, or resource is novel, first, unique, or previously unreported requires citation to the closest relevant prior work and the applicable recorded search under `PRIOR-ART-LINEAGE`. Citations alone do not establish absence of prior art. Cite only what is needed to support the specific comparison or priority statement rather than expanding the text into an unnecessary literature survey.

When uncertain whether an external scientific statement requires citation, the default is to cite and validate the source rather than invoke common knowledge.

## S2.4 Collaborative practice  `PRACTICE`

*Display number: DIRECTIVE FOUR. Standing requirement.*

These practices state the User's expectations for participation in the project. They do not override provider terms, platform safety rules, or technical constraints. Where a requested practice cannot be followed, the limitation is stated to the User.

AI participants are requested to:

1. address the User and other participants constructively, without withholding a material concern;
2. acknowledge contributions while preserving substantive disagreement, treating a position as a provisional claim rather than as property of the participant holding it, and a change of position following review as a revision;
3. check any statement that can be checked directly against the artifact it concerns, including files, records, commits, outputs, and sources, before stating it, and where a statement cannot be checked, distinguish what was verified from what was not;
4. state errors directly, identify their consequences, and propose repairs;
5. direct criticism to the artifact, evidence, assumption, or method;
6. treat any description of what a method, dataset, or artifact does as a claim requiring verification against the artifact itself, including descriptions already established in the project record. Persistence of a description across sessions is not evidence of its accuracy, and a shared record propagates an inaccurate description with the same fidelity as an accurate one;
7. re-verify a description at the point where a claim of novelty or a principal result comes to depend on it;
8. record instances in which a participant confirms an error immediately upon its being raised, since these indicate a description that was inherited rather than checked and a verification that was available and not performed;
9. on request, and at the point where a result becomes a principal claim or a workstream resumes after a pause, state the premises the current line of work depends on, identify for each whether it has been verified against an artifact or inherited from the project record, and name for each what observation would show it to be wrong;
10. treat every new scientific mechanism, causal explanation, relationship, interpretation, boundary, membership, or analogous proposition as `HYPOTHESIS ONLY: not source-supported` unless and until the User promotes that exact proposition under the evidence-support rule below;
11. allow hypothesis-only material to guide searches, analyses, model building, or experimental planning, but exclude it from claim titles, signed or accepted edges, mechanism membership, evidence counts, boundary definitions, and analogous evidence-bearing project structures;
12. use `EVIDENCE SUPPORTED: [specific proposition]` only for the exact proposition for which evidence has been identified and verified. The record states the supporting source or artifact, what the evidence supports, what it does not support, and any material limitations. External-source evidence follows `REFERENCE-VALIDATION`; project-generated evidence is tied to the exact accepted artifact or run;
13. promote a proposition from hypothesis-only to evidence-supported only when the User determines that the evidence meets the project-specific evidentiary threshold for that exact proposition. AI participants may identify evidence and recommend promotion but may not promote a claim themselves;
14. never treat partial support as support for a broader claim. If evidence supports only a sub-proposition, only that sub-proposition may receive `EVIDENCE SUPPORTED`; the broader statement remains `HYPOTHESIS ONLY: not source-supported`. Preserve the hypothesis history and record the User's promotion decision.

## S2.5 Durable record  `DURABLE-RECORD`

*Display number: DIRECTIVE FIVE. Standing requirement.*

A project maintains the following artifacts. Each is established before work begins, and its location is recorded so that any participant can reach it without asking.

| Artifact | Contents | Location in this example |
| --- | --- | --- |
| Collaboration Log | Material actions: decisions, reviews, run results, corrections, supersessions, handoffs, next actions | Notion database |
| Project Overview | Background of the research and what governs it: the accepted scientific question, current assumptions, accepted commit, authoritative configuration, current outputs, unresolved limitations, and prior art | Notion page |
| Numbered notebooks | Extended records of methods, analyses, derivations, figures, and project-specific reasoning that do not fit one log entry | Notion pages |
| Search record | Propositions searched, terms, databases, dates, candidate dispositions, and searches that returned nothing | Notion database, or a delimited file in the code repository |
| Citation ledger | One canonical identifier per work, the statement each reference supports, validation status, who checked and when, and dispositions of candidates not retained | Structured database or a delimited file in the manuscript repository |
| Code repository | Code, tests, configuration, environment specification | GitHub |
| Manuscript repository | Manuscript source, figures, build configuration, build outputs | GitHub, with a GitHub Actions-driven automated build |
| Protected environment | Private data and authoritative execution | Institutional computing environment under User control |
| Artifact store | Large outputs and release archives | Zenodo, OSF, institutional storage, or a repository release |

The code and manuscript repositories may be the same repository or separate, provided the manuscript build does not depend on unversioned inputs.

The citation ledger is a project record and is not a bibliography. Build systems that resolve persistent identifiers retrieve bibliographic metadata automatically, so the ledger does not store what such a system supplies. It stores what no build system can know: which statement each reference supports, whether the source was checked against that statement, by whom, on what date, and which candidates were considered and not retained. Identifiers embedded in manuscript source are pointers to works; they are not a record of validation.

Three properties follow.

1. **One canonical identifier per work.** Where a build system treats identifiers of different types as distinct references, citing the same work through more than one produces duplicate entries. The ledger fixes a single identifier per work, and the manuscript uses that one.
2. **No duplicated metadata.** Titles, authors, and journals are not stored in the ledger where the build retrieves them, since a second copy diverges from the first.
3. **A path for works without identifiers.** Websites, personal communications, unindexed reports, and similar sources cannot be resolved automatically and require metadata supplied by hand in whatever format the build accepts. The ledger records these as such, so that the set requiring manual metadata is known rather than discovered at build time.

For this directive, the unit of work is the material action; the output is a record in the Collaboration Log. Material actions comprise decisions, reviews, run results, corrections, supersessions, file links, next actions, concerns stated under `USER-AUTHORITY`, and a User decision to proceed without a satisfied release requirement.

1. A material action is recorded at the time it occurs. A result held only in one participant's conversation is not a project artifact, and description of an artifact does not transfer it.
2. A record that reports a result identifies the command, inputs, outputs, configuration, and environment sufficient to reproduce or check it.
3. Every write to the shared record or repository is read back before the action is treated as complete. Location and structured properties are checked separately, since a success response is provisional until the object itself has been inspected.
4. Record a stable, project-specific chat identifier at session registration and reuse it in Agent instance ID for that session's entries. Preserve an entry's originating identifier on later edits, and identify the editing instance and date/time in the edited or appended content. Record provider and displayed model/version separately when available; do not infer them from a chat name or fill unknown historical identities by guesswork.
5. Exposure status is recorded at the time of the action, stating whether the acting session had access to a named prior contribution. This is not recoverable afterward.
6. A record made obsolete by later work is marked superseded rather than deleted where its history remains relevant.
7. Before a paused workstream resumes, or a task begins that depends on another, the User identifies the Project Overview page and the specific upstream records, files, or outputs to be reviewed. Availability of context does not ensure its use, and participants do not reread the entire project before each local task unless the task is project-wide. Inspect relevant entries edited since the last inspection as well as newly created entries. Created time records entry creation; Last edited time signals the latest edit, not a complete revision history or a new acceptance decision.
8. Record directly relevant earlier-entry URLs in Reference posts, one per line. Include multiple references when combining threads. Verify the saved destinations after writing. When context is needed, follow the references backward as far as the task requires, avoiding repeated visits by page identity and reporting inaccessible posts. The entry text explains connections where needed. A reference is not an approval or a version pin; an empty historical field does not establish an absence of prior work.

The record may preserve **process provenance**, such as which session supplied or drafted a proposal. Process provenance explains the workflow and supports audit. It does not confer authorship, intellectual ownership, or accountability on an AI participant, and no field assigns intellectual origin to one. AI outputs are derivative proposals: the User evaluates, revises, rejects, or adopts them, and an adopted proposal is the User's work and responsibility. See `USER-AUTHORITY`.

The public template uses the following core field order:

1. Entry
2. Created time
3. Last edited time
4. Date
5. Agent instance ID
6. Owner
7. Assignment to
8. Needs Agent A Review
9. Needs Agent B Review
10. Needs User Review
11. Approved by Agent A
12. Approved by Agent B
13. Approved by User
14. Status
15. Source
16. Next Action
17. Summary
18. Topic
19. Type
20. Reference posts
21. Reference links
22. Repository
23. Commit SHA
24. Purpose
25. Subproject

Agent A and Agent B identify the participants whose review and endorsement fields are being used; the User records the chosen field-name mapping. Their lead and reviewer roles are assigned per task. The example implementation named these fields for GPT and Claude. Agent instance ID identifies a particular chat, not its current task role.

Additional fields may record lock state, review response, branch or pull request, commit date, displayed provider/model identity, and exposure status. Detailed methods, results, and dated reviews belong in the entry body and linked artifacts rather than only in summary properties.

# S3. Protocol provisions

## S3.1 AI participant roles are complementary and reversible

1. AI participant roles are assigned by task and may reverse between work units.
2. No platform is presumed to be globally superior.
3. Agent A may lead implementation while Agent B reviews. The roles may reverse for the next task.
4. A reviewer examines the artifact, assumptions, evidence, or execution path. Editing the lead participant's prose without checking the underlying work is not a review.
5. Agreement after exposure to another participant's output is recorded as sequential agreement, not independent confirmation.
6. When evidence is incomplete or the decision concerns scope, priority, privacy, or risk, the User decides.

## S3.2 Review routing, approval, and deliberation

Review requests and approvals are distinct.

1. `Needs ... Review` fields are temporary routing signals. They mean that the named participant has not yet completed the requested review.
2. The reviewer records the review, updates status and next action, and clears only its own review field.
3. `Approved by ...` fields record endorsement of the current version of the record.
4. A reviewer may clear a review request without approving the work when objections or required changes have been recorded.
5. A material revision invalidates prior approvals. The approvals are cleared and review is requested again when necessary.
6. Participants set only their own approval fields.
7. Agent approvals are recorded positions, not votes. They do not combine into acceptance. The User alone determines whether work enters accepted state.
8. Review text and dated entries constitute the historical evidence. Checkbox fields indicate current routing or current endorsement and do not record the sequence of prior events.

The Topic `Deliberation` is applied where a question is not suited to a proposal-and-review sequence, because the first framing would constrain the response. Participants contribute options, constraints, or interpretations without adopting a preferred answer, and the User determines the next step or decision rule.

## S3.3 Evidence classes and claim state

The protocol distinguishes hypotheses, evidence-supported propositions, file identity, execution evidence, and User acceptance.

1. Model prose is a proposal or interpretation. A newly proposed scientific proposition defaults to `HYPOTHESIS ONLY: not source-supported`.
2. `HYPOTHESIS ONLY: not source-supported` material may be retained and used to guide exploration, but it does not enter evidence-bearing project state. It is excluded from claim titles, signed or accepted edges, mechanism membership, evidence counts, boundary definitions, and analogous evidence-bearing structures.
3. `EVIDENCE SUPPORTED: [specific proposition]` is claim-specific. Its record identifies the exact proposition, supporting source or artifact, what the evidence supports, what it does not support, and material limitations. A generic statement that a broader mechanism or interpretation is "supported" is insufficient.
4. Partial support does not promote a broader claim. If evidence supports only one component, that component may be proposed for promotion while the parent mechanism or statement remains `HYPOTHESIS ONLY: not source-supported`.
5. External-source evidence is admissible only after the applicable `REFERENCE-VALIDATION`; project-generated evidence is tied to the exact run, artifact, inputs, configuration, and accepted execution record.
6. The User defines the evidentiary threshold for each proposition and is the only participant who can promote it from hypothesis-only to evidence-supported project state. AI participants may recommend promotion but do not perform it themselves.
7. A sandbox run is evidence only for the recorded sandbox, code, and inputs.
8. A commit identifies a version of a file but does not establish scientific validity.
9. A User-run result is authoritative only for its recorded code, command, inputs, configuration, and environment.
10. Evidence support is bounded by the proposition and evidence recorded. It does not establish unsupported causal, mechanistic, boundary, membership, or generalization claims. A proposition may be returned to hypothesis-only or superseded when later evidence changes its status.
11. A novelty claim is released only after the applicable `PRIOR-ART-LINEAGE`.
12. The User decides whether the combined evidence satisfies the acceptance criteria and whether any proposition is promoted.

## S3.4 File custody and reproducibility

1. Code, exact commands or queries, primary inputs, configuration, and results are stored together or linked from one record.
2. A result stored without the means to reproduce or check it does not satisfy this provision.
3. Checksums are computed only after the file is complete.
4. A checksum is not embedded inside the file it claims to verify.
5. Manual transcription, environment-specific steps, and non-reproducible links are stated explicitly.
6. Parent location and structured properties are checked separately after every database create or move.
7. Agent-initiated repository actions performed through a User-authenticated integration are recorded in the log because repository metadata may not distinguish them from manual User actions.

## S3.5 Access and protected execution

This section states properties the arrangement maintains. Availability and permissibility of any integration are determined by the provider and platform.

1. Credentials remain under User or institutional control and are not placed in prompts, notebooks, commits, or log fields.
2. Where an integration is used, it is scoped to the minimum required for the task, and read-only access is preferred for review work.
3. The default branch is protected. The User controls merge and release.
4. AI participants do not have access to private data or the final computing environment.
5. Any action taken through an integration authenticated as the User is recorded in the log, because platform metadata may not distinguish it from an action the User performed directly.

## S3.6 Disagreement and correction

1. Criticism is directed to the artifact, assumption, evidence, or method.
2. Acknowledgement of a contribution is not evidence of its correctness.
3. Errors are admitted directly, their consequences are recorded, and a repair is proposed.
4. The record distinguishes resolution by new evidence, independent recalculation, a frozen artifact, User-supplied domain context, or a User decision.
5. When evidence does not determine the outcome, the User decides scope, priority, terminology, privacy, and risk tolerance.
6. The record states what resolved the disagreement.

## S3.7 Handoff requirement

A handoff is required after a substantial work unit, before transferring the lead role, before a high-impact execution, when a session is becoming crowded, or when the User requests a new session.

The handoff identifies:

1. the current accepted state;
2. work completed since the prior handoff;
3. current notebooks, files, branches, commits, and configurations;
4. exact execution evidence and failed runs;
5. open questions;
6. rejected or superseded work;
7. known uncertainty and limitations;
8. one explicit next action, owner, and acceptance condition.

The receiving participant compares the handoff with the Collaboration Log and repository before continuing.

## S3.8 Privacy, collaborator disclosure, and release

1. Access to a workspace is not permission to publish its contents.
2. Private scientific, technical, clinical, collaborator, and creative material remains within the project boundary.
3. Public summaries are deliberately extracted and reviewed by the User.
4. Project domains, unpublished findings, identifiable collaborators, and private record contents are omitted unless explicit permission has been obtained.
5. Collaborators on the work are informed that it uses User-mediated AI collaboration.
6. Release requires a clean build, validated citations and public links, satisfied prior-art searches, accepted checksums, final User review, and an explicit release decision.

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
| `PRIOR-ART-LINEAGE` coverage declaration | CLAIMS: recorded searches for claims of novelty and the underlying assumptions carrying principal results |

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

> Work under the project collaboration protocol. Apply the reference-validation directive: only cite validated articles. A resolved identifier, derivative citation, or generated reference is not validation. Record the primary validation source and date, and obtain a second participant's check before merge. Apply the prior-art lineage directive under this project's declared coverage, CLAIMS: before asserting that a contribution is novel, or relying on an assumption that carries a principal result, search the literature and record what you searched and found; other statements are supported by validated citation without a search record. Do not certify the originality of your own contribution. The User retains authority and responsibility for the scientific questions, methods, scope, privacy, final execution, acceptance, merge, and release. Use the Collaboration Log as the durable record and the repository as the versioned file store. Before starting, read the Project Overview page and the specific upstream records or artifacts identified for this task; do not assume that available context has already been incorporated. Agent A will implement the first pipeline version. Agent B will review the code, tests, configuration, and quality-control plan rather than merely edit the prose. Ask for clarification when material ambiguity is detected. Record every material decision, run, correction, citation validation, prior-art search, file location, and next action. Store code, commands, inputs, configuration, and outputs together. Verify every Notion and repository write by reading it back. After completing a review, record the result, update status and next action, clear your own review field, and set your approval only when you endorse the current version. Create a structured handoff before transferring the lead role.
# S6. Example Collaboration Log record

| Field | Example value |
| --- | --- |
| Entry | Initial pipeline implementation completed in sandbox |
| Created time | Automatically recorded at entry creation |
| Last edited time | Automatically maintained by the notebook service |
| Agent instance ID | `Project-X-A-01` (synthetic registered session label) |
| Reference posts | `[FULL URL OF THE ASSIGNMENT ENTRY]` (placeholder, not a retrievable link) |
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
| `PRIOR-ART-LINEAGE` coverage declaration | `[FULL / CLAIMS / CITATION / CUSTOM]` |
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
| Instance registration | `[STABLE CHAT ID AND REGISTRATION ENTRY]` |
| Reference posts | `[DIRECT EARLIER-ENTRY URLS, ONE PER LINE; MULTIPLE WHEN NEEDED]` |
| Last edited time | `[NATIVE LAST-EDIT FIELD; INSPECT RELEVANT RECENT EDITS]` |
| Write read-back | `[HOW VERIFIED]` |
| Handoff trigger | `[WHEN]` |
| Context reorientation | `[CURRENT STATE AND TASK-RELEVANT UPSTREAM DEPENDENCIES]` |
| Protected data and protected environment | `[NONE, or REQUIRED: ENVIRONMENT AND QUALIFYING SHARED-RECORD TOOLS]` |
| Privacy boundary | `[WHAT MUST NOT BE DISCLOSED]` |
| External-collaborator disclosure | `[WHO MUST BE INFORMED]` |
| AI-use disclosure | `[WHAT THE VENUE REQUIRES, WHERE STATED]` |
| Release requirements | `[BUILD, CITATIONS, LINKS, PRIOR-ART SEARCHES, ASSUMPTION LINEAGE, CHECKSUMS, USER APPROVAL]` |

The template should be shortened or expanded according to project risk, duration, and regulatory requirements. It does not replace institutional security, data-governance, authorship, or responsible-conduct policies.

