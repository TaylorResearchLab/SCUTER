# SCUTER quick start

For most users, "download SCUTER" means **download one `.skill` file and upload that file into your AI application**. You do not need to build SCUTER from source.

## 1. Download the SCUTER `.skill` file

Download this file to your computer:

**[Download `scuter-v0.2.1-dev.skill`](https://github.com/TaylorResearchLab/SCUTER/raw/refs/heads/main/dist/scuter-v0.2.1-dev.skill)**

The `.skill` file is a packaged set of SCUTER instructions. **Do not unzip it, rename it, or copy its contents into the chat.** Keep the downloaded file intact.

## 2. Upload that exact `.skill` file into your AI application

Use the application's interface for installing or uploading Skills. The wording varies by application and may look like **Add Skill**, **Install Skill**, **Upload Skill**, or a similar control.

Select the file you just downloaded:

```text
scuter-v0.2.1-dev.skill
```

The important step is that the AI application receives the actual `.skill` file. Merely pasting the GitHub link or the filename into a chat does not install SCUTER.

After the Skill is loaded, tell the assistant:

> Use SCUTER for this project. I am the User.

### If your AI application does not support `.skill` files

Use the **[complete Markdown instructions](https://github.com/TaylorResearchLab/SCUTER/raw/refs/heads/main/dist/scuter-v0.2.1-dev.md)** instead. Download or open that Markdown file and provide it through the application's supported project-instructions, persistent-instructions, or instruction-document mechanism.

The Markdown edition contains the same SCUTER entry instructions and companion guidance in one readable document. It is the fallback for applications that cannot install the packaged `.skill` file.

## 3. Give SCUTER the minimum project context

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

## 4. Start one bounded task

The assistant should orient to the project record and assigned context, perform the bounded work, record the evidence and next action, and stop short of accepting its own result. A second AI session can review the work. The User decides whether to accept, reject, revise, or reassign it.

For a second AI assistant, load the same SCUTER version into that application or session, provide the same project locations, and give it its own Agent instance ID and assignment. The User decides which assistant leads or reviews each work unit.

## What installing SCUTER does not do

SCUTER provides the collaboration instructions and recordkeeping protocol. It does not automatically connect an AI application to Notion, GitHub, local files, protected data, or other services, and it does not grant permissions. Available integrations and access must be configured by the User in the application being used.

For the complete setup and operating cycle, see the [implementation guide](docs/implementation-guide.md) and [protocol](protocol/01.work-contract.md).
