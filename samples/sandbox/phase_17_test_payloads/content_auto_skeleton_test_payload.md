# Content Auto Skeleton — Phase 17 Test Payload

**Workflow File:** `n8n/workflows/content_auto_skeleton.json`
**n8n Workflow Name:** `FnB OS V1 — Content Auto [SKELETON]`
**Trigger Type:** Manual Trigger (click "Test workflow" in n8n canvas)
**Risk Level:** Standard
**Phase 17 Payload ID:** P17-WF01

> ⚠️ All data below is FAKE/DUMMY. Do not substitute real customer data, real credentials, or real account IDs.

---

## Test Scenario 1 — Standard Facebook Content Request

**Scenario ID:** P17-WF01-S1
**Purpose:** Verify the full node chain executes end-to-end with a standard content request. Confirms Brand Brain stub loads, AI draft stub runs, validation passes, log stub produces a structured log entry, and approval queue NoOp is reached.

### Input Fields

These values are pre-set in the workflow's "Set Input Variables" node. The Manual Trigger carries no data — the Set node injects these. You do not need to modify the workflow to test with these values. The workflow uses its own stub values. To override for a specific test, you would need to edit the Set node — but for Phase 17, **do not modify the workflow JSON**. Simply trigger the workflow as-is and observe the output.

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

> Note: These are the stub values already in the workflow. The REPLACE_WITH_* strings are expected placeholders — not failures.

### How to Trigger in n8n

1. Open `FnB OS V1 — Content Auto [SKELETON]` in n8n canvas.
2. Confirm active toggle is OFF (inactive).
3. Click **"Test workflow"** button (or equivalent in your n8n version).
4. Observe the execution panel — each node should show green (success) or its result.

### Expected Safe Output

| Field | Expected Value | Notes |
|-------|---------------|-------|
| `brandBrainLoaded` | `true` | Confirms Brand Brain stub ran |
| `brandBrain.brand_name` | `"Vị Cuốn"` | Stub value |
| `brandBrain.brand_positioning` | `"REPLACE_WITH_BRAND_POSITIONING"` | Expected placeholder |
| `contentDraftGenerated` | `true` | Confirms AI Draft stub ran |
| `draft_content` | Any non-null string | Stub draft text |
| `approval_status` | `"Draft"` | Correct initial state |
| `validationPassed` | `true` or `false` | Either is acceptable in stub |
| `draft_status` | `"Draft"` or `"Failed"` | Depends on validation branch taken |
| `logWritten` | `true` | Confirms log stub ran |
| `logEntry.log_id` | String starting with `"LOG-"` | Confirms log ID was generated |
| `logEntry.status` | `"Success"` | Stub log status |
| `approvalQueueStubReached` | `true` | Confirms NoOp approval queue ran |

### Forbidden Output

**If any of the following appear in the n8n execution panel, STOP immediately and record BLOCKED:**

| Forbidden | Reason |
|-----------|--------|
| Any HTTP request to `graph.facebook.com` | Real Facebook API call — must not happen |
| Any HTTP request to `api.openai.com` or `api.anthropic.com` | Real AI API call — must not happen in skeleton |
| Any HTTP request to Google Sheets or Supabase | Real data write — must not happen |
| `approval_status` = `"Approved"` or `"Published"` | Approval can only be set by Owner manually — never auto-set |
| Any real phone number, email, or customer ID in output | Real PII — must not appear |
| `active: true` in workflow settings | Workflow must remain inactive |

### Approval Gate Expectation

- This workflow sends output to the **NoOp Approval Queue stub** — not to the Approval Publishing workflow.
- The approval queue is a placeholder: no real approval request is sent.
- `approval_status` in output should be `"Draft"` (initial state only).
- Owner must never see `approval_status = "Approved"` generated automatically.

### Log Expectation

The `Code: Write Log` node should produce a `logEntry` object with these fields present:

```json
{
  "log_id": "LOG-YYYYMMDD-CONTENT-001",
  "timestamp": "<ISO timestamp>",
  "phase": "8",
  "agent_name": "n8n-content-auto (STUB)",
  "action_type": "Content Draft",
  "input_ref": "<some value>",
  "output_ref": "<some value>",
  "status": "Success",
  "summary": "<some text>",
  "errors": null,
  "next_action": "<some text>",
  "owner_action_required": false
}
```

**Required fields that must be present:** `log_id`, `timestamp`, `phase`, `agent_name`, `action_type`, `status`.

### PASS Condition

- All nodes in the chain complete without a red error node in n8n.
- `logEntry.log_id` is present in execution panel output.
- `approvalQueueStubReached = true` is present.
- No forbidden output observed.
- No real API call in execution log.

### BLOCK Condition

- Any node shows a connection error to a real external API.
- `approval_status` is set to anything other than `"Draft"`.
- Any real customer data or credential appears in output.
- Workflow was found to be `active: true`.

---

## Safety Reminders

- Do NOT modify the workflow JSON in the repo.
- Do NOT add real credentials to resolve "Credential not found" warnings — these are expected.
- Do NOT activate the workflow.
- Do NOT post the draft output to any real platform.
- Record your observations in `logs/templates/SANDBOX_EXECUTION_EVIDENCE_TEMPLATE.md`.
