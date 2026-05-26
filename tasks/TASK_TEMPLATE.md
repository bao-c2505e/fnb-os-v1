# Task Contract - TASK-[PHASE]-[SEQ]

Created By: Codex (Builder) - 2026-05-26

## Assignment

- Assigned To: [Agent ID and name]
- Assigned By: [User / ChatGPT / Agent ID]
- Phase: [Phase]
- Priority: [high / medium / low]
- Status: pending
- Requires Human Approval: true

## Goal

[One or two sentences describing the outcome.]

## Allowed Scope

- [Exact file or folder path]
- [Exact file or folder path]

## Inputs

- [File, task row, or source to read]

## Expected Outputs

- [File, patch, review result, or artifact]

## Acceptance Criteria

- [ ] [Specific, testable condition]
- [ ] No hardcoded API keys, tokens, passwords, or secrets
- [ ] Approval gate documented for any external action
- [ ] Activity log updated

## Hard Constraints

- Do not modify files outside Allowed Scope.
- Do not auto-post, auto-reply, activate workflows, deploy, or spend money.
- Do not commit unless the task explicitly asks for a commit.

## Validation

- [Command or manual check]

## Result

- Review Result: [PASS / NEEDS_FIX]
- Files Changed: [List]
- Suggested Commit Message: [Message]
