# Agent Communication Rules — FnB OS V1

**Version:** v0.1.0
**Last Updated:** 2026-05-26

---

## Core Principle
Agents do NOT communicate directly. All agent-to-agent communication goes through:
1. **Files in this repo** (primary)
2. **Google Sheets** (data layer)
3. **n8n workflow context** (runtime, Phase 3+)
4. **LangGraph state** (orchestration, Phase 3+)

No agent sends messages to another agent via chat, API, or any real-time channel without going through the orchestrator.

---

## Communication Format

Every agent output that must be passed to another agent must be written as a valid JSON file matching the relevant schema in `05_SCHEMAS/`.

```
Agent A produces output → validates against schema → writes to file/Sheet → 
LangGraph/n8n reads file → routes to Agent B → Agent B reads input
```

---

## Session Rules

1. **Session cap:** 10 back-and-forth messages per agent session
2. **At message 10:** create/update `SESSION_SUMMARY.md` before stopping
3. **Session start:** always read `SESSION_HANDOFF.md` and `NEXT_ACTIONS.md` first
4. **Session end:** always update `SESSION_HANDOFF.md` with what was done and what's next

---

## Agent Identity Rules

Each agent must identify itself in every file it creates or modifies:
```
Created By: [Agent Name] — [Date]
```

Valid agent names:
- `ChatGPT (Chief Architect)`
- `LangGraph (Orchestrator)`
- `Claude Code (Builder)`
- `Codex (Builder)`
- `Gemini (Builder)`
- `n8n (Runtime)`
- `Human (User)`

---

## Escalation Protocol

When an agent encounters an issue it cannot resolve:
1. Write error to `ERROR_LOG.md` with full context
2. Set `requires_human_review: true` in output JSON
3. If critical: write to `NEXT_ACTIONS.md` with `[BLOCKED]` tag
4. Do NOT continue to next step — stop and wait for resolution

---

## Conflict Resolution

If two agents produce conflicting outputs for the same object:
1. The output with the higher `confidence_score` takes precedence
2. If scores are equal, QC Agent decides
3. All conflicts are logged in `DECISION_LOG.md`

---

## File Ownership

| File | Owner (can write) | Others |
|------|------------------|--------|
| BRAIN files | Human (User), ChatGPT | Read only |
| PROMPTS | ChatGPT, Claude Code | Read only |
| SCHEMAS | Claude Code, ChatGPT | Read only |
| SOPS | ChatGPT, Claude Code | Read only |
| WORKFLOWS | Claude Code, Codex | Read only |
| HANDOFF files | All agents | Read + Write |
| LOGS | All agents | Append only |
| TEST FIXTURES | ChatGPT, Claude Code | Read only |
| DEPLOY files | Claude Code | Read only (others) |

---

## Prohibited Actions

No agent may:
- Delete files from the repo
- Overwrite another agent's approved output without logging the reason
- Skip the QC step
- Post or send to external services without approval
- Hardcode credentials in any file
- Activate n8n workflows without user approval
