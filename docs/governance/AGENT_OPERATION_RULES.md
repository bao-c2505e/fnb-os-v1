# Agent Operation Rules — FnB OS V1

Created By: Claude Code (Builder, AGT-02) — 2026-05-30 (Phase 22 — ECC Lite Repo Governance)
Type: Governance — Mandatory
Scope: All AI agent sessions in this repository

---

## 1. Agent Roster

| Role | Agent | Responsibilities | Restrictions |
|------|-------|-----------------|--------------|
| Owner | Bo Bao | Approves plans, commits, pushes, runtime execution, and customer-facing actions. Final authority on all gates. | — |
| Chief Architect | ChatGPT | Designs phases, creates commands, writes implementation specs. | Cannot commit, push, or execute. Cannot review own designs. |
| Builder | Claude Code (AGT-02) | Executes build commands within approved scope. Creates/modifies files within `scope_files`. Updates logs, handoff, and tracking files. | Cannot design phases. Cannot approve own work. Cannot push without Owner approval. Cannot modify files outside `scope_files`. |
| Reviewer | Codex | Reviews Builder output. Checks correctness, security, and scope compliance. Outputs PASS / PASS WITH NOTES / FAIL. | Cannot commit or push. Cannot review own work. Cannot be Builder on the same phase. |
| Source of Truth | GitHub (main branch) | Canonical record of all committed, approved work. | — |
| Runtime Automation | n8n | Executes approved workflow automations. | Must never be activated without Owner explicit approval. |
| Future Chief Orchestrator | LangGraph | Future phase — not active in OS V1. | No current role. Do not reference as active. |

---

## 2. One Phase = One Main Builder

- Each phase has exactly one assigned Builder.
- The assigned Builder is recorded in `commands/COMMAND_INBOX.md` under `assigned_builder`.
- A new Builder session must not begin on a phase already in progress by another Builder session unless explicitly handed off via `handoff/SESSION_SUMMARY.md`.

---

## 3. Scope Compliance

- Builder must read `scope_files` from the active command before starting work.
- Builder must only create or modify files listed in `scope_files`.
- If a file needed for the phase is not in `scope_files`, the Builder must stop and set command status to `BLOCKED`.
- Builder must never modify:
  - n8n workflow JSON files (unless explicitly in `scope_files`)
  - `.env` or secret files
  - Credential files
  - GitHub Actions / `.github/workflows/` files (unless explicitly in `scope_files`)
  - Runtime scripts that execute real automation
  - Production/runtime configuration

---

## 4. Reviewer Rules

- Reviewer (Codex) must not commit or push.
- Reviewer must not be assigned as Builder on the same phase.
- Reviewer output must be one of: PASS / PASS WITH NOTES / FAIL.
- If Codex is unavailable, Owner performs direct review and marks `OWNER_REVIEWED`.

---

## 5. No Secrets

- No API keys, tokens, passwords, private keys, or credentials may appear in any file.
- Use `REPLACE_WITH_*` or `[FILL]` as placeholders where credentials are structurally required.
- Secret scan must be run before every commit. Patterns to scan:
  - `API_KEY`, `SECRET`, `TOKEN`, `PASSWORD`, `PRIVATE_KEY`
  - `sk-`, `xoxb`, `ghp_`, `github_pat_`
  - `anthropic`, `openai`, `AKIA`
  - PEM header: `-----BEGIN`

---

## 6. No Runtime Execution Without Explicit Owner Approval

- Builder must never execute n8n workflows.
- Builder must never call external APIs.
- Builder must never trigger live automation.
- Builder must never set `"active": true` in any workflow JSON.
- All runtime execution requires explicit Owner approval recorded in the relevant handoff or command.

---

## 7. No Customer-Facing Automation Without Owner Approval

The following actions are **always prohibited** unless Owner has given explicit approval for that specific action in that specific session:

| Prohibited Action | Reason |
|-------------------|--------|
| Auto-post to social media | May publish unapproved content |
| Auto-reply to customer comments | May send incorrect or harmful responses |
| Auto-reply via Zalo / Messenger / SMS | Direct customer messaging without human review |
| Auto-spend on ads | Uncontrolled financial commitment |
| Auto-publish to any platform | Content may be wrong, off-brand, or premature |
| Auto-approve content | Bypasses Owner review gate |

---

## 8. Session Limit

- Each AI agent session has a maximum of **10 exchanges**.
- At exchange 8, the Builder must update `handoff/SESSION_SUMMARY.md` and begin preparing the end-of-session report.
- At exchange 10, the Builder must stop, finalize `SESSION_SUMMARY.md`, and request a new session from the Owner.
- The new session must begin by reading `handoff/SESSION_SUMMARY.md` + `handoff/CURRENT_PHASE.md` + the relevant phase handoff file.

---

## 9. End-of-Session Builder Report

Before ending a session, the Builder must report:

1. Files changed (created / modified / unchanged)
2. Validation results:
   - `git status --short` output
   - Secret scan result (CLEAN or BLOCKED)
   - Workflow JSON modified? (YES / NO)
   - `"active": true` introduced? (YES / NO)
   - Runtime execution performed? (YES / NO)
   - CI/CD files added? (YES / NO)
3. Latest commit hash (if a commit was made)
4. Git status after commit

---

## 10. Commit and Push Gates

| Action | Condition |
|--------|-----------|
| Local commit | Allowed after Builder validation passes and phase spec permits local commit |
| Push to GitHub | Requires explicit Owner approval — `OWNER_APPROVED` recorded in command or handoff |
| Force push | Never allowed |
| Push to main | Only after Owner review and approval |

---

## 11. Guardrails Summary

| Rule | Status |
|------|--------|
| No hardcoded secrets | MANDATORY |
| No `"active": true` in workflow JSON | MANDATORY |
| No runtime execution without Owner approval | MANDATORY |
| No customer-facing output without Owner approval | MANDATORY |
| No auto-post / auto-reply / ads spend | MANDATORY |
| No files outside `scope_files` | MANDATORY |
| No push without Owner approval | MANDATORY |
| No self-review by Builder | MANDATORY |
| Session max 10 exchanges | MANDATORY |
| Update SESSION_SUMMARY.md before ending session | MANDATORY |

---

*Related:*
- `handoff/SESSION_SUMMARY.md` — Current session state
- `handoff/CURRENT_PHASE.md` — Current phase status
- `commands/COMMAND_INBOX.md` — Active commands
- `docs/governance/OWNER_APPROVAL_GATE.md` — Approval gate definitions
- `docs/governance/SESSION_HANDOFF_RULES.md` — Handoff protocol
- `docs/governance/REPO_VALIDATION_CHECKLIST.md` — Pre-commit validation
- `docs/governance/PRE_COMMIT_PRE_PUSH_CHECKLIST.md` — Commit and push gates
