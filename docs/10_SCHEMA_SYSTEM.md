# 10 — Schema System

Version: 1.0
Created By: Claude Code (Builder, AGT-02)
Date: 2026-05-28
Phase: 3 — Brand Brain + Input/Output Schemas

---

## Why Schemas Exist

FnB OS V1 uses structured JSON schemas to define the **input and output contracts** for every agent. Schemas serve three purposes:

1. **Consistency** — Every agent produces output in a predictable, validated structure.
2. **Approval traceability** — Every output has `approval_status`, `created_by_agent`, and `created_at` fields so the full chain of custody is auditable.
3. **Forward compatibility** — Schemas are designed to be consumed by n8n workflows and LangGraph agents in future phases without modification.

Schemas are not executable code. They are JSON Schema Draft-07 definitions stored in `schemas/`.

---

## Schema Registry

| Schema File | Title | Used By | Purpose |
|------------|-------|---------|---------|
| `schemas/content-output.schema.json` | Content Output | Content Agent | Captions, hooks, scripts, CTAs for any platform |
| `schemas/creative-brief.schema.json` | Creative Brief | Creative Asset Agent | Image/video/design briefs with AI prompts and QA checklist |
| `schemas/ads-pack.schema.json` | Ads Pack | Ads Pack Agent | Ad copy, headlines, audience targeting — no live spend without Approved |
| `schemas/crm-followup.schema.json` | CRM Follow-Up Sequence | CRM Follow-Up Agent | Message sequences — no auto-send without Approved |
| `schemas/comment-inbox-reply.schema.json` | Comment Inbox Reply Draft | Comment Inbox Agent | Reply drafts — no auto-reply without Approved; escalation rules built in |
| `schemas/approval-status.schema.json` | Approval Status | All agents + Owner | Tracks approval state for any item; state machine enforced |
| `schemas/log-entry.schema.json` | Log Entry | All agents | Structured logs for every significant action |
| `schemas/command.schema.json` | Command | Builder, Architect | Command intake lifecycle (Phase 0.6) |
| `schemas/task.schema.json` | Task | All agents | Task tracking (Phase 0.5) |

---

## Which Agent Uses Which Schema

### Content Agent
- **Produces:** `content-output.schema.json` — one record per content piece drafted
- **Reads:** Brand Brain (`brand-brain/vi-cuon.md`) before generating any output
- **Logs:** `log-entry.schema.json` with `action_type: "Content Draft"`

### Creative Asset Agent
- **Produces:** `creative-brief.schema.json` — one record per brief (photo, video, graphic, ad creative)
- **Reads:** Brand Brain for visual direction and brand personality
- **Logs:** `log-entry.schema.json` with `action_type: "Creative Brief Draft"`

### Ads Pack Agent
- **Produces:** `ads-pack.schema.json` — one record per ad pack draft
- **References:** `creative-brief.schema.json` via `creative_brief_ref`
- **Reads:** Brand Brain for audience, tone, and selling points
- **Logs:** `log-entry.schema.json` with `action_type: "Ads Pack Draft"`

### CRM Follow-Up Agent
- **Produces:** `crm-followup.schema.json` — one record per message sequence
- **Reads:** Brand Brain for tone and offer rules
- **Logs:** `log-entry.schema.json` with `action_type: "CRM Sequence Draft"`

### Comment Inbox Agent
- **Produces:** `comment-inbox-reply.schema.json` — one record per reply draft or escalation
- **Reads:** Brand Brain for tone and compliance rules
- **Logs:** `log-entry.schema.json` with `action_type: "Reply Draft"`

### Approval / Publishing Agent
- **Produces:** `approval-status.schema.json` — one record per approval decision
- **Reads:** All output schemas to verify `approval_status` before advancing state
- **Logs:** `log-entry.schema.json` with `action_type: "Approval Decision"`

---

## Required Fields Across All Schemas

Every output schema in FnB OS V1 includes these four universal fields:

| Field | Type | Purpose |
|-------|------|---------|
| `approval_status` | string (enum) | Current approval state — always starts at `Draft` |
| `created_by_agent` | string | Which agent produced this output |
| `created_at` | date-time | When this output was created |
| `notes` | string or null | Optional notes for Owner or Reviewer |

---

## Approval State Machine

All outputs in FnB OS V1 follow this approval lifecycle:

```
Draft
  └─→ Ready for Review
        └─→ Needs Revision ─→ (back to Draft or Ready for Review)
        └─→ Approved (Owner only)
              └─→ Scheduled
              └─→ Published
        └─→ Rejected
```

**Hard rules enforced by all agents and schemas:**

| Rule | Detail |
|------|--------|
| Published requires Approved | No output can be Published without prior Approved status |
| Scheduled requires Approved | No output can be Scheduled without prior Approved status |
| Ad spend requires Approved | No ads-pack can trigger live spend without Approved status |
| Auto-reply requires Approved | No CRM or inbox reply can be sent without Approved status |
| Only Owner sets Approved | Agents cannot self-approve; only Owner sets `owner_decision: Approved` |

---

## Required Logging

Every agent session and significant action must produce a `log-entry.schema.json` record. Log entries are written to:
- `logs/AGENT_ACTIVITY_LOG.md` — human-readable append-only table (existing format)
- `09_LOGS/PHASE_LOG.md` — phase-level milestone entries

In future phases (n8n/LangGraph), structured `log-entry.schema.json` JSON records will be written to Google Sheets or a dedicated log store.

---

## How Schemas Support n8n / LangGraph (Future Phases)

No runtime automation is implemented in Phase 3. However, schemas are designed with these future integrations in mind:

### n8n (Phase 4+)
- Each schema field maps directly to a Google Sheets column in the Content Approval Queue.
- `approval_status` drives workflow branching: Draft → no action; Approved → schedule; Published → archive.
- `created_by_agent` identifies which n8n sub-workflow produced the output.
- `log-entry.schema.json` feeds an append-only Sheets log tab.

### LangGraph (Phase 5+)
- Each schema is a typed node output in the LangGraph state graph.
- `approval_status` is a graph state variable that gates downstream node execution.
- `human_review_required: true` in CRM and inbox schemas triggers a LangGraph interrupt for human-in-the-loop review.
- Schema IDs (`content_id`, `brief_id`, etc.) become edge references between graph nodes.

---

## No Runtime Automation in Phase 3

Phase 3 defines schema contracts only. No runtime automation is created in this phase.

| Phase 3 Does | Phase 3 Does NOT |
|-------------|-----------------|
| Define JSON schemas for all agent outputs | Create n8n workflow JSON files |
| Define approval state machine in schema | Connect to any live API |
| Define logging schema | Auto-send any message or content |
| Document which agent uses which schema | Run ads or spend money |
| Document forward-compatibility notes | Auto-publish any content |
