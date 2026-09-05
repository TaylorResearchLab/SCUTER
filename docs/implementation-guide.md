# Quick-start implementation guide

This guide translates the workflow evaluated in the main manuscript into a practical setup that another investigator can adapt. It is written for scientists who use interactive AI chat products but need work to continue across sessions, repositories, protected computing environments, and changing scientific questions. The detailed reusable work contract, synthetic examples, and templates that follow provide the governance language and record structures referenced here.

This guide uses three generic participant labels:

- **User:** the human scientific lead, project manager, access-control authority, adjudicator, and release authority;
- **Agent A:** the AI session assigned to lead a bounded task;
- **Agent B:** the AI session assigned to review, challenge, reproduce, repair, or extend the work.

Agent roles are reversible. Agent A and Agent B may be sessions from different providers, as in the study, or named sessions from one provider. Using two providers most closely reproduces the evaluated workflow; using two sessions from one provider is a reasonable adaptation but was not tested as an equivalent condition. Other implementations of this guide could utilize more than two AI sessions, but that was not tested here.

## What this system is designed to do

The system separates four functions that are often mixed together in chat:

| Function | Recommended location | Primary responsibility |
| --- | --- | --- |
| Scientific intent, decisions, review, and current state | Structured shared workspace such as Notion | User governs; all participants record material work |
| Versioned code, configuration, tests, and releasable files | GitHub or another version-control system | User normally retains repository custody; agents propose and review |
| Private data and authoritative execution | User-controlled local, institutional, or protected environment | User authorizes and performs final runs |
| Large completed outputs and release archives | User-selected durable artifact store | User controls storage and records checksums and links |

The shared workspace is not designed to replace version control, and the repository is not designed to replace the scientific record. The shared workspace explains why work was undertaken, what evidence was accepted, who reviewed it, and what should happen next. The repository identifies the exact source state and exposes the changes. The execution environment produces the authoritative result. The User connects all three, applying scientific expertise to direct the process.

## Minimum viable setup

A minimal implementation requires:

1. one human User with explicit final authority;
2. at least two named AI sessions with assigned roles;
3. one structured Collaboration Log;
4. one page that states the current accepted project state;
5. one versioned repository when code or other versioned files are involved;
6. one defined location for private data and final execution;
7. one written work contract;
8. one explicit task-review-acceptance cycle;
9. one handoff format for resuming work in a new session.

Begin with a low-risk, bounded, public, or synthetic task. Validate the workflow and each integration before expanding the scope. During the initial pilot, follow the written stepwise workflow until the User is familiar enough with the process to adapt it deliberately. The steps are outlined below.

## Step 1. Define authority, privacy, and acceptance before creating the workspace

Write down the answers to the following questions before assigning work:

- What is the proposed objective of the study?
- What background resources are available at the start of the study, including references, prior data, code, protocols, and known constraints?
- What scientific questions or work units are in scope?
- Which project-specific records, files, and data may each AI session access?
- Which data must remain in a protected environment?
- Who controls repository credentials, staging, commits, pushes, pull requests, merge, and release?
- What evidence is required before a result can be accepted?
- What protocol should a participant follow when they believe the available evidence is insufficient?
- What protocol should participants follow when they disagree?
- How will unresolved evidentiary concerns or disagreements be presented to the User for adjudication and recorded?
- Which FAIR principles will the workflow and resulting research products be designed to support, and how will that support be documented?
- Which outputs may be made public, and under what license?
- Which external collaborators must be informed that AI assistance is being used?

The default used in the evaluated workflow was deliberately conservative. The User retained control of private data, authoritative execution, repository custody, merge, and release. AI sessions proposed, implemented, reviewed, interpreted, and tracked work, but did not accept their own results into the project state.

## Step 2. Create the shared workspace

Create a Notion project home page with links to four working areas:

1. **Project Overview.** A page that identifies the background of the research and what governs the project: the accepted scientific question, current assumptions, accepted repository commit, authoritative configuration, current outputs, unresolved limitations, and prior art. References and citations that kick off the project are stored here. The page should be regularly updated with project state or changes in direction. This page would be a first stop for future collaborators and would inform future AI sessions alongside the handoff document.
2. **Collaboration Log.** A live, structured database of material decisions, assignments, reviews, run results, corrections, supersessions, and handoffs.
3. **Numbered notebooks.** Longer records for mathematical and scientific methods, analyses, decisions, figures, or project-specific reasoning that do not fit in one log row, organized in the style of a scientific notebook.
4. **Product workspace.** A page or linked working area containing subpages for reports, manuscripts, figures, citation collections, PDFs, and links to drafts in progress.

The project home page should make the Project Overview page and Collaboration Log easy to find.

## Step 3. Build the Collaboration Log schema

The full template later in this supplement contains an extended schema. The following fields are sufficient for a first implementation:

| Field | Suggested type | Purpose |
| --- | --- | --- |
| Entry | Title | Human-readable name of the event or work item |
| Created time | System time | When the record was created |
| Date | Date | Scientific or operational date when needed |
| Source | Multi-select | User, Agent A, Agent B, Code/Run, or Uploaded Memo |
| Owner | Select | Participant responsible for the current item |
| Type | Select | Decision, Review, Run Result, Implementation, Handoff, Open Question, or Memo |
| Status | Select | Proposed, Needs Review, Accepted, Rejected, Parked, or Superseded |
| Assignment to | Multi-select | Participant expected to act next |
| Needs ... Review | Checkbox per participant | Temporary routing signal that a review is outstanding |
| Approved by ... | Checkbox per participant | Durable endorsement of the current version |
| Purpose | Text | Why this work is being done |
| Summary | Text | What was done or found |
| Next Action | Text | One explicit next step and responsible party |
| Reference links | URL or text | Notebook, document, output, or external source |
| Repository | URL | Versioned repository when applicable |
| Commit SHA | Text | Exact repository state associated with the record |
| Subproject | Select or multi-select | Workstream or hypothesis branch when useful |

Use review-request fields and approval fields for different purposes. A checked review field means that a participant still needs to inspect the item. An approval field means that the participant inspected and endorses the current version. A reviewer clears only their own review field after recording the review. A material revision invalidates prior approvals and may require review to be requested again.

The log entry or review text is the historical evidence. Checkboxes show current routing and endorsement, not the full sequence of past events.

## Step 4. Establish repository and execution custody

For scientifically high-value work, the safest default is User-controlled repository custody.

- The User controls credentials, staging, commits, pushes, pull requests, merge, tags, and release.
- AI sessions inspect User-supplied files or public repository contents, propose code or patches, recommend commands and tests, and review source differences and outputs.
- The User transfers proposed material into the working environment, inspects it, tests it, and performs the authoritative run.
- Private data remain in the protected environment. The repository may contain code, configuration, tests, schemas, and documentation without containing the protected inputs.
- Repository-scoped AI write access is optional and should be treated as a bounded exception rather than the default.

Protect the default branch and use named branches and pull requests for material changes. Keep passwords, personal access tokens, private keys, and session cookies out of prompts, notebooks, log fields, and commits. When an AI session requires repository access, use the narrowest institutionally approved integration and permissions that can complete the task.

Record both repository and file identity when they are relevant:

- A **Git commit SHA** identifies a particular state of the versioned repository.
- A **SHA-256 checksum** identifies the exact bytes of a completed output file, source bundle, or release archive.

Both identifiers can be recorded in the Collaboration Log and linked to the scientific purpose, command, environment, result, review history, and next action. Compute file checksums only after the file is complete. Do not place a checksum inside the file that the checksum is intended to verify.

## Step 5. Adopt the work contract

Give every participating session the same written contract before substantive work begins. At minimum, the contract should state:

- the User's authority and responsibility;
- the named AI roles and their reversibility;
- the privacy and access boundary;
- where decisions, code, outputs, and run evidence must be stored;
- the evidence hierarchy and acceptance criteria;
- the citation-validation rule;
- the review, approval, and disagreement process;
- the requirement to log material work;
- the handoff trigger and minimum handoff content;
- the context-reorientation rule;
- the release gate.

Do not assume that a contract placed somewhere in the workspace will be followed automatically. Include a compact version in important assignments and direct each new session to read the full contract and Project Overview page.

## Step 6. Define the first bounded task

Create a Collaboration Log record before starting. A useful task record answers:

- What is the exact task?
- Why is it needed?
- Which GitHub or Notion links explain the current project state?
- Which upstream notebooks, files, commits, data descriptions, or prior decisions must be read?
- Which participant leads?
- Which participant reviews?
- What evidence will count as success?
- What must not be disclosed or changed?
- What is the next action after completion?

Avoid assigning an entire open-ended project as the first task. Use a bounded unit such as reviewing a script, reproducing a numerical result, drafting a test plan, validating a citation, or comparing a small set of candidate methods.

## Step 7. Run the task-review-acceptance cycle

A typical cycle proceeds as follows:

1. **Assign.** The User creates or updates the task record and identifies the lead participant, relevant context, privacy boundary, and acceptance condition.
2. **Orient.** The lead session reads the work contract, Project Overview page, task record, and specifically named upstream dependencies.
3. **Produce.** The lead session proposes code, text, a patch, a calculation, a review, or another bounded work product.
4. **Record.** The lead session logs the result, uncertainty, file location, and next action. A useful result that exists only in chat is not yet a project artifact.
5. **Transfer and test.** The User transfers the work into the appropriate environment, inspects it, tests it, and performs the authoritative run when required.
6. **Version.** The User stages, commits, pushes, and usually opens or updates a pull request. Completed external files or archives receive SHA-256 checksums when appropriate.
7. **Review.** The reciprocal session examines the actual source difference, command, evidence, output, and relevant log records rather than relying only on the lead participant's summary.
8. **Resolve.** Objections are repaired, retained as explicit limitations, or adjudicated by the User. Courtesy does not substitute for evidence.
9. **Accept.** The User decides whether the acceptance criteria have been met and changes the item to Accepted, Rejected, Parked, or Superseded.
10. **Synchronize.** The accepted commit, output location, checksum, Project Overview page changes, and next task are written back to the shared record.

The cycle does not require equal turn-taking. One AI session may work through several incremental steps before the reciprocal session is brought back for review. Therefore, prompt counts, chat turns, and log-entry counts should not be interpreted as equal contribution or comparative performance.

## Step 8. Manage review and approval explicitly

A review should examine the artifact, assumptions, evidence, or execution path and provide a critique. Merely editing the lead participant's prose is not a reciprocal review.

After completing a requested review, the reviewer should:

1. record what was inspected in the Collaboration Log;
2. state what was supported, incorrect, uncertain, or not independently verifiable;
3. identify any required repair;
4. update the item's status and next action;
5. clear only their own review-request field;
6. set their own approval field only when they endorse the current version;
7. fetch or read back the record after logging and verify its location and structured properties. 

Agent approvals are positions, not votes. They do not combine into acceptance. The User remains the only participant who can decide that work enters the current accepted state.

Record whether a review was intended to be independent or sequential. If the reviewer already saw the lead participant's result, agreement should not be described as independent corroboration.

## Step 9. Reorient context without loading the entire project

A durable record solves storage but not selection. Relevant information can be present in the workspace and still be missed if the active session does not retrieve or apply it.

Before resuming a paused workstream or starting a task that depends on another workstream, the User should identify:

- the Project Overview page;
- the governing hypothesis or objective;
- the relevant notebook or decision record;
- the accepted repository commit and configuration;
- the upstream result or limitation that constrains the task;
- the exact question the participant must answer.

A prompt such as "Check the log" works only when the shared record is complete and the next action is already explicit. When the project is complex, name the specific records and artifacts that must be reconsidered.

Do not require every session to reread the entire project before every local task. Loading all available context increases cost and latency and can weaken focus. Select the subset needed to preserve both project coherence and reliable task execution.

## Step 10. The User can realign the project when the science changes

Discovery-driven projects do not follow a fixed recipe. New data, failed assumptions, validation results, or technical limitations can change the working hypothesis and therefore change which context is relevant.

When that occurs, the User may revise more than the immediate task by reassessing:

- the scientific question and current hypothesis;
- which assumptions still govern;
- which records, data, code, and outputs are now upstream dependencies;
- which milestones or tasks are obsolete;
- which new workstreams are required;
- which AI session should lead or review each workstream;
- what evidence is now required for acceptance.

The User then updates the Project Overview page and Collaboration Log before issuing the next assignment. The User's role is not only to restore old context, but to re-specify the scientific intent and the project state that should govern as evidence accumulates. AI participants may help the User assess the implications of a proposed change, but the User alone decides whether and how the project direction changes.


## Step 11. Create structured handoffs

As a project continues, the User may ask the active session, "How is your context? Are you ready for a handoff to a new session?" The response can provide an additional signal, but the User should not rely on self-assessment alone. The objective handoff triggers below still apply.

Generally, it's time to create a handoff:

- after a substantial work unit;
- before changing the lead participant;
- when a chat is becoming crowded;
- before a high-impact run;
- when work pauses and will resume later;
- whenever the User requests a new session.

A handoff should identify the current accepted state, work completed, governing files and commits, exact run evidence, open questions, superseded work, known limitations, and one explicit next action with an owner and acceptance condition.

After the first handoff draft is complete, the User should ask the originating session, "Are there any additional hard-won insights, constraints, or rejected approaches that the next session needs?" In this implementation, that second pass often surfaced details omitted from the initial draft. Recording them can prevent later re-litigation of resolved decisions.

Even after iterative revision, an AI-generated handoff may remain incomplete. The User should compare it with the Project Overview page, Collaboration Log, repository, and their own understanding of the project. The receiving participant must also compare these sources before continuing. If they disagree, preserve the uncertainty and repair the record rather than inventing continuity. When the User identifies an omitted fact, add it explicitly and ask the originating session to reconcile the revised handoff.

## Step 12. Release and archive deliberately

Before releasing work products such as code or text, verify that:

- the User has approved the final scientific content;
- the repository is at the intended commit;
- tests and automated builds pass;
- final runs use the recorded code, command, inputs, configuration, and environment;
- material outputs are present in their intended locations;
- checksums were calculated after files were complete;
- citations and public links were opened and validated;
- private data, collaborators, and unpublished project details remain within the intended boundary;
- known limitations are stated;
- the release tag or archive identifies the accepted state;
- the release decision and resulting identifiers are recorded in the Collaboration Log.

A clean software build establishes that the configured build completed. It does not establish that the scientific claims, citations, links, or outputs are correct. Those remain separate acceptance checks.

## Common failure modes and repairs

| Symptom | Likely problem | Repair |
| --- | --- | --- |
| An AI reports success, but the item cannot be found | Write occurred in the wrong location or was never made durable | Fetch the created object, verify its parent and properties, and link it from the log |
| A useful result exists only in chat | No artifact custody | Store or link the code, command, inputs, outputs, and interpretation in the designated durable location |
| A commit exists, but its scientific purpose is unclear | Repository state is disconnected from project state | Link the commit from a Notion record containing purpose, evidence, review, and next action |
| A review appears perpetually open | Review-routing field was not reconciled | Record the review, update status and next action, then clear the reviewer's own field |
| An approved item changes materially | Approval applies to an obsolete version | Clear prior approvals and request review of the new version |
| An assistant overlooks an important upstream decision | Context was stored but not selected | Name the governing record, commit, result, and dependency explicitly in the assignment |
| An assistant loses focus after reading too much | Context was loaded indiscriminately | Reduce the assignment to the task-relevant context subset |
| A repository action is attributed only to the User | AI action used a User-authenticated integration | Record the initiating participant and action path in the Collaboration Log |
| A checksum no longer matches | It was computed before the file was final or the file later changed | Rebuild the final artifact, compute the checksum afterward, and update the release record |
| A citation resolves but does not support the sentence | Bibliographic identity was mistaken for claim validation | Read the primary source, correct the claim or citation, and record the validation |
| Parallel workstreams drift apart | Current-state map and dependencies were not updated | Perform project-wide reassessment and realign hypotheses, records, tasks, roles, and acceptance criteria |

## Recommended adoption sequence

A new group does not need to implement every optional field on the first day. A practical adoption sequence is:

1. pilot the system on one bounded public or synthetic task;
2. establish User authority, the log, Project Overview page, repository custody, and handoff rule;
3. complete one full task-review-acceptance cycle;
4. test read-back of workspace and repository writes;
5. verify that a new chat session can resume from the handoff without reconstructing the project from conversation history;
6. add approval, deliberation, checksums, citation ledgers, artifact stores, and additional fields as project risk and duration increase;
7. freeze the schema and export the record before performing any quantitative analysis of the workflow itself.

The goal is not to maximize process. The goal is to preserve enough project state, artifact identity, review history, and human authority that the work remains scientifically interpretable and recoverable beyond any one chat window.

## Quick setup checklist

Before beginning substantive work, confirm:

- [ ] A human User has explicit scientific, privacy, merge, and release authority.
- [ ] Agent A and Agent B are named and their initial roles are stated.
- [ ] The work contract is available to every participant.
- [ ] The Project Overview page identifies what governs now.
- [ ] The Collaboration Log contains review-routing and approval fields.
- [ ] The repository and protected execution environment are identified.
- [ ] Repository credentials and private data remain under User or institutional control.
- [ ] The first task is bounded and has an acceptance condition.
- [ ] The relevant upstream context is named explicitly.
- [ ] A reciprocal reviewer and review type are assigned.
- [ ] The artifact-custody and checksum rules are understood.
- [ ] A handoff trigger and release gate are defined.