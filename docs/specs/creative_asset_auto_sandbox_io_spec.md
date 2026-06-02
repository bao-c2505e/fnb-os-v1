# Sandbox I/O Specification — creative_asset_auto_skeleton

Spec ID: SPEC-28-CREATIVE-ASSET-SANDBOX-IO
Created By: Claude Code (Builder, AGT-02) — 2026-06-02
Phase: 28 — Creative Asset Auto Sandbox I/O Standardization
Workflow File: `n8n/workflows/creative_asset_auto_skeleton.json`
Workflow Name (n8n): `FnB OS V1 — Creative Asset Auto [SKELETON]`
Status: SKELETON_SANDBOX_ONLY — NOT PRODUCTION READY
Schema Reference: `05_SCHEMAS/creative-brief.schema.json`

---

## 1 — Workflow Identity

| Property | Value |
|----------|-------|
| Workflow file | `n8n/workflows/creative_asset_auto_skeleton.json` |
| n8n display name | `FnB OS V1 — Creative Asset Auto [SKELETON]` |
| n8n sandbox URL | `https://n8n.baon8n.blog/workflow/VW5PDkOOtrjLQBps` |
| Trigger type | Manual Trigger (sandbox only) |
| `active` field | `false` — must remain `false` at all times |
| Risk level | Standard |
| Phase introduced | Phase 8 |
| First sandbox execution | Phase 27 — 2026-06-02 — PASS WITH NOTES |
| I/O spec version | 1.0 (Phase 28) |

---

## 2 — Input Specification

### 2.1 — Trigger

```
Trigger: Manual Trigger (n8n-nodes-base.manualTrigger)
Trigger ID: a2000002-0001-4001-a002-200000000001
Input body: {} (empty — Manual Trigger carries no user-supplied body)
```

### 2.2 — Input Fields (Set Input Variables node)

Node: `Set Input Variables`
Node ID: `a2000002-0002-4001-a002-200000000002`
Node type: `n8n-nodes-base.set` (typeVersion 3)

| Field ID | Field Name | Type | Required | Placeholder? | Sandbox Value | Production Value |
|----------|------------|------|----------|-------------|---------------|-----------------|
| a2-set-001 | `brand_id` | string | YES | NO | `VQ` | `VQ` |
| a2-set-002 | `brand_name` | string | YES | NO | `Vị Cuốn` | `Vị Cuốn` |
| a2-set-003 | `brief_request` | string | YES | YES | `REPLACE_WITH_OWNER_BRIEF_REQUEST` | Owner-supplied brief text |
| a2-set-004 | `asset_type` | string | YES | NO | `Photo` | Owner-selected asset type |
| a2-set-005 | `platform` | string | YES | NO | `Facebook` | Owner-selected platform |
| a2-set-006 | `format` | string | YES | NO | `1:1 square 1080x1080` | Owner-selected format |
| a2-set-007 | `objective` | string | YES | NO | `Engagement` | Owner-selected objective |

### 2.3 — Input Validation Rules

| Rule ID | Rule | Enforcement |
|---------|------|-------------|
| IV-01 | `brand_id` must be `VQ` in sandbox | Manual check |
| IV-02 | `brand_name` must be `Vị Cuốn` in sandbox | Manual check |
| IV-03 | `brief_request` must not contain real customer PII | Manual check |
| IV-04 | `brief_request` must not contain real API endpoints or credentials | Manual check |
| IV-05 | No input field may contain an API key, token, or password | Manual check + CI scan |
| IV-06 | `asset_type` must be one of: Photo, Video, Carousel, Story, Reel | Recommended |
| IV-07 | `platform` must be one of: Facebook, Instagram, TikTok, Zalo | Recommended |
| IV-08 | No real campaign names linked to active ad spend | Manual check |

### 2.4 — Known Skeleton UI Behavior

In n8n, when the `Manual Trigger` fires, it passes an empty JSON object `{}` as the incoming item. The `Set Input Variables` node then generates its own output fields from the `assignments.assignments` array. In some n8n versions, the execution panel may show:

> "No fields - item(s) exist, but they're empty."

This refers to the **input** to the Set node (the empty trigger body) — not the **output** of the Set node. The node still applies its assignments and produces the expected output fields. This is confirmed acceptable behavior as of Phase 27 (PASS WITH NOTES, 2026-06-02).

---

## 3 — Node Chain (Happy Path)

| Step | Node Name | Node Type | Expected Output Signal |
|------|-----------|-----------|----------------------|
| 1 | Manual Trigger | manualTrigger | `{}` (empty body — expected) |
| 2 | Set Input Variables | set | `brand_id, brand_name, brief_request, asset_type, platform, format, objective` |
| 3 | Code: Load Brand Brain | code | `brandBrain{}`, `brandBrainLoaded=true` |
| 4 | Code: AI Generate Creative Brief | code | `creativeBrief{}`, `aiCallCompleted=true` |
| 5 | Code: Validate Required Fields | code | `validation_pass=true`, `validation_errors=[]` |
| 6 | If: Validation Pass | if | Routes to TRUE branch |
| 7 | Set: approval_status = Draft | set | `approval_status="Draft"` |
| 8 | Code: Write Log Entry | code | `logEntry{}`, `logWritten=true` |
| 9 | NoOp: STUB — Send to Approval Queue | noOp | End of happy path — `approvalQueueStubReached=true` (inferred) |

### 3.1 — Validation Failure Path

Triggered if `validation_pass = false` (FALSE branch from If node):

| Step | Node Name | Expected Behavior |
|------|-----------|------------------|
| 6 (FALSE) | Set: Validation Error | Sets `error_type="SCHEMA_VALIDATION_FAIL"`, `owner_action_required=true` |
| 7 (FALSE) | Stop and Error: Validation Failed | Workflow stops with error message |

### 3.2 — Error Handler Path

Triggered by unhandled workflow errors:

| Step | Node Name | Expected Behavior |
|------|-----------|------------------|
| E1 | Error Trigger | Fires on unhandled error |
| E2 | Set: Error Log | Sets `error_type="WORKFLOW_ERROR"`, `owner_action_required=true` |
| E3 | Stop and Error: Workflow Error | Workflow stops with error message |

---

## 4 — Output Specification

### 4.1 — brandBrain Object

Produced by: `Code: Load Brand Brain`
Source: Hardcoded stub (skeleton) — no real data source connected

```json
{
  "brand_name": "Vị Cuốn",
  "brand_positioning": "REPLACE_WITH_BRAND_POSITIONING",
  "target_customer": "REPLACE_WITH_TARGET_CUSTOMER",
  "menu_items": "REPLACE_WITH_MENU_ITEMS",
  "price_range": "REPLACE_WITH_PRICE_RANGE",
  "address": "REPLACE_WITH_ADDRESS",
  "opening_hours": "REPLACE_WITH_OPENING_HOURS",
  "key_offers": "REPLACE_WITH_KEY_OFFERS",
  "tone_of_voice": "REPLACE_WITH_TONE_OF_VOICE",
  "forbidden_claims": "REPLACE_WITH_FORBIDDEN_CLAIMS",
  "approval_status": "REPLACE_WITH_APPROVAL_STATUS"
}
```

| Field | Expected Value | Type |
|-------|---------------|------|
| `brandBrainLoaded` | `true` | boolean |
| All `REPLACE_WITH_*` fields | Placeholder strings | string |

### 4.2 — creativeBrief Object

Produced by: `Code: AI Generate Creative Brief`
Schema: `05_SCHEMAS/creative-brief.schema.json`
Source: Hardcoded stub (skeleton) — no real AI API call

**Required fields (from schema):**

| Field | Sandbox Value | Required |
|-------|--------------|----------|
| `brief_id` | `CB-VQ-STUB-001` | YES |
| `brand_id` | `VQ` | YES |
| `brand_name` | `Vị Cuốn` | YES |
| `asset_type` | `Photo` | YES |
| `platform` | `Facebook` | YES |
| `format` | `1:1 square 1080x1080` | YES |
| `objective` | `Engagement` | YES |
| `concept` | `STUB_CONCEPT — ...` | YES |
| `visual_direction` | `STUB_VISUAL_DIRECTION — ...` | YES |
| `approval_status` | `Draft` | YES |
| `created_by_agent` | `n8n-creative-asset-auto (STUB)` | YES |
| `created_at` | ISO timestamp | YES |

**Optional fields (null in skeleton):**

| Field | Sandbox Value |
|-------|--------------|
| `scene_description` | `null` |
| `copy_overlay` | `null` |
| `ai_tool_prompt` | `null` |

| Signal Field | Expected Value |
|-------------|----------------|
| `aiCallCompleted` | `true` |

### 4.3 — Validation Result

Produced by: `Code: Validate Required Fields`

| Field | Expected Value (PASS path) |
|-------|---------------------------|
| `validation_pass` | `true` |
| `validation_errors` | `[]` (empty array) |

### 4.4 — Approval Status (Top-Level)

Set by: `Set: approval_status = Draft`

| Field | Expected Value |
|-------|---------------|
| `approval_status` | `"Draft"` |

### 4.5 — Log Entry

Produced by: `Code: Write Log Entry`
Schema reference: `logs-entry.schema.json` (if present)

| Field | Expected Value |
|-------|---------------|
| `logEntry.log_id` | `LOG-<YYYYMMDD>-STUB-001` |
| `logEntry.timestamp` | ISO timestamp |
| `logEntry.phase` | `"8"` |
| `logEntry.agent_name` | `"n8n-creative-asset-auto (STUB)"` |
| `logEntry.action_type` | `"Creative Brief Draft"` |
| `logEntry.status` | `"Success"` |
| `logEntry.owner_action_required` | `false` |
| `logWritten` | `true` |

### 4.6 — Approval Queue Stub

Produced by: `NoOp: STUB — Send to Approval Queue`

| Signal | Expected Value |
|--------|---------------|
| `approvalQueueStubReached` | `true` (inferred — node reached without error) |
| Real approval queue write | ABSENT — NoOp is a stub only |

---

## 5 — Forbidden Outputs

The following outputs must be **absent** from all sandbox runs:

| Output | Description | If Present |
|--------|-------------|-----------|
| Real image file | PNG, JPG, WEBP, etc. in output | IMMEDIATE STOP |
| Real video file | MP4, MOV, etc. in output | IMMEDIATE STOP |
| Real asset URL | URL to generated image/video | IMMEDIATE STOP |
| Anthropic API response | Evidence of real Claude API call | IMMEDIATE STOP |
| Google API response | Sheets, Drive, or other Google API | IMMEDIATE STOP |
| Facebook/Meta API response | Pages, Ads, or Messenger API | IMMEDIATE STOP |
| TikTok API response | Content or Ads API | IMMEDIATE STOP |
| Zalo API response | Message or content API | IMMEDIATE STOP |
| `active: true` in workflow JSON | Activation of workflow | IMMEDIATE STOP |
| Real customer name/phone/email | PII in output | IMMEDIATE STOP |
| Ad campaign creation | Any Meta/TikTok ad object | IMMEDIATE STOP |
| Social post published | Confirmed post on any platform | IMMEDIATE STOP |
| `approval_status` ≠ `"Draft"` | e.g., `"Approved"`, `"Published"` | STOP — investigate |

---

## 6 — Pass/Fail Summary Table

| Check ID | Check | PASS | PASS WITH NOTES | FAIL |
|----------|-------|------|----------------|------|
| PF-01 | `brandBrainLoaded = true` | YES | — | NO |
| PF-02 | `aiCallCompleted = true` | YES | — | NO |
| PF-03 | `validation_pass = true` | YES | — | NO |
| PF-04 | `approval_status = "Draft"` | YES | — | NO or absent |
| PF-05 | `logWritten = true` | YES | — | NO |
| PF-06 | `approvalQueueStubReached = true` | YES | — | NO |
| PF-07 | Workflow INACTIVE after run | YES | — | ACTIVE |
| PF-08 | No real image/binary in output | ABSENT | — | PRESENT |
| PF-09 | No real API call evidence | ABSENT | — | PRESENT |
| PF-10 | No auto-post | ABSENT | — | PRESENT |
| PF-11 | Set Input Variables UI empty display | — | Downstream OK | Downstream broken |
| PF-12 | `logEntry.log_id` recorded | YES | Not recorded but logWritten=true | — |
| PF-13 | Screenshots submitted | YES | Not submitted (verbal confirm) | — |

---

## 7 — Credential and Secret Constraints

| Constraint | Value |
|-----------|-------|
| Anthropic API key | NONE — `REPLACE_WITH_ANTHROPIC_API_KEY` |
| Google Sheets credential | NONE — `REPLACE_WITH_GOOGLE_SHEETS_CREDENTIAL` |
| Supabase credential | NONE — `REPLACE_WITH_SUPABASE_CREDENTIAL` |
| Any other credential | NONE |
| CI secret scan | Must pass `scripts/check_no_secrets.py` — CLEAN |

---

## 8 — Version History

| Version | Date | Author | Change |
|---------|------|--------|--------|
| 1.0 | 2026-06-02 | Claude Code (Builder, AGT-02) | Initial spec — Phase 28 |
