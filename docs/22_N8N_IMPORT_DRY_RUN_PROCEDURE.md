# Doc 22 — n8n Import Dry Run Procedure

**Created By:** Claude Code (Builder, AGT-02) — 2026-05-28
**Phase:** 10 — n8n Import Dry Run and Validation
**Status:** ACTIVE — use this document when importing Phase 8 skeletons into n8n

---

## What This Document Is

This document describes the step-by-step procedure for importing the 6 Phase 8 workflow skeleton JSON files into an n8n instance without activating them. This is a **dry run** — the goal is to confirm that all 6 skeletons import cleanly and render their node diagrams correctly. No workflow should be activated, no credential should be configured, and no execution should be triggered.

This procedure connects to:
- `docs/checklists/PHASE_9_N8N_IMPORT_CHECKLIST.md` — the per-workflow import checklist
- `logs/N8N_STATIC_VALIDATION_RUN_PHASE_10.md` — the static inspection results
- `logs/templates/N8N_IMPORT_VALIDATION_LOG_TEMPLATE.md` — the log template to fill after this session
- `logs/templates/N8N_IMPORT_ISSUE_TEMPLATE.md` — if any import fails or raises issues

---

## Scope and Hard Constraints

| Constraint | Detail |
|-----------|--------|
| No workflow activation | `active: false` must remain as-is. Do NOT click Activate. |
| No credential setup | Do not enter real API keys or tokens during this session. |
| No execution triggered | Do not click Execute Workflow or Test Workflow. |
| No production environment | Use a local n8n instance only. Not a production n8n server. |
| No auto-post | No social media, messaging, or ads integration during dry run. |
| Scope: import only | This procedure ends when all 6 workflows are imported and verified visible. |

---

## Pre-Conditions

Before starting the dry run, confirm all of the following:

| # | Pre-condition | How to Verify |
|---|--------------|---------------|
| P-01 | Node.js >= 16 installed | Run `node --version` — must return `v16.x` or higher |
| P-02 | Static validator passed | Run `node scripts/validate_n8n_workflows.mjs` — must exit 0 |
| P-03 | n8n instance running (local) | Open n8n in browser — must show the workflow list page |
| P-04 | n8n version noted | Settings → About — note the version for the import log |
| P-05 | 6 workflow JSON files present | Run `ls n8n/workflows/` — must show all 6 `.json` files |
| P-06 | No active production workflows | Check n8n workflow list — do not import near production workflows |
| P-07 | Import log template copied | Copy `logs/templates/N8N_IMPORT_VALIDATION_LOG_TEMPLATE.md` → `logs/N8N_IMPORT_LOG_PHASE_10_[DATE].md` |

If any pre-condition is not met, do not proceed. Log the blocker in the import log.

---

## Dry Run Procedure

### Step 1: Open n8n Workflow List

1. Start n8n (if not already running).
2. Open your browser and navigate to your local n8n URL (e.g., `http://localhost:5678`).
3. Confirm you see the Workflow list page.
4. Note the current workflow count for comparison after import.

### Step 2: Import Workflow 1 — Content Auto

1. Click **"+ New Workflow"** or use the Import button.
2. In the new workflow screen, click the **three-dot menu (⋮)** → **"Import from File"**.
3. Select: `n8n/workflows/content_auto_skeleton.json`
4. After import, verify:
   - Workflow name shows: `FnB OS V1 — Content Auto [SKELETON]`
   - Active toggle shows **OFF** (grey)
   - Sticky Note node visible in canvas with `## PHASE 8 SKELETON — DO NOT ACTIVATE`
   - Node count: 15 nodes visible
   - No error banner or red nodes
5. Do NOT activate. Do NOT execute.
6. Save the workflow (Ctrl+S or Save button).
7. Record result in import log.

### Step 3: Import Workflow 2 — Creative Asset Auto

1. Create a new workflow tab or go back to workflow list.
2. Import from file: `n8n/workflows/creative_asset_auto_skeleton.json`
3. After import, verify:
   - Workflow name: `FnB OS V1 — Creative Asset Auto [SKELETON]`
   - Active toggle: **OFF**
   - Sticky Note visible
   - Node count: 15 nodes
   - No errors
4. Do NOT activate. Do NOT execute.
5. Save.
6. Record result.

### Step 4: Import Workflow 3 — Ads Pack Auto

1. Import from file: `n8n/workflows/ads_pack_auto_skeleton.json`
2. After import, verify:
   - Workflow name: `FnB OS V1 — Ads Pack Auto [SKELETON]`
   - Active toggle: **OFF**
   - Sticky Note visible (orange color — high-risk warning)
   - Node count: 15 nodes
   - No errors
3. **STOP CHECK**: Confirm NO Meta Ads / TikTok Ads node types appear. All output nodes should be NoOp stubs.
4. Do NOT activate. Do NOT execute.
5. Save.
6. Record result.

### Step 5: Import Workflow 4 — CRM Follow-Up Auto

1. Import from file: `n8n/workflows/crm_followup_auto_skeleton.json`
2. After import, verify:
   - Workflow name: `FnB OS V1 — CRM Follow-Up Auto [SKELETON]`
   - Active toggle: **OFF**
   - Sticky Note visible (orange — high-risk warning)
   - Node count: 15 nodes
   - `Set: Draft Status + Human Review Flag` node visible
   - No errors
3. **STOP CHECK**: Confirm NO Zalo / Facebook Messenger / SMS node types. Only NoOp stub for queue.
4. Do NOT activate. Do NOT execute.
5. Save.
6. Record result.

### Step 6: Import Workflow 5 — Comment Inbox Reply Assistant

1. Import from file: `n8n/workflows/comment_inbox_reply_assistant_skeleton.json`
2. After import, verify:
   - Workflow name: `FnB OS V1 — Comment Inbox Reply Assistant [SKELETON]`
   - Active toggle: **OFF**
   - Sticky Note visible (orange — high-risk warning)
   - Node count: 13 nodes
   - `If: Escalation Required` node visible
   - Two branches visible: escalation path and draft path
   - No errors
3. **STOP CHECK**: Confirm NO Facebook / TikTok / Instagram / Zalo post/reply API nodes. Only NoOp stub for reply queue.
4. Do NOT activate. Do NOT execute.
5. Save.
6. Record result.

### Step 7: Import Workflow 6 — Approval and Publishing Gate

1. Import from file: `n8n/workflows/approval_publishing_skeleton.json`
2. After import, verify:
   - Workflow name: `FnB OS V1 — Approval and Publishing Gate [SKELETON]`
   - Active toggle: **OFF**
   - Sticky Note visible (blue — approval gate)
   - Node count: 18 nodes
   - `Webhook: Receive Approval Request` node shows placeholder path
   - `Switch: Item Type` node with 5 output branches
   - All 5 publish branches are NoOp stubs
   - `If: Is Approved` node visible
   - No errors
3. **STOP CHECK**: Confirm ALL publish nodes are NoOp stubs — no platform publish API nodes.
4. Do NOT activate. Do NOT execute.
5. Save.
6. Record result.

### Step 8: Post-Import Verification

After importing all 6 workflows:

1. Go to the n8n Workflow List page.
2. Confirm all 6 workflows appear:
   - `FnB OS V1 — Content Auto [SKELETON]`
   - `FnB OS V1 — Creative Asset Auto [SKELETON]`
   - `FnB OS V1 — Ads Pack Auto [SKELETON]`
   - `FnB OS V1 — CRM Follow-Up Auto [SKELETON]`
   - `FnB OS V1 — Comment Inbox Reply Assistant [SKELETON]`
   - `FnB OS V1 — Approval and Publishing Gate [SKELETON]`
3. Confirm all 6 show **Inactive** status.
4. Confirm no execution history exists for any of the 6 workflows.

### Step 9: Complete the Import Log

1. Open your copied import log file (`logs/N8N_IMPORT_LOG_PHASE_10_[DATE].md`).
2. Fill in all fields: n8n version, import results per workflow, STOP condition checks, overall result.
3. Answer the sign-off question: "Ready for Phase 11?"
4. Save the log file.

### Step 10: Record Issues (If Any)

If any workflow failed to import, showed errors, or triggered a STOP condition:

1. Copy `logs/templates/N8N_IMPORT_ISSUE_TEMPLATE.md` → `logs/N8N_IMPORT_ISSUE_[WORKFLOW]-[DATE].md`.
2. Fill in all fields for each issue.
3. Do not proceed to Phase 11 until all STOP conditions are resolved.

---

## STOP Conditions

Do not proceed past the dry run if any of the following are true:

| # | STOP Condition | Action |
|---|---------------|--------|
| S-01 | Any workflow failed to import | Log issue, investigate JSON syntax |
| S-02 | Any workflow shows `active: true` after import | Immediately deactivate, log issue |
| S-03 | Any workflow shows real credential (non-placeholder) | Do not save, log as security issue |
| S-04 | Any execution was triggered during import | Log incident, check execution history |
| S-05 | Any platform API node (Meta/TikTok/Zalo/FB/Telegram) visible that is not a NoOp stub | Log issue, do not activate |
| S-06 | Secret scan failed before import | Resolve before proceeding |

---

## What a PASS Looks Like

The dry run is complete and PASSES when:

- All 6 workflows imported without errors
- All 6 show `Inactive` status in the workflow list
- All 6 Sticky Note warnings are visible
- No execution history for any of the 6 workflows
- No STOP conditions triggered
- Import log filled and signed off
- Import checklist complete (all items checked)

---

## Known Limitations

1. This procedure validates import success only — it does not validate that Code node JavaScript would run correctly in production.
2. Webhook trigger in `approval_publishing_skeleton.json` requires path configuration before activation — not in scope for dry run.
3. Node typeVersion numbers may need adjustment for specific n8n instance versions — these show as warnings, not failures.
4. n8n may show "credential not found" warnings for nodes referencing `REPLACE_WITH_*` — these are expected and not errors for the dry run.
5. This procedure does not test inter-workflow data passing — that is a Phase 11+ concern.

---

## Phase Connections

| Phase | What It Produced | Relationship to This Doc |
|-------|-----------------|-------------------------|
| Phase 7 | n8n Runtime Blueprint | Defines what these workflows should do |
| Phase 8 | 6 workflow skeleton JSONs | The files imported by this procedure |
| Phase 9 | Static validator + import checklist | Pre-conditions for this procedure |
| Phase 10 | This procedure + validation run log | Current phase |
| Phase 11 | (Future) Credential wiring and workflow activation | Next step after dry run PASS |

---

*Phase 10 — n8n Import Dry Run and Validation*
*Builder: Claude Code (AGT-02) — 2026-05-28*
