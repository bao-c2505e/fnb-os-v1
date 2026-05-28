# Phase 7 Handoff — n8n Runtime Blueprint

Phase: 7 — n8n Runtime Blueprint
Created By: Claude Code (Builder, AGT-02) — 2026-05-28
Status: BUILDER_DONE_PENDING_REVIEW

---

## Phase Name

Phase 7 — n8n Runtime Blueprint

## Goal

Design the runtime blueprint for future n8n implementation. Define how n8n will connect Brand Brain, schemas, templates, the approval gate, logs, and handoff. All outputs are markdown design documents only — no workflow JSON, no executable code, no live connections.

---

## Files Created

| File | Type | Purpose |
|------|------|---------|
| `runtime-blueprints/n8n/content-auto-blueprint.md` | Blueprint | Content auto workflow: trigger → Brand Brain → draft → validate → log → approval queue |
| `runtime-blueprints/n8n/approval-gate-blueprint.md` | Blueprint | Approval gate: receive draft → notify Owner → wait → route by decision |
| `runtime-blueprints/n8n/logging-blueprint.md` | Blueprint | Logging: schema refs, destinations, n8n log nodes, error log handling |
| `runtime-blueprints/n8n/data-source-blueprint.md` | Blueprint | Data sources: repo sources, future runtime sources, credential placeholders, source of truth |
| `runtime-blueprints/n8n/error-handling-blueprint.md` | Blueprint | Error handling: error types, stop rules, error node plan, hard-block rules |
| `docs/17_N8N_RUNTIME_BLUEPRINT.md` | Overview doc | What the blueprint is, why no JSON yet, modules covered, runtime principles, Phase 1–6 connection |
| `docs/18_RUNTIME_DATA_FLOW.md` | Data flow doc | Full 12-step data flow with input refs, output refs, failure paths |
| `docs/19_APPROVAL_GATE_RUNTIME_DESIGN.md` | Design doc | State machine, allowed/blocked transitions, Owner-only approval, CRM/inbox lock, ads spend lock, audit log |
| `handoff/PHASE_7_HANDOFF.md` | Handoff | This file |

---

## Files Updated

| File | Update |
|------|--------|
| `logs/AGENT_ACTIVITY_LOG.md` | New row prepended for Phase 7 build |
| `09_LOGS/PHASE_LOG.md` | New entry prepended for Phase 7 |
| `handoff/CURRENT_PHASE.md` | Updated to Phase 7 BUILDER_DONE_PENDING_REVIEW |
| `handoff/SESSION_SUMMARY.md` | Phase 7 session context added at top |

---

## Scope Completed

| Item | Status |
|------|--------|
| `runtime-blueprints/n8n/` folder created | Done |
| Content auto workflow blueprint | Done |
| Approval gate blueprint | Done |
| Logging blueprint | Done |
| Data source blueprint | Done |
| Error handling blueprint | Done |
| n8n runtime overview doc (17) | Done |
| Runtime data flow doc (18) | Done |
| Approval gate runtime design doc (19) | Done |
| Handoff file created | Done |
| Activity log updated | Done |
| Phase log updated | Done |
| CURRENT_PHASE updated | Done |
| SESSION_SUMMARY updated | Done |

---

## Validation Checklist

| Check | Result |
|-------|--------|
| No real n8n workflow JSON created | PASS |
| No runtime code or script created | PASS |
| No schema JSON modified | PASS |
| No secrets, tokens, API keys, or credentials added | PASS |
| All new files are markdown only | PASS |
| Approval gate is present and defined | PASS |
| Logging requirements are defined | PASS |
| Error handling is defined | PASS |
| `active: false` rule is documented | PASS |
| Credential placeholder rule is documented | PASS |
| No auto-publish rule is documented | PASS |
| No auto-reply rule is documented | PASS |
| No auto-spend rule is documented | PASS |
| Scope limited to `runtime-blueprints/n8n/` and `docs/` | PASS |

---

## Known Limitations

| Limitation | Detail |
|-----------|--------|
| No workflow JSON | Phase 7 does not produce importable n8n workflow files — these are Phase 8 scope |
| No live connections | No n8n nodes are connected to any real data source, credential, or platform |
| Brand data incomplete | Brand Brain still has placeholder fields (prices, address, hours, offers) — Owner must fill before runtime |
| Approval channel not configured | Telegram Bot and Google Sheet approval table are future setup — Owner must confirm channel preference |
| n8n instance not specified | Owner has not yet confirmed n8n cloud vs. self-hosted — Phase 8 implementation depends on this |
| Only content-auto workflow blueprinted | Full blueprint for creative-asset, ads-pack, CRM, and inbox reply workflows are deferred to Phase 8 |

---

## Codex Review Instructions

Codex (AGT-03): Please review all Phase 7 files listed above.

**Review focus:**
1. All 5 blueprint files in `runtime-blueprints/n8n/` — do they cover their required sections per Phase 7 spec?
2. `docs/17_N8N_RUNTIME_BLUEPRINT.md` — does it correctly explain what the blueprint is and why no JSON yet?
3. `docs/18_RUNTIME_DATA_FLOW.md` — does the 12-step flow cover the full path from Owner request to handoff/execution?
4. `docs/19_APPROVAL_GATE_RUNTIME_DESIGN.md` — does it define state machine, allowed/blocked transitions, and all safety locks?
5. Are any secrets, credentials, or real API keys present? (Should be zero.)
6. Are any n8n workflow JSON files present? (Should be zero.)
7. Are any executable scripts present? (Should be zero.)

**Output format:** PASS / PASS WITH NOTES / FAIL

---

## Next Phase Recommendation

**Phase 8 — n8n Importable Workflow Skeletons**

Build actual importable n8n workflow JSON files based on Phase 7 blueprints. All workflows must:
- Be importable via n8n UI (Export/Import JSON)
- Start with `active: false`
- Use placeholder credential names only
- Include all nodes described in Phase 7 blueprints
- Include error trigger and error handler nodes
- Include logging nodes
- Include approval gate nodes
- Produce no output to real platforms

**Prerequisites for Phase 8:**
- [ ] Owner confirms n8n instance type (cloud / self-hosted)
- [ ] Owner confirms approval channel (Telegram / Google Sheet)
- [ ] Owner fills Brand Brain placeholder fields
- [ ] Phase 7 Codex PASS and Owner approval (commit Phase 7 first)

---

## Commit Instruction

**Do not commit Phase 7 files until:**
1. Codex reviews all files listed above → PASS or PASS WITH NOTES
2. Owner sets `OWNER_APPROVED` on the Phase 7 command

Only then: commit all Phase 7 files to `main`.
