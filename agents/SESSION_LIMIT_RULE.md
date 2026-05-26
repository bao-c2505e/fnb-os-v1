# Session Limit Rule

Created By: Claude Code (Builder) — 2026-05-26
Phase: 0.7

This document formalizes the 10-turn session cap first stated in `06_HANDOFF/AGENT_COMMUNICATION_RULES.md`.
It defines exactly what agents must do when approaching and hitting the cap.

---

## The Rule

**Every agent session has a hard cap of 10 turns (back-and-forth exchanges).**

One turn = one user message + one agent response.

This applies to all agents: Builder (Claude Code), Reviewer (Codex), ChatGPT, and any future agents.

---

## Why This Rule Exists

- Prevents context drift: long sessions lose track of original scope and constraints.
- Prevents runaway sessions: an agent that keeps going past its mandate causes more problems than it solves.
- Ensures handoff: if a session cannot finish within 10 turns, a structured summary must exist so the next session can resume without starting over.
- Enforces accountability: every session must produce a written record, not just implied state.

---

## Turn Count Checkpoints

| Turn | Required Action |
|------|----------------|
| 1 | State role, command ID, phase. Complete Session Start Checklist. |
| 8 | **Write or update `handoff/SESSION_SUMMARY.md` with all 7 required fields** (see below). Announce remaining turns. |
| 10 | **Hard stop.** Finalize status. Do not start new work after this turn. |

---

## At Turn 8 — Forced SESSION_SUMMARY Update

At turn 8, regardless of task completion state, the agent must update `handoff/SESSION_SUMMARY.md` with all 7 required fields:

| Field | Description |
|-------|-------------|
| `current_phase` | Phase number, e.g. 0.7 |
| `current_role` | Builder (Claude Code) or Reviewer (Codex) |
| `files_changed` | Exact list of files created or modified this session |
| `decisions_made` | Key choices made that the next session should know |
| `open_issues` | Anything unresolved, blocked, or needing follow-up |
| `next_agent_action` | What the next agent (or next session) should do first |
| `owner_approval_needed` | true / false — and what specifically needs approval |

This update must be written to `handoff/SESSION_SUMMARY.md`. It is not optional.

---

## At Turn 10 — Hard Stop

At turn 10 the agent must:

1. Write the final `handoff/SESSION_SUMMARY.md` update (if not done at turn 8).
2. Append a row to `logs/AGENT_ACTIVITY_LOG.md`.
3. Set the command status to either:
   - `BUILDER_DONE` — if all acceptance criteria are met
   - `BLOCKED` — if work is incomplete and cannot continue without input
4. Do not start any new file edits or analysis after declaring the status.
5. Write the mandatory final output (see `agents/AGENT_RUN_PROTOCOL.md`, Section 7).

---

## Resuming After Session Cap

When a new session begins after a cap:

1. Read `handoff/SESSION_SUMMARY.md` — the `open_issues` and `next_agent_action` fields are the authoritative starting point.
2. Do not repeat work already marked as done in `files_changed`.
3. Do not re-run the full Session Start Checklist if the command status is already `IN_PROGRESS` — only verify the `open_issues` items.
4. State in the first turn: "Resuming from SESSION_SUMMARY — turn 1 of new session."

---

## Session Cap vs. Task Completion

The session cap does not mean the task must be incomplete. It means:

- If the task fits in under 10 turns → complete it normally.
- If the task requires more than 10 turns → split it across sessions using SESSION_SUMMARY as the bridge.
- If the task is genuinely too large for a single session → Owner or ChatGPT should split it into multiple commands.

---

## Reference

The 10-turn cap was first established in:
`06_HANDOFF/AGENT_COMMUNICATION_RULES.md`

The required SESSION_SUMMARY.md format is used in:
`handoff/SESSION_SUMMARY.md`

The full stop conditions are listed in:
`agents/AGENT_RUN_PROTOCOL.md` — Section 5
