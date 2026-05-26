# Agent Run Protocol

Created By: Claude Code (Builder) — 2026-05-26
Updated By: Claude Code (Builder) — 2026-05-26 (Phase 0.9 — Shortcut layer reference added)
Phase: 0.9

This document is the master operational protocol for all agent sessions in FnB OS V1.
It bridges the Phase 0.6 Command Intake Layer with actual session execution.

Do not restate content from the following — read them first:
- Agent identities: `06_HANDOFF/AGENT_REGISTRY.md`
- Communication rules and file ownership: `06_HANDOFF/AGENT_COMMUNICATION_RULES.md`
- Hard limits and approval gates by role: `docs/agent-system/OPERATING_RULES.md`
- Command lifecycle (10 states) and field reference: `docs/phase-0/PHASE_0_6_COMMAND_INTAKE.md`

---

## 1. Session Start Checklist

Before writing a single line of output, every agent must complete this checklist in order:

| # | Check | Pass Condition |
|---|-------|---------------|
| 1 | Read `handoff/CURRENT_PHASE.md` | Phase number matches the command you were assigned |
| 2 | Read `commands/COMMAND_INBOX.md` | Your command exists and status is `ASSIGNED` (for Builder) or `REVIEW_REQUESTED` (for Reviewer) |
| 3 | Confirm `assigned_builder` or `assigned_reviewer` | Field matches your own agent identity exactly |
| 4 | Read `scope_files` in the command | You can enumerate every file you are allowed to touch |
| 5 | Read `forbidden_actions` in the command | None of them apply to anything you are about to do |
| 6 | Read `acceptance_criteria` | You can describe in plain language what DONE looks like |
| 7 | Read `handoff/SESSION_SUMMARY.md` | You understand any open issues from a previous session |
| 8 | Confirm no secrets in scope | No `.env`, no credential files, no API key strings in your planned work |

If any check fails → do not start work. Set command status to `BLOCKED`, record `blocked_reason`, notify Owner.

---

## 2. Role Confirmation

Every session must start by stating the active role:

```
ROLE: Builder (Claude Code) | Phase 0.X | CMD-0.X-00X
```
or
```
ROLE: Reviewer (Codex) | Phase 0.X | CMD-0.X-00X reviewing
```

A Builder session must not perform Reviewer actions.
A Reviewer session must not rebuild or write new files beyond review notes.
See role-specific protocols: `agents/BUILDER_PROTOCOL.md`, `agents/REVIEWER_PROTOCOL.md`.

---

## 3. Execution Constraints

These apply to every agent session without exception:

- Only create or modify files listed in `scope_files`. Any deviation requires a written reason in the session output.
- Do not hardcode API keys, tokens, passwords, or secrets in any file.
- Do not activate n8n workflows, post content, send messages to real users, reply to real customers, or run paid ads.
- Do not commit or push to git without `OWNER_APPROVED` status on the command.
- Do not open the next phase until the current command is `CLOSED`.
- Do not make decisions that require Owner approval (new integrations, live data access, external publishing) — set `BLOCKED` and wait.

---

## 4. Session Execution Loop

```
[Start] → Session Start Checklist (Section 1)
    ↓
[Confirm Role] → State role, phase, command ID
    ↓
[Lock Scope] → List scope_files explicitly
    ↓
[Execute] → Create/edit files one at a time within scope
    ↓
[Check Turn Count] → At turn 8 of 10: update SESSION_SUMMARY.md
    ↓
[Stop Condition?] → Yes → proceed to Section 5
    ↓
[Continue] → loop back to Execute
```

---

## 5. Stop Conditions

A session must stop when any of the following is true:

| Condition | Action |
|-----------|--------|
| All `acceptance_criteria` satisfied | Proceed to Pre-BUILDER_DONE checklist (Section 6) |
| Turn 10 reached (session cap) | Write SESSION_SUMMARY.md; set status BUILDER_DONE or BLOCKED |
| A `forbidden_actions` item would be violated | Set BLOCKED; record reason; stop immediately |
| A required input is missing | Set BLOCKED; record `blocked_reason`; stop |
| An error requires human judgment | Set BLOCKED; write issue to SESSION_SUMMARY.md |

See `agents/SESSION_LIMIT_RULE.md` for full turn-cap protocol.

---

## 6. Pre-BUILDER_DONE Checklist

Before moving command status to `BUILDER_DONE`, the Builder must confirm all of the following:

- [ ] All `output_required` artifacts exist in the repo
- [ ] All `acceptance_criteria` items are met — verify each one explicitly
- [ ] `handoff/CURRENT_PHASE.md` updated with status `BUILDER_DONE_PENDING_REVIEW`
- [ ] `handoff/SESSION_SUMMARY.md` updated with this session's changes
- [ ] `09_LOGS/PHASE_LOG.md` has a new entry for this session
- [ ] `logs/AGENT_ACTIVITY_LOG.md` has a new row for this session
- [ ] `git status` shows only files within `scope_files` as modified or new
- [ ] No secrets in any file changed this session

If all items pass → update command status to `BUILDER_DONE`, then `REVIEW_REQUESTED`.

---

## 7. Mandatory Final Output Format

Every Builder session must end with this structured summary (not prose):

```
## Phase X.X — Builder Done

### Files Created
- [list]

### Files Modified
- [list]

### Acceptance Criteria
| Criterion | Status |
|-----------|--------|
| [item] | PASS / FAIL |

### Risks / Blockers
[none, or description]

### Git Status
[output of git status --short]

### Checks
| Check | Result |
|-------|--------|
| Schema validation | PASS / FAIL |
| Secret scan | CLEAN / WARN |
| Scope check | PASS / WARN |

READY FOR CODEX REVIEW
```

---

## 8. How This Connects to Phase 0.6, 0.8, and 0.9

```
Owner / ChatGPT creates command (COMMAND_TEMPLATE.md or GITHUB_ISSUE_COMMAND_TEMPLATE.md)
    ↓ status: NEW → ASSIGNED
commands/COMMAND_INBOX.md  [Phase 0.6]
    ↓
Owner pastes shortcut token: RUN_CURRENT_COMMAND  [Phase 0.9]
    ↓
Builder resolves token → reads AGENT_RUN_PROTOCOL.md + BUILDER_PROTOCOL.md
    ↓ Session Start Checklist → Execute → Pre-BUILDER_DONE
    ↓ status: IN_PROGRESS → BUILDER_DONE → REVIEW_REQUESTED
Owner pastes shortcut token: REVIEW_CURRENT_COMMAND  [Phase 0.9]
    ↓
Reviewer resolves token → reads AGENT_RUN_PROTOCOL.md + REVIEWER_PROTOCOL.md
    ↓ status: REVIEW_PASS or REVIEW_FAIL
Owner approves
    ↓ status: OWNER_APPROVED → CLOSED
Owner commits → pastes: CLOSE_APPROVED_COMMAND  [Phase 0.9]
```

State machine: `commands/COMMAND_STATUS.md`
Transition rules: `docs/phase-0/PHASE_0_6_COMMAND_INTAKE.md`
Command modes (repo vs GitHub Issue): `commands/GITHUB_COMMAND_BRIDGE.md`  [Phase 0.8]
Shortcut definitions: `commands/COMMAND_SHORTCUTS.md`  [Phase 0.9]
Shortcut routing + error conditions: `commands/COMMAND_ROUTING_RULES.md` → Shortcut Routing section
