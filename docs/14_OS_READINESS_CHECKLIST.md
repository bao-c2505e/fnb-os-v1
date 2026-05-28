# 14 — OS Readiness Checklist

**Phase:** 6 — OS Readiness Pack
**Created By:** Claude Code (Builder, AGT-02) — 2026-05-28
**Purpose:** Validate FnB OS V1 foundation is complete and safe before runtime/n8n phases begin.

---

## How to Use

For each item: check the required file(s), verify the pass criteria, and mark `[x]`. If any item fails, follow the failure action before proceeding to Phase 7.

---

## 1. Repo Governance Readiness

- [ ] **CLAUDE.md exists and defines Builder rules**
  - Required: `CLAUDE.md`
  - Pass: File exists, defines agent identity (AGT-02), hard rules, session cap, and key file locations
  - Failure: Recreate from `agents/builder-claude-code.md` — escalate to Chief Architect

- [ ] **AGENTS.md defines agent roster**
  - Required: `agents/AGENT_REGISTRY.md` or `AGENTS.md`
  - Pass: File exists, lists all named agents with roles and IDs
  - Failure: Create or update agent registry

- [ ] **Command inbox is present**
  - Required: `commands/COMMAND_INBOX.md`
  - Pass: File exists and is parseable
  - Failure: Recreate from `commands/COMMAND_TEMPLATE.md`

- [ ] **Git repo is on main branch with clean working tree**
  - Required: `git status --short` (no output), `git branch` shows main
  - Pass: No uncommitted changes, no untracked Phase 6 files after commit
  - Failure: Commit or stash pending changes before runtime phases

- [ ] **No .env, credentials, or API keys committed**
  - Required: `git log --all --full-history -- '*.env'` returns nothing; grep for `sk-`, `Bearer`, `api_key` in tracked files returns nothing
  - Pass: Zero results
  - Failure: Remove immediately and rotate credentials if exposed

---

## 2. Agent Role Readiness

- [ ] **All 9 agent role files exist**
  - Required: `agents/chief-architect.md`, `agents/builder-claude-code.md`, `agents/reviewer-codex.md`, `agents/content-agent.md`, `agents/creative-asset-agent.md`, `agents/ads-pack-agent.md`, `agents/crm-followup-agent.md`, `agents/comment-inbox-agent.md`, `agents/approval-publishing-agent.md`
  - Pass: All 9 files exist and have non-empty content
  - Failure: Rebuild missing agent file from Phase 2 scope

- [ ] **Each agent file has required sections**
  - Required: Role, Mission, Inputs, Outputs, Guardrails, Approval Requirements, Done Criteria
  - Pass: All 7 sections present in each file
  - Failure: Patch missing sections — Codex review before proceeding

- [ ] **No agent file claims to be able to self-approve**
  - Required: All agent files
  - Pass: No agent file contains language allowing self-approval or direct publishing
  - Failure: Correct wording immediately

---

## 3. Brand Brain Readiness

- [ ] **Brand Brain file exists**
  - Required: `brand-brain/vi-cuon.md`
  - Pass: File exists with 6+ sections (Brand Snapshot, Target Customers, Core Selling Points, Tone of Voice, Content Pillars, Offer Rules, Compliance/Safety)
  - Failure: Rebuild from Phase 3 scope

- [ ] **Missing brand data is explicitly placeholdered (not invented)**
  - Required: `brand-brain/vi-cuon.md`, `01_BRAIN/menu_brain.md`
  - Pass: Prices, address, opening hours use `[FILL]` or `[OWNER_TO_PROVIDE_*]` — no invented values
  - Failure: Replace any invented values with correct placeholders immediately

- [ ] **Brand Brain is replaceable for other F&B brands**
  - Required: `brand-brain/vi-cuon.md` section "Replaceable Brand Context"
  - Pass: Replacement guide exists and is clear
  - Failure: Add replacement guide

---

## 4. Schema Readiness

- [ ] **All 7 marketing schemas exist**
  - Required: `schemas/content-output.schema.json`, `schemas/creative-brief.schema.json`, `schemas/ads-pack.schema.json`, `schemas/crm-followup.schema.json`, `schemas/comment-inbox-reply.schema.json`, `schemas/approval-status.schema.json`, `schemas/log-entry.schema.json`
  - Pass: All 7 files exist and are valid JSON
  - Failure: Rebuild from Phase 3 scope

- [ ] **All schemas use JSON Schema Draft-07 with additionalProperties: false**
  - Required: All 7 schema files
  - Pass: `"$schema": "http://json-schema.org/draft-07/schema#"` and `"additionalProperties": false` in each
  - Failure: Patch non-conforming schemas — Codex review required

- [ ] **approval_status enum is consistent across all schemas**
  - Required: All marketing schemas
  - Pass: All schemas use the same 7-state enum: Draft, Ready for Review, Needs Revision, Approved, Rejected, Scheduled, Published
  - Failure: Align inconsistent schemas

- [ ] **CRM and inbox schemas have human_review_required: const true**
  - Required: `schemas/crm-followup.schema.json`, `schemas/comment-inbox-reply.schema.json`
  - Pass: Both schemas have `"const": true` on `human_review_required`
  - Failure: Add `const: true` — Codex review required

---

## 5. Template Readiness

- [ ] **All 7 output templates exist**
  - Required: `templates/content-output-template.md`, `templates/creative-brief-template.md`, `templates/ads-pack-template.md`, `templates/crm-followup-template.md`, `templates/comment-inbox-reply-template.md`, `templates/approval-status-template.md`, `templates/log-entry-template.md`
  - Pass: All 7 files exist and are non-empty
  - Failure: Rebuild from Phase 4 scope

- [ ] **All templates include approval_status field**
  - Required: All 7 template files
  - Pass: `## approval_status` heading present with `Draft` default
  - Failure: Add approval_status field to any missing template

- [ ] **CRM and inbox templates have human_review_required: true**
  - Required: `templates/crm-followup-template.md`, `templates/comment-inbox-reply-template.md`
  - Pass: Both templates have `human_review_required` set to literal `true`
  - Failure: Correct the template value

- [ ] **All templates use [TO_FILL] / [OWNER_TO_PROVIDE_*] / [AUTO_GENERATED] placeholders**
  - Required: All 7 template files
  - Pass: No template has hardcoded brand-specific values in required fields
  - Failure: Replace hardcoded values with correct placeholders

---

## 6. Sample Output Readiness

- [ ] **All 7 sample files exist under samples/vi-cuon/**
  - Required: `samples/vi-cuon/content-sample.md`, `creative-brief-sample.md`, `ads-pack-sample.md`, `crm-followup-sample.md`, `comment-inbox-reply-sample.md`, `approval-status-sample.md`, `log-entry-sample.md`
  - Pass: All 7 files exist and are non-empty
  - Failure: Rebuild from Phase 5 scope

- [ ] **All samples have approval_status: Draft**
  - Required: All sample files (except approval-status-sample which tracks state)
  - Pass: No sample is marked Approved, Published, or Scheduled
  - Failure: Reset any incorrectly advanced status to Draft

- [ ] **CRM and inbox samples have human_review_required: true**
  - Required: `samples/vi-cuon/crm-followup-sample.md`, `samples/vi-cuon/comment-inbox-reply-sample.md`
  - Pass: Both files contain `human_review_required: true` (not false, not missing)
  - Failure: Correct immediately

- [ ] **No fake prices, offers, addresses, or scarcity claims in samples**
  - Required: All sample files
  - Pass: All monetary values and contact details use `[OWNER_TO_PROVIDE_*]` placeholders; no "only X left", no invented star ratings
  - Failure: Replace invented values with placeholders

---

## 7. Approval Gate Readiness

- [ ] **Approval state machine is documented**
  - Required: `docs/10_SCHEMA_SYSTEM.md` or `module-sops/approval-publishing-sop.md`
  - Pass: 7-state machine (Draft → … → Published) is clearly defined with who-can-set rules
  - Failure: Document the state machine

- [ ] **Only Owner can set Approved — documented**
  - Required: `module-sops/approval-publishing-sop.md`
  - Pass: Explicit statement that only Owner may set `Approved`
  - Failure: Add explicit ownership rule

- [ ] **Published and Scheduled require prior Approved**
  - Required: `schemas/approval-status.schema.json`, `module-sops/approval-publishing-sop.md`
  - Pass: Both files state this prerequisite
  - Failure: Add the rule where missing

- [ ] **Owner does not debug agent outputs manually (no screenshot workflow)**
  - Required: `docs/11_MODULE_SOP_SYSTEM.md`
  - Pass: Doc explicitly states why screenshots are not substitutes for logs
  - Failure: Add clarification

---

## 8. Logging / Handoff Readiness

- [ ] **Agent Activity Log exists and has Phase 5 entry**
  - Required: `logs/AGENT_ACTIVITY_LOG.md`
  - Pass: File exists, Phase 5 row is present
  - Failure: Add missing log entry

- [ ] **Phase Log exists and has Phase 5 entry**
  - Required: `09_LOGS/PHASE_LOG.md`
  - Pass: File exists, Phase 5 entry is present
  - Failure: Add missing log entry

- [ ] **Current Phase file reflects Phase 6**
  - Required: `handoff/CURRENT_PHASE.md`
  - Pass: Phase 6 is shown as current phase with BUILDER_DONE_PENDING_REVIEW
  - Failure: Update the file

- [ ] **Session Summary is up to date**
  - Required: `handoff/SESSION_SUMMARY.md`
  - Pass: Latest session block covers Phase 6 build
  - Failure: Update the file

- [ ] **Log entries use structured format (not screenshots or free text)**
  - Required: `logs/AGENT_ACTIVITY_LOG.md`
  - Pass: All entries use the table format: Time | Agent | Task | Action | Result | Files
  - Failure: Reformat non-conforming entries

---

## 9. Safety Readiness

- [ ] **No secrets in any tracked file**
  - Required: Entire repo
  - Pass: No API key, token, password, or credential in any committed file
  - Failure: Remove and rotate immediately

- [ ] **No auto-post capability wired**
  - Required: All agent files, SOPs, templates, samples
  - Pass: No file contains code or instruction to post directly to any platform
  - Failure: Remove auto-post reference

- [ ] **No auto-reply to real customers wired**
  - Required: All agent files, SOPs, templates, samples
  - Pass: All inbox/CRM files state human_review_required and no auto-send
  - Failure: Add explicit block

- [ ] **No ads spend wired**
  - Required: All ads-pack files, SOPs, samples
  - Pass: All ads files state no campaign launch without Owner Approved
  - Failure: Add explicit block

- [ ] **n8n active=false rule documented for future phases**
  - Required: `docs/16_PRE_RUNTIME_PLAN.md`
  - Pass: Runtime safety rules section states all n8n workflows must default to `active: false`
  - Failure: Add the rule

---

## 10. Pre-Runtime Readiness

- [ ] **No n8n workflow JSON exists yet**
  - Required: `n8n/` folder (check for .json workflow files)
  - Pass: No workflow JSON files present in n8n/ (only smoke-tests or empty)
  - Failure: Review and remove any premature workflow files

- [ ] **No runtime automation script exists**
  - Required: Entire repo
  - Pass: No `.py`, `.js`, `.ts`, `.sh` runtime scripts in Phase 4–6 scope folders
  - Failure: Remove or move to correct phase scope

- [ ] **Pre-runtime plan is documented**
  - Required: `docs/16_PRE_RUNTIME_PLAN.md`
  - Pass: File exists with: what is ready, what is not, required external systems, data still needed, runtime safety rules
  - Failure: Create the file

- [ ] **All docs reference correct file paths**
  - Required: All docs/1*.md files
  - Pass: File path references in docs match actual files in repo
  - Failure: Update stale paths

---

## Summary

**Total checks:** 34

To pass readiness review, all 34 items must be `[x]`. Any unchecked item is a blocker for Phase 7.

If 1–3 items fail due to missing brand data (prices, address, etc.) — these are **known limitations**, not blockers. Document them in `handoff/PHASE_6_HANDOFF.md` and proceed.
