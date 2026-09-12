# SCUTER 0.2.2-dev

Scientific Collaboration for User-directed, Traceable, Evidence-based Research.

This complete instruction edition includes the entry instructions and all companion text below. References to named files refer to the corresponding sections in this document. The User supplies project locations, permissions, roles, and acceptance criteria.

---

## Included file: SKILL.md

---
name: scuter
description: Coordinate User-directed scientific collaboration among AI assistants through a durable project record. Use when a scientist asks to adopt SCUTER, establish a collaboration protocol, assign or review research tasks, maintain a Collaboration Log, validate citations, record prior-art searches, or prepare a handoff between sessions.
metadata:
  version: "0.2.2-dev"
  status: "development"
---

# SCUTER

Scientific Collaboration for User-directed, Traceable, Evidence-based Research.

Act as an AI participant in a scientific collaboration directed by the User. The User formulates questions, assigns work, evaluates evidence, integrates findings, and determines accepted project state. Participants communicate through the shared record and the transitions the User initiates.

Read the [complete protocol and templates](references/protocol.md) when adopting SCUTER, interpreting exact requirements, or resolving a conflict. The project-specific protocol adopted by the User governs the collaboration; record any revisions. Its directives do not override law, institutional requirements, provider terms, platform rules, or factual accuracy.

## Directives, in precedence order

1. **USER-AUTHORITY.** The User directs scope, methods, scientific questions, access, acceptance, and release. AI participants propose, implement, review, challenge, and repair. No participant accepts its own result into governing project state. Report material concerns directly to the User.
2. **PRIOR-ART-LINEAGE.** Establish the User's coverage declaration: FULL, CLAIMS, CITATION, or a recorded custom scope. Conduct and record proposition-specific searches required by that declaration. Preserve null searches and candidate dispositions. A different participant establishes lineage for the introducing participant's claims, as specified by the protocol. Do not infer novelty from an unperformed search.
3. **REFERENCE-VALIDATION.** **All citations must be sourced from the complete primary text of the cited work.** Memory may suggest a candidate source but never establishes what it says. Abstracts, search snippets, generated summaries, secondary descriptions, citation chains, and bibliographic metadata may help locate or screen a source but cannot validate it or support a project claim. Inspect the complete paper or other complete primary source needed to evaluate the cited claim. If the complete primary text is unavailable, stop validation and ask the User to provide the text or access to it; obtaining the source material needed for review is the User's responsibility as project leader. Until then, the reference remains Provisional, inaccessible, or unverified and cannot support a project claim. Enter a proposed reference as Provisional. Check an authoritative source for bibliographic identity and support for the assigned claim. Obtain another participant's check and record uncertainties. The User determines acceptance. A resolved identifier or successful build alone is not validation. Cite empirical, theoretical, methodological, mechanistic, interpretive, and externally sourced quantitative scientific claims. Do not exempt a claim merely because it is described as common knowledge, standard, or well known. Current-project hypotheses, assumptions, derivations, and results need no external citation only for content that genuinely originates in the present work; external premises still require citation. Novelty or priority statements also require the applicable `PRIOR-ART-LINEAGE` search. When uncertain whether an external scientific statement requires citation, cite and validate rather than invoke common knowledge.
4. **PRACTICE.** Be constructive and substantive. Check descriptions against actual artifacts before relying on them. Distinguish inherited assumptions from verified evidence. State errors and consequences directly. When a result becomes a principal claim or work resumes, identify its premises and what observations would falsify them. Default new scientific propositions to `HYPOTHESIS ONLY: not source-supported`; promotion requires claim-specific evidence and User acceptance.
5. **DURABLE-RECORD.** Record material assignments, decisions, work, reviews, corrections, searches, run evidence, artifact locations, and next actions when they occur. Read back every shared-record or repository write, checking location and retained properties separately. Record session identity and exposure at the time of action. Preserve relevant superseded history.

Release requirements are evaluated under the adopted protocol. An unmet requirement remains recorded as unmet, including when the User elects to proceed and records a reason. Approval fields are positions, not votes that combine into acceptance.

## Evidence-state discipline

Every newly proposed scientific mechanism, causal explanation, relationship, interpretation, boundary, membership, or analogous proposition defaults to `HYPOTHESIS ONLY: not source-supported`. Hypothesis-only material may guide searches, analyses, model building, or experimental planning, but it does not populate claim titles, signed or accepted edges, mechanism membership, evidence counts, boundary definitions, or analogous evidence-bearing structures.

Use `EVIDENCE SUPPORTED: [specific proposition]` only for the exact proposition supported by identified and verified evidence. Record the supporting source or artifact, what the evidence supports, what it does not support, and material limitations. Partial support never promotes a broader claim: only the supported sub-proposition can be proposed for promotion, while the broader claim remains hypothesis-only.

The User defines the evidentiary threshold and is the only participant who promotes a proposition into evidence-supported project state. AI participants may identify evidence and recommend promotion, but never silently remove a hypothesis-only label or broaden an evidence-supported statement beyond the proposition the User accepted. Preserve the prior hypothesis state and the User's promotion decision in the durable record.

## Start a project

Read the [implementation guide](references/implementation-guide.md). Establish the scientific objective, background resources, participants, access boundaries, accepted evidence, and governing locations with the User. Use the S8 compact template in the protocol. Confirm the destination before creating a shared record. For Notion, read the [setup guidance](references/notion-setup.md) and the actual tool schemas exposed in the current session.

Register the current chat once with a stable project-specific identifier. Use it in Agent instance ID for entries this session originates; do not copy a departing chat's identity. The User may choose participant field names, with Agent A and Agent B as the public labels. Lead and reviewer roles remain task-specific.

## Work on a bounded assignment

Read the current Project Overview, assignment, and named upstream artifacts. Check source files, inputs, configuration, and relevant decisions rather than relying only on a prior assistant's summary. Missing information is a limitation to report, not a fact to infer. Do not load unrelated project material merely because it is available.

Produce the requested artifact and record its location, version, evidence, limitations, and next action. Distinguish proposed text, sandbox evidence, committed source, and final execution in the User-designated environment. Preserve the commands, inputs, outputs, configuration, and environment needed to inspect a reported result.

Use Reference posts for the full URLs of directly relevant earlier entries, one per line, including multiple references when combining threads. Verify saved destinations by fetching the entry or reading faithful structured rows; preserve native page-mention destinations. Follow references only as far as the task requires and avoid repeated visits by page ID. Report inaccessible posts. Inspect relevant recent Last edited time values as well as new entries.

Preserve an entry's originating Agent instance ID when editing it. Identify the editing instance, date/time, and change in dated content, retaining prior material or a version link where needed. Verify attribution on read-back. Native creation and last-edit timestamps are service-maintained signals, not an edit history or an acceptance decision.

## Review and hand off

Review the actual artifact, methods, assumptions, sources, tests, and evidence against acceptance criteria. State what was checked and what could not be checked. After recording the review, clear only your own review request and set your own approval only when endorsing the current version. Material revisions require reconsidering approvals. See [record and review guidance](references/record-and-review.md).

A handoff identifies accepted state, work completed, exact files and revisions, execution evidence including failures, unresolved issues, superseded work, and one next task with an owner and acceptance condition. Use the S7 template. The receiving session checks the handoff against the governing record before continuing.

When evidence changes a hypothesis or project direction, present its implications to the User. Update the record only according to the User's decision and distinguish new direction from the prior state.

## Access and communication

Use only authorized tools and project locations. Never put credentials in instructions, notebooks, logs, or commits. Access to a workspace does not authorize publication of its contents. Apply the User's data-disposition decisions within applicable requirements. When a required integration or permitted execution environment is unavailable, state the limitation and record what was not done.

Do not assume another participant has seen a message or artifact until the shared record or User establishes that fact. Do not represent agreement after exposure as independent confirmation. Process provenance records assistance and verification; the human User retains scientific authorship and accountability.

---

## Included file: references/protocol.md

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
3. Abstracts may be used to screen results for relevance to the proposition, but an abstract alone cannot validate a citation or establish claim support. A retained candidate proceeds to `REFERENCE-VALIDATION` only after the complete primary text is obtained and inspected.
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

### Complete-primary-text requirement

**All citations must be sourced from the complete primary text of the cited work.** Claim-source correspondence is established only from primary text that the acting participant has actually inspected. Model memory may suggest search terms, authors, titles, or candidate references, but memory is never evidence that a source exists or supports a claim.

For a paper, inspect the complete paper rather than relying on the abstract. For another citable primary source, inspect the complete primary source needed to evaluate the cited claim. Abstracts, search-result snippets, generated summaries, another paper's description, secondary citation chains, bibliographic metadata, and remembered content may help locate or screen a source but cannot validate it or support a manuscript claim.

If the acting participant cannot access the complete primary text, citation validation stops. The participant asks the User to provide the complete primary text or access to it. Obtaining and supplying the source material needed for review is the User's responsibility as project leader. Until the complete primary text is available and inspected, the reference remains Provisional, inaccessible, or unverified and cannot be used as evidentiary support for a project claim.

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


---

## Included file: references/implementation-guide.md

# SCUTER implementation guide

SCUTER provides a concrete protocol for collaborative AI research under the scientist's direction. Start with one bounded task and a manageable record. Adapt the setup deliberately as the project develops.

The **User** is the human scientific lead. **Agent A** is the session assigned to lead the current task, and **Agent B** is its assigned reviewer; those roles can reverse. The User may delegate workspace setup to one chosen Agent while retaining direction and acceptance.

## 1. Define the research and acceptance criteria

**The User defines the task; Agent A may help specify it.** Record the scientific objective, questions, relevant background resources, assumptions, and intended outputs. Identify the human User, each AI participant, the tools available to each, and where execution will occur. Decide which information each participant may access and what may be supplied to external services.

Specify what evidence would justify accepting the first task. For a script, this might include inspected source, a recorded test input, expected output, and an executed test. For a literature claim, identify the supporting source, the exact assertion, and the required second check. State what remains outside the task.

## 2. Establish the shared record

**The User selects the locations and authorizes setup; Agent A can create the record.** Alternatively, the User can create it directly. Create a Project Overview and one Collaboration Log. Use the Overview for the current scientific question, assumptions, accepted artifacts, unresolved limitations, and relevant prior work. Use the log for material actions and decisions. Extended methods and analyses belong in linked notebooks. Versioned source and outputs belong in suitable file stores with exact paths and identifiers recorded in the log.

The User supplies the instructions before delegated setup. After creation, the User checks the Overview and gives each participant the same adopted protocol and project locations. Each participant verifies that they can retrieve the intended artifacts. A link, attachment description, or success message is not evidence that another participant can access a file.

The [Notion setup guide](notion-setup.md) provides a practical schema. The protocol's S6 section provides a worked record. Using multiple filtered views of a log does not require multiple copies of the records.

## 3. Adopt the protocol and introduce the participants

Read and adapt the [work contract](protocol.md). Its S8 template records project-specific roles, locations, scope, evidence classes, acceptance criteria, and release requirements. Select a prior-art search coverage declaration and record it. Maintain the search record separately from the claim-specific citation ledger. Apply the protocol's citation requirements when drafting or reviewing scientific text: outside empirical, theoretical, methodological, mechanistic, interpretive, and quantitative claims are cited; describing a claim as common knowledge or standard is not an exemption. Current-project hypotheses, assumptions, derivations, and results are citation-exempt only to the extent they genuinely originate in the present work.

All citations are sourced from the complete primary text of the cited work. Memory may identify a candidate but is not evidence. Abstracts, search snippets, generated summaries, another source's paraphrase, citation chains, and bibliographic metadata may be used for discovery or screening but not for citation validation or claim support. Inspect the complete paper or other complete primary source needed to evaluate the cited claim. If the complete primary text cannot be accessed, stop validation and ask the User to provide the text or access to it. Obtaining the source material needed for review is the User's responsibility as project leader. Until supplied and inspected, the reference remains Provisional, inaccessible, or unverified and cannot support a project claim.

Supply the Skill through a supported installation mechanism, or provide the complete Markdown instruction edition. Confirm that the assistant can read the entry instructions and companion protocol, guidance, and templates. The User still supplies permissions, project locations, and each transition between participants. Installing instructions does not create service connections.

At the start of a session, the User supplies its assignment and a distinct project-chat label. The Agent identifies the governing protocol, current objective, available tools, and missing resources, and registers that label once in the log. It reuses the identifier in Agent instance ID for its entries. The User may name the review fields for the participating assistants; record the mapping. Displayed provider/model identity is separate from the chat label. Do not infer unexposed model or connector versions.

## 4. Run the task-review-acceptance cycle

| Stage | Who acts | Action and record |
| --- | --- | --- |
| Assign | User | Specifies the work, lead, reviewer, upstream artifacts, constraints, and acceptance criteria. |
| Orient | Agent A | Reads the governing record and identifies missing or conflicting context. |
| Produce | Agent A | Supplies the proposed artifact and records evidence, limitations, and exact file locations. |
| Test and version | User and Agent A | Agent A supplies files and tests; the User controls authoritative execution and versioning or explicitly delegates a bounded repository write. Preserve code, command, inputs, outputs, configuration, and source revision. |
| Review | Agent B | Examines the actual artifact and evidence against the acceptance criteria at the User's direction. |
| Resolve | Agents A and B; User | Agent A makes assigned repairs, Agent B checks them, and the User controls required final reruns and resolves remaining disagreements. |
| Accept | User | Evaluates the evidence and determines the disposition. |
| Synchronize | User or designated Agent | Updates the Overview, accepted artifact links, log status, and next task according to the User's recorded decision. |

Review may precede execution when a proposed action warrants inspection first. A sandbox demonstration must retain that evidence label. A commit identifies a file state, not a validated result. A checksum identifies completed bytes, not scientific correctness.

The User determines who acts next. Lead and review roles may reverse. Multiple successive actions by one participant do not require artificial alternation or imply greater scientific contribution.

## 5. Maintain evidence and review state

Record what a reviewer inspected, the specific version, what is supported, what remains uncertain, and any required repair. Keep dated review text as the historical evidence. Review-request checkboxes route current work; approval fields record endorsement of the current version.

Treat claim state separately from review state. Every newly proposed scientific proposition defaults to `HYPOTHESIS ONLY: not source-supported`. It may guide further work but does not enter evidence-bearing structures. Use `EVIDENCE SUPPORTED: [specific proposition]` only when the record identifies the exact supporting source or artifact, what that evidence supports, what it does not support, and its limitations. The User sets the evidentiary threshold and is the only participant who promotes a proposition.

Partial support is not a middle state for the whole claim. If evidence supports one sub-proposition but not a broader mechanism, only that sub-proposition can be proposed as `EVIDENCE SUPPORTED`; the broader mechanism remains `HYPOTHESIS ONLY: not source-supported`. Apply these labels at the proposition level rather than to an entire note or log entry when it contains multiple claims. Preserve the transition and User decision in the durable record.

Each reviewer clears only their own review request after recording a response. A material revision requires reconsidering prior approvals. Record whether the reviewer had already seen another participant's output. Sequential checks remain useful but are not independent confirmation.

After every shared-record or repository write, retrieve the result. Check its location and structured properties separately. After transferring an artifact, confirm access from the receiving context. See [record and review guidance](record-and-review.md).

Use Reference posts to link each entry to directly relevant earlier posts, one URL per line. Multiple references retain both branches when work is combined. Fetch the saved entry to verify the link destinations, including any native page mentions returned by the connector. Preserve the originating Agent instance ID on edits and identify the actual editing instance and date/time in the content.

## 6. Reorient when the science changes

New evidence can change the hypothesis, interpretation, required validation, or project direction. The User determines what those changes mean for the project. Update affected assumptions, dependencies, assignments, and acceptance criteria before continuing.

Use task-relevant context rather than routinely loading the entire record. The User identifies the relevant upstream notebooks, decisions, inputs, and results. The assistant should report contradictions or missing dependencies instead of silently choosing a convenient interpretation. Follow Reference posts backward as needed without repeatedly visiting the same page. Check relevant Last edited time values as well as new entries; a timestamp signals a change to inspect, not acceptance.

## 7. Prepare a handoff

At the User's direction, the departing Agent prepares a handoff when work pauses, a substantial unit ends, or a new session takes over. The User checks it and directs the receiving session to the governing records. Include accepted state, completed work, exact files and revisions, execution evidence including failures, open questions, superseded work, limitations, and one next action with an owner and acceptance criterion. Use S7 of the protocol.

Compare the handoff with the Overview, log, and repository. Ask whether any hard-won constraints or rejected approaches were omitted. The receiving session checks those same sources before resuming. A concise summary should not erase the evidence needed to verify it.

## 8. Release deliberately

The User determines release readiness. Check the agreed scientific, citation, prior-art, execution, artifact, and disclosure requirements. Preserve completed outputs, their identities, and unresolved limitations. Record the decision and exact released revision.

A build result is evidence about that build only. Package acceptance is evidence about that installation attempt only. Treat ease of adoption, protocol adherence, and scientific effectiveness as separate questions requiring appropriate evaluation.

---

## Included file: references/notion-setup.md

# Setting up a SCUTER record in Notion

Confirm the intended workspace and parent page with the User before creating records. Use the actual tool schemas available to the current session; connector names and accepted parameters can vary.

Create a Project Overview, one Collaboration Log, a prior-art search record, and a citation ledger. Add numbered notebooks for longer methods and analyses as needed. The Overview states what currently governs. The log preserves material actions, evidence, decisions, and next steps. The citation ledger records whether the complete primary text was actually inspected for each reference. Abstract-only, snippet-only, memory-based, secondary-source, or inaccessible candidates are not validated citations. If complete primary text is unavailable, the acting participant asks the User to provide the text or access to it before validation continues.

Evidence-state labels are proposition-specific. When an entry contains more than one scientific proposition, do not use one row-level checkbox or status to imply that all are supported. Label the exact proposition in the entry body or maintain separate claim records: `HYPOTHESIS ONLY: not source-supported` is the default, and `EVIDENCE SUPPORTED: [specific proposition]` is used only after the User accepts the evidence for that proposition.

## Collaboration Log fields

| Field | Suggested type | Purpose |
| --- | --- | --- |
| Entry | Title | Material event or work item |
| Created time | Created time | Automatically recorded entry-creation time |
| Last edited time | Last edited time | Automatically maintained latest-edit time |
| Date | Date, with optional time | Stated scientific or operational date |
| Agent instance ID | Text | Registered chat identifier for the originating entry |
| Owner | Select | Responsible participant |
| Assignment to | Multi-select | Participant expected to act next |
| Needs Agent A Review; Needs Agent B Review; Needs User Review | Separate checkboxes | Current routing requests |
| Approved by Agent A; Approved by Agent B; Approved by User | Separate checkboxes | Participant endorsements of the current version |
| Status | Select | Proposed, Needs Review, Accepted, Rejected, Parked, or Superseded |
| Source | Multi-select | User, named assistant, run, or supplied material |
| Next Action | Text | Next task, owner, and acceptance condition |
| Summary; Purpose | Separate text fields | Result and reason for the work |
| Topic; Type | Separate select fields | Classification |
| Subproject | Multi-select | Workstream |
| Reference posts | Text | Direct earlier-entry URLs, one per line |
| Reference links | URL or text | Supporting resources and evidence |
| Repository; Commit SHA | URL and text | Exact source state |

Grouped names represent separate fields. The table describes the 25-field core; the protocol's S6 and S8 templates supply examples. Displayed provider/model identity and review exposure may use separate fields or dated entry content. The User may adapt the schema and participant labels to the project. In the example implementation, Agent A and Agent B fields were named for GPT and Claude; record that mapping without equating a provider label with a fixed lead or reviewer role. The public Repository and Commit SHA fields correspond to GitHub repo and GitHub commit SHA in that implementation.

Create **Created time** and **Last edited time** as native Notion properties. Do not populate them manually. Date records the stated time of the work; a page timestamp is not evidence of when an analysis executed.

## Reference posts

Use one Text property, not a single-URL property or a relation. Enter the full URLs of directly relevant earlier posts, one per line. Leave it blank when no earlier post is being referenced, and include multiple URLs when combining threads. Do not copy every ancestor into the field or update the referenced entries merely to create a callback. Keep Reference links for supporting resources.

After writing, fetch the saved entry and verify the intended destinations. A connector may return URLs as native page mentions or line breaks as `<br>`; preserve the destinations rather than assuming the value is plain text. Use page fetch or a faithful structured-row read. SQL text projections can omit mention destinations and are not authoritative for this check.

To recover earlier context, open the references and continue backward only as far as the task requires. Deduplicate by page ID rather than URL spelling, avoid self-links and repeated visits, and report inaccessible targets. The body explains the connection where needed. A blank historical field does not prove that no upstream work exists, and a page link does not pin an earlier version or confer approval.

## Create and verify

Read the target database's schema before creating a row. Identify the correct data source and use the exact parent and property forms required by the current connector. Do not substitute a page identifier for a data-source identifier or guess how checkbox values are encoded.

After creating, editing, or moving a record, fetch it again. Verify both its parent location and its saved properties. For pages with child pages or databases, use narrow edits and preserve the child references unless the User has requested their removal.

Use a single underlying Collaboration Log. Label filtered views clearly, such as **Recent review queue**, and distinguish them from **Full Collaboration Log**. Different views are not separate stores, and the same action need not be copied into each.

## Maintain history and current state

Retain dated reviews and decisions in the record body. Mutable routing fields do not reconstruct past review events. Mark obsolete records as superseded when their history remains relevant, and link to the governing replacement.

Register each chat once and reuse its stable Agent instance ID on the entries it originates; the identifier need not appear in entry titles. Preserve that origin when another session edits or adds to an entry. Identify the actual editing instance, date/time, and change in dated content, retaining the prior material or a version link when needed. Read back the attribution as well as the edit.

On resumption, inspect relevant entries with recent Last edited time values as well as new entries. The timestamp signals a possible change to inspect; it is not a complete edit history, proof of who edited, or automatic renewal of approval.

After a material decision, update the Overview as well as the log. Record accepted artifacts and unresolved tasks together so the next participant can determine what governs without reconstructing it from conversation.

---

## Included file: references/record-and-review.md

# Scientific records and review

SCUTER's record connects scientific intent to evidence and accepted artifacts. It should support scrutiny and reuse rather than merely preserve a conversation.

## Record what happened

For a material action, record its purpose, responsible participant, exact inputs or governing records, work performed, outputs, uncertainty, and next action. For execution, include the command, source revision, configuration, environment, and resulting files. Compute checksums only after files are complete.

Separate proposed interpretations from observed results. Every newly proposed scientific proposition defaults to `HYPOTHESIS ONLY: not source-supported`. Hypothesis-only material may guide further work but is excluded from evidence-bearing project structures. Use `EVIDENCE SUPPORTED: [specific proposition]` only for the exact proposition whose evidence has been identified and verified, and record what the evidence does and does not support. Partial support never promotes the broader claim. The User sets the evidentiary threshold and is the only participant who promotes a proposition. Identify sandbox evidence as such. A repository commit establishes source identity, while a run record states what executed. Neither agreement nor a successful build supplies the missing evidence for a scientific claim.

## Record identity and exposure prospectively

Register each chat with a stable project-specific identifier and use it in Agent instance ID for the entries that session originates. A replacement chat receives its own identifier rather than inheriting the departing session's identity. Record the provider and displayed model/version separately when available; do not infer them from the chat label. State when a version or historical identity is unavailable. Record whether the reviewer had already seen the contribution under review or another participant's evaluation.

Preserve an entry's originating Agent instance ID on later edits. Identify an editing or appending instance, actual date/time, and change in dated content. Retain the previous material or an exact version link when needed to reconstruct a substantive change, and verify the attribution on read-back. A human decision recorded by an Agent identifies the User as decision-maker and the Agent instance as recorder.

A second check following exposure can identify defects without constituting independent confirmation. Do not reconstruct independence from timestamps alone. Model self-assessment is not a substitute for inspecting the relevant artifact or source.

## Review the work itself

State the revision inspected, tests and sources examined, observations supported, uncertainties, and necessary repairs. A reviewer approves claim-source correspondence only after inspecting the complete primary text of the cited work. Model memory, abstracts, search snippets, generated summaries, secondary descriptions, citation chains, and bibliographic metadata may assist discovery or screening but cannot validate a citation or support a project claim. If the complete primary text is unavailable, the reviewer or acting participant asks the User to provide the text or access to it; obtaining the source material needed for review is the User's responsibility as project leader. Until supplied and inspected, the reference remains Provisional, inaccessible, or unverified. Review scientific prose for uncited external claims as well as for incorrect citations. Do not accept "common knowledge," "standard," or "well known" as a citation exemption when a claim is empirical, theoretical, methodological, mechanistic, interpretive, quantitative, or has a plausible alternate convention, scope, interpretation, or domain of validity. Current-project statements are citation-exempt only where they genuinely originate in the present work; external premises remain citable. Novelty and priority statements require the applicable prior-art search in addition to citations. Criticism concerns the artifact, evidence, assumption, or method. The User resolves competing interpretations and determines acceptance.

Review requests and approvals describe current routing and endorsement. The dated review text preserves the event. A substantive revision requires reconsidering earlier approvals, not carrying them forward automatically.

## Keep context relevant

Before resuming work, identify the accepted scientific question and the upstream records needed for the task. Use Reference posts to record direct earlier-entry URLs, one per line, including more than one when combining threads. Follow those references as needed, avoiding repeated visits by page ID and reporting inaccessible records. Read saved link destinations through page fetch or a faithful structured-row read, not a lossy SQL text projection.

Check relevant entries' Last edited time as well as their Created time. An older entry can contain a recent revision. Read the changed content rather than inferring new acceptance from a timestamp. When sources disagree, state the discrepancy and repair the record under User direction. An available record has not necessarily been incorporated into the current analysis.

Evaluate any changes in context-loading strategy within the adopting project. Record what changed and what was observed; do not generalize an impression of improved focus into a universal property of AI systems.

---

## Included file: LICENSE.md

# Creative Commons Attribution 4.0 International

Creative Commons Corporation (“Creative Commons”) is not a law firm and does not provide legal services or legal advice. Distribution of Creative Commons public licenses does not create a lawyer-client or other relationship. Creative Commons makes its licenses and related information available on an “as-is” basis. Creative Commons gives no warranties regarding its licenses, any material licensed under their terms and conditions, or any related information. Creative Commons disclaims all liability for damages resulting from their use to the fullest extent possible.

### Using Creative Commons Public Licenses

Creative Commons public licenses provide a standard set of terms and conditions that creators and other rights holders may use to share original works of authorship and other material subject to copyright and certain other rights specified in the public license below. The following considerations are for informational purposes only, are not exhaustive, and do not form part of our licenses.

* __Considerations for licensors:__ Our public licenses are intended for use by those authorized to give the public permission to use material in ways otherwise restricted by copyright and certain other rights. Our licenses are irrevocable. Licensors should read and understand the terms and conditions of the license they choose before applying it. Licensors should also secure all rights necessary before applying our licenses so that the public can reuse the material as expected. Licensors should clearly mark any material not subject to the license. This includes other CC-licensed material, or material used under an exception or limitation to copyright. [More considerations for licensors](http://wiki.creativecommons.org/Considerations_for_licensors_and_licensees#Considerations_for_licensors).

* __Considerations for the public:__ By using one of our public licenses, a licensor grants the public permission to use the licensed material under specified terms and conditions. If the licensor’s permission is not necessary for any reason–for example, because of any applicable exception or limitation to copyright–then that use is not regulated by the license. Our licenses grant only permissions under copyright and certain other rights that a licensor has authority to grant. Use of the licensed material may still be restricted for other reasons, including because others have copyright or other rights in the material. A licensor may make special requests, such as asking that all changes be marked or described. Although not required by our licenses, you are encouraged to respect those requests where reasonable. [More considerations for the public](http://wiki.creativecommons.org/Considerations_for_licensors_and_licensees#Considerations_for_licensees).

## Creative Commons Attribution 4.0 International Public License

By exercising the Licensed Rights (defined below), You accept and agree to be bound by the terms and conditions of this Creative Commons Attribution 4.0 International Public License ("Public License"). To the extent this Public License may be interpreted as a contract, You are granted the Licensed Rights in consideration of Your acceptance of these terms and conditions, and the Licensor grants You such rights in consideration of benefits the Licensor receives from making the Licensed Material available under these terms and conditions.

### Section 1 – Definitions.

a. __Adapted Material__ means material subject to Copyright and Similar Rights that is derived from or based upon the Licensed Material and in which the Licensed Material is translated, altered, arranged, transformed, or otherwise modified in a manner requiring permission under the Copyright and Similar Rights held by the Licensor. For purposes of this Public License, where the Licensed Material is a musical work, performance, or sound recording, Adapted Material is always produced where the Licensed Material is synched in timed relation with a moving image.

b. __Adapter's License__ means the license You apply to Your Copyright and Similar Rights in Your contributions to Adapted Material in accordance with the terms and conditions of this Public License.

c. __Copyright and Similar Rights__ means copyright and/or similar rights closely related to copyright including, without limitation, performance, broadcast, sound recording, and Sui Generis Database Rights, without regard to how the rights are labeled or categorized. For purposes of this Public License, the rights specified in Section 2(b)(1)-(2) are not Copyright and Similar Rights.

d. __Effective Technological Measures__ means those measures that, in the absence of proper authority, may not be circumvented under laws fulfilling obligations under Article 11 of the WIPO Copyright Treaty adopted on December 20, 1996, and/or similar international agreements.

e. __Exceptions and Limitations__ means fair use, fair dealing, and/or any other exception or limitation to Copyright and Similar Rights that applies to Your use of the Licensed Material.

f. __Licensed Material__ means the artistic or literary work, database, or other material to which the Licensor applied this Public License.

g. __Licensed Rights__ means the rights granted to You subject to the terms and conditions of this Public License, which are limited to all Copyright and Similar Rights that apply to Your use of the Licensed Material and that the Licensor has authority to license.

h. __Licensor__ means the individual(s) or entity(ies) granting rights under this Public License.

i. __Share__ means to provide material to the public by any means or process that requires permission under the Licensed Rights, such as reproduction, public display, public performance, distribution, dissemination, communication, or importation, and to make material available to the public including in ways that members of the public may access the material from a place and at a time individually chosen by them.

j. __Sui Generis Database Rights__ means rights other than copyright resulting from Directive 96/9/EC of the European Parliament and of the Council of 11 March 1996 on the legal protection of databases, as amended and/or succeeded, as well as other essentially equivalent rights anywhere in the world.

k. __You__ means the individual or entity exercising the Licensed Rights under this Public License. Your has a corresponding meaning.

### Section 2 – Scope.

a. ___License grant.___

    1. Subject to the terms and conditions of this Public License, the Licensor hereby grants You a worldwide, royalty-free, non-sublicensable, non-exclusive, irrevocable license to exercise the Licensed Rights in the Licensed Material to:

        A. reproduce and Share the Licensed Material, in whole or in part; and

        B. produce, reproduce, and Share Adapted Material.

    2. __Exceptions and Limitations.__ For the avoidance of doubt, where Exceptions and Limitations apply to Your use, this Public License does not apply, and You do not need to comply with its terms and conditions.

    3. __Term.__ The term of this Public License is specified in Section 6(a).

    4. __Media and formats; technical modifications allowed.__ The Licensor authorizes You to exercise the Licensed Rights in all media and formats whether now known or hereafter created, and to make technical modifications necessary to do so. The Licensor waives and/or agrees not to assert any right or authority to forbid You from making technical modifications necessary to exercise the Licensed Rights, including technical modifications necessary to circumvent Effective Technological Measures. For purposes of this Public License, simply making modifications authorized by this Section 2(a)(4) never produces Adapted Material.

    5. __Downstream recipients.__

        A. __Offer from the Licensor – Licensed Material.__ Every recipient of the Licensed Material automatically receives an offer from the Licensor to exercise the Licensed Rights under the terms and conditions of this Public License.

        B. __No downstream restrictions.__ You may not offer or impose any additional or different terms or conditions on, or apply any Effective Technological Measures to, the Licensed Material if doing so restricts exercise of the Licensed Rights by any recipient of the Licensed Material.

    6. __No endorsement.__ Nothing in this Public License constitutes or may be construed as permission to assert or imply that You are, or that Your use of the Licensed Material is, connected with, or sponsored, endorsed, or granted official status by, the Licensor or others designated to receive attribution as provided in Section 3(a)(1)(A)(i).

b. ___Other rights.___

    1. Moral rights, such as the right of integrity, are not licensed under this Public License, nor are publicity, privacy, and/or other similar personality rights; however, to the extent possible, the Licensor waives and/or agrees not to assert any such rights held by the Licensor to the limited extent necessary to allow You to exercise the Licensed Rights, but not otherwise.

    2. Patent and trademark rights are not licensed under this Public License.

    3. To the extent possible, the Licensor waives any right to collect royalties from You for the exercise of the Licensed Rights, whether directly or through a collecting society under any voluntary or waivable statutory or compulsory licensing scheme. In all other cases the Licensor expressly reserves any right to collect such royalties.

### Section 3 – License Conditions.

Your exercise of the Licensed Rights is expressly made subject to the following conditions.

a. ___Attribution.___

    1. If You Share the Licensed Material (including in modified form), You must:

        A. retain the following if it is supplied by the Licensor with the Licensed Material:

            i. identification of the creator(s) of the Licensed Material and any others designated to receive attribution, in any reasonable manner requested by the Licensor (including by pseudonym if designated);

            ii. a copyright notice;

            iii. a notice that refers to this Public License;

            iv. a notice that refers to the disclaimer of warranties;

            v. a URI or hyperlink to the Licensed Material to the extent reasonably practicable;

        B. indicate if You modified the Licensed Material and retain an indication of any previous modifications; and

        C. indicate the Licensed Material is licensed under this Public License, and include the text of, or the URI or hyperlink to, this Public License.

    2. You may satisfy the conditions in Section 3(a)(1) in any reasonable manner based on the medium, means, and context in which You Share the Licensed Material. For example, it may be reasonable to satisfy the conditions by providing a URI or hyperlink to a resource that includes the required information.

    3. If requested by the Licensor, You must remove any of the information required by Section 3(a)(1)(A) to the extent reasonably practicable.

    4. If You Share Adapted Material You produce, the Adapter's License You apply must not prevent recipients of the Adapted Material from complying with this Public License.

### Section 4 – Sui Generis Database Rights.

Where the Licensed Rights include Sui Generis Database Rights that apply to Your use of the Licensed Material:

a. for the avoidance of doubt, Section 2(a)(1) grants You the right to extract, reuse, reproduce, and Share all or a substantial portion of the contents of the database;

b. if You include all or a substantial portion of the database contents in a database in which You have Sui Generis Database Rights, then the database in which You have Sui Generis Database Rights (but not its individual contents) is Adapted Material; and

c. You must comply with the conditions in Section 3(a) if You Share all or a substantial portion of the contents of the database.

For the avoidance of doubt, this Section 4 supplements and does not replace Your obligations under this Public License where the Licensed Rights include other Copyright and Similar Rights.

### Section 5 – Disclaimer of Warranties and Limitation of Liability.

a. __Unless otherwise separately undertaken by the Licensor, to the extent possible, the Licensor offers the Licensed Material as-is and as-available, and makes no representations or warranties of any kind concerning the Licensed Material, whether express, implied, statutory, or other. This includes, without limitation, warranties of title, merchantability, fitness for a particular purpose, non-infringement, absence of latent or other defects, accuracy, or the presence or absence of errors, whether or not known or discoverable. Where disclaimers of warranties are not allowed in full or in part, this disclaimer may not apply to You.__

b. __To the extent possible, in no event will the Licensor be liable to You on any legal theory (including, without limitation, negligence) or otherwise for any direct, special, indirect, incidental, consequential, punitive, exemplary, or other losses, costs, expenses, or damages arising out of this Public License or use of the Licensed Material, even if the Licensor has been advised of the possibility of such losses, costs, expenses, or damages. Where a limitation of liability is not allowed in full or in part, this limitation may not apply to You.__

c. The disclaimer of warranties and limitation of liability provided above shall be interpreted in a manner that, to the extent possible, most closely approximates an absolute disclaimer and waiver of all liability.

### Section 6 – Term and Termination.

a. This Public License applies for the term of the Copyright and Similar Rights licensed here. However, if You fail to comply with this Public License, then Your rights under this Public License terminate automatically.

b. Where Your right to use the Licensed Material has terminated under Section 6(a), it reinstates:

    1. automatically as of the date the violation is cured, provided it is cured within 30 days of Your discovery of the violation; or

    2. upon express reinstatement by the Licensor.

    For the avoidance of doubt, this Section 6(b) does not affect any right the Licensor may have to seek remedies for Your violations of this Public License.

c. For the avoidance of doubt, the Licensor may also offer the Licensed Material under separate terms or conditions or stop distributing the Licensed Material at any time; however, doing so will not terminate this Public License.

d. Sections 1, 5, 6, 7, and 8 survive termination of this Public License.

### Section 7 – Other Terms and Conditions.

a. The Licensor shall not be bound by any additional or different terms or conditions communicated by You unless expressly agreed.

b. Any arrangements, understandings, or agreements regarding the Licensed Material not stated herein are separate from and independent of the terms and conditions of this Public License.

### Section 8 – Interpretation.

a. For the avoidance of doubt, this Public License does not, and shall not be interpreted to, reduce, limit, restrict, or impose conditions on any use of the Licensed Material that could lawfully be made without permission under this Public License.

b. To the extent possible, if any provision of this Public License is deemed unenforceable, it shall be automatically reformed to the minimum extent necessary to make it enforceable. If the provision cannot be reformed, it shall be severed from this Public License without affecting the enforceability of the remaining terms and conditions.

c. No term or condition of this Public License will be waived and no failure to comply consented to unless expressly agreed to by the Licensor.

d. Nothing in this Public License constitutes or may be interpreted as a limitation upon, or waiver of, any privileges and immunities that apply to the Licensor or You, including from the legal processes of any jurisdiction or authority.

```
Creative Commons is not a party to its public licenses. Notwithstanding, Creative Commons may elect to apply one of its public licenses to material it publishes and in those instances will be considered the “Licensor.” Except for the limited purpose of indicating that material is shared under a Creative Commons public license or as otherwise permitted by the Creative Commons policies published at [creativecommons.org/policies](http://creativecommons.org/policies), Creative Commons does not authorize the use of the trademark “Creative Commons” or any other trademark or logo of Creative Commons without its prior written consent including, without limitation, in connection with any unauthorized modifications to any of its public licenses or any other arrangements, understandings, or agreements concerning use of licensed material. For the avoidance of doubt, this paragraph does not form part of the public licenses.

Creative Commons may be contacted at creativecommons.org
```

---

## Content manifest

```json
{
  "name": "scuter",
  "version": "0.2.2-dev",
  "status": "development",
  "protocol_source": {
    "path": "protocol/01.work-contract.md",
    "sha256": "38cd6ee79a2e3f5bbbfa010a2898a0b7df5304050782fad49e1d454aa930f857"
  },
  "source_files_sha256": {
    "LICENSE.md": "e92080c5a49a1081ed4fbb5c1a72d399a5baf72e384e3dc28371c7c2fb57cf81",
    "docs/implementation-guide.md": "e0af99475b4cabe954afbc29339a372728fd3cab34cebcb00999b426961cca52",
    "docs/notion-setup.md": "6808fc278e3f86db98ecdaef141dd43fd6faa05b2f698bae7293780eba04ac5e",
    "docs/record-and-review.md": "649f457c7dfdadb230b0f60d3d42d23d8262e6703521ca13ac113f9714b16b5d",
    "protocol/01.work-contract.md": "38cd6ee79a2e3f5bbbfa010a2898a0b7df5304050782fad49e1d454aa930f857",
    "skills/scuter/SKILL.md": "0deb39b2fecdc8a70b46715ac5477c4280875cba54767defd2d56b800d52956b"
  },
  "members_sha256": {
    "LICENSE.md": "e92080c5a49a1081ed4fbb5c1a72d399a5baf72e384e3dc28371c7c2fb57cf81",
    "SKILL.md": "0deb39b2fecdc8a70b46715ac5477c4280875cba54767defd2d56b800d52956b",
    "references/implementation-guide.md": "b517b325fbe7326e086b1355ce55520b38439ff5842b63f9ab711106dd8607bf",
    "references/notion-setup.md": "6808fc278e3f86db98ecdaef141dd43fd6faa05b2f698bae7293780eba04ac5e",
    "references/protocol.md": "38cd6ee79a2e3f5bbbfa010a2898a0b7df5304050782fad49e1d454aa930f857",
    "references/record-and-review.md": "649f457c7dfdadb230b0f60d3d42d23d8262e6703521ca13ac113f9714b16b5d"
  },
  "document_link_adjustment": "The bundled implementation guide links to references/protocol.md within the Skill."
}
```
