# 08_DEPLOY — Deployment & Environment Setup

This folder contains everything needed to configure the external services and environment for FnB OS V1.

## Files

| File | Purpose |
|------|---------|
| `env.example` | Template for `.env` file — copy and fill |
| `n8n_credentials_checklist.md` | n8n credential setup guide |
| `google_sheet_schema.md` | Google Sheet tabs and column structure |
| `google_drive_structure.md` | Google Drive folder structure |
| `telegram_setup_checklist.md` | Telegram bot setup guide |
| `openai_setup_checklist.md` | OpenAI API setup guide |
| `gemini_setup_checklist.md` | Google Gemini API setup guide |
| `claude_code_setup_checklist.md` | Anthropic Claude API setup guide |
| `codex_setup_checklist.md` | OpenAI Codex setup guide |
| `github_setup_checklist.md` | GitHub repo setup guide |

## Critical Rules
- NEVER commit `.env` to the repo
- NEVER put real credentials in any file in this folder
- `env.example` uses only placeholder values
- Service account JSON key files must NOT be placed in this repo
