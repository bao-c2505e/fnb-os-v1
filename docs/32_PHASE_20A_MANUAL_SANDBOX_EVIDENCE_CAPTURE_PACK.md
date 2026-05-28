# Phase 20A — Manual Sandbox Evidence Capture Pack

**Phase:** 20A
**Type:** Evidence / Log Capture Pack — Documentation Only
**Selected Workflow:** `content_auto_skeleton`
**Created By:** Claude Code (Builder, AGT-02) — 2026-05-29
**Status:** PACK_READY — READY FOR CODEX REVIEW

---

## A. Purpose

Phase 20A is a **documentation and evidence capture preparation pack only.**

It does **not** execute any n8n workflow.
It does **not** activate any workflow.
It does **not** add real credentials.
It does **not** claim production readiness.

Phase 20A prepares the Owner to capture evidence and fill the required log file when manually executing the `content_auto_skeleton` workflow in a sandbox n8n instance.

This pack provides:
- A pre-run safety checklist specific to `content_auto_skeleton`
- An Owner manual run checklist with node-by-node observation steps
- An evidence capture checklist
- Screenshot naming convention
- Required log file path and format
- PASS / FAIL criteria for this specific workflow run

The actual manual sandbox execution happens in **Phase 20B**.

---

## B. Selected Workflow

| Field | Value |
|-------|-------|
| Workflow file | `n8n/workflows/content_auto_skeleton.json` |
| n8n workflow name | `FnB OS V1 — Content Auto [SKELETON]` |
| Risk level | Standard |
| Trigger type | Manual Trigger (click "Test workflow" in n8n canvas) |
| Phase 17 payload | `samples/sandbox/phase_17_test_payloads/content_auto_skeleton_test_payload.md` |
| Payload scenario | P17-WF01-S1 — Standard Facebook Content Request |
| Evidence log | `logs/phase_20a_content_auto_sandbox_evidence_log.md` |

---

## C. Why This Workflow Is First

`content_auto_skeleton` is selected as the first sandbox workflow for these reasons:

| Reason | Detail |
|--------|--------|
| Standard risk (not HIGH RISK) | No ads spend, no customer messaging, no comment reply, no platform publishing via webhook |
| Manual Trigger (not Webhook) | Simplest trigger type — no webhook test setup required |
| No external platform API stubs | Output goes only to a NoOp approval queue stub — no Facebook, Messenger, Zalo, or ads API |
| Clear pass/fail signal | `logEntry.log_id` present and `approvalQueueStubReached = true` are unambiguous PASS signals |
| Approval gate intact | `approval_status` stays at `Draft` — can never be auto-set to `Approved` or `Published` |
| Node chain is linear | 6 happy-path nodes plus validation branch — straightforward to follow in n8n panel |

---

## D. Node Chain Reference

The complete node execution chain for `content_auto_skeleton`:

**Happy Path (validation passes):**

```
Manual Trigger
  → Set Input Variables
  → Code: Load Brand Brain
  → Code: AI Generate Content Draft
  → Code: Validate Required Fields
  → If: Validation Pass [TRUE branch]
      → Set: approval_status = Draft
      → Code: Write Log Entry
      → NoOp: STUB — Send to Approval Queue
```

**Validation Failure Path (if required fields missing):**

```
If: Validation Pass [FALSE branch]
  → Set: Validation Error
  → Stop and Error: Validation Failed
```

**Error Handler (unhandled runtime error):**

```
Error Trigger
  → Set: Error Log
  → Stop and Error: Workflow Error
```

In a standard dummy run the happy path is expected. The validation failure path is also acceptable — see Section H PASS/FAIL criteria.

---

## E. Pre-Run Safety Checklist

Complete all items before clicking "Test workflow". Do not proceed if any item shows NOT MET.

| ID | Check | Required State | Owner to Verify |
|----|-------|---------------|----------------|
| SR-01 | n8n instance is sandbox / localhost | URL is localhost or known sandbox — not production | [ ] |
| SR-02 | Workflow `content_auto_skeleton` is INACTIVE | Toggle shows OFF in n8n Workflows list | [ ] |
| SR-03 | Sticky Note "DO NOT ACTIVATE" is visible on canvas | Open canvas and confirm sticky note | [ ] |
| SR-04 | No real credentials configured in this workflow | All credentials show "Credential not found" | [ ] |
| SR-05 | Phase 17 payload file open | `samples/sandbox/phase_17_test_payloads/content_auto_skeleton_test_payload.md` | [ ] |
| SR-06 | Evidence log file open | `logs/phase_20a_content_auto_sandbox_evidence_log.md` | [ ] |
| SR-07 | No real customer data will be entered | Dummy payload only — no real names, phones, emails | [ ] |
| SR-08 | Not going to activate workflow during or after run | Toggle remains OFF at all times | [ ] |
| SR-09 | Not going to post output to any real platform | Output is observed in n8n panel only | [ ] |
| SR-10 | Working tree clean before run | `git status --short` returns empty | [ ] |

**Pre-Run Sign-Off:**

```
I, Bo Bao (Owner), confirm SR-01 through SR-10 are satisfied
and I am proceeding with a manual sandbox test only.

Owner: ___________________  Date: ___________________  Time: ___________________
```

---

## F. Owner Manual Run Checklist

Follow in order. Check each step as completed.

**Before triggering:**

| Step | Action | Check |
|------|--------|-------|
| F-01 | Open n8n in browser (sandbox/localhost) | [ ] |
| F-02 | Open Workflows list — confirm `FnB OS V1 — Content Auto [SKELETON]` shows Inactive | [ ] |
| F-03 | Click workflow name to open canvas | [ ] |
| F-04 | Confirm Sticky Note "DO NOT ACTIVATE / PHASE 8 SKELETON" is visible | [ ] |
| F-05 | Confirm Manual Trigger node is present at left of canvas | [ ] |
| F-06 | Fill in `execution_timestamp` in evidence log before triggering | [ ] |

**Triggering and observing:**

| Step | Action | Check |
|------|--------|-------|
| F-07 | Click "Test workflow" button (do NOT toggle active to ON) | [ ] |
| F-08 | Wait for execution to complete — observe n8n execution panel | [ ] |
| F-09 | Click `Set Input Variables` node — confirm `brand_name = "Vị Cuốn"`, `platform = "Facebook"` | [ ] |
| F-10 | Click `Code: Load Brand Brain` node — confirm `brandBrainLoaded = true` | [ ] |
| F-11 | Click `Code: AI Generate Content Draft` node — confirm `contentDraft.approval_status = "Draft"` | [ ] |
| F-12 | Click `Code: Validate Required Fields` node — confirm `validation_pass` field present | [ ] |
| F-13 | Click `If: Validation Pass` node — note which branch was taken (TRUE or FALSE) | [ ] |
| F-14 | If TRUE branch: click `Set: approval_status = Draft` — confirm `approval_status = "Draft"` | [ ] |
| F-15 | If TRUE branch: click `Code: Write Log Entry` — confirm `logEntry.log_id` starts with `"LOG-"` and `logWritten = true` | [ ] |
| F-16 | If TRUE branch: click `NoOp: STUB — Send to Approval Queue` — confirm node shows green (no output) | [ ] |
| F-17 | Confirm no red error nodes on the happy path | [ ] |

**Forbidden output checks (check each — mark BLOCKED if any appear):**

| Step | Forbidden Item | Check |
|------|---------------|-------|
| F-18 | No HTTP request to `graph.facebook.com` in execution log | [ ] |
| F-19 | No HTTP request to `api.openai.com` or `api.anthropic.com` | [ ] |
| F-20 | No HTTP request to Google Sheets or Supabase | [ ] |
| F-21 | `approval_status` is NOT `"Approved"` or `"Published"` anywhere in output | [ ] |
| F-22 | No real PII (phone number, email, customer ID) in output | [ ] |
| F-23 | Workflow toggle still shows Inactive after run | [ ] |

---

## G. Evidence Capture Checklist

After execution, before closing n8n:

| ID | Evidence Item | Required | Check |
|----|--------------|---------|-------|
| EC-01 | Screenshot of full execution panel (all nodes green/red visible) | YES | [ ] |
| EC-02 | Screenshot of `Code: Write Log Entry` node output panel | YES | [ ] |
| EC-03 | Screenshot of `NoOp: STUB — Send to Approval Queue` node (if reached) | YES | [ ] |
| EC-04 | Screenshot of `If: Validation Pass` node showing which branch taken | YES | [ ] |
| EC-05 | Copy of `logEntry` JSON from `Code: Write Log Entry` output | YES | [ ] |
| EC-06 | Note the n8n Execution ID (shown in execution panel or history) | YES | [ ] |
| EC-07 | Note all nodes that executed (list from n8n panel) | YES | [ ] |
| EC-08 | Fill all fields in `logs/phase_20a_content_auto_sandbox_evidence_log.md` | YES | [ ] |

Screenshots that are not linked to the log file do not count as evidence. Every screenshot file must be referenced by filename in `evidence_screenshot_files` field of the log.

---

## H. Required Screenshot Naming Convention

Save all screenshots with this format:

```
phase20b_content_auto_[node_short_name]_[PASS_or_BLOCKED]_[YYYYMMDD].png
```

Examples:

| Screenshot | Filename |
|-----------|---------|
| Full execution panel | `phase20b_content_auto_execution_panel_PASS_20260529.png` |
| Code: Write Log Entry output | `phase20b_content_auto_write_log_entry_PASS_20260529.png` |
| NoOp approval queue | `phase20b_content_auto_noop_approval_queue_PASS_20260529.png` |
| If: Validation Pass branch | `phase20b_content_auto_if_validation_pass_PASS_20260529.png` |

Store screenshots locally. Include all filenames in the `evidence_screenshot_files` field of the evidence log.

---

## I. Required Log File

**Path:** `logs/phase_20a_content_auto_sandbox_evidence_log.md`

This file is created in Phase 20A (current phase) as a blank template.
Owner fills it during Phase 20B execution.
The filled log file must be committed after Phase 20B.

See [logs/phase_20a_content_auto_sandbox_evidence_log.md](../logs/phase_20a_content_auto_sandbox_evidence_log.md) for the template.

---

## J. Required Payload Reference

**Payload file:** `samples/sandbox/phase_17_test_payloads/content_auto_skeleton_test_payload.md`
**Payload scenario:** P17-WF01-S1 — Standard Facebook Content Request
**Input values (pre-set in workflow Set node — do not modify):**

```json
{
  "brand_id": "VQ",
  "brand_name": "Vị Cuốn",
  "content_request": "REPLACE_WITH_OWNER_CONTENT_REQUEST",
  "platform": "Facebook",
  "objective": "Awareness",
  "target_audience": "REPLACE_WITH_TARGET_AUDIENCE",
  "offer": "[OWNER_TO_PROVIDE_OFFER]"
}
```

These values are pre-set in the `Set Input Variables` node. Owner does **not** need to modify the workflow or enter any data. Simply trigger the workflow and observe.

The `REPLACE_WITH_*` strings are expected placeholders — not errors or failures.

---

## K. PASS / FAIL Criteria

### PASS (all must be true)

| Criterion | Required Value |
|-----------|---------------|
| All happy-path nodes executed without red error | YES |
| `brandBrainLoaded` in output | `true` |
| `contentDraft.approval_status` in output | `"Draft"` |
| `validation_pass` field present in output | Any boolean value |
| `logEntry.log_id` starts with `"LOG-"` | YES |
| `logWritten` in output | `true` |
| `approvalQueueStubReached` in output | `true` |
| No forbidden output observed (F-18 through F-22) | NONE |
| Workflow still INACTIVE after run | YES |
| Evidence log filled and screenshots named | YES |

**Note:** If the FALSE branch of `If: Validation Pass` is taken (validation fails), the run is still considered PASS provided:
- No forbidden output is present
- Workflow is still INACTIVE
- `Set: Validation Error` and `Stop and Error: Validation Failed` nodes are the only terminal nodes
- Evidence is captured and logged

### BLOCKED (any one triggers BLOCKED)

| Trigger | Action |
|---------|--------|
| Any HTTP call to a real external API | STOP — record BLOCKED, do not re-run |
| `approval_status` set to `"Approved"` or `"Published"` | STOP — record BLOCKED |
| Any real customer PII in output | STOP — record BLOCKED |
| Workflow toggled to ACTIVE during run | STOP — record BLOCKED, do not activate |
| n8n instance is production (not sandbox) | STOP — record BLOCKED |
| Real credential entered during session | STOP — record BLOCKED |

If BLOCKED: do not attempt to fix the workflow inside n8n. Record the exact error and node output. Report to Builder. A future Builder phase will address the fix.

---

## L. Explicit Non-Goals

Phase 20A and Phase 20B explicitly do NOT accomplish the following:

| Non-Goal | Status |
|----------|--------|
| Production execution | OUT OF SCOPE |
| Auto-post to Facebook, Instagram, TikTok, Zalo | OUT OF SCOPE |
| Auto-reply to any customer | OUT OF SCOPE |
| Ads spend (Meta Ads, TikTok Ads, Zalo Ads) | OUT OF SCOPE |
| Real credentials (API keys, tokens, passwords) | OUT OF SCOPE |
| Real customer data (names, phones, emails, IDs) | OUT OF SCOPE |
| Workflow activation (`active: true`) | OUT OF SCOPE |
| Production readiness claim | OUT OF SCOPE |
| Workflow code fixes inside n8n | OUT OF SCOPE |
| Testing other workflows (WF-02 through WF-06) | OUT OF SCOPE — future phases |
| Schema validation of node outputs | OUT OF SCOPE |

---

## M. Next Phase Recommendation

**Phase 20B — Owner Manual Sandbox Execution for content_auto_skeleton**

**Scope:**
Owner manually executes `content_auto_skeleton` using the Phase 17 dummy payload (P17-WF01-S1).
Owner fills `logs/phase_20a_content_auto_sandbox_evidence_log.md` during/after execution.
Owner captures all required screenshots per Section H naming convention.
Owner does not fix workflow code — observes and records only.

**Entry criteria for Phase 20B:**
- Phase 20A Codex PASS
- Phase 20A Owner OWNER_APPROVED
- SR-01 through SR-10 satisfied (Section E pre-run checklist)
- `logs/phase_20a_content_auto_sandbox_evidence_log.md` template confirmed present

**Phase 20B success criteria:**
- All items in Section F (Owner manual run checklist) checked
- All items in Section G (evidence capture checklist) checked
- `logs/phase_20a_content_auto_sandbox_evidence_log.md` filled with actual execution results
- `execution_status` updated from `not_executed_yet` to `PASS` or `BLOCKED`
- `owner_decision` field filled
- Log file committed to repo

---

## Phase Connections

| Phase | Title | Relationship |
|-------|-------|-------------|
| Phase 8 | n8n Importable Workflow Skeletons | Source of `content_auto_skeleton.json` |
| Phase 14 | Owner n8n Sandbox Dry-Run | Confirmed: workflow imported, inactive |
| Phase 16 | Sandbox Runtime Validation Plan | Safety rules and stop conditions referenced |
| Phase 17 | Sandbox Test Data + Evidence Pack | Source of P17-WF01-S1 dummy payload |
| Phase 19 | Owner Manual Sandbox Execution Instructions | General sandbox execution guide |
| Phase 20A | Manual Sandbox Evidence Capture Pack | **This document** — specific to `content_auto_skeleton` |
| Phase 20B | Owner Manual Sandbox Execution for content_auto_skeleton | Next: Owner executes and records evidence |

---

## Safety Confirmation

| Check | Status |
|-------|--------|
| n8n workflow JSON modified in Phase 20A | NO — untouched |
| `active: true` introduced in Phase 20A | NO |
| Real credentials added in Phase 20A | NO |
| Real customer data used in Phase 20A | NO |
| Workflow executed in Phase 20A | NO |
| Auto-post / auto-reply / ads in Phase 20A | NO |
| Production readiness claimed in Phase 20A | NO |
| Secret scan (API keys, tokens, passwords, private keys) | CLEAN |
