# Command Routing Rules

Created By: Claude Code (Builder) — 2026-05-26
Phase: 0.8

This document defines how commands are routed to agents, what each agent may do, and what error conditions require a stop.

---

## Routing by Agent

### Claude Code (Builder)

Claude Code handles a command when:
- `assigned_builder: Claude Code` in the command record
- Command status is `ASSIGNED` (start) or `IN_PROGRESS` (resume) or `REVIEW_FAIL` (fix)

Claude Code must NOT handle a command when:
- `assigned_builder` is blank or names a different agent
- Command status is `REVIEW_REQUESTED`, `REVIEW_PASS`, `REVIEW_FAIL` (before Builder is notified), `OWNER_APPROVED`, or `CLOSED`
- Another Builder agent is already `IN_PROGRESS` on the same command

### Codex (Reviewer)

Codex handles a command when:
- `assigned_reviewer: Codex` in the command record
- Command status is `REVIEW_REQUESTED`

Codex must NOT handle a command when:
- `assigned_reviewer` is blank or names a different agent
- Command status is anything other than `REVIEW_REQUESTED`
- The Builder has not yet set status to `REVIEW_REQUESTED`

### Owner / ChatGPT (Chief Architect)

Owner or ChatGPT creates and closes commands:
- Create command → set `ASSIGNED`
- Move `REVIEW_PASS → OWNER_APPROVED → CLOSED`
- Update `scope_files` if Builder requests a scope expansion (requires BLOCKED status)

---

## No-Concurrent-Edit Rule

**Two agents must never modify the same file group at the same time.**

| File Group | Who Owns It During Build |
|------------|--------------------------|
| `scope_files` content | Builder (Claude Code) only, while IN_PROGRESS |
| `commands/COMMAND_STATUS.md` index row | Builder updates status; Reviewer updates status; Owner updates status — but only in sequence, never simultaneously |
| `handoff/CURRENT_PHASE.md` | Builder updates during build; Reviewer must not edit |
| `handoff/SESSION_SUMMARY.md` | Builder updates during build; Reviewer adds review_notes only |
| `09_LOGS/PHASE_LOG.md` | Append-only; each agent appends their own entry |
| `logs/AGENT_ACTIVITY_LOG.md` | Append-only; each agent appends their own row |

If two agents are active on the same command simultaneously → stop, set `BLOCKED`, notify Owner.

---

## Builder Constraints

- Builder reads `scope_files` from the command and lists them explicitly before starting (scope lock).
- Builder may only create or modify files listed in `scope_files`.
- Builder may not self-review own output.
- Builder may not move status to `REVIEW_PASS`, `OWNER_APPROVED`, or `CLOSED`.
- If Builder needs a file outside `scope_files` → set `BLOCKED`, record reason, wait for Owner to update scope.

---

## Reviewer Constraints

- Reviewer reads the command record and all `output_required` files before evaluating.
- Reviewer checks each `acceptance_criteria` item: PASS or FAIL with specific reason.
- Reviewer does not rebuild or rewrite scope content.
- Reviewer may add `review_notes` to SESSION_SUMMARY.md but must not edit Builder's output files.
- Reviewer may not move status to `IN_PROGRESS`, `OWNER_APPROVED`, or `CLOSED`.
- Reviewer outputs `REVIEW RESULT: PASS` or `REVIEW RESULT: FAIL` — no ambiguous prose.

---

## Error Conditions

### NEED_COMMAND_CLARIFICATION

**Trigger:** Agent receives a command that is missing one or more required fields:
`command_id`, `assigned_builder`, `assigned_reviewer`, `scope_files`, `acceptance_criteria`, `output_required`.

**Action:**
1. Agent must NOT start work.
2. Set command status to `BLOCKED`.
3. Record `blocked_reason: NEED_COMMAND_CLARIFICATION — missing fields: [list]`.
4. Notify Owner or ChatGPT to complete the command record.

---

### SCOPE_CONFLICT

**Trigger:** Agent is asked to modify a file that is:
- Not listed in `scope_files`, **or**
- Currently being modified by another agent's active command.

**Action:**
1. Agent must NOT modify the conflicting file.
2. Set command status to `BLOCKED`.
3. Record `blocked_reason: SCOPE_CONFLICT — [file path] is outside scope_files or owned by another active command`.
4. Notify Owner to either update `scope_files` or resolve the concurrent command.

---

### SECRET_RISK

**Trigger:** Agent observes or is about to write a value that matches a known secret pattern:
- API key formats: `sk-`, `AIza`, `ghp_`, `ya29.`, `xoxb-`
- Password or token assignment in any file
- Real credential values (not placeholder text)

**Action:**
1. Agent must IMMEDIATELY stop all file writes.
2. Do NOT write the secret to any file.
3. Set command status to `BLOCKED`.
4. Record `blocked_reason: SECRET_RISK — potential secret detected in [context]. No file written.`
5. Notify Owner immediately. Owner must assess and confirm no secret was committed.

---

## Command Completion Conditions

A command is complete (`CLOSED`) when ALL of the following are true:

| Condition | How Verified |
|-----------|-------------|
| All `acceptance_criteria` items: PASS | Reviewer confirmed in REVIEW RESULT: PASS |
| `OWNER_APPROVED` status set | Owner updated `commands/COMMAND_STATUS.md` |
| `git log` shows commit for this phase | Owner ran git commit/push |
| No open issues in `handoff/SESSION_SUMMARY.md` | Builder confirmed before BUILDER_DONE |
| No secrets in any changed file | Reviewer confirmed in secret scan |

If any condition is unmet → command is not closed.

---

## Routing Summary Table

| Command Status | Who Acts | Allowed Actions |
|----------------|----------|-----------------|
| `NEW` | Owner / ChatGPT | Set to ASSIGNED, assign Builder/Reviewer |
| `ASSIGNED` | Builder | Move to IN_PROGRESS, start scope lock |
| `IN_PROGRESS` | Builder | Edit scope_files, update handoff/logs |
| `BLOCKED` | Builder / Owner | Builder records reason; Owner resolves |
| `BUILDER_DONE` | Builder | Move to REVIEW_REQUESTED |
| `REVIEW_REQUESTED` | Reviewer | Run review checks, set REVIEW_PASS or REVIEW_FAIL |
| `REVIEW_FAIL` | Builder | Fix issues, return to IN_PROGRESS |
| `REVIEW_PASS` | Owner | Set OWNER_APPROVED |
| `OWNER_APPROVED` | Owner | Run git commit/push, set CLOSED |
| `CLOSED` | None | No further action |
