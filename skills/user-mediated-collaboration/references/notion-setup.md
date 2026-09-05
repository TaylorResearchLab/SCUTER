# Notion bootstrap and MCP operating notes

This file covers standing up the durable-record infrastructure in Notion and the empirically confirmed behaviors of the Notion MCP connector. The behaviors listed here were established by direct testing during the workflow's development; they are not documented in the connector's tool descriptions, and ignoring them produces silent failures (pages landing outside databases, properties not set) that only read-back verification catches.

## What to create, in order

Confirm with the User before creating anything, and confirm the parent workspace or teamspace location. Under `USER-AUTHORITY`, infrastructure location is the User's decision.

1. **Project Overview page** — a plain Notion page recording: the accepted scientific question, current assumptions, accepted commit, authoritative configuration, current outputs, unresolved limitations, and prior art. This is the reorientation anchor: it is what a participant reads before resuming a paused workstream.
2. **Collaboration Log** — a Notion database. Use the canonical field order below.
3. **Search record** — a Notion database (or a delimited file in the code repository, if the User prefers): proposition searched, terms, databases, dates, candidate dispositions, and searches that returned nothing. Null results are recorded with the same detail as hits — they are a deliberate internal resource.
4. **Citation ledger** — a structured database (or delimited file in the manuscript repository). It is a project record, not a bibliography: it stores which statement each reference supports, validation status, who checked and when, and dispositions of candidates not retained. It does not duplicate metadata the manuscript build system resolves from identifiers (e.g., Manubot).
5. **Numbered notebooks** — created as needed, as Notion pages, for extended methods and reasoning that do not fit one log entry.

## Collaboration Log field schema

Core field order (from `DURABLE-RECORD`):

1. Entry (title)
2. Created time (created_time)
3. Date (date)
4. Owner (select or multi-select: e.g., User, Agent A, Agent B)
5. Assignment to (multi-select)
6. Needs Agent A Review (checkbox)
7. Needs Agent B Review (checkbox)
8. Needs User Review (checkbox)
9. Approved by Agent A (checkbox)
10. Approved by Agent B (checkbox)
11. Approved by User (checkbox)
12. Status (select: e.g., Proposed, Needs Review, In Revision, Accepted, Superseded, Parked)
13. Source (text or multi-select)
14. Next Action (text)
15. Summary (text)
16. Topic (select; include `Deliberation` as an option)
17. Type (select: e.g., Decision, Implementation, Review, Run Result, Correction, Supersession, Handoff, Citation Validation, Prior-Art Search)
18. Reference links (url or text)
19. Repository (text)
20. Commit SHA (text)
21. Purpose (text)
22. Subproject (select)

Optional additional fields: timestamp, lock state, review response, branch or pull request, commit date, session and model identity, exposure status. Session/model identity and exposure status are worth including from the start — they are recorded at the time of an action because they are not recoverable afterward.

Rename "Agent A" / "Agent B" fields to the participant names the User designates.

## Confirmed Notion MCP behaviors

These were confirmed empirically. Treat them as required practice, not suggestions:

- **`notion-create-pages` requires an explicit `parent` with `data_source_id`**, or created pages land outside the target database. Passing a database page ID as parent is not sufficient.
- **Moving a page uses `notion-move-pages` with `new_parent`.** Do not attempt moves through page updates.
- **Boolean (checkbox) schema fields are set with the string values `'__YES__'` and `'__NO__'`**, not true/false.
- **`notion-update-page` uses `update_properties` as the command, with a flat properties dict.**
- **Read-back verification is required after every write.** A success response is provisional. After every create, update, or move: fetch the object and check (a) the parent location and (b) the structured property values, separately. Only after read-back is the action treated as complete and recordable. This is `DURABLE-RECORD` item 3 and it exists because success responses have been observed to mislead.

## Multi-platform note

Only one AI participant holds a live Notion connection per platform session; collaboration between AI participants is asynchronous through the shared log, mediated by the User. Do not assume another participant has seen anything that is not in the log. A result held only in one participant's conversation is not a project artifact.
