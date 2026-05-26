# Phase 0.11 — Owner Approval Shortcut

Created By: Claude Code (Builder) — 2026-05-26

---

## Problem Being Solved

After Phase 0.10, Owner can type `RUN_CURRENT_COMMAND` and `REVIEW_CURRENT_COMMAND` to trigger Builder and Reviewer sessions with a single line. But the approval step still requires Owner to manually edit `commands/COMMAND_STATUS.md`, `commands/COMMAND_INBOX.md`, `commands/CURRENT_COMMAND.md`, and `handoff/CURRENT_PHASE.md` to set `OWNER_APPROVED`.

Phase 0.11 closes this gap by adding `APPROVE_CURRENT_PHASE` — a shortcut Owner can type once to have an agent update all approval status files and output the ready-to-paste commit command.

After Phase 0.11, the full phase lifecycle is triggerable with four one-line Owner instructions:

```
Owner → Claude Code:  RUN_CURRENT_COMMAND        (Builder executes)
Owner → Codex:        REVIEW_CURRENT_COMMAND      (Reviewer reviews)
Owner → Claude Code:  APPROVE_CURRENT_PHASE       (status → OWNER_APPROVED + commit command output)
Owner → terminal:     git add ... && git commit && git push
Owner → Claude Code:  CLOSE_APPROVED_COMMAND      (status → CLOSED)
```

---

## Objective

1. Define the `APPROVE_CURRENT_PHASE` shortcut: what it does, when it is valid, and what it must not do.
2. Add guardrails so the shortcut cannot be run after `REVIEW_FAIL` or before a Reviewer has passed.
3. Update shortcut definitions and routing rules.
4. Add Owner usage example.
5. Keep scope small — no new agent roles, no new lifecycle states.

**Phase 0.11 does NOT add new command lifecycle states.** The existing `OWNER_APPROVED` state is unchanged. This shortcut only automates the file-editing step to reach it.

---

## APPROVE_CURRENT_PHASE — How It Works

### Trigger Condition

`APPROVE_CURRENT_PHASE` is valid only when the active command has status `REVIEW_PASS`.

The `REVIEW_PASS` status is set by the Reviewer (Codex) after outputting either:
- `REVIEW RESULT: PASS` — all criteria met, no issues
- `REVIEW RESULT: PASS_WITH_NOTES` — all criteria met, minor non-blocking observations

Both result in status `REVIEW_PASS` in `commands/COMMAND_STATUS.md`. Both allow `APPROVE_CURRENT_PHASE`.

### What the Agent Does

When Owner types `APPROVE_CURRENT_PHASE`, Claude Code (Builder):

```
Step 1  — Active Command Inference: scan COMMAND_INBOX.md top-to-bottom, find first non-CLOSED record.
Step 2  — Check status field:
           If REVIEW_PASS → proceed.
           If anything else → STOP. Report:
           "Found [CMD-ID] with status [actual]. APPROVE_CURRENT_PHASE requires REVIEW_PASS.
            Cannot approve. Check that Reviewer has returned PASS or PASS_WITH_NOTES first."
Step 3  — Update commands/COMMAND_STATUS.md: status → OWNER_APPROVED.
Step 4  — Update commands/COMMAND_INBOX.md: status field in active command record → OWNER_APPROVED.
Step 5  — Update commands/CURRENT_COMMAND.md: status → OWNER_APPROVED; Next Gate → commit instructions.
Step 6  — Update handoff/CURRENT_PHASE.md: Status → OWNER_APPROVED.
Step 7  — Update handoff/SESSION_SUMMARY.md: owner_approval_needed → false;
           next_agent_action → "Owner: run git commit + git push, then run CLOSE_APPROVED_COMMAND."
Step 8  — Output recommended commit command (do NOT run it):
           git add [scope_files from the active command]
           git commit -m "[suggested message derived from phase objective]"
           git push
Step 9  — End output with: OWNER_APPROVED — READY FOR COMMIT
```

### What the Agent Must NOT Do

- Run `git commit` or `git push` — Owner must execute these manually in terminal.
- Move status to `CLOSED` — that is `CLOSE_APPROVED_COMMAND` after commit.
- Skip the status check — if status is not `REVIEW_PASS`, stop immediately.
- Approve work that has a recorded `REVIEW_FAIL` — even if the status has since changed, if the Reviewer's FAIL output has not been followed by a new REVIEW_PASS, do not proceed.

---

## Guardrails

| Condition | Behaviour |
|-----------|-----------|
| Status is `REVIEW_PASS` | Proceed — update all approval files, output commit command |
| Status is `REVIEW_FAIL` | STOP — report: "APPROVE_CURRENT_PHASE blocked: command has REVIEW_FAIL. Builder must fix and re-submit." |
| Status is `REVIEW_REQUESTED` | STOP — report: "APPROVE_CURRENT_PHASE blocked: Reviewer has not yet returned a result." |
| Status is `IN_PROGRESS` or `ASSIGNED` | STOP — report: "APPROVE_CURRENT_PHASE blocked: Builder has not finished yet." |
| Status is `OWNER_APPROVED` | STOP — report: "Already OWNER_APPROVED. Run CLOSE_APPROVED_COMMAND after git commit/push." |
| Status is `CLOSED` | STOP — report: "Command is already CLOSED. No action needed." |
| No non-CLOSED record exists | `NO_ACTIVE_COMMAND` — report to Owner. |

---

## End-to-End Example

Owner types:
```
APPROVE_CURRENT_PHASE
```

Agent (Claude Code) executes:
```
1. Reads commands/COMMAND_SHORTCUTS.md → resolves token to action list
2. Scans commands/COMMAND_INBOX.md → first non-CLOSED: CMD-0.11-001, status REVIEW_PASS
3. Status matches trigger → proceed
4. Updates COMMAND_STATUS.md: CMD-0.11-001 → OWNER_APPROVED
5. Updates COMMAND_INBOX.md: status field → OWNER_APPROVED
6. Updates CURRENT_COMMAND.md: status → OWNER_APPROVED, Next Gate → commit instructions
7. Updates CURRENT_PHASE.md: Status → OWNER_APPROVED
8. Updates SESSION_SUMMARY.md: owner_approval_needed → false
9. Outputs:

   ## Recommended Commit Command

   git add docs/phase-0/PHASE_0_11_OWNER_APPROVAL_SHORTCUT.md \
           commands/COMMAND_SHORTCUTS.md \
           commands/COMMAND_ROUTING_RULES.md \
           agents/AGENT_RUN_PROTOCOL.md \
           commands/COMMAND_INBOX.md commands/COMMAND_STATUS.md \
           commands/CURRENT_COMMAND.md handoff/ logs/ \
           06_HANDOFF/NEXT_ACTIONS.md 09_LOGS/PHASE_LOG.md
   git commit -m "feat(phase-0.11): add owner approval shortcut"
   git push

10. Ends with: OWNER_APPROVED — READY FOR COMMIT
```

Owner copies the three git lines, pastes in terminal, runs them.
Then types `CLOSE_APPROVED_COMMAND` with the commit hash to finalize.

---

## What Phase 0.11 Does NOT Do

- Does not add new command lifecycle states
- Does not call any API
- Does not create n8n workflows or GitHub Actions
- Does not auto-commit or auto-push
- Does not open Phase 1

---

## Files Delivered

| File | Purpose |
|------|---------|
| `docs/phase-0/PHASE_0_11_OWNER_APPROVAL_SHORTCUT.md` | This file — problem, shortcut spec, guardrails, example |
| `commands/COMMAND_SHORTCUTS.md` | Updated — APPROVE_CURRENT_PHASE shortcut + Owner usage example |
| `commands/COMMAND_ROUTING_RULES.md` | Updated — APPROVE_CURRENT_PHASE row in Shortcut Role Gate table |
| `agents/AGENT_RUN_PROTOCOL.md` | Updated — integration diagram includes APPROVE_CURRENT_PHASE |

---

## Done Criteria — Phase 0.11

- [x] `PHASE_0_11_OWNER_APPROVAL_SHORTCUT.md` explains problem, shortcut spec, guardrails, end-to-end example
- [x] `COMMAND_SHORTCUTS.md` has `APPROVE_CURRENT_PHASE` definition with action list, guardrails, must-nots
- [x] `COMMAND_SHORTCUTS.md` has Owner usage example for `APPROVE_CURRENT_PHASE`
- [x] `COMMAND_ROUTING_RULES.md` Shortcut Role Gate table includes `APPROVE_CURRENT_PHASE`
- [x] `COMMAND_ROUTING_RULES.md` Routing Summary Table reflects `REVIEW_PASS → OWNER_APPROVED` via shortcut
- [x] `AGENT_RUN_PROTOCOL.md` integration diagram updated with `APPROVE_CURRENT_PHASE` step
- [x] CMD-0.11-001 in `COMMAND_INBOX.md` and `COMMAND_STATUS.md`
- [x] Handoff and logs updated
- [x] No secrets in any Phase 0.11 file
