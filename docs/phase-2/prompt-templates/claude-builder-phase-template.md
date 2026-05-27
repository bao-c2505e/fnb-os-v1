# Claude Builder Phase Template

**Template Version:** 2.1
**Maintained By:** ChatGPT (Chief Architect)
**Last Updated:** 2026-05-28
**Used By:** ChatGPT when writing a new Builder prompt; Claude Code when confirming scope

This template is the standard format for all Builder phase prompts in FnB OS V1 / Vị Cuốn Growth OS.
ChatGPT fills in all placeholders before delivering the prompt to Claude Code.
Claude Code treats every field as a binding constraint — not a suggestion.

---

## How to Use This Template

1. ChatGPT copies this template and fills every `[PLACEHOLDER]`.
2. ChatGPT delivers the completed prompt to the Owner.
3. Owner pastes the completed prompt into a Claude Code session.
4. Claude Code reads every field before writing any file.
5. Claude Code states the Phase ID and scope lock in its first response.

Placeholders that are intentionally left empty must be written as `[NONE]` — never deleted.

---

---

## PHASE [PHASE_ID] — [PHASE_NAME]

You are Claude Code acting as BUILDER for FnB OS V1 / Vị Cuốn Growth OS.

### PROJECT CONTEXT

- Local repo: D:\FNB_OS_V1
- GitHub repo: https://github.com/bao-c2505e/fnb-os-v1
- Branch: main
- ChatGPT = Chief Architect
- Claude Code = Builder
- Codex = Reviewer only
- GitHub = Source of Truth

### PHASE

Phase [PHASE_ID] — [PHASE_NAME]

### GOAL

[GOAL]

One paragraph. Describe what this phase accomplishes and why it matters for Vị Cuốn / FnB OS V1.
Do not describe implementation details here — only the outcome.

### SYSTEM PRINCIPLES (apply to every phase)

- This is an AI Marketing Automation system for F&B, not only video.
- SOLO Business direction: Owner approves plans and outputs; Owner should not manually debug via screenshots/copy-paste.
- GitHub is the Source of Truth.
- Everything must go through repo files: markdown, schemas, importable workflow JSON, logs, handoff, approval gates.
- No hardcoded API keys, tokens, passwords, credentials, or secrets.
- Do not commit .claude/.
- Every agent session should stay short. At turn 8 of 10, update SESSION_SUMMARY.md and report remaining turns.

### SCOPE

[SCOPE]

Describe what this phase covers in 2–5 sentences.
Be explicit about what is in scope AND what is explicitly out of scope for this phase.

### FILES TO CREATE OR UPDATE

[FILES_TO_CREATE_OR_UPDATE]

List every file. Use exact repo-relative paths.

```
- docs/phase-X/file-name.md  (CREATE)
- docs/phase-X/another-file.md  (UPDATE — describe what changes)
- schemas/example-schema.json  (CREATE)
```

No file outside this list may be created or modified.
If Claude Code discovers it needs a file not listed here, it must stop and report — not proceed.

### DO NOT TOUCH

[DO_NOT_TOUCH]

List files, directories, or categories that must not be modified.

```
- Do not edit .env or any credential file.
- Do not add secrets.
- Do not create n8n production workflows.
- Do not add runnable automation that posts, replies to customers, or runs ads.
- Do not commit .claude/.
- Do not make broad unrelated refactors.
- [add phase-specific restrictions here]
```

### ACCEPTANCE CRITERIA

[ACCEPTANCE_CRITERIA]

Every item will be evaluated as PASS or FAIL by both Builder (self-check) and Reviewer (Codex).

```
Phase [PHASE_ID] is complete when:
- [ ] [Criterion 1 — specific and verifiable]
- [ ] [Criterion 2]
- [ ] [Criterion 3]
- [ ] No secret/API key/token/password is present in any scoped file.
- [ ] .claude/ is not staged or committed.
- [ ] No production n8n workflow is created.
- [ ] No auto-post, auto-reply, or ads execution code is present.
- [ ] All scoped files are non-empty and specific to FnB OS V1 / Vị Cuốn brand.
```

### SELF-CHECK COMMANDS

[SELF_CHECK_COMMANDS]

Run or verify these before posting the Builder Report.

```
# Confirm only scoped files are modified
git status --short

# Confirm .claude/ is not staged
git status --short | grep ".claude"
# Expected output: nothing (empty)

# Scan for secret patterns
grep -r "api_key\|token\|password\|secret\|sk-\|xox\|AIza\|ghp_\|ya29\." [scope_directory]
# Expected output: nothing (empty), or only placeholder text like [YOUR_API_KEY]

# Confirm no scoped file is empty
# Manually verify each file in FILES_TO_CREATE_OR_UPDATE has substantive content
```

### FINAL REPORT FORMAT

[FINAL_REPORT_FORMAT]

When done, report in this exact structure — no deviation:

```
PHASE [PHASE_ID] BUILDER REPORT

1. Status
   - DONE / NEEDS_FIX / BLOCKED

2. Files created/updated
   - [list with paths]

3. What changed
   - [short bullet summary per file]

4. Safety check
   - Secrets: PASS/FAIL
   - .claude staged: NO/YES
   - Production n8n workflow: NO/YES
   - Auto-post/auto-reply/ads execution: NO/YES

5. Scope check
   - In scope: YES/NO
   - Files outside scope: NONE / [list]

6. Acceptance criteria
   | # | Criterion | Status |
   |---|-----------|--------|
   | 1 | [text] | PASS/FAIL |

7. Suggested commit message
   - feat(phase-[PHASE_ID]): [short description]

8. Ready for Codex review?
   - YES/NO
```

**IMPORTANT:** Do not commit until the Owner explicitly says "APPROVED — commit and push" after Codex review.

---

## Checklist for ChatGPT When Filling This Template

Before delivering the prompt to the Owner, verify:

- [ ] `[PHASE_ID]` is filled everywhere it appears (at least 5 occurrences)
- [ ] `[PHASE_NAME]` is filled
- [ ] `[GOAL]` is one clear paragraph, outcome-focused
- [ ] `[SCOPE]` distinguishes what IS and IS NOT in scope
- [ ] `[FILES_TO_CREATE_OR_UPDATE]` lists exact paths with CREATE/UPDATE labels
- [ ] `[DO_NOT_TOUCH]` includes phase-specific restrictions beyond the standard list
- [ ] `[ACCEPTANCE_CRITERIA]` items are specific and verifiable — not vague
- [ ] `[SELF_CHECK_COMMANDS]` includes commands relevant to this phase's file types
- [ ] `[FINAL_REPORT_FORMAT]` is either left as-is (uses the default structure above) or customized with phase-specific fields
- [ ] No placeholder text (`[FILL]`, `[TODO]`, `[PLACEHOLDER]`) remains in the final prompt
- [ ] No real API keys, tokens, or credentials appear anywhere in the prompt
