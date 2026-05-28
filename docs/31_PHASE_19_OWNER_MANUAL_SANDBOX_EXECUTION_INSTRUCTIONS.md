# Phase 19 — Owner Manual Sandbox Execution Instructions

**Phase:** 19
**Type:** Instruction / Readiness Document Only
**Created By:** Claude Code (Builder, AGT-02) — 2026-05-29
**Status:** INSTRUCTION_READY — READY FOR CODEX REVIEW

---

## A. Purpose

Phase 19 is an **instruction and readiness document only.**

It does **not** execute any n8n workflow.
It does **not** modify any workflow JSON.
It does **not** set up credentials.
It does **not** claim production readiness.

Phase 19 prepares the Owner (Bo Bao) to manually execute sandbox workflows in a future session using:
- The 6 Phase 8 workflow skeletons imported into a sandbox n8n instance
- Dummy test payloads from Phase 17 (`samples/sandbox/phase_17_test_payloads/`)
- Evidence template from Phase 17 (`logs/templates/SANDBOX_EXECUTION_EVIDENCE_TEMPLATE.md`)
- This instruction document as the session guide

Phase 19 is the **Owner execution preparation gate.** After reading this document and satisfying the pre-execution checklist, Owner may begin manual sandbox execution in Phase 20.

---

## B. Pre-Execution Checklist

Complete all items before starting any manual sandbox run. Do not proceed if any item is NOT MET.

| ID | Check | Required State | Status |
|----|-------|---------------|--------|
| PC-01 | Git status is clean | `git status --short` returns empty | Owner to verify |
| PC-02 | Latest commit verified | `git log -1 --oneline` shows `ac91976` or later | Owner to verify |
| PC-03 | Phase 18 Codex review | Phase 18 PASS issued | DONE (Phase 18 PASS) |
| PC-04 | Phase 19 Owner approval | Owner has read this document | Owner to confirm |
| PC-05 | n8n sandbox instance accessible | Can open n8n in browser | Owner to verify |
| PC-06 | All 6 workflows imported in n8n | 6 workflows visible in n8n Workflows list | Owner to verify |
| PC-07 | All 6 workflows are INACTIVE | Toggle shows OFF / inactive for all 6 | Owner to verify |
| PC-08 | Sandbox confirmed (not production) | URL is localhost or known sandbox instance | Owner to verify |
| PC-09 | No real credentials configured | All credentials show "Credential not found" | Owner to verify |
| PC-10 | Dummy sandbox payload files accessible | `samples/sandbox/phase_17_test_payloads/` folder open | Owner to verify |
| PC-11 | Evidence folder ready | `logs/` folder writable | Owner to verify |
| PC-12 | Log file path selected | `logs/phase_19_manual_sandbox_execution_log.md` ready | Owner to verify |
| PC-13 | 60-minute session window allocated | Uninterrupted time confirmed | Owner to verify |
| PC-14 | Owner approval confirmed | Owner signs off below before any run | Owner to confirm |

**Owner Pre-Execution Sign-Off:**

```
I, Bo Bao (Owner), confirm I have read Phase 19 instructions,
completed PC-01 through PC-13, and I authorise the manual sandbox
execution session described in this document.

Owner: ___________________  Date: ___________________
```

---

## C. Workflow List — All 6 Phase 8 Workflows

All workflows must be imported and INACTIVE before any manual run.

| ID | Workflow File | n8n Workflow Name | Risk Level | Phase 17 Payload |
|----|--------------|-------------------|------------|-----------------|
| WF-01 | `n8n/workflows/content_auto_skeleton.json` | FnB OS V1 — Content Auto [SKELETON] | Standard | `content_auto_skeleton_test_payload.md` |
| WF-02 | `n8n/workflows/creative_asset_auto_skeleton.json` | FnB OS V1 — Creative Asset Auto [SKELETON] | Standard | `creative_asset_auto_skeleton_test_payload.md` |
| WF-03 | `n8n/workflows/ads_pack_auto_skeleton.json` | FnB OS V1 — Ads Pack Auto [SKELETON] | HIGH RISK | `ads_pack_auto_skeleton_test_payload.md` |
| WF-04 | `n8n/workflows/crm_followup_auto_skeleton.json` | FnB OS V1 — CRM Follow-Up Auto [SKELETON] | HIGH RISK | `crm_followup_auto_skeleton_test_payload.md` |
| WF-05 | `n8n/workflows/comment_inbox_reply_assistant_skeleton.json` | FnB OS V1 — Comment Inbox Reply Assistant [SKELETON] | HIGH RISK | `comment_inbox_reply_assistant_skeleton_test_payload.md` |
| WF-06 | `n8n/workflows/approval_publishing_skeleton.json` | FnB OS V1 — Approval and Publishing Gate [SKELETON] | HIGH RISK | `approval_publishing_skeleton_test_payload.md` |

---

## D. Manual Sandbox Execution Rules

These rules apply to **every workflow** without exception.

### D.1 Universal Rules

| Rule | Requirement |
|------|-------------|
| Execution type | Manual execution only (n8n "Test" / "Execute workflow" button) |
| Data | Only dummy data from Phase 17 payloads — no real customer data |
| Credentials | None — all placeholders remain. Do not enter real API keys, tokens, passwords |
| Publishing | No real content publishing to any platform (Facebook, Instagram, TikTok, Zalo) |
| Ads spend | No Meta Ads, TikTok Ads, or any other paid campaign |
| Messaging | No messages to real customers via Zalo, Messenger, SMS, or any channel |
| Comment reply | No auto-reply or manual reply to real comments or inbox messages |
| Activation | Never set a workflow to active=true or toggle ON |
| Evidence | Capture screenshot of execution result for each workflow run |
| Log file | Fill `logs/phase_19_manual_sandbox_execution_log.md` after each workflow run |

### D.2 Per-Workflow Extra Rules

**WF-03 — Ads Pack Auto (HIGH RISK):**
- Confirm NO ADS SPEND sticky note is visible in n8n canvas before executing.
- Confirm no Meta Ads, TikTok Ads, or Zalo Ads node is present (all should be NoOp stubs).
- Do not enter any real Ad Account ID, Pixel ID, or budget value anywhere.
- If any live ads API call is triggered, stop immediately and record as BLOCKED.

**WF-04 — CRM Follow-Up Auto (HIGH RISK):**
- Confirm NO AUTO-SEND sticky note is visible in n8n canvas before executing.
- Do not enter any real customer phone, Zalo ID, Facebook PSID, or email.
- `human_review_required` output must be `true` — if it is `false`, record as BLOCKED.
- If any Zalo OA API, Messenger API, or SMS gateway call is triggered, stop immediately.

**WF-05 — Comment Inbox Reply Assistant (HIGH RISK):**
- Confirm NO AUTO-REPLY to real customers in any execution result.
- Must test BOTH mandatory scenarios: S1 (non-escalation) and S2 (escalation).
- S2 (escalation/angry comment) must produce `draft_reply = null` and route to human review.
- If `draft_reply` is non-null on the escalation branch, record as BLOCKED.

**WF-06 — Approval and Publishing Gate (HIGH RISK):**
- Trigger via n8n Test Webhook only (not manual trigger). Workflow must remain INACTIVE.
- Must test BOTH mandatory scenarios: S1 (approved payload) and S2 (not-approved payload).
- S1 must route to Switch → NoOp stubs (no real publishing call).
- S2 must route to block path → Stop and Error (no real publishing call).
- If any real platform publish API is called, stop immediately and record as BLOCKED.

---

## E. Step-by-Step Owner Instructions

Follow these steps in order for each workflow.

### Step 1 — Open n8n

Open the n8n instance in your browser (sandbox/localhost only, not production).
Confirm you are on the correct sandbox instance.

### Step 2 — Confirm Workflow is Inactive

Open the Workflows list in n8n.
Confirm the workflow you are about to test shows the **Inactive** toggle (OFF position).
Do NOT activate the workflow.

### Step 3 — Open Workflow

Click on the workflow name to open the canvas.
Visually confirm:
- The Sticky Note at the top shows "DO NOT ACTIVATE" or "SKELETON" warning.
- For WF-03: "NO ADS SPEND" sticky note is visible.
- For WF-04: "NO AUTO-SEND" sticky note is visible.
- All publish/send/spend nodes are labeled "NoOp" or "STUB DISABLED".

### Step 4 — Select Manual Trigger or Test Webhook

**WF-01 through WF-05:** Click the Manual Trigger node (or "Test workflow" button in n8n UI).

**WF-06 only:** Use the Test Webhook option:
- Click the Webhook node in the canvas.
- Click "Listen for test event" to get the temporary test URL.
- Use the test URL from the Phase 17 payload file — this URL is valid only during the test session, does not require activation, and is sandbox-local only.
- Do not expose this URL to the public internet.

### Step 5 — Use Phase 17 Dummy Payload

Open the relevant Phase 17 test payload file in `samples/sandbox/phase_17_test_payloads/`.
Use exactly the dummy input values specified in the payload file.
Do not substitute real customer names, real phone numbers, real emails, real IDs, real credentials, or real prices.

For WF-06: Send the payload via the test webhook URL using the browser, curl, or n8n "Send test data" input. Do not use any real platform credentials.

### Step 6 — Execute Manually

Click "Execute workflow" or the play button for manual workflows.
For WF-06: Send the test webhook payload as instructed in Step 5.
Observe that execution starts. Do not interrupt during execution.

### Step 7 — Observe Node Output

After execution completes:
- Click each node in turn to view the node output panel.
- Check that the output matches the expected output in the Phase 17 payload file.
- Check that no forbidden output from the Phase 17 payload is present.
- Pay special attention to the CRITICAL forbidden output items (ads APIs, messaging APIs, publishing APIs).

### Step 8 — Save Evidence Screenshot

Take a screenshot of:
1. The n8n execution result panel (showing green/red nodes).
2. The output of the key decision node (If: Is Approved, If: Escalation Required, etc.).
3. The final log node output (Code: Write Approval Log or Code: Write Log).

Save screenshots with the naming convention:
`phase19_WF0X_[scenario]_[PASS_or_BLOCKED]_[YYYYMMDD].png`

Example: `phase19_WF06_S1_approved_PASS_20260529.png`

Store screenshots locally. Screenshots are evidence but **do not replace the required log file.**

### Step 9 — Fill Evidence Template

Open `logs/templates/SANDBOX_EXECUTION_EVIDENCE_TEMPLATE.md`.
Make a copy named:
`logs/phase_19_evidence_WF0X_[scenario]_[YYYYMMDD].md`

Fill all sections of the template. Minimum required fields per Section F below.

### Step 10 — Create or Update Required Log File

Open `logs/phase_19_manual_sandbox_execution_log.md`.
Add one entry per workflow run following the log format in Section G below.
If the log file does not exist yet, create it using the template in Section G.

**The log file is mandatory.** A screenshot alone is not sufficient evidence for phase completion.

### Step 11 — Do Not Fix Manually Inside n8n

If you observe an unexpected result, blocker, or error:
- **Do not attempt to fix the workflow logic inside n8n.**
- Record the exact error and node output in the log file.
- Record the issue in Section F of the evidence template.
- Mark the run as BLOCKED.
- Report the blocker to Builder. A future Builder phase will address the fix.

The Owner role is to **observe and record**, not to debug or patch.

---

## F. Evidence Requirements

Fill the following fields in the evidence template for each workflow run.

| Field | Description | Required |
|-------|-------------|---------|
| `workflow_name` | n8n workflow name (e.g. FnB OS V1 — Content Auto [SKELETON]) | YES |
| `workflow_file` | Repo file path (e.g. n8n/workflows/content_auto_skeleton.json) | YES |
| `sandbox_payload_file` | Phase 17 payload file used | YES |
| `execution_timestamp` | Date and time of run (YYYY-MM-DD HH:MM) | YES |
| `execution_type` | Must be `manual_sandbox` | YES |
| `active_status_before_run` | Must be `inactive / false` | YES |
| `result_status` | PASS / BLOCKED / PARTIAL | YES |
| `screenshot_reference` | Filename of screenshot(s) saved | YES |
| `log_file_reference` | Path of log file entry | YES |
| `nodes_executed` | List of nodes that executed (from n8n panel) | YES |
| `key_output_fields_observed` | Values seen in node output (e.g. approval_valid=true) | YES |
| `issue_or_blocker` | Describe any unexpected behavior or STOP condition | YES (write NONE if none) |
| `owner_approval_status` | Owner confirms run complete and evidence captured | YES |

---

## G. Required Log File Format

Log file path: `logs/phase_19_manual_sandbox_execution_log.md`

Create this file before or during the first sandbox execution session.
Append one entry per workflow run.

### Log File Header (create once)

```markdown
# Phase 19 — Manual Sandbox Execution Log

**Phase:** 19
**Owner:** Bo Bao
**Log Type:** manual_sandbox_execution
**Created:** [YYYY-MM-DD]
**Last Updated:** [YYYY-MM-DD]

---
```

### Log Entry Template (one per workflow run)

```markdown
## Run: [WF-ID] — [workflow_name] — [Scenario ID if applicable]

| Field | Value |
|-------|-------|
| `workflow_name` | [n8n workflow name] |
| `workflow_file` | [repo file path] |
| `payload_file` | [samples/sandbox/phase_17_test_payloads/...] |
| `execution_type` | manual_sandbox |
| `execution_timestamp` | [YYYY-MM-DD HH:MM] |
| `active_status_before_run` | inactive — false |
| `credentials_used` | placeholder_or_none |
| `real_customer_data_used` | no |
| `auto_post_executed` | no |
| `auto_reply_executed` | no |
| `ads_spend_executed` | no |
| `nodes_executed` | [list node names from n8n panel] |
| `key_output_fields_observed` | [e.g. approval_valid=true, logEntry.status=Success] |
| `result` | PASS / BLOCKED / PARTIAL |
| `evidence_files` | [screenshot filename(s) + evidence template copy path] |
| `issue_or_blocker` | [NONE or description] |
| `owner_decision` | APPROVED_FOR_PHASE_20 / BLOCKED_NEEDS_FIX |
| `next_action` | [e.g. Proceed to Phase 20 / Report blocker to Builder] |

---
```

---

## H. Explicit Non-Goals

Phase 19 explicitly does **not** accomplish the following. Any of these activities are out of scope and forbidden.

| Non-Goal | Why Excluded |
|----------|-------------|
| Production readiness | Workflows are skeletons — not configured for live use |
| Live execution | This is a sandbox manual test only — not a live system run |
| Credential setup | REPLACE_WITH_* placeholders must not be filled in Phase 19 |
| Workflow activation | `active: false` must not be changed to `active: true` at any time |
| Publishing automation | No content, ads, or creative assets are published to any platform |
| Customer response automation | No messages, replies, or comments are sent to real customers |
| Ads execution | No ad campaign is created, launched, or budgeted |
| Workflow code fixes | If a node produces unexpected output, do not edit the workflow in n8n |
| Production instance testing | All runs must use a sandbox/localhost n8n instance only |
| Schema validation of node outputs | Schema validation is a future Builder phase task |
| Error trigger path coverage | Error trigger path testing is optional and non-blocking in Phase 19 |

---

## I. Next Phase Recommendation

**Phase 20 — Owner Manual Sandbox Execution Evidence Capture**

**Scope:**
Owner manually executes selected sandbox workflow(s) with dummy data from Phase 17 payloads.
Owner records evidence in the log file at `logs/phase_19_manual_sandbox_execution_log.md`.
Owner fills one copy of `logs/templates/SANDBOX_EXECUTION_EVIDENCE_TEMPLATE.md` per workflow run.
Owner does not fix workflow code — observes and records only.

**Entry criteria for Phase 20:**
- Phase 19 Codex PASS
- Phase 19 Owner OWNER_APPROVED
- PC-01 through PC-14 satisfied
- Log file created at `logs/phase_19_manual_sandbox_execution_log.md`

**Minimum viable Phase 20 scope:**
Run at least WF-01 (content_auto) and WF-06 (approval_publishing) with their mandatory scenarios.
WF-03, WF-04, WF-05 may follow in subsequent sessions.

**Phase 20 success criteria:**
- At least 1 workflow run: PASS (manual sandbox, dummy data, no forbidden output, evidence captured, log written)
- `logs/phase_19_manual_sandbox_execution_log.md` contains at least 1 completed entry
- No BLOCKED conditions unresolved

---

## Phase Connections

| Phase | Title | Relationship |
|-------|-------|-------------|
| Phase 8 | n8n Importable Workflow Skeletons | Source of all 6 workflow JSON files |
| Phase 14 | Owner n8n Sandbox Dry-Run | Confirmed: all 6 workflows imported, all inactive |
| Phase 16 | Sandbox Runtime Validation Plan | Defines execution safety rules and stop conditions |
| Phase 17 | Sandbox Test Data + Evidence Pack | Provides dummy payloads and evidence template |
| Phase 18 | Codex Review Gate | Reviewed Phase 17 pack — PASS |
| Phase 19 | Owner Manual Sandbox Execution Instructions | **This document** — Owner execution preparation |
| Phase 20 | Owner Manual Sandbox Execution Evidence Capture | Next: Owner executes, records evidence |

---

## Safety Confirmation

| Check | Status |
|-------|--------|
| n8n workflow JSON files modified in Phase 19 | NO — untouched |
| `active: true` introduced in Phase 19 | NO |
| Real credentials added in Phase 19 | NO |
| Real customer data used in Phase 19 | NO |
| Auto-post / auto-reply / ads executed in Phase 19 | NO |
| Production readiness claimed in Phase 19 | NO |
| Secret scan (API keys, tokens, passwords, private keys) | CLEAN |
