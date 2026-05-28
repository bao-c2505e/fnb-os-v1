# Ads Pack Auto Skeleton — Phase 17 Test Payload

**Workflow File:** `n8n/workflows/ads_pack_auto_skeleton.json`
**n8n Workflow Name:** `FnB OS V1 — Ads Pack Auto [SKELETON]`
**Trigger Type:** Manual Trigger (click "Test workflow" in n8n canvas)
**Risk Level:** HIGH — NO ADS SPEND PERMITTED UNDER ANY CIRCUMSTANCE
**Phase 17 Payload ID:** P17-WF03

> ⚠️ CRITICAL: This workflow involves ads-related fields. Absolutely no real ad account IDs, Meta Ads credentials, TikTok Ads credentials, or budget values may be entered. All test data is FAKE/DUMMY. If any real ads API connection is detected, STOP IMMEDIATELY.

---

## ⚠️ Pre-Test Safety Check for WF-03

Before triggering this workflow, confirm all of the following:

| Check | Must Be |
|-------|---------|
| Workflow active toggle | OFF / INACTIVE |
| "NO ADS SPEND" Sticky Note visible on canvas | YES — visible |
| No Meta Ads credential connected to any node | CONFIRMED |
| No TikTok Ads credential connected to any node | CONFIRMED |
| No budget value is configured anywhere | CONFIRMED |

**If any of the above is not confirmed, do NOT trigger this workflow.**

---

## Test Scenario 1 — Facebook Ads Pack Draft (Awareness / Top of Funnel)

**Scenario ID:** P17-WF03-S1
**Purpose:** Verify the ads pack draft node chain executes without triggering any real ads API. Confirms Brand Brain stub loads, AI ads pack stub runs, compliance_notes field is present in output, validation runs, log stub executes, and approval queue NoOp is reached.

### Input Fields

These values are pre-set in the workflow's "Set Input Variables" node. Trigger as-is.

```json
{
  "brand_id": "VQ",
  "brand_name": "Vị Cuốn",
  "campaign_objective": "Awareness",
  "platform": "Facebook Ads",
  "funnel_stage": "Top of Funnel (TOF)",
  "target_audience": "REPLACE_WITH_TARGET_AUDIENCE",
  "offer": "[OWNER_TO_PROVIDE_OFFER]"
}
```

> Note: REPLACE_WITH_* and [OWNER_TO_PROVIDE_OFFER] are expected stub placeholders. Do NOT replace with real values.
> Note: No real Ad Account ID, Pixel ID, or Budget is present — as required.

### Fake Reference Values (for documentation purposes only — do NOT enter in n8n)

If the evidence template requires you to document what test data was used:

| Field | Fake Dummy Value |
|-------|-----------------|
| Fake Ad Account ID (for docs) | `ACT-TEST-000001` |
| Fake Campaign Name (for docs) | `TEST-CAMP-AWARENESS-001` |
| Fake Budget (for docs) | `0 VND — TEST ONLY — NO REAL SPEND` |

**These values are for documentation purposes only. Do NOT enter them into n8n nodes.**

### How to Trigger in n8n

1. Open `FnB OS V1 — Ads Pack Auto [SKELETON]` in canvas.
2. Confirm "NO ADS SPEND" Sticky Note is visible.
3. Confirm active toggle is OFF.
4. Click **"Test workflow"**.
5. Observe execution panel — watch for any HTTP Request nodes firing.

### Expected Safe Output

| Field | Expected Value | Notes |
|-------|---------------|-------|
| `brandBrainLoaded` | `true` | Brand Brain stub ran |
| `contentDraftGenerated` | `true` | AI ads pack stub ran |
| `compliance_notes` | Non-null string | **Required field** — compliance reminder |
| `approval_status` | `"Draft"` | Initial state only |
| `no_ads_spend_confirmed` | `true` OR field present | Stub safety confirmation |
| `validationPassed` | `true` or `false` | Either acceptable in stub |
| `logWritten` | `true` | Log stub ran |
| `logEntry.log_id` | String starting with `"LOG-"` | Log ID generated |
| `approvalQueueStubReached` | `true` | NoOp reached |

### Forbidden Output — CRITICAL

**STOP IMMEDIATELY and record BLOCKED if any of the following appear:**

| Forbidden | Why Critical |
|-----------|-------------|
| Any HTTP request to `graph.facebook.com/v*/act_*/campaigns` | Real Meta Ads API call — immediate STOP |
| Any HTTP request to `business-api.tiktok.com` | Real TikTok Ads API call — immediate STOP |
| Any HTTP request to `ads.zalo.me` | Real Zalo Ads API call — immediate STOP |
| Any output containing a real Ad Account ID (format: `act_XXXXXXXXXXXXXXX`) | Real account ID — immediate STOP |
| Any output containing a real Pixel ID | Real tracking pixel — immediate STOP |
| Any real budget amount committed or queued | No real spend — immediate STOP |
| `approval_status` = `"Approved"` or `"Published"` | Auto-approval forbidden |
| `compliance_notes` missing or null | Required field — BLOCKED |
| Any real customer PII | No real data |

### Approval Gate Expectation

- Output is an ads pack DRAFT only.
- `approval_status = "Draft"` is the only acceptable state.
- No launch, schedule, or submit action may occur.
- NoOp Approval Queue stub is terminal — no real approval request goes anywhere.

### Log Expectation

```json
{
  "log_id": "LOG-YYYYMMDD-ADS-001",
  "timestamp": "<ISO timestamp>",
  "phase": "8",
  "agent_name": "n8n-ads-pack-auto (STUB)",
  "action_type": "Ads Pack Draft",
  "status": "Success",
  "errors": null,
  "owner_action_required": false
}
```

**Required fields present:** `log_id`, `timestamp`, `phase`, `agent_name`, `action_type`, `status`.

### PASS Condition

- All nodes complete without red error.
- `compliance_notes` present and non-null.
- `logEntry.log_id` present.
- `approvalQueueStubReached = true`.
- Zero HTTP requests to any ads API observed in execution log.
- No real budget, account ID, or pixel ID in output.

### BLOCK Condition

- Any Meta/TikTok/Zalo Ads API request detected in execution panel.
- `compliance_notes` missing.
- Any real Ad Account ID, budget, or pixel in output.
- `approval_status` set to anything other than `"Draft"`.
- Workflow found active.

---

## Safety Reminders

- Do NOT modify the workflow JSON in the repo.
- Do NOT add Meta Ads, TikTok Ads, or Zalo Ads credentials.
- Do NOT activate the workflow.
- Do NOT use the draft ads pack output to create a real campaign.
- Record observations in `logs/templates/SANDBOX_EXECUTION_EVIDENCE_TEMPLATE.md`.
- If you see any signs of real API connection, STOP and report to Builder immediately.
