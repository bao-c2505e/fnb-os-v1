# docs/21 — n8n Import Validation Guide

Phase: 9 — n8n Import Validation Pack
Created By: Claude Code (Builder, AGT-02) — 2026-05-28
Status: PHASE_9_BUILDER_DONE

---

## What This Document Covers

Phase 9 defines how to validate the Phase 8 n8n workflow skeleton files before any production use.
Validation has two layers:

| Layer | Who Runs It | Tool | When |
|-------|-------------|------|------|
| Static structural check | Builder / Codex | `scripts/validate_n8n_workflows.mjs` | Before any import |
| Manual import check | Owner | `docs/checklists/PHASE_9_N8N_IMPORT_CHECKLIST.md` | In n8n UI after import |

Neither layer executes workflows, connects to external services, or touches credentials.

---

## Phase 9 Files

| File | Purpose |
|------|---------|
| `docs/21_N8N_IMPORT_VALIDATION.md` | This document |
| `docs/checklists/PHASE_9_N8N_IMPORT_CHECKLIST.md` | Manual import checklist for Owner |
| `scripts/validate_n8n_workflows.mjs` | Static validator (Node.js ESM, read-only) |
| `logs/templates/N8N_IMPORT_VALIDATION_LOG_TEMPLATE.md` | Log template for recording import results |
| `handoff/PHASE_9_HANDOFF.md` | Handoff + Codex review instructions |

---

## Workflows to Validate

| File | Workflow Name | Nodes | Risk Level |
|------|--------------|-------|------------|
| `n8n/workflows/content_auto_skeleton.json` | FnB OS V1 — Content Auto [SKELETON] | 15 | LOW |
| `n8n/workflows/creative_asset_auto_skeleton.json` | FnB OS V1 — Creative Asset Auto [SKELETON] | 15 | LOW |
| `n8n/workflows/ads_pack_auto_skeleton.json` | FnB OS V1 — Ads Pack Auto [SKELETON] | 15 | MEDIUM (ads budget gate) |
| `n8n/workflows/crm_followup_auto_skeleton.json` | FnB OS V1 — CRM Followup Auto [SKELETON] | 15 | MEDIUM (messaging gate) |
| `n8n/workflows/comment_inbox_reply_assistant_skeleton.json` | FnB OS V1 — Comment Inbox Reply Assistant [SKELETON] | 13 | MEDIUM (reply gate) |
| `n8n/workflows/approval_publishing_skeleton.json` | FnB OS V1 — Approval & Publishing [SKELETON] | 17 | HIGH (publishing gate) |

All workflows have `active: false`. None will run automatically after import.

---

## Static Validation Script

**File:** `scripts/validate_n8n_workflows.mjs`
**Type:** Node.js ESM — read-only static analysis
**Requires:** Node.js >= 16
**Does NOT:** execute workflows, call external services, read credentials, write files

### What the script checks per workflow

| Check | Pass Condition |
|-------|---------------|
| File exists | File present at expected path |
| Valid JSON | `JSON.parse()` succeeds |
| `active: false` | `workflow.active === false` |
| Workflow has name | `name` field is non-empty string |
| Name contains `[SKELETON]` | Name string includes `[SKELETON]` |
| Has nodes array (non-empty) | `nodes` is non-empty array |
| Has node: Error Trigger | Node of type `n8n-nodes-base.errorTrigger` present |
| Has node: Sticky Note (safety warning) | Node of type `n8n-nodes-base.stickyNote` present |
| No secret: Anthropic API key | No `sk-ant-` pattern in file content |
| No secret: Generic API key | No `sk-` key pattern in file content |
| No secret: Private key | No `BEGIN PRIVATE KEY` block in file content |
| No secret: GitHub PAT | No `ghp_` pattern in file content |
| No secret: JWT token | No `eyJhbGciOi` JWT pattern in file content |
| No secret: Hardcoded password | No `password:` with value pattern |
| No secret: Telegram bot token | No Telegram token pattern in file content |
| `versionId` uses placeholder | `versionId` starts with `REPLACE_WITH` |
| `instanceId` uses placeholder | `instanceId` starts with `REPLACE_WITH` |

### How to run

```
node scripts/validate_n8n_workflows.mjs
```

Run from the repo root (`D:\FNB_OS_V1` or equivalent).

**Prerequisites:**
- Node.js >= 16 installed (`node --version` to check)
- Phase 8 workflow files present at `n8n/workflows/*.json`
- Do NOT run in production n8n instance — this is a local repo check only

**Output:** Console report with PASS/FAIL per check. Exit code 0 = all pass. Exit code 1 = failures found.

**If script fails (Node.js not available):** Perform the same checks manually using the import checklist.
The script is a convenience tool — the checklist is the authoritative manual fallback.

---

## Manual Import Validation (Owner)

After confirming static checks pass, the Owner imports each skeleton into n8n manually.

Full steps: `docs/checklists/PHASE_9_N8N_IMPORT_CHECKLIST.md`

**Critical rule: Importing a skeleton is read-only.** n8n creates a local copy of the workflow.
The skeleton JSON file in the repo is not modified. The workflow remains inactive after import.

### n8n Import Steps (summary)

1. Open n8n (local or cloud instance)
2. Go to Workflows → New → Import from file
3. Select one `.json` file from `n8n/workflows/`
4. Verify import preview shows correct name and node count
5. Click Import
6. In the workflow canvas, verify:
   - `active` toggle is OFF
   - All nodes are visible and connected
   - Sticky Note warning is visible
   - No credentials have been auto-filled (all show "credential required")
7. Do NOT activate the workflow
8. Record result in `logs/templates/N8N_IMPORT_VALIDATION_LOG_TEMPLATE.md`

---

## What PASS Means at Phase 9

| Gate | Pass Condition |
|------|---------------|
| Static validator | All 6 workflows: all checks PASS |
| Manual import | All 6 workflows import without n8n errors |
| Canvas verification | All 6 workflows: active=OFF, Sticky Note visible, credentials empty |
| Log recorded | Owner has filled in import log with results |

Phase 9 does NOT require:
- Filling real credentials
- Activating any workflow
- Running any workflow execution
- Connecting to any external service

---

## What Is NOT Validated in Phase 9

| Item | Phase |
|------|-------|
| Real AI API call working | Phase 10+ |
| Google Sheets credential configured | Phase 10+ |
| Telegram notification working | Phase 10+ |
| Webhook URL configured | Phase 10+ |
| Approval queue sheet connected | Phase 10+ |
| End-to-end execution test | Phase 10+ |

---

## Guardrails

- Do not fill real credentials during Phase 9 import validation.
- Do not activate any workflow during Phase 9.
- Do not run any workflow execution during Phase 9.
- Do not connect workflows to production social media accounts.
- Do not run paid ads.
- Do not auto-post or auto-reply.
- The validation script is static and safe — it does not execute any workflow code.

---

## Connection to Phase 8

Phase 8 produced the 6 skeleton JSON files. Phase 9 validates that they are structurally correct and safely importable. Phase 10+ will wire credentials and test execution.

| Phase | Output |
|-------|--------|
| Phase 8 | 6 n8n skeleton workflow JSONs + docs/20 |
| Phase 9 | Import validation pack (this file + checklist + script + log template) |
| Phase 10+ | Credential configuration + end-to-end execution test |
