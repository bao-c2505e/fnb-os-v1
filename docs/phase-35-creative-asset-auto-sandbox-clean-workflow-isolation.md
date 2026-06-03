# Phase 35 — Creative Asset Auto Sandbox Clean Workflow Isolation

Created By: Claude Code (Builder, AGT-02) — 2026-06-03
Updated By: Claude Code (Builder, AGT-02) — 2026-06-03 (Phase 35 Evidence Recording)
Phase: 35 — Creative Asset Auto Sandbox Clean Workflow Isolation
Type: EVIDENCE_RECORDED — PASS
Branch: main

---

## 1. Purpose

Cô lập một workflow Creative Asset Auto sandbox sạch trong n8n vì Phase 32 re-import đã không thực hiện clean replace — thay vào đó nó merge các node vào workflow đang tồn tại, tạo ra hai cụm skeleton trên cùng một canvas.

**Phase 35 là isolation/docs only.** Claude không thao tác n8n trực tiếp. Owner thực hiện các bước rename và import theo hướng dẫn trong doc này. Không execute, không activate, không credential, không API trong Phase 35.

---

## 2. Current Problem

| Issue | Detail |
|-------|--------|
| Duplicate workflows in n8n list | YES — at least 2 Creative Asset Auto workflows exist |
| Current SANDBOX workflow title | `FnB OS V1 — Creative Asset Auto [SKELETON] — CURRENT SANDBOX` |
| Canvas state of CURRENT SANDBOX | Contaminated — 2 complete skeleton clusters on same canvas |
| Top cluster (original) | Manual Trigger → Set Input Variables → Code: Load Brand Brain → Code: AI Generate Creative Brief → Code: Validate Required Fields → IF Validation Pass → approval/log/noop path |
| Lower cluster (duplicate) | Set Input Variables**1** → Code: Load Brand Brain**1** → Code: AI Generate Creative Brief**1** → Code: Validate Required Fields**1** → IF Validation Pass**1** → duplicate approval/log/noop path |
| Phase 33 execution result | FAIL — ran on contaminated canvas, execution path unpredictable |
| Can Phase 30 patch be tested? | NOT YET — need clean single-cluster workflow first |
| JSON patch fix status | DEFERRED — not applied until clean workflow isolated and tested |

**Root cause:** n8n import (Phase 32) merged re-imported nodes alongside existing nodes instead of cleanly replacing the workflow. This is a known n8n import behavior when targeting an existing workflow — it can append rather than replace.

---

## 3. Safe Owner Isolation Plan

**Owner performs the following steps in n8n sandbox UI. Claude does not touch n8n.**

**Prerequisites before starting:**
- Confirm n8n instance is sandbox: `https://n8n.baon8n.blog`
- NOT production instance
- Have repo file ready: `n8n/workflows/creative_asset_auto_skeleton.json`

### Step A — Rename the contaminated workflow (do NOT delete)

1. In n8n sandbox workflow list, locate the contaminated workflow:
   `FnB OS V1 — Creative Asset Auto [SKELETON] — CURRENT SANDBOX`
2. Rename it to:
   **`FnB OS V1 — Creative Asset Auto [SKELETON] — DUPLICATED DO NOT USE`**
3. Do NOT delete it — keep as historical reference.
4. Do NOT execute it.
5. Do NOT activate it.

### Step B — Import the repo JSON as a brand-new workflow

1. In n8n sandbox, go to **Workflows** list.
2. Click **+ New workflow** or **Import from file** (depending on n8n version).
3. Import from file: `n8n/workflows/creative_asset_auto_skeleton.json`
4. **Do NOT overwrite** the contaminated workflow — create a new workflow entry.
5. If n8n asks for a target: choose "New workflow" or equivalent.

### Step C — Rename the newly imported workflow

After import, rename the new workflow to:
**`FnB OS V1 — Creative Asset Auto [SKELETON] — CURRENT CLEAN SANDBOX`**

### Step D — Post-import verification (before exiting)

Owner must verify all of the following before reporting Phase 35 PASS:

| Verification Item | Expected | Owner confirms |
|-------------------|----------|----------------|
| Workflow title | `FnB OS V1 — Creative Asset Auto [SKELETON] — CURRENT CLEAN SANDBOX` | [ ] |
| Workflow `active` status | INACTIVE (toggle = grey/off) | [ ] |
| Workflow published | NO | [ ] |
| Credentials attached to any node | NONE | [ ] |
| Canvas cluster count | Exactly 1 cluster | [ ] |
| `Set Input Variables` node count | Exactly 1 (no `Set Input Variables1`) | [ ] |
| `Code: Load Brand Brain` node count | Exactly 1 (no `Code: Load Brand Brain1`) | [ ] |
| `IF Validation Pass` node count | Exactly 1 (no `IF Validation Pass1`) | [ ] |
| Any `1`-suffixed nodes visible | NONE | [ ] |
| Manual execution performed | NO | [ ] |

---

## 4. Evidence Form

Owner evidence received 2026-06-03:

```
Phase 35 Evidence:
- Date/time: 2026-06-03
- n8n instance URL: https://n8n.baon8n.blog
- New workflow name: FnB OS V1 — Creative Asset Auto [SKELETON] — CURRENT CLEAN SANDBOX ✓
- Current clean workflow opened: YES
- Canvas has exactly one skeleton cluster: YES
- Duplicate suffix nodes visible: NO
- Set Input Variables node count on main path: 1
- Workflow active status: inactive / not activated ✓ INACTIVE
- Workflow published: NO
- Credentials attached: NO / NONE
- Manual execution performed after clean isolation: NO
- Ready for Phase 36 clean sandbox manual execution retest: YES
- Notes: Owner confirmed clean isolation complete. All Phase 35 verification items PASS.
```

**Evidence Result: PASS**

---

## 5. What Not To Do

| Forbidden Action | Reason |
|------------------|--------|
| Execute the new workflow in Phase 35 | Phase 35 is isolation only — execution belongs to Phase 36 |
| Activate (toggle on) any workflow | Hard constraint — all workflows must remain INACTIVE |
| Publish any workflow | Hard constraint — no publishing |
| Attach real credentials | Hard constraint — no real credentials in sandbox skeleton |
| Delete the contaminated workflow | Keep as reference — do not delete without explicit Architect approval |
| Manually delete duplicate nodes on the contaminated canvas | High risk of breaking connections — do not modify the contaminated workflow |
| Edit workflow JSON in repo | Phase 35 is docs/isolation only — JSON patch deferred |
| Apply Code node fix | JSON patch deferred to Phase 36 or later, conditional on Phase 36 findings |
| Call any external API | No real API calls |

---

## 6. Success Criteria

**Phase 35 PASS** if all of the following:

| Criterion | Required |
|-----------|----------|
| Contaminated workflow renamed to `DUPLICATED DO NOT USE` | YES |
| New workflow `CURRENT CLEAN SANDBOX` imported from repo JSON | YES |
| New workflow has exactly 1 skeleton cluster on canvas | YES |
| No `1`-suffixed nodes present on new workflow canvas | YES |
| New workflow active status = INACTIVE | YES |
| No credentials attached to new workflow | YES |
| No manual execution performed in Phase 35 | YES |
| No workflow published | YES |
| No production side effect | YES |

**Phase 35 FAIL / BLOCKED** if any of:
- New import still produces duplicate node clusters on canvas
- New workflow imports as ACTIVE (stop immediately, deactivate)
- n8n does not allow fresh import as new workflow
- Credentials were prompted or auto-attached
- Manual execution was triggered accidentally

---

## 7. Recommended Phase 36

### If Phase 35 PASS:
**Phase 36 — Creative Asset Auto Current Clean Sandbox Manual Execution Retest**

Goal: Owner manually executes the `CURRENT CLEAN SANDBOX` workflow, inspects `Set Input Variables` output panel, and checks whether 19 fields are visible.

- If 19 fields visible → Phase 30 patch is correct, no JSON fix needed. Proceed to evidence recording.
- If Set Input Variables still empty → JSON patch fix (Code node replacement, per Phase 34 Section 5) is confirmed needed. Proceed to Phase 37 Code node fix.

### If Phase 35 FAIL:
**Phase 36 — Creative Asset Auto Sandbox Import Cleanup Planning**

Goal: Investigate why fresh import still produces duplicate clusters. May require n8n version check, alternative import method (create blank workflow + paste JSON), or Owner Architect escalation.

---

## 8. Safety Checklist

| Item | Phase 35 Status |
|------|----------------|
| Workflow JSON changed in repo | NO |
| `active = true` introduced in repo | NO |
| Secrets added | NO |
| Credentials added | NO |
| Real API calls added | NO |
| n8n execution performed by Builder/Claude | NO |
| Workflow activated | NO |
| Workflow published | NO |
| Production side effect risk | NO |
| Claude touches n8n UI directly | NO — Owner performs isolation steps |
| Duplicate nodes deleted from contaminated canvas | NO — contaminated workflow kept as-is |

---

## 9. Phase Connections

| Phase | Description | Status |
|-------|-------------|--------|
| Phase 26 | First Sandbox Import — original workflow created | DONE + PUSHED |
| Phase 27 | Sandbox Manual Execution — PASS WITH NOTES | DONE + PUSHED |
| Phase 30 | Safe Sample Input Patch — 19 fields in repo JSON | DONE + PUSHED |
| Phase 32 | Re-import — canvas contaminated (nodes merged, not replaced) | DONE + PUSHED |
| Phase 33 | Manual Execution — FAIL (contaminated canvas) | DONE + PUSHED |
| Phase 34 | Debug Planning + Owner cross-check — contamination confirmed | DONE + PUSHED |
| **Phase 35** | **Clean Workflow Isolation — rename contaminated, fresh import (this phase)** | **EVIDENCE_RECORDED — PASS** |
| Phase 36 (TBD) | Execution retest on clean workflow OR import cleanup planning | NOT STARTED |
| Phase 37+ (TBD) | Code node fix (conditional) OR evidence recording (conditional) | NOT STARTED |

---

## 10. Safety Confirmation

| Item | Confirmed |
|------|-----------|
| Workflow JSON modified in Phase 35 | NO |
| `active = true` introduced | NO |
| Real credentials added | NO |
| Real API calls added | NO |
| Auto-post / auto-reply / ad spend | NO |
| Production system modified | NO |
| n8n execution performed by Builder | NO |
| n8n import performed by Builder | NO |
| Secret scan (new files) | CLEAN |
| Scope creep beyond docs/isolation planning | NO |
