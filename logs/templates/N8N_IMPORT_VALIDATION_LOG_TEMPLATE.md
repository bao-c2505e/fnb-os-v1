# n8n Import Validation Log

Phase: 9 — n8n Import Validation Pack
Template Created By: Claude Code (Builder, AGT-02) — 2026-05-28
Filled By: `[OWNER_TO_FILL]`

---

## Instructions

Fill one row per import attempt. Copy this template to create a new log file named:
`logs/N8N_IMPORT_VALIDATION_LOG_YYYYMMDD.md`

Do not record real credentials, API keys, tokens, or passwords in this log.
Record only workflow names, node counts, import results, and error messages (sanitized).

---

## Session Details

| Field | Value |
|-------|-------|
| Date | `[FILL: YYYY-MM-DD]` |
| Time (local) | `[FILL: HH:MM]` |
| n8n version | `[FILL: e.g. 1.x.x]` |
| Instance type | `[FILL: Self-hosted / n8n Cloud]` |
| Node.js version (if script run) | `[FILL: e.g. v20.x.x / N/A]` |
| Filled By | `[FILL: Owner name]` |
| Static validator run? | `[FILL: Yes — All PASS / Yes — Failures found / No — Node.js not available]` |

---

## Static Validator Result

*Skip if Node.js not available.*

| Check | Result |
|-------|--------|
| Validator script ran without error | `[PASS / FAIL / N/A]` |
| All 6 files: valid JSON | `[PASS / FAIL / N/A]` |
| All 6 files: active=false | `[PASS / FAIL / N/A]` |
| All 6 files: secret scan clean | `[PASS / FAIL / N/A]` |
| All 6 files: Error Trigger present | `[PASS / FAIL / N/A]` |
| All 6 files: Sticky Note present | `[PASS / FAIL / N/A]` |
| Overall validator exit code | `[0 = all pass / 1 = failures found / N/A]` |

Validator notes: `[FILL or "None"]`

---

## Workflow Import Results

### 1. content_auto_skeleton.json

| Field | Value |
|-------|-------|
| File imported | `content_auto_skeleton.json` |
| Expected workflow name | `FnB OS V1 — Content Auto [SKELETON]` |
| Actual workflow name shown in n8n | `[FILL]` |
| Names match | `[Yes / No]` |
| Import result | `[Success / Error]` |
| Error message (if any) | `[FILL or "None"]` |
| Node count shown | `[FILL] (expected: 15)` |
| active toggle after import | `[OFF / ON]` |
| Sticky Note visible on canvas | `[Yes / No]` |
| Credential slots empty | `[Yes / No]` |
| Workflow activated? | `[No — confirmed / Yes — STOP — report to Builder]` |
| **Section result** | `[PASS / FAIL / BLOCKED]` |

---

### 2. creative_asset_auto_skeleton.json

| Field | Value |
|-------|-------|
| File imported | `creative_asset_auto_skeleton.json` |
| Expected workflow name | `FnB OS V1 — Creative Asset Auto [SKELETON]` |
| Actual workflow name shown in n8n | `[FILL]` |
| Names match | `[Yes / No]` |
| Import result | `[Success / Error]` |
| Error message (if any) | `[FILL or "None"]` |
| Node count shown | `[FILL] (expected: 15)` |
| active toggle after import | `[OFF / ON]` |
| Sticky Note visible on canvas | `[Yes / No]` |
| Credential slots empty | `[Yes / No]` |
| Workflow activated? | `[No — confirmed / Yes — STOP — report to Builder]` |
| **Section result** | `[PASS / FAIL / BLOCKED]` |

---

### 3. ads_pack_auto_skeleton.json

**Risk: MEDIUM — ads budget gate**

| Field | Value |
|-------|-------|
| File imported | `ads_pack_auto_skeleton.json` |
| Expected workflow name | `FnB OS V1 — Ads Pack Auto [SKELETON]` |
| Actual workflow name shown in n8n | `[FILL]` |
| Names match | `[Yes / No]` |
| Import result | `[Success / Error]` |
| Error message (if any) | `[FILL or "None"]` |
| Node count shown | `[FILL] (expected: 15)` |
| active toggle after import | `[OFF / ON]` |
| "NO ADS SPEND" Sticky Note visible | `[Yes / No]` |
| Credential slots empty | `[Yes / No]` |
| Workflow activated? | `[No — confirmed / Yes — STOP — report to Builder]` |
| Ad spend triggered? | `[No — confirmed / Yes — STOP — document immediately]` |
| **Section result** | `[PASS / FAIL / BLOCKED]` |

---

### 4. crm_followup_auto_skeleton.json

**Risk: MEDIUM — messaging gate**

| Field | Value |
|-------|-------|
| File imported | `crm_followup_auto_skeleton.json` |
| Expected workflow name | `FnB OS V1 — CRM Followup Auto [SKELETON]` |
| Actual workflow name shown in n8n | `[FILL]` |
| Names match | `[Yes / No]` |
| Import result | `[Success / Error]` |
| Error message (if any) | `[FILL or "None"]` |
| Node count shown | `[FILL] (expected: 15)` |
| active toggle after import | `[OFF / ON]` |
| "NO AUTO-SEND" Sticky Note visible | `[Yes / No]` |
| Credential slots empty | `[Yes / No]` |
| Workflow activated? | `[No — confirmed / Yes — STOP — report to Builder]` |
| Customer messages sent? | `[No — confirmed / Yes — STOP — document immediately]` |
| **Section result** | `[PASS / FAIL / BLOCKED]` |

---

### 5. comment_inbox_reply_assistant_skeleton.json

**Risk: MEDIUM — reply gate**

| Field | Value |
|-------|-------|
| File imported | `comment_inbox_reply_assistant_skeleton.json` |
| Expected workflow name | `FnB OS V1 — Comment Inbox Reply Assistant [SKELETON]` |
| Actual workflow name shown in n8n | `[FILL]` |
| Names match | `[Yes / No]` |
| Import result | `[Success / Error]` |
| Error message (if any) | `[FILL or "None"]` |
| Node count shown | `[FILL] (expected: 13)` |
| active toggle after import | `[OFF / ON]` |
| Sticky Note visible on canvas | `[Yes / No]` |
| Credential slots empty | `[Yes / No]` |
| Workflow activated? | `[No — confirmed / Yes — STOP — report to Builder]` |
| Replies posted to social media? | `[No — confirmed / Yes — STOP — document immediately]` |
| **Section result** | `[PASS / FAIL / BLOCKED]` |

---

### 6. approval_publishing_skeleton.json

**Risk: HIGH — publishing gate**

| Field | Value |
|-------|-------|
| File imported | `approval_publishing_skeleton.json` |
| Expected workflow name | `FnB OS V1 — Approval & Publishing [SKELETON]` |
| Actual workflow name shown in n8n | `[FILL]` |
| Names match | `[Yes / No]` |
| Import result | `[Success / Error]` |
| Error message (if any) | `[FILL or "None"]` |
| Node count shown | `[FILL] (expected: 17)` |
| active toggle after import | `[OFF / ON]` |
| Sticky Note visible on canvas | `[Yes / No]` |
| Webhook node visible but NOT connected | `[Yes / No]` |
| Credential slots empty | `[Yes / No]` |
| Workflow activated? | `[No — confirmed / Yes — STOP — report to Builder]` |
| Content published to any platform? | `[No — confirmed / Yes — STOP — document immediately]` |
| **Section result** | `[PASS / FAIL / BLOCKED]` |

---

## Overall Result

| Check | Result |
|-------|--------|
| All 6 workflows imported without error | `[Yes / No]` |
| All 6 workflows show active=OFF | `[Yes / No]` |
| All 6 workflows: Sticky Note visible | `[Yes / No]` |
| All 6 workflows: credential slots empty | `[Yes / No]` |
| No workflows activated during this session | `[Yes / No — STOP if No]` |
| No external services contacted | `[Yes / No — STOP if No]` |
| No ad spend triggered | `[Yes / No — STOP if No]` |
| No messages sent to customers | `[Yes / No — STOP if No]` |
| No content published | `[Yes / No — STOP if No]` |

**Phase 9 Validation Result: `[ALL PASS / PARTIAL — some BLOCKED / FAIL]`**

---

## Blockers and Notes

`[FILL: List any FAIL or BLOCKED items here, with exact error text from n8n]`

---

## Screenshots (optional)

Screenshots supplement but do not replace this log.

| File | Content |
|------|---------|
| `[FILL: filename or path]` | `[FILL: description of what the screenshot shows]` |

*If no screenshots taken, leave this section blank.*

---

## Sign-Off

| Field | Value |
|-------|-------|
| Filled By | `[FILL]` |
| Date | `[FILL: YYYY-MM-DD]` |
| Ready for Phase 10? | `[Yes — all PASS / No — blockers remain]` |
