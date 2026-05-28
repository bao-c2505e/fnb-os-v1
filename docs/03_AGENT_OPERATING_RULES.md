# Agent Operating Rules — FnB OS V1

Version: 1.0
Date: 2026-05-28
Authority: ChatGPT (Chief Architect)
Maintained by: Claude Code (Builder)

This document is the expanded operating ruleset for all agents.
It consolidates and supersedes `docs/agent-system/OPERATING_RULES.md`.

---

## 1. Agent Roles and Boundaries

| Agent | Core Function | Hard Boundary |
|-------|--------------|---------------|
| Owner (USER) | Final approver | No boundary — all authority |
| ChatGPT (AGT-01) | Chief Architect — design, specs, contracts | Cannot execute repo changes or approve own designs |
| Claude Code (AGT-02) | Builder — repo edits, docs, schemas, scripts | Cannot commit without OWNER_APPROVED; cannot review own work |
| Codex (AGT-03) | Reviewer — diff review, validation | Cannot write new features; cannot commit or push |
| Gemini (AGT-04) | Optional worker — content, prompts, multimodal | Cannot publish, message customers, or activate automations |
| n8n (AGT-05) | Runtime automation | Cannot self-activate; cannot make approval decisions |
| GitHub (AGT-06) | Source of truth | Read/write by authorized agents only; no real secrets |
| LangGraph (AGT-07) | Future orchestrator | Inactive — reserved for future activation |

---

## 2. Session Lifecycle

```
[Owner or ChatGPT creates command]
        ↓
[Builder: Session Start Checklist]
        ↓
[Builder: Scope Lock — list scope_files]
        ↓
[Builder: Execute — one file at a time]
        ↓  (turn 8 → update SESSION_SUMMARY.md)
[Builder: Pre-BUILDER_DONE Checklist]
        ↓
[Builder: status → BUILDER_DONE → REVIEW_REQUESTED]
        ↓
[Reviewer: Session Start Checklist]
        ↓
[Reviewer: Review Checklist (8 items)]
        ↓
[Reviewer: status → REVIEW_PASS or REVIEW_FAIL]
        ↓  (REVIEW_FAIL → Builder fixes → re-review)
[Owner: APPROVE_CURRENT_PHASE]
        ↓
[Owner: records OWNER_APPROVED status, or Builder records it only after explicit Owner approval]
        ↓
[Owner: git commit + git push in terminal]
        ↓
[Owner or Builder: CLOSE_APPROVED_COMMAND → CLOSED]
```

---

## 3. Session Start Checklist (All Agents)

Before writing any output, every agent must verify:

| # | Check | Pass Condition |
|---|-------|----------------|
| 1 | Active command identified | First non-CLOSED record in `commands/COMMAND_INBOX.md` |
| 2 | Phase matches | Command phase = `handoff/CURRENT_PHASE.md` phase number |
| 3 | Role assignment confirmed | `assigned_builder` or `assigned_reviewer` matches your identity |
| 4 | Scope files enumerated | You can list every file you are allowed to touch |
| 5 | Forbidden actions read | None of them apply to your planned work |
| 6 | Acceptance criteria understood | You can describe DONE in plain language |
| 7 | Session summary read | Open issues from prior sessions understood |
| 8 | No secrets in scope | No `.env`, no credential files, no key strings in planned work |

Fail any check → set status `BLOCKED`, record `blocked_reason`, notify Owner.

---

## 4. Turn Cap and Session Summary Rule

- Maximum **10 turns** per agent session.
- At or before turn **8**, the active agent must update `handoff/SESSION_SUMMARY.md` with:
  1. Current phase and command
  2. What was done this session
  3. What remains
  4. Open issues or blockers
  5. Next action required
  6. Files touched
  7. Git status snapshot
- At turn 10, if work is not complete: set status `BUILDER_DONE` (partial) or `BLOCKED`, document remaining work.

A new session may continue the work after the Owner reviews and re-issues the command.

---

## 5. Scope Enforcement

- Work only on files in `scope_files` as defined in the active command.
- If a required file is not in `scope_files`:
  - Stop work immediately.
  - Add a note to `handoff/SESSION_SUMMARY.md` under "open_issues".
  - Set status `BLOCKED` with `blocked_reason`.
  - Do not proceed until Owner or ChatGPT updates `scope_files`.
- `git status --short` at session end must show only `scope_files` as modified.

---

## 6. Logging Requirements

Every agent session must append to both:

**`logs/AGENT_ACTIVITY_LOG.md`** — one row per session:
```
| YYYY-MM-DD HH:MM | [Agent] | [Phase X.X] | [Action summary] | [Result] | [Files changed] |
```

**`09_LOGS/PHASE_LOG.md`** — one entry per phase:
```
| YYYY-MM-DD | [Agent] | [Phase X.X] | [Status] | [Detail] |
```

Commands that generate output must also write to `/logs/` as specified in the command.

---

## 7. Communication Channels

| Channel | Purpose | Who Uses |
|---------|---------|----------|
| `commands/COMMAND_INBOX.md` | Active work queue | All agents |
| `handoff/SESSION_SUMMARY.md` | Cross-session context | Builder, Reviewer |
| `handoff/CURRENT_PHASE.md` | Phase status | Builder, Reviewer, Owner |
| `logs/AGENT_ACTIVITY_LOG.md` | Activity history | All agents |
| GitHub Issues | Async command input (Phase 0.8+) | Owner, ChatGPT |
| Telegram (future) | Approval notifications | n8n → Owner |

Agents must not communicate with each other outside these defined channels.

---

## 8. What Every Agent Must Never Do

- Hardcode API keys, tokens, passwords, OAuth secrets, or any credentials.
- Post to social media, send messages to real customers, or run paid ads.
- Activate n8n workflows without Owner approval.
- Commit or push to git without `OWNER_APPROVED` on the active command.
- Open the next phase before the current command reaches `CLOSED`.
- Make decisions that require Owner approval — set `BLOCKED` and wait.
- Perform actions outside the assigned role (Builder does not review; Reviewer does not build).
