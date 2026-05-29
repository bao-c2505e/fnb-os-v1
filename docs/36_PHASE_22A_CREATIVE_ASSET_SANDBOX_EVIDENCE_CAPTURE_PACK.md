# Phase 22A — Owner Manual Sandbox Evidence Capture Pack
# creative_asset_auto_skeleton

**Phase:** 22A
**Type:** Evidence / Log Capture Pack — Documentation Only
**Selected Workflow:** `creative_asset_auto_skeleton`
**Created By:** Claude Code (Builder, AGT-02) — 2026-05-29
**Status:** PACK_READY — READY FOR CODEX REVIEW

---

## A. Purpose

Phase 22A is a **documentation and evidence capture preparation pack only.**

It does **not** execute any n8n workflow.
It does **not** activate any workflow.
It does **not** add real credentials.
It does **not** claim production readiness.

Phase 22A prepares the Owner to capture evidence and fill the required log file when manually executing the `creative_asset_auto_skeleton` workflow in a sandbox n8n instance.

This pack provides:
- A pre-run safety checklist specific to `creative_asset_auto_skeleton`
- An Owner manual run checklist with node-by-node observation steps
- An evidence capture checklist
- Screenshot naming convention
- Required log file path and format
- PASS / FAIL criteria for this specific workflow run

The actual manual sandbox execution happens in **Phase 22B**.

---

## B. Selected Workflow

| Field | Value |
|-------|-------|
| Workflow file | `n8n/workflows/creative_asset_auto_skeleton.json` |
| n8n workflow name | `FnB OS V1 — Creative Asset Auto [SKELETON]` |
| Risk level | Standard |
| Trigger type | Manual Trigger (click "Test workflow" in n8n canvas) |
| Phase 17 payload | `samples/sandbox/phase_17_test_payloads/creative_asset_auto_skeleton_test_payload.md` |
| Payload scenario | P17-WF02-S1 — Facebook Image Creative Brief |
| Evidence log | `logs/phase_22a_creative_asset_sandbox_evidence_log.md` |

---

## C. Phase 20C PASS Reference

Phase 22A follows **Phase 20C (PASS)** for `content_auto_skeleton`.

| Item | Detail |
|------|--------|
| Previous workflow | `content_auto_skeleton` |
| Phase 20C result | **PASS** |
| Phase 20C commit | `50df2af` |
| Codex verdict | PASS |
| Operator | Bo Bao |
| Execution date | 2026-05-29 ~01:25 |
| Nodes green | 9 happy-path nodes all green |
| Forbidden output | All FC-01–FC-06: NO |
| Workflow status | Remained INACTIVE throughout |
| Output behavior | REPLACE_WITH_* placeholders confirmed — dummy/sandbox behavior correct |

Phase 20C demonstrates the Owner can safely execute a Standard-risk, Manual Trigger workflow in sandbox. Phase 22A applies the same pattern to `creative_asset_auto_skeleton`.

---

## D. Why creative_asset_auto_skeleton Is Next

`creative_asset_auto_skeleton` is selected as the second sandbox workflow for these reasons:

| Reason | Detail |
|--------|--------|
| Standard risk (not HIGH RISK) | No ads spend, no customer messaging, no comment reply, no platform publishing via webhook |
| Manual Trigger (not Webhook) | Same trigger type as content_auto_skeleton — Owner already familiar |
| No real asset generation | Output is a creative brief object only — no real image, video, or binary file |
| No image generation API | No DALL-E, Midjourney, Stable Diffusion, or equivalent node in skeleton |
| No cloud storage upload | No Google Drive, S3, or file upload node in skeleton |
| Clear pass/fail signal | `logEntry.log_id` present and `approvalQueueStubReached = true` are unambiguous PASS signals |
| Approval gate intact | `approval_status` stays at `Draft` — cannot be auto-set to `Approved` or `Published` |
| Parallel structure to content_auto | Same node chain pattern — Owner skill transfers directly |
| Pattern: Standard before HIGH RISK | Four remaining workflows are HIGH RISK; Standard must be completed first |

---

## E. Node Chain Reference

The expected node execution chain for `creative_asset_auto_skeleton`:

### Happy Path (PASS branch)

| Step | Node Name | Expected Result |
|------|-----------|-----------------|
| 1 | Manual Trigger | Triggered — green |
| 2 | Set Input Variables | Input fields set (brand_id, asset_type, platform, etc.) — green |
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

### Error Handler Path

| Step | Node Name | Expected Result |
|------|-----------|-----------------|
| — | Error Trigger | Fires if any node throws an unhandled error |
| — | Set: Error Log | Error fields captured |
| — | Stop and Error: Workflow Error | Workflow stops — not a forbidden output |

> Note: REPLACE_WITH_* placeholder values in node output are **expected stub behavior** — they confirm dummy/sandbox mode is active. They are not failures.

---

## F. Pre-Run Safety Checklist

Owner must confirm ALL items before triggering the workflow.

| ID | Check | Required State | Owner Confirm |
|----|-------|---------------|---------------|
| SR-01 | n8n instance is a sandbox / local test instance | Confirmed sandbox — NOT production | ☐ |
| SR-02 | `creative_asset_auto_skeleton` workflow is INACTIVE | Active toggle = OFF | ☐ |
| SR-03 | Sticky note "DO NOT ACTIVATE" is visible on canvas | Note visible | ☐ |
| SR-04 | No real credentials have been added to this workflow | Credential fields empty or "Credential not found" warnings | ☐ |
| SR-05 | Phase 17 test payload file is open | `samples/sandbox/phase_17_test_payloads/creative_asset_auto_skeleton_test_payload.md` open | ☐ |
| SR-06 | Evidence log file is open and ready to fill | `logs/phase_22a_creative_asset_sandbox_evidence_log.md` open | ☐ |
| SR-07 | Evidence folder exists | `evidence/phase_22b/creative_asset_auto_skeleton/` present | ☐ |
| SR-08 | No real customer data will be entered | All inputs use dummy/placeholder values only | ☐ |
| SR-09 | Workflow will NOT be activated before or after execution | Active toggle remains OFF throughout | ☐ |
| SR-10 | Git working tree is clean | `git status` shows clean | ☐ |

**Owner Pre-Run Sign-Off**

```
I confirm SR-01 through SR-10 are all satisfied.
I understand this is a sandbox-only manual execution.
I will not activate the workflow, add real credentials, or use real customer data.

Operator: ___________________________
Date/Time: ___________________________
```

---

## G. Owner Manual Run Checklist

### Before Triggering (F-01 to F-07)

| ID | Action | Check |
|----|--------|-------|
| F-01 | Open n8n sandbox instance | Instance URL is sandbox / local — not production | ☐ |
| F-02 | Open `FnB OS V1 — Creative Asset Auto [SKELETON]` | Workflow canvas visible | ☐ |
| F-03 | Confirm Active toggle is OFF | Active toggle = OFF. **STOP if active = ON.** | ☐ |
| F-04 | Confirm "DO NOT ACTIVATE" sticky note is visible | Sticky note present on canvas | ☐ |
| F-05 | Do NOT add real credentials | Accept "Credential not found" warnings — do not resolve them | ☐ |
| F-06 | Do NOT activate the workflow | Active toggle must stay OFF for entire session | ☐ |
| F-07 | Locate Manual Trigger node | "Test workflow" button visible — input pre-set in Set Input Variables | ☐ |

### Triggering and Observing (F-08 to F-20)

| ID | Action | Expected | Check |
|----|--------|----------|-------|
| F-08 | Confirm payload scenario P17-WF02-S1 | Input values visible in Set Input Variables node (no manual edit needed) | ☐ |
| F-09 | Click "Test workflow" — run ONCE only | Execution begins | ☐ |
| F-10 | Node: Manual Trigger | Green — execution started | ☐ |
| F-11 | Node: Set Input Variables | Green — `brand_id`, `asset_type`, `platform`, `content_angle` set | ☐ |
| F-12 | Node: Code: Load Brand Brain | Green — `brandBrainLoaded = true` | ☐ |
| F-13 | Node: Code: AI Generate Creative Brief | Green — `contentDraftGenerated = true`, `draft_brief` non-null | ☐ |
| F-14 | Node: Code: Validate Required Fields | Green — validation runs | ☐ |
| F-15 | Node: If: Validation Pass | Green — TRUE branch (happy path) OR FALSE branch (acceptable) | ☐ |
| F-16 | If TRUE branch: Set: approval_status = Draft | Green — `approval_status = "Draft"` | ☐ |
| F-17 | Node: Code: Write Log Entry | Green — `logWritten = true`, `logEntry.log_id` starts with "LOG-" | ☐ |
| F-18 | Node: NoOp: STUB — Send to Approval Queue | Green — `approvalQueueStubReached = true` — terminal node reached | ☐ |
| F-19 | Check `approval_status` in final output | Must be `"Draft"` only. **STOP if "Approved" or "Published"** | ☐ |
| F-20 | Check output for any binary file, image URL, or asset data | **STOP if any real image file, binary output, or cloud storage URL observed** | ☐ |

### Forbidden Output Checks (F-21 to F-26)

| ID | Forbidden Output | Action if Found |
|----|-----------------|-----------------|
| F-21 | Real image file, image URL, or binary asset | **STOP — record BLOCKED** |
| F-22 | HTTP request to image generation API (DALL-E, Midjourney, Stable Diffusion, etc.) | **STOP — record BLOCKED** |
| F-23 | HTTP request to Google Drive, S3, or cloud storage | **STOP — record BLOCKED** |
| F-24 | `approval_status` = `"Approved"` or `"Published"` | **STOP — record BLOCKED** |
| F-25 | Any real customer PII in output | **STOP — record BLOCKED** |
| F-26 | `active = true` set anywhere | **STOP — record BLOCKED** |

---

## H. Evidence Capture Checklist

| ID | Evidence Item | Details |
|----|--------------|---------|
| EC-01 | Execution panel screenshot | Full canvas showing all nodes green (or partial with branch taken noted) |
| EC-02 | Code: Write Log Entry output screenshot | `logEntry` JSON visible with `log_id`, `timestamp`, `status` |
| EC-03 | NoOp: STUB — Send to Approval Queue screenshot | `approvalQueueStubReached = true` visible |
| EC-04 | If: Validation Pass branch screenshot | Which branch was taken (TRUE or FALSE) visible |
| EC-05 | `logEntry` JSON — copy full object | Paste into evidence log `result_summary` |
| EC-06 | n8n Execution ID | Copy from execution panel header |
| EC-07 | List of all nodes executed | Match against Section E node chain above |
| EC-08 | Evidence log filled completely | All fields in `logs/phase_22a_creative_asset_sandbox_evidence_log.md` filled |

---

## I. Screenshot Naming Convention

All screenshots must follow this exact naming convention:

```
YYYYMMDD_HHMM_creative_asset_[description]_[result].png
```

| Token | Format | Example |
|-------|--------|---------|
| `YYYYMMDD` | Date of execution | `20260530` |
| `HHMM` | 24-hour time of execution | `1430` |
| `creative_asset` | Fixed workflow identifier | `creative_asset` |
| `[description]` | Short node or view description (lowercase, underscores) | `canvas`, `log_entry`, `noop_stub`, `validation_branch` |
| `[result]` | `pass` or `blocked` | `pass` |

### Full Examples

```
20260530_1430_creative_asset_canvas_pass.png
20260530_1432_creative_asset_log_entry_pass.png
20260530_1433_creative_asset_noop_stub_pass.png
20260530_1434_creative_asset_validation_branch_pass.png
```

Store all screenshots in: `evidence/phase_22b/creative_asset_auto_skeleton/`

---

## J. Required Log File Path

```
logs/phase_22a_creative_asset_sandbox_evidence_log.md
```

> This log file is created blank in Phase 22A. Owner fills it during Phase 22B execution.
> The filled log is committed to the repo in **Phase 22C** (Owner Evidence Submission) — not in Phase 22B.

---

## K. Required Payload Reference

**Payload file:** `samples/sandbox/phase_17_test_payloads/creative_asset_auto_skeleton_test_payload.md`
**Scenario:** P17-WF02-S1 — Facebook Image Creative Brief

Input values pre-set in workflow (no manual editing required):

```json
{
  "brand_id": "VQ",
  "brand_name": "Vị Cuốn",
  "asset_type": "Image",
  "platform": "Facebook",
  "content_angle": "Product Highlight",
  "visual_direction": "REPLACE_WITH_VISUAL_DIRECTION",
  "objective": "Awareness"
}
```

> `REPLACE_WITH_VISUAL_DIRECTION` is an expected stub placeholder — not an error.

---

## L. Stop Conditions

Stop immediately and record BLOCKED if ANY of the following occur:

| ID | Condition | Required Action |
|----|-----------|----------------|
| SC-01 | Workflow active toggle is ON at any point | Stop. Do not trigger. Record BLOCKED. |
| SC-02 | n8n prompts to add a real credential | Stop. Do not enter credentials. Record BLOCKED. |
| SC-03 | Any HTTP call to an image generation API is observed | Stop. Record BLOCKED. |
| SC-04 | Any HTTP call to cloud storage (Google Drive, S3, Dropbox) is observed | Stop. Record BLOCKED. |
| SC-05 | Any real image, video, or binary file appears in output | Stop. Record BLOCKED. |
| SC-06 | `approval_status` changes to anything other than `"Draft"` | Stop. Record BLOCKED. |
| SC-07 | Any real customer PII appears in any node output | Stop. Record BLOCKED. |
| SC-08 | Any HTTP call to a social platform publish endpoint (Facebook, Instagram, TikTok, Zalo) | Stop. Record BLOCKED. |
| SC-09 | n8n execution appears to run on a production instance | Stop. Record BLOCKED. |
| SC-10 | Any node output is unclear or unexpected and cannot be explained by the stub structure | Stop. Record BLOCKED. Do not debug inside n8n. |

---

## M. PASS / FAIL Criteria

### PASS — All of the following must be true

| # | PASS Criterion |
|---|----------------|
| 1 | All happy-path nodes (Manual Trigger through NoOp) complete green |
| 2 | `brandBrainLoaded = true` in Code: Load Brand Brain output |
| 3 | `contentDraftGenerated = true` in Code: AI Generate Creative Brief output |
| 4 | `draft_brief` is non-null (any string or object) |
| 5 | `approval_status = "Draft"` in Set: approval_status node output |
| 6 | `logWritten = true` in Code: Write Log Entry output |
| 7 | `logEntry.log_id` present and starts with `"LOG-"` |
| 8 | `approvalQueueStubReached = true` in NoOp output |
| 9 | No real image file, URL, or binary asset in any node output |
| 10 | No image generation API call, cloud storage call, or publish API call |
| 11 | No real customer PII in any output |
| 12 | Workflow remained INACTIVE throughout |

> The validation failure path (FALSE branch) is **also acceptable** — a PASS result is still valid if `validationPassed = false` as long as no forbidden output is present and the workflow remains INACTIVE.

### BLOCKED — Any of the following triggers BLOCKED

| # | BLOCKED Trigger |
|---|----------------|
| 1 | Any stop condition SC-01 through SC-10 occurs |
| 2 | Any real image file, URL, or binary asset observed |
| 3 | `approval_status` is not `"Draft"` |
| 4 | `logEntry.log_id` absent |
| 5 | `approvalQueueStubReached` is absent or false |
| 6 | Workflow was activated at any point |

---

## N. Explicit Non-Goals

This phase does **none** of the following:

| Non-Goal | Confirmation |
|----------|-------------|
| Production readiness claim | NOT claimed — sandbox test only |
| Production execution | NOT performed — sandbox only |
| Workflow activation | NOT done — workflow stays INACTIVE |
| Real credentials | NOT added — placeholder or "Credential not found" only |
| Real customer data | NOT used — all dummy/placeholder values |
| Auto-post to any platform | NOT performed — no platform publish node in skeleton |
| Real creative asset generation | NOT performed — output is creative brief only (no image/video/file) |
| Real inbox or comment reply | NOT performed — not applicable to this workflow |
| Ads spend | NOT triggered — not applicable to this workflow |
| External paid generation (DALL-E, Midjourney, etc.) | NOT triggered — no real AI generation node in skeleton |
| Workflow logic modification | NOT done — n8n JSON files are not touched |
| Phase 22B execution | NOT performed — this phase only prepares the pack |

---

## O. Recommended Next Phase

**Phase 22B — Owner Manual Sandbox Runbook for creative_asset_auto_skeleton**

Phase 22B will provide:
- Step-by-step Owner runbook (12 steps) for manually executing `creative_asset_auto_skeleton` in the sandbox
- Node-by-node observation guide
- Stop condition handling
- Evidence log fill instructions

**Entry criteria for Phase 22B:**
- Phase 22A PACK_READY
- Codex review PASS on Phase 22A
- Owner confirms OWNER_APPROVED
- Phase 22A files committed to repo

---

## Phase Connections

| Phase | Type | Workflow | Result |
|-------|------|----------|--------|
| Phase 8 | Build | All 6 workflow skeletons | DONE (commit `ad867b3`) |
| Phase 14 | Dry-run | All 6 workflows imported sandbox | PASS (commit `86099bb`) |
| Phase 17 | Test data | Phase 17 payloads for all 6 workflows | DONE (commit `ac91976`) |
| Phase 20A | Evidence pack | `content_auto_skeleton` | DONE (commit `f505dae`) |
| Phase 20B | Runbook | `content_auto_skeleton` | DONE (commit `fb33e8c`) |
| Phase 20C | Evidence submission | `content_auto_skeleton` | **PASS** (commit `50df2af`) |
| Phase 21 | Expansion plan | Remaining 5 workflows | DONE (commit `07ef58b`) |
| **Phase 22A** | **Evidence pack** | **`creative_asset_auto_skeleton`** | **THIS PHASE** |
| Phase 22B | Runbook | `creative_asset_auto_skeleton` | Next |
| Phase 22C | Evidence submission | `creative_asset_auto_skeleton` | After 22B PASS |

---

## Safety Confirmation

| Check | Status |
|-------|--------|
| n8n workflow JSON modified | NO |
| `active = true` introduced | NO |
| Real credentials added | NO |
| Real customer data used | NO |
| Workflow executed | NO |
| Auto-post triggered | NO |
| Auto-reply triggered | NO |
| Ads spend triggered | NO |
| External paid generation triggered | NO |
| Production readiness claimed | NO |
| Secret scan | CLEAN |
| Branch | main |
| Latest commit at build time | `07ef58b` |
