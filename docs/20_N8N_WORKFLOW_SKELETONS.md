# 20 — n8n Workflow Skeletons

Phase: 8 — n8n Importable Workflow Skeletons
Created By: Claude Code (Builder, AGT-02) — 2026-05-28
Status: SKELETON_IMPORTABLE — Not production. No execution. active=false.

---

## Purpose

This document explains the Phase 8 n8n workflow skeleton files created in `n8n/workflows/`. These files are importable n8n JSON skeletons for the six core FnB OS V1 automation modules.

**What these skeletons are:**
- Importable n8n workflow JSON files
- Visual workflow maps showing node structure, approval gates, logging steps, and error chains
- Placeholders for AI calls, credentials, and production endpoints
- Safe to import — no real actions are triggered

**What these skeletons are NOT:**
- Production-ready workflows
- Connected to any live API, platform, or credential
- Workflows that will auto-publish, auto-send, or auto-spend
- Workflows that require Owner action after import (they are inactive by default)

---

## Workflow Files

| File | Module | Schema | Trigger |
|------|--------|--------|---------|
| `n8n/workflows/content_auto_skeleton.json` | Content Auto | `content-output.schema.json` | Manual Trigger |
| `n8n/workflows/creative_asset_auto_skeleton.json` | Creative Asset Auto | `creative-brief.schema.json` | Manual Trigger |
| `n8n/workflows/ads_pack_auto_skeleton.json` | Ads Pack Auto | `ads-pack.schema.json` | Manual Trigger |
| `n8n/workflows/crm_followup_auto_skeleton.json` | CRM Follow-Up Auto | `crm-followup.schema.json` | Manual Trigger |
| `n8n/workflows/comment_inbox_reply_assistant_skeleton.json` | Comment Inbox Reply Assistant | `comment-inbox-reply.schema.json` | Manual Trigger |
| `n8n/workflows/approval_publishing_skeleton.json` | Approval and Publishing Gate | `approval-status.schema.json` | Webhook (placeholder) |

---

## How to Import into n8n

### Step 1 — Open your n8n instance

Open your self-hosted n8n instance in a browser. Do not import into a shared or production n8n instance until Owner and Codex have reviewed and approved the workflow.

### Step 2 — Navigate to Workflows

In the left sidebar, click **Workflows**.

### Step 3 — Import from file

Click the **⋮ (More)** menu or the **Import** button depending on your n8n version:
- n8n v1.x: Click the three-dot menu (⋮) → **Import from File**
- Or drag and drop the `.json` file onto the workflow canvas

### Step 4 — Select the skeleton file

Navigate to `n8n/workflows/` in this repo and select the `.json` file you want to import.

### Step 5 — Verify import

After import, verify:
- Workflow name includes `[SKELETON]` in the title
- `active` status shows **Inactive** (not Active)
- All nodes are visible on the canvas
- Sticky Note warning is visible

### Step 6 — Do NOT activate

Do **not** toggle the workflow to Active. The workflow must remain `active: false` until:
1. All `REPLACE_WITH_*` credential placeholders are replaced with real credentials
2. All `REPLACE_WITH_*` data fields are filled with real values
3. All NoOp stub nodes are replaced with real API nodes
4. Owner has reviewed and approved the workflow
5. Codex has reviewed and issued PASS

---

## Workflow Node Structure (All Modules)

All content generation workflows (modules 1–4) share this base structure:

```
[Manual Trigger]
      ↓
[Set Input Variables]  ← mock/sample data
      ↓
[Code: Load Brand Brain]  ← STUB — no real credential
      ↓
[Code: AI Generate Draft]  ← STUB — no real API call
      ↓
[Code: Validate Required Fields]  ← checks schema required fields
      ↓
[If: Validation Pass]
    ↓ TRUE                  ↓ FALSE
[Set: approval_status=Draft]  [Set: Validation Error]
      ↓                           ↓
[Code: Write Log Entry]  [Stop and Error: Validation Failed]
      ↓
[NoOp: STUB — Send to Approval Queue]  ← STUB DISABLED

[Error Trigger] → [Set: Error Log] → [Stop and Error: Workflow Error]
```

The Comment Inbox Reply workflow has a modified structure with an escalation gate:

```
[Manual Trigger]
      ↓
[Set Input Variables]
      ↓
[Code: Load Brand Brain]
      ↓
[Code: Detect Intent and Sentiment]  ← STUB
      ↓
[If: Escalation Required]
    ↓ TRUE (escalate)        ↓ FALSE (safe to draft)
[Set: Escalation Flag]    [Code: AI Generate Reply Draft]  ← STUB
    ↓                           ↓
    └─────────────────────────→ [Code: Write Log Entry]
                                      ↓
                              [NoOp: STUB — Send to Reply Queue]
```

The Approval and Publishing Gate workflow has a distinct structure:

```
[Webhook: Receive Approval Request]  ← placeholder, not active
      ↓
[Code: Check Approval Status]
      ↓
[If: Is Approved]
    ↓ TRUE (approved)        ↓ FALSE (not approved)
[Switch: Item Type]       [Set: Block — Not Approved]
    ↓ (5 branches)              ↓
[NoOp: STUB × 5]          [Code: Write Block Log]
    ↓                           ↓
[Code: Write Approval Log]  [Stop and Error: Not Approved]
```

---

## Required Credentials (Placeholder List)

These credentials must be configured in your n8n instance before production use. All are placeholder references in skeleton files.

| Placeholder | Required For | n8n Credential Type |
|------------|-------------|---------------------|
| `REPLACE_WITH_ANTHROPIC_API_KEY` | All AI generation Code nodes | HTTP Header Auth or custom Anthropic credential |
| `REPLACE_WITH_GOOGLE_SHEETS_CREDENTIAL` | Log writes, approval queue writes | Google Sheets OAuth2 |
| `REPLACE_WITH_SUPABASE_CREDENTIAL` | Log writes (alternative to Sheets) | Supabase credential |
| `REPLACE_WITH_GOOGLE_DRIVE_CREDENTIAL` | Creative brief archive | Google Drive OAuth2 |
| `REPLACE_WITH_PLATFORM_CREDENTIAL` | Content publishing (Facebook/TikTok/Instagram/Zalo) | Platform-specific |
| `REPLACE_WITH_META_ADS_CREDENTIAL` | Ads launch (approval_publishing only) | Facebook Graph API |
| `REPLACE_WITH_TIKTOK_ADS_CREDENTIAL` | Ads launch (approval_publishing only) | TikTok Ads API |
| `REPLACE_WITH_MESSAGING_CREDENTIAL` | CRM sends (approval_publishing only) | Zalo/Messenger API |
| `REPLACE_WITH_INSTANCE_ID` | All workflows (meta field) | Not a credential — n8n instance ID |

**Rule:** No real credential is ever stored in a skeleton file. All `REPLACE_WITH_*` strings are placeholders only.

---

## Schema Alignment Notes

Each workflow's Code stub output is validated against the corresponding schema:

| Workflow | Schema | Key Constraint |
|----------|--------|----------------|
| content_auto | `content-output.schema.json` | No `hashtags` or `human_review_required` — not in schema (Codex constraint Phase 8) |
| creative_asset_auto | `creative-brief.schema.json` | Output is brief only — no actual asset generation |
| ads_pack_auto | `ads-pack.schema.json` | `compliance_notes` required in every output |
| crm_followup_auto | `crm-followup.schema.json` | `human_review_required: true` is schema `const` — cannot be false |
| comment_inbox_reply | `comment-inbox-reply.schema.json` | `human_review_required: true` is schema `const`. Escalated cases: `draft_reply: null` |
| approval_publishing | `approval-status.schema.json` | Only `approval_status: Approved` + `owner_decision: Approved` passes the gate |

---

## Approval Gate Summary

All workflows enforce the approval gate as follows:

| Rule | Enforcement |
|------|-------------|
| All outputs start as `Draft` | Set node before log and queue step |
| No publishing without `Approved` | `approval_publishing_skeleton.json` If node hard-blocks non-Approved items |
| No ads spend without `Approved` | `ads_pack_auto_skeleton.json` note + approval gate |
| No auto-reply without `Approved` | `comment_inbox_reply_assistant_skeleton.json` + approval gate |
| No auto-send CRM without `Approved` | `crm_followup_auto_skeleton.json` + approval gate |
| Owner-only approval | Documented in `schemas/approval-status.schema.json` and `docs/19_APPROVAL_GATE_RUNTIME_DESIGN.md` |

---

## Safety Checks — What to Verify Before Activating Any Workflow

Before activating any workflow in a production n8n instance, verify all of the following:

- [ ] All `REPLACE_WITH_*` credential placeholders replaced with real credentials
- [ ] All `REPLACE_WITH_*` data field values replaced with real Owner-provided data
- [ ] All NoOp stub nodes replaced with real API/integration nodes
- [ ] All Code stub nodes replaced with real AI API calls or logic
- [ ] Webhook path configured and secured (for approval_publishing)
- [ ] `active` status toggled by Owner only after reviewing the complete workflow
- [ ] Owner has set approval_status=Approved on a test item before enabling publish path
- [ ] Codex has reviewed workflow changes and issued PASS
- [ ] No real customer PII in any workflow node
- [ ] Logging destination configured and tested
- [ ] Error notifications configured (Telegram or equivalent)
- [ ] Phase 9 or later approved before production activation

---

## Validation Notes

| Check | Result |
|-------|--------|
| All 6 workflow JSON files are valid JSON | Verified — no syntax errors |
| `active: false` on all 6 workflows | Confirmed |
| No real API keys or credentials | Confirmed — all placeholders |
| No real platform endpoints wired | Confirmed — all NoOp stubs |
| All required schema fields present in mock output | Confirmed per schema review |
| `hashtags` and `human_review_required` absent from content_auto output | Confirmed — not in content-output.schema.json |
| `human_review_required: true` set in crm_followup and comment_inbox workflows | Confirmed — matches schema const |
| `compliance_notes` present in ads_pack mock output | Confirmed |
| Escalation logic present in comment_inbox workflow | Confirmed — Complaint/Angry → escalation_required=true, draft_reply=null |
| Approval gate blocks non-Approved items in approval_publishing | Confirmed — If node + Stop and Error |
| Error Trigger chain present in all 6 workflows | Confirmed |
| Log entry conforms to log-entry.schema.json fields | Confirmed |

---

## Known Limitations

1. Code nodes are JavaScript stubs only — no real AI calls are made.
2. All log writes are in-memory only — no real Google Sheets or Supabase writes.
3. All approval queue writes are NoOp — no real queue is populated.
4. Mock data uses literal placeholder strings — must be replaced before production.
5. Webhook in approval_publishing is unconfigured — path and auth must be set.
6. Error notifications (Telegram) are not wired — placeholder comment only.
7. n8n typeVersion numbers may need adjustment for specific n8n instance versions.

---

## Phase 8 Connection to Prior Phases

| Phase | Contribution to Phase 8 |
|-------|------------------------|
| Phase 3 | JSON schemas used for validation in all 6 workflows |
| Phase 4 | Module SOPs define the logic each workflow implements |
| Phase 5 | Sample outputs confirm mock data values are realistic |
| Phase 7 | Blueprint files define node plan, approval gate design, error handling |

---

_Phase 8 complete. Workflow skeletons ready for Codex review and Owner import-test._
