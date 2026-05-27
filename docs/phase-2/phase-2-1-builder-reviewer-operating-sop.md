# Phase 2.1 — Builder / Reviewer Operating SOP

**Status:** CLOSED
**Phase:** 2.1
**Builder:** Claude Code (AGT-02)
**Date:** 2026-05-28
**Branch:** main
**Previous Phase:** 1.7 — First Manual Content Pack Test (CLOSED, commit: 7061560)

---

## Purpose of Phase 2

Phase 1 established the brand, content, approval, and content-pack foundations for Vị Cuốn Growth OS. Every artifact was documentation and schema only — no live automation.

Phase 2 formalizes how the AI agents collaborate so that future phases can be built and reviewed faster, with less manual copy-paste and screenshot debugging from the Owner. The goal is a repeatable, auditable workflow where each agent knows exactly what it owns, what it may not touch, and how to hand off cleanly to the next agent.

Phase 2 does NOT activate n8n, does NOT post to any platform, and does NOT interact with real customers.

---

## Agent Roles

| ID | Agent | Role | Owns | Must Not Do |
|----|-------|------|------|-------------|
| USER | Owner | Final approver | Approve phases, publish outputs, spend money | None — Owner has full authority |
| AGT-01 | ChatGPT / Chief Architect | System design and phase planning | Write Builder prompts, phase specs, task contracts, architecture decisions | Directly edit repo files; bypass Owner approval |
| AGT-02 | Claude Code / Builder | Implementation | Create/edit repo files; run local checks; commit after OWNER_APPROVED | Hardcode secrets; auto-post; auto-reply to real users; activate n8n workflows; commit before OWNER_APPROVED |
| AGT-03 | Codex / Reviewer | Code and doc review | Review diffs; return REVIEW_PASS or REVIEW_CHANGES_REQUESTED; flag blockers | Rebuild Builder output; make edits to reviewed files; approve own work; commit or push |
| AGT-04 | Gemini | Content and multimodal | Draft content, design briefs, creative prompts from approved inputs | Publish or message customers directly |
| AGT-05 | n8n / Runtime | Workflow automation | Execute approved, imported workflows after Owner enables them in Phase 3+ | Self-activate; make approval decisions; run in Phase 2 |
| AGT-06 | GitHub / Source of Truth | Version control and audit | Store all versioned files, diffs, commits, and history | Store real API keys, tokens, or passwords |
| AGT-07 | LangGraph / Chief Orchestrator | Future multi-agent coordination *(not active in Phase 2)* | Coordinate handoff between ChatGPT, Builder agents, Reviewer agents, n8n runtime, logs, and approval gates — activates in a later phase | Make approval decisions; bypass Owner; activate workflows |

Reference: `agents/AGENT_REGISTRY.md`

---

## Future Orchestration Layer — LangGraph (NOT Active in Phase 2)

LangGraph will eventually serve as the Chief Orchestrator for FnB OS V1, replacing the current manual handoff model. It is documented here for awareness only. No LangGraph implementation is required in Phase 2.1 or any Phase 2 sub-phase.

**What LangGraph will do when activated:**
- Coordinate the full multi-agent handoff pipeline: ChatGPT (planning) → Claude Code (building) → Codex (reviewing) → Owner gate → n8n (execution)
- Route tasks to the correct agent based on task type (build / review / approve / execute)
- Track phase state across sessions so agents do not need to re-read `handoff/SESSION_SUMMARY.md` manually
- Connect to approval gates, log entries, and n8n workflow triggers as a single orchestration surface
- Enforce the 10-turn session cap at the infrastructure level

**What LangGraph will NOT do:**
- Make approval decisions — Owner approves
- Override the blocker policy
- Bypass Codex review

**Current state (Phase 2):** All handoff steps in the Standard Handoff Flow below are done manually by the Owner copy-pasting between agent sessions. LangGraph replaces this manual routing in a future phase.

---

## Standard Handoff Flow

Every phase follows this exact sequence. No steps may be skipped.

```
Step 1 — ChatGPT writes the Builder prompt
         - Includes: PHASE_ID, GOAL, SCOPE, FILES_TO_CREATE_OR_UPDATE,
           DO_NOT_TOUCH, ACCEPTANCE_CRITERIA, SELF_CHECK_COMMANDS
         - Uses template: docs/phase-2/prompt-templates/claude-builder-phase-template.md

Step 2 — Owner delivers the prompt to Claude Code Builder
         - Owner pastes the prompt into the Claude Code session
         - Owner does NOT need to debug or interpret the prompt

Step 3 — Claude Code builds scoped files
         - Works only within stated scope
         - Creates or edits files one at a time
         - Does not add features beyond the command

Step 4 — Claude Code self-checks
         - Runs git status --short
         - Confirms .claude/ is NOT staged
         - Scans for secret patterns: api_key, token, password, secret, sk-, xox
         - Confirms all output files are non-empty
         - Checks every ACCEPTANCE_CRITERIA item: PASS or FAIL

Step 5 — Claude Code posts Builder Report
         - Reports in the exact format defined in this document (see below)
         - Lists all changed files, risks, test notes, and safety checks
         - Does NOT commit yet

Step 6 — Codex reviews only
         - Owner delivers Builder Report + changed files to Codex
         - Uses template: docs/phase-2/prompt-templates/codex-reviewer-phase-template.md
         - Codex reads every scoped file and checks all criteria

Step 7 — Codex returns verdict
         - REVIEW_PASS — all criteria met, no blockers
         - REVIEW_PASS_WITH_NOTES — all criteria met, minor non-blocking observations
         - REVIEW_CHANGES_REQUESTED — one or more criteria failed; Builder must fix

Step 8 — Claude Code fixes (only if REVIEW_CHANGES_REQUESTED)
         - Fixes only the issues listed by Codex
         - Does not refactor or extend beyond the fix
         - Re-runs self-check
         - Re-posts Builder Report

Step 9 — Owner approves (only after REVIEW_PASS or REVIEW_PASS_WITH_NOTES)
         - Owner reviews Builder Report and Codex verdict
         - Owner says: "APPROVED — commit and push" or equivalent
         - Owner does NOT need to inspect individual file diffs

Step 10 — Claude Code commits and pushes
          - Only after explicit Owner approval
          - Commits with the suggested commit message
          - Pushes to main (or specified branch)
```

---

## Builder Rules (Claude Code)

1. **Read the entire prompt before writing any file.** State the phase ID and scope in your first output line.
2. **Lock scope explicitly.** List every file you will touch before touching anything.
3. **Work within scope.** If you discover you need a file not in scope, stop and report — do not proceed.
4. **One file at a time.** State what you did and why after each file.
5. **No secrets.** Use placeholder text for all credentials, keys, tokens, or passwords. Example: `[YOUR_API_KEY]`, `[FILL_BEFORE_USE]`.
6. **No production automation.** Do not create n8n workflows with `"active": true`. Do not write code that auto-posts, auto-replies, or spends money.
7. **No unsolicited refactors.** A bug fix fixes the bug. A doc phase creates docs. Do not clean up surrounding files.
8. **Run self-check before reporting.** Every item in the self-check must be explicitly addressed.
9. **Do not commit without OWNER_APPROVED.** Even after REVIEW_PASS, wait for Owner's explicit instruction.
10. **Session length.** At turn 8 of 10, update `handoff/SESSION_SUMMARY.md`. At turn 10, stop and write final status.

---

## Reviewer Rules (Codex)

1. **Read the original prompt and all scoped files.** Do not review from memory or summaries alone.
2. **Check every acceptance criterion explicitly.** State PASS or FAIL with a specific reason for each.
3. **Check scope.** List every file that was created or modified. Flag any file outside the stated scope.
4. **Check for secrets.** Scan for: `api_key`, `token`, `password`, `secret`, `sk-`, `xox`, `AIza`, `ghp_`, `ya29.`. Any real value → FAIL.
5. **Check for role conflicts.** Did the Builder commit? Did the Builder self-approve? → FAIL.
6. **Check for safety violations.** Did the Builder auto-post, activate a workflow, or run ads? → FAIL.
7. **Do not rebuild.** If issues are found, list them clearly. Builder fixes. Reviewer does not rewrite files.
8. **Use the exact output format** defined in this document (see below).
9. **Reviewer does not commit, push, or approve.** Only the Owner approves.
10. **Non-blocking observations** go in REVIEW_PASS_WITH_NOTES notes section — they do not block the phase.

---

## Commit and Push Rules

| Action | Who | Condition |
|--------|-----|-----------|
| Stage files | Claude Code | After self-check passes |
| Create commit | Claude Code | After OWNER_APPROVED |
| Push to remote | Claude Code | After OWNER_APPROVED, same session |
| Force push | NEVER | — |
| Commit .claude/ | NEVER | — |
| Commit .env | NEVER | — |
| Commit real secrets | NEVER | — |

**Suggested commit message format:**
```
feat(phase-X.Y): short description of what was added or changed
```

---

## Blocker vs. Warning Policy

### Blockers — Phase MUST stop immediately

A Builder session is BLOCKED if any of the following is detected:

1. **Exposed secret** — a real API key, token, password, or credential is present in any repo file.
2. **.claude/ staged or committed** — the `.claude/` directory appears in `git status` as staged or in a commit.
3. **Major scope violation** — files outside the stated scope were created or modified without Owner/ChatGPT updating the command.
4. **Production n8n workflow created** — any workflow JSON with `"active": true` was created before Owner approval.
5. **Auto-post / auto-reply / ads execution** — any code or workflow that posts to social media, messages real users, or runs paid ads was activated.
6. **Empty or useless files** — any output file is empty, contains only a title, or is unrelated to F&B / Vị Cuốn brand.

**When blocked:** Stop immediately. Set status `BLOCKED`. Record the exact reason. Notify Owner. Do not attempt to work around the blocker.

### Non-Blocking Warnings — Phase continues, noted in report

The following are warnings, not blockers:

- Metadata wording or label inconsistency
- Placeholder text like `[FILL]`, `[OWNER_CONFIRM]`, `[TODO]`
- Minor formatting inconsistency (spacing, heading level)
- Slightly imperfect file naming if the file is still usable and correctly scoped
- Duplicate information that was inherited from a template

Warnings are noted in the Builder Report and Codex Review but do not stop the phase.

---

## Session Length Policy

Every agent session has a **hard cap of 10 turns** (one turn = one user message + one agent response).

| Turn | Required Action |
|------|----------------|
| 1 | State role, phase, scope. Confirm command or prompt is understood. |
| 8 | Write or update `handoff/SESSION_SUMMARY.md` with 7 required fields. Announce remaining turns. |
| 10 | Hard stop. Do not start new work. Finalize status. Write final output. |

Reference: `agents/SESSION_LIMIT_RULE.md`

---

## Required Final Report Format — Builder

Claude Code must end every phase session with this exact structure:

```
## Phase X.X — Builder Done

### Files Created
- [exact/path/to/file.md]

### Files Modified
- [exact/path/to/file.md]

### Acceptance Criteria
| # | Criterion | Status |
|---|-----------|--------|
| 1 | [text from prompt] | PASS |

### Risks / Blockers
[none, or specific description]

### Git Status
[paste of: git status --short output]

### Safety Check
| Check | Result |
|-------|--------|
| Secrets scan | CLEAN |
| .claude/ staged | NO |
| Production n8n workflow | NO |
| Auto-post / auto-reply / ads | NO |

### Scope Check
| Check | Result |
|-------|--------|
| All files within stated scope | YES |
| Files outside scope | NONE |

### Suggested Commit Message
feat(phase-X.Y): [short description]

READY FOR CODEX REVIEW
```

---

## Required Final Review Format — Codex

Codex must end every review session with this exact structure:

```
## REVIEW RESULT: PASS | PASS_WITH_NOTES | FAIL

### Acceptance Criteria
| # | Criterion | Result | Reason |
|---|-----------|--------|--------|

### Scope Violation Check
| File | In scope? | Note |
|------|-----------|------|

### Secret Scan
Result: CLEAN / WARN
[If WARN: file name and pattern found]

### Role Conflict Check
Result: PASS / FAIL
[If FAIL: describe]

### Safety Check
Result: PASS / FAIL
[If FAIL: describe]

### Importability Check (n8n workflows only)
Result: PASS / SKIP / FAIL

### Notes (PASS_WITH_NOTES only)
[List non-blocking observations]

### Summary
[2–3 sentences]
```

If PASS or PASS_WITH_NOTES:
```
OWNER CAN APPROVE
Next: Owner says "APPROVED — commit and push" to Claude Code.
```

If FAIL:
```
RETURN TO BUILDER
Issues:
1. [exact issue with file and line if applicable]
Builder must fix and re-submit for review.
```

---

## What the Owner Should and Should Not Need to Do

### Owner DOES:
- Deliver the ChatGPT-written Builder prompt to Claude Code
- Deliver the Builder Report to Codex for review
- Read the Builder Report and Codex verdict
- Say "APPROVED — commit and push" when satisfied
- Make final go/no-go decisions on phase completion
- Handle anything involving real money, real customers, or live publishing

### Owner does NOT need to:
- Debug individual files or diff hunks
- Copy-paste file contents between agents
- Manually check for secrets or scope violations
- Write commit messages
- Decide whether a file is correctly formatted
- Translate between agents

If the Owner is doing any of the above regularly, the SOP is not being followed correctly — flag and fix the process, not the Owner's workflow.

---

## Reference Documents

| Document | Purpose |
|----------|---------|
| `agents/AGENT_REGISTRY.md` | Agent IDs and capabilities |
| `agents/AGENT_RUN_PROTOCOL.md` | Full session start/stop protocol |
| `agents/BUILDER_PROTOCOL.md` | Detailed Builder steps |
| `agents/REVIEWER_PROTOCOL.md` | Detailed Reviewer steps |
| `agents/SESSION_LIMIT_RULE.md` | 10-turn session cap rules |
| `commands/COMMAND_SHORTCUTS.md` | Active command inference shortcuts |
| `docs/phase-2/prompt-templates/claude-builder-phase-template.md` | Reusable Builder prompt template |
| `docs/phase-2/prompt-templates/codex-reviewer-phase-template.md` | Reusable Reviewer prompt template |
| `handoff/SESSION_SUMMARY.md` | Cross-session state bridge |
| `logs/AGENT_ACTIVITY_LOG.md` | Per-session activity log |
