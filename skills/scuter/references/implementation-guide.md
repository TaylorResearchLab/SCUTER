# SCUTER implementation guide

SCUTER provides a concrete protocol for collaborative AI research under the scientist's direction. Start with one bounded task and a manageable record. Adapt the setup deliberately as the project develops.

## 1. Define the research and acceptance criteria

Record the scientific objective, questions, relevant background resources, assumptions, and intended outputs. Identify the human User, each AI participant, the tools available to each, and where execution will occur. Decide which information each participant may access and what may be supplied to external services.

Specify what evidence would justify accepting the first task. For a script, this might include inspected source, a recorded test input, expected output, and an executed test. For a literature claim, identify the supporting source, the exact assertion, and the required second check. State what remains outside the task.

## 2. Establish the shared record

Create a Project Overview and one Collaboration Log. Use the Overview for the current scientific question, assumptions, accepted artifacts, unresolved limitations, and relevant prior work. Use the log for material actions and decisions. Extended methods and analyses belong in linked notebooks. Versioned source and outputs belong in suitable file stores with exact paths and identifiers recorded in the log.

Give each participant the same project locations. Verify that they can retrieve the intended artifacts. A link, attachment description, or success message is not evidence that another participant can access a file.

The [Notion setup guide](notion-setup.md) provides a practical schema. The protocol's S6 section provides a worked record. Using multiple filtered views of a log does not require multiple copies of the records.

## 3. Adopt the protocol and introduce the participants

Read and adapt the [work contract](protocol.md). Its S8 template records project-specific roles, locations, scope, evidence classes, acceptance criteria, and release requirements. Select a prior-art search coverage declaration and record it. Maintain the search record separately from the claim-specific citation ledger.

Supply the Skill through a supported installation mechanism, or provide the complete Markdown instruction edition. Confirm that the assistant can read the entry instructions and companion protocol, guidance, and templates. The User still supplies permissions, project locations, and each transition between participants. Installing instructions does not create service connections.

At the start of a session, ask the assistant to identify the governing protocol, current objective, assignment, available tools, and any missing resources. Record its displayed identity when available. Do not infer unexposed model or connector versions.

## 4. Run the task-review-acceptance cycle

| Stage | Action and record |
| --- | --- |
| Assign | The User specifies the work, lead, reviewer, upstream artifacts, constraints, and acceptance criteria. |
| Orient | The lead reads the governing record and identifies missing or conflicting context. |
| Produce | The lead supplies the proposed artifact and records evidence, limitations, and exact file locations. |
| Test and version | Test in the appropriate environment. Preserve the code, command, inputs, outputs, configuration, and source revision. |
| Review | Another participant examines the actual artifact and evidence against the acceptance criteria. |
| Resolve | Repair defects, rerun affected checks, and record unresolved disagreements for the User. |
| Accept | The User evaluates the evidence and determines the disposition. |
| Synchronize | Update the Overview, accepted artifact links, log status, and next task together. |

Review may precede execution when a proposed action warrants inspection first. A sandbox demonstration must retain that evidence label. A commit identifies a file state, not a validated result. A checksum identifies completed bytes, not scientific correctness.

The User determines who acts next. Lead and review roles may reverse. Multiple successive actions by one participant do not require artificial alternation or imply greater scientific contribution.

## 5. Maintain evidence and review state

Record what a reviewer inspected, the specific version, what is supported, what remains uncertain, and any required repair. Keep dated review text as the historical evidence. Review-request checkboxes route current work; approval fields record endorsement of the current version.

Each reviewer clears only their own review request after recording a response. A material revision requires reconsidering prior approvals. Record whether the reviewer had already seen another participant's output. Sequential checks remain useful but are not independent confirmation.

After every shared-record or repository write, retrieve the result. Check its location and structured properties separately. After transferring an artifact, confirm access from the receiving context. See [record and review guidance](record-and-review.md).

## 6. Reorient when the science changes

New evidence can change the hypothesis, interpretation, required validation, or project direction. The User determines what those changes mean for the project. Update affected assumptions, dependencies, assignments, and acceptance criteria before continuing.

Use task-relevant context rather than routinely loading the entire record. The User identifies the relevant upstream notebooks, decisions, inputs, and results. The assistant should report contradictions or missing dependencies instead of silently choosing a convenient interpretation.

## 7. Prepare a handoff

Create a handoff when work pauses, a substantial unit ends, a new participant takes over, or the User requests one. Include accepted state, completed work, exact files and revisions, execution evidence including failures, open questions, superseded work, limitations, and one next action with an owner and acceptance criterion. Use S7 of the protocol.

Compare the handoff with the Overview, log, and repository. Ask whether any hard-won constraints or rejected approaches were omitted. The receiving session checks those same sources before resuming. A concise summary should not erase the evidence needed to verify it.

## 8. Release deliberately

The User determines release readiness. Check the agreed scientific, citation, prior-art, execution, artifact, and disclosure requirements. Preserve completed outputs, their identities, and unresolved limitations. Record the decision and exact released revision.

A build result is evidence about that build only. Package acceptance is evidence about that installation attempt only. Treat ease of adoption, protocol adherence, and scientific effectiveness as separate questions requiring appropriate evaluation.
