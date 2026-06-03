# Phase 37 Handoff — Creative Asset Auto Set Input Variables Code Node Patch

Created By: Claude Code (Builder, AGT-02) — 2026-06-03
Phase: 37 — Creative Asset Auto Set Input Variables Code Node Patch
Type: BUILD_READY
Branch: main

---

## Phase 37 Summary

Phase 37 patches `n8n/workflows/creative_asset_auto_skeleton.json` to replace the `Set Input Variables` node from a Set node (typeVersion 3, `assignments.assignments` format — unrecognized by n8n) with a Code node (typeVersion 2, `jsCode` — proven reliable in this workflow) that returns all 14 safe sample input fields as an explicit JS object.

Root cause confirmed in Phase 36: n8n cannot parse the `assignments.assignments` format used by Set node typeVersion 3 — this was the cause of the empty output across Phase 27, Phase 33, and Phase 36. The Code node approach bypasses this format issue entirely.

No n8n import or execution performed. Phase 38 = re-import patched workflow + execution retest.

---

## Phase Context

| Item | Detail |
|------|--------|
| Phase 36 result | EVIDENCE_RECORDED — FAIL (commit `66f8c28`) |
| Root cause | n8n Set node typeVersion 3 / `assignments.assignments` format mismatch |
| Duplicate workflow issue | Eliminated (Phase 35) — not the cause |
| HEAD at start of Phase 37 | `66f8c28` (= origin/main) |
| File patched | `n8n/workflows/creative_asset_auto_skeleton.json` |
| Node patched | `Set Input Variables` (ID `a2000002-0002-4001-a002-200000000002`) |
| Change | Set node typeVersion 3 → Code node typeVersion 2 |
| Node name | UNCHANGED — `Set Input Variables` |
| Node position | UNCHANGED — [500, 420] |
| Connections | UNCHANGED — connections reference node NAME, not node type |
| `active` field | UNCHANGED — `false` |

---

## Patch Detail

### Before (Set node — unrecognized format)

```
"type": "n8n-nodes-base.set"
"typeVersion": 3
"parameters": { "assignments": { "assignments": [...19 items...] }, "options": {} }
```

### After (Code node — explicit JS object)

```
"type": "n8n-nodes-base.code"
"typeVersion": 2
"parameters": {
  "jsCode": "return [{ json: { request_id, brand_name, campaign_name, channel, asset_type,
    product_name, offer, target_audience, key_message, tone_of_voice, visual_direction,
    required_output, approval_required: true, sandbox_mode: true } }];"
  "mode": "runOnceForAllItems"
}
```

### Fields returned by Code node (14 fields)

| Field | Value | Type |
|-------|-------|------|
| request_id | creative_asset_sandbox_001 | string |
| brand_name | Vi Cuon | string |
| campaign_name | Sandbox Creative Asset Test | string |
| channel | facebook | string |
| asset_type | social_static_post | string |
| product_name | Heo quay nuong lu | string |
| offer | Sandbox sample only - no real promotion | string |
| target_audience | office workers and local food lovers in Vinh | string |
| key_message | Fresh rolled food with warm street-premium visual direction | string |
| tone_of_voice | friendly, appetizing, local, premium-but-accessible | string |
| visual_direction | warm brown, orange accent, clean food photography style | string |
| required_output | design_brief | string |
| approval_required | true | **boolean** |
| sandbox_mode | true | **boolean** |

---

## Files Created (Phase 37)

| File | Change |
|------|--------|
| `handoff/PHASE_37_HANDOFF.md` | CREATED — this file |

---

## Files Modified (Phase 37)

| File | Change |
|------|--------|
| `n8n/workflows/creative_asset_auto_skeleton.json` | PATCHED — Set Input Variables: Set node → Code node |
| `handoff/CURRENT_PHASE.md` | Updated to Phase 37 BUILD_READY |
| `handoff/SESSION_SUMMARY.md` | New session entry prepended |
| `logs/AGENT_ACTIVITY_LOG.md` | New row prepended |
| `09_LOGS/PHASE_LOG.md` | New entry prepended |

---

## Files NOT Modified (Phase 37)

| File | Status |
|------|--------|
| All other `n8n/workflows/*.json` | UNTOUCHED |
| All `docs/` files | UNTOUCHED |
| All previous handoff files | UNTOUCHED |

---

## Validation Results (Phase 37)

| Check | Result |
|-------|--------|
| JSON valid (`validate_json.py`) | ALL PASS |
| `active=false` confirmed (`check_n8n_workflows.py`) | ALL PASS — 6/6 |
| Secret scan (`check_no_secrets.py`) | 3 pre-existing findings (.env gitignored + Phase 20 doc) — NOT introduced by Phase 37 |
| Only creative_asset workflow changed | YES — `git diff --stat` shows 1 file |
| Only Set Input Variables node changed | YES |
| Node type converted | `n8n-nodes-base.set` → `n8n-nodes-base.code` |
| typeVersion | 3 → 2 |
| Node name unchanged | YES — `Set Input Variables` |
| Node position unchanged | YES — [500, 420] |
| Connections intact | YES — Manual Trigger → Set Input Variables → Code: Load Brand Brain |
| approval_required | boolean `true` (not string) |
| sandbox_mode | boolean `true` (not string) |
| brand_name | `Vi Cuon` (no Unicode, no duplicate) |
| No credential in jsCode | CLEAN |
| No API key in jsCode | CLEAN |

---

## Runtime Safety Confirmation (Phase 37)

| Item | Status |
|------|--------|
| Workflow JSON patched | YES — Set Input Variables node only |
| `active = true` introduced | NO |
| Real credentials added | NO |
| Real API calls added | NO |
| Auto-post / auto-reply / ad spend | NO |
| Production system modified | NO |
| n8n workflow executed by Builder | NO |
| n8n workflow imported by Builder | NO |
| Secret scan new content | CLEAN |
| Other workflow files modified | NO |
| Other nodes modified | NO |

---

## Acceptance Criteria (Phase 37)

| Criterion | Status |
|-----------|--------|
| `Set Input Variables` node type → `n8n-nodes-base.code` | PASS |
| typeVersion → 2 | PASS |
| jsCode returns 14 fields as explicit JS object | PASS |
| `approval_required: true` (boolean) | PASS |
| `sandbox_mode: true` (boolean) | PASS |
| `brand_name: "Vi Cuon"` (no Unicode, no duplicate) | PASS |
| Node name unchanged: `Set Input Variables` | PASS |
| Node position unchanged: [500, 420] | PASS |
| Connections unchanged | PASS |
| `active` remains `false` | PASS |
| No credentials added | PASS |
| No API calls added | PASS |
| JSON valid (`validate_json.py` ALL PASS) | PASS |
| Only creative_asset workflow changed | PASS |
| Only Set Input Variables node changed | PASS |
| Secret scan CLEAN (new content) | PASS |

---

## Owner Next Action

1. Review `git diff n8n/workflows/creative_asset_auto_skeleton.json`
2. Review this handoff
3. Authorize commit and push: `workflow: convert creative asset input node to code sample`
4. Proceed to Phase 38 — Creative Asset Auto Code Node Patch Re-import Only
5. In Phase 38: Owner imports patched JSON into `CURRENT CLEAN SANDBOX` (fresh import or update), then Phase 39 = execution retest

---

## Codex Review Instructions

1. Confirm `n8n/workflows/creative_asset_auto_skeleton.json`:
   - Only `Set Input Variables` node changed
   - `"type": "n8n-nodes-base.code"`, `"typeVersion": 2`
   - `jsCode` returns 14 fields with explicit values
   - `approval_required: true` and `sandbox_mode: true` as boolean literals (not strings)
   - `active: false` unchanged
   - All connections unchanged
   - No credentials, no API keys, no REPLACE_WITH_* secrets in jsCode
2. Confirm no other workflow JSON changed
3. Output: PASS / PASS WITH NOTES / BLOCK

---

## Phase Connections

| Phase | Description | Status |
|-------|-------------|--------|
| Phase 30 | Safe Sample Input Patch — Set node `assignments.assignments` format (unrecognized by n8n) | DONE + PUSHED |
| Phase 33 | Manual Execution — FAIL (contaminated canvas) | DONE + PUSHED |
| Phase 35 | Clean Workflow Isolation — PASS | DONE + PUSHED (`6eac786`) |
| Phase 36 | Clean Sandbox Execution Retest — FAIL (Set node format confirmed) | DONE + PUSHED (`66f8c28`) |
| **Phase 37** | **Set Input Variables Code Node Patch (this phase)** | **BUILD_READY** |
| Phase 38 | Re-import patched workflow to `CURRENT CLEAN SANDBOX` | NOT STARTED |
| Phase 39 | Execution retest on re-imported workflow | NOT STARTED |
