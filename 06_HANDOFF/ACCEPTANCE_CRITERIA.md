# Acceptance Criteria — FnB OS V1

Pass/fail criteria for each phase. All items must pass before phase is marked COMPLETE.

---

## Phase 0 — Environment & Project Setup

### Must Pass (Blocking)

| # | Criteria | Check Method | Status |
|---|----------|-------------|--------|
| 1 | All specified folders exist (00–09) | List directory | ✅ Pass |
| 2 | All specified files created | List files per spec | ✅ Pass |
| 3 | No hardcoded API keys in any file | `grep -r "sk-" .` | ✅ Pass |
| 4 | No hardcoded passwords or tokens | Manual review | ✅ Pass |
| 5 | All JSON schemas are valid JSON | JSON validator | ✅ Pass |
| 6 | `env.example` contains all required variables | Review file | ✅ Pass |
| 7 | PHASE_STATUS.md exists and is accurate | Review file | ✅ Pass |
| 8 | DECISION_LOG.md has at least 5 entries | Review file | ✅ Pass |
| 9 | AGENT_COMMUNICATION_RULES.md is complete | Review file | ✅ Pass |
| 10 | TASK_CONTRACT.md defines the format | Review file | ✅ Pass |
| 11 | NEXT_ACTIONS.md has clear Phase 1 tasks | Review file | ✅ Pass |
| 12 | All test fixtures are valid JSON | JSON validator | ✅ Pass |
| 13 | No n8n workflow JSON files created yet | List 04_WORKFLOWS | ✅ Pass |
| 14 | No production actions taken | Confirm no API calls | ✅ Pass |

### Should Pass (Non-blocking)

| # | Criteria | Status |
|---|----------|--------|
| 1 | BRAIN files have complete structure (even with [FILL]) | ✅ Pass |
| 2 | All agent prompts reference master_system_prompt.md | ✅ Pass |
| 3 | All SOPs have trigger, steps, output, failure handling | ✅ Pass |
| 4 | Workflow inventory lists all planned workflows | ✅ Pass |

---

## Phase 1 — Core Data Layer

### Must Pass (Blocking)

| # | Criteria |
|---|----------|
| 1 | Google Sheet live with all tabs from schema |
| 2 | Service account can read/write Sheet |
| 3 | Test campaign data seeded successfully |
| 4 | Google Drive folders created |
| 5 | Service account has Drive access |
| 6 | n8n can connect to Sheets (test workflow) |
| 7 | Sheet ID in `.env` |
| 8 | Drive Folder ID in `.env` |

---

## Phase 2 — Prompts & SOPs Finalized

| # | Criteria |
|---|----------|
| 1 | All BRAIN files have 0 `[FILL]` placeholders |
| 2 | All prompts reviewed by user |
| 3 | All prompts bumped to v1.0.0 |
| 4 | All SOPs approved by user |
| 5 | QC Agent prompt test run completed |

---

## Phase 3 — Workflow Scaffolding

| # | Criteria |
|---|----------|
| 1 | All 10 workflow JSON files created |
| 2 | No hardcoded credentials in workflow JSON |
| 3 | All workflows use `{{ $env.VAR }}` syntax for secrets |
| 4 | Workflow inventory fully updated |
| 5 | All workflows imported to n8n (not activated) |

---

## Phase 4 — Dry Run

| # | Criteria |
|---|----------|
| 1 | All 5 test fixtures processed successfully |
| 2 | All outputs written to Google Drive |
| 3 | Telegram approval messages sent and received |
| 4 | No live posting, no real messages sent |
| 5 | Error log clean (no open errors) |
| 6 | Execution log shows all steps completed |
