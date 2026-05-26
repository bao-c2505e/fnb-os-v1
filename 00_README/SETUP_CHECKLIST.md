# Master Setup Checklist — FnB OS V1

Complete all items before starting Phase 1.
Detailed checklists for each tool are in `08_DEPLOY/`.

---

## Status Legend
- [ ] Not started
- [~] In progress
- [x] Complete
- [!] Blocked — needs input

---

## 1. GitHub

- [ ] Repo created (private)
- [ ] Main branch protected
- [ ] `.gitignore` configured (blocks `.env`, `*.key`, `*.pem`, `node_modules`)
- [ ] All team members / agents have access
- [ ] Branch naming convention agreed: `phase-X/feature-name`

Details: `08_DEPLOY/github_setup_checklist.md`

---

## 2. OpenAI

- [ ] API key created (project-scoped, not personal)
- [ ] Usage limits set
- [ ] Key stored in `.env` as `OPENAI_API_KEY`
- [ ] Test call confirmed: `gpt-4o` accessible

Details: `08_DEPLOY/openai_setup_checklist.md`

---

## 3. Google Gemini

- [ ] API key created in Google AI Studio
- [ ] Usage limits noted
- [ ] Key stored in `.env` as `GEMINI_API_KEY`
- [ ] Test call confirmed: `gemini-1.5-pro` accessible

Details: `08_DEPLOY/gemini_setup_checklist.md`

---

## 4. Anthropic Claude

- [ ] API key created
- [ ] Usage limits set
- [ ] Key stored in `.env` as `ANTHROPIC_API_KEY`
- [ ] Test call confirmed: `claude-sonnet-4-5` accessible

Details: `08_DEPLOY/claude_code_setup_checklist.md`

---

## 5. OpenAI Codex

- [ ] Access confirmed (via OpenAI API)
- [ ] Model endpoint noted
- [ ] Key reuses `OPENAI_API_KEY`

Details: `08_DEPLOY/codex_setup_checklist.md`

---

## 6. n8n

- [ ] n8n instance running (self-hosted or cloud)
- [ ] n8n URL noted in `.env` as `N8N_BASE_URL`
- [ ] n8n API key stored as `N8N_API_KEY`
- [ ] Webhook base URL configured
- [ ] All required credentials added to n8n credential store (not repo)

Details: `08_DEPLOY/n8n_credentials_checklist.md`

---

## 7. Google Sheets

- [ ] Google Cloud project created
- [ ] Sheets API enabled
- [ ] Drive API enabled
- [ ] Service account created
- [ ] Service account JSON key downloaded and stored securely (NOT in repo)
- [ ] Service account email noted in `.env` as `GOOGLE_SERVICE_ACCOUNT_EMAIL`
- [ ] Sheet created and shared with service account
- [ ] Sheet ID noted in `.env` as `GOOGLE_SHEET_ID`
- [ ] Schema tabs created per `08_DEPLOY/google_sheet_schema.md`

Details: `08_DEPLOY/google_sheet_schema.md`

---

## 8. Google Drive

- [ ] Drive folder created for Vị Cuốn assets
- [ ] Folder ID noted in `.env` as `GOOGLE_DRIVE_FOLDER_ID`
- [ ] Sub-folder structure created per `08_DEPLOY/google_drive_structure.md`
- [ ] Service account has Editor access to folder

Details: `08_DEPLOY/google_drive_structure.md`

---

## 9. Telegram

- [ ] Bot created via BotFather
- [ ] Bot token stored in `.env` as `TELEGRAM_BOT_TOKEN`
- [ ] Chat ID for approval channel noted as `TELEGRAM_APPROVAL_CHAT_ID`
- [ ] Bot added to approval channel
- [ ] Test message sent and received

Details: `08_DEPLOY/telegram_setup_checklist.md`

---

## 10. Environment File

- [ ] `.env` file created from `08_DEPLOY/env.example`
- [ ] All placeholders replaced with real values
- [ ] `.env` added to `.gitignore` and NOT committed
- [ ] `.env` backed up securely (password manager or secrets vault)

---

## Final Gate

Before proceeding to Phase 1, confirm:
- [ ] All items above checked
- [ ] User has reviewed and approved this checklist
- [ ] Decision logged in `06_HANDOFF/DECISION_LOG.md`
- [ ] Phase 0 status set to COMPLETE in `06_HANDOFF/PHASE_STATUS.md`
