# Agent OS Operating Manual — FnB OS V1

Created By: Claude Code (Builder, AGT-02) — 2026-05-30 (Phase 23 — Agent OS Layer)
Type: Governance — Primary Agent Reference
Scope: All AI agents operating in this repository

---

## 1. Purpose

This manual is the **single entry point** for agent operation in FnB OS V1.

It does not replace the detailed governance documents in `docs/governance/` — those remain authoritative for their respective areas. This manual:
- Indexes all governance documents
- Defines the standard phase lifecycle
- Provides the session startup procedure
- Summarizes operating constraints in one place

**Every new agent session should begin by reading this file and `handoff/CURRENT_PHASE.md`.**

---

## 2. Agent Roles

| Role | Agent | Authority | Restrictions |
|------|-------|-----------|--------------|
| Owner | Bo Bao | Final approver. Highest authority on all gates. | — |
| Chief Architect | ChatGPT | Designs phases, writes specs, creates commands. | Cannot commit, push, or execute. Cannot review own designs. |
| Builder | Claude Code (AGT-02) | Executes builds within approved `scope_files`. Creates/modifies files. Updates logs, handoff, tracking files. | Cannot design phases. Cannot approve own work. Cannot push without Owner approval. Cannot touch files outside `scope_files`. |
| Reviewer | Codex | Reviews Builder output. Returns PASS / PASS WITH NOTES / BLOCK. | Cannot commit, push, or execute. Cannot review own work. |
| Source of Truth | GitHub (`main`) | Canonical record of all approved committed work. | — |
| Runtime Automation | n8n | Executes approved workflow automations. | Must never be activated without Owner explicit approval. |
| Future Orchestrator | LangGraph | Planned for future phase — not active in OS V1. | No current role. |
| Worker Agents | Gemini / Antigravity / others | Optional support agents assigned per phase. | Only when explicitly assigned in the phase command. No independent authority. |

---

## 3. Agent Hierarchy

```
Owner (highest authority)
  └── GitHub / repo artifacts (source of truth)
        └── ChatGPT (defines phase plan and scope)
              └── Claude Code (builds within approved scope)
                    └── Codex (reviews only — no write access)
                          └── n8n / runtime (executes only when Owner approves)
```

Key rules:
- **Owner approval overrides everything.**
- **Repo files are source of truth over chat history, screenshots, or agent memory.**
- ChatGPT defines scope — Builder does not expand scope unilaterally.
- Codex reviews only — no commits, no pushes.
- Runtime systems are never changed unless explicitly in the phase's approved scope.

---

## 4. Standard Phase Lifecycle

Every phase in FnB OS V1 follows this lifecycle:

| Step | Actor | Action |
|------|-------|--------|
| 1. Phase proposal | ChatGPT | Writes phase plan, scope, and implementation spec |
| 2. Owner approval | Owner | Reviews plan, approves scope (`OWNER_APPROVED`) |
| 3. Builder implementation | Claude Code | Creates/modifies files within `scope_files` only |
| 4. Builder validation | Claude Code | Runs pre-commit checklist: git status, secret scan, workflow JSON check, active:true check, log/handoff update |
| 5. Local commit | Claude Code | `git commit` only — does NOT push |
| 6. Reviewer validation | Codex | Reviews files, returns PASS / PASS WITH NOTES / BLOCK (if available) |
| 7. Push approval | Owner | Explicitly approves push (`OWNER_APPROVED` for push) |
| 8. Push to GitHub | Claude Code | `git push origin main` |
| 9. Phase handoff | Claude Code | Updates `CURRENT_PHASE.md`, `SESSION_SUMMARY.md`, `PHASE_LOG.md`, `AGENT_ACTIVITY_LOG.md` |
| 10. Next phase | ChatGPT | Plans next phase based on current repo state |

**Notes:**
- Steps 5 and 7 are separate gates. Commit approval ≠ push approval.
- If Codex is unavailable, Owner performs direct review (step 6 becomes Owner review).
- If a step cannot proceed, set status to `BLOCKED` and report to Owner.

---

## 5. Session Startup Procedure

**Every new agent session must read these files before doing any work:**

| Order | File | Why |
|-------|------|-----|
| 1 | `handoff/CURRENT_PHASE.md` | Current phase name and status |
| 2 | `handoff/SESSION_SUMMARY.md` | Latest session state, decisions, and next actions |
| 3 | Latest phase handoff file (`handoff/PHASE_XX_HANDOFF.md`) | Phase-specific context, acceptance criteria, blockers |
| 4 | `docs/governance/AGENT_OS_OPERATING_MANUAL.md` (this file) | Startup and operation rules |
| 5 | `docs/governance/AGENT_OPERATION_RULES.md` | Full agent role and constraint rules |
| 6 | `docs/governance/OWNER_APPROVAL_GATE.md` | Which actions require Owner approval |
| 7 | `docs/governance/REPO_VALIDATION_CHECKLIST.md` | Pre-commit validation procedure |

After reading, confirm:
- Current branch is `main`
- `git status --short` is clean (or understand what is pending)
- `git log -1 --oneline` matches the expected HEAD from `SESSION_SUMMARY.md`

---

## 6. Operating Constraints

These constraints apply to **every session** regardless of phase:

| Constraint | Rule |
|------------|------|
| No secrets | Never write API keys, tokens, passwords, private keys, or credentials. Use `REPLACE_WITH_*` placeholders. |
| No auto-post | Never post content to social media, blogs, or any public channel. |
| No auto-reply | Never send messages to real customers (Zalo, Messenger, SMS, comment reply). |
| No ads spend | Never commit advertising budget or trigger paid campaigns. |
| No runtime execution | Never execute n8n workflows, call external APIs, or trigger live automation. |
| No `active: true` | Never introduce `"active": true` in any workflow JSON file. |
| No workflow JSON modification | Do not modify `n8n/workflows/*.json` unless the phase's `scope_files` explicitly includes the file. |
| No push without approval | Never run `git push` without explicit Owner `OWNER_APPROVED` for that specific push. |
| No CI unless requested | Do not add `.github/workflows/` files unless explicitly authorized in the phase spec. |
| No scope creep | If a needed file is not in `scope_files`, stop and set status to `BLOCKED`. |
| Session limit | Max 10 exchanges per session. At exchange 8, begin end-of-session preparation. |

---

## 7. Builder Rules

Before starting:
1. Run `git status --short` — confirm clean working tree.
2. Confirm branch: `git branch --show-current` → must be `main`.
3. Confirm HEAD: `git log -1 --oneline` → matches expected from `SESSION_SUMMARY.md`.
4. Read `scope_files` from active command — only touch those files.

During build:
- Create or modify only files in `scope_files`.
- Do not introduce secrets, credentials, or real customer data.
- Do not modify n8n workflow JSON unless explicitly authorized.
- Do not set `"active": true` anywhere.

Before finishing:
1. Run pre-commit validation (`docs/governance/REPO_VALIDATION_CHECKLIST.md`).
2. Update `handoff/CURRENT_PHASE.md`.
3. Update `handoff/SESSION_SUMMARY.md`.
4. Prepend new row to `logs/AGENT_ACTIVITY_LOG.md`.
5. Prepend new entry to `09_LOGS/PHASE_LOG.md`.
6. Create/update phase handoff file (`handoff/PHASE_XX_HANDOFF.md`).
7. If validation passes and phase requested local commit: `git commit`.

End-of-session report must include:
- Files created and modified
- Validation results (branch, status, secret scan, workflow JSON, active:true, CI)
- Commit hash (if committed)
- `git status --short` after commit
- Next recommended action for Owner

---

## 8. Reviewer Rules

When acting as Reviewer (Codex):
- Read only. Do not modify any files.
- Do not run `git commit` or `git push`.
- Do not execute n8n workflows or any runtime action.
- Review against the phase handoff file's acceptance criteria and Codex review instructions.
- Check: no secrets, no workflow JSON modified outside scope, no `active:true`, no production readiness claimed.
- Output exactly one of:
  - `PASS` — all checks met
  - `PASS WITH NOTES` — all checks met, minor observations
  - `BLOCK` — one or more checks failed; list what failed

---

## 9. Owner Approval Gates Summary

For full gate definitions see `docs/governance/OWNER_APPROVAL_GATE.md`.

| Gate | Required for |
|------|-------------|
| Build approval | Starting build work |
| Commit approval | Running `git commit` |
| Push approval | Running `git push` (separate from commit) |
| Runtime import approval | Importing workflow into n8n |
| Runtime execution approval | Triggering a workflow in n8n |
| Customer-facing output approval | Any publish, post, reply, or message to real users |
| Ads spend approval | Any advertising budget commitment |
| Publishing approval | Publishing content to any public platform |
| Emergency rollback approval | Reverting commits or resetting branch |

Key rule: **Local commit ≠ push authorization.** Each gate is independent.

---

## 10. Session Handoff Rule

- Maximum **10 exchanges** per agent session.
- At exchange 8: start updating `SESSION_SUMMARY.md` and preparing end-of-session report.
- At exchange 10: stop all new work, finalize handoff, signal to Owner that a new session is needed.
- **New session must begin from repo artifacts** — not from chat history, screenshots, or agent memory.
- If state is not in a file, it does not count.

Required before ending session:

| File | Must be updated |
|------|----------------|
| `handoff/SESSION_SUMMARY.md` | Latest session state (14 required fields — see `SESSION_HANDOFF_RULES.md`) |
| `handoff/CURRENT_PHASE.md` | Current phase status |
| `handoff/PHASE_XX_HANDOFF.md` | Phase-specific handoff |
| `logs/AGENT_ACTIVITY_LOG.md` | New row prepended |
| `09_LOGS/PHASE_LOG.md` | New entry prepended |

---

## 11. Related Governance Documents

| Document | When to read |
|----------|-------------|
| `docs/governance/AGENT_OS_OPERATING_MANUAL.md` (this file) | Start of every session |
| `docs/governance/AGENT_STARTUP_CHECKLIST.md` | Quick-start checklist — run before work |
| `docs/governance/AGENT_OPERATION_RULES.md` | Full agent roles, scope, session limit |
| `docs/governance/REPO_VALIDATION_CHECKLIST.md` | Before every commit |
| `docs/governance/PRE_COMMIT_PRE_PUSH_CHECKLIST.md` | Quick checkbox form — before commit and push |
| `docs/governance/OWNER_APPROVAL_GATE.md` | Before any gated action (commit, push, runtime, publish) |
| `docs/governance/SESSION_HANDOFF_RULES.md` | Before ending a session or handing off to a new agent |
| `docs/governance/README.md` | Governance directory index |

---

*FnB OS V1 — Vị Cuốn Growth OS*
*GitHub: https://github.com/bao-c2505e/fnb-os-v1 (branch: main)*
