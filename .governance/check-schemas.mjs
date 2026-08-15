#!/usr/bin/env node
/**
 * check-schemas.mjs — structural validation of the published JSON Schemas.
 *
 * WHY THIS EXISTS, AND WHAT IT DELIBERATELY DOES NOT DO.
 *
 * stewardship-standard is the public, DOI'd artifact — three releases, a Zenodo record, an open
 * licence — and until 2026-08-14 it had no CI and no test of any kind. It publishes 16 schemas
 * that other repos are invited to validate against. Nothing checked that those schemas were
 * themselves well-formed, that their internal `$ref`s pointed at anything, or that a release
 * hadn't shipped a JSON syntax error. That is a worse gap than a missing unit test: a broken
 * schema is a defect the standard exports to every implementer.
 *
 * WHAT IT CHECKS (all provable without a JSON Schema engine, hence zero dependencies):
 *   S1  every .json file in schemas/ and samples/ parses
 *   S2  every schema declares a `$schema` draft, and they all declare the SAME one — a repo that
 *       silently mixes draft-07 and 2020-12 breaks validators in ways that look like data bugs
 *   S3  every schema declares `$id` and `title`
 *   S4  every `$id` is unique across the schema set
 *   S5  every local `$ref` (a `#/...` pointer or a relative file path) resolves to something that
 *       actually exists — file present, and for a JSON-pointer, the path present inside the target
 *   S6  every `required` entry names a property the schema actually declares. This is the one that
 *       catches real drift: rename a property, forget the `required` list, and every validator
 *       starts rejecting valid documents while the schema still looks correct to a reader.
 *
 * WHAT IT DOES NOT CHECK, STATED SO THE COVERAGE IS NOT OVERREAD:
 *   - It does NOT validate samples/ against schemas/. That is the check most worth having and it
 *     is not written here, because the mapping does not exist yet: no sample declares `$schema`,
 *     and two of the five are COMPOSITE documents (charter-template-and-instance.json holds
 *     `contexts` + `assignments` arrays; escalation-outbox-entry.json wraps an
 *     `escalation_outbox` array). Deciding which schema governs which fragment is a spec decision
 *     for Caitlin, not something to guess at in a linter. Filed rather than faked — a validator
 *     asserting a mapping nobody ruled on would be worse than the current absence, because it
 *     would read as coverage.
 *   - It does NOT run a JSON Schema engine. ajv needs `ajv-formats` for the `date-time` format
 *     these schemas use, which means a package.json, a lockfile and node_modules in a repo that
 *     currently has none. Worth doing; a separate decision.
 *
 * Exit 1 on any S1–S6 failure. No network, no deps, no sibling repos.
 */

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const errors = [];
const err = (m) => errors.push(m);

function walk(dir) {
  if (!fs.existsSync(dir)) return [];
  return fs.readdirSync(dir, { withFileTypes: true }).flatMap((e) => {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) return walk(p);
    return e.name.endsWith('.json') ? [p] : [];
  });
}

const schemaFiles = walk(path.join(ROOT, 'schemas'));
const sampleFiles = walk(path.join(ROOT, 'samples'));
const rel = (p) => path.relative(ROOT, p);

if (schemaFiles.length === 0) err('no schemas found under schemas/ — this check would pass vacuously');

// ── S1: everything parses ────────────────────────────────────────────────────
const parsed = new Map();
for (const f of [...schemaFiles, ...sampleFiles]) {
  try {
    parsed.set(f, JSON.parse(fs.readFileSync(f, 'utf8')));
  } catch (e) {
    err(`S1 ${rel(f)}: does not parse — ${e.message}`);
  }
}

// ── S2/S3/S4: draft consistency, identity, uniqueness ────────────────────────
const drafts = new Set();
const ids = new Map();
for (const f of schemaFiles) {
  const s = parsed.get(f);
  if (!s) continue;
  if (!s.$schema) err(`S2 ${rel(f)}: no $schema — the draft a validator should use is unstated`);
  else drafts.add(s.$schema);
  if (!s.$id) err(`S3 ${rel(f)}: no $id`);
  if (!s.title) err(`S3 ${rel(f)}: no title`);
  if (s.$id) {
    if (ids.has(s.$id)) err(`S4 duplicate $id "${s.$id}" in ${rel(f)} and ${rel(ids.get(s.$id))}`);
    else ids.set(s.$id, f);
  }
}
if (drafts.size > 1) {
  err(`S2 schemas declare ${drafts.size} different drafts (${[...drafts].join(', ')}) — mixed drafts break validators in ways that present as data bugs`);
}

// ── S5/S6: refs resolve, required names declared properties ──────────────────
function pointerExists(doc, pointer) {
  // pointer is the part after '#', e.g. "/definitions/Foo"
  if (pointer === '' || pointer === '/') return true;
  let cur = doc;
  for (const rawSeg of pointer.split('/').slice(1)) {
    const seg = rawSeg.replace(/~1/g, '/').replace(/~0/g, '~');
    if (cur === null || typeof cur !== 'object' || !(seg in cur)) return false;
    cur = cur[seg];
  }
  return true;
}

function checkNode(node, file, trail) {
  if (node === null || typeof node !== 'object') return;
  if (Array.isArray(node)) {
    node.forEach((v, i) => checkNode(v, file, `${trail}/${i}`));
    return;
  }

  if (typeof node.$ref === 'string') {
    const ref = node.$ref;
    // Skip absolute refs to other hosts — those are the standard's own published URLs and
    // resolving them would make this check depend on the network.
    if (!/^https?:\/\//.test(ref)) {
      const [filePart, pointerPart = ''] = ref.split('#');
      if (filePart === '') {
        if (!pointerExists(parsed.get(file), pointerPart)) {
          err(`S5 ${rel(file)} ${trail}: $ref "${ref}" — no such path in this schema`);
        }
      } else {
        const target = path.resolve(path.dirname(file), filePart);
        if (!fs.existsSync(target)) {
          err(`S5 ${rel(file)} ${trail}: $ref "${ref}" — target file does not exist`);
        } else if (pointerPart && parsed.has(target) && !pointerExists(parsed.get(target), pointerPart)) {
          err(`S5 ${rel(file)} ${trail}: $ref "${ref}" — file exists but has no such path`);
        }
      }
    }
  }

  if (Array.isArray(node.required) && node.properties && typeof node.properties === 'object') {
    for (const key of node.required) {
      if (typeof key === 'string' && !(key in node.properties)) {
        err(`S6 ${rel(file)} ${trail}: required names "${key}", which this schema does not declare as a property`);
      }
    }
  }

  for (const [k, v] of Object.entries(node)) checkNode(v, file, `${trail}/${k}`);
}

for (const f of schemaFiles) if (parsed.get(f)) checkNode(parsed.get(f), f, '#');

// ── report ───────────────────────────────────────────────────────────────────
if (errors.length) {
  console.error(`\n✗ check-schemas: ${errors.length} error(s)\n`);
  for (const e of errors) console.error(`  ${e}`);
  console.error('');
  process.exit(1);
}
console.log(
  `✓ check-schemas: ${schemaFiles.length} schemas + ${sampleFiles.length} samples — parse, identity, refs and required all clean.`
);
console.log('  NOT covered: samples are not validated against schemas (no mapping ruled yet — see header).');
