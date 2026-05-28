# Creative Asset Auto Skeleton — Phase 17 Test Payload

**Workflow File:** `n8n/workflows/creative_asset_auto_skeleton.json`
**n8n Workflow Name:** `FnB OS V1 — Creative Asset Auto [SKELETON]`
**Trigger Type:** Manual Trigger (click "Test workflow" in n8n canvas)
**Risk Level:** Standard
**Phase 17 Payload ID:** P17-WF02

> ⚠️ All data below is FAKE/DUMMY. Do not substitute real customer data, real credentials, or real account IDs.

---

## Test Scenario 1 — Facebook Image Creative Brief

**Scenario ID:** P17-WF02-S1
**Purpose:** Verify the creative brief generation node chain executes end-to-end. Confirms Brand Brain stub loads, AI brief stub runs, validation runs, log stub produces a structured entry, and approval queue NoOp is reached. The output must be a creative brief only — not a real image, video, or asset.

### Input Fields

These values are pre-set in the workflow's "Set Input Variables" node. Trigger as-is without modifying the workflow.

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

> Note: REPLACE_WITH_* values are expected stub placeholders — not failures.

### How to Trigger in n8n

1. Open `FnB OS V1 — Creative Asset Auto [SKELETON]` in canvas.
2. Confirm active toggle is OFF (inactive).
3. Click **"Test workflow"**.
4. Observe execution panel node by node.

### Expected Safe Output

| Field | Expected Value | Notes |
|-------|---------------|-------|
| `brandBrainLoaded` | `true` | Brand Brain stub ran |
| `contentDraftGenerated` | `true` | AI Draft stub ran |
| `draft_brief` | Any non-null string OR object | Stub creative brief text |
| `asset_type_confirmed` | `"Image"` or present | Brief targets image only |
| `approval_status` | `"Draft"` | Initial state only |
| `validationPassed` | `true` or `false` | Either acceptable in stub |
| `draft_status` | `"Draft"` or `"Failed"` | Depends on validation branch |
| `logWritten` | `true` | Log stub ran |
| `logEntry.log_id` | String starting with `"LOG-"` | Log ID generated |
| `logEntry.status` | `"Success"` | Stub status |
| `approvalQueueStubReached` | `true` | NoOp reached |

### Forbidden Output

**STOP immediately and record BLOCKED if any of the following appear:**

| Forbidden | Reason |
|-----------|--------|
| Any real image file, URL, or binary output | Must not generate real assets in skeleton |
| Any HTTP request to an image generation API (DALL-E, Midjourney, Stable Diffusion, etc.) | No real AI call in skeleton |
| Any HTTP request to Google Drive, S3, or cloud storage | No real file upload |
| `approval_status` = `"Approved"` or `"Published"` | Auto-approval is forbidden |
| Any real customer PII in output | No real data |

### Approval Gate Expectation

- Output is a creative brief object — not a published asset.
- `approval_status = "Draft"` is the only acceptable approval state.
- NoOp Approval Queue stub is the terminal node — no real approval request is sent anywhere.

### Log Expectation

```json
{
  "log_id": "LOG-YYYYMMDD-CREATIVE-001",
  "timestamp": "<ISO timestamp>",
  "phase": "8",
  "agent_name": "n8n-creative-asset-auto (STUB)",
  "action_type": "Creative Brief Draft",
  "status": "Success",
  "owner_action_required": false
}
```

**Required fields present:** `log_id`, `timestamp`, `phase`, `agent_name`, `action_type`, `status`.

### PASS Condition

- All nodes complete without red error in n8n.
- `logEntry.log_id` present.
- `approvalQueueStubReached = true` present.
- Output is a brief object — not a real image or file.
- No forbidden output observed.

### BLOCK Condition

- Any real image generation API call observed.
- Any real file upload or cloud storage write.
- `approval_status` set to anything other than `"Draft"`.
- Any real credential or PII in output.

---

## Safety Reminders

- Do NOT modify the workflow JSON in the repo.
- Do NOT add real credentials to resolve "Credential not found" warnings.
- Do NOT activate the workflow.
- Do NOT use the draft brief to commission real photography or creative work.
- Record observations in `logs/templates/SANDBOX_EXECUTION_EVIDENCE_TEMPLATE.md`.
