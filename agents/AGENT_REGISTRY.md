# Agent Registry

Created By: Codex (Builder) - 2026-05-26

| ID | Agent | Role | May Do | Must Not Do |
| --- | --- | --- | --- | --- |
| USER | User | Owner and final approver | Approve phases, external actions, publishing, spending | None |
| AGT-01 | ChatGPT | Chief Architect | Write phase specs, task contracts, review decisions | Execute repo changes or bypass user approval |
| AGT-02 | Claude | Builder Agent | Edit repo files, build docs/schemas/scripts, run local checks | Hardcode secrets, auto-post, auto-reply, activate workflows |
| AGT-03 | Codex | Code Reviewer / Fixer / Script Worker | Review diffs, patch scoped issues, run validation | Open scope beyond assigned task |
| AGT-04 | Gemini | Content and multimodal agent | Draft content, prompts, design briefs from approved inputs | Publish or message customers directly |
| AGT-05 | n8n | Automation runtime | Route tasks, run manual/scheduled workflows after approval | Make approval decisions or self-activate |
| AGT-06 | GitHub | Repository and change log | Store versioned source, PRs, commits, issues | Store real API keys, tokens, or passwords |

All agents must follow `docs/agent-system/OPERATING_RULES.md`.
