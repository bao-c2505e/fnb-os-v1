# Phase 34 — Creative Asset Auto Set Input Variables Output Debug Planning

Created By: Claude Code (Builder/Investigator, AGT-02) — 2026-06-03
Phase: 34 — Creative Asset Auto Set Input Variables Output Debug Planning
Type: DEBUG_PLAN_READY
Branch: main

---

## 1. Purpose

Investigate why `Set Input Variables` output remains empty after Phase 30 safe sample input patch and Phase 32 re-import. Determine root cause. Produce a controlled fix plan for Phase 35. **No workflow JSON changes in Phase 34. No n8n import or execution.**

---

## 2. Observed Failure From Phase 33

| Observation | Value |
|-------------|-------|
| Execution completed | YES — workflow ran |
| Set Input Variables node clicked | YES |
| Output panel | 1 item, 0 fields visible |
| Message (output panel) | "No fields - item(s) exist, but they're empty." |
| Message (parameters panel) | **"Currently no items exist"** |
| Expected 19 safe sample fields | ALL MISSING |
| Same behavior as Phase 27 (pre-patch) | YES — identical |
| Credentials attached | NO |
| API calls | NO |
| Production side effect | NO |

The **parameters panel** message "Currently no items exist" is the critical indicator. It means n8n UI shows the `Set Input Variables` node has **zero assignments configured** — not just empty output, but empty configuration as seen by n8n. The Phase 30 patch wrote 19 fields into the repo JSON, but n8n does not display or execute them.

---

## 3. Repo Workflow Inspection

**File:** `n8n/workflows/creative_asset_auto_skeleton.json`

### 3.1 — Set Input Variables Node Identity

| Property | Value |
|----------|-------|
| Node name | `Set Input Variables` |
| Node ID | `a2000002-0002-4001-a002-200000000002` |
| Node type | `n8n-nodes-base.set` |
| typeVersion | `3` |
| Position | `[500, 420]` |
| On main execution path | **YES** — connections confirm: `Manual Trigger → Set Input Variables → Code: Load Brand Brain` |
| Duplicate nodes named "Set Input Variables" | **NO** — exactly one node with this name |

### 3.2 — Current Parameters in Repo JSON

The repo JSON has 19 assignments in `parameters.assignments.assignments`:

```json
"parameters": {
  "assignments": {
    "assignments": [
      { "id": "a2-set-001", "name": "brand_id",      "value": "VQ",                    "type": "string" },
      { "id": "a2-set-002", "name": "brand_name",    "value": "Vi Cuon",               "type": "string" },
      { "id": "a2-set-003", "name": "brief_request", "value": "REPLACE_WITH_...",       "type": "string" },
      { "id": "a2-set-004", "name": "asset_type",    "value": "social_static_post",    "type": "string" },
      { "id": "a2-set-005", "name": "platform",      "value": "Facebook",              "type": "string" },
      { "id": "a2-set-006", "name": "format",        "value": "1:1 square 1080x1080", "type": "string" },
      { "id": "a2-set-007", "name": "objective",     "value": "Engagement",            "type": "string" },
      { "id": "a2-set-008", "name": "request_id",    "value": "creative_asset_sandbox_001", "type": "string" },
      ... (19 total, including approval_required: true boolean, sandbox_mode: true boolean)
    ]
  },
  "options": {}
}
```

**The 19 fields ARE present and correctly formed in the repo JSON.** The Phase 30 patch was applied correctly to the repo file.

### 3.3 — Format Comparison: All Set Nodes in the Workflow

| Node | typeVersion | Assignments | Fields | Execution Result (Phase 27/33) |
|------|-------------|-------------|--------|-------------------------------|
| `Set Input Variables` | 3 | `assignments.assignments` | 19 | **EMPTY — "no items"** |
| `Set: approval_status = Draft` | 3 | `assignments.assignments` | 1 | Reported green in Phase 27 |
| `Set: Validation Error` | 3 | `assignments.assignments` | 2 | Not reached in Phase 27/33 |
| `Set: Error Log` | 3 | `assignments.assignments` | 4 | Not reached in Phase 27/33 |

All four Set nodes use the **identical** `assignments.assignments` format. However, only `Set Input Variables` output was confirmed empty. The others were not directly verified — `Set: approval_status = Draft` appeared green, but the `approval_status = Draft` value in the downstream output may have originated from `Code: AI Generate Creative Brief` (which hardcodes `approval_status: 'Draft'`), not from the Set node.

### 3.4 — Cross-Workflow Format Check

`content_auto_skeleton.json` was also inspected. Its `Set Input Variables` node uses the **identical** format:

```json
"type": "n8n-nodes-base.set",
"typeVersion": 3,
"parameters": {
  "assignments": {
    "assignments": [
      { "id": "a1-set-001", "name": "brand_id", "value": "VQ", "type": "string" },
      ...7 fields total...
    ]
  },
  "options": {}
}
```

Phase 20C execution of `content_auto_skeleton` also showed empty `Set Input Variables` output (classified PASS WITH NOTES because downstream Code nodes filled fallback values). This **confirms the issue is not specific to the creative_asset workflow or the Phase 30 patch** — it is a systemic format issue present since Phase 8.

### 3.5 — Execution Path Confirmed

```
Manual Trigger
   → Set Input Variables  [typeVersion 3 — assignments NOT rendered by n8n]
     → Code: Load Brand Brain  [uses inputData.brand_name || 'Vị Cuốn' fallback]
       → Code: AI Generate Creative Brief  [uses inputData.brand_id || 'VQ' fallback]
         → Code: Validate Required Fields
           → If: Validation Pass
             [TRUE] → Set: approval_status = Draft
                        → Code: Write Log Entry
                          → NoOp: STUB — Send to Approval Queue
             [FALSE] → Set: Validation Error → Stop and Error
```

The downstream Code nodes succeed via `|| fallback` regardless of `Set Input Variables` output. This masked the issue in Phase 27 and Phase 20C.

---

## 4. Likely Root Cause Ranking

**Updated 2026-06-03 — Owner canvas cross-check confirmed duplicate node clusters within the same workflow.**

### Rank 1 — n8n import merged/duplicated nodes into the existing workflow instead of clean replace (CONFIRMED — MOST LIKELY PRIMARY CAUSE)

**Evidence:**
- Owner canvas cross-check (2026-06-03) confirmed: the current sandbox workflow (`FnB OS V1 — Creative Asset Auto [SKELETON] — CURRENT SANDBOX`) contains **two complete node clusters** on the same canvas:
  - Top cluster: `Manual Trigger → Set Input Variables → Code: Load Brand Brain → Code: AI Generate Creative Brief → Code: Validate Required Fields → IF Validation Pass → approval/log/noop path`
  - Lower cluster: `Set Input Variables1 → Code: Load Brand Brain1 → Code: AI Generate Creative Brief1 → Code: Validate Required Fields1 → IF Validation Pass1 → duplicate approval/log/noop path`
- n8n import did NOT overwrite the existing workflow cleanly — it **merged the re-imported nodes alongside the existing ones**, creating a contaminated duplicate structure within the same workflow.
- Phase 32 re-import procedure did not produce a clean single-cluster workflow as intended.

### Rank 2 — Owner may have executed a contaminated workflow with duplicate branches (LIKELY — consequence of Rank 1)

**Evidence:**
- With duplicate node clusters on the canvas, n8n execution path is unpredictable — it may follow either the original or the duplicated branch.
- Phase 33 execution result ("Currently no items exist") is consistent with execution of either the pre-patch original Set node or the contaminated/disconnected duplicate.
- The Phase 30-patched Set Input Variables node (19 fields) may never have been executed cleanly.

### Rank 3 — n8n Set node typeVersion 3 does not parse `assignments.assignments` as written (POSSIBLE — deferred)

**Evidence:**
- "Currently no items exist" in parameters panel — may reflect the contaminated canvas state, not a format issue.
- Identical behavior in `content_auto_skeleton` (Phase 20C) — same format, same empty result.
- **Cannot confirm or rule out** until a clean single-cluster workflow is isolated and executed.
- **Deferred:** investigate only if Phase 35 clean isolation + Phase 36 execution still shows empty fields.

---

## 5. Fix Strategy — JSON Patch DEFERRED Pending Phase 35 Duplicate Isolation

**Updated 2026-06-03 — Architect decision: JSON patch fix (Code node replacement) is DEFERRED.**

The Owner cross-check (Section 6) confirmed a duplicate workflow exists in n8n. Because the duplicate means Phase 33 may have executed the wrong (pre-Phase 30) workflow instance, the root cause cannot be confirmed as a JSON format issue until the correct workflow is identified and tested. Proceeding directly to a JSON patch without resolving the duplicate would risk fixing the wrong problem.

**JSON patch fix is DEFERRED to Phase 36 or later, conditional on Phase 35 findings.**

### Deferred Fix Strategy (Phase 36 or later — conditional)

If Phase 35 duplicate isolation confirms that the correct (Phase 30-patched) workflow STILL shows empty Set Input Variables fields, then the Code node replacement below is the recommended fix.

**Proposed replacement approach:**
Replace `Set Input Variables` node (ID `a2000002-0002-4001-a002-200000000002`) — change `type` from `n8n-nodes-base.set` to `n8n-nodes-base.code`, `typeVersion` from `3` to `2`, and replace `parameters` with a `jsCode` block that explicitly returns all 19 fields.

```javascript
// Deferred Fix — Set Input Variables via Code node
// Replaces n8n-nodes-base.set typeVersion 3 (format unrecognized by n8n)
// Returns all 19 safe sample input fields explicitly.

return [{
  json: {
    brand_id:        "VQ",
    brand_name:      "Vi Cuon",
    brief_request:   "REPLACE_WITH_OWNER_BRIEF_REQUEST",
    asset_type:      "social_static_post",
    platform:        "Facebook",
    format:          "1:1 square 1080x1080",
    objective:       "Engagement",
    request_id:      "creative_asset_sandbox_001",
    campaign_name:   "Sandbox Creative Asset Test",
    channel:         "facebook",
    product_name:    "Heo quay nuong lu",
    offer:           "Sandbox sample only - no real promotion",
    target_audience: "office workers and local food lovers in Vinh",
    key_message:     "Fresh rolled food with warm street-premium visual direction",
    tone_of_voice:   "friendly, appetizing, local, premium-but-accessible",
    visual_direction:"warm brown, orange accent, clean food photography style",
    required_output: "design_brief",
    approval_required: true,
    sandbox_mode:    true
  }
}];
```

**What does NOT change if this fix is applied:**
- Node ID (keep `a2000002-0002-4001-a002-200000000002`)
- Node name (keep `"Set Input Variables"`)
- Node position (keep `[500, 420]`)
- Connections (unchanged — same node name in connections map)
- All other nodes, `active: false`, no credentials, no real API calls

**This fix is NOT applied in Phase 34 or Phase 35. Phase 35 scope is duplicate isolation only.**

---

## 6. Owner / n8n UI Cross-check — COMPLETED 2026-06-03 (Two rounds)

### Round 1 — Workflow-level check

| Check | Question | Owner Result |
|-------|----------|-------------|
| Check 1 | Workflow title correct? | **YES** — `FnB OS V1 — Creative Asset Auto [SKELETON] — CURRENT SANDBOX` |
| Check 2 | Duplicate workflow exists in n8n? | **YES — confirmed** |
| Check 3 | Set Input Variables is first node after Manual Trigger? | **YES** |

### Round 2 — Canvas-level check (critical finding)

Owner inspected the canvas of the current sandbox workflow. Observed:

| Cluster | Nodes | Status |
|---------|-------|--------|
| Top cluster (original) | Manual Trigger → Set Input Variables → Code: Load Brand Brain → Code: AI Generate Creative Brief → Code: Validate Required Fields → IF Validation Pass → approval/log/noop path | Present |
| Lower cluster (duplicate) | Set Input Variables**1** → Code: Load Brand Brain**1** → Code: AI Generate Creative Brief**1** → Code: Validate Required Fields**1** → IF Validation Pass**1** → duplicate approval/log/noop path | Present — **contaminated** |

**Critical finding:** n8n import did NOT overwrite the workflow cleanly. It **merged the re-imported nodes alongside the existing ones**, creating two complete parallel node clusters on the same canvas. The workflow is contaminated — it is not a clean single-cluster workflow.

**Architect decision (received 2026-06-03):**
- Do NOT execute again.
- Do NOT patch JSON yet.
- Do NOT delete nodes manually in n8n UI.
- Do NOT activate or publish.
- Do NOT attach credentials.
- Phase 35 must isolate a clean workflow target before any retest.

---

## 7. Safety Checklist

| Check | Status |
|-------|--------|
| Workflow JSON changed in Phase 34 | **NO** |
| `active=true` introduced | NO |
| Secrets added | NO |
| Credentials added | NO |
| Real API calls added | NO |
| n8n import executed | NO |
| n8n execution performed | NO |
| Auto-post / auto-reply | NO |
| Ads spend | NO |
| Production side effect risk | NO |
| Claude Code has n8n UI access | NO — analysis is repo-only |

---

## 8. Recommended Phase 35

**Phase 35 — Creative Asset Auto Sandbox Clean Workflow Isolation**

**Architect decision (2026-06-03):** The current sandbox workflow is contaminated — two complete node clusters exist on the same canvas. Do NOT execute or patch until a clean single-cluster workflow is established.

**Goal:** Identify a clean way to get one and only one Creative Asset Auto skeleton workflow in n8n sandbox — with a single uncontaminated node cluster — and record its identity for Phase 36 retesting.

**Phase 35 approach options (Builder will document in Phase 35 plan):**

| Option | Description | Preference |
|--------|-------------|------------|
| A — Archive + fresh import | Archive or rename the contaminated workflow, then import `creative_asset_auto_skeleton.json` as a brand-new workflow (no overwrite) | **Preferred — cleanest result** |
| B — Delete contaminated workflow + fresh import | Delete the contaminated workflow entirely, then import JSON fresh | Acceptable if archive not available |
| C — Manual node deletion in n8n UI | Manually delete the lower (duplicate) cluster nodes from the canvas | **NOT recommended** — risk of breaking connections; requires explicit Owner approval if pursued |

**Phase 35 constraints:**
- No manual node deletion unless Owner explicitly approves and Architect agrees.
- No workflow JSON modification.
- No execution in Phase 35 — isolation and inspection only.
- No activation, no credentials, no publish.
- Verify the resulting workflow has exactly 1 cluster, is INACTIVE, and has 0 credentials attached before exiting Phase 35.

**Phase 35 deliverable:**
- A single clean `FnB OS V1 — Creative Asset Auto [SKELETON]` workflow in n8n sandbox.
- Canvas: one Manual Trigger, one Set Input Variables, no `1`-suffixed duplicate nodes visible.
- active = INACTIVE, credentials = NONE, execution count = 0.

**Phase 36 (after Phase 35 — conditional):**
- Owner executes the clean workflow manually.
- If Set Input Variables output shows 19 fields → Phase 30 patch works — no JSON fix needed.
- If Set Input Variables output still empty → JSON patch fix (Code node replacement, Section 5) applied in Phase 36/37.

**Phase 35 entry criteria:**
- Phase 34 DONE + PUSHED.
- Owner has access to n8n sandbox.
- Contaminated workflow identified and documented.

---

## 9. Phase Connections

| Phase | Description | Status |
|-------|-------------|--------|
| Phase 8 | n8n Workflow Skeleton Build | DONE + PUSHED |
| Phase 27 | Sandbox Manual Execution — PASS WITH NOTES (empty Set node masked by fallbacks) | DONE + PUSHED |
| Phase 30 | Safe Sample Input Patch — 7 → 19 fields in Set node assignments | DONE + PUSHED |
| Phase 32 | Sandbox Re-import — merged nodes into existing workflow (contaminated canvas) | DONE + PUSHED |
| Phase 33 | Sandbox Manual Execution — FAIL (contaminated canvas, wrong/duplicate branch likely) | DONE + PUSHED |
| **Phase 34** | **Set Input Variables Debug Planning + 2 rounds of Owner cross-check (this phase)** | **DEBUG_PLAN_READY** |
| Phase 35 (TBD) | Clean Workflow Isolation — archive/replace contaminated canvas, establish single clean workflow | NOT STARTED |
| Phase 36 (TBD) | Manual execution check on clean workflow — conditional Code node fix if still empty | NOT STARTED |
| Phase 37+ (TBD) | Scope TBD based on Phase 35/36 findings | NOT STARTED |

---

## 10. Safety Confirmation

| Item | Status |
|------|--------|
| Workflow JSON modified in Phase 34 | NO |
| `active = true` introduced | NO |
| Real credentials added | NO |
| Real API calls added | NO |
| Auto-post / auto-reply / ad spend | NO |
| Production system modified | NO |
| n8n execution performed by Builder | NO |
| n8n import performed by Builder | NO |
| Secret scan (new files) | CLEAN |
| Scope creep | NO — read-only inspection + planning only |
