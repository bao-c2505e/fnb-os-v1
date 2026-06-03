# Phase 36 — Creative Asset Auto Current Clean Sandbox Manual Execution Retest

Created By: Claude Code (Builder, AGT-02) — 2026-06-03
Updated By: Claude Code (Builder, AGT-02) — 2026-06-03 (Phase 36 Evidence Recording — FAIL)
Phase: 36 — Creative Asset Auto Current Clean Sandbox Manual Execution Retest
Type: EVIDENCE_RECORDED — FAIL
Branch: main

---

## 1. Purpose

Retest the clean sandbox workflow `CURRENT CLEAN SANDBOX` after Phase 35 successfully isolated it from the contaminated canvas. Phase 33 FAIL was caused by running on a contaminated workflow with two parallel node clusters. Phase 35 confirmed the new clean workflow has exactly one skeleton cluster and has not been executed yet.

**Goal of Phase 36:** Owner manually executes `CURRENT CLEAN SANDBOX` once and inspects `Set Input Variables` output to determine whether the Phase 30 patch (19 fields) is visible in n8n.

- If 19 fields visible → Phase 30 patch correct, no Code node fix needed. Proceed to evidence recording.
- If output still empty → Code node fix (Phase 37) is confirmed needed.

**Phase 36 scope:** Runbook + evidence form creation only. Claude does not operate n8n. Owner performs manual execution.

---

## 2. Preconditions

All of the following must be true before Owner executes:

| Precondition | Required | Source |
|--------------|----------|--------|
| Phase 35 result | PASS | Phase 35 evidence (2026-06-03) |
| Workflow name | `FnB OS V1 — Creative Asset Auto [SKELETON] — CURRENT CLEAN SANDBOX` | Owner confirmed Phase 35 |
| Canvas cluster count | Exactly 1 skeleton cluster | Owner confirmed Phase 35 |
| Duplicate suffix nodes | NONE (`Set Input Variables1` etc. absent) | Owner confirmed Phase 35 |
| Workflow active status | INACTIVE | Owner confirmed Phase 35 |
| Credentials attached | NONE | Owner confirmed Phase 35 |
| Manual execution since isolation | NOT YET performed | Owner confirmed Phase 35 |
| n8n instance | Sandbox only: `https://n8n.baon8n.blog` | Prior phases |

---

## 3. Owner Execution Steps

**Claude does not operate n8n. Owner performs all steps below.**

### Pre-execution checks (before clicking Execute)

1. Open n8n sandbox: `https://n8n.baon8n.blog`
2. Open workflow: `FnB OS V1 — Creative Asset Auto [SKELETON] — CURRENT CLEAN SANDBOX`
3. Confirm workflow name matches exactly.
4. Confirm Active toggle is OFF (grey/inactive).
5. Do NOT click Publish.
6. Do NOT toggle Active ON.
7. Do NOT attach credentials to any node.
8. Confirm canvas shows exactly 1 skeleton cluster (no `1`-suffix nodes visible).

### Execution

9. Click **Execute workflow** (Manual Trigger).
10. Wait for execution to complete — all nodes should turn green on the happy path.

### Inspection

11. Click node: **Set Input Variables**
12. Open the **Output** tab (not Input tab).
13. Inspect what is shown:
    - If fields are listed → record all field names and values.
    - If message "No fields - item(s) exist, but they're empty" → FAIL — record and stop.
    - If message "Currently no items exist" → FAIL — record and stop.
14. Do NOT edit nodes or fields in the n8n UI.
15. Do NOT add fields manually in the n8n editor.
16. Record all observations in the Evidence Form (Section 7).

---

## 4. Expected Output

If Phase 30 patch is correctly loaded by n8n, `Set Input Variables` output panel must show the following 19 fields:

| # | Field name | Expected value | Type |
|---|-----------|---------------|------|
| 1 | brand_id | VQ | string |
| 2 | brand_name | Vi Cuon | string |
| 3 | brief_request | REPLACE_WITH_OWNER_BRIEF_REQUEST | string |
| 4 | asset_type | social_static_post | string |
| 5 | platform | Facebook | string |
| 6 | format | 1:1 square 1080x1080 | string |
| 7 | objective | Engagement | string |
| 8 | request_id | creative_asset_sandbox_001 | string |
| 9 | campaign_name | Sandbox Creative Asset Test | string |
| 10 | channel | facebook | string |
| 11 | product_name | Heo quay nuong lu | string |
| 12 | offer | Sandbox sample only - no real promotion | string |
| 13 | target_audience | office workers and local food lovers in Vinh | string |
| 14 | key_message | Fresh rolled food with warm street-premium visual direction | string |
| 15 | tone_of_voice | friendly, appetizing, local, premium-but-accessible | string |
| 16 | visual_direction | warm brown, orange accent, clean food photography style | string |
| 17 | required_output | design_brief | string |
| 18 | approval_required | true | boolean |
| 19 | sandbox_mode | true | boolean |

**Key verification targets:**
- `brand_name` = `Vi Cuon` (ASCII — no Unicode `Vị Cuốn`, no duplicate `brand_name` field)
- `approval_required` = `true` as **boolean** (not string `"true"`)
- `sandbox_mode` = `true` as **boolean** (not string `"true"`)
- All 19 fields present, no field missing

**Note on `brief_request`:** Value `REPLACE_WITH_OWNER_BRIEF_REQUEST` is expected and acceptable — this is a placeholder, not a failure.

---

## 5. PASS Criteria

Phase 36 PASS if ALL of the following:

| Criterion | Required |
|-----------|----------|
| Manual execution performed by Owner once | YES |
| Execution completes without error (green nodes on happy path) | YES |
| `Set Input Variables` output panel shows fields (not empty message) | YES |
| "No fields - item(s) exist, but they're empty" message absent | YES |
| "Currently no items exist" message absent | YES |
| At minimum `brand_name`, `approval_required`, `sandbox_mode` visible | YES |
| No duplicate `brand_name` field | YES |
| `approval_required` = boolean `true` (not string) | YES |
| `sandbox_mode` = boolean `true` (not string) | YES |
| Workflow remains INACTIVE after execution | YES |
| No credentials attached | YES |
| No real API calls | YES |
| No production side effect | YES |

---

## 6. FAIL Criteria

Phase 36 FAIL if ANY of:

| Fail Condition | Action |
|----------------|--------|
| Output panel still shows "No fields - item(s) exist, but they're empty" | STOP — record evidence — do NOT edit UI |
| Parameters panel shows "Currently no items exist" | STOP — record evidence |
| Expected sample fields missing from output | STOP — record evidence |
| Execution errors on any node | STOP — record error details |
| Workflow somehow activated | STOP — deactivate immediately — record |

**If FAIL:**
- Do NOT edit nodes or fields in the n8n UI.
- Do NOT add fields manually.
- Do NOT attempt a second execution without Builder guidance.
- Stop and fill the Evidence Form (Section 7) with FAIL details.
- Recommended next phase: **Phase 37 — Creative Asset Auto Set Input Variables Code Node Patch**

---

## 7. Evidence Form

Owner evidence received 2026-06-03:

```
Phase 36 Evidence:
- Date/time: 2026-06-03
- n8n instance URL: https://n8n.baon8n.blog
- Workflow name (exact): FnB OS V1 — Creative Asset Auto [SKELETON] — CURRENT CLEAN SANDBOX
- Workflow active status before execution: INACTIVE / not activated
- Manual execution performed: YES
- Workflow published: NO
- Credentials attached: NO / NONE
- API calls observed: NO / NONE
- Production side effect: NO
- Canvas clean before execution: YES
- Duplicate suffix nodes visible: NO
- Set Input Variables node count on main path: 1
- Set Input Variables node clicked: YES
- Output item count: 1
- Output fields visible: NO
- Empty item message present ("No fields - item(s) exist, but they're empty"): YES (FAIL)
- "Currently no items exist" in parameters panel: YES (FAIL)
- Expected Phase 30 safe sample fields missing: YES
- request_id field visible: NO
- brand_name field visible: NO
- approval_required visible: NO
- sandbox_mode visible: NO
- Total fields visible (count): 0
- Downstream IF Validation Pass node: shows fields from later Code nodes / placeholders
- Duplicate brand_name field exists: N/A — no fields visible
- Workflow active status after execution: INACTIVE
- Phase 36 result: FAIL
- Notes: Tested on CURRENT CLEAN SANDBOX — duplicate workflow/canvas issue no longer main cause.
  Root cause confirmed: n8n Set node typeVersion 3 / assignments.assignments JSON format mismatch.
  Downstream Code nodes use || fallback so execution continues but Set node output is empty.
- Ready for next phase: YES — Phase 37: Set Input Variables Code Node Patch
```

**Evidence Result: FAIL**
**Architect conclusion:** Root cause is n8n Set node typeVersion / JSON parameter format mismatch. Duplicate workflow issue eliminated as cause. Phase 37 = Code Node Patch confirmed.

---

## 8. Safety Checklist

| Item | Phase 36 Status |
|------|----------------|
| Workflow JSON changed in repo | NO |
| `active = true` introduced in repo | NO |
| Secrets added | NO |
| Credentials added | NO |
| Real API calls added | NO |
| n8n execution performed by Builder/Claude | NO — Owner only |
| Workflow activated | NO |
| Workflow published | NO |
| Production side effect risk | NO |
| UI editing of nodes | NO — forbidden |

---

## 9. Recommended Phase 37

### If Phase 36 PASS:
**Phase 37 — Creative Asset Auto Clean Sandbox Execution Evidence Recording**

Goal: Record full evidence pack for Phase 36 PASS. Confirm all 19 fields, boolean types, downstream nodes (Code: Load Brand Brain → Code: AI Generate Creative Brief → Validate → approval_status=Draft → Log → NoOp). Update phase docs. Phase 30 patch confirmed correct. Proceed to Phase 38+ module planning.

### If Phase 36 FAIL:
**Phase 37 — Creative Asset Auto Set Input Variables Code Node Patch**

Goal: Replace `Set Input Variables` node (typeVersion 3) with a `Code` node (typeVersion 2) that returns all 19 fields as a JS object. This approach bypasses the `assignments.assignments` format that n8n cannot parse. JS code for the replacement was specified in Phase 34 Section 5. Connections reference node NAME — keeping the name `Set Input Variables` preserves all existing connections.

---

## 10. Phase Connections

| Phase | Description | Status |
|-------|-------------|--------|
| Phase 30 | Safe Sample Input Patch — 19 fields added to repo JSON | DONE + PUSHED |
| Phase 32 | Re-import — canvas contaminated | DONE + PUSHED |
| Phase 33 | Manual Execution — FAIL (contaminated canvas) | DONE + PUSHED |
| Phase 34 | Debug Planning — contamination confirmed | DONE + PUSHED |
| Phase 35 | Clean Workflow Isolation — PASS | DONE + PUSHED (`6eac786`) |
| **Phase 36** | **Current Clean Sandbox Manual Execution Retest (this phase)** | **EVIDENCE_RECORDED — FAIL** |
| Phase 37 | Set Input Variables Code Node Patch (FAIL path — confirmed) | NOT STARTED |
| Phase 38+ (TBD) | Module planning / next workflow | NOT STARTED |

---

## 11. Safety Confirmation

| Item | Confirmed |
|------|-----------|
| Workflow JSON modified in Phase 36 | NO |
| `active = true` introduced | NO |
| Real credentials added | NO |
| Real API calls added | NO |
| Auto-post / auto-reply / ad spend | NO |
| Production system modified | NO |
| n8n execution performed by Builder | NO |
| n8n import performed by Builder | NO |
| Secret scan (new files) | CLEAN |
| Scope creep beyond runbook/evidence creation | NO |
