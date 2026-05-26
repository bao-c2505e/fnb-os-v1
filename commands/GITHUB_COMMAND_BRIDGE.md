# GitHub Command Bridge

Created By: Claude Code (Builder) — 2026-05-26
Phase: 0.8

This document defines how commands move between ChatGPT, Claude, Codex, and Owner via the repo and GitHub Issues.

---

## Two Command Modes

### Mode 1 — Repo File (`commands/COMMAND_INBOX.md`)

The command record lives entirely in `commands/COMMAND_INBOX.md`.

**Use Mode 1 when:**
- All agents are working locally or via Claude Code CLI
- No GitHub remote interaction is needed
- The command is part of an internal repo build phase

**How it works:**
1. ChatGPT drafts the command using `commands/COMMAND_TEMPLATE.md`.
2. Owner pastes the command record into `commands/COMMAND_INBOX.md` at the top of the Inbox section.
3. Owner sets `status: ASSIGNED`.
4. Agents read by opening `commands/COMMAND_INBOX.md` and finding their command ID.

---

### Mode 2 — GitHub Issue

The command is filed as a GitHub Issue using `commands/GITHUB_ISSUE_COMMAND_TEMPLATE.md`.
The repo's `commands/COMMAND_INBOX.md` contains a reference row pointing to the Issue.

**Use Mode 2 when:**
- Owner wants a persistent, linkable audit trail outside the repo files
- ChatGPT needs to reference the command from a browser (not the CLI)
- The command involves review or comment from external stakeholders
- Owner wants automatic GitHub notifications when status labels change

**How it works:**
1. ChatGPT drafts the command using `commands/GITHUB_ISSUE_COMMAND_TEMPLATE.md`.
2. Owner opens a GitHub Issue with the title `[CMD-X.X-XXX] <phase> — <objective>`.
3. Owner adds a reference row to `commands/COMMAND_INBOX.md`:
   ```
   | CMD-X.X-XXX | X.X | GitHub Issue #NNN | https://github.com/owner/repo/issues/NNN |
   ```
4. Owner sets the Issue label to `status:assigned`.
5. Agents read the command from the GitHub Issue body.

---

## Field Mapping — COMMAND_TEMPLATE.md → GitHub Issue

| Command Field | GitHub Issue Location |
|---------------|-----------------------|
| `command_id` | Issue title prefix: `[CMD-X.X-XXX]` |
| `phase` | Issue title body |
| `created_by` | Issue author |
| `assigned_builder` | Issue body `assigned_builder:` field |
| `assigned_reviewer` | Issue body `assigned_reviewer:` field |
| `priority` | Issue label: `priority:high`, `priority:medium`, `priority:low` |
| `status` | Issue label: see Status-to-Label Mapping below |
| `owner_request` | Issue body `## Owner Request` section |
| `scope_files` | Issue body `## Scope Files` section |
| `forbidden_actions` | Issue body `## Forbidden Actions` section |
| `acceptance_criteria` | Issue body `## Acceptance Criteria` section (checkboxes) |
| `output_required` | Issue body `## Output Required` section |
| `review_required` | Issue body field |
| `approval_required` | Issue body field |
| `blocked_reason` | Issue comment by Builder |
| `review_notes` | Issue comment by Reviewer |

---

## Status-to-Label Mapping

| Command Status | GitHub Issue Label |
|----------------|--------------------|
| `NEW` | `status:new` |
| `ASSIGNED` | `status:assigned` |
| `IN_PROGRESS` | `status:in-progress` |
| `BLOCKED` | `status:blocked` |
| `BUILDER_DONE` | `status:builder-done` |
| `REVIEW_REQUESTED` | `status:review-requested` |
| `REVIEW_PASS` | `status:review-pass` |
| `REVIEW_FAIL` | `status:review-fail` |
| `OWNER_APPROVED` | `status:owner-approved` |
| `CLOSED` | Issue closed + `status:closed` |

Labels must be created in the GitHub repo settings before use. Label names must match exactly.

---

## Ownership Rules

| Action | Who Does It |
|--------|-------------|
| Create command record (Mode 1 or Mode 2) | Owner or ChatGPT |
| Set status to ASSIGNED | Owner or ChatGPT |
| Move IN_PROGRESS → BUILDER_DONE → REVIEW_REQUESTED | Claude Code (Builder) |
| Move REVIEW_REQUESTED → REVIEW_PASS / REVIEW_FAIL | Codex (Reviewer) |
| Move REVIEW_PASS → OWNER_APPROVED → CLOSED | Owner |
| Update GitHub Issue labels | Owner (manually until automation is built) |
| Close GitHub Issue | Owner, after CLOSED status confirmed in repo |

No agent may change a status state that belongs to another role.

---

## When a Command Is Closed

A command is CLOSED when **all** of the following are true:

1. Status in `commands/COMMAND_STATUS.md` = `CLOSED`
2. `git log` confirms the commit for this phase/command
3. If Mode 2: GitHub Issue is closed with label `status:closed`

Do not close a command if the commit has not been made.

---

## Reference to COMMAND_INBOX.md for Mode 2

When using GitHub Issue mode, add a row to the inbox:

```markdown
### CMD-X.X-XXX (GitHub Issue)

| Field | Value |
|-------|-------|
| `command_id` | CMD-X.X-XXX |
| `mode` | GitHub Issue |
| `issue_url` | https://github.com/[owner]/[repo]/issues/[number] |
| `status` | [current status] |
| `assigned_builder` | Claude Code |
| `assigned_reviewer` | Codex |
```

The full command fields live in the Issue body. The COMMAND_INBOX.md row is the index pointer only.

---

## Future Automation (Out of Scope for Phase 0.8)

Once n8n or GitHub Actions are available (Phase 2+), the following can be automated:
- Auto-create COMMAND_INBOX.md row when a GitHub Issue is opened with `[CMD-` prefix
- Auto-update Issue label when Builder changes status in COMMAND_STATUS.md
- Auto-notify Codex (via Telegram) when status reaches REVIEW_REQUESTED
- Auto-close Issue when CLOSED status is set in repo

None of this is implemented in Phase 0.8.
