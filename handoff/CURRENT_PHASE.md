# Current Phase

Updated By: Claude Code (Builder) — 2026-05-26

## Phase

Phase 0.7 — Agent Run Protocol

## Status

**REVIEW_REQUESTED**

## Current Command

**CMD-0.7-001** — Phase 0.7, Agent Run Protocol
Status: `REVIEW_REQUESTED`
See full record: `commands/COMMAND_INBOX.md` → CMD-0.7-001 section

## Builder

Claude Code (AGT-02)

## Reviewer

Codex / GPT-4o (AGT-04)

## Next Gate

Codex reviews CMD-0.7-001 using `agents/REVIEWER_PROTOCOL.md`.
Acceptance criteria for review are in `commands/COMMAND_INBOX.md` → CMD-0.7-001.

If REVIEW_PASS → Owner approves CMD-0.7-001 → Owner commits → ChatGPT opens next phase.

## Phase 0.7 Files

| File | Status |
|------|--------|
| `agents/AGENT_RUN_PROTOCOL.md` | Complete — master protocol |
| `agents/BUILDER_PROTOCOL.md` | Complete — Builder step-by-step |
| `agents/REVIEWER_PROTOCOL.md` | Complete — Reviewer step-by-step |
| `agents/SESSION_LIMIT_RULE.md` | Complete — 10-turn cap + SESSION_SUMMARY fields |
| `docs/phase-0/PHASE_0_7_AGENT_RUN_PROTOCOL.md` | Complete — phase doc |

## Guardrails

- Do not hardcode secrets.
- Do not auto-post or auto-reply.
- Do not activate n8n workflows.
- Do not run ads or spend money.
- Do not modify files outside Phase 0.7 scope.
- Do not commit until `OWNER_APPROVED`.
