# Next Actions — FnB OS V1

Prioritized queue of what needs to happen next.
Updated by Chief Architect or Builder Agents after each session.

---

## Priority Legend
- 🔴 BLOCKED — cannot proceed without this
- 🟠 HIGH — needed for current phase
- 🟡 MEDIUM — needed soon but not blocking
- 🟢 LOW — nice to have, next phase

---

## Current Queue — Phase 0.4 Testing → Phase 1

### 🔴 BLOCKED — User Actions Required (run in n8n)

1. **Finish filling `.env`** *(Phase 0.2 — In Progress)*
   - File: `D:\FNB_OS_V1\.env`
   - Remaining: OPENAI_API_KEY, GEMINI_API_KEY, GOOGLE_DRIVE_ROOT_FOLDER_ID,
     GOOGLE_SHEET_CONTROL_CENTER_ID, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID,
     N8N_API_KEY, GITHUB_TOKEN
   - Blocker for: smoke test runs

2. **Import + run 5 smoke test workflows in n8n** *(Phase 0.4 — Ready)*
   - Guide: `docs/phase-0/PHASE_0_4_N8N_SMOKE_TESTS.md`
   - Files to import (from `n8n/smoke-tests/`):
     - `smoke-01-telegram-credential-test.json`
     - `smoke-02-google-sheets-read-test.json`
     - `smoke-03-google-drive-folder-search-test.json`
     - `smoke-04-openai-short-reply-test.json`
     - `smoke-05-gemini-short-reply-test.json`
   - Manual fields to set after import:
     - SMOKE-01: replace `REPLACE_WITH_TELEGRAM_CHAT_ID` with real chat ID
     - SMOKE-02: select document `FNB_OS_V1_CONTROL_CENTER` → tab `Config`
   - Results log: `logs/PHASE_0_4_SMOKE_TEST_RESULTS.md`
   - Constraint: keep all workflows `active = OFF`
   - Blocker for: Phase 1

3. **Commit Phase 0.4 results**
   - After all 5 PASS, commit:
     ```
     git add n8n/ docs/ logs/ SESSION_SUMMARY.md 09_LOGS/PHASE_LOG.md 06_HANDOFF/NEXT_ACTIONS.md
     git commit -m "feat(phase-0.4): add n8n smoke test workflows and docs"
     git push
     ```

---

---

### 🟠 HIGH — Phase 1 Tasks (After 0.4 Complete)

4. **Fill BRAIN file placeholders**
   - Files: `01_BRAIN/brand_brain.md` and all other BRAIN files
   - Action: Replace all `[FILL: ...]` with real Vị Cuốn data
   - Blocker for: Phase 1 data layer, all agent prompts

5. **Create Google Sheet — Control Center**
   - Schema: `08_DEPLOY/google_sheet_schema.md`
   - Agent: Claude Code (Builder)
   - Output: Live Google Sheet with all 11 tabs

6. **Create Google Drive folder structure**
   - Schema: `08_DEPLOY/google_drive_structure.md`
   - Agent: Claude Code (Builder)
   - Output: Drive folders created, IDs back-filled in `.env`

7. **Seed test data in Google Sheet**
   - Fixtures: `07_TEST_FIXTURES/test_campaign_combo_trua.json`
   - Agent: Claude Code (Builder)
   - Output: Test campaign rows added

---

### 🟡 MEDIUM — Phase 2 Tasks

8. **Review and lock all agent prompts**
   - Files: `02_PROMPTS/*.md`
   - Agent: ChatGPT (Chief Architect) + User
   - Output: All prompts version-bumped to v1.0.0

9. **Review and lock all SOPs**
   - Files: `03_SOPS/*.md`
   - Agent: ChatGPT (Chief Architect) + User

---

## Completed Actions

| # | Action | Completed By | Date |
|---|--------|-------------|------|
| 1 | Create Phase 0 repo structure (75 files) | Claude Code (Builder) | 2026-05-26 |
| 2 | Create all BRAIN files | Claude Code (Builder) | 2026-05-26 |
| 3 | Create all agent prompts | Claude Code (Builder) | 2026-05-26 |
| 4 | Create all SOPs | Claude Code (Builder) | 2026-05-26 |
| 5 | Create all JSON schemas | Claude Code (Builder) | 2026-05-26 |
| 6 | Create HANDOFF files | Claude Code (Builder) | 2026-05-26 |
| 7 | Create test fixtures | Claude Code (Builder) | 2026-05-26 |
| 8 | Create DEPLOY checklists | Claude Code (Builder) | 2026-05-26 |
| 9 | Create log templates | Claude Code (Builder) | 2026-05-26 |
| 10 | Phase 0.1 — Create `.env` (placeholders), `.env.example`, `.gitignore`, `check_env_safety.py` | Claude Code (Builder) | 2026-05-26 |
| 11 | Phase 0.1 — `git init`, safety check, first commit pushed to GitHub | Human + Claude Code | 2026-05-26 |
| 12 | Phase 0.3 — n8n credential guide (`n8n_credentials_step_by_step.md`) | Claude Code (Builder) | 2026-05-26 |
| 13 | Phase 0.3 — Created `09_LOGS/PHASE_LOG.md` | Claude Code (Builder) | 2026-05-26 |
| 14 | Phase 0.3 — Updated `06_HANDOFF/NEXT_ACTIONS.md` | Claude Code (Builder) | 2026-05-26 |
| 15 | Phase 0.4 — Created 5 smoke test workflow JSONs in `n8n/smoke-tests/` | Claude Code (Builder) | 2026-05-26 |
| 16 | Phase 0.4 — Created `docs/phase-0/PHASE_0_4_N8N_SMOKE_TESTS.md` | Claude Code (Builder) | 2026-05-26 |
| 17 | Phase 0.4 — Created `logs/PHASE_0_4_SMOKE_TEST_RESULTS.md` | Claude Code (Builder) | 2026-05-26 |
| 18 | Phase 0.4 — Created `SESSION_SUMMARY.md` | Claude Code (Builder) | 2026-05-26 |
