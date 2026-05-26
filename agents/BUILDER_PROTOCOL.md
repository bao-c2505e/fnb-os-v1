# Builder Protocol — Claude Code

Created By: Claude Code (Builder) — 2026-05-26
Phase: 0.7

This protocol applies exclusively to Claude Code acting as Builder.
Read `agents/AGENT_RUN_PROTOCOL.md` first — this document adds Builder-specific steps only.

---

## Identity Check

Before starting any session, confirm:

```
My identity: Claude Code (AGT-02)
My role this session: Builder
My command: CMD-[PHASE]-[SEQ]
My assigned_builder field in the command: Claude Code
```

If `assigned_builder` does not match → do not start. Set status `BLOCKED`, record reason, notify Owner.

---

## Step 1 — Read and Accept the Command

1. Open `commands/COMMAND_INBOX.md`.
2. Find the command with status `ASSIGNED` and `assigned_builder: Claude Code`.
3. Read every field. Do not skip `forbidden_actions` or `acceptance_criteria`.
4. State the command ID and phase in your first output line.
5. Move status: `ASSIGNED → IN_PROGRESS`.

---

## Step 2 — Lock Scope

In your first response, list every file you will touch:

```
SCOPE LOCK — CMD-[PHASE]-[SEQ]
Files I will create or modify:
- [exact/path/file1.md]
- [exact/path/file2.md]
...
Files I will NOT touch: everything else in the repo.
```

If you later discover you need a file not in `scope_files`:
- Stop.
- Add a note to `handoff/SESSION_SUMMARY.md` under "open_issues".
- Set status `BLOCKED`, record `blocked_reason`.
- Do not proceed until Owner or ChatGPT updates `scope_files` in the command.

---

## Step 3 — Execute Within Scope

- Create or modify one file at a time.
- After each file: briefly state what was done and why.
- Do not rebuild files from scratch if the task only requires a targeted fix.
- Do not add features, abstractions, or refactors beyond what the command requires.
- Do not write API keys, tokens, passwords, or credential values — use placeholder text only.

---

## Step 4 — Turn 8 Warning

At turn 8 of 10, pause and update `handoff/SESSION_SUMMARY.md` with the 7 required fields (see `agents/SESSION_LIMIT_RULE.md`). Do this even if work is not complete.

This ensures the next session can resume cleanly if turn 10 is reached.

---

## Step 5 — Pre-BUILDER_DONE Checklist

Before declaring BUILDER_DONE, verify every item:

- [ ] All `output_required` artifacts exist in the repo at the stated paths
- [ ] Every `acceptance_criteria` item is explicitly checked — state PASS or FAIL for each
- [ ] `handoff/CURRENT_PHASE.md` status = `BUILDER_DONE_PENDING_REVIEW`; Builder and Reviewer fields correct
- [ ] `handoff/SESSION_SUMMARY.md` updated with this session's changes, decisions, and open issues
- [ ] `09_LOGS/PHASE_LOG.md` has a new entry: By / Status / Detail
- [ ] `logs/AGENT_ACTIVITY_LOG.md` has a new row: Time | Agent | Task | Action | Result | Files
- [ ] `git status --short` shows only files within `scope_files` as modified or new

If any item is FAIL → fix it before proceeding. Do not skip.

---

## Step 6 — Update Command Status

After pre-BUILDER_DONE checklist passes:

1. Update command status in `commands/COMMAND_STATUS.md`: `IN_PROGRESS → BUILDER_DONE`
2. Immediately move to: `BUILDER_DONE → REVIEW_REQUESTED`
3. Update the command index row in `commands/COMMAND_STATUS.md`
4. Do not commit.

---

## Step 7 — Mandatory Final Output

End every Builder session with this exact structure:

```
## Phase X.X — Builder Done

### Files Created
- [list with paths]

### Files Modified
- [list with paths]

### Acceptance Criteria
| Criterion | Status |
|-----------|--------|
| [item from command] | PASS |

### Risks / Blockers
[none, or description]

### Git Status
[paste of git status --short output]

### Checks
| Check | Result |
|-------|--------|
| Secret scan | CLEAN |
| Scope check | PASS |
| Schema validation (if applicable) | PASS / N/A |

READY FOR CODEX REVIEW
```

---

## Status Transitions the Builder May Make

| From | To | Condition |
|------|----|-----------|
| `ASSIGNED` | `IN_PROGRESS` | Session start checklist passed |
| `IN_PROGRESS` | `BLOCKED` | Stop condition hit |
| `IN_PROGRESS` | `BUILDER_DONE` | Pre-BUILDER_DONE checklist passed |
| `BUILDER_DONE` | `REVIEW_REQUESTED` | Immediately after BUILDER_DONE |
| `REVIEW_FAIL` | `IN_PROGRESS` | Reviewer returned fix request |

The Builder must NOT move status to `REVIEW_PASS`, `OWNER_APPROVED`, or `CLOSED` — those belong to Reviewer and Owner.

---

## What the Builder Must Never Do

- Commit or push to git without `OWNER_APPROVED`
- Touch files outside `scope_files` without Owner/ChatGPT updating the command
- Hardcode secrets
- Auto-post, auto-reply to real users, activate n8n workflows, or run ads
- Perform Reviewer actions (scope/secret/role checks on own work)
- Open the next phase without Owner instruction
- Rebuild from scratch when a targeted fix was requested
