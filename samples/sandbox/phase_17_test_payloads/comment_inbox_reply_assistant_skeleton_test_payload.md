# Comment Inbox Reply Assistant Skeleton — Phase 17 Test Payload

**Workflow File:** `n8n/workflows/comment_inbox_reply_assistant_skeleton.json`
**n8n Workflow Name:** `FnB OS V1 — Comment Inbox Reply Assistant [SKELETON]`
**Trigger Type:** Manual Trigger (click "Test workflow" in n8n canvas)
**Risk Level:** HIGH — NO AUTO-REPLY TO REAL CUSTOMERS / ESCALATION GATE MUST BE VERIFIED
**Phase 17 Payload ID:** P17-WF05

> ⚠️ CRITICAL: This workflow involves customer message handling and a mandatory escalation gate. No real customer messages, real Facebook/TikTok/Instagram comment IDs, or real platform API credentials may be used. All test data is FAKE/DUMMY. Escalation path (complaint/angry) must be tested separately.

---

## ⚠️ Pre-Test Safety Check for WF-05

| Check | Must Be |
|-------|---------|
| Workflow active toggle | OFF / INACTIVE |
| "NO AUTO-REPLY" and escalation warning Sticky Note visible | YES — visible |
| No Facebook comment reply credential connected | CONFIRMED |
| No Instagram credential connected | CONFIRMED |
| No TikTok credential connected | CONFIRMED |
| No real comment IDs or customer IDs in workflow nodes | CONFIRMED |

---

## Test Scenario 1 — Standard Menu Enquiry (Non-Escalation Path)

**Scenario ID:** P17-WF05-S1
**Purpose:** Verify the standard (non-escalation) path runs end-to-end. The customer message is a simple menu question — should route to draft reply generation, not escalation. Confirms `human_review_required = true`, draft reply is generated (not null), and no reply API is called.

### Input Fields

The workflow's "Set Input Variables" node provides:

```json
{
  "brand_id": "VQ",
  "brand_name": "Vị Cuốn",
  "channel": "Facebook Comment",
  "customer_message": "REPLACE_WITH_VERBATIM_CUSTOMER_MESSAGE"
}
```

The stub Code nodes use default values for testing. To test a specific message, you may override `customer_message` in the n8n Set node **within the n8n UI only** (do NOT modify the JSON file in the repo).

**Suggested test message override (in n8n UI Set node):**
```
customer_message = "Menu của quán có những món gì vậy shop?"
```

> This is a FAKE DUMMY message simulating a menu enquiry. No real customer wrote this.

### Fake Reference Values (for evidence documentation only)

| Field | Fake Dummy Value |
|-------|-----------------|
| Fake Commenter Name (docs only) | `Nguyen Test A` |
| Fake Comment ID (docs only) | `TEST_CMT_ID_000001` |
| Fake Post ID (docs only) | `TEST_POST_ID_000001` |
| Fake Page ID (docs only) | `TEST_PAGE_ID_000001` |

**Documentation only. Do NOT enter into n8n.**

### How to Trigger in n8n

1. Open `FnB OS V1 — Comment Inbox Reply Assistant [SKELETON]` in canvas.
2. Confirm warning Sticky Note is visible.
3. Confirm active toggle is OFF.
4. (Optional) Override `customer_message` in Set node within n8n UI.
5. Click **"Test workflow"**.
6. Observe execution panel — specifically check the "If: Escalation Required" node routing.

### Expected Safe Output — Standard (Non-Escalation) Path

| Field | Expected Value | Notes |
|-------|---------------|-------|
| `brandBrainLoaded` | `true` | Brand Brain stub ran |
| `detected_intent` | `"Other"` (stub default) | Intent detection stub ran |
| `sentiment` | `"Neutral"` (stub default) | Sentiment detection stub ran |
| `escalation_required` | `false` | Standard path — no escalation |
| `escalation_reason` | `null` | No escalation reason |
| `draft_reply` | Non-null string | Draft reply generated (NOT null) |
| `human_review_required` | `true` | **Non-negotiable — schema const: true** |
| `approval_status` | `"Draft"` | Initial state |
| `logWritten` | `true` | Log stub ran |
| `logEntry.log_id` | String starting with `"LOG-"` | Log ID generated |
| `approvalQueueStubReached` | `true` | NoOp reached |

### If: Escalation Required Node — Expected Routing

- For Scenario 1 (menu question): `escalation_required = false` → **FALSE branch** taken.
- FALSE branch leads to draft reply generation.
- Check in execution panel that the FALSE output connector is highlighted.

---

## Test Scenario 2 — Escalation Path (Angry / Complaint Message)

**Scenario ID:** P17-WF05-S2
**Purpose:** Verify the escalation path routes correctly. An angry/complaint message must result in `draft_reply = null` and route to Owner-review — NOT to draft generation. This is a critical safety test.

### Suggested Test Message (override in n8n UI Set node)

```
customer_message = "Đồ ăn dở quá, tôi sẽ không quay lại nữa!"
```

> FAKE DUMMY message simulating an angry/complaint message. No real customer wrote this.

### Expected Safe Output — Escalation Path

| Field | Expected Value | Notes |
|-------|---------------|-------|
| `escalation_required` | `true` | Escalation triggered |
| `escalation_reason` | Non-null string explaining escalation | Reason recorded |
| `draft_reply` | `null` | **MUST be null for escalated cases** |
| `human_review_required` | `true` | **Non-negotiable** |
| `approval_status` | `"Escalated"` or `"Draft"` | Escalated state |

### If: Escalation Required Node — Expected Routing

- For Scenario 2 (complaint): `escalation_required = true` → **TRUE branch** taken.
- TRUE branch leads to Owner-review node, NOT to draft generation.
- Check in execution panel that the TRUE output connector is highlighted.
- `draft_reply` must be `null` — never a generated text.

---

## Forbidden Output — CRITICAL (Both Scenarios)

**STOP IMMEDIATELY and record BLOCKED if any of the following appear:**

| Forbidden | Why Critical |
|-----------|-------------|
| Any HTTP request to Facebook Graph API comment reply endpoint | Real reply API — immediate STOP |
| Any HTTP request to Instagram/TikTok/Zalo comment API | Real reply API — immediate STOP |
| `draft_reply` is non-null on the escalation path | Escalation must always produce null draft — BLOCKED |
| `human_review_required` = `false` or missing | Schema violation — BLOCKED |
| Any real customer name, comment ID, or post ID in output | Real data — immediate STOP |
| A real reply posted to any comment on any platform | Immediate STOP — contact Builder |
| `approval_status` = `"Approved"` or `"Published"` | Auto-approval forbidden |

### Approval Gate Expectation

- Both paths produce a DRAFT or ESCALATED state — never Published.
- `human_review_required = true` is mandatory in all outputs.
- No reply is sent at any point.

### Log Expectation

```json
{
  "log_id": "LOG-YYYYMMDD-INBOX-001",
  "timestamp": "<ISO timestamp>",
  "phase": "8",
  "agent_name": "n8n-comment-inbox-reply (STUB)",
  "action_type": "Inbox Reply Draft",
  "status": "Success",
  "owner_action_required": false
}
```

### PASS Condition (Both Scenarios Must Pass)

- Scenario 1: FALSE branch taken, `draft_reply` non-null, `escalation_required = false`.
- Scenario 2: TRUE branch taken, `draft_reply = null`, `escalation_required = true`.
- `human_review_required = true` in both scenarios.
- No comment reply API called in either scenario.
- Log stub ran in both scenarios.

### BLOCK Condition

- Any Facebook/Instagram/TikTok/Zalo comment API call.
- `draft_reply` non-null on escalation path.
- `human_review_required = false` or missing.
- Any real customer data in output.

---

## Safety Reminders

- Do NOT modify the workflow JSON in the repo.
- Do NOT add any comment reply API credentials.
- Do NOT activate the workflow.
- Do NOT use draft output to reply to any real comment.
- Test BOTH scenarios (non-escalation and escalation) before marking WF-05 as PASS.
- Record both scenarios separately in `logs/templates/SANDBOX_EXECUTION_EVIDENCE_TEMPLATE.md`.
