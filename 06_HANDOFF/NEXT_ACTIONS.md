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

## Current Queue (Phase 0 → Phase 1 Transition)

### 🔴 BLOCKED — User Actions Required

1. **Fill BRAIN file placeholders**
   - Files: `01_BRAIN/brand_brain.md`, `menu_brain.md`, `customer_brain.md`, `offer_brain.md`, `content_brain.md`, `ads_brain.md`, `crm_brain.md`, `comment_reply_brain.md`, `design_brain.md`
   - Action: Replace all `[FILL: ...]` with real Vị Cuốn data
   - Blocker for: Phase 1, all agent prompts

2. **Complete SETUP_CHECKLIST.md**
   - File: `00_README/SETUP_CHECKLIST.md`
   - Action: Check off each item as services are configured
   - Blocker for: Phase 1

3. **Create .env file**
   - Template: `08_DEPLOY/env.example`
   - Action: Copy to `.env`, fill all values
   - Blocker for: Phase 1

4. **Approve Phase 0**
   - Action: User reviews all created files, confirms Phase 0 complete
   - Log in: `06_HANDOFF/DECISION_LOG.md`
   - Update: `06_HANDOFF/PHASE_STATUS.md`

---

### 🟠 HIGH — Phase 1 Tasks (After User Unblocks)

5. **Create Google Sheet**
   - Schema: `08_DEPLOY/google_sheet_schema.md`
   - Agent: Claude Code (Builder)
   - Output: Live Google Sheet with all tabs

6. **Create Google Drive folder structure**
   - Schema: `08_DEPLOY/google_drive_structure.md`
   - Agent: Claude Code (Builder)
   - Output: Drive folders created, IDs in `.env`

7. **Seed test data in Google Sheet**
   - Fixtures: `07_TEST_FIXTURES/test_campaign_combo_trua.json`
   - Agent: Claude Code (Builder)
   - Output: Sheet rows added for test campaigns

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
| 1 | Create Phase 0 repo structure | Claude Code (Builder) | 2026-05-26 |
| 2 | Create all BRAIN files | Claude Code (Builder) | 2026-05-26 |
| 3 | Create all agent prompts | Claude Code (Builder) | 2026-05-26 |
| 4 | Create all SOPs | Claude Code (Builder) | 2026-05-26 |
| 5 | Create all JSON schemas | Claude Code (Builder) | 2026-05-26 |
| 6 | Create HANDOFF files | Claude Code (Builder) | 2026-05-26 |
| 7 | Create test fixtures | Claude Code (Builder) | 2026-05-26 |
| 8 | Create DEPLOY checklists | Claude Code (Builder) | 2026-05-26 |
| 9 | Create log templates | Claude Code (Builder) | 2026-05-26 |
