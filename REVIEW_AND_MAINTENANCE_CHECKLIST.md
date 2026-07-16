# Review and Maintenance Checklist

## Purpose

Use this checklist to maintain this Git-backed Markdown documentation repository as a coherent, navigable, publication-safe guidance set.

## Per-Change Checklist

Before merging a meaningful change:

- [ ] Change is scoped to a branch.
- [ ] Affected documents have clear headings and purpose.
- [ ] New files are linked from `README.md` where appropriate.
- [ ] New files are linked from `DOCUMENT_MAP.md` where appropriate.
- [ ] Related audience or discipline guides are cross-linked.
- [ ] GitHub links use the expected base URL where public navigation matters.
- [ ] Sensitive sections are marked and gated.
- [ ] TODO/backlog is updated.
- [ ] `git diff --check` passes.

## Navigation Review

Periodically check:

- [ ] `README.md` includes all major docs.
- [ ] `DOCUMENT_MAP.md` includes all major docs, discipline guides, and templates.
- [ ] Audience guides link to relevant discipline guides.
- [ ] Discipline guides link to relevant templates and audience guides where useful.
- [ ] No useful document is orphaned.
- [ ] No README/document-map link points to a missing file.

## Content Quality Review

For each guide, check:

- [ ] Purpose is clear.
- [ ] Audience/scope is clear.
- [ ] Guidance is practical, not abstract leadership vapour.
- [ ] Anti-patterns are named plainly.
- [ ] Disagree-and-commit implications are included where relevant.
- [ ] Artifacts/templates are referenced where useful.
- [ ] Examples are human and engaging without creating stereotype problems.
- [ ] Claims are proportionate and supported when needed.

## Publication Safety Review

Before public or employment-facing use:

- [ ] Run `templates/publication-review-checklist.md`.
- [ ] Review `WRITING_STYLE_GUIDANCE.md`.
- [ ] Review `PUBLICATION_DECISION_GATES.md`.
- [ ] Check sensitive content involving DEI, demographics, hiring, protected characteristics, legal, HR, or employment-market claims.
- [ ] Check examples for aggregate representation patterns.
- [ ] Remove or revise content that could be read as hostile, resentful, discriminatory, or needlessly culture-war coded.

## Source, Copyright, and Originality Review

Before public release:

- [ ] Review `SOURCE_AND_PERMISSIONS_REGISTER.md`.
- [ ] Confirm substantial third-party influences are tracked.
- [ ] Confirm no copied/proprietary diagrams, tables, or text are included without permission.
- [ ] Confirm AI-assisted material has been reviewed for originality and factual correctness.
- [ ] Confirm material AI-assisted drafting, review, synthesis, repository maintenance, or decision support is captured in the [AI Use Register](templates/ai-use-register.md) when required.
- [ ] Confirm AI-use disclosure decisions are recorded for publication-sensitive material.
- [ ] Confirm factual/sensitive claims are sourced or removed.

## Maintenance Cadence

Suggested cadence:

- after each meaningful work item: per-change checklist
- monthly during active development: navigation and TODO review
- before public release: full publication, source, and originality review
- after publication: collect errata, feedback, and revision backlog

## Lightweight Link Check

Until an automated checker exists, use manual checks:

- [ ] every file listed in README exists locally
- [ ] every file listed in DOCUMENT_MAP exists locally
- [ ] every new local file appears in at least one navigation document
- [ ] every GitHub URL uses `https://github.com/RusDavies/docs-management-practices/blob/master/`

Future improvement: add a script to verify Markdown links and orphaned docs automatically, because humans are bad regex engines with snacks.
