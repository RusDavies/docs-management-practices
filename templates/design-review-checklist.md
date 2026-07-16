# Design Review Checklist

## Purpose

Review consequential software design decisions before expensive commitments become production facts with invoices, users, and incident potential.

## Review Context

- Design / change name:
- Review owner:
- Date:
- Product / system:
- Related product-process artifact: architecture note / ADR / requirements / security review / other
- Decision needed:

## Scope and Alternatives

| Question | Answer / evidence |
| --- | --- |
| What problem is this design solving? |  |
| What is in scope and out of scope? |  |
| What alternatives were considered? |  |
| Why is the proposed option preferred? |  |
| What assumptions must hold? |  |
| What would cause us to revisit this decision? |  |

## Review Checklist

| Area | Check | Status | Evidence / notes | Owner |
| --- | --- | --- | --- | --- |
| Product fit | Requirements and user/customer impact are understood |  |  |  |
| Architecture | Boundaries, components, data model, and integration contracts are clear |  |  |  |
| Security / privacy | Trust boundaries, authz/authn, secrets, data exposure, and abuse cases are addressed |  |  |  |
| Operability | Health, logs, metrics, alerts, runbooks, and recovery path are considered |  |  |  |
| Reliability | Failure modes, retries, idempotency, rollback, and graceful degradation are addressed |  |  |  |
| QA / testability | Test strategy, environments, regression risk, and acceptance evidence are defined |  |  |  |
| Compliance / governance | Required approvals, accepted risks, and evidence paths are identified |  |  |  |
| AI / automation | Agent/tool permissions, data exposure, approvals, and audit trails are bounded where relevant |  |  |  |
| Lifecycle | Migration, versioning, compatibility, maintenance, and retirement path are understood |  |  |  |

## Decision Record

- Decision:
- Conditions / constraints:
- Risks accepted:
- Follow-up actions:
- Approver / decision owner:
- Record location:

## Usage Notes

- Trigger review for new services, data model changes, auth/permission changes, external integrations, AI tool/action risk, high-availability paths, or hard-to-reverse choices.
- Do not use design review as taste enforcement. Use it to expose tradeoffs, evidence, and ownership.
- Link to `docs-software-product-process` architecture, security, QA, and governance guidance when the work is a software product.

## Example

A new customer-data export feature should review data scope, authorization, audit events, file expiry, privacy deletion behavior, abuse cases, performance limits, support path, and rollback before implementation commits to the design.
