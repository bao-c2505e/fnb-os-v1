# Phase 32 — Creative Asset Auto Sandbox Re-import Only

Created By: Claude Code (Builder, AGT-02) — 2026-06-03
Phase: 32 — Creative Asset Auto Sandbox Re-import Only
Type: INSTRUCTIONS — OWNER ACTION REQUIRED
Branch: main

---

## 1. Purpose

Phase 32 provides Owner instructions to re-import the patched `creative_asset_auto_skeleton.json` into n8n sandbox.

The workflow file was patched in Phase 30 (commit `18c681d`) to add 19 safe sample input fields to the `Set Input Variables` node. That patch has been committed and pushed to GitHub. The n8n sandbox still contains the pre-patch version from the Phase 26 import. Phase 32 re-imports the patched version so the sandbox is in sync with the repo.

**Phase 32 scope is re-import only.**
- No workflow execution in Phase 32.
- No activation in Phase 32.
- No credentials in Phase 32.
- No API calls in Phase 32.
- No production side effect in Phase 32.
- No workflow JSON change in Phase 32.

Phase 33 (manual execution check) follows after Phase 32 is confirmed complete.

---

## 2. Scope

| Item | Phase 32 Scope |
|------|---------------|
| Workflow JSON change | OUT OF SCOPE |
| n8n re-import (Owner manual) | IN SCOPE |
| n8n execution | OUT OF SCOPE |
| Activate workflow | OUT OF SCOPE |
| Attach real credentials | OUT OF SCOPE |
| Real API calls | OUT OF SCOPE |
| Auto-post / auto-reply | OUT OF SCOPE |
| Ads spend | OUT OF SCOPE |
| Production side effect | OUT OF SCOPE |

---

## 3. Workflow File

| Item | Value |
|------|-------|
| Repo path | `n8n/workflows/creative_asset_auto_skeleton.json` |
| n8n workflow name | `FnB OS V1 — Creative Asset Auto [SKELETON]` |
| n8n workflow ID | `VW5PDkOOtrjLQBps` |
| `active` field | `false` — must remain false |
| Node count (JSON) | 15 (14 execution + 1 Sticky Note) |
| Phase 30 patch | Set Input Variables: 7 → 19 fields |
| Latest commit with patch | `18c681d` (Phase 30) |

---

## 4. Owner Re-import Steps

Before starting, confirm you have the latest version of the repo locally:

```
git status
git log --oneline -3
```

Expected output:
- Branch: `main`
- HEAD at or after `18c681d`
- Working tree clean

### Step-by-Step Re-import

**Step 1.** Open n8n sandbox in your browser.

**Step 2.** Navigate to the workflow named `FnB OS V1 — Creative Asset Auto [SKELETON]` (ID: `VW5PDkOOtrjLQBps`).

**Step 3.** Confirm the workflow is currently **inactive** (toggle is OFF / grey). Do NOT proceed if the workflow is active.

**Step 4.** To import the updated workflow:
- In n8n, go to the workflow canvas for `FnB OS V1 — Creative Asset Auto [SKELETON]`.
- Use the n8n menu: **...** (three dots) → **Import from File**, or use the main menu **Workflows** → **Import**.
- Select the file: `n8n/workflows/creative_asset_auto_skeleton.json` from your local repo at `D:\FNB_OS_V1\`.

**Step 5.** If n8n asks whether to **replace / overwrite** the existing workflow, choose **replace / overwrite**. This ensures the sandbox uses the new patched version from the repo.

**Step 6.** After import, verify:
- Workflow name is still `FnB OS V1 — Creative Asset Auto [SKELETON]`.
- Workflow is **inactive** (active toggle is OFF).
- Canvas shows nodes — count approximately 10–15 visible nodes.

**Step 7.** Click on the **Set Input Variables** node. In the node parameters, confirm you can see the 19 fields, including:
- `brand_id` = `VQ`
- `brand_name` = `Vi Cuon`
- `request_id` = `creative_asset_sandbox_001`
- `approval_required` = `true` (boolean)
- `sandbox_mode` = `true` (boolean)

**Step 8.** Do **NOT** click Execute.

**Step 9.** Do **NOT** click Activate.

**Step 10.** Do **NOT** attach any credentials.

**Step 11.** Do **NOT** publish the workflow.

**Step 12.** Record the re-import result in the checklist below (Section 5).

---

## 5. Re-import Evidence Checklist

Owner records after completing Phase 32 re-import:

| Item | Expected | Owner Result |
|------|----------|-------------|
| Workflow name after import | `FnB OS V1 — Creative Asset Auto [SKELETON]` | [OWNER TO FILL] |
| Re-import completed | YES | [OWNER TO FILL] |
| Workflow active status after import | inactive (OFF) | [OWNER TO FILL] |
| Manual execution performed | NO | [OWNER TO FILL] |
| Credentials attached | NO | [OWNER TO FILL] |
| API calls observed during import | NO | [OWNER TO FILL] |
| Workflow canvas opened successfully | YES | [OWNER TO FILL] |
| Nodes visible on canvas | YES — approx 10–15 | [OWNER TO FILL — count: __] |
| Set Input Variables node shows 19 fields | YES | [OWNER TO FILL] |
| `brand_name` shows `Vi Cuon` | YES | [OWNER TO FILL] |
| `approval_required` shows boolean `true` | YES | [OWNER TO FILL] |
| `sandbox_mode` shows boolean `true` | YES | [OWNER TO FILL] |
| Ready for Phase 33 manual execution check | YES | [OWNER TO FILL] |

---

## 6. What NOT To Do in Phase 32

| Forbidden Action | Reason |
|-----------------|--------|
| Execute the workflow | Phase 33 only — after re-import confirmed |
| Test any node output | Phase 33 only |
| Attach any real credential | Not authorized in Phase 32 or Phase 33 (sandbox uses stub credentials only) |
| Set workflow to active | Never — `active: false` is a hard constraint for all skeleton workflows |
| Publish the workflow | Never in sandbox phase |
| Edit workflow directly in n8n UI and treat as source of truth | n8n UI is NOT source of truth — repo file `n8n/workflows/creative_asset_auto_skeleton.json` is source of truth |
| If you notice any UI change is needed, make it in the repo JSON file | Stop, record the change needed, report to Architect — do not modify n8n UI directly and call it done |

---

## 7. Expected Result After Phase 32

After Phase 32 completes, the n8n sandbox will contain:
- `FnB OS V1 — Creative Asset Auto [SKELETON]` — re-imported from `18c681d` patch version
- `Set Input Variables` node showing 19 fields with safe sample values
- Workflow inactive
- No execution performed
- No credentials attached
- Sandbox ready for Phase 33 manual execution check

The Phase 27 execution note ("No fields - item(s) exist, but they're empty" on Set Input Variables) should be resolved after re-import — the 19 fields should now be visible when opening the Set Input Variables node.

---

## 8. Safety Checklist

| Check | Status |
|-------|--------|
| Workflow JSON changed in Phase 32 | NO |
| `active=true` introduced | NO |
| Secrets added | NO |
| Real credentials added | NO |
| Real API calls added | NO |
| n8n import executed by Claude (Builder) | NO — Owner manual only |
| n8n execution performed in Phase 32 | NO |
| Auto-post / auto-reply | NO |
| Ads spend | NO |
| Production side effect risk | NO |
| Builder (Claude Code) has n8n UI access | NO — Owner performs import |

---

## 9. Recommended Phase 33

**Phase 33 — Creative Asset Auto Sandbox Manual Execution Check**

After Phase 32 re-import is confirmed:

**Phase 33 Objectives:**
1. Owner executes the workflow manually in n8n sandbox (Manual Trigger, once).
2. Open the `Set Input Variables` node output panel.
3. Confirm all 19 fields are visible with expected values (no "empty" message).
4. Confirm happy-path runs to completion: `approval_status = Draft`, `logWritten = true`, `approvalQueueStubReached = true`.
5. Confirm no forbidden output: no real API call, no auto-post, no real credential, workflow remains inactive.
6. Record evidence per Phase 27 evidence log pattern.

**Phase 33 Entry Criteria:**
- Phase 32 re-import confirmed by Owner (checklist in Section 5 complete).
- Phase 32 evidence committed and pushed.
- Owner issues Phase 33 approval phrase before execution.

---

## 10. Phase Connections

| Phase | Description | Status |
|-------|-------------|--------|
| Phase 8 | n8n Workflow Skeleton Build | DONE + PUSHED |
| Phase 26 | First Sandbox Import | DONE + PUSHED |
| Phase 27 | Sandbox Manual Execution — PASS WITH NOTES | DONE + PUSHED |
| Phase 28 | Sandbox I/O Standardization | DONE + PUSHED |
| Phase 29 | Safe Sample Input Patch Planning | DONE + PUSHED |
| Phase 30 | Safe Sample Input Patch Implementation | DONE + PUSHED (commit `18c681d`) |
| Phase 31 | Sandbox Re-import & Manual Execution Planning | DONE + PUSHED (commit `d6570f0`) |
| **Phase 32** | **Sandbox Re-import Only (this phase)** | **INSTRUCTIONS READY — OWNER ACTION REQUIRED** |
| Phase 33 (TBD) | Manual Execution Check — verify 19-field output | NOT STARTED |

---

## 11. Safety Confirmation

| Item | Status |
|------|--------|
| Workflow JSON modified in Phase 32 | NO |
| `active = true` introduced | NO |
| Real credentials added | NO |
| Real API calls added | NO |
| Auto-post / auto-reply / ad spend | NO |
| Production system modified | NO |
| Real customer data added | NO |
| n8n workflow imported by Builder (Claude Code) | NO |
| n8n workflow executed by Builder (Claude Code) | NO |
| n8n import planned for Owner manual action | YES — Section 4 |
| Secret scan (new files) | CLEAN |
| Scope creep | NO — instructions/docs only |
