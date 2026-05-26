# FnB OS V1 — Solo AI Marketing Agency Operating System

## Project Name
FnB OS V1 — Vị Cuốn Growth OS

## What This Is
A fully automated AI-powered marketing operating system built for F&B businesses.
Starting brand: **Vị Cuốn** (Vietnamese fresh roll restaurant).

This repo is the source of truth for all agents, workflows, schemas, SOPs, and handoffs.

## Who Uses This
- **User** — approves plans and final outputs only
- **ChatGPT** — Chief Architect / Product Owner (creates phase specs, reviews outputs)
- **LangGraph** — Chief Orchestrator (multi-agent controller)
- **n8n** — Automation runtime (executes workflows)
- **Claude Code / Codex / Gemini / Antigravity** — Worker agents (build and fix)
- **Google Sheets / Google Drive** — Data and asset layer
- **Telegram** — Approval gate
- **OpenAI / Gemini / Claude** — AI providers

## Current Phase
**Phase 0 — Environment & Project Setup** ✅ IN PROGRESS

## Folder Map
| Folder | Purpose |
|--------|---------|
| `00_README` | Project overview, roadmap, setup checklist |
| `01_BRAIN` | Brand knowledge, menu, customer, content, ads intelligence |
| `02_PROMPTS` | All agent system prompts |
| `03_SOPS` | Standard operating procedures for every workflow |
| `04_WORKFLOWS` | n8n workflow JSON files and inventory |
| `05_SCHEMAS` | JSON schemas for all data objects |
| `06_HANDOFF` | Agent communication, session handoff, decisions, errors |
| `07_TEST_FIXTURES` | Test input data for QA and dry runs |
| `08_DEPLOY` | Environment setup, credentials checklists |
| `09_LOGS` | Execution, error, and approval log templates |

## Core Rules
1. No hardcoded secrets — use `env.example` and placeholders only
2. No production actions until Phase 3+
3. No live n8n workflow activation until fully tested
4. Every decision goes into `06_HANDOFF/DECISION_LOG.md`
5. Every phase status goes into `06_HANDOFF/PHASE_STATUS.md`
6. Sessions are capped at 10 messages; summarize in `SESSION_SUMMARY.md`

## Quick Links
- [System Overview](SYSTEM_OVERVIEW.md)
- [Roadmap](ROADMAP.md)
- [Setup Checklist](SETUP_CHECKLIST.md)
- [Agent Communication Rules](../06_HANDOFF/AGENT_COMMUNICATION_RULES.md)
- [Task Contract](../06_HANDOFF/TASK_CONTRACT.md)
- [Phase Status](../06_HANDOFF/PHASE_STATUS.md)
