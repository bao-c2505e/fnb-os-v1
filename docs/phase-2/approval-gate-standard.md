# Approval Gate Standard — FnB OS V1

**Version:** 2.2
**Maintained By:** ChatGPT (Chief Architect) + Claude Code (Builder)
**Last Updated:** 2026-05-28
**Phase:** 2.2
**Module:** MOD-07 — Approval + Publishing Automation

This document defines the approval rules, status lifecycle, and execution gates for all outputs in FnB OS V1.
Every module that produces a draft output must follow this standard before any external action is triggered.

Related: `03_APPROVAL_PIPELINE/status_lifecycle.md` (Phase 1.3 content-specific lifecycle)
This document supersedes and extends Phase 1.3 to cover all module types, not only content packs.

---

## Core Rule

**The AI may generate drafts, route drafts, and log status updates automatically.**
**The AI must never publish, reply, send CRM messages, execute ads, or take any external action without explicit Owner Approval.**
**Approval must be stored as structured data — not only as a message in a chat.**

---

## What AI May Do Without Approval

| Action | Module | Notes |
|--------|--------|-------|
| Generate a draft content pack | MOD-02 | Draft status only |
| Generate a design brief | MOD-03 | Draft status only |
| Generate an ads pack | MOD-04 | Draft status only |
| Generate a draft CRM message | MOD-05 | Draft status only |
| Classify a comment intent | MOD-06 | Classification only |
| Generate a draft comment reply | MOD-06 | Draft status only |
| Route a draft to Owner for review | MOD-07 | Routing only, no execution |
| Update item status in the pipeline | MOD-07 | Status write only |
| Log an agent action | MOD-12 | Logging only |
| Generate an intelligence report | MOD-08, 09, 10 | Read-only output |
| Store an asset in Asset Library | MOD-11 | After prior approval |
| Run AI self-check on a draft | Any | Internal validation only |

---

## What Requires Owner Approval

| Action | Module | Gate Type |
|--------|--------|-----------|
| Publish a social media post | MOD-02, 07 | APPROVAL_REQUIRED — HARD |
| Post a reply to a comment | MOD-06, 07 | APPROVAL_REQUIRED — HARD |
| Send a CRM message to a customer | MOD-05, 07 | APPROVAL_REQUIRED — HARD |
| Set up or launch a paid ad | MOD-04, 07 | APPROVAL_REQUIRED — HARD |
| Apply a website / landing page change | MOD-10, 07 | APPROVAL_REQUIRED — HARD |
| Activate an n8n workflow | Any | APPROVAL_REQUIRED — HARD |
| Change Brand Brain data | MOD-01 | APPROVAL_REQUIRED — SOFT (review) |
| Archive or delete an asset | MOD-11 | APPROVAL_REQUIRED — SOFT (review) |

**HARD** = execution is blocked at the system level until an approval record exists.
**SOFT** = change is flagged for Owner review; a missing approval should alert but may not hard-block in V1 manual flow.

---

## Approval Status Lifecycle

### Full Status List

| Status | Code | Meaning | Who Sets It |
|--------|------|---------|-------------|
| Draft | `DRAFT` | AI has generated the item. Self-check not yet run or not yet passed. | AI Agent |
| Pending Review | `PENDING_REVIEW` | AI self-check passed. Item is ready for Owner review. | AI Agent (after self-check pass) |
| Needs Fix | `NEEDS_FIX` | Owner reviewed and requested changes. AI must revise. | Owner |
| Approved | `APPROVED` | Owner has explicitly approved the item. Execution may be triggered. | Owner |
| Rejected | `REJECTED` | Owner has explicitly rejected the item. No execution. Archive. | Owner |
| Ready for Publish | `READY_FOR_PUBLISH` | Content approved. Scheduled or queued for social media publishing. | System (after APPROVED) |
| Ready for Reply | `READY_FOR_REPLY` | Comment reply approved. Queued for posting. | System (after APPROVED) |
| Ready for CRM Send | `READY_FOR_CRM_SEND` | CRM message approved. Queued for Zalo OA / SMS send. | System (after APPROVED) |
| Ready for Ads Setup | `READY_FOR_ADS_SETUP` | Ads pack approved. Queued for Meta/TikTok ads setup. | System (after APPROVED) |
| Published | `PUBLISHED` | Content has been published to the platform. | System (after execution) or Owner (manual) |
| Sent | `SENT` | CRM message or reply has been delivered. | System (after execution) or Owner (manual) |
| Archived | `ARCHIVED` | Item is closed. No further action. | Owner or System |

---

## Status Flow Diagrams

### Content Pack (MOD-02 → MOD-07)

```
DRAFT
  ↓ (AI self-check runs)
  ├─→ DRAFT (if self-check fails — AI revises and re-checks)
  ↓ (self-check passes)
PENDING_REVIEW
  ↓ (Owner notified)
  ├─→ NEEDS_FIX → DRAFT (Owner requests changes, AI revises)
  ├─→ REJECTED → ARCHIVED
  └─→ APPROVED
        ↓
     READY_FOR_PUBLISH
        ↓ (Owner confirms publish time, or auto-schedule after approval)
     PUBLISHED
        ↓
     ARCHIVED
```

### Comment Reply (MOD-06 → MOD-07)

```
DRAFT
  ↓ (AI self-check and intent classification)
PENDING_REVIEW
  ↓ (Owner reviews draft reply)
  ├─→ NEEDS_FIX → DRAFT
  ├─→ REJECTED → ARCHIVED
  └─→ APPROVED
        ↓
     READY_FOR_REPLY
        ↓ (Owner confirms OR auto-post after approval in future phase)
     SENT
        ↓
     ARCHIVED
```

### CRM Message (MOD-05 → MOD-07)

```
DRAFT
  ↓ (AI self-check)
PENDING_REVIEW
  ↓ (Owner reviews)
  ├─→ NEEDS_FIX → DRAFT
  ├─→ REJECTED → ARCHIVED
  └─→ APPROVED
        ↓
     READY_FOR_CRM_SEND
        ↓ (Owner confirms send OR auto-send via Zalo OA in future phase)
     SENT
        ↓
     ARCHIVED
```

### Ads Pack (MOD-04 → MOD-07)

```
DRAFT
  ↓ (AI self-check — includes budget and compliance flags)
PENDING_REVIEW
  ↓ (Owner reviews — mandatory budget review)
  ├─→ NEEDS_FIX → DRAFT
  ├─→ REJECTED → ARCHIVED
  └─→ APPROVED
        ↓
     READY_FOR_ADS_SETUP
        ↓ (Owner manually sets up ad OR future: Meta/TikTok API after approval)
     PUBLISHED (ad is live)
        ↓
     ARCHIVED (ad ends)
```

---

## Approval Record Format

Every approval decision must be stored as structured data — not only as a message in a chat or a note on a Google Sheet row.

Minimum required fields for a valid approval record:

```json
{
  "item_id": "[content ID or module output ID]",
  "item_type": "content_pack | comment_reply | crm_message | ads_pack | design_brief",
  "module": "MOD-0X",
  "status": "APPROVED | REJECTED | NEEDS_FIX",
  "decision_by": "Owner",
  "decision_timestamp": "YYYY-MM-DDTHH:MM:SS+07:00",
  "notes": "[optional: reason for rejection or fix request]",
  "execution_triggered": false
}
```

`execution_triggered` must remain `false` until the execution action has been confirmed.
Once set to `true`, it must not be reset — create a new record if re-execution is needed.

In V1, approval records are stored in Google Sheets with these columns as minimum fields.
In future phases, approval records may be stored in a database or n8n data store.

---

## AI Self-Check Rules

Before any draft advances to `PENDING_REVIEW`, the generating AI agent must run a self-check against Brand Brain constraints. The self-check covers:

### Content Self-Check (MOD-02)
- [ ] All prices mentioned are in `menu_brain.md` or `offer_engine.md`
- [ ] No unsubstantiated health or nutrition claims
- [ ] No competitor names mentioned
- [ ] No fake urgency language
- [ ] Brand voice and tone match `brand_brain.md`
- [ ] Correct hashtag set for the platform
- [ ] Emoji count within brand guidelines
- [ ] If offer included: offer exists in `offer_engine.md`

### CRM Message Self-Check (MOD-05)
- [ ] Customer name and phone are present (no blank contact fields)
- [ ] Message tone matches `crm_brain.md`
- [ ] No price or offer that is not in `offer_engine.md`
- [ ] Opt-out note included if required by brand policy
- [ ] Send timing is within approved hours

### Comment Reply Self-Check (MOD-06)
- [ ] Intent classification is confirmed (not ambiguous)
- [ ] Reply tone matches `comment_reply_brain.md`
- [ ] No price quoted without checking `menu_brain.md`
- [ ] Complaint or legal intent → always escalate to Owner (no auto-approve)
- [ ] No competitor reference
- [ ] Reply length is appropriate for platform

### Ads Pack Self-Check (MOD-04)
- [ ] Audience targeting is based on approved segments from `customer_brain.md`
- [ ] Budget is within Owner-set range
- [ ] Ad copy does not make unsubstantiated claims
- [ ] Creative brief references an approved asset or MOD-03 output
- [ ] Compliance flag checked: any claim that needs a disclaimer is flagged

**If any self-check item fails:** The AI marks the status `DRAFT` (not `PENDING_REVIEW`), records the failed item, and revises before re-checking.

---

## Escalation Rules

Certain conditions require mandatory Owner escalation — no auto-approve, no delegation:

| Condition | Module | Escalation Type |
|-----------|--------|----------------|
| Customer complaint or negative review | MOD-06 | Mandatory Owner review |
| Price dispute or refund request | MOD-06, 05 | Mandatory Owner review |
| Any legal or compliance claim in content | MOD-02, 04 | Mandatory Owner review |
| Budget above Owner-set threshold | MOD-04 | Mandatory Owner budget confirmation |
| Any new external integration (API, platform) | Any | Mandatory Owner approval before activation |
| n8n workflow activation (first run) | Any | Mandatory Owner approval |
| Brand Brain data change | MOD-01 | Owner review before next content generation |

Escalated items must not be auto-closed. They remain in `PENDING_REVIEW` until Owner explicitly resolves them.

---

## Approval Storage Standard

### V1 (Manual — Google Sheets)

In V1, approvals are tracked manually in a Google Sheet with columns matching the approval record format above. The sheet is the single source of truth for approval status.

Minimum sheet columns:
```
item_id | item_type | module | status | decision_by | decision_timestamp | notes | execution_triggered
```

Sheet location: defined in `08_DEPLOY/google_sheet_schema.md`

### Future (Automated — n8n + Data Store)

In future phases, approval records will be written automatically by n8n workflows to a database or structured data store. The Google Sheet may remain as a human-readable view.

Regardless of storage method, the approval record schema defined above must be followed.

---

## What the Approval Gate Protects Against

| Risk | Gate |
|------|------|
| AI publishes content without Owner seeing it | PENDING_REVIEW blocks → APPROVED required |
| AI replies to a customer complaint incorrectly | Complaint intent → mandatory escalation |
| AI sends CRM to wrong customer or at wrong time | CRM self-check + Owner approval |
| AI spends budget on ads without Owner knowing | Ads pack approval + budget gate |
| AI activates n8n workflow in production | Workflow activation requires Owner approval |
| Approval is lost or untraceable | Structured approval record stored as data |

---

## Relationship to Phase 1.3 Status Lifecycle

`03_APPROVAL_PIPELINE/status_lifecycle.md` (Phase 1.3) defines the content-specific status lifecycle for Vị Cuốn content packs.

This document (`approval-gate-standard.md`) defines the system-wide approval standard for all module types.

The two documents are compatible. Phase 1.3 status codes (`DRAFT`, `READY_FOR_REVIEW`, `APPROVED`, etc.) map to the codes in this document. Where there are minor naming differences, this document's codes are the canonical system-wide standard.

| Phase 1.3 Code | This Document | Notes |
|----------------|---------------|-------|
| `DRAFT` | `DRAFT` | Same |
| `READY_FOR_REVIEW` | `PENDING_REVIEW` | Same concept, standardized name |
| `REVISION_REQUESTED` | `NEEDS_FIX` | Same concept, standardized name |
| `APPROVED` | `APPROVED` | Same |
| `REJECTED` | `REJECTED` | Same |
| `SCHEDULE_PROPOSED` | `READY_FOR_PUBLISH` | Same concept, generalized |
| `PUBLISHED_MANUAL` | `PUBLISHED` | Same |
| `ARCHIVED` | `ARCHIVED` | Same |

Both documents remain valid. Phase 1.3 may continue to use its original naming for content-specific flows.
