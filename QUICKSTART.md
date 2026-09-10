# SCUTER quick start

You do not need to build SCUTER before using it.

## 1. Give SCUTER to your AI application

If your application supports Skill packages, download and install or attach the [SCUTER Skill package](dist/scuter-v0.2.1-dev.skill?raw=true) using the application's supported mechanism.

If it does not support Skill packages, use the [complete Markdown instructions](dist/scuter-v0.2.1-dev.md?raw=true) as project instructions, persistent instructions, or an attached instruction document, as supported by the application.

Then tell the assistant:

> Use SCUTER for this project. I am the User.

## 2. Give it the minimum project context

Provide the information SCUTER cannot know on its own:

```text
Project: [NAME]
Scientific objective: [QUESTION OR GOAL]
Shared project record: [LOCATION]
Versioned repository or artifact store: [LOCATION, IF USED]
Private/protected data location: [LOCATION OR NONE]
Your Agent instance ID: [PROJECT-SPECIFIC CHAT LABEL]
First task: [BOUNDED ASSIGNMENT]
Acceptance criteria: [WHAT THE USER REQUIRES BEFORE ACCEPTING THE RESULT]
```

If you do not yet have a shared project record, ask the assistant:

> Help me create the minimum SCUTER setup for this project.

SCUTER can use Notion and GitHub, as in the companion study, but neither is required. Use durable record and version-control tools appropriate for your project.

## 3. Start one bounded task

The assistant should orient to the project record and assigned context, perform the bounded work, record the evidence and next action, and stop short of accepting its own result. A second AI session can review the work. The User decides whether to accept, reject, revise, or reassign it.

For a second AI assistant, give it the same SCUTER version and project locations, but assign it its own Agent instance ID and task. The User decides which assistant leads or reviews each work unit.

## What installing SCUTER does not do

SCUTER provides the collaboration instructions and recordkeeping protocol. It does not automatically connect an AI application to Notion, GitHub, local files, protected data, or other services, and it does not grant permissions. Available integrations and access must be configured by the User in the application being used.

For the complete setup and operating cycle, see the [implementation guide](docs/implementation-guide.md) and [protocol](protocol/01.work-contract.md).
