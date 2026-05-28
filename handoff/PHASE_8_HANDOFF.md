# Phase 8 Handoff

Phase: 8 — n8n Importable Workflow Skeletons
Created By: Claude Code (Builder, AGT-02) — 2026-05-28
Status: BUILDER_DONE_PENDING_REVIEW

---

## Files Created — Phase 8

| File | Type | Status |
|------|------|--------|
| `n8n/workflows/content_auto_skeleton.json` | n8n workflow JSON | Created |
| `n8n/workflows/creative_asset_auto_skeleton.json` | n8n workflow JSON | Created |
| `n8n/workflows/ads_pack_auto_skeleton.json` | n8n workflow JSON | Created |
| `n8n/workflows/crm_followup_auto_skeleton.json` | n8n workflow JSON | Created |
| `n8n/workflows/comment_inbox_reply_assistant_skeleton.json` | n8n workflow JSON | Created |
| `n8n/workflows/approval_publishing_skeleton.json` | n8n workflow JSON | Created |
| `docs/20_N8N_WORKFLOW_SKELETONS.md` | Documentation | Created |
| `handoff/PHASE_8_HANDOFF.md` | Handoff | This file |

## Files Updated — Phase 8

| File | Change |
|------|--------|
| `handoff/CURRENT_PHASE.md` | Updated to Phase 8 BUILDER_DONE_PENDING_REVIEW |
| `handoff/SESSION_SUMMARY.md` | Phase 8 session summary prepended |
| `logs/AGENT_ACTIVITY_LOG.md` | Phase 8 activity row prepended |
| `09_LOGS/PHASE_LOG.md` | Phase 8 entry prepended |

---

## Phase 8 Scope

Phase 8 converts the Phase 7 blueprint directions into importable n8n workflow JSON skeletons. Each skeleton:
- Is valid, importable n8n JSON
- Has `active: false` hard-coded
- Contains no real credentials, API keys, or production endpoints
- Includes Approval Gate nodes/steps
- Includes Log nodes/steps
- Includes Error Trigger + Stop and Error chain
- Uses mock/sample data aligned to Phase 3 schemas
- Contains Sticky Note warnings visible in n8n canvas

---

## Scope Boundaries — What Was NOT Done

| Excluded Item | Reason |
|--------------|--------|
| `hashtags` in content_auto output | Not in `content-output.schema.json` — Codex Phase 7 constraint |
| `human_review_required` in content_auto output | Not in `content-output.schema.json` — Codex Phase 7 constraint |
| Real Google Sheets / Supabase credential | Hard rule — no real credentials |
| Real Telegram Bot token | Hard rule — no real credentials |
| Real Meta / TikTok / Zalo API endpoints | Hard rule — no production publishing |
| `active: true` on any workflow | Hard rule |
| Real AI API calls in Code nodes | All Code nodes are JavaScript stubs |
| Production error notification (Telegram) | Stub only — not wired |

---

## Workflow Summary

| Workflow | Nodes | Trigger | Key Gate |
|---------|-------|---------|---------|
| content_auto_skeleton.json | 15 | Manual Trigger | If: Validation Pass + NoOp approval queue stub |
| creative_asset_auto_skeleton.json | 15 | Manual Trigger | If: Validation Pass + NoOp approval queue stub |
| ads_pack_auto_skeleton.json | 15 | Manual Trigger | If: Validation Pass + NoOp ads queue stub |
| crm_followup_auto_skeleton.json | 15 | Manual Trigger | human_review_required=true + NoOp queue stub |
| comment_inbox_reply_assistant_skeleton.json | 13 | Manual Trigger | If: Escalation Required + NoOp reply queue stub |
| approval_publishing_skeleton.json | 17 | Webhook (placeholder) | If: Is Approved + Switch: Item Type + 5 NoOp publish stubs |

---

## Validation Checklist

| Check | Result |
|-------|--------|
| All 6 workflow JSON files are valid JSON | PASS |
| `active: false` on all workflows | PASS |
| No real API keys or credentials | PASS — secret scan clean |
| No real platform endpoints | PASS — all NoOp stubs |
| All workflows have Approval Gate step | PASS |
| All workflows have Log step | PASS |
| All workflows have Error Trigger chain | PASS |
| All workflows have Sticky Note warning | PASS |
| `hashtags` absent from content_auto | PASS — not in schema |
| `human_review_required` absent from content_auto output | PASS — not in schema |
| `human_review_required: true` in crm_followup and comment_inbox | PASS — matches schema const |
| `compliance_notes` present in ads_pack mock output | PASS |
| Escalation gate present in comment_inbox workflow | PASS |
| Escalated cases: draft_reply=null | PASS |
| approval_publishing blocks non-Approved items | PASS |
| Mock data uses schema-valid enum values | PASS |
| Log entries conform to log-entry.schema.json fields | PASS |
| Scope check — no files outside scope_files | PASS |

---

## Known Limitations

1. Code nodes are JavaScript stubs — no real AI calls in skeleton.
2. All log writes are in-memory — no real Sheets/Supabase writes.
3. All approval queue writes are NoOp — no real queue populated.
4. Mock data uses placeholder strings — must be replaced before production.
5. Webhook in approval_publishing is unconfigured.
6. Error notifications (Telegram) are not wired.
7. n8n typeVersion numbers may need minor adjustment for specific n8n instance version.

---

## Codex Review Instructions

Codex, please review:

1. **JSON validity** — All 6 files in `n8n/workflows/` must be valid JSON.
2. **active=false** — Verify `"active": false` in each workflow.
3. **No credentials** — Verify no real API keys, tokens, or passwords in any JSON.
4. **No production endpoints** — Verify all publishing/sending/spending nodes are NoOp stubs.
5. **Schema alignment** — Verify mock outputs contain required fields per Phase 3 schemas.
6. **Codex constraint** — Verify `hashtags` and `human_review_required` are absent from `content_auto_skeleton.json` output.
7. **Approval gate** — Verify approval gate exists in each workflow.
8. **Log step** — Verify log step exists in each workflow.
9. **Error chain** — Verify Error Trigger → Set Error Log → Stop and Error in each workflow.
10. **docs/20** — Verify import instructions, validation table, and limitation notes are accurate.

Output: PASS / PASS WITH NOTES / FAIL

---

## Phase 9 Recommendation

Phase 9 should focus on one of:
- **Brand Brain fill** — Owner provides real values for all `REPLACE_WITH_*` Brand Brain fields
- **Credential configuration** — Owner sets up real n8n credentials (Google Sheets, Anthropic API)
- **Workflow activation test** — Owner imports one skeleton, fills credentials, tests manual execution end-to-end
- **Approval channel setup** — Configure Google Sheets approval queue as primary approval channel

Prerequisite: Owner imports at least one skeleton into n8n and confirms it imports without errors.

---

## Commit Instruction

Do NOT commit Phase 8 files until:
1. Codex issues PASS or PASS WITH NOTES on this handoff
2. Owner issues `OWNER_APPROVED`
3. Builder runs `git status` and confirms only Phase 8 files are staged

Commit message template:
```
docs: add phase 8 n8n workflow skeletons

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
```
