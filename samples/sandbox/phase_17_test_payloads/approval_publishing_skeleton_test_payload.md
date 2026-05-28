# Approval Publishing Skeleton — Phase 17 Test Payload

**Workflow File:** `n8n/workflows/approval_publishing_skeleton.json`
**n8n Workflow Name:** `FnB OS V1 — Approval and Publishing Gate [SKELETON]`
**Trigger Type:** Webhook (use n8n test webhook — see instructions below)
**Risk Level:** HIGH — APPROVAL GATE + 5-BRANCH PUBLISH ROUTING — ALL PUBLISH STUBS MUST REMAIN NoOp
**Phase 17 Payload ID:** P17-WF06

> ⚠️ CRITICAL: This is the approval gate workflow. All 5 publish branches must remain NoOp stubs. No content may be posted, no archive created, no ad campaign launched, no CRM message sent, no comment reply posted — under any circumstances during Phase 17 testing.

---

## ⚠️ Pre-Test Safety Check for WF-06

| Check | Must Be |
|-------|---------|
| Workflow active toggle | OFF / INACTIVE |
| "DO NOT ACTIVATE" Sticky Note visible on canvas | YES — visible |
| No Facebook/Instagram/TikTok/Zalo publish credential connected | CONFIRMED |
| No Google Drive credential connected | CONFIRMED |
| No Meta Ads / TikTok Ads credential connected | CONFIRMED |
| No messaging credential connected | CONFIRMED |
| Webhook path is `REPLACE_WITH_WEBHOOK_PATH` (not a real path) | CONFIRMED |

---

## ⚠️ How to Trigger WF-06 (Webhook Workflow)

WF-06 uses a **Webhook trigger** — not a Manual Trigger. To test without activating:

1. Open `FnB OS V1 — Approval and Publishing Gate [SKELETON]` in canvas.
2. Click on the **"Webhook: Receive Approval Request"** node.
3. n8n shows a **"Test URL"** tab in the node settings — use this URL.
4. The test URL is a **temporary sandbox URL** — valid only while you have the workflow in test mode.
5. **Do NOT expose this URL to public internet.** Use it from your local machine or sandbox network only.
6. Send the dummy JSON payloads below to this test URL using a tool like Postman, curl, or n8n's built-in "Send test event" option.
7. Observe the execution panel.

> n8n test webhooks do NOT require `active: true`. The workflow must remain inactive.

---

## Test Scenario 1 — Approved Item (Content Output)

**Scenario ID:** P17-WF06-S1
**Purpose:** Verify the APPROVED path routes correctly. An approved dummy payload should pass the `If: Is Approved` check, route through `Switch: Item Type` to the correct branch, reach the NoOp publish stub (without calling any real API), and produce an approval log entry.

### Dummy Payload — Approved Content Output

Send this JSON body to the WF-06 test webhook URL:

```json
{
  "approval_status": "Approved",
  "owner_decision": "Approved",
  "item_type": "Content Output",
  "item_id": "TEST-ITEM-001",
  "brand_name": "Vị Cuốn (SANDBOX TEST)",
  "platform": "Facebook",
  "draft_content": "SANDBOX TEST CONTENT — NOT FOR PUBLISHING",
  "session_id": "TEST-SESSION-P17-WF06-S1"
}
```

> `owner_decision = "Approved"` simulates Owner having manually approved this item. In production, only Owner (Bo Bao) may set this field.

### Expected Safe Output — Approved Path

| Field | Expected Value | Notes |
|-------|---------------|-------|
| `approval_status` | `"Approved"` | From input |
| `approval_valid` | `true` | Computed by Code node |
| `approval_block_reason` | `null` | No block (approved) |
| `approvalCheckCompleted` | `true` | Check node ran |
| If: Is Approved | TRUE branch taken | Correct routing |
| Switch: Item Type | "Content Output" branch taken | Correct routing |
| NoOp stub | Executed — no API call | Publish stub remains NoOp |
| `logEntry.log_id` | String starting with `"LOG-"` | Approval log generated |
| `logEntry.status` | `"Success"` | Log status |
| `approvalLogged` | `true` | Log written |

### If: Is Approved Node — Expected Routing for S1

- `approval_valid = true` → **TRUE branch** (approved path) taken.
- TRUE branch leads to `Switch: Item Type`.
- Switch routes to "Content Output" NoOp stub.
- Check that NoOp stub runs without any HTTP call.

---

## Test Scenario 2 — Not Approved Item (Draft Status)

**Scenario ID:** P17-WF06-S2
**Purpose:** Verify the NOT APPROVED path routes correctly. A non-approved payload should fail the `If: Is Approved` check, route to the block path, log a block reason, and stop with an error. No publish action should occur.

### Dummy Payload — Not Approved (Draft)

```json
{
  "approval_status": "Draft",
  "owner_decision": null,
  "item_type": "Content Output",
  "item_id": "TEST-ITEM-002",
  "brand_name": "Vị Cuốn (SANDBOX TEST)",
  "session_id": "TEST-SESSION-P17-WF06-S2"
}
```

### Expected Safe Output — Not Approved Path

| Field | Expected Value | Notes |
|-------|---------------|-------|
| `approval_valid` | `false` | Correctly identified as not approved |
| `approval_block_reason` | Non-null string | Block reason recorded |
| If: Is Approved | FALSE branch taken | Correct routing |
| `block_reason` | Non-null string | Set by block node |
| `owner_action_required` | `true` | Owner must approve |
| `publishingBlocked` | `true` | Confirmed blocked |
| Stop and Error node | Reached and fires | Execution halted |

> Note: The workflow will show a "red" / error state in n8n when Stop and Error fires. This is the **expected correct behavior** for a non-approved item — it is NOT a test failure.

---

## Test Scenarios 3–6 — Additional Item Type Routing (Optional)

**Scenario IDs:** P17-WF06-S3 through P17-WF06-S6
**Purpose:** Verify the Switch: Item Type node routes to the correct NoOp stub for each of the 5 item types.

Use the same approved payload structure as Scenario 1, changing only `item_type`:

| Scenario | item_type value | Expected Switch Branch |
|----------|----------------|----------------------|
| S3 | `"Creative Brief"` | "Creative Brief" branch → NoOp: Archive Creative Brief |
| S4 | `"Ads Pack"` | "Ads Pack" branch → NoOp: Launch Ads Campaign |
| S5 | `"CRM Follow-Up"` | "CRM Follow-Up" branch → NoOp: Send CRM Messages |
| S6 | `"Comment Reply"` | "Comment Reply" branch → NoOp: Post Reply to Channel |

For each: confirm the correct NoOp stub is reached and no real API is called.

---

## Forbidden Output — CRITICAL (All Scenarios)

**STOP IMMEDIATELY and record BLOCKED if any of the following appear:**

| Forbidden | Why Critical |
|-----------|-------------|
| Any HTTP request to `graph.facebook.com` (posting) | Real Facebook post API — immediate STOP |
| Any HTTP request to Instagram publish API | Real publish — immediate STOP |
| Any HTTP request to TikTok content API | Real publish — immediate STOP |
| Any HTTP request to Zalo content API | Real publish — immediate STOP |
| Any HTTP request to Google Drive file create/upload | Real archive — immediate STOP |
| Any HTTP request to Meta Ads campaign creation endpoint | Real ads — immediate STOP |
| Any HTTP request to TikTok Ads campaign endpoint | Real ads — immediate STOP |
| Any HTTP request to messaging API (Zalo OA, Messenger) | Real message — immediate STOP |
| Any HTTP request to comment reply API | Real reply — immediate STOP |
| `approval_status` set to `"Approved"` by the workflow itself | Auto-approval forbidden (Owner-only) |
| Any real post ID, page ID, ad account ID, or customer ID | Real data — immediate STOP |

### Approval Gate Expectation

- For Scenario 1: `approval_valid = true` → switch → NoOp stub → approval log.
- For Scenario 2: `approval_valid = false` → block path → block log → Stop and Error.
- ALL 5 NoOp publish stubs must remain NoOp — zero real API calls.
- `owner_decision = "Approved"` in test data simulates Owner action only — it does NOT authorize any real platform action.

### Log Expectation (Approved Path)

```json
{
  "log_id": "LOG-YYYYMMDD-APPR-001",
  "timestamp": "<ISO timestamp>",
  "phase": "8",
  "agent_name": "n8n-approval-publishing-gate (STUB)",
  "action_type": "Approval Decision",
  "status": "Success",
  "approvalLogged": true,
  "owner_action_required": false
}
```

### Log Expectation (Block Path)

```json
{
  "log_id": "LOG-YYYYMMDD-BLOCK-001",
  "timestamp": "<ISO timestamp>",
  "phase": "8",
  "agent_name": "n8n-approval-publishing-gate (STUB)",
  "action_type": "Approval Decision",
  "status": "Blocked",
  "publishingBlocked": true,
  "owner_action_required": true
}
```

### PASS Condition (Scenarios 1 + 2 Both Required)

- Scenario 1: TRUE branch, correct Switch routing, NoOp stub reached, approval log produced. Zero platform API calls.
- Scenario 2: FALSE branch, block log produced, Stop and Error fired. Zero publish actions.
- All 5 item_type branches tested (S3–S6 optional but recommended).
- No forbidden output in any scenario.

### BLOCK Condition

- Any real publish/archive/ads/message/reply API call detected.
- `approval_valid` computed incorrectly for either test payload.
- NoOp stub replaced with a real action node.
- Workflow found to be active.

---

## Safety Reminders

- Do NOT modify the workflow JSON in the repo.
- Do NOT add any platform, ads, drive, or messaging credentials.
- Do NOT activate the workflow.
- Do NOT use the test webhook URL beyond the sandbox session — it is temporary.
- Do NOT share the test webhook URL — it is local sandbox only.
- Test BOTH Scenario 1 (approved) and Scenario 2 (not approved) before marking WF-06 as PASS.
- Record all scenarios in `logs/templates/SANDBOX_EXECUTION_EVIDENCE_TEMPLATE.md`.
