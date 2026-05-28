# Phase 17 — Sandbox Test Data + Evidence Pack — Activity Log

**Project:** FnB OS V1 / Vị Cuốn Growth OS
**Phase:** 17
**Created By:** Claude Code (Builder, AGT-02)
**Date:** 2026-05-29
**Status:** PACK_CREATED — AWAITING CODEX REVIEW + OWNER APPROVAL

---

## Session Details

| Field | Value |
|-------|-------|
| Date | 2026-05-29 |
| Builder | Claude Code (AGT-02) |
| Phase | 17 — Sandbox Test Data + Evidence Pack |
| Session type | Document/pack creation only — no n8n execution |
| n8n accessed | NO |
| Workflow executed | NO |
| Workflow activated | NO |
| Real credentials added | NO |
| Real customer data used | NO |
| Phase 8 JSON modified | NO — untouched at commit `ad867b3` |
| Auto-post / auto-reply / ads | NO |
| Commit | NO — awaiting Codex review + Owner OWNER_APPROVED |
| Push | NO — awaiting Codex review + Owner OWNER_APPROVED |

---

## Phase Objective

Phase 16 created the runtime validation plan and per-workflow checklists. Phase 17 creates the **ready-to-use test materials** so Owner can execute that plan without guessing test data, without risk of using real customer information, and with a structured evidence record for each workflow test. Phase 17 deliverables: dummy test payloads for all 6 workflows, an evidence collection template, and this activity log.

---

## Files Created

| File | Type | Purpose |
|------|------|---------|
| `docs/PHASE_17_SANDBOX_TEST_DATA_EVIDENCE_PACK.md` | Pack overview doc | Purpose, scope, safety rules, how pack relates to Phase 16, test data structure, evidence collection rules, PASS/BLOCKED criteria, next phase recommendation |
| `samples/sandbox/phase_17_test_payloads/content_auto_skeleton_test_payload.md` | Test payload | WF-01: dummy input values, expected safe output, forbidden output, log expectation, PASS/BLOCK criteria |
| `samples/sandbox/phase_17_test_payloads/creative_asset_auto_skeleton_test_payload.md` | Test payload | WF-02: dummy input values, expected safe output, forbidden output (no real image generation), PASS/BLOCK criteria |
| `samples/sandbox/phase_17_test_payloads/ads_pack_auto_skeleton_test_payload.md` | Test payload | WF-03 HIGH RISK: dummy input, pre-test safety checklist, no-ads-spend check, compliance_notes requirement, CRITICAL forbidden output table, PASS/BLOCK criteria |
| `samples/sandbox/phase_17_test_payloads/crm_followup_auto_skeleton_test_payload.md` | Test payload | WF-04 HIGH RISK: dummy input (fake customer names/IDs), no-auto-send check, human_review_required=true verification, CRITICAL forbidden output, 2 test scenarios (new lead + lapsed customer) |
| `samples/sandbox/phase_17_test_payloads/comment_inbox_reply_assistant_skeleton_test_payload.md` | Test payload | WF-05 HIGH RISK: 2 mandatory scenarios — Scenario 1 (standard menu query, non-escalation) + Scenario 2 (angry/complaint, escalation → draft_reply=null), CRITICAL forbidden output, both scenarios required for PASS |
| `samples/sandbox/phase_17_test_payloads/approval_publishing_skeleton_test_payload.md` | Test payload | WF-06 HIGH RISK: webhook trigger instructions, Scenario 1 (approved payload → TRUE path → NoOp stub → approval log), Scenario 2 (not-approved → FALSE path → block log → Stop and Error), S3–S6 additional item_type routing tests, CRITICAL forbidden output (all 5 platform/ads/messaging/reply publish paths), both S1+S2 required for PASS |
| `logs/templates/SANDBOX_EXECUTION_EVIDENCE_TEMPLATE.md` | Evidence template | 9-section reusable template: Section 1 session identity; Section 2 workflow under test; Section 3 pre-test confirmation (with WF-03/04/05/06 extra checks); Section 4 test execution (trigger method, per-node result table, key output fields observed); Section 5 post-execution safety checks; Section 6 issues/anomalies; Section 7 evidence references; Section 8 PASS/BLOCKED verdict; Section 9 Owner sign-off |
| `logs/PHASE_17_SANDBOX_TEST_DATA_EVIDENCE_PACK_LOG.md` | Activity log | This file |

---

## Files Updated

| File | Change |
|------|--------|
| `handoff/CURRENT_PHASE.md` | Updated to Phase 17 — Sandbox Test Data + Evidence Pack |
| `logs/AGENT_ACTIVITY_LOG.md` | New Phase 17 row prepended |
| `handoff/SESSION_SUMMARY.md` | Phase 17 session summary added |
| `09_LOGS/PHASE_LOG.md` | Phase 17 entry prepended |

---

## Files NOT Modified

| File | Status |
|------|--------|
| `n8n/workflows/content_auto_skeleton.json` | UNTOUCHED — unchanged since commit `ad867b3` |
| `n8n/workflows/creative_asset_auto_skeleton.json` | UNTOUCHED — unchanged since commit `ad867b3` |
| `n8n/workflows/ads_pack_auto_skeleton.json` | UNTOUCHED — unchanged since commit `ad867b3` |
| `n8n/workflows/crm_followup_auto_skeleton.json` | UNTOUCHED — unchanged since commit `ad867b3` |
| `n8n/workflows/comment_inbox_reply_assistant_skeleton.json` | UNTOUCHED — unchanged since commit `ad867b3` |
| `n8n/workflows/approval_publishing_skeleton.json` | UNTOUCHED — unchanged since commit `ad867b3` |

---

## Dummy Data Policy Compliance

All test payloads use only fake/dummy data. Verification:

| Policy Item | Status |
|-------------|--------|
| No real customer names | CONFIRMED — used `Nguyen Test A`, `Tran Sandbox B` format only |
| No real phone numbers | CONFIRMED — used `0900000000`, `0911111111` format only |
| No real emails | CONFIRMED — used `sandbox@example.com` format only |
| No real Facebook Page IDs | CONFIRMED — used `TEST_PAGE_ID_000001` format only |
| No real Facebook User IDs / PSIDs | CONFIRMED — used `TEST_FBUID_000001` format only |
| No real Zalo User IDs | CONFIRMED — used `TEST_ZALOID_000001` format only |
| No real Ad Account IDs | CONFIRMED — used `ACT-TEST-000001` format only |
| No real comment IDs | CONFIRMED — used `TEST_CMT_ID_000001` format only |
| No real API keys / access tokens | CONFIRMED — no credentials in any payload |
| No real social comment text from real customers | CONFIRMED — all messages are fictional sandbox examples |
| Fake customer reference values labeled "docs only" | CONFIRMED — all fake reference values marked "for documentation purposes only — do NOT enter in n8n" |

---

## Safety Confirmations

| Check | Result |
|-------|--------|
| No n8n execution performed | CONFIRMED — test payloads and templates are documents only |
| No workflow activated | CONFIRMED — all 6 remain `active: false` as committed |
| No real credentials added | CONFIRMED — no API keys, tokens, passwords, or credentials in any file |
| No real customer data used | CONFIRMED — all customer-like data is explicitly fake |
| No content posted | CONFIRMED — no social media post, no message sent, no ad campaign |
| No auto-post, auto-reply, or ads | CONFIRMED — explicitly prohibited in all 6 payload files |
| No production readiness claim | CONFIRMED — all files state sandbox-only, plan/template only |
| Phase 8 workflow JSON untouched | CONFIRMED — Builder read workflow JSONs as reference only; no write operations |
| No secrets in any created file | CONFIRMED — see secret scan below |
| Scope boundaries observed | CONFIRMED — 8 new files created + 4 state files updated, no extra scope |

---

## Secret Scan Summary

Patterns scanned across all 8 new files:
`sk-ant-`, `sk-[a-zA-Z0-9]{20,}`, `private_key`, `ghp_[a-zA-Z0-9]+`, `eyJ[a-zA-Z0-9]+\.[a-zA-Z0-9]`, Telegram bot token pattern (`[0-9]{9,10}:[a-zA-Z0-9_-]{35}`), `"client_secret"`, `access_token`, `api_key`, `password`

Result: **CLEAN — no real credentials found in any created file.**

Note: Fake reference values like `ACT-TEST-000001`, `TEST_PAGE_ID_000001`, `sandbox@example.com` are clearly dummy identifiers — not real credentials.

---

## Test Payload Summary

| Payload ID | Workflow | Scenarios | Risk | Critical Checks |
|------------|----------|-----------|------|----------------|
| P17-WF01 | content_auto_skeleton | 1 | Standard | No real AI/platform API calls |
| P17-WF02 | creative_asset_auto_skeleton | 1 | Standard | No real image generation/upload |
| P17-WF03 | ads_pack_auto_skeleton | 1 | **HIGH** | No Meta/TikTok/Zalo Ads API; compliance_notes required |
| P17-WF04 | crm_followup_auto_skeleton | 2 | **HIGH** | No Zalo/Messenger/SMS API; human_review_required=true |
| P17-WF05 | comment_inbox_reply_assistant_skeleton | 2 (both required) | **HIGH** | Non-escalation path + escalation path; draft_reply=null for escalation |
| P17-WF06 | approval_publishing_skeleton | 2 required + 4 optional | **HIGH** | Approved path + not-approved path; all 5 NoOp stubs confirmed; no platform/ads/messaging/reply API |

---

## Next Recommended Phase

**Phase 18: Sandbox Execution Result Recording**

After Codex PASS and Owner OWNER_APPROVED on Phase 17:

1. Owner opens Phase 16 plan + Phase 17 test payload files as session guides.
2. Owner confirms all Phase 16 preconditions (PC-01 through PC-12).
3. Owner executes each workflow using Phase 17 dummy payloads.
4. Owner fills one `SANDBOX_EXECUTION_EVIDENCE_TEMPLATE.md` copy per workflow.
5. Owner reports results to Builder.
6. Builder (Phase 18) records the execution result in a structured log.
7. Codex reviews Phase 18 log.
8. Owner approves Phase 18 commit.

Phase 18 will be structured similarly to Phase 14 (execution record) — the canonical "did it run and what was the result" record for the sandbox runtime validation.

---

*End of Phase 17 Activity Log*
*Pack created. No execution performed. Awaiting Codex PASS + Owner OWNER_APPROVED.*
