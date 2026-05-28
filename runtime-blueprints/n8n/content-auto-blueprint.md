# Content Auto Workflow — n8n Blueprint

Phase: 7 — n8n Runtime Blueprint
Created By: Claude Code (Builder, AGT-02) — 2026-05-28
Status: BLUEPRINT_DRAFT — Not implemented. No workflow JSON. No execution.

---

## Purpose

Define the future n8n workflow that automates content draft generation for Vị Cuốn. This blueprint describes how the system will accept an Owner request, load Brand Brain, load a content template, generate a draft, validate it, set approval status, write a log, and send the draft to the approval queue.

This blueprint does NOT create any executable workflow. No n8n JSON is included. All credentials are placeholders.

---

## Trigger Options

The workflow will support the following trigger methods (to be implemented in a future phase):

| Trigger | Method | Notes |
|---------|--------|-------|
| Manual Trigger | n8n Manual Trigger node | Owner clicks "Execute" in n8n |
| Google Sheet row trigger | Google Sheets Trigger node | New row in content request sheet triggers workflow |
| Supabase row trigger | Supabase Trigger node (future) | New record in content_requests table |
| Owner command trigger | Webhook Trigger node | Owner sends command via Telegram or web form |

Phase 7 does not activate any trigger. All workflows must be imported with `active: false`.

---

## Required Inputs

Every content auto request must include the following fields. These map to `schemas/content-output.schema.json`.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `brand_id` | string | yes | Brand identifier. Example: `vi-cuon` |
| `brand_brain_ref` | string | yes | Path to Brand Brain file. Example: `brand-brain/vi-cuon.md` |
| `content_request` | string | yes | Plain-language request from Owner. Example: "lunch promotion for Wednesday" |
| `platform` | string | yes | Target platform. One of: `facebook`, `instagram`, `tiktok`, `zalo` |
| `objective` | string | yes | Content objective. Example: `awareness`, `conversion`, `engagement` |
| `target_audience` | string | yes | Audience description from Brand Brain |
| `offer` | string | yes | Offer to feature. Must be Owner-confirmed. Use `[OWNER_TO_PROVIDE_OFFER]` if unknown |

---

## Data Sources

The workflow reads from the following sources:

| Source | File / Location | Used For |
|--------|----------------|---------|
| Brand Brain | `brand-brain/vi-cuon.md` | Brand identity, voice, menu, audience, offers |
| Content template | `templates/content-output-template.md` | Output structure |
| Content schema | `schemas/content-output.schema.json` | Validation rules |

In future runtime phases, Brand Brain data may be loaded from Google Sheets or Supabase instead of repo files.

---

## Future n8n Node Plan

The following node sequence describes the intended workflow implementation. Node names and types are illustrative — exact implementation will be defined in Phase 8.

| Step | Node Type | Node Name | Action |
|------|-----------|-----------|--------|
| 1 | Manual Trigger / Webhook | Trigger | Receive Owner request with required input fields |
| 2 | Read Binary File / HTTP Request | Load Brand Brain | Read `brand-brain/vi-cuon.md` from repo or external source |
| 3 | Read Binary File / HTTP Request | Load Content Template | Read `templates/content-output-template.md` |
| 4 | AI Agent / HTTP Request | Generate Content Draft | Call AI model (Claude or equivalent) with Brand Brain + template + request |
| 5 | Function / Code | Validate Required Fields | Check all required fields present; check no placeholder fields unfilled |
| 6 | Set | Set approval_status = Draft | Assign `approval_status: Draft` to output object |
| 7 | Function / Code | Write Log | Create structured log entry per `schemas/log-entry.schema.json` |
| 8 | HTTP Request / Google Sheets | Send to Approval Queue | Write draft to approval queue (Google Sheet or Supabase table) |

---

## Output

The workflow produces a content draft only. No publishing action is taken at this stage.

Output format: as defined in `templates/content-output-template.md` and validated against `schemas/content-output.schema.json`.

**Output fields include:**
- `brand_id`
- `platform`
- `objective`
- `hook`
- `caption`
- `hashtags`
- `visual_direction`
- `cta`
- `approval_status: Draft`
- `human_review_required: true`
- `log_ref`

---

## Approval Requirement

- Every content draft output must have `approval_status: Draft` before reaching the approval queue.
- No content may be posted to any platform without Owner setting `approval_status: Approved`.
- The workflow MUST NOT trigger any publishing action.
- See `runtime-blueprints/n8n/approval-gate-blueprint.md` for full approval gate design.

---

## Logging Requirement

- Every execution must write a structured log entry to `logs/AGENT_ACTIVITY_LOG.md` (build phase) or Google Sheets / Supabase (runtime phase).
- Log fields: `phase`, `agent`, `input_ref`, `output_ref`, `approval_status`, `errors`, `owner_action_required`, `next_action`.
- See `runtime-blueprints/n8n/logging-blueprint.md` for full logging design.

---

## Failure Handling

| Failure | Required Behavior |
|---------|------------------|
| Brand Brain file not found | Stop workflow; write error log; set `owner_action_required: true`; notify Owner |
| Required input field missing | Stop workflow; write error log; return field name in error message |
| AI generation returns empty output | Stop workflow; write error log; do not send to approval queue |
| Schema validation fails | Stop workflow; write error log; send validation error to Owner review |
| Approval queue write fails | Stop workflow; write error log; retain draft locally |

See `runtime-blueprints/n8n/error-handling-blueprint.md` for full error handling design.

---

## Done Criteria

This blueprint is complete when:

- [ ] All required input fields are defined
- [ ] All data sources are listed with file paths
- [ ] All n8n nodes are described in sequence
- [ ] Output format references correct template and schema
- [ ] Approval requirement is documented
- [ ] Logging requirement is documented
- [ ] All failure cases have required behavior defined
- [ ] No real n8n JSON created
- [ ] No credentials stored
- [ ] No publishing action described or implied

---

_This is a design document only. Implementation in Phase 8._
