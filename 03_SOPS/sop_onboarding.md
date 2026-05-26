# SOP — New Brand Onboarding

**Version:** v0.1.0
**Status:** DRAFT

---

## Trigger
User initiates onboarding for a new F&B brand.

## Pre-conditions
- User has brand name, contact info, and basic menu
- GitHub repo is initialized
- `.env` file is created from template

## Steps

1. **User fills BRAIN files**
   - Agent: Human (user) + ChatGPT (Chief Architect)
   - Files: `01_BRAIN/*.md` — replace all `[FILL]` placeholders
   - Output: Completed brand_brain.md, menu_brain.md, customer_brain.md

2. **User configures environment**
   - Agent: Human
   - Action: Complete `00_README/SETUP_CHECKLIST.md`
   - Output: All credentials in `.env`, services confirmed

3. **Builder Agent creates Google Sheet**
   - Agent: Claude Code (Builder)
   - Action: Create Sheet with schema from `08_DEPLOY/google_sheet_schema.md`
   - Output: Sheet ID noted in `.env`

4. **Builder Agent creates Google Drive folders**
   - Agent: Claude Code (Builder)
   - Action: Create folder structure from `08_DEPLOY/google_drive_structure.md`
   - Output: Folder IDs noted in `.env`

5. **QC Agent reviews BRAIN files**
   - Agent: QC Agent
   - Action: Check all placeholders filled, no contradictions
   - Output: QC report in `09_LOGS/`

6. **Chief Architect reviews and approves**
   - Agent: ChatGPT
   - Action: Review BRAIN files, approve for Phase 1
   - Output: Decision logged in `06_HANDOFF/DECISION_LOG.md`

7. **User final approval**
   - Agent: Human
   - Action: Review checklist, approve Phase 0 complete
   - Output: `06_HANDOFF/PHASE_STATUS.md` updated

## Output
- Completed BRAIN files
- Live Google Sheet with schema
- Google Drive structure
- Phase 0 marked COMPLETE

## Failure Handling
| Failure | Action |
|---------|--------|
| Missing BRAIN placeholder | Flag in QC report, block Phase 1 |
| Google API error | Log in ERROR_LOG.md, escalate to user |
| n8n not reachable | Log and pause until resolved |

## Approval Gate
User approves in SETUP_CHECKLIST.md before Phase 1 begins.

## Logging
- All steps logged in `09_LOGS/execution_log_template.md`
- Errors in `06_HANDOFF/ERROR_LOG.md`
- Decisions in `06_HANDOFF/DECISION_LOG.md`
