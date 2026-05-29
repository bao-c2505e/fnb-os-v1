# Phase 21 — Remaining Workflows Sandbox Plan Log

**File:** logs/phase_21_remaining_workflows_sandbox_plan.md
**Phase:** 21
**Date:** 2026-05-29
**Created By:** Claude Code (Builder, AGT-02)
**Status:** PLAN_RECORDED — not_executed_yet

---

## Overview

This log records the sandbox execution plan for the 5 remaining workflow skeletons not yet covered by Phase 20A–20C.
`content_auto_skeleton` (WF-01) completed Phase 20A–20C with result **PASS** (commit `50df2af`).
The 5 workflows below are scheduled for manual sandbox execution starting with Phase 22A.

---

## Remaining Workflows Sandbox Plan Table

| workflow_name | risk_level | planned_order | execution_status | payload_type | active_status_required | credentials_allowed | real_customer_data_allowed | production_side_effect_allowed | evidence_required | log_required | next_phase |
|--------------|------------|--------------|-----------------|--------------|----------------------|--------------------|--------------------------|-----------------------------|-------------------|-------------|------------|
| creative_asset_auto_skeleton | Standard | 1 | not_executed_yet | dummy | inactive / active=false | placeholder_or_none | no | no | yes | yes | Phase 22A |
| ads_pack_auto_skeleton | HIGH RISK | 2 | not_executed_yet | dummy | inactive / active=false | placeholder_or_none | no | no | yes | yes | Phase 23A |
| crm_followup_auto_skeleton | HIGH RISK | 3 | not_executed_yet | dummy | inactive / active=false | placeholder_or_none | no | no | yes | yes | Phase 24A |
| comment_inbox_reply_assistant | HIGH RISK | 4 | not_executed_yet | dummy | inactive / active=false | placeholder_or_none | no | no | yes | yes | Phase 25A |
| approval_publishing_skeleton | HIGH RISK | 5 | not_executed_yet | dummy | inactive / active=false (test webhook only) | placeholder_or_none | no | no | yes | yes | Phase 26A |

---

## Detail Per Workflow

### creative_asset_auto_skeleton

| Field | Value |
|-------|-------|
| workflow_file | `n8n/workflows/creative_asset_auto_skeleton.json` |
| n8n_name | FnB OS V1 — Creative Asset Auto [SKELETON] |
| risk_level | Standard |
| planned_order | 1 |
| execution_status | not_executed_yet |
| payload_file | `samples/sandbox/phase_17_test_payloads/creative_asset_auto_skeleton_test_payload.md` |
| payload_scenario | P17-WF02-S1 |
| payload_type | dummy |
| active_status_required | inactive / active=false |
| credentials_allowed | placeholder_or_none |
| real_customer_data_allowed | no |
| production_side_effect_allowed | no |
| auto_post_allowed | no |
| auto_reply_allowed | no |
| ads_spend_allowed | no |
| evidence_required | yes |
| log_required | yes |
| evidence_log_path | logs/phase_22a_creative_asset_auto_sandbox_evidence_log.md (to be created in Phase 22A) |
| scenarios_required | 1 (S1 — creative brief output, no real image generation) |
| critical_forbidden_checks | No real image generation API; no file upload to platform; no platform post |
| next_phase | Phase 22A — Evidence Capture Pack for creative_asset_auto_skeleton |

---

### ads_pack_auto_skeleton

| Field | Value |
|-------|-------|
| workflow_file | `n8n/workflows/ads_pack_auto_skeleton.json` |
| n8n_name | FnB OS V1 — Ads Pack Auto [SKELETON] |
| risk_level | HIGH RISK |
| planned_order | 2 |
| execution_status | not_executed_yet |
| payload_file | `samples/sandbox/phase_17_test_payloads/ads_pack_auto_skeleton_test_payload.md` |
| payload_scenario | P17-WF03-S1 |
| payload_type | dummy |
| active_status_required | inactive / active=false |
| credentials_allowed | placeholder_or_none |
| real_customer_data_allowed | no |
| production_side_effect_allowed | no |
| auto_post_allowed | no |
| ads_spend_allowed | no — NO ADS SPEND sticky must be visible |
| evidence_required | yes |
| log_required | yes |
| evidence_log_path | logs/phase_23a_ads_pack_auto_sandbox_evidence_log.md (to be created in Phase 23A) |
| scenarios_required | 1 (S1 — ads pack planning output with compliance_notes) |
| critical_forbidden_checks | NO Meta Ads API; NO TikTok Ads; NO Zalo Ads; no real Ad Account ID; no real Pixel ID; no budget |
| pre_run_extra_check | NO ADS SPEND sticky visible in n8n canvas |
| next_phase | Phase 23A — Evidence Capture Pack for ads_pack_auto_skeleton |

---

### crm_followup_auto_skeleton

| Field | Value |
|-------|-------|
| workflow_file | `n8n/workflows/crm_followup_auto_skeleton.json` |
| n8n_name | FnB OS V1 — CRM Followup Auto [SKELETON] |
| risk_level | HIGH RISK |
| planned_order | 3 |
| execution_status | not_executed_yet |
| payload_file | `samples/sandbox/phase_17_test_payloads/crm_followup_auto_skeleton_test_payload.md` |
| payload_scenarios | P17-WF04-S1 (new lead Messenger); P17-WF04-S2 (lapsed customer Zalo) |
| payload_type | dummy |
| active_status_required | inactive / active=false |
| credentials_allowed | placeholder_or_none |
| real_customer_data_allowed | no — fake names/phones/emails/IDs only |
| production_side_effect_allowed | no |
| auto_post_allowed | no |
| auto_reply_allowed | no — NO AUTO-SEND sticky must be visible |
| evidence_required | yes |
| log_required | yes |
| evidence_log_path | logs/phase_24a_crm_followup_auto_sandbox_evidence_log.md (to be created in Phase 24A) |
| scenarios_required | 2 mandatory (S1 new lead + S2 lapsed customer) |
| critical_forbidden_checks | NO Zalo OA API; NO Facebook Messenger API; NO SMS gateway; human_review_required=true in all outputs |
| pre_run_extra_check | NO AUTO-SEND sticky visible in n8n canvas |
| next_phase | Phase 24A — Evidence Capture Pack for crm_followup_auto_skeleton |

---

### comment_inbox_reply_assistant

| Field | Value |
|-------|-------|
| workflow_file | `n8n/workflows/comment_inbox_reply_assistant_skeleton.json` |
| n8n_name | FnB OS V1 — Comment Inbox Reply Assistant [SKELETON] |
| risk_level | HIGH RISK |
| planned_order | 4 |
| execution_status | not_executed_yet |
| payload_file | `samples/sandbox/phase_17_test_payloads/comment_inbox_reply_assistant_skeleton_test_payload.md` |
| payload_scenarios | P17-WF05-S1 (standard menu query — non-escalation); P17-WF05-S2 (angry complaint — escalation) |
| payload_type | dummy |
| active_status_required | inactive / active=false |
| credentials_allowed | placeholder_or_none |
| real_customer_data_allowed | no — fake commenter IDs, post IDs, page IDs only |
| production_side_effect_allowed | no |
| auto_post_allowed | no |
| auto_reply_allowed | no — NO AUTO-REPLY sticky must be visible |
| evidence_required | yes |
| log_required | yes |
| evidence_log_path | logs/phase_25a_comment_inbox_reply_sandbox_evidence_log.md (to be created in Phase 25A) |
| scenarios_required | 2 mandatory (S1 non-escalation + S2 escalation) |
| critical_forbidden_checks | NO FB/IG/TikTok/Zalo comment API; draft_reply=null on escalation scenario (S2) |
| escalation_gate_check | S2 MUST produce draft_reply=null and escalation_required=true |
| pre_run_extra_check | NO AUTO-REPLY sticky visible in n8n canvas |
| next_phase | Phase 25A — Evidence Capture Pack for comment_inbox_reply_assistant |

---

### approval_publishing_skeleton

| Field | Value |
|-------|-------|
| workflow_file | `n8n/workflows/approval_publishing_skeleton.json` |
| n8n_name | FnB OS V1 — Approval Publishing [SKELETON] |
| risk_level | HIGH RISK |
| planned_order | 5 |
| execution_status | not_executed_yet |
| payload_file | `samples/sandbox/phase_17_test_payloads/approval_publishing_skeleton_test_payload.md` |
| payload_scenarios | P17-WF06-S1 (approved payload); P17-WF06-S2 (not-approved payload) |
| payload_type | dummy |
| active_status_required | MUST NOT be activated — test webhook only (sandbox local, not public internet) |
| credentials_allowed | placeholder_or_none |
| real_customer_data_allowed | no |
| production_side_effect_allowed | no |
| auto_post_allowed | no |
| auto_reply_allowed | no |
| ads_spend_allowed | no |
| evidence_required | yes |
| log_required | yes |
| evidence_log_path | logs/phase_26a_approval_publishing_sandbox_evidence_log.md (to be created in Phase 26A) |
| scenarios_required | 2 mandatory (S1 approved path + S2 not-approved path) |
| trigger_method | n8n test webhook — sandbox local only — NO activation required |
| critical_forbidden_checks | NO FB post API; NO IG publish; NO TikTok; NO Zalo content; NO Google Drive file create; NO Meta Ads; NO TikTok Ads; NO Zalo messaging; NO comment reply API |
| switch_check | All 5 NoOp stubs confirmed on S1 (approved path) |
| block_check | Stop and Error confirmed on S2 (not-approved path) |
| next_phase | Phase 26A — Evidence Capture Pack for approval_publishing_skeleton |

---

## Phase 20C Reference (Content Auto — PASS)

| workflow_name | risk_level | execution_status | result | commit |
|--------------|------------|-----------------|--------|--------|
| content_auto_skeleton | Standard | executed | PASS | `50df2af` |

---

## Safety Checks — Phase 21 Build

| Check | Status |
|-------|--------|
| Workflow JSON modified | NO |
| active=true introduced | NO |
| Real credentials added | NO |
| Real customer data added | NO |
| Workflow execution performed by Builder | NO |
| Workflow execution claimed | NO |
| Auto-post executed | NO |
| Auto-reply executed | NO |
| Ads spend occurred | NO |
| Production readiness claimed | NO |
| Secret scan | CLEAN |
| Branch | main |
| Latest commit at Phase 21 build | 50df2af |
