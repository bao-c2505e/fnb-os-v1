# Current Phase

Updated By: Claude Code (Builder) — 2026-05-26

## Phase

Phase 0.8 — GitHub Command Bridge

## Status

**REVIEW_REQUESTED**

## Current Command

**CMD-0.8-001** — Phase 0.8, GitHub Command Bridge
Status: `REVIEW_REQUESTED`
See full record: `commands/COMMAND_INBOX.md` → CMD-0.8-001 section

## Builder

Claude Code (AGT-02)

## Reviewer

Codex / GPT-4o (AGT-04)

## Next Gate

Codex reviews CMD-0.8-001 using `agents/REVIEWER_PROTOCOL.md`.
Acceptance criteria for review are in `commands/COMMAND_INBOX.md` → CMD-0.8-001.

If REVIEW_PASS → Owner approves CMD-0.8-001 → Owner commits → ChatGPT opens next phase.

## Phase 0.8 Files

| File | Status |
|------|--------|
| `docs/phase-0/PHASE_0_8_GITHUB_COMMAND_BRIDGE.md` | Complete — phase doc |
| `commands/GITHUB_COMMAND_BRIDGE.md` | Complete — mode guide + field/status mapping |
| `commands/GITHUB_ISSUE_COMMAND_TEMPLATE.md` | Complete — GitHub Issue template |
| `commands/COMMAND_ROUTING_RULES.md` | Complete — routing rules + error conditions |

## Previous Phase

Phase 0.7 — CLOSED (commit d4771a)

## Guardrails

- Do not hardcode secrets.
- Do not auto-post or auto-reply.
- Do not activate n8n workflows.
- Do not run ads or spend money.
- Do not modify files outside Phase 0.8 scope.
- Do not commit until `OWNER_APPROVED`.
