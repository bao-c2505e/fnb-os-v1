# Pre-Commit / Pre-Push Checklist — FnB OS V1

Created By: Claude Code (Builder, AGT-02) — 2026-05-30 (Phase 22 — ECC Lite Repo Governance)
Type: Governance — Quick-Reference Checklist
Scope: Every commit and push in this repository

---

## Purpose

Lightweight, fast-reference checklist to run before every commit and push.
Full detail is in `docs/governance/REPO_VALIDATION_CHECKLIST.md`.

---

## Pre-Commit Checklist

Complete all items before running `git commit`.

### 1. Review Changes

- [ ] `git diff` reviewed — I know what is changing
- [ ] Only files from `scope_files` appear in the diff
- [ ] `.claude/` directory is NOT staged
- [ ] No unexpected files are staged

### 2. Secret Check

- [ ] Scanned all new/modified files for: `API_KEY`, `SECRET`, `TOKEN`, `PASSWORD`, `PRIVATE_KEY`, `sk-`, `xoxb`, `ghp_`, `github_pat_`, `AKIA`, `-----BEGIN`
- [ ] No real secrets found (`REPLACE_WITH_*` placeholders are OK)
- [ ] Secret scan result: **CLEAN**

### 3. Runtime File Check

- [ ] No n8n workflow JSON files modified (unless explicitly authorized in `scope_files`)
- [ ] No `.github/workflows/` files modified (unless explicitly authorized)
- [ ] No production runtime configuration files modified

### 4. Workflow JSON Check

- [ ] `git diff --name-only` shows no `n8n/workflows/*.json` (or modification is explicitly authorized)
- [ ] `"active": true` is NOT present anywhere in the diff
- [ ] `active: true` (YAML form) is NOT present anywhere in the diff

### 5. Log and Handoff Updated

- [ ] `handoff/CURRENT_PHASE.md` updated with current phase status
- [ ] `handoff/SESSION_SUMMARY.md` updated with latest session state
- [ ] Phase-specific handoff file (`handoff/PHASE_XX_HANDOFF.md`) created or updated
- [ ] `logs/AGENT_ACTIVITY_LOG.md` — new row prepended
- [ ] `09_LOGS/PHASE_LOG.md` — new entry prepended

### 6. Scope Compliance

- [ ] Confirmed no files outside `scope_files` were modified
- [ ] No new dependencies or lock files introduced unless explicitly required

### 7. Commit Message

- [ ] Commit message follows convention: `docs: ...` / `feat: ...` / `ci: ...`
- [ ] Commit message clearly describes the phase intent
- [ ] Commit message contains no secrets

---

**Commit may proceed when all boxes are checked.**

---

## Pre-Push Checklist

Complete all items before running `git push`. Do NOT push without completing this checklist.

### 1. Owner Approval

- [ ] Owner has explicitly said **`OWNER_APPROVED`** for this push (not just for the commit)
- [ ] `OWNER_APPROVED` is recorded in the command (`commands/COMMAND_INBOX.md`) or the handoff file

### 2. Post-Commit State

- [ ] `git status` is clean after the commit (no unstaged changes)
- [ ] Latest commit hash has been recorded in `handoff/CURRENT_PHASE.md` or `handoff/SESSION_SUMMARY.md`
- [ ] `git log -1` confirms the correct commit is at HEAD

### 3. No Unreviewed Runtime Changes

- [ ] All n8n workflow JSON changes (if any) have been reviewed by Codex or Owner
- [ ] No `"active": true` was introduced in the commit

### 4. Final Safety Check

- [ ] No secrets in any committed file
- [ ] No auto-post / auto-reply / ads spend capability introduced
- [ ] No live customer-facing automation introduced

### 5. Push Command

- [ ] Using `git push` (not `git push --force` — force push is never allowed)
- [ ] Pushing to `origin main`

---

**Push may proceed only when all boxes are checked AND Owner has said `OWNER_APPROVED`.**

---

## Quick Summary Table

| Gate | When | Requires |
|------|------|---------|
| Pre-commit | Before every `git commit` | Scope OK + Secret CLEAN + No active=true + Logs updated |
| Pre-push | Before every `git push` | All pre-commit + Owner `OWNER_APPROVED` |
| Runtime execution | Before any n8n run | Explicit Owner approval for that specific run |
| Customer-facing output | Before any publish/post/reply | Explicit Owner approval for that specific output |

---

*Full validation detail: `docs/governance/REPO_VALIDATION_CHECKLIST.md`*
*Approval gate definitions: `docs/governance/OWNER_APPROVAL_GATE.md`*
*Agent rules: `docs/governance/AGENT_OPERATION_RULES.md`*
