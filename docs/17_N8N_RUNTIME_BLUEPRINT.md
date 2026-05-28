# 17 — n8n Runtime Blueprint Overview

Phase: 7 — n8n Runtime Blueprint
Created By: Claude Code (Builder, AGT-02) — 2026-05-28
Status: BLUEPRINT_DRAFT

---

## What Is the Runtime Blueprint?

The runtime blueprint is a set of design documents that describe how n8n automation workflows will connect Brand Brain, schemas, templates, the approval gate, logs, and handoff files. It is a forward-looking design — not an implementation.

The runtime blueprint answers: "When n8n workflows are built in a future phase, how should they be structured, what should they connect to, and what rules must they follow?"

---

## Why Phase 7 Does Not Create Workflow JSON

Phase 7 deliberately creates markdown blueprint files only — no n8n workflow JSON, no executable code, no runtime connections. This is intentional for the following reasons:

| Reason | Detail |
|--------|--------|
| Owner infrastructure not yet confirmed | n8n instance type (cloud/self-hosted), Telegram channel, and Google Sheets structure have not been finalized by Owner |
| Brand data incomplete | Real prices, address, hours, offers still contain placeholders — workflows cannot produce accurate output until Owner fills Brand Brain |
| Approval channel not configured | Telegram Bot or Google Sheet approval table has not been set up by Owner |
| Credential placeholders only | No real API keys or credentials exist yet — workflows cannot authenticate to any platform |
| Design must be reviewed first | Codex must review and Owner must approve the blueprint before any implementation begins |

Phase 7 outputs are design documents. Phase 8 will produce importable n8n workflow JSON skeletons based on this blueprint.

---

## Modules Covered by This Blueprint

| File | Module | Purpose |
|------|--------|---------|
| `runtime-blueprints/n8n/content-auto-blueprint.md` | Content Auto | Trigger → Brand Brain → Draft → Validate → Log → Approval Queue |
| `runtime-blueprints/n8n/approval-gate-blueprint.md` | Approval Gate | Receive draft → Notify Owner → Wait → Route by decision |
| `runtime-blueprints/n8n/logging-blueprint.md` | Logging | Log schema, destinations, n8n log nodes, error log handling |
| `runtime-blueprints/n8n/data-source-blueprint.md` | Data Sources | Repo sources, future runtime sources, credential placeholders, source of truth |
| `runtime-blueprints/n8n/error-handling-blueprint.md` | Error Handling | Error types, stop rules, error node plan, approval/credential/API error rules |

---

## Future n8n Runtime Principles

These principles must be applied to every n8n workflow built in Phase 8 and beyond.

| Principle | Rule |
|-----------|------|
| Importable JSON | Every workflow is distributed as a JSON file that can be imported into n8n via the UI |
| `active: false` by default | All imported workflows start with `active: false` — Owner must manually activate after review |
| Placeholder credentials | All credentials in workflow JSON use placeholder names — never real keys |
| Approval gate required | Every content output, CRM message, ads pack, and inbox reply must pass the approval gate before any customer-facing or budget-spending action |
| Logs required | Every execution must write a structured log entry — no execution is silent |
| No auto-publish | No workflow may publish content to any platform without `approval_status: Approved` set by Owner |
| No auto-reply | No workflow may send a reply to a real customer without Owner approval |
| No auto-spend | No workflow may commit any ads budget without Owner approval |
| Error stops execution | Any blocking error must halt the workflow, write an error log, and notify Owner if needed |
| Brand Brain is required | No content workflow may run without loading and validating Brand Brain data first |

---

## How This Connects to Phase 1–6

| Phase | What It Built | How Phase 7 Connects |
|-------|--------------|---------------------|
| Phase 1 | Brand Brain foundation (01_BRAIN/ files) | Phase 7 blueprints read from `brand-brain/vi-cuon.md` |
| Phase 2 | Agent prompt files and SOPs | Phase 7 blueprints describe how n8n nodes will call agent-equivalent logic |
| Phase 3 | I/O schemas (JSON Schema) | Phase 7 blueprints reference all 7 schemas for validation nodes |
| Phase 4 | Module SOPs and output templates | Phase 7 blueprints reference all 7 templates as output formats |
| Phase 5 | Sample outputs | Phase 7 blueprints reference samples as test fixtures for future workflow testing |
| Phase 6 | OS readiness checklist and pre-runtime plan | Phase 7 implements the n8n design step identified in Phase 6 pre-runtime plan |

---

## Next Steps After Phase 7

1. Codex reviews all Phase 7 blueprint files → PASS / FAIL
2. Owner approves commit → `OWNER_APPROVED`
3. Owner confirms: n8n instance type, approval channel, brand data filled
4. Phase 8 begins: create importable n8n workflow JSON skeletons (not active, placeholders only)

---

_This is a design document only. Implementation begins in Phase 8._
