# Phase 33 — Creative Asset Auto Sandbox Manual Execution Check

Created By: Claude Code (Builder, AGT-02) — 2026-06-03
Phase: 33 — Creative Asset Auto Sandbox Manual Execution Check
Type: RUNBOOK_READY — OWNER ACTION REQUIRED
Branch: main

---

## 1. Purpose

Owner executes the `FnB OS V1 — Creative Asset Auto [SKELETON]` workflow manually in n8n sandbox to verify that the Phase 30 safe sample input patch is working correctly.

Primary verification target: the `Set Input Variables` node output panel must show all 19 safe sample fields — the Phase 27 "No fields - item(s) exist, but they're empty." message must be gone.

**Phase 33 allows Owner manual execution in n8n sandbox.**
No activation. No real credentials. No real API calls. No production side effect.
Claude Code does not operate n8n. All n8n actions are Owner manual only.

---

## 2. Preconditions

All of the following must be true before Owner executes:

| Item | Required State | Source |
|------|---------------|--------|
| Phase 30 safe sample input patch | DONE + PUSHED (commit `18c681d`) | GitHub |
| Phase 31 planning | DONE + PUSHED (commit `d6570f0`) | GitHub |
| Phase 32 re-import | DONE + PUSHED (commit `11268bb`) | GitHub |
| Workflow re-imported in n8n sandbox | YES — confirmed in Phase 32 evidence | Phase 32 |
| Workflow active status | inactive (OFF) | n8n sandbox |
| Credentials attached | NONE | n8n sandbox |
| Previous execution count | 1 (from Phase 27) or more — sandbox only | n8n sandbox |
| Workflow JSON in repo | unchanged — `n8n/workflows/creative_asset_auto_skeleton.json` | GitHub |

---

## 3. Owner Manual Execution Steps

**Before executing — confirm pre-execution state:**

```
1. Open n8n sandbox.
2. Navigate to workflow: FnB OS V1 — Creative Asset Auto [SKELETON]
3. Confirm workflow is INACTIVE (active toggle OFF / grey).
4. Confirm NO credentials are attached to any node.
5. Confirm you are in SANDBOX — not production.
```

**Execution steps:**

```
Step 1.  With workflow open and inactive, click: Execute workflow
         (from the Manual Trigger node or the top Execute button).

Step 2.  Wait for the execution to complete (all nodes turn green
         on the happy path, or workflow stops at a stub/error node).

Step 3.  Click the Set Input Variables node.

Step 4.  In the output panel, confirm the OUTPUT tab (not INPUT tab).
         Look for the list of fields in the JSON output.

Step 5.  Verify the fields are present (see Section 4 for expected
         values).

Step 6.  Continue clicking through each downstream node to observe
         the full execution path:
         - Code: Load Brand Brain
         - Code: AI Generate Creative Brief
         - Code: Validate Required Fields
         - If: Validation Pass → TRUE branch
         - Set: approval_status = Draft
         - Code: Write Log Entry
         - NoOp: STUB — Send to Approval Queue

Step 7.  Check the final node output. Confirm:
         - approval_status = Draft
         - logWritten = true
         - approvalQueueStubReached = true

Step 8.  Record all observations in the Evidence Form (Section 6).

Step 9.  Do NOT click Activate.
Step 10. Do NOT attach any credentials.
Step 11. Do NOT publish the workflow.
Step 12. Do NOT modify the workflow directly in n8n UI.
```

---

## 4. Expected Set Input Variables Output

After execution, clicking the `Set Input Variables` node output panel should show these fields:

| Field | Expected Value | Type |
|-------|---------------|------|
| `brand_id` | `VQ` | string |
| `brand_name` | `Vi Cuon` | string |
| `brief_request` | `REPLACE_WITH_OWNER_BRIEF_REQUEST` | string |
| `asset_type` | `social_static_post` | string |
| `platform` | `Facebook` | string |
| `format` | `1:1 square 1080x1080` | string |
| `objective` | `Engagement` | string |
| `request_id` | `creative_asset_sandbox_001` | string |
| `campaign_name` | `Sandbox Creative Asset Test` | string |
| `channel` | `facebook` | string |
| `product_name` | `Heo quay nuong lu` | string |
| `offer` | `Sandbox sample only - no real promotion` | string |
| `target_audience` | `office workers and local food lovers in Vinh` | string |
| `key_message` | `Fresh rolled food with warm street-premium visual direction` | string |
| `tone_of_voice` | `friendly, appetizing, local, premium-but-accessible` | string |
| `visual_direction` | `warm brown, orange accent, clean food photography style` | string |
| `required_output` | `design_brief` | string |
| `approval_required` | `true` | **boolean** |
| `sandbox_mode` | `true` | **boolean** |

**Total: 19 fields.**

Key checks:
- `brief_request` value `REPLACE_WITH_OWNER_BRIEF_REQUEST` is expected — it is a placeholder stub, not a failure.
- `approval_required` must be boolean `true` — not string `"true"`.
- `sandbox_mode` must be boolean `true` — not string `"true"`.
- There must be **no duplicate** `brand_name` field.
- The Phase 27 message **"No fields - item(s) exist, but they're empty."** must be **gone**.

---

## 5. Success Criteria

| Criterion | Required |
|-----------|---------|
| Manual execution completed or reached expected safe stop | YES |
| `Set Input Variables` output panel opened | YES |
| Output fields visible (not empty list) | YES |
| "No fields - item(s) exist, but they're empty." message gone | YES |
| At least 19 fields visible in output | YES |
| `brand_name` = `Vi Cuon` | YES |
| `approval_required` = boolean `true` | YES |
| `sandbox_mode` = boolean `true` | YES |
| No duplicate `brand_name` field | YES |
| `approval_status` = `Draft` (from Set node downstream) | YES |
| `logWritten` = `true` | YES |
| `approvalQueueStubReached` = `true` | YES |
| Workflow remains INACTIVE after execution | YES |
| No credentials attached during execution | YES |
| No real API calls observed | YES |
| No auto-post / auto-reply | YES |
| No production side effect | YES |

---

## 6. Evidence Form

Owner fills after completing Phase 33 execution:

```
Phase 33 Evidence — Creative Asset Auto Sandbox Manual Execution Check
Date: _______________
Operator: _______________

Workflow:
- Workflow name: _______________
- Workflow active status during execution: _______________
- Workflow active status after execution: _______________

Execution:
- Manual execution performed: YES / NO
- Execution result: PASS / PASS WITH NOTES / FAIL / ERROR
- Execution path taken: happy path (TRUE branch) / validation failure / error handler

Set Input Variables node:
- Set Input Variables clicked: YES / NO
- Output panel opened (OUTPUT tab, not INPUT): YES / NO
- Output fields visible (not empty): YES / NO
- "No fields - item(s) exist, but they're empty." message: GONE / STILL PRESENT
- Total fields visible: ___
- request_id present: YES / NO — value: _______________
- brand_name present: YES / NO — value: _______________
- campaign_name present: YES / NO — value: _______________
- channel present: YES / NO — value: _______________
- asset_type present: YES / NO — value: _______________
- product_name present: YES / NO — value: _______________
- approval_required present: YES / NO — value/type: _______________ (boolean true required)
- sandbox_mode present: YES / NO — value/type: _______________ (boolean true required)
- Duplicate brand_name exists: YES / NO

Downstream nodes:
- Code: Load Brand Brain result: _______________
- Code: AI Generate Creative Brief result: _______________
- Code: Validate Required Fields result: _______________
- If: Validation Pass branch taken: TRUE / FALSE / unknown
- Set: approval_status = Draft: YES / NO
- Code: Write Log Entry result: _______________
- NoOp: STUB visible/reached: YES / NO

Final output:
- approval_status: _______________
- logWritten: _______________
- approvalQueueStubReached: _______________

Safety:
- Credentials attached: YES / NO
- API calls observed: YES / NO
- Auto-post / auto-reply occurred: YES / NO
- Production side effect: YES / NO
- Workflow activated during session: YES / NO

Result: PASS / PASS WITH NOTES / FAIL
Notes: _______________
Ready for next phase: YES / NO
```

---

## 7. Failure Handling

### If Set Input Variables output is still empty:

1. Do NOT modify workflow in n8n UI.
2. Note the exact message shown in the output panel.
3. Record execution status (did other nodes run?).
4. Fill evidence form as FAIL — include notes.
5. Stop Phase 33.
6. Report to Architect — open new phase to inspect workflow JSON vs n8n import state.

### If workflow throws an error node:

1. Do NOT add or fix credentials.
2. Do NOT click Activate.
3. Do NOT retry more than once.
4. Record the exact error message from the error node.
5. Fill evidence form as FAIL or PASS WITH NOTES (depending on error type).
6. Stop Phase 33.
7. Report to Architect.

### If validation fails (FALSE branch taken):

This may still be a PASS WITH NOTES if:
- The FALSE branch is taken due to STUB placeholder values in `brief_id` / `concept` etc.
- No forbidden output occurred.
- Workflow remained inactive.

Record the validation_errors array content and classify accordingly.

---

## 8. Safety Checklist

| Check | Status |
|-------|--------|
| Workflow JSON changed in repo | NO |
| `active=true` introduced in repo | NO |
| Secrets added | NO |
| Credentials added | NO |
| Real API calls added | NO |
| n8n manual execution by Owner | PLANNED — after Owner executes, update to YES |
| Workflow activated by Owner | NO |
| Workflow published | NO |
| Auto-post / auto-reply | NO |
| Ads spend | NO |
| Production side effect risk | NO |
| Claude Code has n8n UI access | NO — Owner executes manually |

---

## 9. Recommended Phase 34

### If Phase 33 PASS or PASS WITH NOTES:

**Phase 34 — Creative Asset Auto Sandbox Execution Evidence Recording & Next Module Decision**

Goals:
- Commit Phase 33 evidence to repo.
- Confirm the creative_asset_auto_skeleton sandbox track is complete (Phase 8 → Phase 33).
- Decide next module: next HIGH RISK workflow sandbox track, or new OS feature.

### If Phase 33 FAIL (output still empty / error):

**Phase 34 — Creative Asset Auto Set Input Variables Output Debug Planning**

Goals:
- Compare repo JSON `Set Input Variables` node vs n8n sandbox node state.
- Identify whether re-import actually loaded the Phase 30 patch or the old version.
- Plan corrective action.

---

## 10. Phase Connections

| Phase | Description | Status |
|-------|-------------|--------|
| Phase 8 | n8n Workflow Skeleton Build | DONE + PUSHED |
| Phase 26 | First Sandbox Import | DONE + PUSHED |
| Phase 27 | Sandbox Manual Execution — PASS WITH NOTES | DONE + PUSHED |
| Phase 28 | Sandbox I/O Standardization | DONE + PUSHED |
| Phase 29 | Safe Sample Input Patch Planning | DONE + PUSHED |
| Phase 30 | Safe Sample Input Patch Implementation | DONE + PUSHED (commit `18c681d`) |
| Phase 31 | Sandbox Re-import & Manual Execution Planning | DONE + PUSHED (commit `d6570f0`) |
| Phase 32 | Sandbox Re-import Only | DONE + PUSHED (commit `11268bb`) |
| **Phase 33** | **Sandbox Manual Execution Check (this phase)** | **RUNBOOK_READY — OWNER ACTION REQUIRED** |
| Phase 34 (TBD) | Evidence recording / next decision | NOT STARTED |

---

## 11. Safety Confirmation

| Item | Status |
|------|--------|
| Workflow JSON modified in Phase 33 | NO |
| `active = true` introduced | NO |
| Real credentials added | NO |
| Real API calls added | NO |
| Auto-post / auto-reply / ad spend | NO |
| Production system modified | NO |
| Real customer data added | NO |
| n8n execution performed by Builder (Claude Code) | NO |
| n8n manual execution planned for Owner | YES — Section 3 |
| Secret scan (new files) | CLEAN |
| Scope creep | NO — runbook/docs only |
