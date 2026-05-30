# Repo Validation Checklist — FnB OS V1

Created By: Claude Code (Builder, AGT-02) — 2026-05-30 (Phase 22 — ECC Lite Repo Governance)
Type: Governance — Mandatory Pre-Commit Checklist
Scope: All phases before committing work

---

## Purpose

This checklist must be completed before any `git commit` in this repository.
It ensures that no secrets, runtime changes, or out-of-scope modifications enter the commit history.

---

## Section A — Before Starting Work

| Check | Action | Expected Result |
|-------|--------|----------------|
| A-01 | Run `git status --short` | Working tree clean before starting |
| A-02 | Confirm current branch | `main` |
| A-03 | Confirm latest HEAD | Matches expected last commit from `handoff/CURRENT_PHASE.md` |
| A-04 | Read active command from `commands/COMMAND_INBOX.md` | Assigned Builder = Claude Code, Status = ASSIGNED |
| A-05 | Read `handoff/CURRENT_PHASE.md` | Phase status understood |
| A-06 | Read `handoff/SESSION_SUMMARY.md` | Previous session context understood |
| A-07 | List `scope_files` from active command | All planned files are within scope |

---

## Section B — Inspect Changed Files

| Check | Action | Expected Result |
|-------|--------|----------------|
| B-01 | Run `git diff --name-only` | Only `scope_files` listed |
| B-02 | Run `git status` | No unexpected files modified or untracked |
| B-03 | Review each changed file manually | Content matches phase intent |
| B-04 | Confirm no files outside `scope_files` were touched | PASS |
| B-05 | Confirm `.claude/` directory not staged | `.claude/` must never be committed |

---

## Section C — Secret Scan

Scan all new or modified files for the following patterns. If any match is found, **stop immediately** and do not commit.

| Pattern | Risk | Action if Found |
|---------|------|----------------|
| `API_KEY` | Credential | STOP — remove before commit |
| `SECRET` | Credential | STOP — check if structural or actual secret |
| `TOKEN` | Credential | STOP — use `REPLACE_WITH_TOKEN` instead |
| `PASSWORD` | Credential | STOP — remove before commit |
| `PRIVATE_KEY` | Credential | STOP — remove before commit |
| `sk-` | OpenAI / Anthropic API key prefix | STOP — remove before commit |
| `xoxb` | Slack bot token prefix | STOP — remove before commit |
| `ghp_` | GitHub PAT prefix | STOP — remove before commit |
| `github_pat_` | GitHub fine-grained PAT | STOP — remove before commit |
| `anthropic` | Anthropic reference (check context) | Review — may be a safe doc reference |
| `openai` | OpenAI reference (check context) | Review — may be a safe doc reference |
| `AKIA` | AWS access key prefix | STOP — remove before commit |
| `-----BEGIN` | PEM private key block | STOP — remove before commit |

**Exception:** `REPLACE_WITH_*` placeholders are safe and expected. Do not flag them.

**Secret scan result options:**
- `CLEAN` — No secrets found in new/modified files
- `BLOCKED` — Possible secret found; commit must not proceed

---

## Section D — Workflow JSON Check

| Check | Action | Expected Result |
|-------|--------|----------------|
| D-01 | Run `git diff --name-only` | No files matching `n8n/workflows/*.json` should appear unless phase explicitly permits modification |
| D-02 | If any workflow JSON appears in diff | Stop and confirm this was explicitly authorized in `scope_files` |
| D-03 | Confirm `"active": true` not present in diff | Run: search diff for `active.*true` |
| D-04 | Confirm `active: true` (YAML form) not present in diff | PASS |

---

## Section E — Runtime Execution Confirmation

| Check | Action | Expected Result |
|-------|--------|----------------|
| E-01 | Confirm no n8n workflow was executed | Builder explicitly states: no n8n run performed |
| E-02 | Confirm no external API was called | Builder explicitly states: no external API called |
| E-03 | Confirm no live workflow was triggered | Builder explicitly states: no live workflow triggered |
| E-04 | Confirm no production system was modified | Builder explicitly states: no production system touched |

---

## Section F — Handoff and Log Updates

| Check | Action | Expected Result |
|-------|--------|----------------|
| F-01 | `handoff/CURRENT_PHASE.md` updated | Reflects current phase status |
| F-02 | `handoff/SESSION_SUMMARY.md` updated | Concise latest session state recorded |
| F-03 | Phase-specific handoff file created/updated | `handoff/PHASE_XX_HANDOFF.md` present |
| F-04 | `logs/AGENT_ACTIVITY_LOG.md` updated | New row prepended with this session's activity |
| F-05 | `09_LOGS/PHASE_LOG.md` updated | New entry prepended with this phase's milestone |

---

## Section G — Commit Message

| Check | Action | Expected Result |
|-------|--------|----------------|
| G-01 | Draft commit message | Follows pattern: `docs: [description]` or `feat: [description]` |
| G-02 | Commit message matches phase intent | No vague messages like "update files" |
| G-03 | Commit message does not contain secrets | CLEAN |

---

## Section H — Final Pre-Commit Gate

| Check | Result |
|-------|--------|
| Branch is `main` | YES / NO |
| `git status` clean before work | YES / NO |
| Only `scope_files` modified | YES / NO |
| Secret scan | CLEAN / BLOCKED |
| Workflow JSON modified without authorization | YES / NO |
| `"active": true` introduced | YES / NO |
| Runtime execution performed | YES / NO |
| Handoff and log files updated | YES / NO |
| Commit message correct | YES / NO |

**Commit may proceed only when:**
- All YES items are YES
- Secret scan = CLEAN
- Workflow JSON modified without authorization = NO
- `"active": true` introduced = NO
- Runtime execution = NO

---

## Section I — Push Gate (Separate from Commit)

**Push to GitHub requires Owner explicit approval. Commit alone does not authorize push.**

| Check | Required |
|-------|---------|
| Owner has said `OWNER_APPROVED` for this push | YES |
| `git status` clean after commit | YES |
| Latest commit hash recorded in handoff | YES |
| No unreviewed runtime changes present | YES |
| No secrets in committed files | YES |
| Force push (`--force`) | NEVER |

---

*Related:*
- `docs/governance/AGENT_OPERATION_RULES.md` — Agent role and scope rules
- `docs/governance/PRE_COMMIT_PRE_PUSH_CHECKLIST.md` — Quick-reference checklist
- `docs/governance/OWNER_APPROVAL_GATE.md` — Approval gate definitions
