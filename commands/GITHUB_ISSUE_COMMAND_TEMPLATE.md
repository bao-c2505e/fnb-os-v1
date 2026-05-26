# GitHub Issue Command Template

Created By: Claude Code (Builder) — 2026-05-26
Phase: 0.8

Use this template when opening a GitHub Issue as a command (Mode 2).
Copy the Issue Body section below — do not include this header in the actual Issue.

---

## Issue Title Format

```
[CMD-X.X-XXX] Phase X.X — <Short objective, max 60 chars>
```

Example:
```
[CMD-0.8-001] Phase 0.8 — GitHub Command Bridge
```

---

## Issue Labels to Apply at Creation

- `status:assigned`
- `priority:high` (or medium / low)
- `phase:0.8` (replace with actual phase)

---

## Issue Body

Copy everything below this line into the GitHub Issue body:

---

### Command Metadata

| Field | Value |
|-------|-------|
| `command_id` | CMD-X.X-XXX |
| `phase` | X.X |
| `objective` | [One-line summary of what needs to be built or fixed] |
| `created_by` | [ChatGPT / Owner] |
| `assigned_builder` | Claude Code |
| `assigned_reviewer` | Codex |
| `chief_architect` | ChatGPT |
| `owner_approver` | Owner |
| `priority` | high / medium / low |
| `status` | ASSIGNED |
| `review_required` | true |
| `approval_required` | true |
| `handoff_required` | true |
| `logs_required` | true |
| `log_required` | true |

---

### Owner Request

[Plain-language description of what needs to be built or fixed. 2–4 sentences. No screenshots — reference exact repo file paths, log entries, or error text.]

---

### Scope Files

Files the Builder is allowed to create or modify:

- `[exact/path/file1.md]`
- `[exact/path/file2.md]`
- `[folder/]` (if all files in folder are in scope)

---

### Forbidden Actions

- Do not hardcode API keys, tokens, passwords, or secrets.
- Do not commit or push without `OWNER_APPROVED`.
- Do not auto-post, auto-reply to real users, activate n8n workflows, or run paid ads.
- Do not modify files outside Scope Files.
- Do not open the next phase.
- [Add phase-specific forbidden actions here]

---

### Acceptance Criteria

- [ ] [Specific, testable condition — what does DONE look like?]
- [ ] [Another condition]
- [ ] Handoff and logs updated
- [ ] No secrets in any file changed this phase
- [ ] `git status` shows only Scope Files as modified or new

---

### required_outputs

- [e.g. `commands/GITHUB_COMMAND_BRIDGE.md` created with mode guide]
- [e.g. Updated `handoff/CURRENT_PHASE.md` with status BUILDER_DONE_PENDING_REVIEW]
- [e.g. Final output ending with `READY FOR CODEX REVIEW`]

---

### Review Checklist

Codex must verify each item:

- [ ] All acceptance criteria met — state PASS or FAIL for each
- [ ] No files outside Scope Files were modified
- [ ] No hardcoded secrets in any changed file
- [ ] Builder did not perform Reviewer or Owner actions
- [ ] No auto-post, auto-reply, workflow activation, or ads
- [ ] `handoff/CURRENT_PHASE.md` and `handoff/SESSION_SUMMARY.md` updated
- [ ] Logs appended (`09_LOGS/PHASE_LOG.md`, `logs/AGENT_ACTIVITY_LOG.md`)

---

### Approval Gate

Owner must confirm before committing:

- [ ] Codex REVIEW_PASS recorded in `commands/COMMAND_STATUS.md`
- [ ] `handoff/SESSION_SUMMARY.md` reviewed and satisfactory
- [ ] No outstanding open issues in SESSION_SUMMARY
- [ ] `git status` shows only expected files

**Commit only after all items above are checked.**

---

### Status History

| Date | Actor | Status | Note |
|------|-------|--------|------|
| [YYYY-MM-DD] | Owner | ASSIGNED | Command opened |

*Update this table as status changes. Mirrors `commands/COMMAND_STATUS.md`.*

---

### logs_required

- `09_LOGS/PHASE_LOG.md` — append phase entry
- `logs/AGENT_ACTIVITY_LOG.md` — append session row

---

*This Issue was created using `commands/GITHUB_ISSUE_COMMAND_TEMPLATE.md`.*
*Full bridge rules: `commands/GITHUB_COMMAND_BRIDGE.md`*
*Routing rules: `commands/COMMAND_ROUTING_RULES.md`*
