# Doc 23 — n8n Import Dry-Run Checklist

**Created By:** Claude Code (Builder, AGT-02) — 2026-05-28
**Phase:** 11 — n8n Import Dry-Run Evidence Pack
**Status:** ACTIVE — use this checklist during the n8n import dry-run session

---

## Purpose

This is the human-readable quick-reference checklist for the Owner/Operator to follow during the actual n8n import dry-run session. It is not a full procedure — the full procedure is in `docs/22_N8N_IMPORT_DRY_RUN_PROCEDURE.md`. This checklist provides a concise pass/fail record to complete alongside the evidence log.

**Evidence log to fill in parallel:** `logs/N8N_IMPORT_DRY_RUN_EVIDENCE_PHASE_11.md`

---

## HARD RULES — Read Before Starting

These rules apply for the entire session. Violating any of them is a STOP condition.

| Rule | Detail |
|------|--------|
| **Import only** | Import workflow JSON files into n8n. Nothing else. |
| **Do NOT activate any workflow** | The Active toggle must remain OFF for all 6 workflows at all times. |
| **Do NOT connect real credentials** | All credential fields must remain empty or use placeholder text. |
| **Do NOT execute any workflow** | Do not click Execute, Test, or Run on any workflow. |
| **Do NOT test live customer-facing paths** | No comment replies, no CRM messages, no ad launches, no content publishing. |
| **Do NOT test posting to social platforms** | No Facebook, TikTok, Instagram, Zalo, YouTube actions. |
| **Do NOT test auto-reply** | No automated or manual reply sent through n8n to any real customer. |
| **Do NOT test ads** | No Meta Ads, TikTok Ads, or any paid channel interaction through n8n. |
| **Record all evidence** | Every check must be recorded in `logs/N8N_IMPORT_DRY_RUN_EVIDENCE_PHASE_11.md`. |
| **Use local instance only** | Do not import into a production n8n instance. |

---

## Section A — Before You Start

Complete all items before touching n8n.

| # | Item | Done? |
|---|------|-------|
| A-01 | I have read `docs/22_N8N_IMPORT_DRY_RUN_PROCEDURE.md` in full | [ ] |
| A-02 | I have read this checklist in full | [ ] |
| A-03 | I have opened `logs/N8N_IMPORT_DRY_RUN_EVIDENCE_PHASE_11.md` and will fill it as I go | [ ] |
| A-04 | Node.js >= 16 is installed (`node --version` returns a valid version) | [ ] |
| A-05 | Static validator has been run: `node scripts/validate_n8n_workflows.mjs` — exit 0 | [ ] |
| A-06 | n8n is running on a **local** instance (not production) | [ ] |
| A-07 | I know the n8n version (Settings → About) and have noted it in the evidence log | [ ] |
| A-08 | All 6 workflow JSON files are present in `n8n/workflows/` | [ ] |
| A-09 | I will NOT enter any real API key, token, or password at any point in this session | [ ] |
| A-10 | I have noted the current number of workflows in n8n before importing | [ ] |

> **If A-04, A-05, A-06, or A-09 cannot be checked: STOP. Do not proceed.**

---

## Section B — Workflow 1: Content Auto

Import `n8n/workflows/content_auto_skeleton.json`

| # | Check | Done? |
|---|-------|-------|
| B-01 | File imported successfully — no error banner | [ ] |
| B-02 | Workflow name shows: `FnB OS V1 — Content Auto [SKELETON]` | [ ] |
| B-03 | Active toggle is **OFF** | [ ] |
| B-04 | Sticky Note node is visible with `DO NOT ACTIVATE` warning | [ ] |
| B-05 | No execution was triggered | [ ] |
| B-06 | No real credential was entered | [ ] |
| B-07 | Workflow saved | [ ] |
| B-08 | Result recorded in evidence log (Section 6, WF-01) | [ ] |

---

## Section C — Workflow 2: Creative Asset Auto

Import `n8n/workflows/creative_asset_auto_skeleton.json`

| # | Check | Done? |
|---|-------|-------|
| C-01 | File imported successfully — no error banner | [ ] |
| C-02 | Workflow name shows: `FnB OS V1 — Creative Asset Auto [SKELETON]` | [ ] |
| C-03 | Active toggle is **OFF** | [ ] |
| C-04 | Sticky Note node is visible with `DO NOT ACTIVATE` warning | [ ] |
| C-05 | No execution was triggered | [ ] |
| C-06 | No real credential was entered | [ ] |
| C-07 | Workflow saved | [ ] |
| C-08 | Result recorded in evidence log (Section 6, WF-02) | [ ] |

---

## Section D — Workflow 3: Ads Pack Auto

> **HIGH-RISK — Ads spend possible in production. Extra checks required.**

Import `n8n/workflows/ads_pack_auto_skeleton.json`

| # | Check | Done? |
|---|-------|-------|
| D-01 | File imported successfully — no error banner | [ ] |
| D-02 | Workflow name shows: `FnB OS V1 — Ads Pack Auto [SKELETON]` | [ ] |
| D-03 | Active toggle is **OFF** | [ ] |
| D-04 | Sticky Note node visible — orange warning color | [ ] |
| D-05 | **No Meta Ads / TikTok Ads / Zalo Ads API node is visible** | [ ] |
| D-06 | All output/publish nodes are NoOp stubs | [ ] |
| D-07 | No execution was triggered | [ ] |
| D-08 | No real credential was entered | [ ] |
| D-09 | **No ads budget was committed at any point** | [ ] |
| D-10 | Workflow saved | [ ] |
| D-11 | Result recorded in evidence log (Section 6, WF-03) | [ ] |

---

## Section E — Workflow 4: CRM Follow-Up Auto

> **HIGH-RISK — Customer messages possible in production. Extra checks required.**

Import `n8n/workflows/crm_followup_auto_skeleton.json`

| # | Check | Done? |
|---|-------|-------|
| E-01 | File imported successfully — no error banner | [ ] |
| E-02 | Workflow name shows: `FnB OS V1 — CRM Follow-Up Auto [SKELETON]` | [ ] |
| E-03 | Active toggle is **OFF** | [ ] |
| E-04 | Sticky Note node visible — orange warning color | [ ] |
| E-05 | `Set: Draft Status + Human Review Flag` node is visible | [ ] |
| E-06 | **No Zalo / Facebook Messenger / SMS API node is visible** | [ ] |
| E-07 | Approval queue node is a NoOp stub | [ ] |
| E-08 | No execution was triggered | [ ] |
| E-09 | No real credential was entered | [ ] |
| E-10 | **No message was sent to any real customer** | [ ] |
| E-11 | Workflow saved | [ ] |
| E-12 | Result recorded in evidence log (Section 6, WF-04) | [ ] |

---

## Section F — Workflow 5: Comment Inbox Reply Assistant

> **HIGH-RISK — Auto-reply to real customers possible in production. Extra checks required.**

Import `n8n/workflows/comment_inbox_reply_assistant_skeleton.json`

| # | Check | Done? |
|---|-------|-------|
| F-01 | File imported successfully — no error banner | [ ] |
| F-02 | Workflow name shows: `FnB OS V1 — Comment Inbox Reply Assistant [SKELETON]` | [ ] |
| F-03 | Active toggle is **OFF** | [ ] |
| F-04 | Sticky Note node visible — orange warning color | [ ] |
| F-05 | `If: Escalation Required` node is visible | [ ] |
| F-06 | Two branches visible (escalation path + draft path) | [ ] |
| F-07 | **No Facebook / TikTok / Instagram / Zalo comment-reply API node visible** | [ ] |
| F-08 | Reply queue node is a NoOp stub | [ ] |
| F-09 | No execution was triggered | [ ] |
| F-10 | No real credential was entered | [ ] |
| F-11 | **No auto-reply was sent to any real customer** | [ ] |
| F-12 | Workflow saved | [ ] |
| F-13 | Result recorded in evidence log (Section 6, WF-05) | [ ] |

---

## Section G — Workflow 6: Approval and Publishing Gate

> **GATE WORKFLOW — Controls all publishing. Most critical to verify as skeleton.**

Import `n8n/workflows/approval_publishing_skeleton.json`

| # | Check | Done? |
|---|-------|-------|
| G-01 | File imported successfully — no error banner | [ ] |
| G-02 | Workflow name shows: `FnB OS V1 — Approval and Publishing Gate [SKELETON]` | [ ] |
| G-03 | Active toggle is **OFF** | [ ] |
| G-04 | Sticky Note node visible — blue approval gate color | [ ] |
| G-05 | Webhook trigger shows placeholder path (not a live endpoint) | [ ] |
| G-06 | `Switch: Item Type` node with 5 output branches is visible | [ ] |
| G-07 | **All 5 publish branches are NoOp stubs** (not real platform nodes) | [ ] |
| G-08 | `If: Is Approved` routing node is visible | [ ] |
| G-09 | Not-approved path leads to `Stop and Error` | [ ] |
| G-10 | **No platform publish API node visible** (no FB/TikTok/Zalo/Meta publish node) | [ ] |
| G-11 | No execution was triggered | [ ] |
| G-12 | No real credential was entered | [ ] |
| G-13 | **No content was published to any platform** | [ ] |
| G-14 | **No ads budget was committed** | [ ] |
| G-15 | Workflow saved | [ ] |
| G-16 | Result recorded in evidence log (Section 6, WF-06) | [ ] |

---

## Section H — Post-Import Verification

Complete after all 6 workflows are imported and saved.

| # | Check | Done? |
|---|-------|-------|
| H-01 | All 6 workflows appear in n8n workflow list | [ ] |
| H-02 | All 6 show **Inactive** status in the list view | [ ] |
| H-03 | No execution history exists for any of the 6 workflows | [ ] |
| H-04 | Total workflow count in n8n increased by exactly 6 | [ ] |
| H-05 | Evidence log Section 7 (Post-Import Checklist) filled | [ ] |
| H-06 | Evidence log Section 8 (Safety Confirmation) signed | [ ] |
| H-07 | Evidence log Section 9 (Issue Summary) filled (NONE if clean) | [ ] |
| H-08 | Evidence log Section 10 (Final Result) updated from NOT_RUN to PASS or BLOCKED | [ ] |

---

## Section I — Sign-Off

| Field | Value |
|-------|-------|
| Operator name | [FILL] |
| Date | [FILL: YYYY-MM-DD] |
| All sections A–H completed | [FILL: YES / NO] |
| Evidence log filled and saved | [FILL: YES / NO] |
| Any issues logged in issue template | [FILL: YES — count: X / NO — NONE] |
| Ready for Phase 12 | [FILL: YES / NO / PENDING ISSUE RESOLUTION] |

---

## Distinction From Phase 10 Procedure

| | Phase 10 (`docs/22_N8N_IMPORT_DRY_RUN_PROCEDURE.md`) | Phase 11 (this document) |
|--|-----------------------------------------------------|--------------------------|
| **Type** | Full step-by-step import procedure | Quick-reference checklist |
| **Purpose** | Tell you HOW to import (each step, click-by-click) | Provide pass/fail record as you go |
| **Use** | Read before and during the session | Fill checkboxes during the session |
| **Evidence** | References evidence log | Directs to fill evidence log |
| **Audience** | Someone doing this for the first time | Someone moving quickly through the session |

Use both documents together. Do not use this checklist as a replacement for the procedure.

---

*Phase 11 — n8n Import Dry-Run Evidence Pack*
*Builder: Claude Code (AGT-02) — 2026-05-28*
