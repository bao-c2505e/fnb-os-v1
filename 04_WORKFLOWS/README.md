# 04_WORKFLOWS — n8n Workflow Files

This folder stores all n8n workflow JSON files.

**Phase 0 status:** No workflows created yet. Inventory documented only.

## Rules
- All workflow JSON files must be validated before committing
- Workflows are INACTIVE by default — never activate without user approval
- Each workflow file must have a corresponding entry in `workflow_inventory.md`
- Workflow IDs must be consistent between n8n instance and this repo

## File Naming Convention
```
[number]_[workflow_name]_v[version].json
```
Examples:
- `01_content_generation_v1.json`
- `02_approval_gate_v1.json`
- `03_crm_followup_v1.json`

## Workflow Import Process
1. Export from n8n as JSON
2. Remove any hardcoded credentials (replace with `{{ $env.VAR_NAME }}`)
3. Commit to this folder
4. Update `workflow_inventory.md`
5. Log in `06_HANDOFF/DECISION_LOG.md`
