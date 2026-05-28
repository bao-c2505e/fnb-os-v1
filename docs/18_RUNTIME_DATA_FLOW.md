# 18 — Runtime Data Flow

Phase: 7 — n8n Runtime Blueprint
Created By: Claude Code (Builder, AGT-02) — 2026-05-28
Status: BLUEPRINT_DRAFT

---

## Overview

This document defines the complete data flow from Owner request to handoff or future execution. Every step identifies what data moves, where it comes from, and what rule or gate controls it.

**No screenshot-as-log rule applies throughout this entire flow: every step that produces a log must write a structured log entry. Screenshots are supplementary only.**

---

## Full Data Flow

```
Owner Request
→ Runtime Trigger
→ Load Brand Brain
→ Load Template
→ Generate Draft
→ Validate Schema
→ Set approval_status = Draft
→ Write Log
→ Send to Approval Queue
→ Owner Decision
→ Route Next Step
→ Handoff / Future Execution
```

---

## Step-by-Step Data Flow

### Step 1 — Owner Request

| Field | Detail |
|-------|--------|
| Input | Owner submits request: brand_id, content_request, platform, objective, target_audience, offer |
| Input ref | Manual form, Google Sheet row (future), Telegram command (future) |
| Validation | All required fields must be present; no placeholder values allowed for offer |
| Failure path | If required field missing: stop; write error log; notify Owner |

---

### Step 2 — Runtime Trigger

| Field | Detail |
|-------|--------|
| Input | Owner request data from Step 1 |
| n8n node | Manual Trigger / Webhook / Google Sheets Trigger |
| Output | Structured input object passed to next node |
| Failure path | If trigger fails: stop; write error log |

---

### Step 3 — Load Brand Brain

| Field | Detail |
|-------|--------|
| Input | `brand_brain_ref` from Owner request |
| Source | `brand-brain/vi-cuon.md` (current) or Google Drive / Supabase (future) |
| Output | Brand Brain data object: brand name, voice, menu, audience, offers, visual style |
| Validation | Brand Brain must exist and must not contain unfilled placeholders for required fields |
| Failure path | If Brand Brain not found or has unfilled placeholders: stop; write error log; set owner_action_required: true |

---

### Step 4 — Load Template

| Field | Detail |
|-------|--------|
| Input | Platform and objective from Owner request |
| Source | `templates/content-output-template.md` (or equivalent module template) |
| Output | Template structure with field placeholders |
| Failure path | If template not found: stop; write error log |

---

### Step 5 — Generate Draft

| Field | Detail |
|-------|--------|
| Input | Brand Brain data + Template structure + Owner request |
| Process | AI agent (Claude or equivalent) generates draft filling template fields using Brand Brain |
| Output | Draft content object with all template fields populated |
| Rule | Generated content must not invent prices, addresses, or offers not confirmed in Brand Brain |
| Failure path | If AI returns empty or malformed output: stop; write error log |

---

### Step 6 — Validate Schema

| Field | Detail |
|-------|--------|
| Input | Draft content object from Step 5 |
| Source | `schemas/content-output.schema.json` (or equivalent module schema) |
| Process | Validate output object against JSON schema |
| Output | Validated draft object (if passes) |
| Failure path | If schema validation fails: stop; write error log with field list; return to revision queue |

---

### Step 7 — Set approval_status = Draft

| Field | Detail |
|-------|--------|
| Input | Validated draft object from Step 6 |
| Process | Set `approval_status: Draft` on output object |
| Rule | `approval_status` must be `Draft` — never `Approved`, `Scheduled`, or `Published` at this stage |
| Output | Draft object with `approval_status: Draft` |

---

### Step 8 — Write Log

| Field | Detail |
|-------|--------|
| Input | Validated draft object + workflow metadata |
| Process | Create structured log entry per `schemas/log-entry.schema.json` |
| Output | Log entry written to `logs/AGENT_ACTIVITY_LOG.md` (build) or Google Sheets / Supabase (runtime) |
| Log fields | log_id, timestamp, phase, agent, input_ref, output_ref, approval_status: Draft, errors: [], owner_action_required: false, next_action: "send to approval queue" |
| Failure path | If log write fails: stop; write fallback error note; set owner_action_required: true |
| Screenshot rule | Log file write is the authoritative record — screenshots do not replace this step |

---

### Step 9 — Send to Approval Queue

| Field | Detail |
|-------|--------|
| Input | Draft object with `approval_status: Draft` |
| Destination | Google Sheets approval table (future) or Telegram message (future) or manual repo file (current) |
| Output | Draft visible to Owner for review |
| Failure path | If delivery fails: stop; write error log; retain draft locally |

---

### Step 10 — Owner Decision

| Field | Detail |
|-------|--------|
| Input | Owner reviews draft in approval queue |
| Owner actions | Set `approval_status` to: `Approved`, `Rejected`, or `Needs Revision` |
| Rule | Only Owner (Bo Bao) may set `approval_status: Approved` |
| Output | Updated approval record with Owner decision and timestamp |
| Log | Approval log entry written immediately on Owner decision |
| Timeout | If Owner does not respond within configured timeout: stop workflow; write timeout log; notify Owner |

---

### Step 11 — Route Next Step

| Field | Detail |
|-------|--------|
| Input | Approval decision from Step 10 |
| Route: Approved | Proceed to publishing preparation or scheduled delivery (future phase) |
| Route: Needs Revision | Return to agent with revision notes; restart from Step 5 |
| Route: Rejected | Archive draft; write rejection log; end workflow |
| Rule | Route to publish/send/spend is ONLY available when `approval_status: Approved` |

---

### Step 12 — Handoff / Future Execution

| Field | Detail |
|-------|--------|
| Current phase (7) | End of flow — no execution. Draft and approval records stored in repo or handoff files |
| Future phases (8+) | If Approved: proceed to platform-specific publish node (future); write publish log; update approval record to `Published` |
| Log | Final log entry written: status, output_ref, publish_ref (if applicable) |

---

## Failure Path Summary

| Step | Failure | Action |
|------|---------|--------|
| 1 | Missing required field | Stop; error log; notify Owner |
| 2 | Trigger fails | Stop; error log |
| 3 | Brand Brain not found / placeholder unfilled | Stop; error log; owner_action_required: true |
| 4 | Template not found | Stop; error log |
| 5 | AI returns empty/malformed output | Stop; error log |
| 6 | Schema validation fails | Stop; error log; return to revision |
| 8 | Log write fails | Stop; fallback note; owner_action_required: true |
| 9 | Approval queue delivery fails | Stop; error log; retain draft locally |
| 10 | Owner timeout | Stop; timeout log; notify Owner |
| 11 | Route to publish without Approved status | Block immediately; error log |

---

## No Screenshot-as-Log Rule

Every step that produces a log must write a structured entry in the designated log file or table. A screenshot of an output, a message, or a screen capture is NOT an acceptable substitute for a log entry.

---

_This is a design document only. Implementation begins in Phase 8._
