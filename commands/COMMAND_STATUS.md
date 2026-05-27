# Command Status

Created By: Codex (Reviewer) - 2026-05-26
Updated By: Claude Code (Builder) — 2026-05-27 (Phase 1.1 close)

## Status Lifecycle

```
NEW
 └─> ASSIGNED
      └─> IN_PROGRESS
           ├─> BUILDER_DONE
           │    └─> REVIEW_REQUESTED
           │         ├─> REVIEW_PASS
           │         │    └─> OWNER_APPROVED
           │         │         └─> CLOSED
           │         └─> REVIEW_FAIL
           │              └─> IN_PROGRESS  (builder fixes and re-submits)
           └─> BLOCKED  (awaiting input or clarification)
```

## Status Definitions

| Status | Meaning | Responsibility |
| --- | --- | --- |
| `NEW` | Command created, not yet accepted by any agent | ChatGPT / Owner |
| `ASSIGNED` | Command assigned to a specific Builder agent | ChatGPT / Owner |
| `IN_PROGRESS` | Builder is actively working on the command | Assigned Builder |
| `BLOCKED` | Work cannot continue — missing input, credential, or approval | Assigned Builder |
| `BUILDER_DONE` | Builder finished output and updated handoff/logs; awaiting review | Assigned Builder |
| `REVIEW_REQUESTED` | Reviewer has been formally asked to review the output | Assigned Builder |
| `REVIEW_PASS` | Reviewer confirmed output meets acceptance criteria | Assigned Reviewer |
| `REVIEW_FAIL` | Reviewer rejected output with reason recorded | Assigned Reviewer |
| `OWNER_APPROVED` | Owner approved the reviewed output; ready to commit | Owner |
| `CLOSED` | Command committed and completed. No further action. | Owner / ChatGPT |

## Transition Rules

- Only the **Builder** may move: `ASSIGNED → IN_PROGRESS → BUILDER_DONE → REVIEW_REQUESTED`
- Only the **Reviewer** may move: `REVIEW_REQUESTED → REVIEW_PASS` or `→ REVIEW_FAIL`
- On `REVIEW_FAIL`: Builder fixes issues, moves back to `IN_PROGRESS`, then re-submits to `BUILDER_DONE`
- Only the **Owner** may move: `REVIEW_PASS → OWNER_APPROVED → CLOSED`
- A command in `BLOCKED` status must include a `blocked_reason` field
- **Commit is only allowed after `OWNER_APPROVED`**

## Current Command Index

| Command ID | Phase | Builder | Reviewer | Priority | Status |
| --- | --- | --- | --- | --- | --- |
| CMD-1.1-001 | 1.1 | Claude Code | Codex | high | CLOSED (commit d054f65) |
| CMD-0.15-001 | 0.15 | Claude Code | Codex | high | CLOSED (commit 1239a1d) |
| CMD-0.14-001 | 0.14 | Claude Code | Codex | high | CLOSED (commit 7305acb) |
| CMD-0.13-001 | 0.13 | Claude Code | Codex | high | CLOSED (commit c014a25) |
| CMD-0.12-001 | 0.12 | Claude Code | Codex | high | CLOSED (commit 36fcfe) |
| CMD-0.11-001 | 0.11 | Claude Code | Codex | high | CLOSED (commit bbda9d1) |
| CMD-0.10-001 | 0.10 | Claude Code | Codex | high | CLOSED (commit 7498c73) |
| CMD-0.9-001 | 0.9 | Claude Code | Codex | high | CLOSED (commit fd9c750) |
| CMD-0.8-001 | 0.8 | Claude Code | Codex | high | CLOSED (commit e58427c) |
| CMD-0.7-001 | 0.7 | Claude Code | Codex | high | CLOSED (commit d4771a) |
| CMD-0.6-001 | 0.6 | Claude Code | Codex | high | CLOSED (commit c20ca42) |
