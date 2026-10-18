# Project Agent 007 — Workspace Blueprint

## Purpose
Build a safe, modular workspace inside Mini Mailbox to help Agent 007
organize research, preserve project knowledge, develop code, test changes,
and collaborate with the user and ChatGPT.

## 1. Backpack
The Backpack is a collection area for:
- Research findings and their sources
- Tools and possible integrations
- Ideas and hypotheses
- Reusable code modules
- Test results and evidence
- Agent messages and review notes
- Unfinished investigations and next steps

Items should be searchable, categorized, and retrievable later.

## 2. Clipboard
The Clipboard is a development workspace for:
- Drafting and revising code
- Assembling reusable modules
- Recording proposed changes and their purpose
- Preparing previews when practical
- Running isolated tests
- Recording actual results, failures, and uncertainties
- Preparing changes for user review

A proposed change must not automatically become a live change.

## 3. Persistent Memory
Project decisions, approved notes, research, and investigation progress
should survive browser refreshes and future sessions.

The design should support reviewing, correcting, exporting, and deleting
saved information.

Secrets, API keys, and private credentials must never be stored in public
source code or committed to the repository.

## 4. Knowledge Graph
Connect related:
- Research findings
- Sources
- Tools
- Ideas
- Code modules
- Tests
- Decisions
- Projects and investigations

Connections should be meaningful and useful for retrieving information.

## 5. Trinity Collaboration
The three participants are:
- User: provides goals, ideas, direction, and final approval
- Agent 007: investigates, builds, and tests
- ChatGPT: independently reviews reasoning, code, risks, and test plans

Record agreements, disagreements, evidence, and unresolved questions.
Agreement alone does not prove a proposal is correct.

## 6. Review and Safety
Before a consequential change is approved, present:
- The objective
- Files affected
- Proposed implementation
- Expected result or preview when practical
- Risks and alternatives
- Tests performed and their actual results
- Remaining uncertainties

The user retains final approval for consequential changes.

## 7. Constant Heart Principle
Preserve CONSTANT_HEART.md.

Core principles include compassion, honesty, respect for life,
avoiding unnecessary harm, and protecting the user's work.

Identity principles, editable memory, and available capabilities must remain
distinct. Changes to core principles require explicit user approval.

## 8. Voice Communication
Add voice controls directly inside the Mini Mailbox webpage:
- Microphone control for speech-to-text
- Speaker control for reading Agent 007 replies aloud
- Clear status messages and useful error handling

The user should be able to review dictated text before sending it.

## 9. Development Roadmap
1. Establish the Workspace interface.
2. Add Backpack and Clipboard sections.
3. Build persistent storage with appropriate access controls.
4. Add searchable research and investigation records.
5. Connect records through the Knowledge Graph.
6. Add voice communication.
7. Build the Trinity review workflow.
8. Test each feature before proposing integration into the live app.

## 10. Development Rules
- Work on the agent007-backpack-clipboard branch.
- Preserve existing working code and web-search capability.
- Do not deploy unreviewed changes to the live service.
- Never claim a test passed unless it was actually performed.
- Document important decisions and unresolved issues.
