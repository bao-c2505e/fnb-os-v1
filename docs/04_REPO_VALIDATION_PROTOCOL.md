# Repo Validation Protocol — FnB OS V1

Version: 1.0
Date: 2026-05-28
Authority: ChatGPT (Chief Architect)
Executed by: Claude Code (Builder) + Codex (Reviewer)

Run this protocol at session start, at session end, and before any commit.

---

## 1. Pre-Session Validation (Builder runs before starting work)

| # | Check | Command / Action | Pass Condition |
|---|-------|-----------------|----------------|
| 1 | Working tree | `git status --short` | Only expected files modified; no untracked secrets |
| 2 | On correct branch | `git branch --show-current` | `main` (or feature branch as specified in command) |
| 3 | Sync with remote | `git fetch && git status` | Not behind remote HEAD |
| 4 | No secret files staged | Scan for `.env`, `credentials.*`, `*_key.json` | None present in tracked changes |
| 5 | Active command exists | Read `commands/COMMAND_INBOX.md` | First non-CLOSED record found; status is `ASSIGNED` or `IN_PROGRESS` |
| 6 | Phase file coherent | Read `handoff/CURRENT_PHASE.md` | Phase number matches active command |

If any check fails → do not start work. Set command status `BLOCKED`.

---

## 2. Post-Session Validation (Builder runs before declaring BUILDER_DONE)

| # | Check | How to Verify | Pass Condition |
|---|-------|--------------|----------------|
| 1 | Scope boundary | `git status --short` | Only `scope_files` listed as modified or new |
| 2 | Secret scan | Read every changed file; search for patterns below | No secrets found |
| 3 | Output artifacts | List `output_required` from command | Every artifact exists at its stated path |
| 4 | Schema validity | For each `.json` file changed: validate structure | Valid JSON; required fields present |
| 5 | Log updated | Read `logs/AGENT_ACTIVITY_LOG.md` | New row added for this session |
| 6 | Phase log updated | Read `09_LOGS/PHASE_LOG.md` | New entry added for this session |
| 7 | Handoff updated | Read `handoff/SESSION_SUMMARY.md` | Current session details recorded |
| 8 | Current phase updated | Read `handoff/CURRENT_PHASE.md` | Status = `BUILDER_DONE_PENDING_REVIEW` |
| 9 | No broken references | Check any `source:` or `ref:` links in changed docs | All referenced files exist |

---

## 3. Secret Scan Patterns

Search every changed file for these patterns before any commit. If found, stop immediately.

```
Patterns to flag:
- sk-[a-zA-Z0-9]{40,}                  (OpenAI API key)
- AIza[0-9A-Za-z-_]{35}               (Google API key)
- [0-9]:[A-Za-z0-9_-]{35}             (Telegram bot token)
- ghp_[A-Za-z0-9]{36}                 (GitHub personal access token)
- xoxb-[0-9-]+-[A-Za-z0-9]+           (Slack bot token)
- -----BEGIN.*PRIVATE KEY-----         (Private key)
- password\s*[:=]\s*[^\s$\[{]         (Hardcoded password)
- token\s*[:=]\s*[^\s$\[{]            (Hardcoded token)
- secret\s*[:=]\s*[^\s$\[{]           (Hardcoded secret)
```

If any pattern matches a real value (not a placeholder like `REPLACE_WITH_*`):
1. Do not commit.
2. Report immediately to Owner.
3. Request credential rotation.
4. Set command status `BLOCKED`.

---

## 4. Reviewer Validation (Codex runs on REVIEW_REQUESTED)

The Reviewer runs the same Post-Session Validation checks (Section 2) independently, plus:

| # | Additional Check | Pass Condition |
|---|-----------------|----------------|
| 10 | Role compliance | Builder did not commit, push, or perform Reviewer/Owner actions |
| 11 | n8n workflows (if any) | `active: false`; placeholder credentials; approval gate node present; log step present |
| 12 | Acceptance criteria | Every item from `acceptance_criteria` field explicitly met |

---

## 5. Pre-Commit Gate (Owner runs before git commit)

The Owner should verify:

1. Codex status = `REVIEW_PASS` on the active command.
2. `handoff/CURRENT_PHASE.md` status = `OWNER_APPROVED`.
3. `git diff --stat` shows only expected files.
4. No `.env` or credential files in `git status`.

Only then run:
```bash
git add [specific files from scope_files]
git commit -m "feat(phase-X.X): [description]"
git push
```

Never use `git add -A` or `git add .` — always add specific files.

---

## 6. Required Repo Structure

These paths must always exist. Validate after any phase that could affect structure:

```
D:\FNB_OS_V1\
├── AGENTS.md                        ← Agent manifest
├── CLAUDE.md                        ← Claude Code instructions
├── CODEX.md                         ← Codex reviewer instructions
├── commands/
│   ├── COMMAND_INBOX.md
│   └── COMMAND_STATUS.md
├── handoff/
│   ├── CURRENT_PHASE.md
│   └── SESSION_SUMMARY.md
├── logs/
│   └── AGENT_ACTIVITY_LOG.md
├── 09_LOGS/
│   └── PHASE_LOG.md
├── docs/
│   ├── 03_AGENT_OPERATING_RULES.md
│   ├── 04_REPO_VALIDATION_PROTOCOL.md
│   ├── 05_N8N_RUNTIME_RULES.md
│   └── 06_SECURITY_AND_APPROVAL_RULES.md
└── n8n/                             ← Workflow JSON files
```
