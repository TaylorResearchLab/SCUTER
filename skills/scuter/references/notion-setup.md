# Setting up a SCUTER record in Notion

Confirm the intended workspace and parent page with the User before creating records. Use the actual tool schemas available to the current session; connector names and accepted parameters can vary.

Create a Project Overview, one Collaboration Log, a prior-art search record, and a citation ledger. Add numbered notebooks for longer methods and analyses as needed. The Overview states what currently governs. The log preserves material actions, evidence, decisions, and next steps.

## Collaboration Log fields

| Field | Suggested type | Purpose |
| --- | --- | --- |
| Entry | Title | Material event or work item |
| Created time | System time | Record-creation time |
| Date | Date | Scientific or operational date |
| Owner | Select | Responsible participant |
| Assignment to | Multi-select | Participant expected to act next |
| Needs participant review | Checkbox per participant | Current routing request |
| Approved by participant | Checkbox per participant | Endorsement of the current version |
| Status | Select | Proposed, Needs Review, Accepted, Rejected, Parked, or Superseded |
| Source | Text or multi-select | User, named assistant, run, or supplied material |
| Next Action | Text | Next task, owner, and acceptance condition |
| Summary and Purpose | Text | Result and reason for the work |
| Topic, Type, Subproject | Select fields | Classification and workstream |
| Reference links | URL or text | Governing records and evidence |
| Repository and Commit SHA | URL and text | Exact source state |
| Session/model identity | Text | Identity displayed at the time of action |
| Exposure status | Text or select | Prior relevant material seen before a review |

Use names chosen by the User for participant fields. The protocol's S6 and S8 templates supply examples. The schema is a starting point, not an obligation to create fields irrelevant to a project.

## Create and verify

Read the target database's schema before creating a row. Identify the correct data source and use the exact parent and property forms required by the current connector. Do not substitute a page identifier for a data-source identifier or guess how checkbox values are encoded.

After creating, editing, or moving a record, fetch it again. Verify both its parent location and its saved properties. For pages with child pages or databases, use narrow edits and preserve the child references unless the User has requested their removal.

Use a single underlying Collaboration Log. Label filtered views clearly, such as **Recent review queue**, and distinguish them from **Full Collaboration Log**. Different views are not separate stores, and the same action need not be copied into each.

## Maintain history and current state

Retain dated reviews and decisions in the record body. Mutable routing fields do not reconstruct past review events. Mark obsolete records as superseded when their history remains relevant, and link to the governing replacement.

After a material decision, update the Overview as well as the log. Record accepted artifacts and unresolved tasks together so the next participant can determine what governs without reconstructing it from conversation.
