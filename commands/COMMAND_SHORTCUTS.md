# Command Execution Shortcuts

Created By: Claude Code (Builder) — 2026-05-26
Updated By: Claude Code (Builder) — 2026-05-26 (Phase 0.10 — Active Command Inference added)
Phase: 0.10

Shortcuts replace the need to write or paste long role-specific prompts. Each shortcut maps to a named set of actions an agent must perform. Owner pastes the shortcut token; the agent resolves it against the active command in `commands/COMMAND_INBOX.md`.

Routing rules for shortcuts: `commands/COMMAND_ROUTING_RULES.md` → Shortcut Routing section.
Inference algorithm detail: `docs/phase-0/PHASE_0_10_ONE_LINE_AGENT_COMMANDS.md`.

---

## Active Command Inference

When an agent receives a shortcut token and no other context, it identifies the active command using this algorithm:

1. Open `commands/COMMAND_INBOX.md`.
2. Scan records from top to bottom.
3. Find the **first record that is NOT a CLOSED stub** (a CLOSED stub has `status: CLOSED` or `**CLOSED**`).
4. Read that record's `status` field.
5. Check: does the status match the shortcut's required trigger status? (See Shortcut Quick-Reference table below.)
6. If YES → this is the active command. Read all fields and proceed.
7. If NO → report the mismatch to Owner: `"Found [CMD-ID] with status [actual], but [SHORTCUT] requires [expected]."` Do not proceed.
8. Verify `assigned_builder` or `assigned_reviewer` matches your own agent identity. If mismatch → `ROLE_CONFLICT` → stop and report.
9. Read `scope_files`, `forbidden_actions`, `acceptance_criteria` from the active command.
10. Execute the shortcut action list.

**Why this works:** `COMMAND_INBOX.md` is maintained with new commands at the top and CLOSED stubs below. The first non-CLOSED record is always the most recent active command — no ID lookup required.

---

## Shortcut Reference

### RUN_CURRENT_COMMAND

**Role:** Builder (Claude Code only)
**When to use:** Owner gives Claude Code a new session to build the active command.

**Agent must:**
1. Read `commands/COMMAND_INBOX.md` — find the command with status `ASSIGNED` or `IN_PROGRESS` and `assigned_builder: Claude Code`.
2. Read `handoff/CURRENT_PHASE.md` — confirm phase matches.
3. Read `handoff/SESSION_SUMMARY.md` — pick up any open issues from a prior session.
4. Lock scope: list every `scope_files` entry in the first output line.
5. Move command status `ASSIGNED → IN_PROGRESS` (if not already).
6. Execute all `acceptance_criteria` within `scope_files`.
7. Update `handoff/CURRENT_PHASE.md`, `handoff/SESSION_SUMMARY.md`, `09_LOGS/PHASE_LOG.md`, `logs/AGENT_ACTIVITY_LOG.md`.
8. Run `git status --short` and secret scan.
9. Move status `IN_PROGRESS → BUILDER_DONE → REVIEW_REQUESTED`.
10. End output with: `READY FOR CODEX REVIEW`

**Agent must NOT:**
- Commit or push.
- Touch files outside `scope_files`.
- Hardcode secrets.
- Open the next phase.

---

### REVIEW_CURRENT_COMMAND

**Role:** Reviewer (Codex only)
**When to use:** Owner gives Codex a new session to review the active command.

**Agent must:**
1. Read `commands/COMMAND_INBOX.md` — find the command with status `REVIEW_REQUESTED` and `assigned_reviewer: Codex`.
2. Read every file listed in `output_required`.
3. Read `handoff/SESSION_SUMMARY.md` — Builder's session notes.
4. Check each `acceptance_criteria` item: PASS or FAIL with specific reason.
5. Run scope violation check, secret scan, role conflict check, safety check.
6. End output with `## REVIEW RESULT: PASS` or `## REVIEW RESULT: FAIL` followed by the full structured table.

**Agent must NOT:**
- Rebuild or rewrite Builder output files.
- Commit or push.
- Move status to `OWNER_APPROVED` or `CLOSED`.

---

### FIX_REVIEW_FAIL

**Role:** Builder (Claude Code only)
**When to use:** Codex returned `REVIEW RESULT: FAIL` and Owner asks Builder to fix.

**Agent must:**
1. Read `commands/COMMAND_INBOX.md` — find the command with status `REVIEW_FAIL`.
2. Read the Reviewer's `REVIEW RESULT: FAIL` output — identify every listed issue.
3. Fix only the specific issues listed. Do not rebuild. Do not change unrelated files.
4. For each fix: state the file changed, the issue addressed, and what was changed.
5. Move status `REVIEW_FAIL → IN_PROGRESS → BUILDER_DONE → REVIEW_REQUESTED`.
6. Update `handoff/SESSION_SUMMARY.md`, `09_LOGS/PHASE_LOG.md`, `logs/AGENT_ACTIVITY_LOG.md`.
7. Run `git status --short` and secret scan.
8. End output with: `READY FOR CODEX RE-REVIEW`

**Agent must NOT:**
- Rebuild the phase from scratch.
- Open the next phase.
- Commit or push.

---

### CLOSE_APPROVED_COMMAND

**Role:** Owner (only after Owner has committed and pushed)
**When to use:** After Owner has run `git commit` + `git push` on an `OWNER_APPROVED` command.

**Agent must:**
1. Confirm `git log` shows a commit for this phase (Owner provides commit hash).
2. Update `commands/COMMAND_STATUS.md` — set command status to `CLOSED`, record commit hash.
3. Update `commands/COMMAND_INBOX.md` — collapse the command entry to a CLOSED stub.
4. Update `handoff/CURRENT_PHASE.md` — previous phase = CLOSED + commit.

**Agent must NOT:**
- Run this shortcut before Owner has committed and pushed.
- Self-approve: Owner must have explicitly set `OWNER_APPROVED` first.
- Skip recording the commit hash.

---

### CREATE_SESSION_SUMMARY

**Role:** Any agent (Builder or Reviewer) when approaching session limit
**When to use:** At turn 8 of 10, or whenever session state must be preserved before stopping.

**Agent must write `handoff/SESSION_SUMMARY.md` with all 7 required fields:**

| Field | Required Content |
|-------|-----------------|
| `current_phase` | Phase number and name |
| `current_role` | Agent name and role |
| `files_changed` | Complete list with path and what changed |
| `decisions_made` | Non-obvious choices and the reason for each |
| `open_issues` | Anything incomplete, blocked, or uncertain |
| `next_agent_action` | Exactly who should do what next, referencing command ID |
| `owner_approval_needed` | `true` or `false` with reason |

This shortcut does not change command status. It only preserves session state so the next session can resume cleanly.

---

### SHOW_CURRENT_STATUS

**Role:** Any agent or Owner
**When to use:** At the start of any session, or any time current state is unclear.

**Agent must:**
1. Read `handoff/CURRENT_PHASE.md`.
2. Read `commands/COMMAND_INBOX.md` — active command section only.
3. Read `commands/COMMAND_STATUS.md` — current index.
4. Output a structured summary:

```
## Current Status — FnB OS V1

Phase:          [phase number and name]
Active Command: [CMD-X.X-XXX]
Status:         [status]
Builder:        [agent name]
Reviewer:       [agent name]
Next Gate:      [what must happen next and who does it]

Recent CLOSED:
- [CMD-X.X-XXX] commit [hash]
```

This shortcut makes no file changes and does not move any status.

---

## Owner Usage Examples

### Starting a Builder session

Owner opens a chat with Claude Code and types:

```
RUN_CURRENT_COMMAND
```

Claude Code:
1. Reads `commands/CURRENT_COMMAND.md` or scans `commands/COMMAND_INBOX.md` (first non-CLOSED record)
2. Finds CMD-0.10-001, status ASSIGNED, assigned_builder: Claude Code
3. Announces scope lock
4. Executes acceptance_criteria within scope_files
5. Ends with: `READY FOR CODEX REVIEW`

No phase number. No command ID. No context paste. One line.

---

### Starting a Reviewer session

Owner opens a chat with Codex and types:

```
REVIEW_CURRENT_COMMAND
```

Codex:
1. Reads `commands/CURRENT_COMMAND.md` or scans `commands/COMMAND_INBOX.md` (first non-CLOSED record)
2. Finds CMD-0.10-001, status REVIEW_REQUESTED, assigned_reviewer: Codex
3. Reads all output_required files
4. Evaluates each acceptance_criteria
5. Ends with: `REVIEW RESULT: PASS` / `PASS_WITH_NOTES` / `FAIL`

No instructions needed. One line.

---

### Checking current status

Owner (or any agent) types:

```
SHOW_CURRENT_STATUS
```

Agent reads `commands/CURRENT_COMMAND.md` → outputs structured summary block. No file changes.

---

## Shortcut Error Conditions

| Error | Trigger | Required Action |
|-------|---------|-----------------|
| `ROLE_CONFLICT` | Agent invokes a shortcut reserved for a different role | Stop immediately. Do not execute the shortcut. Report to Owner. |
| `NO_ACTIVE_COMMAND` | Shortcut is invoked but no command matches the required status | Report to Owner. Do not start or continue work. |
| `NEED_COMMAND_CLARIFICATION` | Active command is missing required fields | Set status `BLOCKED`, record missing fields, notify Owner. |
| `SCOPE_CONFLICT` | Shortcut execution would touch a file outside `scope_files` | Set status `BLOCKED`, record conflict, notify Owner. |
| `SECRET_RISK` | Shortcut execution would write a secret pattern | Stop all writes immediately. Set status `BLOCKED`. Notify Owner. |

---

## Shortcut Quick-Reference

| Shortcut | Role | Trigger Status | Output Ends With |
|----------|------|---------------|-----------------|
| `RUN_CURRENT_COMMAND` | Builder | ASSIGNED / IN_PROGRESS | `READY FOR CODEX REVIEW` |
| `REVIEW_CURRENT_COMMAND` | Reviewer | REVIEW_REQUESTED | `REVIEW RESULT: PASS/FAIL` |
| `FIX_REVIEW_FAIL` | Builder | REVIEW_FAIL | `READY FOR CODEX RE-REVIEW` |
| `CLOSE_APPROVED_COMMAND` | Owner | OWNER_APPROVED (after commit) | Status → CLOSED |
| `CREATE_SESSION_SUMMARY` | Any | Any (turn 8+) | SESSION_SUMMARY updated |
| `SHOW_CURRENT_STATUS` | Any | Any | Structured status block |
