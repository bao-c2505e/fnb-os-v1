# Phase 20B Handoff

**Phase:** 20B — Owner Manual Sandbox Runbook: content_auto_skeleton
**Created By:** Claude Code (Builder, AGT-02) — 2026-05-29
**Status:** RUNBOOK_READY — AWAITING OWNER EXECUTION

---

## Phase Summary

Phase 20B creates the Owner-facing step-by-step runbook for the first actual manual sandbox execution of `content_auto_skeleton`. It also creates the `evidence/phase_20b/content_auto_skeleton/` folder placeholder and updates the Phase 20A evidence log with the runbook reference and evidence folder path.

Phase 20B is **documentation only** from the Builder's perspective. No workflow was executed by Builder. The Owner executes independently using the runbook.

---

## Phase Distinction

| Phase | Type | What it produces |
|-------|------|-----------------|
| Phase 20A | Evidence Pack | Pre-run checklist, blank evidence log template, PASS/BLOCKED criteria |
| Phase 20B | Runbook | Exact 12-step Owner execution guide, stop conditions, evidence requirements |
| Phase 20C | Evidence Submission | Owner submits filled log → Builder commits → Codex reviews |

---

## Selected Workflow

| Field | Value |
|-------|-------|
| Workflow file | `n8n/workflows/content_auto_skeleton.json` |
| n8n name | FnB OS V1 — Content Auto [SKELETON] |
| Risk level | Standard |
| Trigger | Manual Trigger (not webhook) |

---

## Files Created

| File | Status |
|------|--------|
| `docs/33_PHASE_20B_OWNER_MANUAL_SANDBOX_RUNBOOK_CONTENT_AUTO.md` | Created |
| `evidence/phase_20b/content_auto_skeleton/.gitkeep` | Created (folder placeholder) |
| `handoff/PHASE_20B_HANDOFF.md` | Created (this file) |

## Files Updated

| File | Change |
|------|--------|
| `logs/phase_20a_content_auto_sandbox_evidence_log.md` | Runbook reference + evidence folder path added; `execution_status` remains `not_executed_yet` |
| `handoff/CURRENT_PHASE.md` | Updated to Phase 20B RUNBOOK_READY |
| `handoff/SESSION_SUMMARY.md` | Phase 20B session prepended |
| `logs/AGENT_ACTIVITY_LOG.md` | Phase 20B activity row prepended |
| `09_LOGS/PHASE_LOG.md` | Phase 20B entry prepended |

## Files Not Modified

| File | Reason |
|------|--------|
| `n8n/workflows/content_auto_skeleton.json` | Phase 20B is docs only — no workflow JSON changes |
| `n8n/workflows/creative_asset_auto_skeleton.json` | Out of Phase 20B scope |
| `n8n/workflows/ads_pack_auto_skeleton.json` | Out of Phase 20B scope |
| `n8n/workflows/crm_followup_auto_skeleton.json` | Out of Phase 20B scope |
| `n8n/workflows/comment_inbox_reply_assistant_skeleton.json` | Out of Phase 20B scope |
| `n8n/workflows/approval_publishing_skeleton.json` | Out of Phase 20B scope |

---

## Runbook Summary

`docs/33_PHASE_20B_OWNER_MANUAL_SANDBOX_RUNBOOK_CONTENT_AUTO.md` contains:

| Section | Content |
|---------|---------|
| A — Purpose | Phase 20B is first actual manual sandbox execution; Owner executes independently |
| B — Selected Workflow | File, n8n name, risk, trigger, payload, evidence log, evidence folder |
| C — Required Pre-Run State | PRE-01–PRE-10 checklist + Owner sign-off block |
| D — Exact n8n UI Steps | 12 steps: open n8n → confirm inactive → no credentials → no activation → locate trigger → confirm payload (no modification needed) → run once → observe per-node output table → screenshot evidence → fill evidence log → stop-and-record if any failure |
| E — Stop Conditions | 8 explicit stop conditions with BLOCKED action |
| F — Evidence Requirements | 11 required fields in evidence log |
| G — Screenshot Naming Convention | Full path + 4 token definitions + 4 examples |
| H — Log File to Update | Path + note that commit happens in Phase 20C not 20B |
| I — Pass Criteria | 11-item checklist |
| J — Fail Criteria | 10 BLOCKED/INCOMPLETE triggers |
| K — Explicit Non-Goals | 10 non-goals |
| L — Next Phase | Phase 20C — Owner Evidence Submission and Codex Review |
| Phase Connections | Phase 8 through Phase 20C |
| Safety Confirmation | 8 items all NO/CLEAN |

---

## Evidence Log Update Summary

`logs/phase_20a_content_auto_sandbox_evidence_log.md` updated:
- Header now references Phase 20B runbook
- `Phase 20B Runbook:` field added pointing to `docs/33_PHASE_20B_OWNER_MANUAL_SANDBOX_RUNBOOK_CONTENT_AUTO.md`
- `Evidence Folder:` field added: `evidence/phase_20b/content_auto_skeleton/`
- `Screenshot Convention:` field added with full path template
- `execution_status` remains `not_executed_yet` — no execution claimed

---

## Safety Constraints

| Constraint | Status |
|-----------|--------|
| Workflow remains inactive / active=false | ENFORCED — runbook explicitly forbids activation |
| Dummy payload only | ENFORCED — Phase 17 P17-WF01-S1 referenced; no modifications required |
| No real customer data | ENFORCED — stop condition explicitly listed |
| No API key / token / password / private key | ENFORCED — stop condition explicitly listed |
| No production publishing | ENFORCED — stop condition and non-goals |
| No real customer messaging | ENFORCED — stop condition and non-goals |
| No ads spend | ENFORCED — stop condition and non-goals |
| Screenshot is evidence only, not log replacement | ENFORCED — Section F evidence requirements |
| Owner does not debug inside n8n | ENFORCED — Step 12 stop-and-record instruction |
| No execution performed by Builder | CONFIRMED — Owner executes independently |

---

## No-Execution Confirmation

| Item | Status |
|------|--------|
| n8n workflow executed by Builder | NO |
| n8n accessed by Builder | NO |
| Workflow activated | NO |
| Real credentials added | NO |
| Phase 8 workflow JSON modified | NO |
| Real customer data used | NO |
| Auto-post / auto-reply / ads triggered | NO |
| `active: true` introduced | NO |
| Production readiness claimed | NO |
| `execution_status` changed from `not_executed_yet` | NO — unchanged |

---

## Owner Next Action

1. Read `docs/33_PHASE_20B_OWNER_MANUAL_SANDBOX_RUNBOOK_CONTENT_AUTO.md` fully.
2. Confirm PRE-01 through PRE-10 in Section C.
3. Sign the Pre-Run Sign-Off block.
4. Follow Steps 1–12 in Section D.
5. Complete the evidence log `logs/phase_20a_content_auto_sandbox_evidence_log.md`.
6. Report result (PASS or BLOCKED) to Builder for Phase 20C.

---

## Next Recommended Phase

**Phase 20C — Owner Evidence Submission and Codex Review for content_auto_skeleton**

Scope: Owner submits the filled evidence log. Builder commits the log to the repo. Codex reviews to confirm Phase 20B was executed safely and evidence is complete.

Entry criteria:
- Phase 20B execution completed (PASS or BLOCKED)
- `logs/phase_20a_content_auto_sandbox_evidence_log.md` filled with actual results
- `execution_status` updated from `not_executed_yet`
- Owner Sign-Off present in evidence log

---

## Acceptance Criteria

| Criterion | Status |
|-----------|--------|
| Phase 20B runbook created (docs/33) | PASS |
| Evidence folder placeholder created | PASS |
| Evidence log updated with runbook reference | PASS |
| Evidence log `execution_status` remains `not_executed_yet` | PASS |
| Handoff created | PASS |
| CURRENT_PHASE.md updated | PASS |
| SESSION_SUMMARY.md updated | PASS |
| AGENT_ACTIVITY_LOG.md updated | PASS |
| PHASE_LOG.md updated | PASS |
| All 6 workflow JSONs untouched | PASS |
| `active: true` not introduced | PASS |
| No real credentials added | PASS |
| No real customer data added | PASS |
| No workflow execution performed | PASS |
| No production readiness claimed | PASS |
| Runbook has 12 UI steps | PASS |
| Runbook has 8 stop conditions | PASS |
| Screenshot naming convention defined | PASS |
| Pass/fail criteria defined | PASS |
| Explicit non-goals (10 items) present | PASS |
| Phase 20C recommendation present | PASS |
| Secret scan CLEAN | PASS |

---

## Secret Scan

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

1. Does `docs/33_PHASE_20B_OWNER_MANUAL_SANDBOX_RUNBOOK_CONTENT_AUTO.md` provide a clear, safe, step-by-step Owner execution guide that cannot be misread as authorising activation, real credentials, or production use?
2. Does Step 12 unambiguously tell Owner to stop and record (not fix) when any node fails?
3. Does Section E list all critical stop conditions including real credential prompt, active toggle, and unexpected external API call?
4. Does `logs/phase_20a_content_auto_sandbox_evidence_log.md` correctly show `execution_status: not_executed_yet` (no execution claimed)?
5. Is `evidence/phase_20b/content_auto_skeleton/.gitkeep` present and the folder path consistent with screenshot naming convention in the runbook?
6. Confirm: no `active: true` introduced, no real credentials present, no workflow JSON modified, secret scan CLEAN.

Output: **PASS** / **PASS WITH NOTES** / **FAIL**

---

## Commit Instruction (after Codex PASS + Owner OWNER_APPROVED)

```
git add docs/33_PHASE_20B_OWNER_MANUAL_SANDBOX_RUNBOOK_CONTENT_AUTO.md
git add evidence/phase_20b/content_auto_skeleton/.gitkeep
git add logs/phase_20a_content_auto_sandbox_evidence_log.md
git add handoff/PHASE_20B_HANDOFF.md
git add handoff/CURRENT_PHASE.md
git add handoff/SESSION_SUMMARY.md
git add logs/AGENT_ACTIVITY_LOG.md
git add 09_LOGS/PHASE_LOG.md
git commit -m "docs: add phase 20b owner manual sandbox runbook for content_auto_skeleton"
```
