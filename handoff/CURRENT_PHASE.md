# Current Phase

Updated By: Claude Code (Builder) — 2026-05-28 (Phase 8 Build)

## Phase

Phase 8 — n8n Importable Workflow Skeletons

## Status

**BUILDER_DONE_PENDING_REVIEW**

## Current Command

Phase 8 build complete. Awaiting Codex review.
See `handoff/PHASE_8_HANDOFF.md` for full file list and validation checklist.

## Builder

Claude Code (AGT-02)

## Reviewer

Codex (AGT-03) — PENDING

## Next Gate

Codex reviews all Phase 8 files → PASS → Owner approves commit.
See `handoff/PHASE_8_HANDOFF.md` for Codex review instructions and commit instruction.

## Phase 8 Files

| File | Status |
|------|--------|
| `n8n/workflows/content_auto_skeleton.json` | Created |
| `n8n/workflows/creative_asset_auto_skeleton.json` | Created |
| `n8n/workflows/ads_pack_auto_skeleton.json` | Created |
| `n8n/workflows/crm_followup_auto_skeleton.json` | Created |
| `n8n/workflows/comment_inbox_reply_assistant_skeleton.json` | Created |
| `n8n/workflows/approval_publishing_skeleton.json` | Created |
| `docs/20_N8N_WORKFLOW_SKELETONS.md` | Created |
| `handoff/PHASE_8_HANDOFF.md` | Created |

## Previous Phase

Phase 7 — n8n Runtime Blueprint (commit 4bfbe96)
Phase 6 — OS Readiness Pack (commit f66e2e9)
Phase 5 — Sample Outputs for Vị Cuốn (commit 761240f)
Phase 4 — Module SOP + Output Templates (commit 8942fd7)
Phase 3 — Brand Brain + Input/Output Schemas (commit 93d7010)

## Guardrails

- Do not hardcode secrets or credentials.
- Do not auto-post, auto-reply, or auto-spend.
- Do not activate n8n workflows.
- Do not run ads or spend money.
- Do not commit until `OWNER_APPROVED`.
- .claude/ must NEVER be committed.
