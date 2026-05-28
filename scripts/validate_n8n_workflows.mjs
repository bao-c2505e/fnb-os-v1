#!/usr/bin/env node
/**
 * Phase 9 — Static n8n Workflow Validator
 * FnB OS V1 / Vị Cuốn Growth OS
 *
 * Runs static structural checks on Phase 8 n8n workflow skeleton JSON files.
 * DOES NOT execute workflows, connect to external services, or read live credentials.
 * Safe to run on any machine with Node.js >= 16.
 *
 * Usage:   node scripts/validate_n8n_workflows.mjs
 * Output:  Console report with PASS/FAIL per check + summary
 * Exit:    0 = all checks pass, 1 = one or more checks fail
 *
 * If Node.js is not available, perform checks manually using:
 *   docs/checklists/PHASE_9_N8N_IMPORT_CHECKLIST.md
 */

import { readFileSync, existsSync } from 'fs';
import { resolve, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = resolve(__dirname, '..');

// Expected workflow files — all 6 Phase 8 skeletons
const WORKFLOW_FILES = [
  'n8n/workflows/content_auto_skeleton.json',
  'n8n/workflows/creative_asset_auto_skeleton.json',
  'n8n/workflows/ads_pack_auto_skeleton.json',
  'n8n/workflows/crm_followup_auto_skeleton.json',
  'n8n/workflows/comment_inbox_reply_assistant_skeleton.json',
  'n8n/workflows/approval_publishing_skeleton.json',
];

// Real secret patterns that must NOT appear in workflow files.
// REPLACE_WITH_* placeholders are allowed — these patterns detect actual leaked secrets.
const FORBIDDEN_SECRET_PATTERNS = [
  { label: 'Anthropic API key (sk-ant-)',  pattern: /sk-ant-[a-zA-Z0-9\-_]{20,}/ },
  { label: 'OpenAI API key (sk-)',          pattern: /\bsk-[a-zA-Z0-9]{40,}\b/ },
  { label: 'Private key block',             pattern: /-----BEGIN (RSA |EC |OPENSSH |)PRIVATE KEY-----/ },
  { label: 'GitHub PAT (ghp_)',             pattern: /ghp_[a-zA-Z0-9]{36}/ },
  { label: 'JWT token (eyJhbGciOi…)',       pattern: /eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9\.[a-zA-Z0-9\-_]+\.[a-zA-Z0-9\-_]+/ },
  { label: 'Telegram bot token',            pattern: /\b[0-9]{9,10}:[a-zA-Z0-9_\-]{35}\b/ },
  { label: 'Google service account key',    pattern: /"type"\s*:\s*"service_account"/ },
];

// Node types required in every workflow
const REQUIRED_NODE_TYPES = [
  { type: 'n8n-nodes-base.errorTrigger', label: 'Error Trigger node' },
  { type: 'n8n-nodes-base.stickyNote',   label: 'Sticky Note (safety warning) node' },
];

let totalPass = 0;
let totalFail = 0;
const allResults = [];

function check(label, pass, detail) {
  if (pass) totalPass++; else totalFail++;
  return { label, pass, detail: detail || '' };
}

// ─── Header ───────────────────────────────────────────────────────────────────

console.log('');
console.log('╔═══════════════════════════════════════════════════════════╗');
console.log('║  FnB OS V1 — Phase 9 Static Workflow Validator            ║');
console.log('║  STATIC ANALYSIS ONLY — No workflows executed             ║');
console.log('╚═══════════════════════════════════════════════════════════╝');
console.log(`  Root:  ${ROOT}`);
console.log(`  Date:  ${new Date().toISOString()}`);
console.log(`  Files: ${WORKFLOW_FILES.length} expected\n`);

// ─── Check each workflow file ─────────────────────────────────────────────────

for (const relPath of WORKFLOW_FILES) {
  const filePath = resolve(ROOT, relPath);
  const checks = [];

  // 1 — File exists
  const fileExists = existsSync(filePath);
  checks.push(check('File exists', fileExists, fileExists ? '' : `Not found: ${filePath}`));

  if (!fileExists) {
    allResults.push({ file: relPath, checks });
    continue;
  }

  const rawContent = readFileSync(filePath, 'utf-8');

  // 2 — Valid JSON
  let workflow = null;
  try {
    workflow = JSON.parse(rawContent);
    checks.push(check('Valid JSON', true));
  } catch (err) {
    checks.push(check('Valid JSON', false, err.message));
    allResults.push({ file: relPath, checks });
    continue;
  }

  // 3 — active === false (hard requirement — must never be true in skeleton)
  checks.push(check(
    'active: false',
    workflow.active === false,
    workflow.active !== false ? `FAIL — active is: ${JSON.stringify(workflow.active)}` : ''
  ));

  // 4 — Workflow has a name
  const hasName = typeof workflow.name === 'string' && workflow.name.length > 0;
  checks.push(check('Has workflow name', hasName, hasName ? '' : 'name field missing or empty'));

  // 5 — Name contains [SKELETON] — safety label
  const hasSkeleton = typeof workflow.name === 'string' && workflow.name.includes('[SKELETON]');
  checks.push(check(
    'Name contains [SKELETON]',
    hasSkeleton,
    hasSkeleton ? '' : `Name is: "${workflow.name}"`
  ));

  // 6 — Has non-empty nodes array
  const hasNodes = Array.isArray(workflow.nodes) && workflow.nodes.length > 0;
  checks.push(check('Has nodes array (non-empty)', hasNodes, hasNodes ? '' : 'nodes missing or empty'));

  if (hasNodes) {
    // 7 — Required node types
    for (const req of REQUIRED_NODE_TYPES) {
      const found = workflow.nodes.some(n => n.type === req.type);
      checks.push(check(
        `Has ${req.label}`,
        found,
        found ? '' : `No node of type "${req.type}" found in nodes array`
      ));
    }
  }

  // 8 — Secret scan (raw content — catches any interpolated value)
  for (const { label, pattern } of FORBIDDEN_SECRET_PATTERNS) {
    const found = pattern.test(rawContent);
    checks.push(check(
      `Secret scan: no ${label}`,
      !found,
      found ? `SECURITY ALERT — Pattern matched for: ${label}` : ''
    ));
  }

  // 9 — versionId is a placeholder, not a real UUID
  const vId = workflow.versionId;
  const vIdSafe = !vId || typeof vId !== 'string' || vId.startsWith('REPLACE_WITH');
  checks.push(check(
    'versionId is placeholder (not real UUID)',
    vIdSafe,
    vIdSafe ? '' : `versionId value: "${vId}"`
  ));

  // 10 — instanceId is a placeholder, not a real instance ID
  const iId = workflow?.meta?.instanceId;
  const iIdSafe = !iId || typeof iId !== 'string' || iId.startsWith('REPLACE_WITH');
  checks.push(check(
    'instanceId is placeholder (not real)',
    iIdSafe,
    iIdSafe ? '' : `instanceId value: "${iId}"`
  ));

  allResults.push({ file: relPath, checks });
}

// ─── Print per-file results ────────────────────────────────────────────────────

console.log('─── Check Results ───────────────────────────────────────────\n');

for (const { file, checks } of allResults) {
  const filePassed = checks.every(c => c.pass);
  const fileLabel = filePassed ? 'PASS' : 'FAIL';
  console.log(`  [${fileLabel}] ${file}`);
  for (const { label, pass, detail } of checks) {
    const icon = pass ? '✓' : '✗';
    const status = pass ? 'PASS' : 'FAIL';
    console.log(`         ${icon} ${status.padEnd(4)}  ${label}`);
    if (detail) {
      console.log(`                └─ ${detail}`);
    }
  }
  console.log('');
}

// ─── Summary ─────────────────────────────────────────────────────────────────

const allPass = totalFail === 0;
console.log('─── Summary ─────────────────────────────────────────────────');
console.log(`  Files checked : ${WORKFLOW_FILES.length}`);
console.log(`  Total checks  : ${totalPass + totalFail}`);
console.log(`  PASS          : ${totalPass}`);
console.log(`  FAIL          : ${totalFail}`);
console.log(`  Overall       : ${allPass ? 'ALL PASS — safe for import review' : 'FAILURES FOUND — review details above'}`);
console.log('');
console.log('  NOTE: Static analysis only. No workflows executed.');
console.log('        No external services contacted.');
console.log('        No credentials read or modified.');
console.log('        For manual import validation, use:');
console.log('        docs/checklists/PHASE_9_N8N_IMPORT_CHECKLIST.md');
console.log('');

process.exit(allPass ? 0 : 1);
