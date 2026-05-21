# AI-Assisted Work Plan - ADD Project

## 3.1 Title block

**Document title:** AI-Assisted Work Plan - ADD Project  
**Student ID:** s34538  
**Student name:** Enes Gezici  
**Last updated:** 2026-05-21  
**Course:** Analysis of Large Data Sets (ADD)  
**Repository:** https://github.com/Enes-Gezici-PJATK/s34538_kafka  

This document describes how I will use AI tools during the ADD project and the Phase 2 additional assignments. The goal is to use AI as a helper for planning, debugging, documentation, command conversion and code review. AI output will not be submitted blindly. Every generated command, code block, configuration file and explanation must be checked, tested and adapted to the real repository before it is committed.

## 3.2 Scope of AI use in this project

| Activity | Allowed? | Notes |
|---|---:|---|
| Boilerplate code and CLI scaffolding | Yes | AI may suggest simple scripts, commands and folder structure. |
| React and Vite UI code | Yes | AI may help with components, state handling and build errors. |
| Kafka/SSE stock application logic | Yes | AI may explain connection flow and error handling, but I must test locally. |
| History viewer/downloader app | Yes | AI may help with UI, fetch logic and documentation. |
| Local anonymizer development | Limited | AI may help during development, but the anonymizer must run locally without AI at runtime. |
| Runtime anonymization | No | The anonymizer must not call AI, LLMs, HTTP APIs or external services while masking data. |
| Debugging error messages | Yes | AI may explain terminal errors and suggest fixes. |
| README and documentation | Yes | AI may draft text, but I must edit it to match the real repository. |
| Architecture planning | Yes | AI may suggest folder maps and workflow diagrams. |
| Secrets, API keys and .env contents | No | These must never be pasted into AI tools or committed. |
| Exam or restricted individual work | Per course rules | AI use must follow course rules and cannot replace my own understanding. |

## 3.3 Tools and models

I plan to use ChatGPT as my main AI chat assistant. It is useful for understanding assignment requirements, preparing checklists, converting Linux commands into Windows PowerShell commands, debugging Git, Node, npm and Vite errors, and drafting documentation. Because ChatGPT is a cloud tool, I will not paste API keys, passwords, real `.env` files, private credentials or real personal data into it.

I may also use GitHub Copilot or IDE autocomplete for small code suggestions. This can help with React, JavaScript, TypeScript and Python syntax. However, Copilot suggestions will be treated as drafts, not final code. I must review imports, package names, file paths and logic before using them.

For verification I use local tools such as Git, Node.js, npm, Python and PowerShell. These tools are not AI tools, but they are the final proof that the project works. If AI says that something is correct but the local build fails, the local build result is more important.

## 3.4 Standard workflow

1. I start with a short human specification that describes the goal, input files, output files, constraints and expected result.
2. I provide AI only the minimum required context, such as the exact error message, file path, package script or small code snippet.
3. For risky changes, I ask AI for a plan first. I do not immediately ask it to rewrite large parts of the project.
4. I ask for commands that match my environment. In this repository I mainly use Windows PowerShell.
5. I apply the suggested change manually and inspect files before committing.
6. I run the relevant local command. For the anonymizer, I run the Python command with `examples/mapping.json`. For stock apps, I run `npm install` and `npm run build`.
7. I update documentation when paths or commands change.
8. I check `git status` and `git diff --check`.
9. I verify that no `.env` file, API key, password, token or cloud credential is staged.
10. I commit with a meaningful message and push to the correct repository: `s34538_kafka` on `main`.

## 3.5 Prompting rules

- Always include the real folder path, for example `anonymizer/`, `realtime-dashboard/` or `history-viewer/`.
- Always state the operating system and shell when asking for commands.
- Always paste the exact error message when debugging.
- Ask for minimal changes instead of unnecessary restructuring.
- Ask AI not to rename folders unless the assignment requires it.
- Include the rule that secrets must not be committed.
- Include the AA1 rule that the anonymizer must not call AI or HTTP services at runtime.
- Ask for commands that can be run from the repository root.
- Ask for verification commands after every important change.
- Require error handling for missing files, missing dependencies and wrong paths.
- Ask AI to avoid invented libraries, endpoints or CLI flags.
- If AI is unsure, it should say so instead of guessing.

## 3.6 Precautions and prohibited uses

1. I must never paste real API keys, passwords, tokens, `.env` contents or cloud credentials into AI tools.
2. I must not upload real personal data to AI tools. I will use fictional examples or public datasets.
3. I must never merge AI output without running it locally.
4. I must verify commands, CLI flags, package names and framework APIs when needed.
5. I must not let AI rewrite unrelated files.
6. I must not let AI add features outside the assignment specification.
7. I must keep testing evidence such as build logs, screenshots or sample outputs.
8. I must remain able to explain the code and commands during grading.
9. I must not use AI in restricted exam conditions unless allowed by the course.
10. I must stop using AI and inspect manually if there is a possible secret leak or data leakage issue.
11. I must not commit fake screenshots.
12. I must not hardcode API keys in React, Python, documentation or configuration files.
13. I must not accept invented endpoints or fake external services from AI.
14. I must review AI-generated documentation so it matches the real repository.
15. I must keep the anonymizer local-only at runtime.

## 3.7 Task-specific AI plans

### AA1 - Local Data Anonymizer

What I will ask AI to do:

- Explain Python errors.
- Suggest README improvements.
- Check whether commands work after moving files into `anonymizer/`.
- Suggest verification commands using `examples/mapping.json`.

What I will do myself:

- Run the anonymizer locally.
- Check sample input and output.
- Confirm that no AI or HTTP call is used at runtime.
- Check that screenshots are real.

Definition of done:

- The anonymizer is in `anonymizer/`.
- The documented command runs from the final repository.
- Sample files produce anonymized output.

### AA2 - Realtime Dashboard

What I will ask AI to do:

- Help debug npm, Vite and React errors.
- Explain API or SSE connection errors.
- Suggest safe environment variable handling.
- Improve quick-start documentation.

What I will do myself:

- Run `npm install`.
- Run `npm run build`.
- Start the dev server when needed.
- Check that no API key is hardcoded.

Definition of done:

- `realtime-dashboard/` builds successfully.
- README explains how to run it.
- Secrets are not committed.

### AA2 - History Viewer

What I will ask AI to do:

- Help debug the Vite build.
- Help document that `history-viewer` is the history/downloader app.
- Suggest Windows PowerShell commands.
- Review quick-start instructions.

What I will do myself:

- Run `npm install`.
- Run `npm run build`.
- Check package scripts.
- Verify that `node_modules/` and `dist/` are not committed.

Definition of done:

- `history-viewer/` builds successfully.
- Folder name remains documented correctly.
- No secrets are committed.

### AA3 - Unified Repository

What I will ask AI to do:

- Help plan the merge from `s34538_anonymize` into `s34538_kafka`.
- Convert Linux commands such as `rsync` into PowerShell.
- Draft consolidation notes.
- Check whether the final layout is clear.

What I will do myself:

- Copy files into the repository.
- Run Git commands.
- Check `git status`.
- Commit and push to `main`.

Definition of done:

- `s34538_kafka` contains AA1 and AA2 on `main`.
- `consolidation/CONSOLIDATION.md` explains the merge.
- The final submission repository is not the old anonymizer repository.

### AA4 - AI Work Plan

What I will ask AI to do:

- Draft the required sections 3.1 to 3.10.
- Suggest project-specific precautions.
- Suggest checklist items.
- Improve English wording.

What I will do myself:

- Edit the plan to match my real workflow.
- Add the real repository URL.
- Remove generic or false statements.
- Confirm that the disclosure is honest.

Definition of done:

- `documentation/ai-work-plan.md` exists.
- It contains all required sections.
- It includes scope, workflow, prompting rules, precautions, task-specific plans, disclosure, checklist and revision log.

## 3.8 Disclosure: how this document was produced with AI

This document was produced with help from ChatGPT. I used ChatGPT to understand the Phase 2 requirements, organize the final repository layout and draft the first version of this AI-assisted work plan. At a high level, I asked for help with merging my AA1 anonymizer repository into my AA2 Kafka repository, keeping the final repository name as `s34538_kafka`, preparing a root README, writing consolidation notes and creating an AA4 work plan with the required sections.

I manually reviewed the generated text and adjusted it to match my real repository. For example, I kept the folder name `history-viewer` instead of renaming it to `history-downloader`, because that is the name used in my AA2 repository. I also changed the workflow to mention Windows PowerShell because that is the terminal I used during consolidation.

I rejected suggestions that created unnecessary folder renames or extra restructuring. I also rejected any approach that would commit real secrets or fake screenshots. AI helped me draft and debug, but I am responsible for the final files, commands and submitted repository.

## 3.9 Review checklist before every commit

- [ ] I ran the anonymizer command if I changed anything under `anonymizer/`.
- [ ] I ran `npm run build` for `realtime-dashboard/` if I changed the realtime app.
- [ ] I ran `npm run build` for `history-viewer/` if I changed the history app.
- [ ] I checked `git status`.
- [ ] I checked `git diff --check`.
- [ ] I verified that no `.env` file is staged.
- [ ] I verified that no API key, password, token or cloud credential is staged.
- [ ] I checked that README paths match the real folder names.
- [ ] I confirmed that screenshots are real.
- [ ] I used a meaningful commit message.
- [ ] I pushed to `s34538_kafka` on `main`.

## 3.10 Revision log

| Date | Version | Change |
|---|---:|---|
| 2026-05-21 | 0.1 | Initial AI-assisted draft created for Phase 2. |
| 2026-05-21 | 1.0 | Added project-specific folders, precautions, workflow and disclosure. |
