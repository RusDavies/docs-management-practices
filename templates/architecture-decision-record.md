# Architecture Decision Record

## Purpose

Use this template for consequential architecture decisions: choices that affect multiple teams, data movement, security/privacy posture, operating cost, vendor lock-in, resilience, integration strategy, platform direction, or long-term maintainability.

Use the smallest useful record. If the decision is local, reversible, and low risk, do not summon the paperwork kraken.

## Decision Summary

| Field | Value |
| --- | --- |
| Decision ID | ADR-001 |
| Title |  |
| Date |  |
| Status | Proposed / Approved / Approved with conditions / Rejected / Superseded / Retired |
| Decision owner |  |
| Accountable business owner |  |
| Technical owner |  |
| Architecture reviewer(s) |  |
| Affected product/service/capability |  |
| Related capability / operating model |  |
| Review date / trigger |  |

## Context

What problem, constraint, opportunity, or risk requires an architecture decision?

Include:

- business capability or outcome affected
- current-state problem
- target-state need
- users/customers/stakeholders affected
- systems, data domains, platforms, vendors, and teams affected
- constraints: time, cost, regulation, security, operations, vendor, skills, existing commitments

## Decision Needed

State the decision plainly.

Example:

> Decide whether customer-event processing should use synchronous API calls, asynchronous events, or batch integration for the first production release.

## Options Considered

| Option | Summary | Benefits | Costs / Risks | Reversibility | Notes |
| --- | --- | --- | --- | --- | --- |
| Option A |  |  |  | High / Medium / Low |  |
| Option B |  |  |  | High / Medium / Low |  |
| Option C |  |  |  | High / Medium / Low |  |

## Evaluation Criteria

| Criterion | Weight / Importance | Notes |
| --- | --- | --- |
| Business fit | High / Medium / Low |  |
| Customer/stakeholder impact | High / Medium / Low |  |
| Security/privacy/compliance | High / Medium / Low |  |
| Reliability/resilience | High / Medium / Low |  |
| Operability/supportability | High / Medium / Low |  |
| Data ownership/quality | High / Medium / Low |  |
| Integration complexity | High / Medium / Low |  |
| Cost | High / Medium / Low |  |
| Delivery speed | High / Medium / Low |  |
| Reversibility | High / Medium / Low |  |
| Vendor/platform lock-in | High / Medium / Low |  |

## Recommended Decision

Recommended option:

Rationale:

Why this is the right decision now:

Why this is the minimum necessary architecture decision:

## Tradeoffs

What do we gain?

- 

What do we give up or accept?

- 

What remains uncertain?

- 

What would cause us to revisit this decision?

- 

## Operating Model Impact

| Area | Impact / Decision |
| --- | --- |
| Capability owner |  |
| Day-to-day operator |  |
| Support model |  |
| Incident owner/path |  |
| Data owner |  |
| Security/privacy/control owner |  |
| Cost owner |  |
| Vendor/platform owner |  |
| Lifecycle/retirement owner |  |

## Risk and Controls

| Risk | Impact | Mitigation / Control | Owner | Review Trigger |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Decision

Decision made:

Approved by:

Date:

Conditions:

Rejected options and why:

## Follow-Up Actions

| Action | Owner | Due Date | Evidence / Notes |
| --- | --- | --- | --- |
|  |  |  |  |

## Related Records

- Capability map / planning record:
- Operating model blueprint:
- 4+1 architecture view worksheet:
- Production-readiness checklist:
- Risk register:
- Technical debt register:
- Prior/superseded ADRs:

## Review / Retirement

When should this decision be reviewed, superseded, or retired?

Review trigger examples:

- scale changes materially
- vendor/provider changes
- cost changes materially
- incidents expose weakness
- regulation/security posture changes
- business capability or operating model changes
- better evidence invalidates assumptions

## Related Guidance

- [Architecture Management](https://github.com/RusDavies/docs-management-practices/blob/master/disciplines/ARCHITECTURE_MANAGEMENT.md)
- [Risk Management](https://github.com/RusDavies/docs-management-practices/blob/master/disciplines/RISK_MANAGEMENT.md)
- [Technical Debt Management](https://github.com/RusDavies/docs-management-practices/blob/master/disciplines/TECHNICAL_DEBT_MANAGEMENT.md)
- [Decision Record](https://github.com/RusDavies/docs-management-practices/blob/master/templates/decision-record.md)

## Usage Notes

- Use for consequential decisions, not every small implementation choice.
- Keep the record short enough that future teams will actually read it.
- Capture rejected options and tradeoffs; they are often more useful later than the winning answer.
- Add a review trigger when the decision depends on assumptions that may expire.

## Example

For choosing event streaming over synchronous APIs, record affected capabilities, options, criteria, recommended decision, operational consequences, security/data implications, and what would trigger reconsideration.
