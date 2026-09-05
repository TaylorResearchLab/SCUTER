# Implementation notes: prospective provenance and interpretation

The retrospective study outlined here was not designed to capture the exact model identity or exposure state for every historical action because those variables were not recorded prospectively. A new implementation should avoid reproducing that limitation.

## Add session and model identity to the Collaboration Log

In addition to the minimum fields listed in Step 3, add the following fields when model attribution or review independence may matter:

| Field | Suggested type | Purpose |
| --- | --- | --- |
| Session and model identity | Text | Named session, provider, model, and displayed version when available |
| Exposure status | Select or checkbox | Whether the acting session had already seen another participant's relevant output |

Record the identity shown by the product at the time of action. When an exact model or connector version is unavailable, record that it was unavailable rather than inferring it retrospectively. Exposure status should likewise be recorded when the action occurs. Timestamps may show that exposure was possible, but they do not establish what information was actually present in a session.

## Interpret context-loading effects cautiously

The evaluated workflow showed an association between broad context loading and reduced focus on a bounded task, but it did not establish a causal mechanism. Treat selective context assembly as an operational strategy to be tested in the adopting project. When an assistant appears less focused after receiving extensive context, narrow the assignment to the task-relevant context subset, compare the resulting work, and record whether performance improves. Do not describe the association as a general property of all models or future systems.
