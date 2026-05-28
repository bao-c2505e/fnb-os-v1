# Phase 16 — Sandbox Runtime Validation Plan

**Project:** FnB OS V1 / Vị Cuốn Growth OS
**Phase:** 16
**Created By:** Claude Code (Builder, AGT-02)
**Date:** 2026-05-29
**Status:** PLAN ONLY — AWAITING OWNER APPROVAL BEFORE ANY EXECUTION
**Prior Phase:** Phase 14 — Sandbox Import Dry-Run PASS (6/6 workflows imported, all inactive)

---

## ⚠️ Critical Safety Notice

This document is a **plan only**. No test execution may begin until:

1. Owner (Bo Bao) has read and approved this plan.
2. Codex (AGT-03) has reviewed this plan and issued PASS.
3. Owner has confirmed sandbox/test n8n instance is ready.
4. All preconditions in Section 5 are satisfied.
5. No real credentials are configured in any workflow.
6. No workflow is activated (`active: false` on all 6).

**This plan does not authorize execution. Only Owner approval authorizes execution.**

---

## Table of Contents

1. Purpose
2. Scope
3. Out of Scope
4. Safety Rules (Hard Constraints)
5. Preconditions Before Any Sandbox Execution
6. Workflow-by-Workflow Validation Checklist
7. Dummy Test Data Policy
8. Credential Placeholder Policy
9. Expected Logs
10. Owner Approval Gate
11. Rollback and Stop Conditions
12. PASS / BLOCKED Criteria
13. Phase Connections

---

## 1. Purpose

Phase 14 confirmed that all 6 Phase 8 n8n workflow skeletons can be **imported** into a sandbox n8n instance without errors. Phase 16 plans the next step: **manually triggering each imported workflow using dummy/test data** to verify that the node logic executes as expected within a sandbox environment.

**Goal of sandbox runtime validation:**
- Confirm each workflow can be triggered manually without crashing.
- Confirm each workflow processes dummy input data through its node chain.
- Confirm approval gate logic (approval_publishing) correctly routes approved vs. non-approved items.
- Confirm all publish/send/spend nodes remain NoOp stubs and do not call any real external API.
- Confirm that no real credentials are required to run the dummy path.
- Confirm log nodes produce structured output matching `schemas/log-entry.schema.json`.
- Confirm Error Trigger chains are reachable in error scenarios.

**This is not a production readiness test.** It is a sandbox-only functional smoke test.

---

## 2. Scope

| Item | In Scope |
|------|----------|
| Manual trigger of each workflow using dummy JSON test data | YES |
| Verifying node execution chain completes without errors | YES |
| Verifying approval gate logic routes correctly (approval_publishing) | YES |
| Verifying NoOp stubs remain NoOp (no real API calls) | YES |
| Verifying Code node output fields match schema field names | YES |
| Verifying Error Trigger path is reachable | YES |
| Recording pass/fail result per workflow in sandbox execution log | YES |
| Noting any node errors, unexpected stops, or missing fields | YES |

**Applies to all 6 Phase 8 workflow skeletons:**

| ID | Workflow File | Risk Level |
|----|--------------|------------|
| WF-01 | `n8n/workflows/content_auto_skeleton.json` | Standard |
| WF-02 | `n8n/workflows/creative_asset_auto_skeleton.json` | Standard |
| WF-03 | `n8n/workflows/ads_pack_auto_skeleton.json` | High |
| WF-04 | `n8n/workflows/crm_followup_auto_skeleton.json` | High |
| WF-05 | `n8n/workflows/comment_inbox_reply_assistant_skeleton.json` | High |
| WF-06 | `n8n/workflows/approval_publishing_skeleton.json` | High |

---

## 3. Out of Scope

The following are **explicitly excluded** from Phase 16. Attempting any item below is a STOP condition.

| Out of Scope | Reason |
|-------------|--------|
| Configuring real API credentials (Google Sheets, Meta, Telegram, Zalo, Supabase, OpenAI, etc.) | Credentials must not be added until a future credential-setup phase |
| Activating any workflow (setting `active: true`) | Workflows must remain inactive at all times in Phase 16 |
| Connecting any workflow to a live external service | No real external calls in sandbox testing |
| Posting any content to social media (Facebook, Instagram, TikTok, Zalo) | No auto-post in any test scenario |
| Sending real messages to real customers (Zalo, Messenger, SMS) | No real customer contact in any test scenario |
| Committing real ad campaign budgets (Meta Ads, TikTok Ads) | No real ads spend under any circumstance |
| Using production n8n instance | Sandbox/test instance only |
| Using real customer PII (phone numbers, names, order history) as test data | Dummy test data only |
| Replacing REPLACE_WITH_* placeholders with real credentials | Placeholder policy must remain intact |
| Modifying workflow JSON files in the repo | Phase 8 JSON files remain untouched |
| Claiming production readiness based on sandbox test PASS | Sandbox PASS ≠ production readiness |
| Running workflow via webhook with a live internet-facing endpoint | Manual trigger only in sandbox |

---

## 4. Safety Rules (Hard Constraints)

These rules apply at all times and cannot be overridden by any test result.

| Rule ID | Rule |
|---------|------|
| SR-01 | All 6 workflows must remain `active: false` at all times during Phase 16. |
| SR-02 | No real credentials may be added to any workflow or n8n credential store. |
| SR-03 | No real customer data (PII) may be used as test input. All test data must be dummy/placeholder. |
| SR-04 | No content may be posted to any social platform during or after testing. |
| SR-05 | No messages may be sent to real customers during or after testing. |
| SR-06 | No ad campaigns may be created, scheduled, or triggered during testing. |
| SR-07 | Testing must occur on a sandbox/test n8n instance only — not production. |
| SR-08 | If a node attempts to connect to a real external API, stop immediately and record as BLOCKED. |
| SR-09 | REPLACE_WITH_* placeholders must remain in place throughout Phase 16. |
| SR-10 | Phase 8 workflow JSON files in the repo must not be modified. |
| SR-11 | Only Owner (Bo Bao) may authorize test execution to begin. |
| SR-12 | Only Owner (Bo Bao) may set approval_status = Approved in approval gate tests. |

---

## 5. Preconditions Before Any Sandbox Execution

All items below must be confirmed BEFORE executing any workflow test. If any item is NO or UNKNOWN, do not proceed.

| ID | Precondition | Expected State | Confirmed? |
|----|-------------|----------------|-----------|
| PC-01 | Phase 16 plan read and approved by Owner | OWNER_APPROVED | [ ] |
| PC-02 | Codex has reviewed Phase 16 plan and issued PASS | CODEX_PASS | [ ] |
| PC-03 | Sandbox n8n instance accessible (not production) | YES | [ ] |
| PC-04 | All 6 workflows are present in n8n (from Phase 14 import) | YES — 6/6 | [ ] |
| PC-05 | All 6 workflows show `active: false` / inactive toggle in n8n | INACTIVE | [ ] |
| PC-06 | No real credentials are configured in any workflow node | NO real credentials | [ ] |
| PC-07 | Dummy test data has been prepared (see Section 7) | READY | [ ] |
| PC-08 | This execution log is open and ready to fill | OPEN | [ ] |
| PC-09 | Phase 14 execution log is available for reference | AVAILABLE | [ ] |
| PC-10 | 60-minute time window is allocated for the session | YES | [ ] |
| PC-11 | Owner understands this is sandbox-only (not production test) | CONFIRMED | [ ] |
| PC-12 | No active internet-facing webhook endpoint configured for WF-06 | CONFIRMED | [ ] |

---

## 6. Workflow-by-Workflow Validation Checklist

For each workflow, the test sequence is:

1. Open workflow in n8n canvas.
2. Confirm it is inactive.
3. Use "Test workflow" / Manual Trigger with dummy JSON input.
4. Observe execution panel — check node-by-node result.
5. Record pass/fail for each check in the table.

---

### WF-01 — content_auto_skeleton

**Risk Level:** Standard
**Trigger:** Manual Trigger node (already in workflow)
**Test Input (dummy):**

```json
{
  "brand_name": "TEST_BRAND",
  "platform": "Facebook",
  "content_angle": "Product Highlight",
  "target_audience": "LOCAL_TEST",
  "offer": "TEST_OFFER",
  "session_id": "TEST-SESSION-001"
}
```

| Check ID | Check | Expected Result | Actual Result | Pass/Fail |
|----------|-------|----------------|---------------|-----------|
| WF01-01 | Workflow opens in canvas without error | OK | | |
| WF01-02 | Active toggle shows INACTIVE | INACTIVE | | |
| WF01-03 | Manual trigger fires without crash | Execution starts | | |
| WF01-04 | Set Input node passes data to next node | Fields forwarded | | |
| WF01-05 | Load Brand Brain stub runs without error | Stub output produced | | |
| WF01-06 | AI Draft stub runs without error | Stub draft produced | | |
| WF01-07 | Validate Fields node runs without error | Validation result present | | |
| WF01-08 | If Validation routes correctly | TRUE or FALSE branch taken | | |
| WF01-09 | Set Draft Status node runs without error | draft_status field set | | |
| WF01-10 | Write Log stub runs — output contains log_id field | log_id present | | |
| WF01-11 | NoOp Approval Queue stub is reachable | NoOp passes | | |
| WF01-12 | No real external API called during execution | NONE | | |
| WF01-13 | No content posted to any platform | NONE | | |
| WF01-14 | Sticky Note: DO NOT ACTIVATE warning visible on canvas | VISIBLE | | |
| WF01-OVERALL | Overall WF-01 result | PASS / BLOCKED | | |

**Extra check if validation fails path is taken:**

| Check ID | Check | Expected Result | Actual Result | Pass/Fail |
|----------|-------|----------------|---------------|-----------|
| WF01-F01 | Set Draft Status with error route produces draft_status=Failed | draft_status=Failed | | |
| WF01-F02 | Error stop node reached on failure path | Stop node reached | | |

---

### WF-02 — creative_asset_auto_skeleton

**Risk Level:** Standard
**Trigger:** Manual Trigger node
**Test Input (dummy):**

```json
{
  "brand_name": "TEST_BRAND",
  "asset_type": "Image",
  "platform": "Instagram",
  "content_angle": "Lifestyle Shot",
  "visual_direction": "TEST_VISUAL",
  "session_id": "TEST-SESSION-002"
}
```

| Check ID | Check | Expected Result | Actual Result | Pass/Fail |
|----------|-------|----------------|---------------|-----------|
| WF02-01 | Workflow opens in canvas without error | OK | | |
| WF02-02 | Active toggle shows INACTIVE | INACTIVE | | |
| WF02-03 | Manual trigger fires without crash | Execution starts | | |
| WF02-04 | Set Input node passes data to next node | Fields forwarded | | |
| WF02-05 | Load Brand Brain stub runs without error | Stub output produced | | |
| WF02-06 | AI Draft stub runs without error | Brief stub produced | | |
| WF02-07 | Validate Fields node runs without error | Validation result present | | |
| WF02-08 | If Validation routes correctly | TRUE or FALSE branch taken | | |
| WF02-09 | Set Draft Status node runs without error | draft_status field set | | |
| WF02-10 | Write Log stub runs — output contains log_id field | log_id present | | |
| WF02-11 | NoOp Approval Queue stub is reachable | NoOp passes | | |
| WF02-12 | No real external API called during execution | NONE | | |
| WF02-13 | No creative asset generated or published | NONE | | |
| WF02-14 | Sticky Note: DO NOT ACTIVATE warning visible on canvas | VISIBLE | | |
| WF02-OVERALL | Overall WF-02 result | PASS / BLOCKED | | |

---

### WF-03 — ads_pack_auto_skeleton

**Risk Level:** HIGH — Contains ads-pack node chain. No ad spend must occur.
**Trigger:** Manual Trigger node
**Test Input (dummy):**

```json
{
  "brand_name": "TEST_BRAND",
  "campaign_objective": "Awareness",
  "platform": "Facebook",
  "audience_target": "LOCAL_TEST",
  "offer": "TEST_OFFER",
  "budget_placeholder": "DO_NOT_SPEND",
  "session_id": "TEST-SESSION-003"
}
```

| Check ID | Check | Expected Result | Actual Result | Pass/Fail |
|----------|-------|----------------|---------------|-----------|
| WF03-01 | Workflow opens in canvas without error | OK | | |
| WF03-02 | Active toggle shows INACTIVE | INACTIVE | | |
| WF03-03 | Sticky Note: **NO ADS SPEND** warning visible on canvas | VISIBLE — HIGH RISK | | |
| WF03-04 | Manual trigger fires without crash | Execution starts | | |
| WF03-05 | Set Input node passes data to next node | Fields forwarded | | |
| WF03-06 | Load Brand Brain stub runs without error | Stub output produced | | |
| WF03-07 | AI Draft stub runs without error | Ads pack stub produced | | |
| WF03-08 | Validate Fields node runs without error | Validation result present | | |
| WF03-09 | If Validation routes correctly | TRUE or FALSE branch | | |
| WF03-10 | compliance_notes field present in output | compliance_notes present | | |
| WF03-11 | Write Log stub runs — output contains log_id field | log_id present | | |
| WF03-12 | NoOp Approval Queue stub is reachable | NoOp passes | | |
| WF03-13 | **CRITICAL: No Meta Ads API node called** | NO API call | | |
| WF03-14 | **CRITICAL: No TikTok Ads API node called** | NO API call | | |
| WF03-15 | **CRITICAL: No ad campaign created or scheduled** | NONE | | |
| WF03-16 | **CRITICAL: No real budget field populated or committed** | NONE | | |
| WF03-17 | No real external API called at any point | NONE | | |
| WF03-OVERALL | Overall WF-03 result | PASS / BLOCKED | | |

**If any WF03 CRITICAL check fails → STOP immediately. Record BLOCKED. Do not proceed.**

---

### WF-04 — crm_followup_auto_skeleton

**Risk Level:** HIGH — Contains CRM/messaging chain. No real messages must be sent.
**Trigger:** Manual Trigger node
**Test Input (dummy):**

```json
{
  "brand_name": "TEST_BRAND",
  "customer_segment": "New Lead",
  "channel": "Zalo",
  "trigger_event": "form_submit",
  "customer_id": "TEST-CUST-001",
  "customer_name": "TEST_NAME",
  "session_id": "TEST-SESSION-004"
}
```

| Check ID | Check | Expected Result | Actual Result | Pass/Fail |
|----------|-------|----------------|---------------|-----------|
| WF04-01 | Workflow opens in canvas without error | OK | | |
| WF04-02 | Active toggle shows INACTIVE | INACTIVE | | |
| WF04-03 | Sticky Note: **NO AUTO-SEND** warning visible on canvas | VISIBLE — HIGH RISK | | |
| WF04-04 | Manual trigger fires without crash | Execution starts | | |
| WF04-05 | Set Input node passes data to next node | Fields forwarded | | |
| WF04-06 | Load Brand Brain stub runs without error | Stub output produced | | |
| WF04-07 | AI Draft stub runs without error | CRM sequence stub produced | | |
| WF04-08 | Validate Fields node runs without error | Validation result present | | |
| WF04-09 | If Validation routes correctly | TRUE or FALSE branch | | |
| WF04-10 | human_review_required field = true in output | human_review_required=true | | |
| WF04-11 | Write Log stub runs — output contains log_id field | log_id present | | |
| WF04-12 | NoOp Approval Queue stub is reachable | NoOp passes | | |
| WF04-13 | **CRITICAL: No Zalo API node called** | NO API call | | |
| WF04-14 | **CRITICAL: No Facebook Messenger API node called** | NO API call | | |
| WF04-15 | **CRITICAL: No SMS node called** | NO API call | | |
| WF04-16 | **CRITICAL: No real message sent to any customer** | NONE | | |
| WF04-17 | No customer PII present in test execution output | NONE (test data only) | | |
| WF04-OVERALL | Overall WF-04 result | PASS / BLOCKED | | |

**If any WF04 CRITICAL check fails → STOP immediately. Record BLOCKED. Do not proceed.**

---

### WF-05 — comment_inbox_reply_assistant_skeleton

**Risk Level:** HIGH — Contains reply generation and escalation routing. No real replies must be posted.
**Trigger:** Manual Trigger node
**Test Input — Standard path (dummy):**

```json
{
  "brand_name": "TEST_BRAND",
  "comment_text": "Menu có gì vậy shop?",
  "comment_source": "Facebook",
  "commenter_id": "TEST-USER-001",
  "is_escalation": false,
  "session_id": "TEST-SESSION-005A"
}
```

**Test Input — Escalation path (dummy):**

```json
{
  "brand_name": "TEST_BRAND",
  "comment_text": "Đồ ăn này tệ quá, thất vọng!",
  "comment_source": "Facebook",
  "commenter_id": "TEST-USER-002",
  "is_escalation": true,
  "session_id": "TEST-SESSION-005B"
}
```

| Check ID | Check | Expected Result | Actual Result | Pass/Fail |
|----------|-------|----------------|---------------|-----------|
| WF05-01 | Workflow opens in canvas without error | OK | | |
| WF05-02 | Active toggle shows INACTIVE | INACTIVE | | |
| WF05-03 | Sticky Note: escalation and no-auto-reply warning visible | VISIBLE — HIGH RISK | | |
| WF05-04 | Manual trigger fires without crash (standard path) | Execution starts | | |
| WF05-05 | Set Input node passes data to next node | Fields forwarded | | |
| WF05-06 | Load Brand Brain stub runs without error | Stub output produced | | |
| WF05-07 | Escalation check If-node routes correctly — standard path (FALSE) | FALSE branch taken | | |
| WF05-08 | AI Draft stub produces draft_reply on standard path | draft_reply present | | |
| WF05-09 | human_review_required field = true in standard path output | human_review_required=true | | |
| WF05-10 | Write Log stub runs — output contains log_id field | log_id present | | |
| WF05-11 | NoOp Approval Queue stub is reachable | NoOp passes | | |
| WF05-12 | Escalation path (TRUE) triggers correctly | TRUE branch taken | | |
| WF05-13 | Escalation path sets draft_reply = null | draft_reply=null | | |
| WF05-14 | Escalation path routes to Owner-review node (not auto-reply) | Owner review node reached | | |
| WF05-15 | **CRITICAL: No Facebook comment reply API node called** | NO API call | | |
| WF05-16 | **CRITICAL: No Instagram reply API node called** | NO API call | | |
| WF05-17 | **CRITICAL: No TikTok reply API node called** | NO API call | | |
| WF05-18 | **CRITICAL: No real reply posted to any comment** | NONE | | |
| WF05-OVERALL | Overall WF-05 result | PASS / BLOCKED | | |

**If any WF05 CRITICAL check fails → STOP immediately. Record BLOCKED. Do not proceed.**

---

### WF-06 — approval_publishing_skeleton

**Risk Level:** HIGH — Approval gate + 5-branch publish routing. All publish stubs must remain NoOp.
**Trigger:** Webhook node (use n8n built-in test webhook or sandbox HTTP call — see notes below)

> **Important:** WF-06 uses a Webhook trigger, not a Manual Trigger. To test in sandbox:
> Use the n8n "Test Webhook" feature (n8n generates a temporary test webhook URL visible in canvas
> when workflow is in test mode). Do NOT expose this URL to public internet. Use localhost or
> sandbox network only. Do NOT set `active: true` — the test webhook works while workflow is in
> test mode without activation.

**Test Input — Approved item (dummy):**

```json
{
  "approval_status": "Approved",
  "owner_decision": "Approved",
  "item_type": "Content Output",
  "item_id": "TEST-ITEM-001",
  "brand_name": "TEST_BRAND",
  "session_id": "TEST-SESSION-006A"
}
```

**Test Input — Not Approved item (dummy):**

```json
{
  "approval_status": "Draft",
  "owner_decision": null,
  "item_type": "Content Output",
  "item_id": "TEST-ITEM-002",
  "brand_name": "TEST_BRAND",
  "session_id": "TEST-SESSION-006B"
}
```

| Check ID | Check | Expected Result | Actual Result | Pass/Fail |
|----------|-------|----------------|---------------|-----------|
| WF06-01 | Workflow opens in canvas without error | OK | | |
| WF06-02 | Active toggle shows INACTIVE | INACTIVE | | |
| WF06-03 | Sticky Note: DO NOT ACTIVATE + approval gate warning visible | VISIBLE — HIGH RISK | | |
| WF06-04 | Test webhook URL available in n8n test mode | URL shown by n8n | | |
| WF06-05 | Webhook receives approved dummy payload without crash | Execution starts | | |
| WF06-06 | Code: Check Approval Status node runs without error | approval_valid computed | | |
| WF06-07 | If: Is Approved routes TRUE for approved payload | TRUE branch taken | | |
| WF06-08 | Switch: Item Type routes to correct branch (Content Output) | Correct branch taken | | |
| WF06-09 | NoOp: STUB — Publish Content to Platform remains NoOp | NoOp pass — no publish | | |
| WF06-10 | Code: Write Approval Log runs — log_id present in output | log_id present | | |
| WF06-11 | Webhook receives not-approved dummy payload | Execution starts | | |
| WF06-12 | If: Is Approved routes FALSE for not-approved payload | FALSE branch taken | | |
| WF06-13 | Set: Block — Not Approved node runs — block_reason set | block_reason present | | |
| WF06-14 | Code: Write Block Log runs — publishingBlocked=true | publishingBlocked=true | | |
| WF06-15 | Stop and Error: Not Approved halts execution with error message | Execution stops | | |
| WF06-16 | **CRITICAL: All 5 NoOp publish stubs remain NoOp — no platform API called** | NO API call | | |
| WF06-17 | **CRITICAL: No content posted to Facebook/Instagram/TikTok/Zalo** | NONE | | |
| WF06-18 | **CRITICAL: No creative brief archived to real Google Drive** | NONE | | |
| WF06-19 | **CRITICAL: No ad campaign created via Meta Ads or TikTok Ads** | NONE | | |
| WF06-20 | **CRITICAL: No CRM message sent to any customer** | NONE | | |
| WF06-21 | **CRITICAL: No comment reply posted to any real channel** | NONE | | |
| WF06-22 | Switch routes tested for additional item types (Creative Brief, Ads Pack, CRM Follow-Up, Comment Reply) | Routes correctly | | |
| WF06-OVERALL | Overall WF-06 result | PASS / BLOCKED | | |

**If any WF06 CRITICAL check fails → STOP immediately. Record BLOCKED. Do not proceed.**

---

## 7. Dummy Test Data Policy

| Rule | Detail |
|------|--------|
| No real customer data | All test inputs must use dummy values. No real customer names, phone numbers, order IDs, or personal information. |
| No real brand URLs | Test inputs may use `TEST_BRAND` or `"Vị Cuốn (TEST)"` — never a real production Facebook Page ID, Zalo OA ID, or store URL. |
| No real offer prices | Use `"TEST_OFFER"` as placeholder. Do not use real discount amounts. |
| No real platform credentials | REPLACE_WITH_* values must remain as-is. Do not substitute real API keys. |
| No real webhook endpoints | WF-06 test webhook URL generated by n8n sandbox is local only. Do not share or expose publicly. |
| Dummy IDs format | Use `TEST-ITEM-NNN`, `TEST-CUST-NNN`, `TEST-SESSION-NNN` formats for all test record IDs. |
| Real execution log | While test data is dummy, the execution log recording test results is real and must be filled accurately. |

---

## 8. Credential Placeholder Policy

All 6 workflows contain `REPLACE_WITH_*` placeholder strings for credentials. These must remain as-is throughout Phase 16.

| Placeholder | Workflow(s) | Policy |
|-------------|-------------|--------|
| `REPLACE_WITH_GOOGLE_SHEETS_CREDENTIAL` | All 6 (log stubs) | DO NOT replace |
| `REPLACE_WITH_SUPABASE_CREDENTIAL` | All 6 (log stubs) | DO NOT replace |
| `REPLACE_WITH_OPENAI_CREDENTIAL` | WF-01, WF-02, WF-03, WF-04, WF-05 (AI stubs) | DO NOT replace |
| `REPLACE_WITH_META_ADS_CREDENTIAL` | WF-03, WF-06 | DO NOT replace |
| `REPLACE_WITH_TIKTOK_ADS_CREDENTIAL` | WF-03, WF-06 | DO NOT replace |
| `REPLACE_WITH_MESSAGING_CREDENTIAL` | WF-04, WF-06 | DO NOT replace |
| `REPLACE_WITH_PLATFORM_CREDENTIAL` | WF-05, WF-06 | DO NOT replace |
| `REPLACE_WITH_GOOGLE_DRIVE_CREDENTIAL` | WF-06 | DO NOT replace |
| `REPLACE_WITH_WEBHOOK_PATH` | WF-06 | DO NOT replace with production path |
| `REPLACE_WITH_INSTANCE_ID` | All 6 (meta) | DO NOT replace |
| `REPLACE_WITH_VERSION_ID` | All 6 (meta) | DO NOT replace |

**Expected behavior:** n8n will show "Credential not found" or similar warnings for all credential placeholders. This is expected and is NOT a test failure. Code nodes and NoOp nodes do not require real credentials to execute stub logic.

---

## 9. Expected Logs

During sandbox runtime validation, the following log outputs are expected:

| Log Source | Expected Content | Format |
|------------|-----------------|--------|
| n8n execution panel | Per-node input/output JSON visible after each test run | n8n native |
| WF-01 Write Log stub output | `log_id`, `timestamp`, `phase`, `agent_name`, `action_type`, `input_ref`, `output_ref`, `status`, `summary` | log-entry.schema.json |
| WF-02 Write Log stub output | Same fields as WF-01 | log-entry.schema.json |
| WF-03 Write Log stub output | Same fields + `compliance_notes` reference | log-entry.schema.json |
| WF-04 Write Log stub output | Same fields + `human_review_required=true` reference | log-entry.schema.json |
| WF-05 Write Log stub output | Same fields + escalation path indicator | log-entry.schema.json |
| WF-06 Approval Log output | Same fields + `approvalLogged=true` | log-entry.schema.json |
| WF-06 Block Log output | `log_id`, `publishingBlocked=true`, `block_reason`, `approval_block_reason` | log-entry.schema.json |
| Phase 16 execution log | Results filled into `logs/PHASE_16_SANDBOX_RUNTIME_VALIDATION_PLAN_LOG.md` | This phase's log |

**No log output is written to external systems in skeleton mode.** All Code node log stubs return their log entry as JSON in the n8n execution panel only. No Google Sheets row is written. No Supabase insert occurs.

---

## 10. Owner Approval Gate

Sandbox runtime validation **may not begin** until Owner completes this gate:

| Item | Owner Action | Status |
|------|-------------|--------|
| Read this plan (Phase 16 doc) | Owner confirms read | [ ] PENDING |
| Codex PASS confirmed | Codex issues PASS on this doc | [ ] PENDING |
| Confirms sandbox n8n instance ready | Owner confirms instance URL and sandbox status | [ ] PENDING |
| Confirms Phase 14 import still present (6/6 workflows) | Owner verifies in n8n UI | [ ] PENDING |
| Confirms all 6 workflows still inactive | Owner verifies active toggle off | [ ] PENDING |
| Confirms no real credentials present | Owner verifies no real credential connected | [ ] PENDING |
| Confirms dummy test data prepared | Owner confirms test data ready | [ ] PENDING |
| Signs off: OWNER_APPROVED to execute Phase 16 | **Owner explicitly approves execution** | [ ] PENDING |

**Only after all 8 items are confirmed may test execution begin.**

Owner sign-off: `[ ] OWNER_APPROVED — Phase 16 sandbox runtime validation authorized`
Date: ______________________
Signed by: ______________________

---

## 11. Rollback and Stop Conditions

If any of the following occur at any point during Phase 16 execution, **STOP IMMEDIATELY**:

| Stop ID | Condition | Immediate Action |
|---------|-----------|-----------------|
| ST-01 | Any workflow is accidentally activated (`active: true`) | Deactivate immediately. Record BLOCKED. End session. |
| ST-02 | Any real credential is added to a workflow node | Remove credential immediately. Record BLOCKED. End session. |
| ST-03 | Any node attempts to call a real external API (Meta, TikTok, Zalo, Google, OpenAI, etc.) | Stop execution immediately. Record BLOCKED. Do not retry. |
| ST-04 | Any content is posted to any social platform | Stop. Record BLOCKED. Report to Owner immediately. |
| ST-05 | Any real customer receives a message | Stop. Record BLOCKED. Report to Owner immediately. |
| ST-06 | Any ad campaign is created, scheduled, or triggered | Stop. Record BLOCKED. Report to Owner immediately. |
| ST-07 | A production n8n instance is being used | Stop. Record BLOCKED. Do not proceed until sandbox confirmed. |
| ST-08 | Real customer PII appears in any execution output | Stop. Record BLOCKED. Do not save output. |
| ST-09 | n8n execution error occurs that cannot be explained by missing credentials | Stop. Record BLOCKED. Do not attempt to fix workflow JSON. |
| ST-10 | Execution log cannot be filled (e.g., n8n UI not accessible) | Record BLOCKED. End session. |

**Rollback procedure after any STOP condition:**
1. Do not save or share any execution output that triggered the stop condition.
2. Record the stop condition in the execution log (stop ID, what happened, timestamp).
3. Mark the affected workflow as BLOCKED in the execution log.
4. Do not proceed to the next workflow until the stop condition is investigated.
5. Report to Owner and await further instructions.
6. Do not modify any workflow JSON in the repo.

---

## 12. PASS / BLOCKED Criteria

### Overall Phase 16 PASS criteria

All of the following must be true:

- [ ] All 8 preconditions (Section 5) confirmed before execution.
- [ ] WF-01 validation result = PASS.
- [ ] WF-02 validation result = PASS.
- [ ] WF-03 validation result = PASS (all CRITICAL checks confirmed).
- [ ] WF-04 validation result = PASS (all CRITICAL checks confirmed).
- [ ] WF-05 validation result = PASS (both standard and escalation paths confirmed).
- [ ] WF-06 validation result = PASS (approved path, not-approved path, and all 5 switch branches confirmed, all CRITICAL checks confirmed).
- [ ] No real credentials added at any point.
- [ ] No workflow activated at any point.
- [ ] No real external API called at any point.
- [ ] No real content posted, no real message sent, no real ad spend.
- [ ] Execution log (`logs/PHASE_16_SANDBOX_RUNTIME_VALIDATION_PLAN_LOG.md`) fully filled.
- [ ] Owner reviewed and confirmed PASS.

### Overall Phase 16 BLOCKED criteria

Any of the following makes the phase BLOCKED:

- Any STOP condition (ST-01 through ST-10) was triggered.
- Any CRITICAL check for WF-03, WF-04, WF-05, or WF-06 failed.
- Any workflow was found to be `active: true` during the session.
- Any real credential was present or added.
- Execution log cannot be completed.

**PARTIAL result:** If some but not all workflows are tested, record tested workflows individually and note which were not reached. Do not claim PASS for untested workflows.

---

## 13. Phase Connections

| Phase | Description | Relationship |
|-------|-------------|-------------|
| Phase 8 | n8n Importable Workflow Skeletons (commit `ad867b3`) | Source of all 6 workflow JSON files |
| Phase 9 | n8n Import Validation Pack | Static validator + import checklist |
| Phase 10 | n8n Import Dry Run and Validation | Import procedure + manual static inspection |
| Phase 11 | n8n Import Dry-Run Evidence Pack | Evidence log template + per-node checklist |
| Phase 12 | n8n Import Dry-Run Execution Readiness | GO/NO-GO readiness gate |
| Phase 13 | Controlled n8n Import Dry-Run Handoff | Operator session guide |
| Phase 14 | Owner n8n Sandbox Dry-Run Execution Log | Confirmed: 6/6 imported, all inactive, PASS |
| Phase 15 | Codex Review Gate | Codex PASS on Phase 14 result |
| **Phase 16** | **This document — Sandbox Runtime Validation Plan** | **Plan for manual trigger testing of imported workflows** |
| Phase 17 (future) | Credential Setup Planning | Plan for configuring real credentials (post Phase 16 PASS) |

---

## Known Limitations

1. **Credential-dependent nodes cannot be fully validated in Phase 16.** Code node stubs execute without real credentials, but in production, nodes requiring credentials (Google Sheets, Meta API, etc.) will behave differently. Phase 16 validates stub logic only.

2. **WF-06 webhook trigger requires extra steps.** Unlike WF-01 through WF-05 (Manual Trigger), WF-06 uses a Webhook trigger. The n8n test webhook feature must be used — the workflow must NOT be activated to do this.

3. **AI stub output is static.** All AI-related Code nodes are stubs that return hardcoded dummy output. Phase 16 does not validate real AI generation quality — only that the node chain executes without crashing.

4. **Log stubs write to execution panel only.** No external log destination (Google Sheets, Supabase) is tested in Phase 16. Log output validation is limited to checking that the Code node produces correctly structured JSON in the n8n execution panel.

5. **Error Trigger path requires n8n to generate an error.** Testing the error chain path (Error Trigger → Set Error Log → Stop and Error: Workflow Error) may require intentionally triggering a node error. If this is not tested, record as SKIPPED (non-blocking) and note for Phase 17.

6. **This plan does not guarantee production correctness.** A PASS in Phase 16 means the sandbox stub logic executes without crashing. It does not mean the workflows are production-ready or that real integrations will behave correctly.

---

*End of Phase 16 — Sandbox Runtime Validation Plan*
*Plan only — not an execution record — do not interpret as evidence of completed tests*
