#!/usr/bin/env node
/**
 * check-adrs.mjs — ADR standard enforcement, portable across every venture repo.
 *
 * Originally built for cinderlit-work-system/work-system/adr/; generalized so the exact
 * same file can be vendored, unmodified, into any repo's .governance/adr/ per
 * decision-engine-roadmap.md. Catches the actual drift this ecosystem has already
 * produced: free-text Status fields, renamed section headers, numbering gaps/dupes,
 * README table out of sync with the files on disk, and Superseded ADRs missing a
 * forward link. This is the enforcement layer log4brains explicitly doesn't provide
 * ("no enforced markdown structure" is its own stated design) — run it alongside
 * log4brains, not instead of it.
 *
 * WHAT IT CHECKS (per ADR-NNNN-*.md file):
 *   1. Filename matches ADR-NNNN-kebab-title.md, zero-padded, monotonic, no gaps/dupes.
 *   2. Required frontmatter fields present: Status, Date, Deciders.
 *   3. Status is EXACTLY one of: Proposed | Accepted | Superseded | Deprecated
 *      (no parenthetical riders, no free text — amendments belong in the body).
 *   4. If Status is Superseded, body must contain "Superseded by ADR-NNNN".
 *   5. Required section headers present (parenthetical qualifiers like
 *      "(proposed — not yet accepted)" are stripped before matching, so a section can
 *      still carry status-specific framing in its title as long as the canonical name
 *      is the prefix): Context, Decision, Options Considered, Trade-off Analysis,
 *      Consequences, Action Items.
 *   6. <adr-dir>/README.md's table lists every ADR file, and the Status/Date columns
 *      there match what's actually in the file (this is the #1 source of the "which
 *      one is current" confusion — the table drifts silently otherwise).
 *
 * USAGE:
 *   node check-adrs.mjs                       # defaults to ./adr relative to cwd
 *   node check-adrs.mjs --dir .governance/adr # check a specific ADR folder
 *   node check-adrs.mjs --dir adr --json      # machine-readable report
 *
 * No npm dependencies — Node >= 18, built-ins only. Run this before marking any ADR
 * Accepted, and before merging README.md changes to the ADR table (governance-preamble.md
 * DO rule 7). Cursor can wire this as a pre-commit check; Cowork can run and commit
 * directly too (known-issues.md's Cowork git-lock issue was fixed 2026-07-02).
 */

import fs from 'node:fs';
import path from 'node:path';

function argValue(flag, fallback) {
  const i = process.argv.indexOf(flag);
  return i !== -1 && process.argv[i + 1] ? process.argv[i + 1] : fallback;
}

const ADR_DIR = path.resolve(process.cwd(), argValue('--dir', 'adr'));
const README = path.join(ADR_DIR, 'README.md');

const VALID_STATUSES = ['Proposed', 'Accepted', 'Superseded', 'Deprecated'];
const REQUIRED_SECTIONS = [
  'Context',
  'Decision',
  'Options Considered',
  'Trade-off Analysis',
  'Consequences',
  'Action Items',
];
const FILENAME_RE = /^ADR-(\d{4})-([a-z0-9-]+)\.md$/;

const asJson = process.argv.includes('--json');
const errors = [];
const warnings = [];

function fail(file, msg) {
  errors.push({ file, msg });
}
function warn(file, msg) {
  warnings.push({ file, msg });
}

// --- gather files ---
const SKIP_FILES = new Set(['README.md', 'template.md']);
const allFiles = fs.readdirSync(ADR_DIR).filter((f) => !SKIP_FILES.has(f));
const adrFiles = [];

for (const f of allFiles) {
  const m = f.match(FILENAME_RE);
  if (!m) {
    fail(f, `filename doesn't match ADR-NNNN-kebab-title.md (got "${f}")`);
    continue;
  }
  adrFiles.push({ file: f, num: parseInt(m[1], 10), raw: m[1] });
}

// --- numbering: monotonic, zero-padded, no gaps/dupes ---
adrFiles.sort((a, b) => a.num - b.num);
const seen = new Map();
for (const { file, num, raw } of adrFiles) {
  if (raw.length !== 4) fail(file, `number not zero-padded to 4 digits (got "${raw}")`);
  if (seen.has(num)) fail(file, `duplicate ADR number ${num} (also used by ${seen.get(num)})`);
  seen.set(num, file);
}
const nums = adrFiles.map((a) => a.num).sort((a, b) => a - b);
for (let i = 1; i < nums.length; i++) {
  if (nums[i] !== nums[i - 1] + 1) {
    warn(README, `numbering gap between ADR-${String(nums[i - 1]).padStart(4, '0')} and ADR-${String(nums[i]).padStart(4, '0')}`);
  }
}

// --- per-file content checks ---
const fileMeta = {}; // file -> { status, date }

for (const { file } of adrFiles) {
  const full = path.join(ADR_DIR, file);
  const text = fs.readFileSync(full, 'utf8');

  const statusMatch = text.match(/^\*\*Status:\*\*\s*(.+)$/m);
  const dateMatch = text.match(/^\*\*Date:\*\*\s*(.+)$/m);
  const decidersMatch = text.match(/^\*\*Deciders:\*\*\s*(.+)$/m);

  if (!statusMatch) fail(file, 'missing "**Status:**" field');
  if (!dateMatch) fail(file, 'missing "**Date:**" field');
  if (!decidersMatch) fail(file, 'missing "**Deciders:**" field');

  const status = statusMatch ? statusMatch[1].trim() : null;
  if (status && !VALID_STATUSES.includes(status)) {
    fail(
      file,
      `Status is "${status}" — must be exactly one of ${VALID_STATUSES.join(' | ')}. ` +
        `Riders/amendments ("with the memory-revision amendment below", etc.) belong in the ` +
        `body under Consequences or a new "## Amendments" section, not appended to Status.`
    );
  }

  if (status === 'Superseded' && !/Superseded by ADR-\d{4}/.test(text)) {
    fail(file, 'Status is Superseded but body has no "Superseded by ADR-NNNN" line');
  }

  // section headers — strip parenthetical qualifiers before matching
  const headers = [...text.matchAll(/^##\s+(.+)$/gm)].map((m) => m[1].replace(/\s*\(.*?\)\s*$/, '').trim());
  for (const req of REQUIRED_SECTIONS) {
    if (!headers.includes(req)) {
      fail(file, `missing required section "## ${req}" (found: ${headers.join(', ') || 'none'})`);
    }
  }

  fileMeta[file] = { status, date: dateMatch ? dateMatch[1].trim() : null };
}

// --- README table sync ---
if (!fs.existsSync(README)) {
  fail('README.md', 'adr/README.md does not exist');
} else {
  const readmeText = fs.readFileSync(README, 'utf8');
  const rowRe = /\[(\d{4})\]\([^)]+\)\s*\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|/g;
  const readmeRows = new Map();
  let rm;
  while ((rm = rowRe.exec(readmeText))) {
    readmeRows.set(rm[1], { title: rm[2].trim(), status: rm[3].trim(), date: rm[4].trim() });
  }

  for (const { file, num, raw } of adrFiles) {
    const row = readmeRows.get(raw);
    if (!row) {
      fail('README.md', `ADR-${raw} (${file}) has no row in the README table`);
      continue;
    }
    const meta = fileMeta[file];
    if (meta.status && row.status !== meta.status) {
      fail(
        'README.md',
        `ADR-${raw} table Status says "${row.status}" but file says "${meta.status}"`
      );
    }
    if (meta.date && row.date !== meta.date) {
      fail('README.md', `ADR-${raw} table Date says "${row.date}" but file says "${meta.date}"`);
    }
  }

  for (const raw of readmeRows.keys()) {
    if (!adrFiles.some((a) => a.raw === raw)) {
      fail('README.md', `README table lists ADR-${raw} but no matching file exists in adr/`);
    }
  }
}

// --- report ---
if (asJson) {
  console.log(JSON.stringify({ errors, warnings }, null, 2));
} else {
  if (errors.length === 0 && warnings.length === 0) {
    console.log(`✓ ${adrFiles.length} ADRs checked in ${ADR_DIR} — no issues.`);
  } else {
    if (errors.length) {
      console.log(`✗ ${errors.length} error(s):`);
      for (const e of errors) console.log(`  [${e.file}] ${e.msg}`);
    }
    if (warnings.length) {
      console.log(`⚠ ${warnings.length} warning(s):`);
      for (const w of warnings) console.log(`  [${w.file}] ${w.msg}`);
    }
  }
}

process.exit(errors.length > 0 ? 1 : 0);
