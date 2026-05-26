# Phase 0.9 — Command Execution Shortcuts

Created By: Claude Code (Builder) — 2026-05-26

---

## Problem Being Solved

After Phases 0.6, 0.7, and 0.8, the command lifecycle is fully structured and the GitHub bridge is designed. But Owner still has to paste a long, role-specific prompt every time a new session starts:

- A Builder session requires copying ~200 words of instructions
- A Review session requires copying ~200 words of review criteria
- A fix session requires repeating the Reviewer's output plus new instructions
- Status checks require manually reading 3 separate files

Phase 0.9 introduces **Command Execution Shortcuts** — six named tokens that replace long prompts. Owner pastes one token; the agent resolves the full set of required actions from the active command in the repo.

---

## Objective

Define six shortcut tokens so that Owner can trigger any standard agent action with a single word:

| Shortcut | Replaces |
|----------|----------|
| `RUN_CURRENT_COMMAND` | Full Builder session prompt (~200 words) |
| `REVIEW_CURRENT_COMMAND` | Full Reviewer session prompt (~200 words) |
| `FIX_REVIEW_FAIL` | Fix-session instructions + listing of REVIEW_FAIL issues |
| `CLOSE_APPROVED_COMMAND` | Post-commit status update instructions |
| `CREATE_SESSION_SUMMARY` | SESSION_SUMMARY.md update instructions at turn 8 |
| `SHOW_CURRENT_STATUS` | Manual reading of 3 files to get current phase/command/status |

**Phase 0.9 does NOT automate command execution.** Shortcuts are human-readable tokens; an agent receives the token in chat and resolves it against the repo. Automation (n8n, GitHub Actions, API) is a future concern.

---

## What Changes After Phase 0.9

| Before Phase 0.9 | After Phase 0.9 |
|-------------------|-----------------|
| Owner pastes 200-word Builder prompt | Owner pastes `RUN_CURRENT_COMMAND` |
| Owner pastes 200-word Reviewer prompt | Owner pastes `REVIEW_CURRENT_COMMAND` |
| Owner pastes Reviewer issues + fix instructions | Owner pastes `FIX_REVIEW_FAIL` |
| Owner manually checks 3 files for status | Owner pastes `SHOW_CURRENT_STATUS` |
| SESSION_SUMMARY update requires explicit instruction | Owner pastes `CREATE_SESSION_SUMMARY` |
| Closing a command requires explaining the close flow | Owner pastes `CLOSE_APPROVED_COMMAND` |

---

## Files Delivered

| File | Purpose |
|------|---------|
| `commands/COMMAND_SHORTCUTS.md` | Defines all 6 shortcuts: role, trigger, required actions, error conditions, quick-reference table |
| `commands/COMMAND_ROUTING_RULES.md` | Updated: Shortcut Routing section added (role gating, error conditions per shortcut) |
| `agents/AGENT_RUN_PROTOCOL.md` | Updated: Phase 0.9 shortcut layer described in integration section |
| `agents/BUILDER_PROTOCOL.md` | Updated: Step 1 notes `RUN_CURRENT_COMMAND` as entry point |
| `agents/REVIEWER_PROTOCOL.md` | Updated: Identity check notes `REVIEW_CURRENT_COMMAND` as entry point |

---

## Shortcut Resolution Flow

```
Owner pastes shortcut token (e.g. RUN_CURRENT_COMMAND)
    │
    ▼
Agent reads commands/COMMAND_SHORTCUTS.md → resolves token to action list
    │
    ├── Confirm role matches shortcut's allowed role
    │       If mismatch → ROLE_CONFLICT → stop, report to Owner
    │
    ├── Confirm active command exists with required status
    │       If missing → NO_ACTIVE_COMMAND → stop, report to Owner
    │
    ├── Confirm command has all required fields
    │       If incomplete → NEED_COMMAND_CLARIFICATION → BLOCKED
    │
    └── Execute action list from shortcut definition
            │
            └── Output ends with shortcut's required ending phrase
```

---

## Integration with Prior Phases

```
Phase 0.6 — Command Intake: defines command lifecycle (10 states) and field schema
Phase 0.7 — Agent Run Protocol: defines how to run a session (checklist, turn cap, stop conditions)
Phase 0.8 — GitHub Command Bridge: defines two command modes (repo / GitHub Issue)
Phase 0.9 — Command Execution Shortcuts: defines tokens that trigger Phase 0.7 protocol without long prompts
```

Shortcuts do not replace protocols — they reference them. `RUN_CURRENT_COMMAND` invokes `BUILDER_PROTOCOL.md` in full; it just removes the need to paste those instructions.

---

## What Phase 0.9 Does NOT Do

- Does not automate command execution
- Does not call any API
- Does not create n8n workflows
- Does not connect shortcuts to GitHub Actions or LangGraph
- Does not open Phase 1

Automation of shortcut execution is a future concern (Phase 2+).

---

## Done Criteria — Phase 0.9

- [x] `COMMAND_SHORTCUTS.md` defines all 6 shortcuts with role, trigger status, actions, error conditions, quick-reference table
- [x] `COMMAND_ROUTING_RULES.md` updated with Shortcut Routing section covering role gating and all 5 error conditions
- [x] `BUILDER_PROTOCOL.md` updated to reference `RUN_CURRENT_COMMAND` at Step 1
- [x] `REVIEWER_PROTOCOL.md` updated to reference `REVIEW_CURRENT_COMMAND` at Identity Check
- [x] `AGENT_RUN_PROTOCOL.md` updated to describe shortcut layer in integration section
- [x] CMD-0.9-001 created in `COMMAND_INBOX.md` and `COMMAND_STATUS.md`
- [x] CMD-0.8-001 marked CLOSED in both files
- [x] Handoff and logs updated
- [x] No secrets in any Phase 0.9 file
