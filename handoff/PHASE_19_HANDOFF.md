# Phase 19 Handoff

**Phase:** 19 — Owner Manual Sandbox Execution Instructions
**Created By:** Claude Code (Builder, AGT-02) — 2026-05-29
**Status:** INSTRUCTION_READY — READY FOR CODEX REVIEW

---

## Phase Distinction

| Phase | Type | What it produces |
|-------|------|-----------------|
| Phase 16 | Plan | Sandbox runtime validation plan — safety rules, preconditions, per-workflow checklists |
| Phase 17 | Prep | Dummy test payloads + evidence template — ready-to-use sandbox test data |
| Phase 18 | Review | Codex review gate on Phase 17 — PASS |
| Phase 19 | Instructions | Owner execution instructions — step-by-step guide, log template, evidence requirements |
| Phase 20 | Execution | Owner manually executes sandbox workflows and records evidence |

---

## Files Created

| File | Status |
|------|--------|
| `docs/31_PHASE_19_OWNER_MANUAL_SANDBOX_EXECUTION_INSTRUCTIONS.md` | Created |
| `handoff/PHASE_19_HANDOFF.md` | Created (this file) |

## Files Updated

| File | Change |
|------|--------|
| `handoff/CURRENT_PHASE.md` | Updated to Phase 19 INSTRUCTION_READY |
| `handoff/SESSION_SUMMARY.md` | Phase 19 session prepended |
| `logs/AGENT_ACTIVITY_LOG.md` | Phase 19 activity row prepended |
| `09_LOGS/PHASE_LOG.md` | Phase 19 entry prepended |

## Files Not Modified

| File | Reason |
|------|--------|
| `n8n/workflows/content_auto_skeleton.json` | Phase 19 is docs only — no workflow JSON changes |
| `n8n/workflows/creative_asset_auto_skeleton.json` | Phase 19 is docs only — no workflow JSON changes |
| `n8n/workflows/ads_pack_auto_skeleton.json` | Phase 19 is docs only — no workflow JSON changes |
| `n8n/workflows/crm_followup_auto_skeleton.json` | Phase 19 is docs only — no workflow JSON changes |
| `n8n/workflows/comment_inbox_reply_assistant_skeleton.json` | Phase 19 is docs only — no workflow JSON changes |
| `n8n/workflows/approval_publishing_skeleton.json` | Phase 19 is docs only — no workflow JSON changes |

---

## Commit / Push Status

| Action | Status |
|--------|--------|
| `git commit` | NOT DONE — awaiting Codex PASS + Owner OWNER_APPROVED |
| `git push` | NOT DONE |

---

## Phase 19 Document Summary

`docs/31_PHASE_19_OWNER_MANUAL_SANDBOX_EXECUTION_INSTRUCTIONS.md` contains:

| Section | Content |
|---------|---------|
| A — Purpose | Phase 19 is instruction/readiness only; does not execute workflow; prepares Owner for Phase 20 |
| B — Pre-Execution Checklist | 14 items (PC-01–PC-14): git status, commit, Phase 18 PASS, workflows imported and inactive, no real credentials, dummy payloads ready, log path selected, 60-minute window, Owner sign-off block |
| C — Workflow List | All 6 Phase 8 workflows: file path, n8n name, risk level, Phase 17 payload file |
| D — Manual Sandbox Execution Rules | Universal rules (10) + per-workflow extra rules for WF-03/04/05/06 |
| E — Step-by-Step Owner Instructions | 11 steps: open n8n → confirm inactive → open canvas → select trigger → use dummy payload → execute → observe output → screenshot → fill evidence template → create/update log → do not fix inside n8n |
| F — Evidence Requirements | 13 required fields per run including execution_type, active_status_before_run, result_status, screenshot_reference, log_file_reference |
| G — Required Log File Format | Log path `logs/phase_19_manual_sandbox_execution_log.md`; log entry template with all 13 required fields per run including credentials_used, real_customer_data_used, auto_post_executed, auto_reply_executed, ads_spend_executed |
| H — Explicit Non-Goals | 11 non-goals: production readiness, live execution, credential setup, activation, publishing automation, customer response automation, ads execution, workflow code fixes, production instance, schema validation, error trigger coverage |
| I — Next Phase Recommendation | Phase 20 — Owner Manual Sandbox Execution Evidence Capture; entry criteria; minimum viable scope; success criteria |
| Phase Connections | Phase 8 through Phase 20 relationship table |
| Safety Confirmation | 7-item confirmation table (no JSON changed, no active=true, no real credentials, no real data, no auto-post/ads, no production claim, secret scan CLEAN) |

---

## No-Execution Confirmation

| Item | Status |
|------|--------|
| n8n workflow executed | NO |
| n8n accessed | NO |
| Workflow activated | NO |
| Real credentials added | NO |
| Phase 8 workflow JSON modified | NO |
| Real customer data used | NO |
| Auto-post / auto-reply / ads triggered | NO |
| `active: true` introduced | NO |
| Production readiness claimed | NO |

---

## Acceptance Criteria

| Criterion | Status |
|-----------|--------|
| Phase 19 main doc created | PASS |
| Phase 19 handoff created | PASS |
| CURRENT_PHASE.md updated | PASS |
| SESSION_SUMMARY.md updated | PASS |
| AGENT_ACTIVITY_LOG.md updated | PASS |
| PHASE_LOG.md updated | PASS |
| All 6 workflow JSONs untouched | PASS |
| `active: true` not introduced | PASS |
| No real credentials added | PASS |
| No real customer data used | PASS |
| No auto-post / auto-reply / ads | PASS |
| No production readiness claimed | PASS |
| Pre-execution checklist (PC-01–PC-14) present | PASS |
| All 6 workflows listed in Section C | PASS |
| Universal + per-workflow rules in Section D | PASS |
| 11-step Owner instructions in Section E | PASS |
| Evidence requirements (13 fields) in Section F | PASS |
| Log file template with all required fields in Section G | PASS |
| Explicit non-goals (11 items) in Section H | PASS |
| Phase 20 recommendation in Section I | PASS |
| Secret scan (API keys, tokens, passwords, private keys) | CLEAN |

---

## Secret Scan

Scanned `docs/31_PHASE_19_OWNER_MANUAL_SANDBOX_EXECUTION_INSTRUCTIONS.md` and `handoff/PHASE_19_HANDOFF.md` for:

| Pattern | Result |
|---------|--------|
| `sk-ant-` (Anthropic key) | CLEAN |
| `sk-` (OpenAI key) | CLEAN |
| `private key` | CLEAN |
| GitHub PAT (`ghp_`, `github_pat_`) | CLEAN |
| JWT patterns | CLEAN |
| Telegram bot token (`\d{9}:`) | CLEAN |
| Google service account JSON | CLEAN |
| Hardcoded API key / token / password | CLEAN |

---

## Codex Review Instructions

Codex: please review the following:

1. Does `docs/31_PHASE_19_OWNER_MANUAL_SANDBOX_EXECUTION_INSTRUCTIONS.md` accurately serve as a ready-to-use Owner execution guide for Phase 20?
2. Are all 6 Phase 8 workflows correctly referenced in Section C?
3. Do the per-workflow extra rules in Section D adequately protect against real ads spend, real customer messaging, and real content publishing?
4. Does Section E Step 11 clearly prevent Owner from attempting to fix workflow logic inside n8n?
5. Does Section G log template include all required fields: `workflow_name`, `payload_file`, `execution_type`, `active_status_before_run`, `credentials_used`, `real_customer_data_used`, `auto_post_executed`, `auto_reply_executed`, `ads_spend_executed`, `result`, `evidence_files`, `owner_decision`, `next_action`?
6. Does Section H explicitly exclude all forbidden activities?
7. Confirm: no `active: true` introduced, no real credentials present, no workflow JSON modified, secret scan CLEAN.

Output: **PASS** / **PASS WITH NOTES** / **FAIL**

---

## Commit Instruction (after Codex PASS + Owner OWNER_APPROVED)

```
git add docs/31_PHASE_19_OWNER_MANUAL_SANDBOX_EXECUTION_INSTRUCTIONS.md
git add handoff/PHASE_19_HANDOFF.md
git add handoff/CURRENT_PHASE.md
git add handoff/SESSION_SUMMARY.md
git add logs/AGENT_ACTIVITY_LOG.md
git add 09_LOGS/PHASE_LOG.md
git commit -m "docs: add phase 19 owner manual sandbox execution instructions"
```
