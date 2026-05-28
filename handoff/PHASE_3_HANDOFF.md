# Phase 3 Handoff

Phase: 3 — Brand Brain + Input/Output Schemas
Created By: Claude Code (Builder, AGT-02)
Date: 2026-05-28
Status: BUILDER_DONE_PENDING_REVIEW

---

## Phase Goal

Create the default Brand Brain for Vị Cuốn and all reusable input/output schemas for core FnB OS V1 agents.

---

## Files Created

### New Files

| File | Description |
|------|-------------|
| `brand-brain/vi-cuon.md` | Default Brand Brain for Vị Cuốn — brand identity, audience, tone, content pillars, offer rules, compliance, replacement guide |
| `schemas/content-output.schema.json` | Content output schema — captions, hooks, scripts, CTAs |
| `schemas/creative-brief.schema.json` | Creative brief schema — image/video/design briefs with AI prompts and QA checklist |
| `schemas/ads-pack.schema.json` | Ads pack schema — ad copy, headlines, audience targeting |
| `schemas/crm-followup.schema.json` | CRM follow-up sequence schema — message sequences with human_review_required: true |
| `schemas/comment-inbox-reply.schema.json` | Comment/inbox reply draft schema — escalation rules, no auto-reply |
| `schemas/approval-status.schema.json` | Approval status schema — 7-state machine, Owner-only Approved gate |
| `schemas/log-entry.schema.json` | Log entry schema — structured logs for all agents |
| `docs/09_BRAND_BRAIN_SYSTEM.md` | Brand Brain system documentation — what it is, how to replace it, what agents must read |
| `docs/10_SCHEMA_SYSTEM.md` | Schema system documentation — registry, agent mapping, approval state machine, n8n/LangGraph notes |
| `handoff/PHASE_3_HANDOFF.md` | This file |

### Updated Files

| File | Update |
|------|--------|
| `handoff/CURRENT_PHASE.md` | Status updated to Phase 3 BUILDER_DONE_PENDING_REVIEW |
| `handoff/SESSION_SUMMARY.md` | Phase 3 session context added |
| `logs/AGENT_ACTIVITY_LOG.md` | Phase 3 build row appended |
| `09_LOGS/PHASE_LOG.md` | Phase 3 entry prepended |

---

## Scope Completed

| Scope Item | Status |
|-----------|--------|
| `brand-brain/vi-cuon.md` created | DONE |
| 7 JSON schemas created | DONE |
| `docs/09_BRAND_BRAIN_SYSTEM.md` created | DONE |
| `docs/10_SCHEMA_SYSTEM.md` created | DONE |
| `handoff/CURRENT_PHASE.md` updated | DONE |
| `handoff/SESSION_SUMMARY.md` updated | DONE |
| `logs/AGENT_ACTIVITY_LOG.md` updated | DONE |
| `09_LOGS/PHASE_LOG.md` updated | DONE |
| No n8n workflow created | CONFIRMED |
| No runtime automation code | CONFIRMED |
| No scripts created | CONFIRMED |
| No API keys hardcoded | CONFIRMED |
| No auto-post triggered | CONFIRMED |
| No commit made | CONFIRMED |
| No push made | CONFIRMED |

---

## Validation Checklist

| Check | Result |
|-------|--------|
| All files in scope_files only | PASS |
| No secrets hardcoded | PASS — no API keys, tokens, passwords in any file |
| No auto-post logic | PASS — all schemas require `approval_status: Approved` before any action |
| No n8n workflow JSON | PASS — schemas only, no workflow files |
| No runtime automation | PASS — markdown + JSON schema only |
| `human_review_required: true` in CRM schema | PASS |
| `human_review_required: true` in inbox reply schema | PASS |
| Approval state machine defined | PASS — 7 states, Owner-only Approved gate |
| Brand Brain replaceable | PASS — documented in both `vi-cuon.md` and `09_BRAND_BRAIN_SYSTEM.md` |
| Vị Cuốn as default brand | PASS — `brand_id: VQ`, `brand_name: Vị Cuốn` throughout |
| JSON schemas valid (Draft-07) | See JSON Validation section below |
| Logs updated | PASS |

---

## Known Limitations

1. **Offer details not filled** — `[OWNER_TO_PROVIDE_OFFER]` placeholder used throughout schemas. Owner must provide real offer data before content agents can produce offer-inclusive outputs.
2. **Menu prices not locked** — 60k–80k VND range is approximate. Owner should confirm exact pricing before it appears in public-facing content.
3. **Phase 3 schemas are contracts, not live integrations** — n8n and LangGraph integrations are Phase 4+ work.
4. **No sample schema instances** — Filled example records are not included in Phase 3 to keep scope clean. Sample instances can be added in Phase 4+ or by request.

---

## Codex Review Instructions

Codex should review all 11 new files in this phase.

**Review criteria:**

1. **Secret scan** — Confirm no API keys, tokens, passwords, or credentials in any file.
2. **Scope check** — Confirm no files outside the scope list were created or modified.
3. **No automation** — Confirm no n8n workflow JSON, no runtime scripts, no live API calls.
4. **Schema structure** — Confirm all 7 JSON schemas are valid JSON and contain required fields: `approval_status`, `created_by_agent`, `created_at`.
5. **Approval gate** — Confirm `approval_status` is present in all output schemas and `human_review_required: true` (const) is set in CRM and inbox reply schemas.
6. **Brand Brain completeness** — Confirm `brand-brain/vi-cuon.md` covers all required sections: Brand Snapshot, Target Customers, Core Selling Points, Tone of Voice, Content Pillars, Offer Rules, Compliance/Safety, Replaceable Brand Context.
7. **No auto-post language** — Confirm no file contains instructions to auto-publish, auto-send, or auto-schedule.
8. **No fake content** — Confirm no fake reviews, fake testimonials, or invented offers in any file.

**Expected review output:** PASS / PASS WITH NOTES / FAIL

---

## Next Phase Recommendation

**Phase 4 — Agent I/O Wiring + Sample Instances**

Recommended scope:
- Create filled example JSON instances for each schema (using Vị Cuốn sample data)
- Define the agent-to-schema routing map as a machine-readable config
- Document how n8n reads Brand Brain and produces schema-valid outputs
- Begin Phase 4 n8n workflow planning (not build)

---

## Commit Instruction

**Do not commit until:**
1. Codex reviews all files and returns PASS or PASS WITH NOTES.
2. Owner sets `OWNER_APPROVED` on this phase.

When approved, commit all Phase 3 files together as a single commit.

Suggested commit message:
```
feat(phase-3): add Brand Brain and I/O schemas for core agents

- brand-brain/vi-cuon.md: default Brand Brain for Vị Cuốn
- schemas/: 7 JSON Schema Draft-07 files for all core agent outputs
- docs/09_BRAND_BRAIN_SYSTEM.md + docs/10_SCHEMA_SYSTEM.md
- handoff/PHASE_3_HANDOFF.md + state file updates
```
