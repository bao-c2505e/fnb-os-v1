# Phase 0.7 — Agent Run Protocol

Created By: Claude Code (Builder) — 2026-05-26

---

## Objective

Define the operational protocol that agents must follow when executing a command issued through the Phase 0.6 Command Intake Layer.

Phase 0.6 established *what* a command looks like and *what lifecycle states it moves through*.
Phase 0.7 establishes *how* an agent actually runs a session from start to finish:
- How to start safely
- How to stay in scope
- How to log activity
- How to hand off
- When to stop
- How to review

---

## Files Delivered

| File | Role |
|------|------|
| `agents/AGENT_RUN_PROTOCOL.md` | Master protocol — session start checklist, execution constraints, stop conditions, pre-BUILDER_DONE checklist, mandatory output format |
| `agents/BUILDER_PROTOCOL.md` | Builder (Claude Code) step-by-step: accept command, lock scope, execute, pre-BUILDER_DONE checklist, final output format, allowed status transitions |
| `agents/REVIEWER_PROTOCOL.md` | Reviewer (Codex) step-by-step: read outputs, acceptance criteria check, scope/secret/role/safety checks, mandatory PASS/FAIL output format |
| `agents/SESSION_LIMIT_RULE.md` | 10-turn cap formalization: checkpoints at turn 8 and turn 10, 7 required SESSION_SUMMARY fields, resume protocol |

---

## How Phase 0.7 Connects to Phase 0.6

```
Owner / ChatGPT
    │
    │  creates command using COMMAND_TEMPLATE.md
    ▼
commands/COMMAND_INBOX.md   ← Phase 0.6
    │  status: ASSIGNED
    │
    │  Builder reads AGENT_RUN_PROTOCOL.md + BUILDER_PROTOCOL.md
    ▼
Session Start Checklist (8 items)         ← Phase 0.7
    │
    │  Scope Lock → Execute → Turn 8 check → Pre-BUILDER_DONE
    ▼
status: BUILDER_DONE → REVIEW_REQUESTED
    │
    │  Reviewer reads AGENT_RUN_PROTOCOL.md + REVIEWER_PROTOCOL.md
    ▼
Acceptance Criteria Check                  ← Phase 0.7
Scope / Secret / Role / Safety Checks
    │
    ▼
REVIEW RESULT: PASS or FAIL
    │
    │  If PASS → Owner approves
    ▼
status: OWNER_APPROVED → Owner commits → CLOSED
```

State machine lives in `commands/COMMAND_STATUS.md`.
Transition ownership lives in `docs/phase-0/PHASE_0_6_COMMAND_INTAKE.md`.

---

## Role Map — Phase 0.7

| Role | Agent | Protocol File |
|------|-------|--------------|
| Builder | Claude Code (AGT-02) | `agents/BUILDER_PROTOCOL.md` |
| Reviewer | Codex / GPT-4o (AGT-04) | `agents/REVIEWER_PROTOCOL.md` |
| Chief Architect | ChatGPT (AGT-01) | Issues commands, opens phases |
| Approver | Owner | Approves, commits, pushes |

---

## Approval Gate

No commit or push may occur without `OWNER_APPROVED` status on the command.
No real-world action (post, reply, ad, workflow activation) may occur without Owner approval.
This gate applies to every phase from 0.7 onward.

---

## What Phase 0.7 Does NOT Define

These are already defined in earlier infrastructure — Phase 0.7 references them, does not restate:

| Topic | Source |
|-------|--------|
| Agent identities and capabilities | `06_HANDOFF/AGENT_REGISTRY.md` |
| File ownership matrix | `06_HANDOFF/AGENT_COMMUNICATION_RULES.md` |
| Hard limits per role | `docs/agent-system/OPERATING_RULES.md` |
| Command intake lifecycle (10 states) | `docs/phase-0/PHASE_0_6_COMMAND_INTAKE.md` |
| Command field definitions | `schemas/command.schema.json` |

---

## Done Criteria — Phase 0.7

- [x] `agents/AGENT_RUN_PROTOCOL.md` — master protocol with session start checklist, constraints, stop conditions, pre-BUILDER_DONE checklist, mandatory output format
- [x] `agents/BUILDER_PROTOCOL.md` — Builder step-by-step with 7 pre-BUILDER_DONE items, status transitions, forbidden actions
- [x] `agents/REVIEWER_PROTOCOL.md` — Reviewer step-by-step with 6 checks, unambiguous PASS/FAIL output format
- [x] `agents/SESSION_LIMIT_RULE.md` — 10-turn cap, turn 8 checkpoint, 7 required SESSION_SUMMARY fields, resume protocol
- [x] No content duplicated from Phase 0.5 or 0.6 infrastructure
- [x] Handoff and logs updated
- [x] No secrets in any Phase 0.7 file
- [x] `git status` shows only Phase 0.7 scope files
