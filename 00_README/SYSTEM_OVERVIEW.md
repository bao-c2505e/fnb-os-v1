# System Overview — FnB OS V1

## Architecture Summary

```
User
 └── approves plans & final output only

ChatGPT (Chief Architect / Product Owner)
 └── creates phase specs, reviews agent outputs, owns roadmap

LangGraph (Chief Orchestrator)
 └── routes tasks between agents, manages multi-agent state machine

n8n (Automation Runtime)
 ├── executes all workflows
 ├── triggers agents via HTTP / webhook
 ├── reads/writes Google Sheets
 └── sends Telegram approvals

Worker Agents
 ├── Claude Code — file builder, code, schemas, SOPs
 ├── Codex — code generation, debugging
 ├── Gemini — multimodal, content generation
 └── Antigravity — specialized tasks (TBD)

Data & Asset Layer
 ├── Google Sheets — campaign data, CRM, logs, schedules
 └── Google Drive — image assets, design briefs, content packs

Approval Gate
 └── Telegram — human-in-the-loop approval for key decisions

AI Providers
 ├── OpenAI (GPT-4o / o3)
 ├── Google Gemini (1.5 Pro / 2.0 Flash)
 └── Anthropic Claude (Sonnet 4.5 / Opus)
```

## Data Flow

```
Trigger (schedule / webhook / manual)
  → n8n reads campaign data from Google Sheets
  → n8n calls LangGraph orchestrator
  → LangGraph routes to worker agents
  → Agents generate content / design brief / ads pack
  → Output written to Google Drive + Google Sheets
  → Telegram approval request sent to user
  → User approves → n8n posts / activates output
  → Execution log written to Google Sheets
```

## Key Design Principles

| Principle | Detail |
|-----------|--------|
| Repo is source of truth | All config, schema, prompts, SOPs live in GitHub |
| No debug by screenshot | All agent output is logged, diff-able, reviewable via files |
| Human approves final output | Telegram gate before any live action |
| Phased rollout | Each phase is spec'd, built, tested, approved before next |
| Secrets never in repo | All credentials in `.env` (gitignored), never committed |

## Technology Stack

| Layer | Tool | Version / Notes |
|-------|------|-----------------|
| Orchestration | LangGraph | Python, stateful graph |
| Automation | n8n | Self-hosted or cloud |
| Code agents | Claude Code, Codex | Via API |
| AI content | OpenAI GPT-4o, Gemini 1.5, Claude Sonnet | Via API |
| Data | Google Sheets API v4 | Service account auth |
| Assets | Google Drive API v3 | Service account auth |
| Approval | Telegram Bot API | Webhook mode |
| Source control | GitHub | Main branch = production |
| Secrets | .env file | Never committed |

## Security Boundaries

- All credentials stored in `.env` (gitignored)
- Service accounts used for Google APIs (no user OAuth in automation)
- Telegram bot token scoped to single bot
- n8n credentials encrypted at rest
- No PII stored in repo — only in Google Sheets (access-controlled)
- Agent actions are logged before execution, not after failure
