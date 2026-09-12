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
