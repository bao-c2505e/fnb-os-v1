# Phase 20B — Owner Manual Sandbox Runbook: content_auto_skeleton

**Phase:** 20B
**Type:** Owner Runbook — Manual Sandbox Execution
**Selected Workflow:** `content_auto_skeleton`
**Created By:** Claude Code (Builder, AGT-02) — 2026-05-29
**Status:** RUNBOOK_READY — AWAITING OWNER EXECUTION

---

## A. Purpose

Phase 20B is the **first actual manual sandbox execution** of `content_auto_skeleton`.

The Owner (Bo Bao) follows this runbook to:
1. Open the workflow in the sandbox n8n instance.
2. Trigger it once using dummy data (no modifications required).
3. Observe node output.
4. Capture screenshot evidence.
5. Record the result in the evidence log.

Builder does **not** execute on Owner's behalf.
Builder does **not** observe the n8n session.
Owner executes independently, using this runbook as the step-by-step guide.

This phase does **not** claim production readiness.
This phase does **not** set up real credentials.
This phase does **not** activate the workflow.

---

## B. Selected Workflow

| Field | Value |
|-------|-------|
| Workflow file | `n8n/workflows/content_auto_skeleton.json` |
| n8n workflow name | `FnB OS V1 — Content Auto [SKELETON]` |
| Risk level | Standard |
| Trigger type | Manual Trigger |
| Phase 17 payload | `samples/sandbox/phase_17_test_payloads/content_auto_skeleton_test_payload.md` |
| Payload scenario | P17-WF01-S1 — Standard Facebook Content Request |
| Evidence log | `logs/phase_20a_content_auto_sandbox_evidence_log.md` |
| Evidence folder | `evidence/phase_20b/content_auto_skeleton/` |
| This runbook | `docs/33_PHASE_20B_OWNER_MANUAL_SANDBOX_RUNBOOK_CONTENT_AUTO.md` |

---

## C. Required Pre-Run State

Confirm every item before opening n8n. Do not proceed if any item is NOT MET.

| ID | Required State | How to Verify | Met? |
|----|---------------|--------------|------|
| PRE-01 | Local repo is clean | `git status --short` returns empty | [ ] |
| PRE-02 | Latest commit is `f505dae` or later | `git log -1 --oneline` | [ ] |
| PRE-03 | `content_auto_skeleton` is imported in n8n | Open n8n Workflows list — name visible | [ ] |
| PRE-04 | Workflow is INACTIVE | Toggle shows OFF in Workflows list | [ ] |
| PRE-05 | n8n instance is sandbox / localhost | URL is localhost or known sandbox — not production | [ ] |
| PRE-06 | Phase 17 dummy payload file is accessible | Open `samples/sandbox/phase_17_test_payloads/content_auto_skeleton_test_payload.md` | [ ] |
| PRE-07 | Evidence log file is accessible | Open `logs/phase_20a_content_auto_sandbox_evidence_log.md` | [ ] |
| PRE-08 | Evidence folder exists | `evidence/phase_20b/content_auto_skeleton/` folder present in repo | [ ] |
| PRE-09 | No real credentials will be added | Confirmed — all credentials will remain as "Credential not found" | [ ] |
| PRE-10 | Owner approval confirmed | Owner has read this runbook and is ready to proceed | [ ] |

**Owner Pre-Run Sign-Off:**

```
I, Bo Bao (Owner), confirm PRE-01 through PRE-09 are satisfied
and I am proceeding with a manual sandbox test only.
I will not activate the workflow, add real credentials, or post any content.

Owner: ___________________  Date: ___________________  Time: ___________________
```

---

## D. Exact Owner n8n UI Steps

Follow in order. Do not skip steps. Mark each as done.

### Step 1 — Open n8n

Open your sandbox n8n instance in the browser (localhost or sandbox URL).
Confirm the URL is your sandbox instance, not a production n8n server.

- [ ] n8n sandbox open in browser

### Step 2 — Open content_auto_skeleton

In n8n, click **Workflows** in the left sidebar.
Find `FnB OS V1 — Content Auto [SKELETON]` in the list.
Click the workflow name to open it.

- [ ] Workflow canvas is open

### Step 3 — Confirm Workflow is Inactive

Before doing anything else:
Look at the top-right of the n8n canvas for the Active/Inactive toggle.
Confirm it shows **Inactive** (grey / OFF position).

**If the toggle shows Active: STOP. Do not proceed. Record BLOCKED.**

- [ ] Toggle confirmed INACTIVE

### Step 4 — Do NOT Add Real Credentials

When n8n shows "Credential not found" warnings on Code nodes, this is expected.
These warnings are stubs — do not resolve them by entering real API keys, tokens, or passwords.
Proceed with "Credential not found" warnings in place.

- [ ] Confirmed: no real credentials will be added

### Step 5 — Do NOT Activate the Workflow

Do not click the Active toggle at any point during this session.
The workflow must remain INACTIVE (active: false) before, during, and after the run.

- [ ] Confirmed: workflow will not be activated

### Step 6 — Locate the Manual Trigger

On the workflow canvas, find the **Manual Trigger** node on the far left.
In n8n, you will see a "Test workflow" button or you can right-click the Manual Trigger node to run it.

The input data for this workflow is pre-set inside the `Set Input Variables` node — you do not need to enter any data manually.

- [ ] Manual Trigger located

### Step 7 — Use the Phase 17 Dummy Payload

The Phase 17 dummy payload for this workflow is:
`samples/sandbox/phase_17_test_payloads/content_auto_skeleton_test_payload.md`
Scenario: **P17-WF01-S1 — Standard Facebook Content Request**

The workflow's `Set Input Variables` node already contains these stub values:

```
brand_id: VQ
brand_name: Vị Cuốn
content_request: REPLACE_WITH_OWNER_CONTENT_REQUEST
platform: Facebook
objective: Awareness
target_audience: REPLACE_WITH_TARGET_AUDIENCE
offer: [OWNER_TO_PROVIDE_OFFER]
```

You do **not** need to modify the workflow or enter new values.
The `REPLACE_WITH_*` strings are expected stubs — not failures.

- [ ] Payload reference confirmed — no workflow modification needed

### Step 8 — Run Manual Sandbox Execution Once Only

Click **"Test workflow"** (or the equivalent "Execute workflow" button in your n8n version).

Run **once only**. Do not re-run until you have recorded the result of the first run.

Wait for execution to complete. Each node will show green (success) or red (error) in the canvas.

- [ ] Execution triggered (once)
- [ ] Execution completed

### Step 9 — Observe Output

Click each node in the execution panel to view its output. Record what you see.

Work through the node chain in order:

| Node to click | What to look for |
|--------------|-----------------|
| `Set Input Variables` | `brand_name = "Vị Cuốn"`, `platform = "Facebook"` |
| `Code: Load Brand Brain` | `brandBrainLoaded = true` |
| `Code: AI Generate Content Draft` | `contentDraft.approval_status = "Draft"` |
| `Code: Validate Required Fields` | `validation_pass` field present |
| `If: Validation Pass` | Which branch was taken — TRUE or FALSE |
| `Set: approval_status = Draft` | `approval_status = "Draft"` (if TRUE branch) |
| `Code: Write Log Entry` | `logEntry.log_id` starts with `"LOG-"`, `logWritten = true` |
| `NoOp: STUB — Send to Approval Queue` | Node is green, no output (if happy path) |

Also note the n8n **Execution ID** — visible in the execution panel or Executions history tab.

- [ ] All nodes observed
- [ ] n8n Execution ID noted: ___________________

### Step 10 — Capture Screenshot Evidence

Take screenshots and save them locally before closing n8n:

| Screenshot | Required | Filename |
|-----------|---------|---------|
| Full execution panel (all nodes visible) | YES | `evidence/phase_20b/content_auto_skeleton/YYYYMMDD_HHMM_content_auto_manual_sandbox_<result>.png` |
| `Code: Write Log Entry` output panel | YES | `evidence/phase_20b/content_auto_skeleton/YYYYMMDD_HHMM_content_auto_write_log_entry_<result>.png` |
| `If: Validation Pass` node (branch taken) | YES | `evidence/phase_20b/content_auto_skeleton/YYYYMMDD_HHMM_content_auto_if_validation_<result>.png` |
| `NoOp: STUB — Send to Approval Queue` | YES | `evidence/phase_20b/content_auto_skeleton/YYYYMMDD_HHMM_content_auto_noop_approval_queue_<result>.png` |

Replace `YYYYMMDD_HHMM` with the actual date and time of execution.
Replace `<result>` with `PASS` or `BLOCKED`.

Example: `20260529_1430_content_auto_manual_sandbox_PASS.png`

Screenshots are stored locally by the Owner. They do not need to be committed to the repo unless specifically requested in a future phase.

- [ ] All required screenshots saved with correct naming convention

### Step 11 — Record Result in Evidence Log

Open `logs/phase_20a_content_auto_sandbox_evidence_log.md`.

Fill in every `[Owner to fill]` field based on what you observed:
- `execution_status` → change from `not_executed_yet` to `PASS` or `BLOCKED`
- `active_status_before_run` → `inactive / false`
- `active_status_after_run` → `inactive / false`
- `execution_timestamp` → actual date and time
- `n8n_execution_id` → from n8n Executions panel
- Node Execution Results table → check each node row
- Key Output Fields table → copy values from n8n output panels
- Forbidden Output Checks → FC-01 through FC-06
- Result Summary → fill all 5 fields
- Evidence Files → list screenshot filenames
- Issues Found → write NONE or describe issues
- Post-Run Safety Confirmation → check all 7 boxes
- Owner Decision → fill `owner_decision` and `next_action`
- Owner Sign-Off → sign and date

Save the file. It will be committed in Phase 20C.

- [ ] Evidence log fully filled
- [ ] Owner Sign-Off completed

### Step 12 — If Any Node Fails, Stop and Record Blocker

If any node shows a red error, unexpected output, or anything unclear:

1. **Stop immediately** — do not attempt to fix the workflow inside n8n.
2. Note the node name and the exact error message shown in n8n.
3. Record the issue in the **Issues Found** table in the evidence log.
4. Set `execution_status` to `BLOCKED` in the evidence log.
5. Set `owner_decision` to `BLOCKED_NEEDS_FIX`.
6. Set `next_action` to `Report blocker to Builder — Phase 20C will document the issue`.
7. Save the evidence log.
8. Do not re-run until Builder has reviewed the blocker.

- [ ] Step 12 understood — will stop and record if any node fails

---

## E. Stop Conditions

Stop immediately if any of the following occur. Do not proceed.

| Stop Condition | Action |
|---------------|--------|
| n8n prompts you to add a real API key, token, or password | STOP — record BLOCKED — do not enter real credentials |
| Toggle is Active (workflow is activated) | STOP — record BLOCKED — do not run |
| Any node attempts to post/publish to Facebook, Instagram, TikTok, or Zalo | STOP — record BLOCKED |
| Any node attempts to send a message to a real customer | STOP — record BLOCKED |
| Any node attempts to create or launch an ad campaign | STOP — record BLOCKED |
| Any real customer data (name, phone, email, ID) appears in output | STOP — record BLOCKED |
| Any unexpected HTTP call to an external API appears in execution log | STOP — record BLOCKED |
| Any node output is unclear or not matching Section D Step 9 expectations | STOP — record BLOCKED — do not attempt to fix |

When BLOCKED: fill the Issues Found section of the evidence log with the exact error/node/output, set `execution_status = BLOCKED`, and report to Builder.

---

## F. Evidence Requirements

The following must be present in `logs/phase_20a_content_auto_sandbox_evidence_log.md` after the run:

| Field | Required Value |
|-------|---------------|
| `execution_status` | `PASS` or `BLOCKED` (not `not_executed_yet`) |
| `execution_timestamp` | Actual date and time of run |
| `workflow_name` | `FnB OS V1 — Content Auto [SKELETON]` |
| `payload_file` | `samples/sandbox/phase_17_test_payloads/content_auto_skeleton_test_payload.md` |
| `n8n_execution_id` | Value from n8n Executions panel (or `NOT_AVAILABLE` if not shown) |
| `evidence_screenshot_files` | At least 1 filename using the naming convention in Section D Step 10 |
| `result_summary` | 1–3 sentence description of what happened |
| `owner_decision` | `APPROVED_FOR_PHASE_20C_COMMIT` or `BLOCKED_NEEDS_FIX` |
| `active_status_before_run` | `inactive / false` |
| `active_status_after_run` | `inactive / false` |
| Owner Sign-Off | Signed and dated |

---

## G. Screenshot Naming Convention

```
evidence/phase_20b/content_auto_skeleton/YYYYMMDD_HHMM_content_auto_<description>_<result>.png
```

| Token | Meaning | Example |
|-------|---------|---------|
| `YYYYMMDD` | Date of run | `20260529` |
| `HHMM` | Time of run (24h) | `1430` |
| `<description>` | Short node/panel name | `manual_sandbox`, `write_log_entry`, `if_validation`, `noop_approval_queue` |
| `<result>` | Outcome | `PASS` or `BLOCKED` |

Full examples:
- `20260529_1430_content_auto_manual_sandbox_PASS.png`
- `20260529_1430_content_auto_write_log_entry_PASS.png`
- `20260529_1430_content_auto_if_validation_PASS.png`
- `20260529_1430_content_auto_noop_approval_queue_PASS.png`

---

## H. Log File to Update

**Path:** `logs/phase_20a_content_auto_sandbox_evidence_log.md`

This file was created in Phase 20A as a blank template.
Owner must fill it completely during Phase 20B.
After Owner fills and signs the log, it will be committed in **Phase 20C**.

Do not commit the log file during Phase 20B — wait for Phase 20C.

---

## I. Pass Criteria

All of the following must be true for Phase 20B to be PASS:

| Criterion | Required |
|-----------|---------|
| Manual run completed with dummy data | YES |
| No real credential used | NO real credentials |
| No real customer data in input or output | NO real customer data |
| No content auto-posted to any platform | NO auto-post |
| No customer message auto-sent | NO auto-reply |
| No ad campaign created or budget committed | NO ads spend |
| Workflow remains INACTIVE after run | YES — toggle stays OFF |
| At least one evidence screenshot captured and named correctly | YES |
| Evidence log filled with actual execution results | YES |
| Evidence log `execution_status` updated from `not_executed_yet` | YES — PASS or BLOCKED |
| Owner Sign-Off completed in evidence log | YES |

---

## J. Fail Criteria

Any one of the following causes Phase 20B to be BLOCKED:

| Fail Condition | Classification |
|---------------|---------------|
| Real credential required to proceed | BLOCKED — report to Builder |
| Real customer data present in output | BLOCKED — report to Builder |
| Workflow activation required to run | BLOCKED — report to Builder |
| Content posted or queued to real platform | BLOCKED — report to Builder |
| Message sent to real customer | BLOCKED — report to Builder |
| Ad campaign created or budget touched | BLOCKED — report to Builder |
| Unexpected external API call in execution | BLOCKED — report to Builder |
| Node output unclear — cannot verify result | BLOCKED — report to Builder |
| Evidence screenshot missing or unnamed | INCOMPLETE — redo evidence capture |
| Evidence log not filled or not signed | INCOMPLETE — complete before Phase 20C |

---

## K. Explicit Non-Goals

Phase 20B explicitly does NOT accomplish the following:

| Non-Goal | Status |
|----------|--------|
| Production readiness | OUT OF SCOPE |
| Production execution on live n8n | OUT OF SCOPE |
| Publishing content to Facebook, Instagram, TikTok, Zalo | OUT OF SCOPE |
| Sending messages to real customers | OUT OF SCOPE |
| Running or budgeting any ad campaign | OUT OF SCOPE |
| Setting up real API credentials | OUT OF SCOPE |
| Activating the workflow (`active: true`) | OUT OF SCOPE |
| Manually debugging workflow node code | OUT OF SCOPE — report blockers to Builder |
| Testing other workflows (WF-02 through WF-06) | OUT OF SCOPE — future phases |
| Committing the evidence log (Phase 20C task) | OUT OF SCOPE for Phase 20B |

---

## L. Next Phase

**Phase 20C — Owner Evidence Submission and Codex Review for content_auto_skeleton**

**Scope:**
Owner submits the filled `logs/phase_20a_content_auto_sandbox_evidence_log.md` for Builder to review and commit.
Builder commits the filled evidence log (and optionally evidence screenshots) to the repo.
Codex reviews the evidence to confirm Phase 20B was executed safely.

**Entry criteria for Phase 20C:**
- Phase 20B Owner execution completed (PASS or BLOCKED)
- `logs/phase_20a_content_auto_sandbox_evidence_log.md` filled with actual results
- `execution_status` is no longer `not_executed_yet`
- Owner Sign-Off completed in evidence log

---

## Phase Connections

| Phase | Title | Relationship |
|-------|-------|-------------|
| Phase 8 | n8n Importable Workflow Skeletons | Source of `content_auto_skeleton.json` |
| Phase 14 | Owner n8n Sandbox Dry-Run | Confirmed: workflow imported, inactive |
| Phase 17 | Sandbox Test Data + Evidence Pack | Source of P17-WF01-S1 dummy payload |
| Phase 19 | Owner Manual Sandbox Execution Instructions | General sandbox guide |
| Phase 20A | Manual Sandbox Evidence Capture Pack | Pre-run checklist, evidence log template |
| Phase 20B | Owner Manual Sandbox Runbook | **This document** — step-by-step execution guide |
| Phase 20C | Owner Evidence Submission and Codex Review | Next: commit filled evidence log + Codex review |

---

## Safety Confirmation

| Check | Status |
|-------|--------|
| n8n workflow JSON modified in Phase 20B runbook creation | NO — untouched |
| `active: true` introduced | NO |
| Real credentials added | NO |
| Real customer data added | NO |
| Workflow executed by Builder | NO — Owner executes independently |
| Auto-post / auto-reply / ads | NO |
| Production readiness claimed | NO |
| Secret scan (API keys, tokens, passwords, private keys) | CLEAN |
