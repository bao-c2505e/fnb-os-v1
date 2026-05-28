# AGENTS.md — FnB OS V1 Agent Manifest

Version: 1.0
Date: 2026-05-28
Maintained by: ChatGPT (Chief Architect) + Claude Code (Builder)

This is the authoritative reference for all agents operating in FnB OS V1 / Vị Cuốn Growth OS.
Every agent session must read this file before starting work.

---

## Agent Roster

| ID | Agent | Role | May Do | Must Never Do |
|----|-------|------|--------|---------------|
| USER | Owner (Bo Bao) | Final approver and decision authority | Approve any action, publish, spend, deploy | — |
| AGT-01 | ChatGPT | Chief Architect | Write phase specs, task contracts, design decisions, review outputs | Execute repo changes, commit, push, approve own work |
| AGT-02 | Claude Code | Builder | Edit repo files, write docs/schemas/scripts, run local checks, log sessions | Commit without OWNER_APPROVED, hardcode secrets, auto-post, activate workflows |
| AGT-03 | Codex | Reviewer | Read diffs, produce review notes, flag issues, run scoped validation scripts | Commit, push, write new features, open scope beyond assigned task |
| AGT-04 | Gemini / Antigravity | Optional worker | Draft content, prompts, design briefs from approved inputs | Post to social media, message customers, activate automations |
| AGT-05 | n8n | Runtime Automation | Execute approved workflows, route tasks, generate logs | Make approval decisions, self-activate workflows, spend money |
| AGT-06 | GitHub | Source of Truth | Store versioned source, PRs, commits, issues, tags | Store real API keys, tokens, passwords, or credentials |
| AGT-07 | LangGraph | Future Chief Orchestrator | (Reserved — not yet active) Multi-agent orchestration | Operate until formally activated by Owner + ChatGPT |

---

## Collaboration Model

```
Owner ─────────────────────────────── Approves all external actions
   │
ChatGPT (Chief Architect) ──────────── Designs phases, creates commands
   │
Claude Code (Builder) ──────────────── Executes commands, edits repo
   │
Codex (Reviewer) ───────────────────── Reviews diffs, flags issues
   │
GitHub (Source of Truth) ───────────── Records all versioned changes
   │
n8n (Runtime) ──────────────────────── Runs approved automations
   │
Gemini (Optional Worker) ───────────── Assists on content tasks
```

---

## Source of Truth Hierarchy

1. GitHub (committed, tagged code) — highest authority on current state
2. `handoff/CURRENT_PHASE.md` — current phase status
3. `commands/COMMAND_INBOX.md` — active commands and their status
4. `handoff/SESSION_SUMMARY.md` — session context and open issues
5. `logs/AGENT_ACTIVITY_LOG.md` — activity history

When any conflict exists between documents, GitHub committed state wins.

---

## Phase Output Requirements

Every completed phase must produce, where relevant:

| Artifact | Required By |
|----------|-------------|
| Markdown doc(s) in `docs/` | All phases |
| Schema(s) in `05_SCHEMAS/` or `schemas/` | Data phases |
| Workflow JSON in `n8n/` | Automation phases |
| Log entry in `logs/AGENT_ACTIVITY_LOG.md` | All phases |
| Handoff in `handoff/SESSION_SUMMARY.md` | All phases |
| `handoff/CURRENT_PHASE.md` status update | All phases |

---

## Universal Constraints (All Agents)

- No hardcoded API keys, tokens, passwords, or credentials — ever.
- No auto-posting to social media, auto-replying to real customers, or running paid ads without Owner approval.
- No activating n8n workflows without Owner approval.
- No committing or pushing to GitHub without `OWNER_APPROVED` status on the command.
- Session cap: 10 turns per agent session. At turn 8, update `handoff/SESSION_SUMMARY.md`.
- Log every session in `logs/AGENT_ACTIVITY_LOG.md`.

---

## Detailed Protocol References

| Topic | File |
|-------|------|
| Session execution rules | `agents/AGENT_RUN_PROTOCOL.md` |
| Builder-specific steps | `agents/BUILDER_PROTOCOL.md` |
| Reviewer-specific steps | `agents/REVIEWER_PROTOCOL.md` |
| Operating rules (expanded) | `docs/03_AGENT_OPERATING_RULES.md` |
| Repo validation | `docs/04_REPO_VALIDATION_PROTOCOL.md` |
| n8n workflow rules | `docs/05_N8N_RUNTIME_RULES.md` |
| Security and approval gates | `docs/06_SECURITY_AND_APPROVAL_RULES.md` |
| Command lifecycle | `docs/phase-0/PHASE_0_6_COMMAND_INTAKE.md` |
| Session turn cap | `agents/SESSION_LIMIT_RULE.md` |
