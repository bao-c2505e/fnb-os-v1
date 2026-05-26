# Phase 0.13 — Session Handoff Shortcut

Created By: Claude Code (Builder) — 2026-05-27
Phase: 0.13
Command: CMD-0.13-001
Status: REVIEW_REQUESTED

---

## Objective

Add `CREATE_SESSION_HANDOFF` — a one-line shortcut that produces a complete, cross-session-ready handoff package before a context switch, session limit, or explicit Owner instruction to move to a new chat.

---

## Problem

`CREATE_SESSION_SUMMARY` (Phase 0.7) writes `handoff/SESSION_SUMMARY.md` at turn 8 with 7 fields. It preserves session state for the *same agent* resuming in the next turn window.

But it does not cover:
- Updating `logs/CURRENT_STATUS.md` (the persistent snapshot file added in Phase 0.12)
- Updating `06_HANDOFF/NEXT_ACTIONS.md` with the current gate state
- Appending a row to `logs/AGENT_ACTIVITY_LOG.md`
- Splitting next actions by role (Owner / Builder / Reviewer separately)
- Adding a session limit note so the *next agent* knows the session ended mid-work

When an Owner switches to a new Claude or Codex window, the new agent starts cold. Without a complete handoff package across all four state files, it must read many files to reconstruct context — or risk acting on stale state.

---

## Before / After

| State | Before (CREATE_SESSION_SUMMARY) | After (CREATE_SESSION_HANDOFF) |
|-------|---------------------------------|-------------------------------|
| Files written | `handoff/SESSION_SUMMARY.md` only | SESSION_SUMMARY + CURRENT_STATUS + NEXT_ACTIONS + AGENT_ACTIVITY_LOG |
| SESSION_SUMMARY fields | 7 | 14 (see spec below) |
| Next actions | Single `next_agent_action` field | Role-split: Owner / Builder / Reviewer |
| CURRENT_STATUS.md updated | No | Yes — always current on handoff |
| NEXT_ACTIONS.md updated | No | Yes — current gate reflected |
| Activity log row | No | Yes — handoff event recorded |
| Session limit note | No | Yes — explicit field |
| Use case | Session cap approaching (same session) | Any cross-session switch or context handoff |

---

## Shortcut Spec

### When to Use

- Turn 8+ of 10 (approaching session limit)
- Before switching to a new Claude or Codex chat window
- After a major phase state change (e.g. REVIEW_PASS, OWNER_APPROVED, CLOSED)
- When Owner explicitly says: "move to new chat", "start fresh session", "hand off"

### Files Written (exactly 4)

| File | Action |
|------|--------|
| `handoff/SESSION_SUMMARY.md` | Overwrite with 14-field handoff summary |
| `logs/CURRENT_STATUS.md` | Overwrite with current state snapshot (same format as SHOW_CURRENT_STATUS) |
| `06_HANDOFF/NEXT_ACTIONS.md` | Update CURRENT STATE header to reflect latest phase/status |
| `logs/AGENT_ACTIVITY_LOG.md` | Append one row: agent, task = "CREATE_SESSION_HANDOFF", result = "HANDOFF_WRITTEN" |

No other files may be written.

### 10-Step Action List

1. Read `handoff/CURRENT_PHASE.md` — get current phase, status, active command.
2. Read `commands/COMMAND_INBOX.md` — first non-CLOSED record → active command ID, status, scope_files.
3. Read `commands/COMMAND_STATUS.md` — command index.
4. Read `handoff/SESSION_SUMMARY.md` — existing session state, open issues.
5. Run `git log --oneline -1` — latest commit hash and message.
6. Run `git status --short` — working tree state (list modified/untracked files or "clean").
7. Write `handoff/SESSION_SUMMARY.md` — all 14 required fields (see format below).
8. Write `logs/CURRENT_STATUS.md` — same snapshot format as SHOW_CURRENT_STATUS.
9. Update `06_HANDOFF/NEXT_ACTIONS.md` — CURRENT STATE header line only (phase + status + next gate). Do not modify action items below.
10. Append row to `logs/AGENT_ACTIVITY_LOG.md`.

### SESSION_SUMMARY Required Fields (14)

| Field | Required Content |
|-------|-----------------|
| `current_phase` | Phase number and name |
| `current_role` | Agent name and role (e.g. "Builder — Claude Code") |
| `active_command` | Command ID and current status (e.g. "CMD-0.13-001 — REVIEW_REQUESTED") |
| `latest_commit` | Hash and message (e.g. "36fcfe — feat(phase-0.12): add status snapshot shortcut") |
| `files_changed` | Complete list with path and what changed |
| `files_pending` | Files modified but not yet committed — or "None" |
| `decisions_made` | Non-obvious choices and reason for each — or "None" |
| `open_issues` | Anything incomplete, blocked, or uncertain — or "None" |
| `blockers` | Hard blockers preventing next step — or "None" |
| `next_owner_action` | Exact next step for Owner |
| `next_builder_action` | Exact next step for Builder (Claude Code) |
| `next_reviewer_action` | Exact next step for Reviewer (Codex) |
| `session_limit_note` | e.g. "Session ended at turn 9/10. Resume from this file." or "Owner requested handoff." |
| `owner_approval_needed` | `true` or `false` with reason |

Note: 14 fields listed above — `files_changed`, `files_pending`, `decisions_made`, `open_issues`, `blockers`, `next_owner_action`, `next_builder_action`, `next_reviewer_action`, `session_limit_note` correspond to the 9 required handoff items. Together with `current_phase`, `current_role`, `active_command`, `latest_commit`, `owner_approval_needed` that is 14 total fields. All are required; write "None" if not applicable.

### Guardrails

| Rule | Enforcement |
|------|-------------|
| Write exactly 4 files | `SESSION_SUMMARY.md`, `CURRENT_STATUS.md`, `NEXT_ACTIONS.md`, `AGENT_ACTIVITY_LOG.md` — no others |
| No feature file changes | This shortcut is state-only; never modify docs, schema, prompt, or workflow files |
| No commit or push | Owner controls all commits; shortcut never runs git commands other than log/status reads |
| No API calls | No external HTTP, no n8n, no Google Sheets, no Telegram |
| No secrets in output | Never write API keys, tokens, passwords, credentials, sheet IDs, chat IDs |
| No status change | This shortcut does not advance command status — status is read-only during CREATE_SESSION_HANDOFF |
| NEXT_ACTIONS.md header only | Only the CURRENT STATE header line may be updated; action items below must not be modified |

---

## Integration with Existing Shortcuts

```
CREATE_SESSION_SUMMARY  ←  lightweight; 1 file; 7 fields; turn 8+ same session
CREATE_SESSION_HANDOFF  ←  full package; 4 files; 14 fields; cross-session switch
SHOW_CURRENT_STATUS     ←  snapshot only; 1 file (CURRENT_STATUS.md); read-only except that file
```

All three shortcuts leave command status unchanged. They are observational / handoff tools only.

---

## Done Criteria

- [ ] `CREATE_SESSION_HANDOFF` defined in `commands/COMMAND_SHORTCUTS.md` — 10-step action list, 14-field SESSION_SUMMARY format, guardrails
- [ ] `commands/COMMAND_ROUTING_RULES.md` updated — Shortcut Role Gate table and rules include `CREATE_SESSION_HANDOFF`
- [ ] Quick-Reference table in `COMMAND_SHORTCUTS.md` updated (8 shortcuts total)
- [ ] `PHASE_0_13_SESSION_HANDOFF_SHORTCUT.md` documents problem, before/after, spec, guardrails, done criteria
- [ ] CMD-0.13-001 in `commands/COMMAND_INBOX.md` and `commands/COMMAND_STATUS.md`
- [ ] Handoff and logs updated
- [ ] No secrets in any Phase 0.13 file
