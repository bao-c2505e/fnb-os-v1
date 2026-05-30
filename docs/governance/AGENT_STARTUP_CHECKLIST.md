# Agent Startup Checklist — FnB OS V1

Created By: Claude Code (Builder, AGT-02) — 2026-05-30 (Phase 23 — Agent OS Layer)
Type: Governance — Quick-Start Checklist
Scope: Every new agent session in this repository

---

## Purpose

Run this checklist at the start of every Claude Code, Codex, or ChatGPT session before doing any work.
Takes ~2 minutes. Prevents scope errors, context confusion, and unsafe actions.

---

## Step 1 — Identity Check

Answer these questions before touching any file:

- [ ] **What is my role this session?**
  - [ ] Builder (Claude Code) — I will create/modify files within `scope_files`
  - [ ] Reviewer (Codex) — I will read and review only; I will NOT commit or push
  - [ ] Architect (ChatGPT) — I will plan only; I will NOT commit or push
  - [ ] Other worker agent — I have been explicitly assigned by the phase command

- [ ] **What is the current phase?** → Read `handoff/CURRENT_PHASE.md`

- [ ] **What is the approved scope?** → Read the active command in `commands/COMMAND_INBOX.md` or the phase spec
  - List `scope_files` here before starting: ___________________

- [ ] **Is there a BLOCKED status on the current phase?**
  - If YES → do not start new work. Report blocker to Owner first.

---

## Step 2 — Repo Check

Run the following commands and confirm expected results:

| Command | Expected Result | Actual |
|---------|----------------|--------|
| `git branch --show-current` | `main` | ___ |
| `git status --short` | (empty — clean) | ___ |
| `git log -1 --oneline` | Matches `latest_commit` in `SESSION_SUMMARY.md` | ___ |

- [ ] Branch is `main`
- [ ] Working tree is clean (or I understand what is pending from the previous session)
- [ ] Latest commit matches `SESSION_SUMMARY.md`

If status is NOT clean:
- Read `SESSION_SUMMARY.md` — understand what was left pending.
- Do NOT commit unreviewed files.
- Do NOT discard changes without understanding what they are.

---

## Step 3 — Source-of-Truth Check

Read these files in order:

- [ ] `handoff/CURRENT_PHASE.md` — current phase name and status
- [ ] `handoff/SESSION_SUMMARY.md` — latest session state, decisions made, next actions
- [ ] Latest phase handoff file (`handoff/PHASE_XX_HANDOFF.md`) — phase-specific context
- [ ] `docs/governance/AGENT_OS_OPERATING_MANUAL.md` — startup and operation rules
- [ ] `docs/governance/AGENT_OPERATION_RULES.md` — agent roles and constraints

After reading, confirm:
- [ ] I understand what was done in the last session
- [ ] I understand what needs to be done in this session
- [ ] I understand the next Owner action required
- [ ] I have NOT relied solely on chat history or screenshots to understand repo state

---

## Step 4 — Safety Check

Before touching any file, confirm all of these are TRUE:

| Safety Item | Confirmed? |
|-------------|-----------|
| I will NOT write any API keys, tokens, passwords, or credentials | YES / NO |
| I will NOT modify n8n workflow JSON unless it is in `scope_files` | YES / NO |
| I will NOT set `"active": true` in any file | YES / NO |
| I will NOT execute any n8n workflow or call any external API | YES / NO |
| I will NOT auto-post to social media or messaging platforms | YES / NO |
| I will NOT auto-reply to real customers | YES / NO |
| I will NOT commit ad spend or run paid campaigns | YES / NO |
| I will NOT push to GitHub without Owner saying `OWNER_APPROVED` | YES / NO |
| I will ONLY modify files listed in `scope_files` | YES / NO |
| I will update logs and handoff files before ending session | YES / NO |

If any item is NO → do not proceed. Resolve the constraint first.

---

## Step 5 — Output Checklist

Before finishing any session, confirm all of these are done:

### Files Changed
- [ ] All created files listed
- [ ] All modified files listed
- [ ] No files outside `scope_files` were touched
- [ ] `.claude/` directory was NOT staged or committed

### Validation Results
- [ ] `git status --short` run and result recorded
- [ ] Secret scan complete — result: CLEAN / BLOCKED
- [ ] No n8n workflow JSON modified (or modification was explicitly authorized)
- [ ] No `"active": true` introduced
- [ ] No runtime execution performed
- [ ] No `.github/workflows/` files added or modified

### Commit and Push
- [ ] If committed: commit hash recorded — `_______________`
- [ ] If committed: commit message matches phase intent
- [ ] NOT pushed unless Owner explicitly said `OWNER_APPROVED` for push
- [ ] `git status --short` after commit is clean

### Handoff Updated
- [ ] `handoff/CURRENT_PHASE.md` updated with current phase status
- [ ] `handoff/SESSION_SUMMARY.md` updated with this session's results
- [ ] Phase handoff file (`handoff/PHASE_XX_HANDOFF.md`) created or updated
- [ ] `logs/AGENT_ACTIVITY_LOG.md` — new row prepended
- [ ] `09_LOGS/PHASE_LOG.md` — new entry prepended

### Next Action
- [ ] Next recommended action clearly stated for Owner
- [ ] Reviewer (Codex) review requested if applicable
- [ ] Push decision left to Owner

---

## Quick Reference — What Requires Owner Approval

| Action | Owner approval required? |
|--------|-------------------------|
| Local `git commit` | YES — after Codex PASS (or Owner direct review) |
| `git push` | YES — separate explicit approval |
| Importing workflow into n8n | YES |
| Executing a workflow in n8n | YES |
| Publishing content | YES |
| Ads spend | YES |
| Auto-reply to customer | YES |
| Emergency rollback | YES |

---

*Full operating rules: `docs/governance/AGENT_OS_OPERATING_MANUAL.md`*
*Full governance index: `docs/governance/README.md`*
