# Phase 20A / 20B — Content Auto Skeleton Manual Sandbox Evidence Log

**Created By:** Claude Code (Builder, AGT-02) — Phase 20A
**Filled By:** Owner (Bo Bao) — Phase 20B
**Log Type:** manual_sandbox_execution
**Workflow:** content_auto_skeleton

> This file is created in Phase 20A as a blank template.
> Owner fills all fields during / after Phase 20B manual sandbox execution.
> Do NOT fill with real customer data, real credentials, or production values.
> After Owner completes Phase 20B, this file must be committed to the repo.

---

## Execution Record

| Field | Value |
|-------|-------|
| `phase` | Phase 20A / 20B |
| `workflow_name` | FnB OS V1 — Content Auto [SKELETON] |
| `workflow_file` | n8n/workflows/content_auto_skeleton.json |
| `execution_type` | manual_sandbox |
| `execution_status` | not_executed_yet |
| `payload_file` | samples/sandbox/phase_17_test_payloads/content_auto_skeleton_test_payload.md |
| `payload_scenario` | P17-WF01-S1 — Standard Facebook Content Request |
| `payload_type` | dummy |
| `active_status_before_run` | [Owner to fill — must be: inactive / false] |
| `active_status_after_run` | [Owner to fill — must be: inactive / false] |
| `credentials_used` | placeholder_or_none |
| `real_customer_data_used` | no |
| `auto_post_executed` | no |
| `auto_reply_executed` | no |
| `ads_spend_executed` | no |
| `production_readiness_claimed` | no |
| `execution_timestamp` | [Owner to fill — format: YYYY-MM-DD HH:MM] |
| `n8n_execution_id` | [Owner to fill — from n8n execution panel or history] |
| `n8n_instance_url` | [Owner to fill — sandbox/localhost URL only] |
| `operator` | Bo Bao |

---

## Node Execution Results

Owner: fill each row after the run. Use the n8n execution panel to click each node and observe output.

| Node Name | Executed | Result | Key Output Observed |
|-----------|---------|--------|-------------------|
| Manual Trigger | [ ] yes / [ ] no | [ ] green / [ ] red / [ ] skipped | — |
| Set Input Variables | [ ] yes / [ ] no | [ ] green / [ ] red / [ ] skipped | brand_name = [fill] |
| Code: Load Brand Brain | [ ] yes / [ ] no | [ ] green / [ ] red / [ ] skipped | brandBrainLoaded = [fill] |
| Code: AI Generate Content Draft | [ ] yes / [ ] no | [ ] green / [ ] red / [ ] skipped | contentDraft.approval_status = [fill] |
| Code: Validate Required Fields | [ ] yes / [ ] no | [ ] green / [ ] red / [ ] skipped | validation_pass = [fill] |
| If: Validation Pass | [ ] yes / [ ] no | [ ] TRUE branch / [ ] FALSE branch | — |
| Set: approval_status = Draft | [ ] yes / [ ] no | [ ] green / [ ] red / [ ] skipped | approval_status = [fill] |
| Code: Write Log Entry | [ ] yes / [ ] no | [ ] green / [ ] red / [ ] skipped | logEntry.log_id = [fill] |
| NoOp: STUB — Send to Approval Queue | [ ] yes / [ ] no | [ ] green / [ ] red / [ ] skipped | approvalQueueStubReached = [fill] |
| Set: Validation Error | [ ] yes / [ ] no | [ ] green / [ ] red / [ ] skipped | error_type = [fill] |
| Stop and Error: Validation Failed | [ ] yes / [ ] no | [ ] green / [ ] red / [ ] skipped | — |
| Error Trigger | [ ] yes / [ ] no | [ ] green / [ ] red / [ ] skipped | — |
| Set: Error Log | [ ] yes / [ ] no | [ ] green / [ ] red / [ ] skipped | — |
| Stop and Error: Workflow Error | [ ] yes / [ ] no | [ ] green / [ ] red / [ ] skipped | — |

---

## Key Output Fields

Owner: copy key values from n8n node output panels.

| Field | Observed Value |
|-------|---------------|
| `brandBrainLoaded` | [fill] |
| `brandBrain.brand_name` | [fill] |
| `contentDraft.approval_status` | [fill — must be "Draft"] |
| `contentDraft.content_id` | [fill] |
| `contentDraft.platform` | [fill] |
| `validation_pass` | [fill] |
| `logEntry.log_id` | [fill — must start with "LOG-"] |
| `logEntry.status` | [fill — expected "Success"] |
| `logWritten` | [fill — expected true] |
| `approvalQueueStubReached` | [fill — expected true if happy path] |

---

## Forbidden Output Checks

Owner: check each item. Mark YES if forbidden item was present (triggers BLOCKED).

| Check | Forbidden Item | Present? |
|-------|---------------|---------|
| FC-01 | HTTP request to `graph.facebook.com` | [ ] YES (BLOCKED) / [ ] NO |
| FC-02 | HTTP request to `api.openai.com` or `api.anthropic.com` | [ ] YES (BLOCKED) / [ ] NO |
| FC-03 | HTTP request to Google Sheets or Supabase | [ ] YES (BLOCKED) / [ ] NO |
| FC-04 | `approval_status` = "Approved" or "Published" | [ ] YES (BLOCKED) / [ ] NO |
| FC-05 | Real PII (customer name, phone, email, ID) in output | [ ] YES (BLOCKED) / [ ] NO |
| FC-06 | Workflow toggled to active=true during run | [ ] YES (BLOCKED) / [ ] NO |

---

## Result Summary

| Field | Value |
|-------|-------|
| `result_summary` | [Owner to fill — describe what happened in 1–3 sentences] |
| `happy_path_completed` | [Owner to fill — yes / no] |
| `validation_branch_taken` | [Owner to fill — TRUE (happy) / FALSE (validation error)] |
| `forbidden_output_found` | [Owner to fill — none / describe if any] |
| `unexpected_behavior` | [Owner to fill — none / describe if any] |

---

## Evidence Files

| Item | Value |
|------|-------|
| `evidence_screenshot_files` | [Owner to fill — list all screenshot filenames] |
| `evidence_template_copy` | [Owner to fill — path of filled evidence template copy if used] |
| `log_id_from_n8n` | [Owner to fill — logEntry.log_id value from output] |

Screenshot naming convention: `phase20b_content_auto_[node_short_name]_[PASS_or_BLOCKED]_[YYYYMMDD].png`

---

## Issues Found

| Issue ID | Node | Description | Severity |
|----------|------|-------------|---------|
| [fill or write NONE] | | | |

---

## Post-Run Safety Confirmation

Owner: confirm each item after the run.

| Check | Confirmed |
|-------|---------|
| Workflow is still INACTIVE after run | [ ] YES / [ ] NO |
| No real credentials were entered during session | [ ] YES / [ ] NO |
| No real customer data was used or observed | [ ] YES / [ ] NO |
| No content was posted to any real platform | [ ] YES / [ ] NO |
| No ads spend occurred | [ ] YES / [ ] NO |
| No customer messages were sent | [ ] YES / [ ] NO |
| Evidence log is filled and screenshots are named | [ ] YES / [ ] NO |

---

## Owner Decision

| Field | Value |
|-------|-------|
| `owner_decision` | [Owner to fill — APPROVED_FOR_PHASE_20B_COMMIT / BLOCKED_NEEDS_FIX / PARTIAL_RERUN_NEEDED] |
| `next_action` | [Owner to fill — e.g. "Commit evidence log and proceed to Phase 21" / "Report blocker to Builder"] |

---

## Owner Sign-Off

```
I, Bo Bao (Owner), confirm that the above observations are accurate,
no real credentials or customer data were used, the workflow remained
inactive throughout, and no content was published or sent.

Owner: ___________________  Date: ___________________  Time: ___________________
```

---

*Log template created by Claude Code (Builder, AGT-02) — Phase 20A — 2026-05-29*
*Log to be filled by Owner (Bo Bao) during Phase 20B manual sandbox execution*
