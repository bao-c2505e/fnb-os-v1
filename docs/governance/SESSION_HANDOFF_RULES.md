# Session Handoff Rules — FnB OS V1

Created By: Claude Code (Builder, AGT-02) — 2026-05-30 (Phase 22 — ECC Lite Repo Governance)
Type: Governance — Session Continuity Protocol
Scope: All AI agent sessions in this repository

---

## Purpose

These rules ensure that every AI agent session ends cleanly, that no context is lost between sessions, and that the repository is always the canonical source of truth — not screenshots, copy-paste, or agent memory.

---

## 1. Session Limit

- Each AI agent session (Builder or Reviewer) has a **maximum of 10 exchanges**.
- At **exchange 8**: Builder must update `handoff/SESSION_SUMMARY.md` and begin preparing the end-of-session output.
- At **exchange 10**: Builder must stop all new work, finalize `SESSION_SUMMARY.md`, and signal to Owner that a new session is required.
- If a task cannot be completed within 10 exchanges, it must be split into sub-phases and resumed in a new session.

---

## 2. Before Ending a Session

The Builder must complete all of the following before signaling session end:

### 2a. Update SESSION_SUMMARY.md

`handoff/SESSION_SUMMARY.md` must be updated with:

| Field | Content |
|-------|---------|
| `current_phase` | Phase name and status |
| `current_role` | Builder or Reviewer and what was done |
| `active_command` | Current command status summary |
| `latest_commit` | Last stable commit hash and message |
| `files_changed` | List of created / modified files with summaries |
| `files_pending` | Files created but not yet committed (awaiting approval) |
| `decisions_made` | Non-obvious choices made during the session (with reasoning) |
| `open_issues` | Any unresolved issues |
| `blockers` | Any blocking conditions |
| `next_owner_action` | Exact steps Owner should take next |
| `next_builder_action` | What the next Builder session should do first |
| `next_reviewer_action` | What Codex should review (if applicable) |
| `session_limit_note` | Whether turn limit was reached |
| `owner_approval_needed` | `true` or `false` |

### 2b. Update AGENT_ACTIVITY_LOG.md

`logs/AGENT_ACTIVITY_LOG.md` must have a new row prepended with:
- Time (YYYY-MM-DD)
- Agent name
- Task description (detailed — what was read, created, modified, and confirmed)
- Result
- Files changed

### 2c. Create or Update Phase Handoff File

If the phase has a specific handoff file (`handoff/PHASE_XX_HANDOFF.md`), it must be updated with:
- Phase name and objective
- Files created / updated / not modified
- Validation checklist results
- Acceptance criteria status
- Secret scan result
- No-execution confirmation
- Owner next action
- Codex review instructions (if applicable)
- Next recommended phase

### 2d. Update CURRENT_PHASE.md

`handoff/CURRENT_PHASE.md` must be updated with:
- Current phase name
- Current status (e.g., `BUILD_READY`, `PLAN_READY`, `PACK_READY`, `PUSHED`)
- Latest commit hash (if applicable)
- Next gate required

---

## 3. Starting a New Session

Every new Builder session must begin by reading these files in order:

1. `CLAUDE.md` — Project rules and identity
2. `AGENTS.md` — Agent roster confirmation
3. `commands/COMMAND_INBOX.md` — Active command
4. `handoff/SESSION_SUMMARY.md` — Latest session state
5. `handoff/CURRENT_PHASE.md` — Current phase status
6. Phase-specific handoff file (e.g., `handoff/PHASE_22_HANDOFF.md`)

Do not begin work until all 6 files are read.

---

## 4. Source of Truth Rules

| Source | Authority |
|--------|-----------|
| GitHub `main` branch | Canonical source of all committed work |
| `handoff/SESSION_SUMMARY.md` | Latest session state between commits |
| `handoff/CURRENT_PHASE.md` | Current phase status |
| `commands/COMMAND_INBOX.md` | Active commands and approvals |
| `logs/AGENT_ACTIVITY_LOG.md` | Audit trail of all agent activity |
| `09_LOGS/PHASE_LOG.md` | Phase milestone record |

**The following are NOT sources of truth:**
- Screenshots (Owner provides these for evidence; they are not authoritative for repo state)
- Copy-paste from chat history
- Agent memory / session context alone
- Verbal statements not recorded in repo files

If there is a conflict between chat history and repo files, **repo files win**.

---

## 5. Avoiding Long-Context Degradation

Long AI agent sessions degrade in quality as context grows. To mitigate:

- **Stay within 10 exchanges.** If the task requires more, split it.
- **Write to repo files, not to chat.** Every decision, file, and result should be in a file — not in a long chat thread.
- **Start each session from `SESSION_SUMMARY.md`**, not from re-reading a long chat history.
- **Never rely on agent memory** to carry state between sessions. If it is not in a file, it is not real.
- **Summarize, don't expand.** When updating `SESSION_SUMMARY.md`, be concise but complete.

---

## 6. Switching Between Builders

If a different Builder (or a new Claude Code session) is taking over mid-phase:

1. The previous Builder must finalize `SESSION_SUMMARY.md` before switching.
2. The new Builder must read `SESSION_SUMMARY.md` + `CURRENT_PHASE.md` + the phase handoff file before starting.
3. The new Builder must not re-do work already recorded in `SESSION_SUMMARY.md` as completed.
4. The new Builder must confirm the latest commit hash before starting any new work.

---

## 7. Reviewer (Codex) Handoff

When handing off to Codex for review:

- Builder output must include a `READY FOR CODEX REVIEW` signal in the session report.
- The phase handoff file must contain a `Codex review instructions` section with exact files to review and specific checks to perform.
- Codex must output one of: `PASS` / `PASS WITH NOTES` / `FAIL`.
- If Codex is unavailable (token limit), Owner performs direct review and records `OWNER_REVIEWED`.

---

## 8. Handoff File Naming Convention

| Phase | Handoff File |
|-------|-------------|
| Phase N | `handoff/PHASE_N_HANDOFF.md` |
| Phase N sub-phase A | `handoff/PHASE_NA_HANDOFF.md` |
| Always present | `handoff/CURRENT_PHASE.md` |
| Always present | `handoff/SESSION_SUMMARY.md` |

---

## 9. Emergency Session Stop

If the Builder hits a blocker (out-of-scope file needed, secret found, ambiguous instruction):

1. Stop immediately. Do not attempt to work around the blocker.
2. Set command status to `BLOCKED` in `commands/COMMAND_INBOX.md` (if applicable).
3. Update `handoff/CURRENT_PHASE.md` with status `BLOCKED`.
4. Update `handoff/SESSION_SUMMARY.md` with blocker description and exact files/instructions needed.
5. Report to Owner with exactly what is needed to unblock.
6. Do not commit until the blocker is resolved.

---

*Related:*
- `docs/governance/AGENT_OPERATION_RULES.md` — Agent roles and session limit rules
- `docs/governance/REPO_VALIDATION_CHECKLIST.md` — Pre-commit validation
- `docs/governance/OWNER_APPROVAL_GATE.md` — Approval gate definitions
- `handoff/SESSION_SUMMARY.md` — Current session state
- `handoff/CURRENT_PHASE.md` — Current phase status
