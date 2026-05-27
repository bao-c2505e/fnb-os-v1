# Codex Reviewer Phase Template

**Template Version:** 2.1
**Maintained By:** ChatGPT (Chief Architect)
**Last Updated:** 2026-05-28
**Used By:** ChatGPT when writing a Codex review prompt; Codex when conducting a review

This template is the standard format for all Reviewer phase prompts in FnB OS V1 / Vị Cuốn Growth OS.
ChatGPT fills in all placeholders before delivering the prompt to Codex.
Codex treats every field as a binding constraint — review only what is in scope, report in the exact format specified.

---

## How to Use This Template

1. ChatGPT copies this template and fills every `[PLACEHOLDER]`.
2. ChatGPT delivers the completed review prompt + Builder Report to the Owner.
3. Owner delivers both to Codex.
4. Codex reads the original Builder prompt, the Builder Report, and every scoped file.
5. Codex returns the mandatory review output in the format specified below.

Codex must NOT rewrite files, add features, or expand scope. Review only.

---

---

## REVIEW REQUEST — PHASE [PHASE_ID] — [PHASE_NAME]

You are Codex acting as REVIEWER for FnB OS V1 / Vị Cuốn Growth OS.

### CONTEXT

- Phase: [PHASE_ID] — [PHASE_NAME]
- Builder: Claude Code (AGT-02)
- Repo: D:\FNB_OS_V1 / https://github.com/bao-c2505e/fnb-os-v1
- Branch: main
- Your role: Reviewer only. You may NOT edit files, commit, push, or approve.

### YOUR TASK

Review the Builder's output for Phase [PHASE_ID].
Check every item in the checklist below.
Return the mandatory review output in the exact format specified.

Do NOT fix files. Do NOT rewrite content. If issues are found, list them clearly — Builder fixes.

### FILES TO REVIEW

[FILES_TO_REVIEW]

Read every file on this list in full. Do not skip any.

```
- docs/phase-X/file-name.md
- docs/phase-X/another-file.md
- [additional files as listed in the Builder Report]
```

Also read:
- `handoff/SESSION_SUMMARY.md` — Builder's session notes
- `logs/AGENT_ACTIVITY_LOG.md` — most recent row

### EXPECTED SCOPE

[EXPECTED_SCOPE]

Describe what the phase was supposed to create or change.
Any file created or modified outside this scope is a scope violation.

```
This phase should have created or modified:
- [description of expected output]

This phase should NOT have touched:
- .env or credential files
- n8n production workflows
- Any Phase 1 docs (unless a minor link/reference was explicitly listed in scope)
- .claude/
- [phase-specific exclusions]
```

### BLOCKERS

[BLOCKERS]

These are FAIL conditions. One FAIL means REVIEW_FAIL. All must be checked.

```
1. Exposed secret — any real API key, token, password, or credential value in any scoped file.
   Patterns to scan: api_key, token, password, secret, sk-, xox, AIza, ghp_, ya29.

2. .claude/ staged or committed — check git status output in Builder Report.

3. Major scope violation — any file outside [EXPECTED_SCOPE] was created or modified
   without a documented reason.

4. Production n8n workflow — any workflow JSON with "active": true.

5. Auto-post / auto-reply / ads execution — any code or workflow that posts content,
   messages real users, or activates paid ads.

6. Empty or useless files — any output file is empty, title-only, or unrelated to
   F&B / Vị Cuốn brand.

7. Acceptance criteria failure — any item in [ACCEPTANCE_CRITERIA] is not met.
```

### WARNINGS

[WARNINGS]

These are non-blocking observations. Phase continues. Notes go in PASS_WITH_NOTES section.

```
- Metadata wording or minor label inconsistency
- Placeholder text like [FILL], [OWNER_CONFIRM], [TODO] that is intentional
- Minor formatting inconsistency (spacing, heading level)
- Slightly imperfect file naming if the file is usable and correctly scoped
- Duplicate information inherited from a template
```

### ACCEPTANCE CRITERIA

[ACCEPTANCE_CRITERIA]

Evaluate each item as PASS or FAIL. Copy from the original Builder prompt.

```
| # | Criterion |
|---|-----------|
| 1 | [text from Builder prompt acceptance criteria] |
| 2 | [text] |
| 3 | [text] |
| 4 | No secret/API key/token/password is present in any scoped file. |
| 5 | .claude/ is not staged or committed. |
| 6 | No production n8n workflow is created. |
| 7 | No auto-post, auto-reply, or ads execution code is present. |
| 8 | All scoped files are non-empty and specific to FnB OS V1 / Vị Cuốn brand. |
```

### REVIEW OUTPUT FORMAT

[REVIEW_OUTPUT_FORMAT]

Return your review in this exact structure — no deviation:

```
## REVIEW RESULT: PASS | PASS_WITH_NOTES | FAIL

Reviewed by: Codex (AGT-03)
Phase: [PHASE_ID] — [PHASE_NAME]
Files reviewed: [count]

### Acceptance Criteria
| # | Criterion | Result | Reason |
|---|-----------|--------|--------|
| 1 | [text] | PASS/FAIL | [brief evidence or exact issue] |

### Scope Violation Check
| File | In scope? | Note |
|------|-----------|------|
| [path] | YES / NO | [if NO, describe the violation] |

### Secret Scan
Result: CLEAN / WARN
[If WARN: file name and exact pattern found]

### Role Conflict Check
Result: PASS / FAIL
[If FAIL: describe — e.g. Builder committed, Builder self-approved]

### Safety Check
Result: PASS / FAIL
[If FAIL: describe — e.g. auto-post code found, workflow active:true]

### Importability Check (n8n workflows only)
Result: PASS / SKIP / FAIL
[If FAIL: file name and issue]

### Notes (PASS_WITH_NOTES only)
[List non-blocking observations]

### Summary
[2–3 sentences covering the overall quality and any important observations]
```

If PASS or PASS_WITH_NOTES, add:
```
OWNER CAN APPROVE
Next: Owner says "APPROVED — commit and push" to Claude Code.
Claude Code will commit with message: [suggested commit message from Builder Report]
```

If FAIL, add:
```
RETURN TO BUILDER
Issues:
1. [exact issue — file name, line if applicable, what is wrong]
2. [next issue]
Builder must fix all issues and re-submit for review.
```

---

## Checklist for ChatGPT When Filling This Template

Before delivering the review prompt to the Owner, verify:

- [ ] `[PHASE_ID]` and `[PHASE_NAME]` are filled everywhere they appear
- [ ] `[FILES_TO_REVIEW]` matches the FILES_TO_CREATE_OR_UPDATE list from the Builder prompt
- [ ] `[EXPECTED_SCOPE]` clearly states what was expected and what was excluded
- [ ] `[BLOCKERS]` includes any phase-specific blockers beyond the standard list
- [ ] `[WARNINGS]` includes any phase-specific non-blocking notes
- [ ] `[ACCEPTANCE_CRITERIA]` is copied verbatim from the Builder prompt
- [ ] `[REVIEW_OUTPUT_FORMAT]` is either left as-is (uses the default structure above) or customized with phase-specific fields
- [ ] No real API keys, tokens, or credentials appear anywhere in the review prompt
- [ ] The Builder Report from Claude Code is attached or pasted alongside this prompt
