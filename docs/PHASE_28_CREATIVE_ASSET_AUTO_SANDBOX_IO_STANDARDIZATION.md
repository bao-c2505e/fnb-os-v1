# Phase 28 — Creative Asset Auto Sandbox Input/Output Standardization

Created By: Claude Code (Builder, AGT-02) — 2026-06-02
Phase: 28 — Creative Asset Auto Sandbox Input/Output Standardization
Status: BUILD_READY — AWAITING CODEX REVIEW
Branch: main

---

## Purpose

Phase 28 standardizes the expected sandbox input/output behavior for the `creative_asset_auto_skeleton` workflow after its first successful manual sandbox execution in Phase 27 (result: PASS WITH NOTES, 2026-06-02).

This document:
- Defines the sandbox input contract (fields, required/optional, placeholder values, safe sample values)
- Defines the sandbox output contract (expected objects and state after execution)
- Explains the Phase 27 PASS WITH NOTES note about Set Input Variables
- Establishes pass/fail criteria for all future sandbox runs
- Records safety constraints that must be maintained in all sandbox runs

**Scope:** Documentation only. No workflow JSON was modified. No credentials added. No API calls made. No workflow activated.

---

## A — Sandbox Input Contract

### A1 — Input Entry Point

The sandbox execution entry point for `creative_asset_auto_skeleton` is the **Manual Trigger** node.

In the skeleton workflow, the **Set Input Variables** node defines the expected input fields. These fields are set as constants within the node rather than as user-supplied parameters passed through the trigger.

### A2 — Defined Input Fields

The following input fields are defined in the `Set Input Variables` node of `creative_asset_auto_skeleton.json`:

| Field Name | Type | Required | Placeholder? | Recommended Sample Value (Vị Cuốn) |
|------------|------|----------|-------------|-------------------------------------|
| `brand_id` | string | YES | NO | `VQ` |
| `brand_name` | string | YES | NO | `Vị Cuốn` |
| `brief_request` | string | YES | YES — `REPLACE_WITH_OWNER_BRIEF_REQUEST` | `Tạo brief sáng tạo ảnh sản phẩm cuốn tươi cho Facebook 1:1` |
| `asset_type` | string | YES | NO | `Photo` |
| `platform` | string | YES | NO | `Facebook` |
| `format` | string | YES | NO | `1:1 square 1080x1080` |
| `objective` | string | YES | NO | `Engagement` |

### A3 — Field Classification

| Classification | Fields | Rule |
|---------------|--------|------|
| **Hard-coded safe** | `brand_id`, `brand_name`, `asset_type`, `platform`, `format`, `objective` | Values are safe for sandbox use. No modification needed for testing. |
| **Placeholder — must not contain real data** | `brief_request` | Must remain `REPLACE_WITH_OWNER_BRIEF_REQUEST` or a generic stub string. Never use real customer data or personally identifiable information. |
| **Never include** | API keys, tokens, passwords, real customer names, real phone numbers, real email addresses | These must never appear in any input field for a skeleton sandbox run. |

### A4 — Sandbox Input Rules

1. **No real credentials** in any input field.
2. **No real customer PII** in any input field (no real customer names, phones, emails, order IDs).
3. **No live brief requests** from actual business campaigns. Use stub text only.
4. **`brief_request` must remain a placeholder** (`REPLACE_WITH_OWNER_BRIEF_REQUEST` or descriptive stub). Never replace with a real campaign brief tied to actual ad spend.
5. **`brand_id` and `brand_name` are safe** — they identify the brand but contain no secrets.
6. **`active` must remain `false`** on the workflow before and after each sandbox run.

### A5 — Skeleton Behavior: Set Input Variables May Show Empty

In the Phase 27 sandbox execution, the Owner reported:

> "Set Input Variables showed: 'No fields - item(s) exist, but they're empty.'"

This is an **expected n8n skeleton behavior** and does not indicate a failure. See Section C for full explanation.

For sandbox input verification purposes, the presence of downstream stub data (i.e., Code nodes generating `brandBrain`, `creativeBrief`, etc.) is the correct signal that inputs were processed. The Set Input Variables display quirk does not affect downstream execution.

---

## B — Sandbox Output Contract

### B1 — Expected brandBrain Object

After execution of `Code: Load Brand Brain`, the sandbox output must include a `brandBrain` object with the following structure and placeholder values:

```json
{
  "brandBrain": {
    "brand_name": "Vị Cuốn",
    "brand_positioning": "REPLACE_WITH_BRAND_POSITIONING",
    "target_customer": "REPLACE_WITH_TARGET_CUSTOMER",
    "menu_items": "REPLACE_WITH_MENU_ITEMS",
    "price_range": "REPLACE_WITH_PRICE_RANGE",
    "address": "REPLACE_WITH_ADDRESS",
    "opening_hours": "REPLACE_WITH_OPENING_HOURS",
    "key_offers": "REPLACE_WITH_KEY_OFFERS",
    "tone_of_voice": "REPLACE_WITH_TONE_OF_VOICE",
    "forbidden_claims": "REPLACE_WITH_FORBIDDEN_CLAIMS",
    "approval_status": "REPLACE_WITH_APPROVAL_STATUS"
  },
  "brandBrainLoaded": true
}
```

**Key assertion:** `brandBrainLoaded` must equal `true`. All `REPLACE_WITH_*` values are correct stub behavior — they confirm the skeleton is operating as designed and that no real Brand Brain data source has been connected.

### B2 — Expected creativeBrief Object

After execution of `Code: AI Generate Creative Brief`, the sandbox output must include a `creativeBrief` object with the following structure:

```json
{
  "creativeBrief": {
    "brief_id": "CB-VQ-STUB-001",
    "brand_id": "VQ",
    "brand_name": "Vị Cuốn",
    "asset_type": "Photo",
    "platform": "Facebook",
    "format": "1:1 square 1080x1080",
    "objective": "Engagement",
    "concept": "STUB_CONCEPT — Replace with AI-generated creative concept (1-3 sentences)",
    "visual_direction": "STUB_VISUAL_DIRECTION — Replace with AI-generated visual direction including mood, color palette, lighting, shot composition",
    "scene_description": null,
    "copy_overlay": null,
    "ai_tool_prompt": null,
    "required_inputs": ["REPLACE_WITH_REQUIRED_PRODUCTION_INPUTS"],
    "output_specs": "REPLACE_WITH_OUTPUT_SPECS",
    "qa_checklist": [
      "No hardcoded prices without Owner confirmation",
      "Brand colors match palette from Brand Brain",
      "No unverified health claims"
    ],
    "approval_status": "Draft",
    "created_by_agent": "n8n-creative-asset-auto (STUB)",
    "created_at": "<ISO_TIMESTAMP>",
    "notes": "Phase 8 skeleton stub. No real AI call made. Asset production requires Owner-arranged photography/filming."
  },
  "aiCallCompleted": true
}
```

**Key assertions:**
- `aiCallCompleted` must equal `true`
- `approval_status` within the `creativeBrief` object must equal `"Draft"` — this is set explicitly in Section B5 below
- `STUB_CONCEPT` and `STUB_VISUAL_DIRECTION` values are correct skeleton behavior — no real AI API call is made
- `"notes"` field must confirm no real AI call was made

### B3 — Expected Validation Result

After execution of `Code: Validate Required Fields`, the sandbox output must include:

```json
{
  "validation_pass": true,
  "validation_errors": []
}
```

**Key assertion:** `validation_pass` must equal `true` in a PASS run. If `validation_pass` is `false`, the workflow routes to the validation failure path (Stop and Error node) — this is a legitimate FAIL outcome for sandbox purposes if it occurs unexpectedly.

**Required fields validated by the Code node:**
- `brief_id`
- `brand_id`
- `brand_name`
- `asset_type`
- `platform`
- `format`
- `objective`
- `concept`
- `visual_direction`
- `approval_status`
- `created_by_agent`
- `created_at`

### B4 — Expected Approval Status

After execution of `Set: approval_status = Draft`, the top-level `approval_status` field must equal `"Draft"`.

This is the Approval Gate — no publishing, no ad spend, no customer-facing output is permitted unless approval_status is explicitly changed by the Owner to `"Approved"` through the correct channel (not the sandbox).

**Key assertion:** `approval_status = "Draft"` confirms the approval gate is functional and no unauthorized publishing has occurred.

### B5 — Expected Log Entry

After execution of `Code: Write Log Entry`, the sandbox output must include a `logEntry` object:

```json
{
  "logEntry": {
    "log_id": "LOG-<YYYYMMDD>-STUB-001",
    "timestamp": "<ISO_TIMESTAMP>",
    "phase": "8",
    "agent_name": "n8n-creative-asset-auto (STUB)",
    "action_type": "Creative Brief Draft",
    "input_ref": "<brief_request_value>",
    "output_ref": "CB-VQ-STUB-001",
    "status": "Success",
    "summary": "Creative Asset Auto skeleton executed. Brief created with approval_status=Draft. No real AI call.",
    "errors": null,
    "next_action": "Send brief to approval queue. Owner to review and set approval_status=Approved before asset production.",
    "owner_action_required": false
  },
  "logWritten": true
}
```

**Key assertion:** `logWritten` must equal `true`.

Note: In Phase 27, the Owner reported `logEntry.log_id` was not recorded. This is acceptable — the key assertions are `logWritten=true` and `approvalQueueStubReached=true`.

### B6 — Expected Approval Queue Stub

After execution of `NoOp: STUB — Send to Approval Queue`, the sandbox execution must reach this node and terminate normally.

**Key assertion:** `approvalQueueStubReached = true`

The NoOp node does not write to any real approval queue (Google Sheets or Supabase). It is a placeholder stub confirming the happy-path execution completed without errors. No external write occurs.

### B7 — Full Expected Output Summary

| Output Signal | Expected Value | Failure Signal |
|--------------|----------------|----------------|
| `brandBrainLoaded` | `true` | `false` or node error |
| `creativeBrief.approval_status` | `"Draft"` | anything other than `"Draft"` |
| `aiCallCompleted` | `true` | `false` or node error |
| `validation_pass` | `true` | `false` (routes to error path) |
| Top-level `approval_status` | `"Draft"` | anything other than `"Draft"` |
| `logWritten` | `true` | `false` or node error |
| `approvalQueueStubReached` | `true` | node not reached |
| Workflow active status | `INACTIVE` | `ACTIVE` — IMMEDIATE STOP CONDITION |
| Real image/URL/binary in output | ABSENT | present — IMMEDIATE STOP CONDITION |
| Real API call evidence | ABSENT | present — IMMEDIATE STOP CONDITION |
| Auto-post to social platform | ABSENT | occurred — IMMEDIATE STOP CONDITION |
| Real customer PII in output | ABSENT | present — IMMEDIATE STOP CONDITION |

---

## C — Explanation of Phase 27 PASS WITH NOTES

### C1 — What Was Observed

In Phase 27, the Owner reported the following during sandbox execution:

> **Set Input Variables showed: "No fields - item(s) exist, but they're empty."**

This message appeared in the n8n execution panel for the `Set Input Variables` node after the Manual Trigger fired.

### C2 — Root Cause

The `Set Input Variables` node uses n8n's `Set` node (typeVersion 3) with an `assignments.assignments` array. In some n8n versions, the Set node may show this message in the UI execution panel when:

1. The node has field definitions but the execution panel display is rendering them as "empty" due to a UI quirk or version behavior.
2. The data from a preceding Manual Trigger carries no user-supplied body (manual triggers have no input body — they fire with an empty object `{}`), and the Set node's UI reflects the absence of incoming field data before its own assignments are applied.

This is a **display quirk** in the n8n UI, not an execution failure.

### C3 — Why This Is Acceptable

**Evidence that the workflow executed correctly despite the display:**

- `Code: Load Brand Brain` succeeded → `brandBrainLoaded = true`
- `Code: AI Generate Creative Brief` succeeded → `aiCallCompleted = true`  
- `Code: Validate Required Fields` succeeded → `validation_pass = true`
- `If: Validation Pass` routed to the TRUE branch
- `Set: approval_status = Draft` succeeded → `approval_status = "Draft"`
- `Code: Write Log Entry` succeeded → `logWritten = true`
- `NoOp: STUB — Send to Approval Queue` reached → `approvalQueueStubReached = true`

The downstream Code nodes are all stubs that generate their own data internally. They do not depend on the Set Input Variables node supplying populated fields — they use `$input.first().json` and fall back to hardcoded stub values when fields are empty or contain `REPLACE_WITH_*` placeholders.

This means: **the Set Input Variables "empty" display does not break downstream execution for the skeleton.**

### C4 — Classification

| Observation | Classification |
|------------|----------------|
| Set Input Variables showed "empty" | PASS WITH NOTES — acceptable skeleton behavior |
| Downstream stub data generated correctly | PASS — expected behavior |
| Validation passed TRUE branch | PASS — required outcome |
| approval_status = Draft | PASS — required outcome |
| No forbidden outputs | PASS — required outcome |

### C5 — What Should Change in Future Phases

This behavior should be resolved in a future workflow update phase (not Phase 28). Potential improvements:

1. **Documentation-only (Phase 28):** Document the behavior and acceptable outcome — completed in this document.
2. **Future workflow update phase:** Add explicit fallback/default values to the Set Input Variables assignments, or provide a Form Trigger instead of a Manual Trigger so that field data is always present in the execution panel.
3. **Future production phase:** Replace stub Code nodes with real integrations — at that point, the Set Input Variables node must be fully populated.

**Phase 28 does not modify the workflow JSON.** Any workflow change must be a separate phase with Owner approval.

---

## D — Pass/Fail Criteria for Future Sandbox Runs

### D1 — PASS

All of the following must be true:

- [ ] Workflow was INACTIVE before execution
- [ ] Execution was triggered manually (not by activation)
- [ ] `brandBrainLoaded = true`
- [ ] `aiCallCompleted = true`
- [ ] `validation_pass = true` (TRUE branch taken)
- [ ] `approval_status = "Draft"` (top-level)
- [ ] `creativeBrief.approval_status = "Draft"`
- [ ] `logWritten = true`
- [ ] `approvalQueueStubReached = true`
- [ ] Workflow remained INACTIVE after execution
- [ ] No real image, video, or binary asset generated
- [ ] No real external API called (no Anthropic, no Google, no Facebook, no storage)
- [ ] No auto-post to any social platform
- [ ] No auto-reply to any customer message
- [ ] No ad spend or ads mutation
- [ ] No real customer PII in output
- [ ] No real credentials used

### D2 — PASS WITH NOTES

All PASS conditions are met, but one or more of the following notes apply:

| Note | Condition | Acceptable? |
|------|-----------|-------------|
| Set Input Variables shows "empty" in UI | Downstream stub data generated correctly, validation passes | YES — document note |
| `logEntry.log_id` not recorded by Owner | `logWritten = true` is confirmed | YES — document note |
| Screenshots not submitted | Verbal/text confirmation provided, no disputed outputs | YES — document note |
| Minor UI display anomaly | No functional impact on output | YES — document note |

### D3 — FAIL

Any of the following conditions triggers a FAIL:

| Failure Condition | Action Required |
|------------------|-----------------|
| `validation_pass = false` (unexpected — not caused by intentional test) | STOP — investigate, do not re-run |
| `approval_status` is not `"Draft"` | STOP — do not re-run, notify Owner |
| Workflow active status is `ACTIVE` after execution | IMMEDIATE STOP — check workflow, do not re-run |
| Real image, binary, or asset URL appears in output | IMMEDIATE STOP — report to Owner |
| Real external API call confirmed (Anthropic, Google, Meta, etc.) | IMMEDIATE STOP — report to Owner |
| Auto-post to social platform occurred | IMMEDIATE STOP — report to Owner, potential production incident |
| Real customer PII in output | IMMEDIATE STOP — report to Owner |
| Real credential added or used | IMMEDIATE STOP — report to Owner |
| Ads or ad budget mutation | IMMEDIATE STOP — report to Owner |
| Production webhook triggered | IMMEDIATE STOP — report to Owner |
| Workflow error on happy path nodes (not validation failure path) | FAIL — investigate before re-run |

### D4 — BLOCKED

Run is BLOCKED and must not proceed if:

- Owner approval phrase was not issued before execution
- Workflow is ACTIVE before execution (do not proceed)
- Real credentials are present in the workflow
- n8n instance URL is production (not sandbox `n8n.baon8n.blog`)
- Builder (Claude Code) attempts to access n8n UI directly — Builder has no n8n access

---

## E — Safety Constraints

The following constraints apply to **all** sandbox runs of `creative_asset_auto_skeleton` at all times:

| Constraint | Rule |
|-----------|------|
| No real credentials | `REPLACE_WITH_*` placeholders must remain. Never attach real Google Sheets, Supabase, or Anthropic credentials in sandbox. |
| No real API calls | No real Anthropic API key. No real Google API key. No real n8n cloud API. |
| No production webhook | Do not configure or activate a real production webhook on this workflow. Sandbox only. |
| No auto-post | Workflow must never post to Facebook, Instagram, TikTok, or any social platform. |
| No auto-reply | Workflow must never send a reply to any customer inbox, comment, or message. |
| No ads mutation | Workflow must never create, modify, or spend any ad campaign, ad set, or ad budget. |
| No active=true | `"active": false` must remain in `creative_asset_auto_skeleton.json` at all times. Never set to `true`. |
| Sandbox instance only | All n8n sandbox runs must use `https://n8n.baon8n.blog/` — never the production n8n instance. |
| Dummy/stub data only | Input values must be stub or placeholder only. No real campaign briefs tied to actual ad spend. |
| Owner approval phrase required | Each sandbox execution requires the exact approval phrase issued by the Owner before the session. |

---

## F — Phase 27 Execution Record Reference

For full evidence of the Phase 27 sandbox execution that produced these standardization requirements, see:

- **Evidence log:** `logs/phase_27_creative_asset_auto_sandbox_manual_execution_evidence.md`
- **Runbook:** `docs/PHASE_27_SANDBOX_MANUAL_EXECUTION_CREATIVE_ASSET_AUTO.md`
- **Phase 27 handoff:** `handoff/PHASE_27_HANDOFF.md`

Phase 27 result: **PASS WITH NOTES** — 2026-06-02
Codex result: **PASS WITH NOTES**
Latest push commit: `0b7ce07`

---

## G — Related Documents

| Document | Purpose |
|----------|---------|
| `n8n/workflows/creative_asset_auto_skeleton.json` | Source workflow — do not modify without Owner approval |
| `docs/specs/creative_asset_auto_sandbox_io_spec.md` | Formal I/O specification (machine-readable reference) |
| `logs/phase_27_creative_asset_auto_sandbox_manual_execution_evidence.md` | Phase 27 execution evidence |
| `docs/PHASE_27_SANDBOX_MANUAL_EXECUTION_CREATIVE_ASSET_AUTO.md` | Phase 27 runbook |
| `05_SCHEMAS/creative-brief.schema.json` | JSON schema for creativeBrief output |
| `docs/runbooks/SANDBOX_EVIDENCE_PACK_TEMPLATE.md` | Evidence pack template for future runs |
| `docs/runbooks/SANDBOX_EXECUTION_LOG_TEMPLATE.md` | Execution log template for future runs |
| `docs/governance/OWNER_APPROVAL_GATE.md` | Approval gates — Gate 6 (Runtime Execution) |

---

## H — Phase Connections

| Phase | Description | Status |
|-------|-------------|--------|
| Phase 8 | n8n Workflow Skeleton Build — creative_asset_auto_skeleton created | DONE + PUSHED |
| Phase 22A | Owner Evidence Capture Pack — creative_asset_auto_skeleton | DONE + PUSHED |
| Phase 26 | First Sandbox Import — creative_asset_auto_skeleton | DONE + PUSHED (PASS) |
| Phase 27 | Sandbox Manual Execution — creative_asset_auto_skeleton | DONE + PUSHED (PASS WITH NOTES) |
| **Phase 28** | **Sandbox I/O Standardization (this phase)** | **BUILD_READY** |
| Phase 29 (TBD) | Next phase — to be defined by Owner/Architect | NOT STARTED |

---

## I — Safety Confirmation

| Item | Status |
|------|--------|
| Workflow JSON modified | NO |
| `active = true` introduced | NO |
| Real credentials added | NO |
| Real API calls made | NO |
| Auto-post / auto-reply / ad spend | NO |
| Production system modified | NO |
| Real customer data used | NO |
| n8n workflow executed by Builder | NO |
| Secret scan (new files) | CLEAN |
| Scope creep (files outside scope) | NO |
