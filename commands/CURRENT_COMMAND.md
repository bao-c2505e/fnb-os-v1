# Current Command

Maintained By: Builder agent — updated whenever a new active command begins.

This file is the single-file source of truth for the current active command.
It is a pointer extract from `commands/COMMAND_INBOX.md` (first non-CLOSED record).

Agents receiving only a shortcut token (e.g. `RUN_CURRENT_COMMAND`) may read this file
instead of scanning the full COMMAND_INBOX.md.

---

## Active Command

| Field | Value |
|-------|-------|
| `command_id` | CMD-0.12-001 |
| `phase` | 0.12 — Status Snapshot Shortcut |
| `objective` | Expand SHOW_CURRENT_STATUS to write a persistent status snapshot to logs/CURRENT_STATUS.md |
| `status` | OWNER_APPROVED |
| `assigned_builder` | Claude Code |
| `assigned_reviewer` | Codex |
| `priority` | high |

## Next Gate

Owner: run git commit + git push, then run `CLOSE_APPROVED_COMMAND` with the commit hash.
Full command record: `commands/COMMAND_INBOX.md` → CMD-0.12-001.

---

## How to Use This File

**As Builder (RUN_CURRENT_COMMAND):**
1. Read this file — confirm `assigned_builder: Claude Code` and status is `ASSIGNED` or `IN_PROGRESS`.
2. Open `commands/COMMAND_INBOX.md` → CMD-0.12-001 for full scope_files, forbidden_actions, acceptance_criteria.
3. Execute.

**As Reviewer (REVIEW_CURRENT_COMMAND):**
1. Read this file — confirm `assigned_reviewer: Codex` and status is `REVIEW_REQUESTED`.
2. Open `commands/COMMAND_INBOX.md` → CMD-0.12-001 for full output_required and acceptance_criteria.
3. Review.

**As Owner (SHOW_CURRENT_STATUS):**
Read `logs/CURRENT_STATUS.md` for a fast one-screen summary written by the last SHOW_CURRENT_STATUS run.
Or read this file for the active command pointer.

---

## Update Protocol

Builder must update this file when:
- A new command becomes active (ASSIGNED or IN_PROGRESS).
- Status changes (IN_PROGRESS → REVIEW_REQUESTED, etc.).
- Command is CLOSED (update to show next active command, or mark "No active command").

This file does NOT replace `commands/COMMAND_INBOX.md` or `commands/COMMAND_STATUS.md`.
It is a read-convenience layer only.
