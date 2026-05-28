# 08 — Phase 2 SOP

Standard Operating Procedure: Agent Prompts + SOP Build
Version: 1.0
Created By: Claude Code (Builder) — 2026-05-28
Phase: 2

---

## Purpose

This SOP governs how Phase 2 work is executed: who does what, in what order, what is forbidden, and what must be true before any commit is made.

---

## Phase 2 Scope

Phase 2 delivers:
- Agent prompt files (`agents/*.md`) — role, mission, inputs, outputs, guardrails, approval requirements
- System documentation (`docs/07_AGENT_PROMPT_SYSTEM.md`, `docs/08_PHASE_2_SOP.md`)
- Handoff file (`handoff/PHASE_2_HANDOFF.md`)

Phase 2 does NOT include:
- n8n workflows or runtime automation
- Executable scripts or code
- Live publishing, scheduling, or ad activation
- Hardcoded credentials or API keys

---

## Phase 2 Workflow

### Step 1 — Chief Architect Creates Plan (ChatGPT)

- ChatGPT designs the phase scope and creates a command record in `commands/COMMAND_INBOX.md`.
- Command includes: `scope_files`, `acceptance_criteria`, `forbidden_actions`, `done_criteria`.
- ChatGPT does not modify files directly.

### Step 2 — Owner Approves Plan

- Owner reviews the command record.
- Owner gives explicit approval (written, Telegram, or verbal logged).
- Build does not start until Owner approves.

### Step 3 — Claude Code Builds Files

- Claude Code reads the active command and locks scope.
- Creates all files listed in `scope_files` only.
- Does not touch anything outside scope.
- If a needed file is not in scope → stop, set status BLOCKED, notify Owner.

### Step 4 — Claude Code Validates

Before declaring done, Claude Code verifies:

- [ ] All `scope_files` artifacts exist at their stated paths
- [ ] Every `acceptance_criteria` item is PASS
- [ ] No secrets in any file (`git diff --check` or manual scan)
- [ ] `handoff/CURRENT_PHASE.md` = BUILDER_DONE_PENDING_REVIEW
- [ ] `SESSION_SUMMARY.md` updated
- [ ] `PHASE_LOG.md` has new entry
- [ ] `AGENT_ACTIVITY_LOG.md` has new row
- [ ] `git status` shows only in-scope files

### Step 5 — Codex Reviews

- Codex reads all files in scope + handoff/log files.
- Checks 5 FAIL conditions: secret leak, out-of-scope code, auto-post/ads, missing files, broken structure.
- Outputs: PASS / PASS WITH NOTES / FAIL with evidence.
- If FAIL: Claude Code fixes and resubmits. Owner is notified.

### Step 6 — Owner Approves Commit

- Owner reviews Codex verdict.
- Owner gives explicit `OWNER_APPROVED` to commit.
- Claude Code commits only after this approval.
- Claude Code pushes only if Owner also approves push.

---

## What Owner Does and Does Not Do

### Owner does:
- Approve phase plans
- Approve commits after Codex PASS
- Approve publishing of content
- Approve any ad spend or real customer communication

### Owner does not:
- Manually debug files by editing them directly without a command
- Paste screenshots instead of updating log files
- Communicate issues informally without a repo record
- Skip Codex review to speed up the process

> **Rule:** Every issue, decision, and change must be written into the repo — log file, handoff file, or command update. Screenshots and chat messages are not repo records.

---

## What Agents Do and Do Not Do in Phase 2

| Action | Chief Architect | Builder | Reviewer | Owner |
|--------|----------------|---------|----------|-------|
| Design phase plan | ✓ | — | — | Approves |
| Create/edit files | — | ✓ | — | — |
| Commit to git | — | — | — | Approves |
| Push to GitHub | — | — | — | Approves |
| Review output | — | — | ✓ | — |
| Create n8n workflows | — | — | — | Phase 3+ |
| Auto-post content | — | — | — | Never in Phase 2 |
| Run ads | — | — | — | Never in Phase 2 |

---

## Phase 2 Forbidden Actions

The following are strictly forbidden in Phase 2 for all agents:

| Forbidden | Reason |
|-----------|--------|
| Creating n8n workflow JSON | Runtime automation is Phase 3+ |
| Writing executable scripts | Out of scope for Phase 2 |
| Hardcoding API keys / tokens / passwords | Security — never allowed |
| Auto-posting content to any platform | Requires Owner approval + future phase |
| Sending real customer messages | Requires Owner approval + future phase |
| Running ads or spending budget | Requires Owner approval + future phase |
| Committing before Codex PASS | Quality gate must complete first |
| Pushing before OWNER_APPROVED | Authorization required |

---

## Escalation Path

If any step cannot complete:

1. Builder sets status `BLOCKED` in `commands/COMMAND_INBOX.md`.
2. Builder records `blocked_reason` in `handoff/SESSION_SUMMARY.md`.
3. Owner is notified.
4. Chief Architect updates the command with resolution or revised scope.
5. Build resumes from the blocked step.

---

## Key Principle

> Phase 2 produces only markdown files: agent definitions, SOPs, and handoff docs.
> No automation. No code. No live connections.
> Everything goes through the approval gate before commit.
