# Phase 20A Handoff

**Phase:** 20A — Manual Sandbox Evidence Capture Pack
**Created By:** Claude Code (Builder, AGT-02) — 2026-05-29
**Status:** PACK_READY — READY FOR CODEX REVIEW

---

## Phase Summary

Phase 20A creates the evidence and log capture pack for the first Owner manual sandbox execution — specifically for `content_auto_skeleton` (WF-01, risk level: Standard).

Phase 20A is documentation only. No workflow was executed. No activation occurred. No credentials were added.

The actual manual sandbox run is Phase 20B.

---

## Phase Distinction

| Phase | Type | What it produces |
|-------|------|-----------------|
| Phase 17 | Prep | Dummy test payloads + evidence template for all 6 workflows |
| Phase 19 | Instructions | General Owner execution guide (all 6 workflows) |
| Phase 20A | Evidence Pack | Specific evidence/log capture pack for `content_auto_skeleton` |
| Phase 20B | Execution | Owner manually executes `content_auto_skeleton` and records evidence |

---

## Selected Workflow

| Field | Value |
|-------|-------|
| Workflow file | `n8n/workflows/content_auto_skeleton.json` |
| n8n name | FnB OS V1 — Content Auto [SKELETON] |
| Risk level | Standard |
| Selected reason | Lowest risk: no ads, no messaging, no webhook, no platform publish — best first run |

---

## Files Created

| File | Status |
|------|--------|
| `docs/32_PHASE_20A_MANUAL_SANDBOX_EVIDENCE_CAPTURE_PACK.md` | Created |
| `logs/phase_20a_content_auto_sandbox_evidence_log.md` | Created (blank template — Owner fills in Phase 20B) |
| `handoff/PHASE_20A_HANDOFF.md` | Created (this file) |

## Files Updated

| File | Change |
|------|--------|
| `handoff/CURRENT_PHASE.md` | Updated to Phase 20A PACK_READY |
| `handoff/SESSION_SUMMARY.md` | Phase 20A session prepended |
| `logs/AGENT_ACTIVITY_LOG.md` | Phase 20A activity row prepended |
| `09_LOGS/PHASE_LOG.md` | Phase 20A entry prepended |

## Files Not Modified

| File | Reason |
|------|--------|
| `n8n/workflows/content_auto_skeleton.json` | Phase 20A is docs only |
| `n8n/workflows/creative_asset_auto_skeleton.json` | Phase 20A is docs only |
| `n8n/workflows/ads_pack_auto_skeleton.json` | Phase 20A is docs only |
| `n8n/workflows/crm_followup_auto_skeleton.json` | Phase 20A is docs only |
| `n8n/workflows/comment_inbox_reply_assistant_skeleton.json` | Phase 20A is docs only |
| `n8n/workflows/approval_publishing_skeleton.json` | Phase 20A is docs only |

---

## Evidence Log Template Summary

`logs/phase_20a_content_auto_sandbox_evidence_log.md` contains:

| Section | Fields |
|---------|--------|
| Execution Record | phase, workflow_name, workflow_file, execution_type, execution_status (not_executed_yet), payload_file, payload_type, active_status_before_run, active_status_after_run, credentials_used, real_customer_data_used, auto_post_executed, auto_reply_executed, ads_spend_executed, production_readiness_claimed, execution_timestamp, n8n_execution_id, n8n_instance_url, operator |
| Node Execution Results | Per-node table for all 14 nodes: executed, result (green/red/skipped), key output observed |
| Key Output Fields | 10 key fields: brandBrainLoaded, brand_name, approval_status, content_id, platform, validation_pass, logEntry.log_id, logEntry.status, logWritten, approvalQueueStubReached |
| Forbidden Output Checks | FC-01–FC-06: Facebook API, OpenAI/Anthropic API, Google Sheets/Supabase, approval_status Approved/Published, real PII, active=true |
| Result Summary | result_summary, happy_path_completed, validation_branch_taken, forbidden_output_found, unexpected_behavior |
| Evidence Files | evidence_screenshot_files, evidence_template_copy, log_id_from_n8n |
| Issues Found | Issue table (ID, node, description, severity) |
| Post-Run Safety | 7 confirmation checkboxes |
| Owner Decision | owner_decision, next_action |
| Owner Sign-Off | Confirmation statement with Owner initials/date/time |

---

## Commit / Push Status

| Action | Status |
|--------|--------|
| `git commit` | NOT DONE — awaiting Codex PASS + Owner OWNER_APPROVED |
| `git push` | NOT DONE |

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
| Phase 20A main doc created (docs/32) | PASS |
| Evidence log template created | PASS |
| Handoff created | PASS |
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
| content_auto_skeleton selected + rationale documented | PASS |
| Node chain reference (all 14 nodes) documented | PASS |
| Pre-run safety checklist SR-01–SR-10 present | PASS |
| Owner manual run checklist F-01–F-23 present | PASS |
| Evidence capture checklist EC-01–EC-08 present | PASS |
| Screenshot naming convention defined | PASS |
| PASS/BLOCKED criteria defined | PASS |
| Explicit non-goals (13 items) documented | PASS |
| Phase 20B recommendation present | PASS |
| Evidence log has all required fields from task spec | PASS |
| Secret scan CLEAN | PASS |

---

## Secret Scan

Scanned `docs/32_PHASE_20A_MANUAL_SANDBOX_EVIDENCE_CAPTURE_PACK.md`, `logs/phase_20a_content_auto_sandbox_evidence_log.md`, and `handoff/PHASE_20A_HANDOFF.md` for:

| Pattern | Result |
|---------|--------|
| `sk-ant-` (Anthropic key) | CLEAN |
| `sk-` (OpenAI key) | CLEAN |
| `private key` | CLEAN |
| GitHub PAT (`ghp_`, `github_pat_`) | CLEAN |
| JWT patterns | CLEAN |
| Telegram bot token | CLEAN |
| Google service account JSON | CLEAN |
| Hardcoded API key / token / password | CLEAN |

---

## Codex Review Instructions

Codex: please review the following:

1. Does `docs/32_PHASE_20A_MANUAL_SANDBOX_EVIDENCE_CAPTURE_PACK.md` correctly scope Phase 20A to `content_auto_skeleton` only, with no claims about other workflows?
2. Does the node chain reference in Section D match the actual nodes in `n8n/workflows/content_auto_skeleton.json`?
3. Does the evidence log template `logs/phase_20a_content_auto_sandbox_evidence_log.md` include all required fields from the task spec: `phase`, `workflow_name`, `execution_type`, `execution_status`, `payload_file`, `payload_type`, `active_status_before_run`, `active_status_after_run`, `credentials_used`, `real_customer_data_used`, `auto_post_executed`, `auto_reply_executed`, `ads_spend_executed`, `production_readiness_claimed`, `execution_timestamp`, `n8n_execution_id`, `result_summary`, `evidence_screenshot_files`, `issues_found`, `owner_decision`, `next_action`?
4. Does Section L (non-goals) explicitly exclude production, auto-post, auto-reply, ads spend, real credentials, real customer data, workflow activation, and production readiness claim?
5. Does Section M clearly recommend Phase 20B as the next phase?
6. Confirm: no `active: true` introduced, no real credentials present, no workflow JSON modified, secret scan CLEAN.

Output: **PASS** / **PASS WITH NOTES** / **FAIL**

---

## Commit Instruction (after Codex PASS + Owner OWNER_APPROVED)

```
git add docs/32_PHASE_20A_MANUAL_SANDBOX_EVIDENCE_CAPTURE_PACK.md
git add logs/phase_20a_content_auto_sandbox_evidence_log.md
git add handoff/PHASE_20A_HANDOFF.md
git add handoff/CURRENT_PHASE.md
git add handoff/SESSION_SUMMARY.md
git add logs/AGENT_ACTIVITY_LOG.md
git add 09_LOGS/PHASE_LOG.md
git commit -m "docs: add phase 20a manual sandbox evidence capture pack for content_auto_skeleton"
```
