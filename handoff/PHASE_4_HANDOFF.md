# Phase 4 Handoff

**Phase:** Phase 4 — Module SOP + Output Templates
**Builder:** Claude Code (AGT-02)
**Date:** 2026-05-28
**Status:** BUILDER_DONE_PENDING_REVIEW

---

## Goal

Create practical module SOPs and reusable output templates for the core FnB OS V1 marketing modules, turning Phase 2 agent roles and Phase 3 schemas into concrete operating instructions and structured output formats.

---

## Files Created

### Module SOPs (6)
| File | Module |
|------|--------|
| `module-sops/content-auto-sop.md` | Content Auto |
| `module-sops/creative-asset-auto-sop.md` | Creative Asset Auto |
| `module-sops/ads-pack-auto-sop.md` | Ads Pack Auto |
| `module-sops/crm-followup-auto-sop.md` | CRM Follow-Up Auto |
| `module-sops/comment-inbox-assistant-sop.md` | Comment Inbox Assistant |
| `module-sops/approval-publishing-sop.md` | Approval & Publishing |

### Output Templates (7)
| File | Schema Mirrored |
|------|-----------------|
| `templates/content-output-template.md` | `schemas/content-output.schema.json` |
| `templates/creative-brief-template.md` | `schemas/creative-brief.schema.json` |
| `templates/ads-pack-template.md` | `schemas/ads-pack.schema.json` |
| `templates/crm-followup-template.md` | `schemas/crm-followup.schema.json` |
| `templates/comment-inbox-reply-template.md` | `schemas/comment-inbox-reply.schema.json` |
| `templates/approval-status-template.md` | `schemas/approval-status.schema.json` |
| `templates/log-entry-template.md` | `schemas/log-entry.schema.json` |

### System Docs (2)
| File | Purpose |
|------|---------|
| `docs/11_MODULE_SOP_SYSTEM.md` | SOP registry, approval rules, why no debug by Owner, why no screenshots |
| `docs/12_OUTPUT_TEMPLATE_SYSTEM.md` | Template registry, schema mapping, n8n/LangGraph forward-compatibility, brand replacement guide |

### Handoff & Logs (4)
| File | Action |
|------|--------|
| `handoff/PHASE_4_HANDOFF.md` | This file — created |
| `handoff/CURRENT_PHASE.md` | Updated to Phase 4 BUILDER_DONE_PENDING_REVIEW |
| `handoff/SESSION_SUMMARY.md` | Updated with Phase 4 session context |
| `logs/AGENT_ACTIVITY_LOG.md` | New row prepended |
| `09_LOGS/PHASE_LOG.md` | New entry prepended |

---

## Scope Completed

- [x] 6 module SOP files — each with 8 required sections
- [x] 7 output templates — each mirroring Phase 3 schema fields exactly
- [x] `approval_status: Draft` default on all templates
- [x] `human_review_required: true` on CRM and inbox reply templates
- [x] `[OWNER_TO_PROVIDE_OFFER]` on all offer fields
- [x] 2 system docs explaining SOP and template systems
- [x] Phase 4 handoff, current phase, session summary updated
- [x] Activity log and phase log updated
- [x] No n8n workflow created
- [x] No runtime code or script created
- [x] No API keys or secrets added
- [x] No commit or push

---

## Validation Checklist

| Check | Result |
|-------|--------|
| All 6 SOP files created | PASS |
| All 7 template files created | PASS |
| docs/11 and docs/12 created | PASS |
| All templates include `approval_status` | PASS |
| CRM template has `human_review_required: true` | PASS |
| Inbox reply template has `human_review_required: true` | PASS |
| All offer fields use `[OWNER_TO_PROVIDE_OFFER]` | PASS |
| No JSON schema files modified | PASS |
| No n8n workflow file created | PASS |
| No runtime script created | PASS |
| No secrets or API keys added | PASS |
| No commit executed | PASS |
| No push executed | PASS |

---

## Known Limitations

1. **Offer values are placeholders.** All offer/pricing fields use `[OWNER_TO_PROVIDE_OFFER]`. Owner must confirm actual offers before agents can produce offer-inclusive outputs.
2. **No sample filled instances.** Phase 4 provides templates (structures), not completed example outputs. Sample filled instances are Phase 5 scope.
3. **Automation not wired.** SOPs define the process but n8n/LangGraph integration is Phase 5+.
4. **Brand Brain placeholders remain.** Some fields in `brand-brain/vi-cuon.md` still contain `[FILL]` placeholders (address, phone, confirmed pricing) — these must be filled by Owner before production use.

---

## Codex Review Instructions

Codex must verify:

1. Each SOP file uses the required 8-section structure: Purpose, Required Inputs, Process Steps, Output Template, Approval Gate, Logging Requirements, Human Escalation Rules, Done Criteria.
2. Each SOP references the correct schema and template file.
3. Each template mirrors all required fields from its corresponding schema (check against `schemas/*.schema.json`).
4. `approval_status: Draft` is the default in all templates.
5. `human_review_required: true` is present in `crm-followup-template.md` and `comment-inbox-reply-template.md`.
6. No template hardcodes a price, offer value, or secret.
7. No n8n workflow file exists in the repo after this build.
8. No script or runtime code was created.
9. `docs/11_MODULE_SOP_SYSTEM.md` explains the SOP registry and approval process.
10. `docs/12_OUTPUT_TEMPLATE_SYSTEM.md` explains the template-schema mapping and brand replacement guide.

Output format: `PASS` / `PASS WITH NOTES` / `FAIL` with specific findings.

---

## Next Phase Recommendation

**Phase 5 — Sample Filled Instances + n8n Workflow Scaffolding**

Suggested scope:
- Create 1–2 filled sample instances per module using the Phase 4 templates (demonstrating what a real Content Agent or CRM Agent output looks like).
- Begin n8n workflow scaffolding for content approval routing.
- Wire Brand Brain `[FILL]` fields with Owner-confirmed values.

---

## Commit Instruction

Do not commit until:
1. Codex reviews all Phase 4 files and outputs `PASS` or `PASS WITH NOTES`.
2. Owner reviews Codex verdict and sets `OWNER_APPROVED`.

Commit command (after approval):
```
git add module-sops/ templates/ docs/11_MODULE_SOP_SYSTEM.md docs/12_OUTPUT_TEMPLATE_SYSTEM.md handoff/PHASE_4_HANDOFF.md handoff/CURRENT_PHASE.md handoff/SESSION_SUMMARY.md logs/AGENT_ACTIVITY_LOG.md 09_LOGS/PHASE_LOG.md
git commit -m "docs: add phase 4 module SOPs and output templates"
```
