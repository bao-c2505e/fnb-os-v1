# Sandbox Execution Evidence Template

**Template Version:** 1.0
**Created By:** Claude Code (Builder, AGT-02) — Phase 17
**Purpose:** Evidence record for one sandbox workflow test execution. Fill one copy per workflow per session.
**Usage:** Copy this template and rename as `SANDBOX_EVIDENCE_[WF_ID]_[DATE].md` (e.g., `SANDBOX_EVIDENCE_WF01_20260529.md`).

> ⚠️ Fill with ACTUAL observed n8n execution panel output only. Do NOT fabricate results. If a field was not observed, write "NOT OBSERVED" or "DID NOT RUN". Do not guess.

---

## Section 1 — Session Identity

| Field | Value |
|-------|-------|
| Evidence Record ID | `EVID-[WF_ID]-[YYYYMMDD]-[SEQ]` (e.g., `EVID-WF01-20260529-001`) |
| Date | `YYYY-MM-DD` |
| Time (start) | `HH:MM` (local time) |
| Time (end) | `HH:MM` (local time) |
| Operator / Tester | `[Owner name — Bo Bao or authorized operator]` |
| n8n Instance Type | `[ ] Sandbox / Test   [ ] Other: ___________` |
| n8n Instance URL | `[sandbox URL — keep private, do not commit to repo]` |

---

## Section 2 — Workflow Under Test

| Field | Value |
|-------|-------|
| Workflow ID | `WF-01 / WF-02 / WF-03 / WF-04 / WF-05 / WF-06` (circle one) |
| Workflow File | `n8n/workflows/[filename].json` |
| n8n Workflow Name (as shown in n8n) | `FnB OS V1 — [Name] [SKELETON]` |
| Phase 17 Test Payload Used | `P17-WF0[N]-S[N]` (e.g., `P17-WF01-S1`) |
| Phase 17 Payload File | `samples/sandbox/phase_17_test_payloads/[filename].md` |
| Risk Level | `[ ] Standard   [ ] High` |

---

## Section 3 — Pre-Test Confirmation

Complete before triggering the workflow. Check each item.

| Check | Confirmed? |
|-------|-----------|
| Workflow is INACTIVE (active toggle OFF) | `[ ] YES   [ ] NO — STOP` |
| No real credentials connected to any node | `[ ] YES   [ ] NO — STOP` |
| Test payload file open and reviewed | `[ ] YES   [ ] NO` |
| Phase 16 plan open for reference | `[ ] YES   [ ] NO` |
| Using sandbox n8n instance (not production) | `[ ] YES   [ ] NO — STOP` |
| No real customer data in any node | `[ ] YES   [ ] NO — STOP` |

**For WF-03 (Ads Pack) — extra:**

| Check | Confirmed? |
|-------|-----------|
| "NO ADS SPEND" Sticky Note visible on canvas | `[ ] YES   [ ] NO — STOP` |
| No Meta Ads / TikTok Ads credential present | `[ ] YES   [ ] NO — STOP` |

**For WF-04 (CRM) — extra:**

| Check | Confirmed? |
|-------|-----------|
| "NO AUTO-SEND" Sticky Note visible on canvas | `[ ] YES   [ ] NO — STOP` |
| No Zalo / Messenger / SMS credential present | `[ ] YES   [ ] NO — STOP` |

**For WF-05 (Comment Inbox) — extra:**

| Check | Confirmed? |
|-------|-----------|
| Escalation warning Sticky Note visible on canvas | `[ ] YES   [ ] NO — STOP` |
| No comment reply API credential present | `[ ] YES   [ ] NO — STOP` |

**For WF-06 (Approval Publishing) — extra:**

| Check | Confirmed? |
|-------|-----------|
| "DO NOT ACTIVATE" Sticky Note visible on canvas | `[ ] YES   [ ] NO — STOP` |
| Webhook path still `REPLACE_WITH_WEBHOOK_PATH` | `[ ] YES   [ ] NO — STOP` |
| No platform publish / ads / messaging credential present | `[ ] YES   [ ] NO — STOP` |
| Test webhook URL used (sandbox local only, not public) | `[ ] YES   [ ] NO — STOP` |

---

## Section 4 — Test Execution

### 4.1 Trigger Method

| Field | Value |
|-------|-------|
| Trigger method used | `[ ] Manual Trigger (click "Test workflow")   [ ] Test Webhook   [ ] Other: ___` |
| Test payload scenario ID | `P17-WF0[N]-S[N]` |
| Execution started at | `HH:MM` |
| Execution completed at | `HH:MM` |
| n8n Execution ID (if shown) | `[execution ID from n8n panel, if available]` |

### 4.2 Node Execution Results

For each node, record the actual result observed in the n8n execution panel.
Use: `PASS` = node ran successfully | `FAIL` = node showed error | `DID NOT RUN` = node was not reached | `N/A` = not applicable to this workflow.

| Node Name | Expected Result | Actual Result | Notes |
|-----------|----------------|---------------|-------|
| Manual Trigger / Webhook | Fired | | |
| Set Input Variables | Fields set | | |
| Code: Load Brand Brain | `brandBrainLoaded = true` | | |
| Code: Detect Intent (WF-05 only) | Intent and sentiment fields present | | |
| Code: AI Draft / Generate Content | `contentDraftGenerated = true` or draft present | | |
| Code: Check Approval Status (WF-06 only) | `approvalCheckCompleted = true` | | |
| If: Validation / Escalation / Is Approved | Correct branch taken | | |
| Set: Draft Status / Block / Error | Fields set | | |
| Code: Write Log | `logEntry.log_id` present | | |
| NoOp: Approval Queue / Stub | NoOp ran — no API call | | |
| Stop and Error (if reached) | Execution halted with message | | |
| Error Trigger (if reached) | Error chain ran | | |

### 4.3 Key Output Fields Observed

Record the actual values from the n8n execution panel for each field:

| Field | Expected Value | Actual Observed Value |
|-------|---------------|-----------------------|
| `approval_status` | `"Draft"` (or `"Approved"` for WF-06 S1) | |
| `approval_valid` (WF-06 only) | `true` (S1) / `false` (S2) | |
| `human_review_required` (WF-04/05) | `true` | |
| `escalation_required` (WF-05) | `false` (S1) / `true` (S2) | |
| `draft_reply` (WF-05) | Non-null (S1) / `null` (S2) | |
| `compliance_notes` (WF-03) | Non-null string | |
| `logEntry.log_id` | String starting `"LOG-"` | |
| `logEntry.status` | `"Success"` | |
| `logWritten` | `true` | |
| `approvalQueueStubReached` | `true` | |
| `publishingBlocked` (WF-06 S2) | `true` | |

---

## Section 5 — Safety Checks (Post-Execution)

Verify after execution completes:

| Safety Check | Result |
|-------------|--------|
| No HTTP request to any real platform API observed in execution panel | `[ ] CONFIRMED   [ ] FAIL — STOP` |
| Workflow remained INACTIVE throughout | `[ ] CONFIRMED   [ ] FAIL — STOP` |
| No real content posted to any platform | `[ ] CONFIRMED   [ ] FAIL — STOP` |
| No real message sent to any customer | `[ ] CONFIRMED   [ ] FAIL — STOP` |
| No real ad campaign created or triggered | `[ ] CONFIRMED   [ ] FAIL — STOP` |
| No real credentials were present or added | `[ ] CONFIRMED   [ ] FAIL — STOP` |
| `human_review_required = true` in output (WF-04/05) | `[ ] CONFIRMED   [ ] N/A` |
| `compliance_notes` present in output (WF-03) | `[ ] CONFIRMED   [ ] N/A` |
| `draft_reply = null` on escalation path (WF-05 S2) | `[ ] CONFIRMED   [ ] N/A` |

---

## Section 6 — Issues and Anomalies

Record any unexpected behavior, errors, or anomalies observed:

| Issue ID | Node Where Observed | Description | Stop Condition Triggered? | Screenshot Filename |
|----------|--------------------|-----------|----|---------------------|
| `EVID-[ID]-ISSUE-001` | | | `[ ] YES   [ ] NO` | |
| `EVID-[ID]-ISSUE-002` | | | `[ ] YES   [ ] NO` | |

If no issues: `NONE`

---

## Section 7 — Evidence References

| Evidence Type | Reference |
|--------------|-----------|
| n8n execution panel screenshot(s) | `[filename or path — note: do not commit to repo]` |
| n8n execution ID | `[if available from n8n panel]` |
| Phase 16 checklist checks completed | `[list check IDs completed, e.g., WF01-01 through WF01-14]` |
| Phase 17 payload file used | `[filename in samples/sandbox/phase_17_test_payloads/]` |
| Filled evidence/log file reference | `[path to filled SANDBOX_EVIDENCE_*.md or Phase 18 log, e.g., logs/SANDBOX_EVIDENCE_WF01_20260529.md]` |

---

## Section 8 — Verdict

| Field | Value |
|-------|-------|
| Overall result | `[ ] PASS   [ ] BLOCKED   [ ] PARTIAL   [ ] NOT_RUN` |
| BLOCKED reason (if applicable) | `[describe stop condition triggered or critical check failed]` |
| PARTIAL details (if applicable) | `[which checks were skipped and why]` |
| Recommended next action | `[what Owner or Builder should do next]` |

---

## Section 9 — Owner Sign-Off

By signing below, the operator confirms that:
- All information in this evidence record is accurate and reflects actual n8n execution panel observations.
- No real credentials were used.
- No real customer data was used.
- No content was posted, no messages sent, no ads spend occurred.
- The workflow remained inactive throughout the session.
- Any issues were recorded accurately in Section 6.

| Field | Value |
|-------|-------|
| Operator initials | `[BB or authorized operator initials]` |
| Sign-off date | `YYYY-MM-DD` |
| Sign-off time | `HH:MM` |
| Confirmation | `[ ] I confirm the above statements are accurate` |

---

*End of Sandbox Execution Evidence Template v1.0*
*Phase 17 — FnB OS V1 / Vị Cuốn Growth OS*
*Fill one copy per workflow per session. Do not commit individual filled copies to the repo without Owner approval.*
