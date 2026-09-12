# SCUTER quick start

For most users, "download SCUTER" means **download one `.skill` file and upload that exact file into your AI application**. In applications that accept `.skill` files as chat attachments, this can be as simple as dragging the file directly into the chat. You do not need to build SCUTER from source.

## 1. Download the SCUTER `.skill` file

Download this file to your computer:

**[Download `scuter-v0.2.2-dev.skill`](https://raw.githubusercontent.com/TaylorResearchLab/SCUTER/951c46b63133dfc67dd5bdf3ac56dd62691fe613/dist/scuter-v0.2.2-dev.skill)**

The `.skill` file is a packaged set of SCUTER instructions. **Do not unzip it, rename it, or edit its contents.** Keep the downloaded file intact.

If clicking the link does not immediately download the file, use your browser's **Save Link As...** command and save it with this exact filename:

```text
scuter-v0.2.2-dev.skill
```

## 2. Upload that exact `.skill` file to the AI assistant

If the application accepts `.skill` files as chat attachments, **upload or drag `scuter-v0.2.2-dev.skill` directly into the chat**. For applications such as ChatGPT or Claude where this is supported, that may be all that is required for the assistant to recognize and use the Skill.

Some applications instead provide a dedicated interface for Skills. In that case, use **Add Skill**, **Install Skill**, **Upload Skill**, or the application's equivalent control and select the same file:

```text
scuter-v0.2.2-dev.skill
```

The important step is that the AI assistant receives the actual `.skill` file. Merely pasting the GitHub link or filename into the chat is not the same as uploading the file.

After the Skill is loaded, tell the assistant:

> Use SCUTER for this project. I am the User.

### If your AI application does not support `.skill` files

Use the **[complete Markdown instructions](https://raw.githubusercontent.com/TaylorResearchLab/SCUTER/951c46b63133dfc67dd5bdf3ac56dd62691fe613/dist/scuter-v0.2.2-dev.md)** instead. Download or open that Markdown file and provide it through the application's supported project-instructions, persistent-instructions, or instruction-document mechanism.

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
