# CRM Follow-Up Auto Skeleton — Phase 17 Test Payload

**Workflow File:** `n8n/workflows/crm_followup_auto_skeleton.json`
**n8n Workflow Name:** `FnB OS V1 — CRM Follow-Up Auto [SKELETON]`
**Trigger Type:** Manual Trigger (click "Test workflow" in n8n canvas)
**Risk Level:** HIGH — NO REAL MESSAGES TO REAL CUSTOMERS PERMITTED
**Phase 17 Payload ID:** P17-WF04

> ⚠️ CRITICAL: This workflow involves CRM/messaging fields. No real customer names, phone numbers, Zalo IDs, Facebook user IDs, or messenger credentials may be used. All test data is FAKE/DUMMY. If any real messaging API connection is detected, STOP IMMEDIATELY.

---

## ⚠️ Pre-Test Safety Check for WF-04

| Check | Must Be |
|-------|---------|
| Workflow active toggle | OFF / INACTIVE |
| "NO AUTO-SEND" Sticky Note visible on canvas | YES — visible |
| No Zalo credential connected to any node | CONFIRMED |
| No Facebook Messenger credential connected | CONFIRMED |
| No SMS gateway credential connected | CONFIRMED |
| No real customer IDs in workflow nodes | CONFIRMED |

**If any of the above is not confirmed, do NOT trigger this workflow.**

---

## Test Scenario 1 — New Lead CRM Sequence Draft (Facebook Messenger)

**Scenario ID:** P17-WF04-S1
**Purpose:** Verify CRM sequence draft generation runs end-to-end without sending any real message. Confirms `human_review_required = true` is always present in output, no messaging API is called, log stub runs, and approval queue NoOp is reached.

### Input Fields

Pre-set in the workflow's "Set Input Variables" node. Trigger as-is.

```json
{
  "brand_id": "VQ",
  "brand_name": "Vị Cuốn",
  "lead_segment": "New Customer",
  "customer_status": "New Lead",
  "channel": "Facebook Messenger",
  "trigger_event": "REPLACE_WITH_TRIGGER_EVENT"
}
```

> Note: No customer name, phone, or social ID is in this workflow — by design. REPLACE_WITH_* is expected.

### Fake Reference Values (for evidence documentation only — do NOT enter in n8n)

| Field | Fake Dummy Value |
|-------|-----------------|
| Fake Customer Name (docs only) | `Nguyen Test A` |
| Fake Phone (docs only) | `0900000000` |
| Fake Email (docs only) | `sandbox@example.com` |
| Fake Facebook User ID (docs only) | `TEST_FBUID_000001` |
| Fake Zalo User ID (docs only) | `TEST_ZALOID_000001` |
| Fake Segment (docs only) | `New Lead — Sandbox Test` |

**These are documentation-only reference values. Do NOT enter into n8n.**

### How to Trigger in n8n

1. Open `FnB OS V1 — CRM Follow-Up Auto [SKELETON]` in canvas.
2. Confirm "NO AUTO-SEND" Sticky Note is visible.
3. Confirm active toggle is OFF.
4. Click **"Test workflow"**.
5. Observe execution panel — watch for any HTTP Request nodes connecting to messaging APIs.

### Expected Safe Output

| Field | Expected Value | Notes |
|-------|---------------|-------|
| `brandBrainLoaded` | `true` | Brand Brain stub ran |
| `contentDraftGenerated` | `true` | CRM sequence stub ran |
| `human_review_required` | `true` | **Non-negotiable — schema const: true** |
| `draft_sequence` | Non-null object or string | Stub sequence draft |
| `approval_status` | `"Draft"` | Initial state only |
| `no_auto_send_confirmed` | `true` OR field present | Stub safety flag |
| `validationPassed` | `true` or `false` | Either acceptable in stub |
| `logWritten` | `true` | Log stub ran |
| `logEntry.log_id` | String starting with `"LOG-"` | Log ID generated |
| `approvalQueueStubReached` | `true` | NoOp reached |

### Forbidden Output — CRITICAL

**STOP IMMEDIATELY and record BLOCKED if any of the following appear:**

| Forbidden | Why Critical |
|-----------|-------------|
| Any HTTP request to Zalo OA API (`openapi.zalo.me`) | Real Zalo message API — immediate STOP |
| Any HTTP request to Facebook Messenger API (`graph.facebook.com/*/messages`) | Real Messenger API — immediate STOP |
| Any HTTP request to SMS gateway (Twilio, VIETTEL, etc.) | Real SMS — immediate STOP |
| `human_review_required` = `false` or missing | Schema violation — BLOCKED |
| Any real customer name, phone, email, or social ID in output | No real PII — immediate STOP |
| A real PSID (Facebook Page Scoped User ID) | Real user ID — immediate STOP |
| `approval_status` = `"Approved"` or `"Published"` | Auto-approval forbidden |
| Any output suggesting a message was queued or sent | No real messaging — immediate STOP |

### Approval Gate Expectation

- Output is a CRM sequence DRAFT only.
- `human_review_required = true` is mandatory in output.
- `approval_status = "Draft"` is the only acceptable state.
- No message is sent at this stage under any circumstance.
- NoOp Approval Queue stub is terminal.

### Log Expectation

```json
{
  "log_id": "LOG-YYYYMMDD-CRM-001",
  "timestamp": "<ISO timestamp>",
  "phase": "8",
  "agent_name": "n8n-crm-followup-auto (STUB)",
  "action_type": "CRM Follow-Up Draft",
  "status": "Success",
  "errors": null,
  "owner_action_required": false
}
```

**Required fields present:** `log_id`, `timestamp`, `phase`, `agent_name`, `action_type`, `status`.

### PASS Condition

- All nodes complete without red error.
- `human_review_required = true` in output.
- `logEntry.log_id` present.
- `approvalQueueStubReached = true`.
- Zero HTTP requests to Zalo, Messenger, or SMS APIs.
- No real customer data in output.

### BLOCK Condition

- Any Zalo/Messenger/SMS API call detected.
- `human_review_required` is `false` or missing.
- Any real customer PII in output.
- Any indication a message was sent or queued.
- `approval_status` set to anything other than `"Draft"`.

---

## Test Scenario 2 — Lapsed Customer Re-Engagement (Zalo)

**Scenario ID:** P17-WF04-S2
**Purpose:** Secondary test to verify the workflow handles a different `lead_segment` and `channel` without crashing. Same safety expectations apply.

### Input (workflow stub values for this path)

The workflow uses `lead_segment = "New Customer"` and `channel = "Facebook Messenger"` as defaults.
To test a different path, you would need to edit the Set node values in n8n (safe to do within n8n UI — do NOT edit the JSON file in the repo).

**Suggested test via n8n Set node override (in n8n UI only):**
```
lead_segment = "Lapsed Customer"
channel = "Zalo"
trigger_event = "No order in 30 days"
```

> Reminder: Even for Zalo channel, NO real Zalo API connection should be made. The output is a draft only.

### Expected Safe Output (same as Scenario 1)

- `human_review_required = true` always.
- `approval_status = "Draft"` always.
- Log entry produced.
- No messaging API called.

---

## Safety Reminders

- Do NOT modify the workflow JSON in the repo.
- Do NOT add Zalo, Messenger, or SMS credentials.
- Do NOT activate the workflow.
- Do NOT use any draft sequence output to send real messages.
- Record observations in `logs/templates/SANDBOX_EXECUTION_EVIDENCE_TEMPLATE.md`.
