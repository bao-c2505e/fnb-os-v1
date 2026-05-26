# Command Execution Shortcuts

Created By: Claude Code (Builder) — 2026-05-26
Updated By: Claude Code (Builder) — 2026-05-26 (Phase 0.12 — SHOW_CURRENT_STATUS expanded)
Phase: 0.12

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

### APPROVE_CURRENT_PHASE

**Role:** Builder (Claude Code) — on Owner's explicit approval instruction
**When to use:** After Reviewer returns REVIEW_PASS or PASS_WITH_NOTES. Owner wants to mark the active command as OWNER_APPROVED and receive the ready-to-paste commit command.

**Agent must:**
1. Read `commands/COMMAND_INBOX.md` — find first non-CLOSED record via Active Command Inference.
2. Check status:
   - `REVIEW_PASS` → proceed.
   - Anything else → STOP. Report exact status and reason (see Guardrails below).
3. Update `commands/COMMAND_STATUS.md` — set status to `OWNER_APPROVED`.
4. Update `commands/COMMAND_INBOX.md` — set status field to `OWNER_APPROVED` in the active command record.
5. Update `commands/CURRENT_COMMAND.md` — set status to `OWNER_APPROVED`; update Next Gate to show commit instructions.
6. Update `handoff/CURRENT_PHASE.md` — set Status to `**OWNER_APPROVED**`.
7. Update `handoff/SESSION_SUMMARY.md` — set `owner_approval_needed: false`; update `next_agent_action` to "Owner: run git commit + git push, then run CLOSE_APPROVED_COMMAND."
8. Output recommended commit command (do NOT run it):
   ```
   ## Recommended Commit Command

   git add [scope_files from active command]
   git commit -m "feat(phase-X.X): [objective from active command]"
   git push
   ```
9. End output with: `OWNER_APPROVED — READY FOR COMMIT`

**Guardrails — status checks:**

| Active Command Status | Behaviour |
|----------------------|-----------|
| `REVIEW_PASS` | Proceed |
| `REVIEW_FAIL` | STOP — "APPROVE_CURRENT_PHASE blocked: active command has REVIEW_FAIL. Builder must fix and re-submit." |
| `REVIEW_REQUESTED` | STOP — "APPROVE_CURRENT_PHASE blocked: Reviewer has not yet returned a result." |
| `IN_PROGRESS` / `ASSIGNED` | STOP — "APPROVE_CURRENT_PHASE blocked: Builder has not finished yet." |
| `OWNER_APPROVED` | STOP — "Already OWNER_APPROVED. Run CLOSE_APPROVED_COMMAND after git commit/push." |
| `CLOSED` | STOP — "Command is already CLOSED. No action needed." |

**Agent must NOT:**
- Run `git commit` or `git push` — Owner executes these manually in terminal.
- Move status to `CLOSED` — that is `CLOSE_APPROVED_COMMAND` after commit.
- Skip the status check.
- Approve work that has an unresolved `REVIEW_FAIL`.

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
**When to use:** At the start of any session, or any time current state is unclear. Also useful for sharing repo state without screenshots or copy-paste.

**Agent must:**
1. Read `handoff/CURRENT_PHASE.md`.
2. Read `commands/COMMAND_INBOX.md` — first non-CLOSED record (active command).
3. Read `commands/COMMAND_STATUS.md` — current index.
4. Read `handoff/SESSION_SUMMARY.md` — blockers and next_agent_action fields.
5. Run `git log --oneline -1` — latest commit hash and message.
6. Run `git status --short` — working tree state.
7. Assemble snapshot with all 10 required fields (see format below).
8. Write snapshot to `logs/CURRENT_STATUS.md` (overwrite previous snapshot).
9. Output the same snapshot to chat.

**Snapshot format (written to `logs/CURRENT_STATUS.md` and echoed to chat):**

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

[None — or exact description]

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

**Agent must NOT:**
- Modify any file other than `logs/CURRENT_STATUS.md`.
- Commit or push.
- Call external APIs, activate n8n workflows, or read production data.
- Write any secret, API key, token, password, or production URL to the snapshot.
- Move any command status.

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

Agent:
1. Reads `handoff/CURRENT_PHASE.md`, `commands/COMMAND_INBOX.md`, `commands/COMMAND_STATUS.md`, `handoff/SESSION_SUMMARY.md`
2. Runs `git log --oneline -1` and `git status --short`
3. Assembles a structured snapshot (phase, active command, status, commit state, review state, blockers, next actions)
4. **Writes snapshot to `logs/CURRENT_STATUS.md`** (overwrites previous)
5. Echoes the same snapshot to chat

Owner can read `logs/CURRENT_STATUS.md` at any time — it is the persistent, shareable repo state file.

**Guardrails:** Only `logs/CURRENT_STATUS.md` is written. No feature files modified. No commit or push. No external API calls or workflow activation. No secrets written to the snapshot.

---

### Approving a reviewed phase

After Codex returns REVIEW RESULT: PASS (or PASS_WITH_NOTES), Owner opens Claude Code and types:

```
APPROVE_CURRENT_PHASE
```

Claude Code:
1. Scans `commands/COMMAND_INBOX.md` → first non-CLOSED record; verifies status is `REVIEW_PASS`
2. Updates status → `OWNER_APPROVED` in COMMAND_STATUS.md, COMMAND_INBOX.md, CURRENT_COMMAND.md, CURRENT_PHASE.md, SESSION_SUMMARY.md
3. Outputs the recommended commit command

Owner copies the git lines, pastes in terminal, runs them.
Then types `CLOSE_APPROVED_COMMAND` with the commit hash.

No manual file editing. One line triggers the approval + commit prep.

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
| `APPROVE_CURRENT_PHASE` | Builder (on Owner instruction) | REVIEW_PASS | `OWNER_APPROVED — READY FOR COMMIT` |
| `CLOSE_APPROVED_COMMAND` | Owner | OWNER_APPROVED (after commit) | Status → CLOSED |
| `CREATE_SESSION_SUMMARY` | Any | Any (turn 8+) | SESSION_SUMMARY updated |
| `SHOW_CURRENT_STATUS` | Any | Any | Snapshot written to `logs/CURRENT_STATUS.md` + chat |
