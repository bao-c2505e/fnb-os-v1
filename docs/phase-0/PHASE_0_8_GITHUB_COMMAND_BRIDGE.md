# Phase 0.8 — GitHub Command Bridge

Created By: Claude Code (Builder) — 2026-05-26

---

## Problem Being Solved

After Phases 0.6 and 0.7, the command intake system works — but it still requires Owner to:

1. Copy a long prompt from ChatGPT
2. Paste it into a chat with Claude
3. Manually copy Claude's output back to Codex
4. Manually tell Codex what to review
5. Copy-paste the result back to Owner

This is brittle. Information lives in chat history rather than the repo. A missed paste or window close loses context.

Phase 0.8 bridges the gap: every command becomes a structured object stored in the repo (and optionally a GitHub Issue). Each agent reads the command from the source of truth — not from a chat window.

---

## Objective

Make the command handoff between Owner, ChatGPT, Claude, and Codex repo-native by:

1. Defining two command modes: repo-file mode and GitHub Issue mode.
2. Providing a GitHub Issue template that mirrors the COMMAND_TEMPLATE.md structure.
3. Defining routing rules so each agent knows which commands are theirs and what to do if something is missing.
4. Reducing copy/paste to a single action: Owner pastes a command ID reference, not a full prompt.

**Phase 0.8 does NOT call the GitHub API.** It designs the bridge structure and templates. Automation (n8n, GitHub Actions, LangGraph) is a future phase concern.

---

## What Changes After Phase 0.8

| Before Phase 0.8 | After Phase 0.8 |
|-------------------|-----------------|
| Owner pastes full prompt into every chat | Owner pastes `CMD-X.X-XXX` — agents read the rest from the repo |
| Agent context depends on chat history | Agent context comes from `commands/COMMAND_INBOX.md` or GitHub Issue |
| Review instructions are repeated verbally | Codex reads acceptance criteria from the command record |
| Lost context if chat window closes | Command state is always recoverable from repo |
| No standard for what "done" looks like | Every command has explicit `acceptance_criteria` and `output_required` |

---

## Two Command Modes

### Mode 1 — Repo File (COMMAND_INBOX.md)

Used for all current phases. The command lives entirely in `commands/COMMAND_INBOX.md`.

Suitable when:
- The team is working locally
- No GitHub remote connection is needed
- The command is internal to the repo build process

### Mode 2 — GitHub Issue

The command is filed as a GitHub Issue using `commands/GITHUB_ISSUE_COMMAND_TEMPLATE.md`.
The repo's `COMMAND_INBOX.md` contains a reference row pointing to the Issue URL and number.

Suitable when:
- Owner wants a public or team-visible audit trail
- ChatGPT needs to reference the command from a browser context
- The command involves external stakeholders

See `commands/GITHUB_COMMAND_BRIDGE.md` for the full mode decision guide and field mapping.

---

## Command Flow

```
ChatGPT (Chief Architect) drafts command
    │
    │  using COMMAND_TEMPLATE.md or GITHUB_ISSUE_COMMAND_TEMPLATE.md
    ▼
Owner creates command record
    ├── Mode 1: pastes into commands/COMMAND_INBOX.md
    └── Mode 2: opens GitHub Issue, adds reference row to COMMAND_INBOX.md
    │
    │  sets status: ASSIGNED
    ▼
Claude Code (Builder)
    │  reads command_id from COMMAND_INBOX.md (or Issue)
    │  reads all fields: scope_files, forbidden_actions, acceptance_criteria
    │  executes within scope
    │  updates: CURRENT_PHASE.md, SESSION_SUMMARY.md, PHASE_LOG.md, AGENT_ACTIVITY_LOG.md
    │  sets status: BUILDER_DONE → REVIEW_REQUESTED
    ▼
Codex (Reviewer)
    │  reads command_id reference
    │  reads acceptance_criteria from command record
    │  runs review checks (per agents/REVIEWER_PROTOCOL.md)
    │  sets status: REVIEW_PASS or REVIEW_FAIL
    ▼
Owner
    │  reads REVIEW_PASS notification
    │  sets status: OWNER_APPROVED
    │  runs git commit/push
    │  sets status: CLOSED
    ▼
ChatGPT opens next phase command
```

---

## What This Phase Delivers

| File | Purpose |
|------|---------|
| `commands/GITHUB_COMMAND_BRIDGE.md` | Mode guide: when to use repo vs. Issue; field mapping; status-to-label mapping |
| `commands/GITHUB_ISSUE_COMMAND_TEMPLATE.md` | Markdown template for opening a GitHub Issue as a command |
| `commands/COMMAND_ROUTING_RULES.md` | Rules for who gets which command, error conditions (NEED_COMMAND_CLARIFICATION, SCOPE_CONFLICT, SECRET_RISK) |

---

## What Phase 0.8 Does NOT Do

- Does not call the GitHub API
- Does not create real GitHub Issues
- Does not automate status label updates
- Does not connect n8n or LangGraph to GitHub
- Does not open Phase 1

Automation of this bridge is a future concern (Phase 2+, n8n workflow or GitHub Actions).

---

## Done Criteria — Phase 0.8

- [x] `PHASE_0_8_GITHUB_COMMAND_BRIDGE.md` explains the problem, objective, flow, two modes, and what is out of scope
- [x] `GITHUB_COMMAND_BRIDGE.md` defines mode decision, field mapping, status-to-label mapping, ownership rules, close conditions
- [x] `GITHUB_ISSUE_COMMAND_TEMPLATE.md` provides a complete Issue template matching COMMAND_TEMPLATE.md fields
- [x] `COMMAND_ROUTING_RULES.md` defines routing by agent, no-concurrent-edit rule, NEED_COMMAND_CLARIFICATION / SCOPE_CONFLICT / SECRET_RISK error conditions
- [x] CMD-0.8-001 created in COMMAND_INBOX.md and COMMAND_STATUS.md
- [x] Handoff and logs updated
- [x] No secrets in any Phase 0.8 file
