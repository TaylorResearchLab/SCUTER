# Setting up a SCUTER record in Notion

Confirm the intended workspace and parent page with the User before creating records. Use the actual tool schemas available to the current session; connector names and accepted parameters can vary.

Create a Project Overview, one Collaboration Log, a prior-art search record, and a citation ledger. Add numbered notebooks for longer methods and analyses as needed. The Overview states what currently governs. The log preserves material actions, evidence, decisions, and next steps.

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
