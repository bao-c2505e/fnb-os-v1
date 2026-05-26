# Agent Operating Rules

Created By: Codex (Builder) - 2026-05-26

## Roles

| Role | Responsibility | Hard Limits |
| --- | --- | --- |
| User | Final owner and approval authority | Must approve external actions before execution |
| ChatGPT | Chief Architect: phase specs, task contracts, final review | Does not execute repo changes directly |
| Claude | Builder Agent: repo edits, docs, schemas, scripts | Does not publish, auto-reply, spend money, or commit secrets |
| Codex | Reviewer/Fixer/Script Worker | Works only inside assigned task scope |
| Gemini | Content and multimodal generation | Does not post or message customers directly |
| n8n | Automation runtime and approval routing | Does not decide approvals or activate workflows without user action |
| GitHub | Source of truth for versioned repo state | Stores code and docs only, never real secrets |

## Session Rules

- Maximum session length is 10 back-and-forth turns per agent.
- At or before turn 10, the active agent must update `handoff/SESSION_SUMMARY.md`.
- A new agent session starts by reading `handoff/CURRENT_PHASE.md`, `handoff/SESSION_SUMMARY.md`, `logs/AGENT_ACTIVITY_LOG.md`, and the assigned task file in `tasks/`.
- A session ends by appending a short activity log entry.

## Secret Rules

- Never hardcode API keys, tokens, passwords, OAuth client secrets, private keys, or production credentials.
- Use placeholders such as `REPLACE_WITH_*`, `[FILL]`, or documented environment variable names.
- `.env` and credential exports must not be committed.
- If a secret is found in scope, stop work, report it, and request rotation.

## Approval Gate

Human approval is required before any action that:

- Posts to social media.
- Sends CRM, Telegram, or customer-facing messages.
- Activates or schedules n8n workflows.
- Uses ad accounts or spends money.
- Changes production data.
- Merges or deploys externally visible automation.

Approval state must be written in the task file or Agent_Tasks row before execution.

## Practical Use

- Work only on the assigned task scope.
- Prefer small patches with clear diffs.
- Keep task outputs testable.
- Record blockers in the task and activity log.
