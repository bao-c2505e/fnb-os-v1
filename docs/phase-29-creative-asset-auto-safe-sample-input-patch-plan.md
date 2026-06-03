# Phase 29 — Creative Asset Auto Safe Sample Input Patch Planning

Created By: Claude Code (Builder, AGT-02) — 2026-06-03
Phase: 29 — Creative Asset Auto Safe Sample Input Patch Planning
Status: PLAN_READY — AWAITING CODEX REVIEW
Branch: main
Workflow Target: `n8n/workflows/creative_asset_auto_skeleton.json`

---

## 1. Purpose

Phase 29 plans a safe patch for the `Set Input Variables` node in `creative_asset_auto_skeleton` to eliminate the "No fields - item(s) exist, but they're empty." display observed in Phase 27 sandbox execution and to enrich the sandbox input panel with descriptive, non-sensitive safe sample fields.

**Phase 29 is planning only.** No workflow JSON is modified in this phase.
The actual patch is deferred to Phase 30, pending Owner approval.

---

## 2. Current Finding

### 2.1 — Workflow File

| Property | Value |
|----------|-------|
| File | `n8n/workflows/creative_asset_auto_skeleton.json` |
| n8n display name | `FnB OS V1 — Creative Asset Auto [SKELETON]` |
| `active` field | `false` — must remain `false` at all times |
| Phase 29 reads this file | YES — read-only, no modification |

### 2.2 — Set Input Variables Node (Current State)

| Property | Value |
|----------|-------|
| Node name | `Set Input Variables` |
| Node ID | `a2000002-0002-4001-a002-200000000002` |
| Node type | `n8n-nodes-base.set` |
| typeVersion | `3` |
| Position | `[500, 420]` |
| Connection | Manual Trigger → **Set Input Variables** → Code: Load Brand Brain |

Current `assignments.assignments` array — 7 fields:

| Field ID | Name | Current Value | Type |
|----------|------|---------------|------|
| a2-set-001 | `brand_id` | `"VQ"` | string |
| a2-set-002 | `brand_name` | `"Vị Cuốn"` | string |
| a2-set-003 | `brief_request` | `"REPLACE_WITH_OWNER_BRIEF_REQUEST"` | string |
| a2-set-004 | `asset_type` | `"Photo"` | string |
| a2-set-005 | `platform` | `"Facebook"` | string |
| a2-set-006 | `format` | `"1:1 square 1080x1080"` | string |
| a2-set-007 | `objective` | `"Engagement"` | string |

**Phase 29 status:** Read only. No fields modified. The above represents the current state of the workflow file as of Phase 28 (commit `a7d0bd5`).

---

## 3. Root Cause Hypothesis

### 3.1 — Observed Symptom

During Phase 27 manual sandbox execution, the Owner reported:

> "Set Input Variables showed: 'No fields - item(s) exist, but they're empty.'"

### 3.2 — Confirmed Context (Phase 28 Documentation)

Phase 28 (`docs/PHASE_28_CREATIVE_ASSET_AUTO_SANDBOX_IO_STANDARDIZATION.md`, Section C) documented this as a **PASS WITH NOTES** — expected skeleton behavior. The downstream nodes produced correct stub output, validation passed the TRUE branch, and `approval_status = "Draft"` was set correctly.

### 3.3 — Root Cause Analysis

There are two contributing factors:

**Factor 1 — Empty incoming item from Manual Trigger:**

The `Manual Trigger` node emits an item with an empty JSON body: `{}`.
When this empty item enters the `Set Input Variables` node, the n8n execution panel displays the INCOMING item's state as:
> "No fields - item(s) exist, but they're empty."

This message refers to the **input** side of the Set node — the empty `{}` from Manual Trigger — not the **output** side. The node applies its `assignments.assignments` array and passes its 7 defined fields forward to the next node.

**Factor 2 — Downstream Code nodes use fallback patterns:**

The downstream Code nodes (`Code: Load Brand Brain`, `Code: AI Generate Creative Brief`) use JavaScript `||` fallback patterns:

```javascript
const inputData = $input.first().json;
const brandBrain = {
  brand_name: inputData.brand_name || 'Vị Cuốn',  // fallback if Set node output is empty
  ...
};
```

This means downstream execution succeeds **regardless** of whether the Set node output is actually populated — the Code nodes self-supply their stub data. The current 7-field output from Set Input Variables is redundant for skeleton execution.

**Combined effect:**

Even if the Set node's output fields ARE correctly set, the UI panel "empty" message (referring to the incoming `{}`) creates operator confusion during sandbox verification. Enriching the Set node with more explicit, clearly-named sample fields — especially `sandbox_mode: true` — would make the execution panel state immediately identifiable and remove ambiguity.

### 3.4 — What Phase 30 Patch Addresses

The Phase 30 patch targets **both** factors:

1. **Visual clarity:** Add fields with non-empty, descriptive string values so the execution panel shows populated data, making it immediately clear the node is working.
2. **Semantic clarity:** Add `sandbox_mode: true` to mark each sandbox run as sandbox-only in the execution data.
3. **Operational richness:** Add structured fields (`campaign_name`, `product_name`, `target_audience`, etc.) to make future sandbox runs more informative and closer to production input shape.

---

## 4. Proposed Safe Sample Input Fields

### 4.1 — Fields to ADD in Phase 30

The following 14 fields are proposed to be added to the `Set Input Variables` node's `assignments.assignments` array in Phase 30:

| Field Name | Type | Proposed Sample Value | Classification |
|------------|------|----------------------|----------------|
| `request_id` | string | `"creative_asset_sandbox_001"` | Safe — sandbox identifier |
| `brand_name` | string | `"Vi Cuon"` | Safe — brand identity (no secret) |
| `campaign_name` | string | `"Sandbox Creative Asset Test"` | Safe — clearly a test label |
| `channel` | string | `"facebook"` | Safe — platform identifier |
| `asset_type` | string | `"social_static_post"` | Safe — asset category |
| `product_name` | string | `"Heo quay nuong lu"` | Safe — product name (no price, no PII) |
| `offer` | string | `"Sandbox sample only - no real promotion"` | Safe — explicit sandbox label |
| `target_audience` | string | `"office workers and local food lovers in Vinh"` | Safe — generic demographic (no PII) |
| `key_message` | string | `"Fresh rolled food with warm street-premium visual direction"` | Safe — generic marketing copy |
| `tone_of_voice` | string | `"friendly, appetizing, local, premium-but-accessible"` | Safe — style descriptor |
| `visual_direction` | string | `"warm brown, orange accent, clean food photography style"` | Safe — visual descriptor |
| `required_output` | string | `"design_brief"` | Safe — output type identifier |
| `approval_required` | boolean | `true` | Safe — approval gate flag |
| `sandbox_mode` | boolean | `true` | Safe — explicit sandbox marker |

### 4.2 — Existing Fields to KEEP

All 7 existing fields must be retained in Phase 30 unchanged:

| Field | Current Value | Keep? |
|-------|---------------|-------|
| `brand_id` | `"VQ"` | YES — unchanged |
| `brand_name` | `"Vị Cuốn"` | YES — unchanged (note: proposed adds a second `brand_name` with ASCII value as a display-safe duplicate — Phase 30 to resolve naming) |
| `brief_request` | `"REPLACE_WITH_OWNER_BRIEF_REQUEST"` | YES — unchanged (still placeholder for production) |
| `asset_type` | `"Photo"` | YES — unchanged |
| `platform` | `"Facebook"` | YES — unchanged |
| `format` | `"1:1 square 1080x1080"` | YES — unchanged |
| `objective` | `"Engagement"` | YES — unchanged |

**Note on `brand_name` duplication:** The existing field uses `"Vị Cuốn"` (Unicode). The proposed field uses `"Vi Cuon"` (ASCII). Phase 30 should resolve whether to:
- Keep both (different IDs, different casing)
- Replace the placeholder with a single enriched field
- Rename proposed field to `brand_name_ascii` to avoid confusion

This decision requires Owner and Architect input before Phase 30 begins.

### 4.3 — Fields Safety Classification

| Classification | Fields | Rule |
|----------------|--------|------|
| **Safe — static identifiers** | `request_id`, `brand_name`, `channel`, `asset_type`, `required_output` | Non-sensitive identifiers. Safe for sandbox use. |
| **Safe — descriptor strings** | `campaign_name`, `offer`, `target_audience`, `key_message`, `tone_of_voice`, `visual_direction`, `product_name` | Generic marketing descriptors. No PII, no price, no credential. |
| **Safe — boolean flags** | `approval_required`, `sandbox_mode` | Control flags. No sensitive data. |
| **Placeholder — must not contain real data** | `brief_request` (existing) | Must remain `REPLACE_WITH_OWNER_BRIEF_REQUEST` or stub. Never a real campaign brief. |
| **Never add** | API keys, tokens, passwords, real customer names, real phone numbers, real email addresses, real order IDs | Must never appear in Set node fields. |

---

## 5. Patch Boundary For Next Phase

### 5.1 — What Phase 30 MAY Do

| Action | Permitted |
|--------|-----------|
| Modify `Set Input Variables` assignments in `creative_asset_auto_skeleton.json` | YES — with Owner approval |
| Add proposed 14 new fields | YES — after Owner and Architect review of this plan |
| Adjust field values to match Owner instruction | YES — Owner-directed only |
| Resolve `brand_name` duplication per Owner decision | YES |

### 5.2 — What Phase 30 MUST NOT Do

| Action | Permitted |
|--------|-----------|
| Set `"active": true` on the workflow | NO |
| Modify any node other than `Set Input Variables` | NO — unless separately scoped and approved |
| Add real credentials, API keys, tokens | NO |
| Add real customer PII | NO |
| Import the workflow to n8n | NO — separate phase with Owner approval phrase |
| Execute the workflow in n8n | NO — separate phase with Owner approval phrase |
| Modify any other workflow JSON file | NO |
| Publish or activate any workflow | NO |

### 5.3 — Phase 30 Entry Requirements

Before Phase 30 begins:

- [ ] Owner has reviewed and approved this Phase 29 plan
- [ ] Codex has reviewed Phase 29 and issued PASS
- [ ] Owner has issued explicit approval for Phase 30 patch
- [ ] `brand_name` duplication decision made by Owner/Architect
- [ ] Phase 29 committed and pushed to GitHub

---

## 6. Expected Sandbox Output After Future Patch

After Phase 30 patch is applied and re-imported to n8n sandbox:

| Execution Panel State | Before Phase 30 Patch | After Phase 30 Patch |
|----------------------|----------------------|----------------------|
| Set Input Variables incoming item display | "No fields - item(s) exist, but they're empty." (UI quirk from Manual Trigger `{}`) | Same UI quirk may still show (unchanged: Manual Trigger still emits `{}`), but the node's **output panel** will show 21 populated fields |
| Number of fields in node output | 7 | ~21 (7 existing + 14 new) |
| `sandbox_mode` visible in output | NO | YES — `sandbox_mode: true` |
| `approval_required` visible in output | NO | YES — `approval_required: true` |
| Execution panel ambiguity | High — "empty" message causes operator confusion | Low — additional fields make sandbox state unambiguous |

**Note:** The "No fields - item(s) exist, but they're empty." message may persist even after the patch because it refers to the Manual Trigger's incoming item, not the Set node's output. The patch improves the OUTPUT panel clarity, not the incoming item display. If the incoming item display must also be resolved, a Form Trigger or HTTP Request Trigger would be required in a future phase — that is out of scope for Phase 30.

---

## 7. Safety Checklist

| Check | Status in Phase 29 |
|-------|--------------------|
| Workflow JSON changed in Phase 29 | NO |
| `active=true` introduced | NO |
| Secrets added | NO |
| Credentials added | NO |
| Real API calls added | NO |
| n8n import executed | NO |
| n8n execution performed | NO |
| Real customer PII added | NO |
| Auto-post / auto-reply / ads mutation | NO |
| Production side effect risk | NO |
| Secret scan (new files) | CLEAN |
| Scope creep | NO — all files within Phase 29 scope |

---

## 8. Recommended Phase 30

### Phase 30 — Creative Asset Auto Safe Sample Input Patch Implementation

**Objective:** Implement the safe sample input patch planned in Phase 29. Modify `Set Input Variables` in `creative_asset_auto_skeleton.json` to add the 14 proposed sample fields with safe, non-sensitive values.

**Prerequisites:**
- Phase 29 DONE + PUSHED
- Owner approval for Phase 30 patch
- `brand_name` duplication decision resolved
- Codex PASS on Phase 29

**Scope:**
- File: `n8n/workflows/creative_asset_auto_skeleton.json`
- Node: `Set Input Variables` only
- Action: Add 14 new fields to `assignments.assignments`
- No other node or file modified

**Hard constraints (same as all phases):**
- `active: false` must remain in JSON
- No credentials
- No real API calls
- No activation
- No import (separate phase with Owner approval phrase)
- No execution (separate phase with Owner approval phrase)

**Post-patch verification:**
- Run `scripts/validate_json.py` — must PASS
- Run `scripts/check_n8n_workflows.py` — must PASS (active=false)
- Run `scripts/check_no_secrets.py` — must CLEAN
- Phase 31 (or equivalent): re-import patched workflow to n8n sandbox, re-run sandbox execution, verify enriched output panel

---

## 9. Phase Connections

| Phase | Description | Status |
|-------|-------------|--------|
| Phase 8 | n8n Workflow Skeleton Build — `creative_asset_auto_skeleton` created | DONE + PUSHED |
| Phase 26 | First Sandbox Import — `creative_asset_auto_skeleton` | DONE + PUSHED (PASS) |
| Phase 27 | Sandbox Manual Execution — `creative_asset_auto_skeleton` | DONE + PUSHED (PASS WITH NOTES) |
| Phase 28 | Sandbox I/O Standardization — input/output contracts, Phase 27 PASS WITH NOTES explanation | DONE + PUSHED |
| **Phase 29** | **Safe Sample Input Patch Planning (this phase)** | **PLAN_READY** |
| Phase 30 (TBD) | Safe Sample Input Patch Implementation — pending Owner approval | NOT STARTED |

---

## 10. Safety Confirmation

| Item | Status |
|------|--------|
| Workflow JSON modified | NO |
| `active = true` introduced | NO |
| Real credentials added | NO |
| Real API calls made | NO |
| Auto-post / auto-reply / ad spend | NO |
| Production system modified | NO |
| Real customer data used | NO |
| n8n workflow imported by Builder | NO |
| n8n workflow executed by Builder | NO |
| Secret scan (new files) | CLEAN |
| Scope creep (files outside scope) | NO |
