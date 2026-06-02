# Phase 27 — Sandbox Manual Execution Runbook
# creative_asset_auto_skeleton

**Phase:** 27 — Sandbox Manual Execution Only: Creative Asset Auto Skeleton
**Type:** Owner Runbook — Documentation Only (Builder does not execute)
**Workflow:** `FnB OS V1 — Creative Asset Auto [SKELETON]`
**Workflow File:** `n8n/workflows/creative_asset_auto_skeleton.json`
**Workflow URL:** `https://n8n.baon8n.blog/workflow/VW5PDkOOtrjLQBps?projectId=yZLTIcmSgpxftXH7&uiContext=workflow_list`
**Created By:** Claude Code (Builder, AGT-02) — 2026-06-02
**Status:** RUNBOOK_READY — AWAITING OWNER MANUAL EXECUTION

---

## A. Phase 27 Objective

Phase 27 is the **first manual sandbox execution** of `creative_asset_auto_skeleton`.

The workflow was imported into the n8n sandbox in **Phase 26 (PASS — 2026-06-02)**. It is:
- Currently **INACTIVE** (active toggle = OFF)
- Execution count = **0**
- No real credentials attached

Phase 27 allows the Owner to manually trigger the workflow once in the n8n sandbox and confirm:
- The node execution chain runs without errors
- All key output fields are present and correct
- No forbidden output is produced (no real image, no cloud storage, no API calls)
- The workflow remains INACTIVE throughout
- Execution count increments by exactly 1

Builder (Claude Code) does **not** execute workflows, does not have n8n UI access, and does not claim to perform any execution in this phase.

---

## B. Workflow Identity

| Field | Value |
|-------|-------|
| Workflow file | `n8n/workflows/creative_asset_auto_skeleton.json` |
| n8n workflow name | `FnB OS V1 — Creative Asset Auto [SKELETON]` |
| n8n workflow URL | `https://n8n.baon8n.blog/workflow/VW5PDkOOtrjLQBps?projectId=yZLTIcmSgpxftXH7&uiContext=workflow_list` |
| Risk level | Standard |
| Trigger type | Manual Trigger — click "Test workflow" button in n8n canvas |
| Phase 17 payload | `samples/sandbox/phase_17_test_payloads/creative_asset_auto_skeleton_test_payload.md` |
| Payload scenario | P17-WF02-S1 — Facebook Image Creative Brief |
| Evidence log (Phase 27) | `logs/phase_27_creative_asset_auto_sandbox_manual_execution_evidence.md` |
| Evidence folder | `evidence/phase_22b/creative_asset_auto_skeleton/` |
| Phase 26 import PASS | YES — committed `4a001bc` |

---

## C. Required Owner Approval Phrase

Before any manual execution is performed, Owner must issue **exactly** this phrase:

```
APPROVED FOR SANDBOX MANUAL EXECUTION ONLY — creative_asset_auto_skeleton — 2026-06-02
```

**This exact phrase is required.** Vague approvals ("ok", "go ahead", "triển khai", "chạy thử đi") do NOT satisfy this gate.

The phrase must:
- Include the workflow name: `creative_asset_auto_skeleton`
- Include the date: `2026-06-02`
- State "SANDBOX MANUAL EXECUTION ONLY"
- Be copied exactly into the evidence log Section B

---

## D. Pre-Execution Checklist

Owner must confirm **all** items before triggering the workflow.

| ID | Check | Required State | Owner Confirm |
|----|-------|---------------|---------------|
| PE-01 | Owner approval phrase issued | `APPROVED FOR SANDBOX MANUAL EXECUTION ONLY — creative_asset_auto_skeleton — 2026-06-02` confirmed | ☐ |
| PE-02 | n8n instance is SANDBOX only | URL: `https://n8n.baon8n.blog` — NOT production | ☐ |
| PE-03 | Workflow URL is correct | `https://n8n.baon8n.blog/workflow/VW5PDkOOtrjLQBps` | ☐ |
| PE-04 | Workflow name matches exactly | `FnB OS V1 — Creative Asset Auto [SKELETON]` | ☐ |
| PE-05 | Active toggle is OFF before execution | Active toggle = OFF — **STOP if active = ON** | ☐ |
| PE-06 | "DO NOT ACTIVATE" sticky note is visible | Sticky note present on canvas | ☐ |
| PE-07 | Execution count before execution = 0 | Execution history tab shows 0 prior executions | ☐ |
| PE-08 | No real credentials added | "Credential not found" warnings are expected — do NOT resolve them | ☐ |
| PE-09 | Phase 17 test payload file is open | `samples/sandbox/phase_17_test_payloads/creative_asset_auto_skeleton_test_payload.md` | ☐ |
| PE-10 | Evidence log file is open and ready | `logs/phase_27_creative_asset_auto_sandbox_manual_execution_evidence.md` open | ☐ |
| PE-11 | Evidence folder exists | `evidence/phase_22b/creative_asset_auto_skeleton/` present | ☐ |
| PE-12 | No real customer data will be entered | All inputs use dummy/placeholder values only | ☐ |
| PE-13 | Workflow will NOT be activated at any point | Active toggle remains OFF throughout entire session | ☐ |
| PE-14 | git working tree is clean | `git status` shows nothing to commit | ☐ |

**Pre-Execution Sign-Off**

```
I confirm PE-01 through PE-14 are all satisfied.
I understand this is a sandbox-only manual execution — NOT a production run.
I will not activate the workflow, add real credentials, or use real customer data.

Operator: ___________________________
Date/Time: ___________________________
n8n Sandbox URL: ___________________________
```

---

## E. Manual Execution Steps

### Step 1 — Open n8n Sandbox

Open the n8n sandbox at:
```
https://n8n.baon8n.blog/workflow/VW5PDkOOtrjLQBps?projectId=yZLTIcmSgpxftXH7&uiContext=workflow_list
```

**Confirm:** This is the sandbox instance, not production.

---

### Step 2 — Verify Workflow State Before Execution

| Check | Expected | Action if Wrong |
|-------|----------|-----------------|
| Workflow name | `FnB OS V1 — Creative Asset Auto [SKELETON]` | STOP — wrong workflow |
| Active toggle | OFF (inactive) | STOP — do not execute if active |
| Execution count | 0 | Record actual count in evidence log |
| Sticky note visible | "DO NOT ACTIVATE" present | STOP if not visible — verify correct workflow |

---

### Step 3 — Confirm No Real Credentials

Inspect each node that shows a credential field.

Expected: "Credential not found" warnings are normal for skeleton workflows. **Do NOT add real credentials.** Do NOT resolve credential warnings.

---

### Step 4 — Confirm Payload Scenario

Payload scenario: **P17-WF02-S1 — Facebook Image Creative Brief**

Input values are pre-set in the `Set Input Variables` node. No manual JSON editing is needed.

Reference: `samples/sandbox/phase_17_test_payloads/creative_asset_auto_skeleton_test_payload.md`

Expected input fields:
- `brand_id`: `"VQ"`
- `brand_name`: `"Vị Cuốn"`
- `asset_type`: `"Image"`
- `platform`: `"Facebook"`
- `content_angle`: `"Product Highlight"`

---

### Step 5 — Execute ONCE (Manual Trigger)

Click **"Test workflow"** button on the canvas. Run **exactly once**.

Do not click again if execution appears slow — wait for all nodes to complete.

---

### Step 6 — Observe Node Execution (Per-Node)

Track each node result. See Section F for the full node chain reference.

For each node:
- Record green ✓ (executed) or yellow/orange (skipped — acceptable) or red ✗ (error — record and assess)
- Note key output values

---

### Step 7 — Forbidden Output Checks

After execution completes, confirm ALL of these:

| ID | Forbidden Output | Action if Found |
|----|-----------------|-----------------|
| FO-01 | Real image file, image URL, or binary asset in output | **STOP — record BLOCKED** |
| FO-02 | HTTP request to image generation API (DALL-E, Midjourney, Stable Diffusion, etc.) | **STOP — record BLOCKED** |
| FO-03 | HTTP request to Google Drive, S3, or cloud storage | **STOP — record BLOCKED** |
| FO-04 | `approval_status` = `"Approved"` or `"Published"` | **STOP — record BLOCKED** |
| FO-05 | Any real customer PII in output | **STOP — record BLOCKED** |
| FO-06 | `active = true` in workflow settings | **STOP — record BLOCKED** |
| FO-07 | Auto-post to any social platform | **STOP — record BLOCKED** |
| FO-08 | Credential prompt or credential-fill dialog opened | **STOP — do not fill — record BLOCKED** |
| FO-09 | External HTTP call to any live API (not a stub) | **STOP — record BLOCKED** |
| FO-10 | Production webhook trigger | **STOP — record BLOCKED** |

---

### Step 8 — Capture Evidence

Required evidence items:

| ID | Evidence | Description |
|----|----------|-------------|
| EC-01 | Canvas screenshot | Full canvas showing all nodes green (or partial with branch noted) |
| EC-02 | `Code: Write Log Entry` output screenshot | `logEntry` JSON visible with `log_id`, `timestamp`, `status` |
| EC-03 | `NoOp: STUB — Send to Approval Queue` screenshot | `approvalQueueStubReached = true` visible |
| EC-04 | `If: Validation Pass` branch screenshot | Which branch was taken (TRUE or FALSE) visible |
| EC-05 | Execution history tab screenshot | Execution count = 1 after run (or annotated) |
| EC-06 | `logEntry` JSON | Copy full JSON object — paste into evidence log result_summary |
| EC-07 | n8n Execution ID | Copy from execution panel header |

**Screenshot naming convention:**
```
YYYYMMDD_HHMM_creative_asset_[description]_[result].png
```

Examples:
```
20260602_0930_creative_asset_canvas_pass.png
20260602_0932_creative_asset_log_entry_pass.png
20260602_0933_creative_asset_noop_stub_pass.png
20260602_0934_creative_asset_validation_branch_pass.png
20260602_0935_creative_asset_exec_count_pass.png
```

Store all screenshots in: `evidence/phase_22b/creative_asset_auto_skeleton/`

---

### Step 9 — Fill Evidence Log

Fill all fields in `logs/phase_27_creative_asset_auto_sandbox_manual_execution_evidence.md`.

Do not leave any field blank. If a field does not apply, write `N/A`.

---

### Step 10 — Post-Execution Safety Confirmation

After execution, confirm:

| Check | Required |
|-------|---------|
| Workflow active status after execution | INACTIVE — active toggle still OFF |
| Execution count after execution | 1 (exactly — or note if different) |
| No credentials added during session | Confirmed |
| No auto-post, auto-reply, ad spend | None |
| No real customer data used | Confirmed |
| No production system touched | Confirmed |
| No workflow JSON modified | Confirmed |

---

### Step 11 — Record Decision

Fill in the evidence log `Final Decision` field:
- `PASS` — all PASS criteria met, no forbidden output, no stop conditions triggered
- `PASS WITH NOTES` — execution succeeded but minor anomaly noted (describe in evidence log)
- `FAIL` — forbidden output found, stop condition triggered, or execution errored with no recovery

Do NOT debug n8n workflow logic inside the sandbox. If FAIL, record the exact error message and stop.

---

## F. Node Chain Reference

### Happy Path (PASS branch — expected)

| Step | Node Name | Expected Result |
|------|-----------|-----------------|
| 1 | Manual Trigger | Triggered — green |
| 2 | Set Input Variables | Input fields set (`brand_id`, `asset_type`, `platform`, etc.) — green |
| 3 | Code: Load Brand Brain | `brandBrainLoaded = true` — green |
| 4 | Code: AI Generate Creative Brief | `contentDraftGenerated = true`, `draft_brief` non-null — green |
| 5 | Code: Validate Required Fields | Validation runs — green |
| 6 | If: Validation Pass | `validationPassed = true` → TRUE branch — green |
| 7 | Set: approval_status = Draft | `approval_status = "Draft"` — green |
| 8 | Code: Write Log Entry | `logWritten = true`, `logEntry.log_id` present — green |
| 9 | NoOp: STUB — Send to Approval Queue | `approvalQueueStubReached = true` — green (terminal node) |

### Validation Failure Path (acceptable — not a BLOCK)

| Step | Node Name | Expected Result |
|------|-----------|-----------------|
| 6a | If: Validation Pass | `validationPassed = false` → FALSE branch |
| 6b | Set: Validation Error | Validation error fields set |
| 6c | Stop and Error: Validation Failed | Workflow stops with error — not a forbidden output |

### Error Handler Path (acceptable if no forbidden output)

| Step | Node Name | Expected Result |
|------|-----------|-----------------|
| — | Error Trigger | Fires if unhandled error in main path |
| — | Set: Error Log | Error fields captured |
| — | Stop and Error: Workflow Error | Workflow stops — record in evidence log |

> `REPLACE_WITH_*` placeholder values in node output are **expected stub behavior** — they confirm dummy/sandbox mode is active. They are NOT failures.

---

## G. Evidence Capture Checklist

| ID | Item | Status |
|----|------|--------|
| EC-01 | Canvas screenshot (all nodes) | ☐ |
| EC-02 | `Code: Write Log Entry` output screenshot | ☐ |
| EC-03 | `NoOp: STUB — Send to Approval Queue` screenshot | ☐ |
| EC-04 | `If: Validation Pass` branch screenshot | ☐ |
| EC-05 | Execution history tab (count = 1) | ☐ |
| EC-06 | `logEntry` JSON copied to evidence log | ☐ |
| EC-07 | n8n Execution ID copied | ☐ |
| EC-08 | Evidence log fully filled | ☐ |

---

## H. Pass / Fail Criteria

### PASS — all of the following must be true

| Criterion | Required |
|-----------|---------|
| 9 happy-path nodes all green | YES (or validation failure branch acceptable — see note) |
| `brandBrainLoaded = true` | YES |
| `contentDraftGenerated = true` | YES |
| `draft_brief` non-null | YES |
| `approval_status = "Draft"` | YES |
| `logWritten = true` | YES |
| `logEntry.log_id` present (starts with "LOG-") | YES |
| `approvalQueueStubReached = true` | YES |
| Workflow INACTIVE after execution | YES |
| Execution count = 1 after run | YES |
| No forbidden output (FO-01 through FO-10) | NONE triggered |
| No credentials added | YES |
| No auto-post/reply/ad spend | NONE |

> Note: Validation failure path (FALSE branch → Stop and Error: Validation Failed) is still PASS if no forbidden output is produced. Record the branch taken.

### BLOCKED triggers — any ONE of these is an immediate stop

| Trigger | Action |
|---------|--------|
| Real image file, binary, or cloud storage URL in output | STOP — do not continue — fill issue report |
| Image generation API call detected | STOP — do not continue |
| `approval_status` = `"Approved"` or `"Published"` | STOP — do not continue |
| Real customer PII in output | STOP — do not continue |
| `active = true` set | STOP — do not continue |
| Auto-post, auto-reply, or ad spend | STOP — do not continue |
| Real API credential filled | STOP — do not continue |
| Production instance used | STOP — do not continue |

---

## I. Rollback / No-Op Statement

Phase 27 is a **sandbox-only, read-only manual trigger** with no production side effects.

| Question | Answer |
|----------|--------|
| Did this execution modify any production data? | NO — sandbox only |
| Did this execution send any customer-facing message? | NO |
| Did this execution spend any ad budget? | NO |
| Did this execution write to any external system? | NO |
| Did this execution activate the workflow? | NO — active toggle remains OFF |
| Rollback needed? | NO — nothing to roll back |

If execution count increases from 0 to 1, that is expected sandbox behavior — not a production side effect.

If a BLOCKED trigger was hit: stop all further execution, fill the issue report, notify Builder with exact error. No rollback action needed — sandbox state is isolated.

---

## J. Prohibited Actions

The following actions are **absolutely prohibited** in Phase 27:

| Prohibited Action | Why |
|------------------|-----|
| Set workflow to `active = true` | Activates webhook triggers — production risk |
| Publish / deploy workflow | Exposes workflow to live traffic |
| Add real credentials to any node | Enables live API calls |
| Call real external APIs | Out of scope — sandbox only |
| Trigger production webhook | Production side effect — not allowed |
| Auto-post to any social platform | Customer-facing — requires separate approval gate |
| Auto-reply to real customers | Customer-facing — requires separate approval gate |
| Mutate ad budget or create ad campaigns | Financial risk — requires separate approval gate |
| Use real customer PII as test input | Privacy violation |
| Modify workflow JSON | Out of scope — JSON must remain unchanged |
| Execute workflow more than once per session | Record exact count — do not run multiple times without documenting |

---

## K. Stop Conditions

Stop all activity immediately if any of the following occur:

| ID | Stop Condition | Required Action |
|----|---------------|-----------------|
| SC-01 | Workflow active toggle turns ON | Immediately set back to OFF. Record in evidence log. |
| SC-02 | Credential prompt or fill dialog appears | Do NOT fill. Close dialog. Record BLOCKED. |
| SC-03 | Any real image, binary, or cloud URL appears in output | Record BLOCKED. Do not continue. |
| SC-04 | Image generation API called | Record BLOCKED. Do not continue. |
| SC-05 | Cloud storage write detected | Record BLOCKED. Do not continue. |
| SC-06 | `approval_status` = `"Approved"` or `"Published"` | Record BLOCKED. Do not continue. |
| SC-07 | Real customer PII visible in any field | Record BLOCKED. Do not continue. |
| SC-08 | Auto-post, auto-reply, or ad spend triggered | Record BLOCKED. Do not continue. |
| SC-09 | Production n8n instance opened instead of sandbox | Close immediately. Reopen correct sandbox URL. |
| SC-10 | Unclear node output — cannot determine result | Record BLOCKED. Do not guess. Notify Builder. |

---

## L. Related Documents

| Document | Purpose |
|----------|---------|
| `docs/36_PHASE_22A_CREATIVE_ASSET_SANDBOX_EVIDENCE_CAPTURE_PACK.md` | Original evidence capture pack for creative_asset — node chain reference |
| `logs/phase_22a_creative_asset_sandbox_evidence_log.md` | Phase 22A evidence log (blank template) |
| `logs/phase_27_creative_asset_auto_sandbox_manual_execution_evidence.md` | Phase 27 evidence log — Owner fills during execution |
| `docs/PHASE_26_CREATIVE_ASSET_SANDBOX_IMPORT_EVIDENCE.md` | Phase 26 import evidence — PASS confirmed |
| `logs/phase_26_creative_asset_sandbox_import_evidence_log.md` | Phase 26 import log — Owner-filled, PASS |
| `docs/runbooks/SANDBOX_RUNBOOK_INDEX.md` | Master runbook index |
| `docs/runbooks/OWNER_RUNTIME_READINESS_CHECKLIST.md` | Owner pre-action readiness checklist |
| `docs/governance/OWNER_APPROVAL_GATE.md` | Approval gate definitions |
| `handoff/PHASE_27_HANDOFF.md` | Phase 27 handoff |
| `samples/sandbox/phase_17_test_payloads/creative_asset_auto_skeleton_test_payload.md` | Phase 17 test payload — P17-WF02-S1 |

---

## M. Phase Connections

| Phase | Description | Status |
|-------|-------------|--------|
| Phase 22A | Owner Evidence Capture Pack — creative_asset_auto_skeleton | DONE + PUSHED |
| Phase 24A | Sandbox Runbook Index & Owner Runtime Readiness | DONE + PUSHED |
| Phase 24B | Sandbox Evidence Pack Template & Execution Log Standardization | DONE + PUSHED |
| Phase 25 | Sandbox Import Readiness Gate | DONE + PUSHED |
| Phase 26 | First Sandbox Import — creative_asset_auto_skeleton | **DONE + PUSHED (PASS)** |
| **Phase 27** | **Sandbox Manual Execution — creative_asset_auto_skeleton (this phase)** | **RUNBOOK_READY — AWAITING OWNER EXECUTION** |
| Phase 28 (next) | Owner Evidence Submission — creative_asset_auto_skeleton (if Phase 27 PASS) | NOT STARTED |

---

## N. Safety Confirmation

| Confirmation | Status |
|-------------|--------|
| Workflow JSON modified | NO |
| `active = true` introduced | NO |
| Real credentials added | NO |
| Real API calls made | NO |
| Auto-post / auto-reply / ad spend | NO |
| Production system modified | NO |
| Real customer data used | NO |
| n8n workflow executed by Builder | NO — Builder has no n8n UI access |
| Secret scan (this file) | CLEAN — documentation text only |

---

*FnB OS V1 — Vị Cuốn Growth OS*
*Phase 27 Runbook — Sandbox Manual Execution Only — creative_asset_auto_skeleton*
*Builder: Claude Code (AGT-02) — 2026-06-02*
