# Phase 0.5 — Agent Collaboration Layer

**Phase:** 0.5
**Created:** 2026-05-26
**Created By:** Claude Code (Builder Agent)
**Status:** COMPLETE

---

## Objective

Define and document the full inter-agent collaboration protocol for FnB OS V1.

After Phase 0.5 every agent in the system has:
- A registered identity (`AGENT_REGISTRY.md`)
- A defined input/output contract (`agent_task_schema.json`)
- A known position in the collaboration flow
- Clear safety boundaries that cannot be crossed

This is the last Phase 0 sub-phase. After this, Phase 1 (live Google Sheet + Drive setup) begins.

---

## What Was Built

| File | Purpose |
|------|---------|
| `06_HANDOFF/AGENT_REGISTRY.md` | Registry of all 7 agents — role, model, capabilities, safety limits |
| `05_SCHEMAS/agent_task_schema.json` | JSON schema for `Agent_Tasks` Google Sheet tab |
| `docs/phase-0/PHASE_0_5_AGENT_COLLABORATION.md` | This file |

Builds on top of (existing, not changed):
- `06_HANDOFF/AGENT_COMMUNICATION_RULES.md` — communication protocol
- `06_HANDOFF/TASK_CONTRACT.md` — task assignment format

---

## Agent Collaboration Flow

```
Human Owner
  │
  │ approves phase spec / task
  ▼
ChatGPT (Chief Architect) [AGT-01]
  │
  │ writes Task Contract → commits to repo
  ▼
Google Sheet: Agent_Tasks tab
  │
  │ n8n polls Agent_Tasks (Phase 3+)
  ▼
LangGraph (Orchestrator) [AGT-05]  ◄── reads task_type
  │
  ├─── task_type: content_pack    ──► Gemini [AGT-03]
  │                                     │ output → content_pack_schema.json
  │                                     │ → Google Drive + Sheets
  │                                     ▼
  ├─── task_type: design_brief   ──► Gemini [AGT-03] or Claude [AGT-02]
  │
  ├─── task_type: ads_pack        ──► GPT-4o / Codex [AGT-04]
  │
  ├─── task_type: crm_message     ──► Gemini [AGT-03]
  │
  ├─── task_type: comment_reply   ──► Gemini [AGT-03]
  │
  └─── task_type: repo_build      ──► Claude Code [AGT-02]
         │
         │ all outputs → QC Agent [AGT-07]
         ▼
       QC Agent scores output
         │
         ├── score ≥ 0.80 → n8n sends Telegram approval to Human
         └── score < 0.80 → regenerate (max 3 retries) → escalate
                                │
                                ▼
                           Human Owner
                           approves / rejects / edits via Telegram
                                │
                                ▼
                           n8n executes approved action
                           writes log to Google Sheet System_Log
```

---

## Agent Task Lifecycle

A task in the `Agent_Tasks` Google Sheet goes through these states:

```
pending → in_progress → complete
                     → blocked   (waiting for dependency)
                     → failed    (error, logged in ERROR_LOG)
                     → cancelled (human decision)
```

### State Transitions

| From | To | Triggered By |
|------|----|-------------|
| (created) | `pending` | Chief Architect or n8n |
| `pending` | `in_progress` | Agent picks up task |
| `in_progress` | `complete` | Agent writes output + QC passes |
| `in_progress` | `blocked` | Dependency missing or API error |
| `in_progress` | `failed` | QC fails after 3 retries, or unrecoverable error |
| `blocked` | `pending` | Blocking dependency resolved |
| `failed` | `pending` | Human decides to retry |
| Any | `cancelled` | Human decision |

---

## Agent_Tasks Google Sheet Tab — Column Map

The `Agent_Tasks` tab in `FNB_OS_V1_CONTROL_CENTER` must have these columns
(in this order) for n8n workflows to read/write correctly:

| Col | Field | Type | Notes |
|-----|-------|------|-------|
| A | task_id | string | TASK-[PHASE]-[SEQ] |
| B | task_name | string | Short description |
| C | assigned_to | string | AGT-ID from registry |
| D | assigned_to_name | string | Display name |
| E | assigned_by | string | AGT-ID or HUMAN |
| F | phase | string | 0.5, 1, 2 … |
| G | status | enum | pending/in_progress/blocked/complete/failed |
| H | priority | enum | high/medium/low |
| I | goal | string | What must be done |
| J | input_ref | string | File path or Sheet ref |
| K | output_ref | string | File path or Sheet ref |
| L | requires_human_approval | boolean | TRUE/FALSE |
| M | telegram_notification | boolean | TRUE/FALSE |
| N | blocked_reason | string | Empty unless blocked |
| O | next_task_id | string | Task that starts after |
| P | next_agent | string | Agent that receives output |
| Q | campaign_id | string | Optional |
| R | created_at | datetime | ISO8601 |
| S | started_at | datetime | ISO8601 |
| T | completed_at | datetime | ISO8601 |
| U | notes | string | Free text |

Full schema: `05_SCHEMAS/agent_task_schema.json`

---

## Task Routing Rules

n8n/LangGraph uses `task_type` (embedded in `task_name` or `goal`) to route:

| task_type keyword | Assigned to | Output schema |
|-------------------|------------|---------------|
| `content_pack` | AGT-03 (Gemini) | `content_pack_schema.json` |
| `design_brief` | AGT-03 (Gemini) | `design_brief_schema.json` |
| `ads_pack` | AGT-04 (GPT-4o) | `ads_pack_schema.json` |
| `crm_message` | AGT-03 (Gemini) | `crm_followup_schema.json` |
| `comment_reply` | AGT-03 (Gemini) | `comment_reply_schema.json` |
| `repo_build` | AGT-02 (Claude Code) | Files in GitHub |
| `qc_review` | AGT-07 (QC Agent) | QC result JSON |
| `approval` | AGT-06 (n8n) → HUMAN | `approval_schema.json` |

---

## Telegram Notification Protocol

When an agent completes a task that has `telegram_notification: true`:

```
n8n sends to TELEGRAM_APPROVAL_CHAT_ID:

🔔 Agent Task Complete

Task:    TASK-1-001 — Generate Combo Trưa Content Pack
Agent:   Gemini (Content Agent)
Output:  /Content Packs/2026-06/VQ-CP-20260601-001.json
QC:      0.87 / 1.00 — PASS

Actions:
  ✅ /approve_TASK-1-001
  ❌ /reject_TASK-1-001
  ✏️  /edit_TASK-1-001 [your notes]
```

Human responds via Telegram → n8n webhook reads response → updates Agent_Tasks status.

---

## Safety Rules for All Agents

These rules apply to every agent without exception:

1. **No agent may post to social media** without `status=approved` in Agent_Tasks
2. **No agent may send CRM messages** without `status=approved` + consent confirmed
3. **No agent may activate n8n workflows** — humans toggle activation in n8n UI only
4. **No agent may commit `.env`** — Claude Code has this blocked in safety scan
5. **No agent may invent facts** about Vị Cuốn menu or prices not in BRAIN files
6. **No agent may skip QC** — every content/ads/CRM output goes through AGT-07
7. **Every error must be logged** to `ERROR_LOG.md` and Google Sheet `System_Log`
8. **Session cap = 10 messages** — Claude Code updates `SESSION_SUMMARY.md` at limit

---

## Done Criteria — Phase 0.5

- [x] `AGENT_REGISTRY.md` — all 7 agents defined with capabilities and safety limits
- [x] `agent_task_schema.json` — schema complete, maps to Agent_Tasks sheet
- [x] `PHASE_0_5_AGENT_COLLABORATION.md` — flow, lifecycle, routing, Telegram protocol documented
- [ ] Agent_Tasks tab in Google Sheet has correct columns (Phase 1 action)
- [ ] First real TASK-1-xxx rows seeded in Agent_Tasks tab (Phase 1)

---

## Next Phase

**Phase 1 — Google Sheet & Drive Setup**

1. Create `FNB_OS_V1_CONTROL_CENTER` sheet with all 10 tabs + correct columns
2. Create Google Drive folder structure per `08_DEPLOY/google_drive_structure.md`
3. Seed test campaign data from `07_TEST_FIXTURES/test_campaign_combo_trua.json`
4. Seed first Agent_Tasks rows for Phase 1 build tasks
5. Verify n8n can read/write all tabs (using SMOKE-02 as base)
