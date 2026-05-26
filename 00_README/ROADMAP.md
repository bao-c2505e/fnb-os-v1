# Roadmap — FnB OS V1

## Phase Overview

| Phase | Name | Status | Goal |
|-------|------|--------|------|
| 0 | Environment & Project Setup | 🔄 IN PROGRESS | Repo structure, schemas, rules, checklists |
| 1 | Core Data Layer | ⏳ PENDING | Google Sheets schema live, test data seeded |
| 2 | Agent Prompts & SOPs Finalized | ⏳ PENDING | All prompts reviewed, SOPs approved |
| 3 | n8n Workflow Scaffolding | ⏳ PENDING | Workflow JSON created, not activated |
| 4 | End-to-End Dry Run | ⏳ PENDING | Full flow tested with test fixtures, no live posting |
| 5 | Telegram Approval Gate | ⏳ PENDING | Approval flow working in staging |
| 6 | Soft Launch — Content Auto | ⏳ PENDING | Content generation live for Vị Cuốn |
| 7 | Soft Launch — Ads Pack Auto | ⏳ PENDING | Ads brief generation live |
| 8 | Soft Launch — CRM Follow-up | ⏳ PENDING | CRM automation live |
| 9 | Soft Launch — Comment Reply | ⏳ PENDING | Inbox reply automation live |
| 10 | Full System Monitoring | ⏳ PENDING | Daily summary, error alerts, audit logs |

---

## Phase 0 — Environment & Project Setup

**Goal:** Clean repo foundation. No code, no workflows, no live actions.

**Deliverables:**
- [x] Repo folder structure
- [x] `env.example` with all required variables
- [x] Agent communication rules
- [x] Session handoff rules
- [x] Task contract format
- [x] Setup checklists (all tools)
- [x] Google Sheet schema spec
- [x] n8n credentials checklist
- [x] Phase status and decision logs
- [x] Security rules
- [x] Next actions for Phase 1

**Acceptance Criteria:** See `06_HANDOFF/ACCEPTANCE_CRITERIA.md`

---

## Phase 1 — Core Data Layer

**Goal:** Google Sheets live with correct schema. Test data seeded.

**Deliverables:**
- Google Sheet created with all tabs matching `08_DEPLOY/google_sheet_schema.md`
- Test campaign data seeded (Combo Trưa, Weekend Special)
- Service account credentials configured
- n8n can read/write Sheets successfully
- Dry-run log written

**Gate:** User approves Sheet structure before Phase 2

---

## Phase 2 — Agent Prompts & SOPs Finalized

**Goal:** All agent prompts reviewed and locked. SOPs approved.

**Deliverables:**
- All `02_PROMPTS/*.md` files reviewed and version-locked
- All `03_SOPS/*.md` files reviewed and approved
- Prompt test runs completed with test fixtures
- Quality check scores documented

**Gate:** User approves prompts and SOPs

---

## Phase 3 — n8n Workflow Scaffolding

**Goal:** All n8n workflow JSON files created and validated. Not activated.

**Deliverables:**
- All workflow JSON in `04_WORKFLOWS/`
- Workflow inventory updated
- Credentials mapped (not yet live)
- Dry-run documentation

**Gate:** User approves workflow structure

---

## Phase 4 — End-to-End Dry Run

**Goal:** Full system tested with test fixtures. No live posting.

**Deliverables:**
- All test fixtures run through full pipeline
- Output compared to acceptance criteria
- Error log reviewed and cleared
- Execution log documented

**Gate:** User approves dry-run results

---

## Phase 5+ — Staged Launch

Each feature goes live one at a time:
1. Content generation
2. Ads brief
3. CRM follow-up
4. Comment reply
5. Full monitoring

Each stage requires user approval via Telegram before activation.
