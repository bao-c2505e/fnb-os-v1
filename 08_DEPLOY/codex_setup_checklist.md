# OpenAI Codex Setup Checklist

## Note
As of 2024, Codex capabilities are integrated into GPT-4o via the OpenAI API.
There is no separate Codex API key — it reuses `OPENAI_API_KEY`.

## Setup

- [ ] OpenAI API key already configured (see `openai_setup_checklist.md`)
- [ ] Model for code tasks: `gpt-4o` (includes Codex-level code generation)
- [ ] Model for smaller code tasks: `gpt-4o-mini`

## Usage in FnB OS V1

Codex (via GPT-4o) is used for:
- Generating n8n workflow JSON
- Writing Python/JavaScript helper scripts
- Debugging workflow logic
- Schema validation scripts

## Claude Code CLI as Alternative

Claude Code (via Anthropic) is also available as a Builder Agent.
For file-heavy tasks (creating repo files, editing configs), Claude Code CLI is preferred.

## Test

- [ ] n8n HTTP Request to OpenAI API with code generation prompt
- [ ] Confirm code output is valid JSON / Python / JavaScript
