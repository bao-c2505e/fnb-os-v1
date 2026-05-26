# Agent Registry — FnB OS V1

**Version:** v0.1.0
**Phase:** 0.5
**Updated:** 2026-05-26
**Updated By:** Claude Code (Builder Agent)

This file is the authoritative registry of every agent in the FnB OS V1 system.
All orchestrators, workflows, and task contracts reference agent names exactly as written here.

---

## Registry Format

```
### [AGENT_ID] — [Display Name]
Role:         what this agent does
Model/Tool:   the underlying AI or platform
Trigger:      how this agent is invoked
Credentials:  n8n credential name(s) required
Capabilities: what it can do
Cannot:       hard limits — safety rules
Input:        expected input format
Output:       expected output format
n8n node:     node type used in n8n workflows
Status:       Active | Planned | Deprecated
```

---

### AGT-01 — ChatGPT (Chief Architect)

| Field | Value |
|-------|-------|
| Role | Product owner, phase spec writer, final reviewer |
| Model | GPT-4o / o3 (OpenAI) |
| Trigger | Human instruction or Phase gate completion |
| Credentials | `OpenAI - FNB OS V1` |
| Status | Active |

**Capabilities:**
- Write phase specs and task contracts
- Review and approve all agent outputs
- Design system architecture changes
- Generate master prompts and SOP updates
- Produce campaign briefs for content agents

**Cannot:**
- Execute code directly
- Write files to repo (must instruct Claude Code)
- Access real-time internet without tools
- Activate n8n workflows

**Input format:** Natural language instruction from human owner
**Output format:** Markdown documents → committed to repo by Claude Code
**n8n node:** `n8n-nodes-base.openAi` (resource: chat, operation: create)

---

### AGT-02 — Claude Code (Builder Agent)

| Field | Value |
|-------|-------|
| Role | Repo builder, file writer, schema creator, code executor |
| Model | Claude Sonnet 4.5 / Opus (Anthropic) |
| Trigger | Task contract from Chief Architect, or direct human instruction |
| Credentials | `ANTHROPIC_API_KEY` (local CLI), n8n HTTP Request for API calls |
| Status | Active |

**Capabilities:**
- Create and edit all repo files (markdown, JSON, Python, YAML)
- Run shell/PowerShell commands locally
- Validate JSON schemas
- Run safety and secret scans
- Git operations (add, commit, push)
- Build n8n workflow JSON files
- Execute `check_env_safety.py` and other repo scripts

**Cannot:**
- Activate n8n workflows
- Post to social media
- Send messages to real customers
- Access production databases without explicit approval
- Commit `.env` or any secret file

**Input format:** Task contract (`TASK_CONTRACT.md`) or natural language
**Output format:** Files committed to GitHub repo
**n8n node:** `n8n-nodes-base.httpRequest` → Anthropic Messages API

---

### AGT-03 — Gemini (Content & Multimodal Agent)

| Field | Value |
|-------|-------|
| Role | Content generation, Vietnamese caption writing, image prompt creation |
| Model | Gemini 2.5 Flash / 1.5 Pro (Google) |
| Trigger | n8n HTTP Request node, or LangGraph task dispatch |
| Credentials | `Gemini - FNB OS V1` (HTTP Header Auth: `x-goog-api-key`) |
| Status | Active |

**Capabilities:**
- Generate Vietnamese social media captions
- Create image generation prompts (design briefs)
- Multimodal: analyze food photos for quality check
- Produce content packs from campaign briefs
- Translate and adapt content between Vietnamese/English

**Cannot:**
- Post content directly to social platforms
- Access customer data without explicit data pass
- Generate content without BRAIN context loaded

**Input format:** `content_pack_schema.json` request + BRAIN context
**Output format:** `content_pack_schema.json` (caption, hashtags, image_brief, CTA)
**n8n node:** `n8n-nodes-base.httpRequest` → Gemini REST API (`?key=` query param)
**Auth note:** Gemini REST API requires key as `?key=VALUE` — **not** as HTTP header

---

### AGT-04 — Codex / GPT-4o (Code Agent)

| Field | Value |
|-------|-------|
| Role | Code generation, n8n workflow JSON generation, debugging |
| Model | GPT-4o (OpenAI — Codex capabilities integrated) |
| Trigger | Task contract for code-specific tasks |
| Credentials | `OpenAI - FNB OS V1` |
| Status | Active |

**Capabilities:**
- Generate n8n workflow JSON from natural language specs
- Write Python helper scripts for data processing
- Debug workflow logic
- Validate JSON against schemas
- Write Google Apps Script if needed

**Cannot:**
- Execute generated code without human review
- Deploy workflows directly to n8n without approval

**Input format:** Natural language spec + schema references
**Output format:** Code files committed to repo, or JSON pasted into n8n
**n8n node:** `n8n-nodes-base.openAi` (model: gpt-4o)

---

### AGT-05 — LangGraph (Chief Orchestrator)

| Field | Value |
|-------|-------|
| Role | Multi-agent state machine, task router, context manager |
| Model | Python stateful graph (LangGraph library) |
| Trigger | n8n HTTP Request to LangGraph API endpoint |
| Credentials | `LANGGRAPH_API_KEY` (env var, Phase 3+) |
| Status | Planned (Phase 3) |

**Capabilities:**
- Maintain state across multi-agent workflows
- Route tasks to correct agent based on task type
- Manage retry logic when agent output fails QC
- Aggregate outputs from parallel agents
- Pass context between sessions without losing state

**Cannot:**
- Generate content directly
- Access external APIs without agent delegation

**Input format:** Task object (JSON) with `task_type`, `campaign_id`, `context`
**Output format:** Routed result from downstream agent + orchestration log
**n8n node:** `n8n-nodes-base.httpRequest` → LangGraph API (POST /invoke)

---

### AGT-06 — n8n (Automation Runtime)

| Field | Value |
|-------|-------|
| Role | Workflow automation engine, trigger manager, data pipeline |
| Model | n8n (self-hosted at https://n8n.baon8n.blog) |
| Trigger | Schedule, webhook, manual, Google Sheets poll |
| Credentials | All 5 credentials in `08_DEPLOY/n8n_credentials_step_by_step.md` |
| Status | Active (smoke tests complete) |

**Capabilities:**
- Poll Google Sheets for new campaign rows
- Call AI agents via HTTP Request
- Read/write Google Drive and Sheets
- Send Telegram approval requests
- Route approval responses to correct workflow branch
- Write execution logs to Google Sheets

**Cannot:**
- Make approval decisions without human Telegram response
- Post to social platforms in Phase 0–2
- Activate itself — all activations require explicit human toggle in n8n UI

**Input format:** Trigger event (schedule / webhook / manual)
**Output format:** Execution log row in Google Sheet `System_Log` tab

---

### AGT-07 — QC Agent (Quality Check Agent)

| Field | Value |
|-------|-------|
| Role | Review and score all agent outputs before approval |
| Model | GPT-4o or Claude Sonnet (configurable) |
| Trigger | Auto-called by n8n after every content/ads/CRM generation |
| Credentials | `OpenAI - FNB OS V1` or `Anthropic` credential |
| Status | Planned (Phase 2) |

**Capabilities:**
- Score outputs on 6 dimensions (see `02_PROMPTS/quality_check_prompt.md`)
- Detect safety rule violations
- Flag invented facts, missing CTAs, wrong tone
- Return structured QC result with pass/fail and suggestions

**Cannot:**
- Approve content — score only, human approves via Telegram
- Override escalation flags set by other agents

**Input format:** Any agent output JSON + `qc_request_id`
**Output format:** QC result JSON with `overall_score`, `passed`, `issues[]`
**n8n node:** `n8n-nodes-base.openAi` or HTTP Request to Claude

---

## Agent Capability Matrix

| Capability | AGT-01 | AGT-02 | AGT-03 | AGT-04 | AGT-05 | AGT-06 | AGT-07 |
|-----------|--------|--------|--------|--------|--------|--------|--------|
| Write repo files | — | ✅ | — | ✅ | — | — | — |
| Generate content | ✅ | — | ✅ | — | — | — | — |
| Generate code | ✅ | ✅ | — | ✅ | — | — | — |
| Read Google Sheets | — | — | — | — | — | ✅ | — |
| Write Google Sheets | — | — | — | — | — | ✅ | — |
| Send Telegram | — | — | — | — | — | ✅ | — |
| Route tasks | ✅ | — | — | — | ✅ | ✅ | — |
| QC / score output | ✅ | — | — | — | — | — | ✅ |
| Git operations | — | ✅ | — | — | — | — | — |
| Approve actions | 👁 | — | — | — | — | — | — |

👁 = Review only, final approval always comes from Human (User)

---

## Naming Convention

All task contracts, logs, and workflow JSON files must reference agents using these exact IDs and display names:

| ID | Display Name | Short Name |
|----|-------------|------------|
| AGT-01 | ChatGPT (Chief Architect) | chief-architect |
| AGT-02 | Claude Code (Builder Agent) | builder |
| AGT-03 | Gemini (Content Agent) | content-agent |
| AGT-04 | Codex / GPT-4o (Code Agent) | code-agent |
| AGT-05 | LangGraph (Orchestrator) | orchestrator |
| AGT-06 | n8n (Runtime) | runtime |
| AGT-07 | QC Agent | qc-agent |
| HUMAN | Human Owner (User) | human |

---

## Changelog

| Date | Change | By |
|------|--------|----|
| 2026-05-26 | v0.1.0 — initial registry, 7 agents defined | Claude Code (Builder) |
