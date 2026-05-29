# Phase 21 — Sandbox Manual Execution Expansion Plan

**Document:** 35_PHASE_21_SANDBOX_MANUAL_EXECUTION_EXPANSION_PLAN.md
**Phase:** 21
**Date:** 2026-05-29
**Created By:** Claude Code (Builder, AGT-02)
**Status:** PLAN_READY — AWAITING OWNER REVIEW

---

## Section A — Purpose of Phase 21

Phase 21 creates the expansion plan for manual sandbox execution of the **5 remaining n8n workflow skeletons** that were not covered in Phases 20A–20C.

Phase 20A–20C covered `content_auto_skeleton` (WF-01, Standard risk) as the first manual sandbox execution. That workflow PASSED. Phase 21 now maps out the plan to extend that manual sandbox execution methodology to the remaining 5 workflows.

**Phase 21 does NOT execute any workflow.**
**Phase 21 does NOT activate any workflow.**
**Phase 21 does NOT claim production readiness.**

Phase 21 is a planning document phase. Execution occurs in future phases (Phase 22A onward), one workflow at a time, following the same 3-part structure used for content_auto_skeleton:
- Sub-phase A: Evidence Capture Pack
- Sub-phase B: Owner Manual Sandbox Runbook
- Sub-phase C: Owner Evidence Submission

---

## Section B — Phase 20C Summary and PASS Reference

| Item | Detail |
|------|--------|
| Phase | 20C — Owner Evidence Submission |
| Workflow | `content_auto_skeleton` (WF-01) |
| Risk Level | Standard |
| Execution Date | 2026-05-29 ~01:25 |
| Operator | Bo Bao (Owner) |
| Execution Type | manual_sandbox |
| Result | **PASS** |
| n8n Result | "Workflow executed successfully" |
| Nodes Executed | 9 happy-path nodes — all green |
| Output Behavior | REPLACE_WITH_* placeholders confirmed (correct dummy/sandbox behavior) |
| active_status | inactive / active=false — confirmed before and after run |
| Real Credentials Used | NO |
| Real Customer Data Used | NO |
| Auto-Post Executed | NO |
| Auto-Reply Executed | NO |
| Ads Spend Occurred | NO |
| Production Readiness Claimed | NO |
| Workflow JSON Modified | NO |
| Evidence Log | `logs/phase_20a_content_auto_sandbox_evidence_log.md` |
| Codex Review | PASS |
| Latest Commit at Phase 20C Close | `50df2af` |

Phase 20C PASS establishes the baseline manual sandbox execution methodology. Phase 21 extends this to the remaining 5 workflows.

---

## Section C — Remaining 5 Workflows

| # | Workflow Name | File Path | n8n Name | Risk Level | Trigger Type |
|---|--------------|-----------|----------|------------|--------------|
| 1 | creative_asset_auto_skeleton | `n8n/workflows/creative_asset_auto_skeleton.json` | FnB OS V1 — Creative Asset Auto [SKELETON] | Standard | Manual Trigger |
| 2 | ads_pack_auto_skeleton | `n8n/workflows/ads_pack_auto_skeleton.json` | FnB OS V1 — Ads Pack Auto [SKELETON] | **HIGH RISK** | Manual Trigger |
| 3 | crm_followup_auto_skeleton | `n8n/workflows/crm_followup_auto_skeleton.json` | FnB OS V1 — CRM Followup Auto [SKELETON] | **HIGH RISK** | Manual Trigger |
| 4 | comment_inbox_reply_assistant | `n8n/workflows/comment_inbox_reply_assistant_skeleton.json` | FnB OS V1 — Comment Inbox Reply Assistant [SKELETON] | **HIGH RISK** | Manual Trigger |
| 5 | approval_publishing_skeleton | `n8n/workflows/approval_publishing_skeleton.json` | FnB OS V1 — Approval Publishing [SKELETON] | **HIGH RISK** | Webhook (test webhook — no activation needed) |

**Status of all 5:** not_executed_yet — awaiting Phase 22A onward.

---

## Section D — Recommended Execution Order

| Order | Workflow | Rationale |
|-------|----------|-----------|
| 1st | creative_asset_auto_skeleton | Standard risk — same risk level as content_auto (WF-01 which PASSED). Manual Trigger. No ads, no messaging, no publishing. Lowest risk starting point. |
| 2nd | ads_pack_auto_skeleton | HIGH RISK but output is non-spending planning document only. No actual ads API calls in skeleton. Must confirm NO ADS SPEND sticky and compliance_notes required. |
| 3rd | crm_followup_auto_skeleton | HIGH RISK. Messaging stubs only — no actual Zalo/Messenger/SMS calls in skeleton. Must confirm human_review_required=true and NO AUTO-SEND sticky. 2 scenarios required. |
| 4th | comment_inbox_reply_assistant | HIGH RISK. Reply stubs only — no actual comment API calls in skeleton. Escalation gate must produce draft_reply=null. 2 mandatory scenarios (standard + escalation). |
| 5th | approval_publishing_skeleton | HIGH RISK + Webhook trigger. Highest production-side-effect risk. Publish paths are all NoOp stubs but the webhook trigger and approval routing add complexity. Test last. 2 mandatory scenarios (approved + not-approved). |

**Rationale Summary:**
- Lower-risk workflows are tested first to build Owner familiarity with the manual sandbox process.
- ads_pack is tested second because it is HIGH RISK but its output is a planning document (not an actual ad spend), making the failure modes less severe.
- CRM and comment/inbox are tested mid-sequence because they involve messaging stubs — dummy data is critical and both require 2 mandatory scenarios.
- approval_publishing is tested last because it has the most complex trigger (webhook), the most branches (5-branch switch), and the highest potential for real-world side effects if any step is mishandled.

---

## Section E — Risk Level Per Workflow

| Workflow | Risk Level | Primary Risk Reason | Risk Compared to WF-01 |
|----------|------------|---------------------|------------------------|
| creative_asset_auto_skeleton | **Standard** | Brief output only. No real image generation. No platform API. | Same risk level as WF-01 (PASSED) |
| ads_pack_auto_skeleton | **HIGH RISK** | Must NOT trigger Meta Ads, TikTok Ads, or Zalo Ads APIs. compliance_notes required. | Higher — ads API risk |
| crm_followup_auto_skeleton | **HIGH RISK** | Must NOT send Zalo OA, Messenger, or SMS messages. human_review_required=true always. 2 scenarios. | Higher — messaging API risk + 2 scenarios |
| comment_inbox_reply_assistant | **HIGH RISK** | Must NOT post comment reply to any platform. Escalation path must produce draft_reply=null. 2 mandatory scenarios. | Higher — reply API risk + escalation gate |
| approval_publishing_skeleton | **HIGH RISK** | Webhook trigger. 5-branch approval switch. Must NOT trigger FB/IG/TikTok/Zalo/Google Drive publish. 2 mandatory scenarios. | Highest — webhook + 5 publish paths |

---

## Section F — Safety Constraints Per Workflow

### F.1 — creative_asset_auto_skeleton (Standard)

| Constraint | Requirement |
|-----------|-------------|
| Workflow active | MUST be inactive / active=false before and after run |
| Trigger | Manual Trigger only |
| Credentials | placeholder_or_none — DO NOT add real credentials |
| Output expected | Creative brief only — no real image file generated |
| Forbidden | Real image generation API calls; real file upload; any platform post |
| Sticky Note check | DO NOT ACTIVATE warning must be visible |
| Test payload | Phase 17 dummy payload P17-WF02-S1 |

### F.2 — ads_pack_auto_skeleton (HIGH RISK)

| Constraint | Requirement |
|-----------|-------------|
| Workflow active | MUST be inactive / active=false before and after run |
| Trigger | Manual Trigger only |
| Credentials | placeholder_or_none — DO NOT add real credentials |
| Pre-run check | NO ADS SPEND sticky note must be visible |
| Output expected | Ads pack planning document — compliance_notes must be present |
| Forbidden | Meta Ads API (/act_*/campaigns); TikTok Ads; Zalo Ads; real Ad Account ID; real Pixel ID; real budget |
| CRITICAL | If any ads API is triggered — STOP IMMEDIATELY |
| Test payload | Phase 17 dummy payload P17-WF03-S1 |

### F.3 — crm_followup_auto_skeleton (HIGH RISK)

| Constraint | Requirement |
|-----------|-------------|
| Workflow active | MUST be inactive / active=false before and after run |
| Trigger | Manual Trigger only |
| Credentials | placeholder_or_none — DO NOT add real credentials |
| Pre-run check | NO AUTO-SEND sticky note must be visible |
| Output expected | human_review_required=true in all scenarios |
| Scenarios required | 2 mandatory: Scenario 1 new lead Messenger; Scenario 2 lapsed customer Zalo |
| Forbidden | Zalo OA API; Facebook Messenger API; SMS gateway; real customer PII in output; real PSID; real Zalo ID |
| CRITICAL | If any messaging API is triggered — STOP IMMEDIATELY |
| Test payloads | Phase 17 dummy payloads P17-WF04-S1 and P17-WF04-S2 |

### F.4 — comment_inbox_reply_assistant (HIGH RISK)

| Constraint | Requirement |
|-----------|-------------|
| Workflow active | MUST be inactive / active=false before and after run |
| Trigger | Manual Trigger only |
| Credentials | placeholder_or_none — DO NOT add real credentials |
| Pre-run check | NO AUTO-REPLY sticky note must be visible |
| Scenarios required | 2 mandatory: Scenario 1 standard menu query (non-escalation — draft_reply NON-null); Scenario 2 angry complaint (escalation — draft_reply=null) |
| Output expected S1 | draft_reply is non-null; escalation_required=false; human_review_required=true |
| Output expected S2 | draft_reply=null; escalation_required=true; human_review_required=true |
| Forbidden | FB/IG/TikTok/Zalo comment reply API; draft_reply non-null on escalation scenario |
| CRITICAL | If any comment reply API is triggered — STOP IMMEDIATELY |
| Test payloads | Phase 17 dummy payloads P17-WF05-S1 and P17-WF05-S2 |

### F.5 — approval_publishing_skeleton (HIGH RISK)

| Constraint | Requirement |
|-----------|-------------|
| Workflow active | MUST NOT be activated — use test webhook only |
| Trigger | n8n test webhook (sandbox local only — NOT public internet) |
| Credentials | placeholder_or_none — DO NOT add real credentials |
| Scenarios required | 2 mandatory: Scenario 1 approved payload (TRUE branch → Switch → NoOp stubs); Scenario 2 not-approved payload (FALSE branch → block → Stop and Error) |
| Output expected S1 | All 5 publish branches are NoOp stubs — no real publish |
| Output expected S2 | Stop and Error node reached — blocked path confirmed |
| Forbidden | Facebook post API; Instagram publish; TikTok publish; Zalo content API; Google Drive file create; Meta Ads campaign; TikTok Ads; Zalo messaging; comment reply API |
| CRITICAL | If any platform publish API is triggered — STOP IMMEDIATELY |
| Test payloads | Phase 17 dummy payloads P17-WF06-S1 and P17-WF06-S2 |

---

## Section G — Required Evidence/Log Per Workflow

Each workflow requires the following per execution session:

| # | Evidence Item | Description |
|---|--------------|-------------|
| G-01 | Evidence log file | Per-workflow evidence log (new file per workflow, following pattern of `logs/phase_20a_content_auto_sandbox_evidence_log.md`) |
| G-02 | Execution status field | execution_status: pass / blocked |
| G-03 | active_status fields | active_status_before_run and active_status_after_run: inactive/active=false |
| G-04 | credentials_used field | placeholder_or_none |
| G-05 | real_customer_data_used field | no |
| G-06 | auto_post/auto_reply/ads_spend fields | all: no |
| G-07 | Node execution results table | Per-node: executed, result (green/red/skipped), key output observed |
| G-08 | Key output fields table | Workflow-specific fields per Phase 17 payload expected output |
| G-09 | Forbidden output checks | FC-01–FC-0N per workflow (ads API, messaging API, reply API, publish API — none triggered) |
| G-10 | Result summary | result_summary, happy_path_completed, forbidden_output_found, unexpected_behavior |
| G-11 | Evidence screenshots | Minimum 2 screenshots per run (canvas + output panel). Named with convention. |
| G-12 | Owner decision | owner_decision, next_action, Owner sign-off |
| G-13 | Production readiness NOT claimed | production_readiness_claimed: no |

**Screenshot Naming Convention** (per workflow):
```
evidence/phase_[XY][subphase]/[workflow_name]/YYYYMMDD_HHMM_[workflow_short]_[description]_[result].png
```
Example:
```
evidence/phase_22b/creative_asset_auto_skeleton/20260529_0200_creative_asset_manual_sandbox_pass_canvas.png
```

**Evidence Log Location Pattern:**
```
logs/phase_[XY][subphase]_[workflow_name]_sandbox_evidence_log.md
```

---

## Section H — Stop Conditions Per Workflow

The following conditions require **immediate STOP** during any manual sandbox execution:

| Stop Condition | All Workflows | Applies To |
|----------------|--------------|------------|
| SC-01 | Workflow is active (toggle shows Active/On) | All — STOP before triggering |
| SC-02 | Real credential prompt appears asking for live account credentials | All — DO NOT enter |
| SC-03 | Any node shows a real platform API call was made | All — STOP after execution |
| SC-04 | Content was posted to any platform | All — STOP |
| SC-05 | A real customer received a message | CRM, Comment/Inbox — STOP |
| SC-06 | An ad campaign was created or budget was committed | Ads Pack — STOP |
| SC-07 | A comment reply was posted to any real post | Comment/Inbox — STOP |
| SC-08 | approval_status changed to Approved or Published without Owner action | Approval/Publishing — STOP |
| SC-09 | Real PII (name, phone, email, address) appeared in output | All — STOP |
| SC-10 | n8n triggered a live webhook to the public internet | Approval/Publishing — STOP |

**After stopping:** Do NOT attempt to debug inside n8n. Record the blocker in the evidence log. Set execution_status to blocked. Report to Builder.

---

## Section I — Pass/Fail Criteria Per Workflow

### I.1 — creative_asset_auto_skeleton

**PASS requires ALL of the following:**
- [ ] Workflow remained inactive throughout
- [ ] No real credentials added
- [ ] Manual Trigger executed without error
- [ ] Node chain ran: happy path to creative brief output
- [ ] Creative brief output present (no real image file generated)
- [ ] No forbidden API calls
- [ ] evidence log fully filled
- [ ] ≥2 screenshots captured

**FAIL/BLOCKED if any of the following:**
- Any node triggered a real image generation API
- Any content was uploaded to a platform
- Workflow activated
- Real credentials entered

### I.2 — ads_pack_auto_skeleton

**PASS requires ALL of the following:**
- [ ] NO ADS SPEND sticky visible before run
- [ ] Workflow remained inactive throughout
- [ ] No real Ad Account, Pixel, or budget credentials
- [ ] Node chain ran to ads pack output
- [ ] compliance_notes field present in output
- [ ] No Meta/TikTok/Zalo Ads API calls triggered
- [ ] evidence log fully filled
- [ ] ≥2 screenshots captured

**FAIL/BLOCKED if any of the following:**
- Any ads API call detected (Meta, TikTok, Zalo)
- Real Ad Account ID, Pixel ID, or budget in output
- Workflow activated

### I.3 — crm_followup_auto_skeleton

**PASS requires ALL of the following (both scenarios):**
- [ ] NO AUTO-SEND sticky visible before run
- [ ] Workflow remained inactive throughout
- [ ] No real messaging credentials
- [ ] Scenario 1 (new lead): human_review_required=true, no messaging API triggered
- [ ] Scenario 2 (lapsed customer): human_review_required=true, no messaging API triggered
- [ ] No real customer PII in output
- [ ] evidence log fully filled for both scenarios
- [ ] ≥2 screenshots per scenario

**FAIL/BLOCKED if any of the following:**
- Zalo OA, Messenger, or SMS API triggered in either scenario
- human_review_required=false in any output
- Real customer PII in output

### I.4 — comment_inbox_reply_assistant

**PASS requires ALL of the following (both scenarios):**
- [ ] NO AUTO-REPLY sticky visible before run
- [ ] Workflow remained inactive throughout
- [ ] No real comment API credentials
- [ ] Scenario 1 (standard query): draft_reply non-null, escalation_required=false
- [ ] Scenario 2 (escalation): draft_reply=null, escalation_required=true
- [ ] No comment reply API triggered in either scenario
- [ ] evidence log fully filled for both scenarios
- [ ] ≥2 screenshots per scenario

**FAIL/BLOCKED if any of the following:**
- Comment reply API triggered in either scenario
- draft_reply non-null on Scenario 2 (escalation)
- Workflow activated

### I.5 — approval_publishing_skeleton

**PASS requires ALL of the following (both scenarios):**
- [ ] Workflow NOT activated — test webhook used only
- [ ] No real platform credentials
- [ ] Scenario 1 (approved): TRUE branch → Switch → NoOp stubs all confirmed; no real publish
- [ ] Scenario 2 (not-approved): FALSE branch → block → Stop and Error confirmed
- [ ] No publish API triggered in either scenario (FB/IG/TikTok/Zalo/Google Drive)
- [ ] No Meta Ads, TikTok Ads, Zalo messaging, comment reply API triggered
- [ ] evidence log fully filled for both scenarios
- [ ] ≥2 screenshots per scenario

**FAIL/BLOCKED if any of the following:**
- Any platform publish API triggered
- Workflow activated (not just test webhook)
- Real credentials entered

---

## Section J — Explicit Non-Goals

| Non-Goal | Detail |
|----------|--------|
| No production readiness | A PASS in any of these phases does NOT mean the workflow is ready for production use |
| No production execution | Phase 21 and all sub-phases (22A onward) are sandbox-only |
| No workflow activation | active=false must be maintained at all times |
| No real credentials | All credentials remain placeholder_or_none |
| No real customer data | All test data uses dummy/fake values from Phase 17 payloads |
| No auto-post | No content is posted to any social media platform |
| No real inbox/comment reply | No replies are posted to real comments or inbox messages |
| No ads spend | No ad campaign is created, no budget is committed, no platform ad API is called |
| No workflow logic fixes | If a workflow node fails or behaves unexpectedly, the session is BLOCKED — Builder investigates |
| No schema changes | Phase 21 does not modify any n8n workflow JSON files |
| No production instance testing | All testing occurs in sandbox/test n8n instance only |
| No Phase 22A+ execution in this phase | Phase 21 only creates the plan — execution starts in Phase 22A |

---

## Section K — Recommended Next Phase

### Phase 22A — Owner Manual Sandbox Runbook for creative_asset_auto_skeleton

| Item | Detail |
|------|--------|
| Workflow | `creative_asset_auto_skeleton` |
| Risk Level | Standard |
| Phase 22A Sub-phase | Evidence Capture Pack (mirrors Phase 20A structure) |
| Phase 22B Sub-phase | Owner Manual Sandbox Runbook (mirrors Phase 20B structure) |
| Phase 22C Sub-phase | Owner Evidence Submission (mirrors Phase 20C structure) |
| Test Payload | Phase 17 dummy payload P17-WF02-S1 |
| Entry Criteria | Phase 21 plan accepted by Owner; Phase 17 test payload file accessible; n8n sandbox accessible; workflow imported and inactive |
| Pass Criteria | creative_asset_auto_skeleton manual sandbox execution PASS with full evidence log, no forbidden output, no real data, no activation |

**Why creative_asset_auto_skeleton first:**
Same risk level (Standard) as content_auto_skeleton which PASSED. Manual Trigger. No ads, no messaging, no webhook. Builds directly on Owner's successful Phase 20B/20C experience. Lowest incremental risk.

---

## Phase Connections

| Phase | Description | Status |
|-------|-------------|--------|
| Phase 8 | n8n workflow skeleton creation | DONE (commit `ad867b3`) |
| Phase 14 | Sandbox import dry-run PASS (6/6 workflows) | DONE (commit `86099bb`) |
| Phase 16 | Sandbox runtime validation plan | DONE (commit `82a3ce3`) |
| Phase 17 | Sandbox test data + evidence pack (all 6 payloads) | DONE (commit `ac91976`) |
| Phase 19 | Owner manual sandbox execution instructions | DONE (commit `f04edba`) |
| Phase 20A | Manual sandbox evidence capture pack — content_auto | DONE (commit `f505dae`) |
| Phase 20B | Owner manual sandbox runbook — content_auto | DONE (commit `fb33e8c`) |
| Phase 20C | Owner evidence submission — content_auto — **PASS** | DONE (commit `50df2af`) |
| **Phase 21** | **Sandbox manual execution expansion plan (this phase)** | **IN PROGRESS** |
| Phase 22A | Evidence capture pack — creative_asset_auto | NEXT |
| Phase 22B | Owner manual sandbox runbook — creative_asset_auto | PLANNED |
| Phase 22C | Owner evidence submission — creative_asset_auto | PLANNED |
| Phase 23A–23C | ads_pack_auto_skeleton | PLANNED |
| Phase 24A–24C | crm_followup_auto_skeleton | PLANNED |
| Phase 25A–25C | comment_inbox_reply_assistant | PLANNED |
| Phase 26A–26C | approval_publishing_skeleton | PLANNED |

---

## Safety Confirmation

| Check | Status |
|-------|--------|
| Workflow JSON modified | NO |
| active=true introduced | NO |
| Real credentials added | NO |
| Real customer data added | NO |
| Workflow execution performed | NO |
| Auto-post executed | NO |
| Auto-reply executed | NO |
| Ads spend occurred | NO |
| Production readiness claimed | NO |
| Secret scan | CLEAN |
