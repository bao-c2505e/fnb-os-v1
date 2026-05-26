# Phase 0.6 — Agent Command Intake Layer

Created By: Codex (Reviewer) - 2026-05-26
Updated By: Claude Code (Builder) - 2026-05-26

---

## Objective

Create a canonical command intake system so ChatGPT Chief Architect and Owner can assign work to Builder and Reviewer agents through repo files — without manual screenshots, copy-paste, or ad-hoc chat instructions as the source of truth.

All work must be traceable: every command has a record in the repo, every status transition is explicit, and every output is reviewable before commit.

---

## Files

| File | Purpose |
| --- | --- |
| `commands/COMMAND_INBOX.md` | Human-readable queue for incoming commands |
| `commands/COMMAND_STATUS.md` | Status lifecycle definitions and active command index |
| `commands/COMMAND_TEMPLATE.md` | Markdown template for authoring new commands |
| `schemas/command.schema.json` | JSON Schema (draft-07) for structured command validation |
| `docs/phase-0/PHASE_0_6_COMMAND_INTAKE.md` | This document |

---

## How to Issue a Command

1. Copy `commands/COMMAND_TEMPLATE.md`.
2. Fill all required fields (see Field Reference below).
3. Set `status: NEW`.
4. Add the command to the top of `commands/COMMAND_INBOX.md`.
5. Update the index row in `commands/COMMAND_STATUS.md`.
6. Tag the assigned Builder in conversation or Telegram.

---

## Command Lifecycle

```
NEW
 └─> ASSIGNED          ← Owner or ChatGPT assigns to a Builder
      └─> IN_PROGRESS  ← Builder starts work
           ├─> BLOCKED                   ← Builder cannot continue; records reason
           └─> BUILDER_DONE             ← Builder finished; handoff+logs updated
                └─> REVIEW_REQUESTED    ← Builder notifies Reviewer
                     ├─> REVIEW_PASS    ← Reviewer confirms output is correct
                     │    └─> OWNER_APPROVED  ← Owner signs off
                     │         └─> CLOSED     ← Committed and complete
                     └─> REVIEW_FAIL    ← Reviewer records reason; back to IN_PROGRESS
```

**Commit is only allowed after `OWNER_APPROVED`.**

---

## Who Does What

### Owner / ChatGPT Chief Architect
- Authors commands using `COMMAND_TEMPLATE.md`.
- Sets `assigned_builder` and `assigned_reviewer`.
- Moves status from `REVIEW_PASS` → `OWNER_APPROVED` → `CLOSED` after final sign-off.
- Runs `git commit` only after `OWNER_APPROVED`.

### Builder (Claude Code)
- Reads the command from `COMMAND_INBOX.md`.
- Checks scope: only touches `scope_files`, never violates `forbidden_actions`.
- Moves status: `ASSIGNED → IN_PROGRESS → BUILDER_DONE → REVIEW_REQUESTED`.
- Before `BUILDER_DONE`, must:
  - Update `handoff/CURRENT_PHASE.md` with status `BUILDER_DONE_PENDING_REVIEW`.
  - Update `handoff/SESSION_SUMMARY.md`.
  - Append to `09_LOGS/PHASE_LOG.md`.
  - Append to `logs/AGENT_ACTIVITY_LOG.md`.
- Produces all `output_required` artifacts.
- Does **not** commit.

### Reviewer (Codex)
- Reads the command and all `output_required` artifacts.
- Checks each `acceptance_criteria` item: pass or fail with reason.
- Moves status: `REVIEW_REQUESTED → REVIEW_PASS` or `→ REVIEW_FAIL`.
- On `REVIEW_FAIL`: records reason in `review_notes`; returns to Builder.
- Does **not** commit.

---

## Field Reference

| Field | Required | Description |
| --- | --- | --- |
| `command_id` | yes | Pattern: `CMD-[phase]-[seq]`, e.g. `CMD-0.6-001` |
| `phase` | yes | Phase number, e.g. `0.6` |
| `created_by` | yes | Author: Owner, ChatGPT, or agent ID |
| `assigned_builder` | yes | Builder agent, e.g. Claude Code |
| `assigned_reviewer` | yes | Reviewer agent, e.g. Codex |
| `priority` | yes | `high` / `medium` / `low` |
| `status` | yes | See lifecycle above |
| `owner_request` | yes | Plain-language description, min 10 chars |
| `scope_files` | yes | Array of exact paths allowed |
| `forbidden_actions` | yes | Array of explicit prohibitions |
| `acceptance_criteria` | yes | Array of testable DONE conditions |
| `output_required` | yes | Array of artifacts Builder must produce |
| `review_required` | yes | Boolean |
| `approval_required` | yes | Boolean |
| `handoff_required` | yes | Boolean |
| `log_required` | yes | Boolean |
| `blocked_reason` | when BLOCKED | Describes what is missing |
| `review_notes` | when REVIEW_PASS/FAIL | Reviewer's findings |

---

## Safety Rules

- No API keys, tokens, passwords, or secrets in any command file.
- `scope_files` must list exact paths — "everything" is not valid.
- `forbidden_actions` must always include no-hardcode-secrets and no-auto-publish.
- Repo files are the single source of truth for command state.
- Builder updates handoff and logs before marking `BUILDER_DONE`.

---

## Done Criteria — Phase 0.6

- [x] `commands/` folder created with INBOX, STATUS, TEMPLATE.
- [x] `schemas/command.schema.json` with all required fields and 10-state enum.
- [x] STATUS lifecycle covers: NEW, ASSIGNED, IN_PROGRESS, BLOCKED, BUILDER_DONE, REVIEW_REQUESTED, REVIEW_PASS, REVIEW_FAIL, OWNER_APPROVED, CLOSED.
- [x] TEMPLATE includes: command_id, phase, owner_request, assigned_builder, assigned_reviewer, scope_files, forbidden_actions, acceptance_criteria, output_required, review_required, approval_required.
- [x] Phase doc explains Builder role, Reviewer role, Owner role, commit gate.
- [x] Handoff and logs updated.
- [x] `python -m json.tool schemas/command.schema.json` passes.
- [x] No secrets in any Phase 0.6 file.
