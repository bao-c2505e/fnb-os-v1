# Phase 0.12 — Status Snapshot Shortcut

Created By: Claude Code (Builder) — 2026-05-26

---

## Problem Being Solved

`SHOW_CURRENT_STATUS` was introduced in Phase 0.9 and outputs a structured summary to chat. But the output lives only in the conversation window — it cannot be read by another agent in a different session, referenced in a handoff, or compared across sessions.

Owner currently uses screenshots or copy-paste to share repo state with other agents or stakeholders. This introduces transcription errors and forces agents to re-read the same files each time.

Phase 0.12 closes this gap by making `SHOW_CURRENT_STATUS` write its output to a persistent file: `logs/CURRENT_STATUS.md`. Any agent, any session, any viewer can read the repo state in one file without needing to scan multiple handoff and command files.

---

## Objective

1. Expand `SHOW_CURRENT_STATUS` action list to write `logs/CURRENT_STATUS.md`.
2. Define the snapshot format with all 10 required fields.
3. State explicit guardrails: only one file written, no commit/push, no API calls, no secrets.
4. Create `logs/CURRENT_STATUS.md` as the persistent snapshot target.

**Phase 0.12 does NOT change the command lifecycle.** It only changes one shortcut's output behavior.

---

## What Changes in SHOW_CURRENT_STATUS

| Before Phase 0.12 | After Phase 0.12 |
|-------------------|------------------|
| Reads 3 files | Reads 5 files + 2 git commands |
| Outputs summary to chat only | Outputs to chat AND writes `logs/CURRENT_STATUS.md` |
| "Makes no file changes" | Writes exactly one file: `logs/CURRENT_STATUS.md` |
| Minimal snapshot (6 fields) | Full snapshot (10 required fields) |

---

## SHOW_CURRENT_STATUS — Expanded Action List

When any agent or Owner invokes `SHOW_CURRENT_STATUS`, the agent executes:

```
Step 1  — Read handoff/CURRENT_PHASE.md
Step 2  — Read commands/COMMAND_INBOX.md (first non-CLOSED record)
Step 3  — Read commands/COMMAND_STATUS.md (current index)
Step 4  — Read handoff/SESSION_SUMMARY.md (blockers + next_agent_action)
Step 5  — Run git log --oneline -1  (latest commit hash + message)
Step 6  — Run git status --short    (working tree state)
Step 7  — Assemble snapshot with all 10 required fields (format below)
Step 8  — Write snapshot to logs/CURRENT_STATUS.md (overwrite)
Step 9  — Output the same snapshot to chat
```

---

## Snapshot Format

Written to `logs/CURRENT_STATUS.md` (and echoed to chat):

```markdown
# Current Status — FnB OS V1

Last Updated: [YYYY-MM-DD] by [agent name]

---

## Active Command

| Field | Value |
|-------|-------|
| Phase | [X.XX — Phase Name] |
| Command ID | [CMD-X.XX-XXX] |
| Status | [STATUS] |
| Builder | [name] |
| Reviewer | [name] |

## Commit State

| Field | Value |
|-------|-------|
| Latest Commit | [hash] — [commit message] |
| Working Tree | [CLEAN / N files modified / N untracked] |

## Review & Approval State

| Check | State |
|-------|-------|
| Review result | [REVIEW_REQUESTED / REVIEW_PASS / REVIEW_FAIL / N/A] |
| Owner approval | [OWNER_APPROVED / pending / N/A] |

## Blockers

[None — or exact description of what is blocking progress]

## Next Actions

| Role | Next Action |
|------|-------------|
| Owner | [exact next step] |
| Builder | [exact next step] |
| Reviewer | [exact next step] |

---
*Written by SHOW_CURRENT_STATUS. Do not edit manually.*
*Sources: handoff/CURRENT_PHASE.md · commands/COMMAND_INBOX.md · commands/COMMAND_STATUS.md · handoff/SESSION_SUMMARY.md*
```

---

## Guardrails

| Rule | Detail |
|------|--------|
| Only one file written | `logs/CURRENT_STATUS.md` only — no other file may be created or modified |
| No feature files touched | Scope files, agent protocols, phase docs — all read-only |
| No status transitions | Must not change any command status field |
| No commit or push | `git log` and `git status` are read-only commands; no write git commands |
| No API calls | No external HTTP calls, no n8n activation, no Google API reads |
| No secrets in output | Must never write .env values, API keys, tokens, passwords, or real credentials to the snapshot |
| Overwrite-safe | Each run overwrites the previous `logs/CURRENT_STATUS.md` — this is intentional |

---

## Files Delivered

| File | Purpose |
|------|---------|
| `docs/phase-0/PHASE_0_12_STATUS_SNAPSHOT_SHORTCUT.md` | This file — problem, spec, format, guardrails |
| `commands/COMMAND_SHORTCUTS.md` | Updated — SHOW_CURRENT_STATUS expanded action list + snapshot format + guardrails |
| `commands/COMMAND_ROUTING_RULES.md` | Updated — SHOW_CURRENT_STATUS note updated (now writes one file) |
| `logs/CURRENT_STATUS.md` | New — persistent status snapshot file; initial content for Phase 0.12 |

---

## Done Criteria — Phase 0.12

- [x] `SHOW_CURRENT_STATUS` in `COMMAND_SHORTCUTS.md` has 9-step action list that writes `logs/CURRENT_STATUS.md`
- [x] Snapshot format defined: 10 required fields across Active Command, Commit State, Review & Approval State, Blockers, Next Actions
- [x] Guardrails explicit: only `logs/CURRENT_STATUS.md` written; no commit/push; no API calls; no secrets
- [x] `logs/CURRENT_STATUS.md` exists with initial Phase 0.12 snapshot
- [x] `COMMAND_ROUTING_RULES.md` note updated
- [x] `PHASE_0_12_STATUS_SNAPSHOT_SHORTCUT.md` documents problem, spec, format, guardrails, done criteria
- [x] CMD-0.11-001 CLOSED (commit bbda9d1); CMD-0.12-001 in COMMAND_INBOX.md and COMMAND_STATUS.md
- [x] Handoff and logs updated
- [x] No secrets in any Phase 0.12 file
