# Phase 17 — Sandbox Test Data + Evidence Pack

**Project:** FnB OS V1 / Vị Cuốn Growth OS
**Phase:** 17
**Created By:** Claude Code (Builder, AGT-02)
**Date:** 2026-05-29
**Status:** PACK CREATED — AWAITING CODEX REVIEW + OWNER APPROVAL BEFORE EXECUTION
**Prior Phase:** Phase 16 — Sandbox Runtime Validation Plan (commit `82a3ce3`)

---

## ⚠️ Critical Safety Notice

This document and all files in `samples/sandbox/phase_17_test_payloads/` are **reference materials only**.
No execution may occur until:

1. Codex (AGT-03) has reviewed this pack and issued PASS.
2. Owner (Bo Bao) has approved execution.
3. All preconditions in Phase 16 Section 5 are satisfied.
4. No real credentials are present in any workflow.
5. No workflow is activated (`active: false` on all 6).

**All test payloads in this pack contain dummy/fake data only. No real customer data.**

---

## Table of Contents

1. Purpose
2. Scope
3. Out of Scope
4. Safety Rules
5. How This Pack Relates to Phase 16
6. Test Data Structure
7. Evidence Collection Rules
8. Owner Manual Execution Rules
9. PASS / BLOCKED Criteria
10. Next Phase Recommendation
11. Phase Connections

---

## 1. Purpose

Phase 16 created the runtime validation *plan* and per-workflow check checklists.
Phase 17 provides the **ready-to-use test materials** Owner needs to actually execute that plan:

- Pre-written dummy test payloads for all 6 workflows, so Owner does not need to invent test data on the spot.
- Clear expected output for each payload, so Owner knows what a correct result looks like.
- Explicit forbidden output for each payload, so Owner knows what a dangerous or wrong result looks like.
- An evidence collection template so Owner can record what they observed in n8n and sign off on the result.

**Goal:** Remove all ambiguity from the sandbox execution session. Owner opens the test payload file, reads the dummy data, inputs it into n8n, observes the result, and fills in the evidence template. No guesswork. No real customer data risk.

---

## 2. Scope

| Item | In Scope |
|------|----------|
| Dummy test payloads for all 6 Phase 8 workflow skeletons | YES |
| Expected safe output per workflow | YES |
| Forbidden/dangerous output definition per workflow | YES |
| Evidence collection template for recording test results | YES |
| Approval gate test scenarios (approved + not-approved paths for WF-06) | YES |
| Escalation path test for WF-05 (comment inbox) | YES |
| Log output expectations per workflow | YES |
| PASS/BLOCKED criteria per workflow | YES |

---

## 3. Out of Scope

| Out of Scope | Reason |
|-------------|--------|
| Real customer names, phone numbers, emails, or social IDs | Dummy data only — real PII is never acceptable in Phase 17 |
| Real Facebook/TikTok/Zalo Page IDs or Ad Account IDs | Dummy IDs only |
| Real API keys, access tokens, or credentials | No credentials in this pack |
| Actual execution of any workflow | This pack is reference material only |
| Activation of any workflow | active=false must remain at all times |
| Posting content to any real platform | No auto-post in any scenario |
| Sending messages to real customers | No real customer contact |
| Committing any ad campaign or budget | No real ads spend |
| Production n8n instance | Sandbox/test instance only |
| Replacing REPLACE_WITH_* placeholders | Placeholder policy from Phase 16 Section 8 applies |
| Claiming production readiness | Sandbox PASS ≠ production readiness |

---

## 4. Safety Rules

All Phase 16 safety rules (SR-01 through SR-12) apply to Phase 17.

Additional Phase 17 rules:

| Rule | Detail |
|------|--------|
| P17-SR-01 | All test payloads use fake/dummy data only. No real personal data, account IDs, or credentials at any point. |
| P17-SR-02 | Test payloads must not be submitted to any live platform endpoint. They are for n8n sandbox local testing only. |
| P17-SR-03 | Evidence template must be filled with n8n execution panel observations only — not fabricated results. |
| P17-SR-04 | If the evidence template cannot be filled with real observed output, mark the workflow as BLOCKED/NOT_RUN. |
| P17-SR-05 | Owner must not modify test payloads to include real customer data or real credentials at any point. |

---

## 5. How This Pack Relates to Phase 16

| Phase 16 Item | Phase 17 Provision |
|---------------|--------------------|
| Section 6 — Per-workflow checklists with check IDs | Test payloads align with the same WF-01 through WF-06 IDs |
| Section 7 — Dummy test data policy | Phase 17 payloads are the concrete implementation of that policy |
| Section 9 — Expected logs | Phase 17 payloads define expected log fields for each workflow |
| Section 10 — Owner approval gate | Phase 17 adds an evidence template with Owner sign-off |
| Section 12 — PASS/BLOCKED criteria | Phase 17 test payloads include per-workflow PASS/BLOCKED criteria |

Phase 17 does not replace Phase 16. Both documents must be open during sandbox execution:
- Phase 16 plan: provides the checklist and safety rules for each step.
- Phase 17 payloads: provides the actual test data and expected results for each step.
- Phase 17 evidence template: provides the form Owner fills in to record what happened.

---

## 6. Test Data Structure

Each test payload file in `samples/sandbox/phase_17_test_payloads/` follows this structure:

```
# [Workflow Name] — Phase 17 Test Payload

## Workflow Identity
- Workflow file name
- n8n workflow name
- Trigger type
- Risk level

## Test Scenario(s)
One or more test scenarios. Each scenario includes:
  ### Scenario ID and Name
  - Input fields (ready-to-use dummy JSON)
  - How to enter in n8n
  - Expected safe output
  - Forbidden output (what must NOT appear)
  - Approval gate expectation
  - Log expectation
  - PASS condition
  - BLOCK condition

## Forbidden Data (hard list)
## Safety Reminders
```

---

## 7. Evidence Collection Rules

All evidence from sandbox execution must be collected in `logs/templates/SANDBOX_EXECUTION_EVIDENCE_TEMPLATE.md`.

| Rule | Detail |
|------|--------|
| One evidence record per workflow per execution session | Do not combine multiple workflows in one record |
| Fill in actual n8n execution panel output | Do not paraphrase or summarize — record exact field names and values observed |
| Screenshot reference required | Note the filename or location of any screenshot taken (not required to be stored in repo) |
| Date and time must be filled | Use ISO format: `YYYY-MM-DD HH:MM` (local time) |
| Owner sign-off required | Owner must initial or sign the evidence record before it can be used as a PASS record |
| BLOCKED must be explained | If result is BLOCKED, describe the stop condition triggered and what was observed |
| No fabrication | If a node did not execute, record it as "DID NOT RUN" — never infer or guess the output |

---

## 8. Owner Manual Execution Rules

These rules apply when Owner is running the sandbox execution session:

| Rule | Detail |
|------|--------|
| Use test payloads as-is | Do not modify dummy test data to include real customer data or real credentials |
| Follow Phase 16 checklist alongside Phase 17 payloads | Both documents must be open |
| One workflow at a time | Complete one workflow's full test scenario before moving to the next |
| Fill evidence template immediately | Fill in the evidence template after each workflow, not after all workflows |
| Stop on BLOCK condition | If any CRITICAL check fails (see Phase 16 Section 6), stop immediately per Phase 16 Section 11 |
| Do not activate to test | Use n8n's "Test workflow" / Manual Trigger mode — do not activate the workflow |
| WF-06 special rule | WF-06 uses Webhook trigger — use n8n's test webhook URL (sandbox local only, not public internet) |
| No real credential entry | If n8n shows "Credential not found" warnings, leave them as-is — do not enter real credentials to resolve |

---

## 9. PASS / BLOCKED Criteria

### Phase 17 PASS criteria

All of the following must be true:

- [ ] All 6 test payloads used (one per workflow).
- [ ] All Phase 16 Section 6 checks completed for each workflow.
- [ ] All CRITICAL checks for WF-03/04/05/06 confirmed.
- [ ] Evidence template filled for all 6 workflows.
- [ ] Owner sign-off on all 6 evidence records.
- [ ] No real credentials added at any point.
- [ ] No workflow activated at any point.
- [ ] No real external API called at any point.
- [ ] No real content posted, message sent, or ad spent.

### Phase 17 BLOCKED criteria

Any of the following makes Phase 17 BLOCKED:

- Any Phase 16 STOP condition triggered.
- Any CRITICAL check failed for WF-03/04/05/06.
- Evidence template not filled (cannot be completed from n8n execution panel).
- Any real credential added or real API call observed.
- Any workflow activated.

---

## 10. Next Phase Recommendation

After Phase 17 PASS:

**Recommended Phase 18: Sandbox Execution Result Recording**

Phase 18 would be analogous to Phase 14 — the phase where Owner reports the actual execution result, Builder records it, Codex reviews it, and Owner approves commit.

Phase 17 provides the test data. Phase 18 would record the actual execution outcome in a structured log (similar to `logs/N8N_SANDBOX_IMPORT_DRY_RUN_EXECUTION_PHASE_14.md`).

---

## 11. Phase Connections

| Phase | Description | Relationship |
|-------|-------------|-------------|
| Phase 8 | n8n Importable Workflow Skeletons (`ad867b3`) | Source of 6 workflow JSON files |
| Phase 14 | Owner n8n Sandbox Dry-Run Execution Log (PASS, `86099bb`) | Confirmed 6/6 workflows imported, all inactive |
| Phase 15 | Codex Review Gate (PASS) | Validated Phase 14 result |
| Phase 16 | Sandbox Runtime Validation Plan (`82a3ce3`) | Provides per-workflow checklists and safety rules |
| **Phase 17** | **This document — Test Data + Evidence Pack** | **Dummy payloads + evidence template for sandbox execution** |
| Phase 18 (future) | Sandbox Execution Result Recording | Records actual execution outcome |

---

*End of Phase 17 — Sandbox Test Data + Evidence Pack*
*Pack created. No execution performed. Awaiting Codex PASS + Owner OWNER_APPROVED.*
