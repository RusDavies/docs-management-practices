# Code Review Guidelines

## Purpose

Set practical expectations for code review so reviews improve correctness, maintainability, knowledge sharing, security, and product-process evidence without becoming dominance theatre in diff form.

## Scope

- Team / repository:
- Guideline owner:
- Effective date:
- Review cadence:

## Review Goals

| Goal | What reviewers should look for | Evidence / notes |
| --- | --- | --- |
| Correctness | Requirement fit, edge cases, error handling |  |
| Maintainability | Clarity, structure, naming, coupling, comments for non-obvious choices |  |
| Test coverage | Unit/integration/regression/security tests where relevant |  |
| Security / privacy | Input validation, authorization, secrets, logging, data exposure |  |
| Operability | Logs, metrics, failure modes, config, rollback/readiness implications |  |
| Product-process alignment | Required docs, ADRs, QA notes, release/security evidence updated |  |
| AI-assisted work | Generated code understood, reviewed, tested, and provenance/evidence captured where needed |  |

## Review Norms

| Norm | Agreement |
| --- | --- |
| Required reviewers / approvals |  |
| When design review is required before PR review |  |
| Expected response time |  |
| Blocking vs non-blocking comments |  |
| Handling urgent fixes |  |
| Handling style preferences |  |
| Recording accepted risk or follow-up debt |  |

## Author Checklist

- Change is scoped and understandable:
- Tests / checks run:
- Security/privacy considerations addressed:
- Documentation updated where needed:
- Operational/release impact noted:
- AI assistance disclosed if project policy requires it:
- Follow-up debt or accepted risk recorded:

## Usage Notes

- Code review is not a substitute for design review, QA, release approval, or security risk acceptance.
- Review risky changes more deeply than routine changes. Equal ceremony for everything is how important signals become wallpaper.
- Keep comments about the code, evidence, and decision — not about the author’s worth as a mammal.

## Example

A pull request changing authorization logic may require security-focused review, explicit tests for allowed and denied roles, audit-log checks, release-security-gate evidence, and a linked design or decision note if permissions changed materially.
