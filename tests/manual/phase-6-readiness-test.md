# Phase 6 — Manual Readiness Test

**Phase:** 6 — OS Readiness Pack
**Tester:** Owner or Codex
**Date:** [FILL on execution]
**Repo:** D:\FNB_OS_V1 (or GitHub: bao-c2505e/fnb-os-v1)

Run each check below. Mark `[x]` when confirmed. All items must pass before Phase 7 begins.

---

## A — Repository Clean State

- [ ] `git status --short` returns no output (working tree clean)
- [ ] `git branch` shows `main` as current branch
- [ ] `git log --oneline -1` shows the latest Phase commit (Phase 5 or later)
- [ ] No `.env` file is tracked (`git ls-files | grep .env` returns nothing)
- [ ] No API keys or tokens present in any committed file

---

## B — Required Folders Exist

- [ ] `agents/` exists and is non-empty
- [ ] `brand-brain/` exists and is non-empty
- [ ] `schemas/` exists and is non-empty
- [ ] `templates/` exists and is non-empty
- [ ] `module-sops/` exists and is non-empty
- [ ] `samples/vi-cuon/` exists and is non-empty
- [ ] `docs/` exists and contains docs 01–16
- [ ] `handoff/` exists and is non-empty
- [ ] `logs/` exists and contains AGENT_ACTIVITY_LOG.md
- [ ] `09_LOGS/` exists and contains PHASE_LOG.md
- [ ] `commands/` exists and contains COMMAND_INBOX.md

---

## C — Brand Brain Exists and Is Valid

- [ ] `brand-brain/vi-cuon.md` exists
- [ ] File contains section: Brand Snapshot
- [ ] File contains section: Target Customers
- [ ] File contains section: Tone of Voice
- [ ] File contains section: Content Pillars
- [ ] File contains section: Offer Rules
- [ ] File contains section: Compliance / Safety
- [ ] File contains section: Replaceable Brand Context
- [ ] Prices, address, and opening hours use `[FILL]` or `[OWNER_TO_PROVIDE_*]` — not invented values

---

## D — All Schemas Exist

- [ ] `schemas/content-output.schema.json` exists
- [ ] `schemas/creative-brief.schema.json` exists
- [ ] `schemas/ads-pack.schema.json` exists
- [ ] `schemas/crm-followup.schema.json` exists
- [ ] `schemas/comment-inbox-reply.schema.json` exists
- [ ] `schemas/approval-status.schema.json` exists
- [ ] `schemas/log-entry.schema.json` exists
- [ ] All 7 schema files are valid JSON (open each — no parse errors)
- [ ] `schemas/crm-followup.schema.json` has `"const": true` on `human_review_required`
- [ ] `schemas/comment-inbox-reply.schema.json` has `"const": true` on `human_review_required`

---

## E — All Templates Exist

- [ ] `templates/content-output-template.md` exists
- [ ] `templates/creative-brief-template.md` exists
- [ ] `templates/ads-pack-template.md` exists
- [ ] `templates/crm-followup-template.md` exists
- [ ] `templates/comment-inbox-reply-template.md` exists
- [ ] `templates/approval-status-template.md` exists
- [ ] `templates/log-entry-template.md` exists
- [ ] Every template contains `## approval_status` heading
- [ ] `templates/crm-followup-template.md` contains `human_review_required` set to `true`
- [ ] `templates/comment-inbox-reply-template.md` contains `human_review_required` set to `true`

---

## F — All Sample Outputs Exist

- [ ] `samples/vi-cuon/content-sample.md` exists and has 3 samples
- [ ] `samples/vi-cuon/creative-brief-sample.md` exists and has 2 briefs
- [ ] `samples/vi-cuon/ads-pack-sample.md` exists and has 2 packs
- [ ] `samples/vi-cuon/crm-followup-sample.md` exists and has 2 sequences
- [ ] `samples/vi-cuon/comment-inbox-reply-sample.md` exists and has 5 replies
- [ ] `samples/vi-cuon/approval-status-sample.md` exists and has 5 records
- [ ] `samples/vi-cuon/log-entry-sample.md` exists and has 4 entries

---

## G — approval_status in Templates and Samples

- [ ] `templates/content-output-template.md` — `approval_status` is `Draft`
- [ ] `templates/creative-brief-template.md` — `approval_status` is `Draft`
- [ ] `templates/ads-pack-template.md` — `approval_status` is `Draft`
- [ ] `templates/crm-followup-template.md` — `approval_status` is `Draft`
- [ ] `templates/comment-inbox-reply-template.md` — `approval_status` is `Draft`
- [ ] `samples/vi-cuon/content-sample.md` — all samples have `approval_status: Draft`
- [ ] `samples/vi-cuon/ads-pack-sample.md` — all packs have `approval_status: Draft`
- [ ] `samples/vi-cuon/approval-status-sample.md` — all records are `Draft` or `Ready for Review` only

---

## H — human_review_required: true in CRM and Inbox Files

- [ ] `templates/crm-followup-template.md` — `human_review_required` is literal `true`
- [ ] `templates/comment-inbox-reply-template.md` — `human_review_required` is literal `true`
- [ ] `samples/vi-cuon/crm-followup-sample.md` — Sequence 1 has `human_review_required: true`
- [ ] `samples/vi-cuon/crm-followup-sample.md` — Sequence 2 has `human_review_required: true`
- [ ] `samples/vi-cuon/comment-inbox-reply-sample.md` — Reply 1 has `human_review_required: true`
- [ ] `samples/vi-cuon/comment-inbox-reply-sample.md` — Reply 2 has `human_review_required: true`
- [ ] `samples/vi-cuon/comment-inbox-reply-sample.md` — Reply 3 has `human_review_required: true`
- [ ] `samples/vi-cuon/comment-inbox-reply-sample.md` — Reply 4 has `human_review_required: true`
- [ ] `samples/vi-cuon/comment-inbox-reply-sample.md` — Reply 5 has `human_review_required: true`

---

## I — No n8n Workflow Exists Yet

- [ ] `n8n/` folder contains no `.json` workflow files (only `smoke-tests/` or empty subfolders)
- [ ] No file in the repo contains `"active": true` in an n8n workflow context
- [ ] No file named `*.workflow.json` exists anywhere in the repo

---

## J — No Runtime Script Exists Yet

- [ ] No `.py` files in `module-sops/`, `templates/`, `samples/`, `docs/` scoped to Phase 4–6
- [ ] No `.js` or `.ts` runtime scripts in Phase 4–6 scope folders
- [ ] No `.sh` shell scripts in Phase 4–6 scope folders

---

## K — Handoff and Log Files Updated

- [ ] `handoff/CURRENT_PHASE.md` shows Phase 6 as current phase
- [ ] `handoff/SESSION_SUMMARY.md` has Phase 6 as the latest (top) session block
- [ ] `handoff/PHASE_6_HANDOFF.md` exists
- [ ] `logs/AGENT_ACTIVITY_LOG.md` has a Phase 6 row
- [ ] `09_LOGS/PHASE_LOG.md` has a Phase 6 entry

---

## Result Summary

| Section | Total Items | Passed | Failed |
|---------|-------------|--------|--------|
| A — Repo Clean State | 5 | | |
| B — Folders Exist | 11 | | |
| C — Brand Brain | 9 | | |
| D — Schemas | 10 | | |
| E — Templates | 10 | | |
| F — Sample Outputs | 7 | | |
| G — approval_status | 8 | | |
| H — human_review_required | 9 | | |
| I — No n8n Workflow | 3 | | |
| J — No Runtime Script | 3 | | |
| K — Handoff/Logs | 5 | | |
| **Total** | **80** | | |

**Test date:** [FILL]
**Tester:** [FILL]
**Result:** PASS / FAIL / PASS WITH NOTES

**Notes:**
[FILL any failures or observations here]
