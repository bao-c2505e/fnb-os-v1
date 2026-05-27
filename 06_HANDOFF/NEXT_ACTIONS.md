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

## CURRENT STATE: Phase 1.5 — CLOSED | Content Pack Validation & Sample Queue committed | Next: Phase 1.6

**Phase 0.6–0.15:** CLOSED
**Phase 1.1:** CLOSED (commit d054f65)
**Phase 1.2:** CLOSED (commit a261763, metadata: 75dd288)
**Phase 1.3:** CLOSED (commit 01def32, metadata: bd55fab)
**Phase 1.4:** CLOSED (commit d19bce7, metadata: 898921d)
**Phase 1.5:** CLOSED (commit e18123b, Codex PASS — Owner approved)
**Current command:** CMD-1.5-001 — Status: CLOSED

---

## 🔴 IMMEDIATE — Open Phase 1.6

### Step 1 — ChatGPT: Open Phase 1.6 — Manual Content Pack Runbook

Phase 1.5 CLOSED. ChatGPT (Chief Architect) mở Phase 1.6 qua `commands/COMMAND_INBOX.md`.

Phase 1.6 đề xuất: Manual Content Pack Runbook — hướng dẫn Owner chạy tay một Content Pack hoàn chỉnh từ đầu đến cuối sử dụng 05_VALIDATION_QUEUE + 04_CONTENT_PACK_GENERATOR + 03_APPROVAL_PIPELINE.

### Step 2 — Owner: Điền [FILL] ưu tiên cao để unblock queue

Các [FILL] quan trọng nhất (ảnh hưởng 7–9/10 queue items):
1. Địa chỉ chi tiết → `01_BRAIN/brand_brain.md`
2. Số điện thoại → `01_BRAIN/brand_brain.md`
3. Giá Combo Trưa (OF-01) → `02_CONTENT_ENGINE/offer_engine.md`
4. Offer status OF-01 → OF-08 (ACTIVE/INACTIVE) → `02_CONTENT_ENGINE/offer_engine.md`

---

## 🟠 HIGH — Phase 1.5 (CLOSED)

---

## 🟠 HIGH — Phase 0.6 Gate (must complete in order)

### Step 1 — Codex: Re-review Phase 0.6

Review the following files against acceptance criteria in `docs/phase-0/PHASE_0_6_COMMAND_INTAKE.md`:

1. `commands/COMMAND_INBOX.md` — no `ACCEPTED` status; uses `ASSIGNED`
2. `commands/COMMAND_STATUS.md` — 10-state lifecycle; no `Codex (Builder)` label
3. `commands/COMMAND_TEMPLATE.md` — all required fields present
4. `schemas/command.schema.json` — matches template; validates with `python -m json.tool`
5. `docs/phase-0/PHASE_0_6_COMMAND_INTAKE.md` — Builder = Claude Code only; Reviewer = Codex only

If REVIEW_PASS → update CMD-0.6-001 status → `REVIEW_PASS` → notify Owner.
If REVIEW_FAIL → record reason in `review_notes`; update status → `REVIEW_FAIL`; return to Builder.

### Step 2 — Owner: Approve Phase 0.6

After Codex REVIEW_PASS:
- Review output summary in `handoff/SESSION_SUMMARY.md`.
- If satisfied, update CMD-0.6-001 status → `OWNER_APPROVED`.

### Step 3 — Owner: Commit Phase 0.6

After OWNER_APPROVED:

```
git add commands/ schemas/command.schema.json docs/phase-0/PHASE_0_6_COMMAND_INTAKE.md handoff/ logs/ 09_LOGS/PHASE_LOG.md 06_HANDOFF/NEXT_ACTIONS.md
git commit -m "feat(phase-0.6): add agent command intake layer"
git push
```

Update CMD-0.6-001 status → `CLOSED`.

### Step 4 — ChatGPT: Open Phase 0.7

Only after Phase 0.6 commit is confirmed in git log.
ChatGPT issues next command via `commands/COMMAND_INBOX.md`.

---

## 🔴 BLOCKED — Awaiting Phase 0.6 CLOSED before any item below can start

### Phase 0.4 Smoke Tests (Owner must run in n8n)

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

---

## 🟡 MEDIUM — Phase 1 Roadmap (after all Phase 0 gates passed)

3. **Fill BRAIN file placeholders**
   - Files: `01_BRAIN/brand_brain.md` and all other BRAIN files
   - Action: Replace all `[FILL: ...]` with real Vị Cuốn data
   - Blocker for: Phase 1 data layer, all agent prompts

4. **Create Google Sheet — Control Center**
   - Schema: `08_DEPLOY/google_sheet_schema.md`
   - Agent: Claude Code (Builder)

5. **Create Google Drive folder structure**
   - Schema: `08_DEPLOY/google_drive_structure.md`
   - Agent: Claude Code (Builder)

6. **Seed test data in Google Sheet**
   - Fixtures: `07_TEST_FIXTURES/test_campaign_combo_trua.json`
   - Agent: Claude Code (Builder)

---

## 🟢 LOW — Phase 2 Roadmap

7. **Review and lock all agent prompts**
   - Files: `02_PROMPTS/*.md`
   - Agent: ChatGPT (Chief Architect) + Owner

8. **Review and lock all SOPs**
   - Files: `03_SOPS/*.md`
   - Agent: ChatGPT (Chief Architect) + Owner

---

## Completed Actions

| # | Action | Completed By | Date |
|---|--------|-------------|------|
| 22 | Phase 0.8 — Created GitHub Command Bridge (PHASE_0_8 doc, GITHUB_COMMAND_BRIDGE, GITHUB_ISSUE_COMMAND_TEMPLATE, COMMAND_ROUTING_RULES) | Claude Code (Builder) | 2026-05-26 |
| 21 | Phase 0.7 — Created Agent Run Protocol (AGENT_RUN_PROTOCOL, BUILDER_PROTOCOL, REVIEWER_PROTOCOL, SESSION_LIMIT_RULE) | Claude Code (Builder) | 2026-05-26 |
| 20 | Phase 0.6 — Codex REVIEW_FAIL fix (role labels, ACCEPTED→ASSIGNED, NEXT_ACTIONS restructure) | Claude Code (Builder) | 2026-05-26 |
| 19 | Phase 0.6 — Created Agent Command Intake Layer (initial build) | Codex (Reviewer) | 2026-05-26 |
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
