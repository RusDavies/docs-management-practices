# Architecture Framing Checklist

## Purpose

Use this checklist early in discovery or intake to decide how much architecture attention a change needs.

The goal is not to slow every team down. The goal is to identify consequential decisions early enough that teams can make them deliberately instead of discovering them later in production, where everything is louder and worse dressed.

## Framing Summary

| Field | Value |
| --- | --- |
| Initiative / capability |  |
| Request ID / reference |  |
| Business owner |  |
| Product/service owner |  |
| Technical owner |  |
| Architecture contact |  |
| Date |  |
| Lifecycle stage | Idea / Discovery / Delivery / Production change / Retirement |
| Recommended architecture depth | None / Light review / Framing workshop / Formal review / Architecture decision record required |

## Problem and Outcome

| Question | Answer |
| --- | --- |
| What problem or opportunity is being addressed? |  |
| What business capability is created or changed? |  |
| What outcome should improve? |  |
| Who are the users/customers/stakeholders? |  |
| What happens if this work does not happen? |  |

## Scope and Change Type

| Question | Answer |
| --- | --- |
| Is this a local change or system-shaping decision? | Local / System-shaping / Unknown |
| Is it reversible? | High / Medium / Low / Unknown |
| Is this new build, buy, integrate, reuse, replace, or retire? | Build / Buy / Integrate / Reuse / Replace / Retire / Mixed |
| Does it create or reshape a function, line of business, platform, service, or major capability? | Yes / No / Unknown |
| Does it change an operating model? | Yes / No / Unknown |

## Architecture Impact Scan

| Area | Impact? | Notes |
| --- | --- | --- |
| Multiple teams | Yes / No / Unknown |  |
| Shared platform | Yes / No / Unknown |  |
| Shared data domain | Yes / No / Unknown |  |
| Integration/API/event flow | Yes / No / Unknown |  |
| Security/trust boundary | Yes / No / Unknown |  |
| Privacy/regulatory/compliance | Yes / No / Unknown |  |
| Customer/stakeholder experience | Yes / No / Unknown |  |
| Operations/support/on-call | Yes / No / Unknown |  |
| Vendor/partner dependency | Yes / No / Unknown |  |
| Cost/capacity/scaling | Yes / No / Unknown |  |
| Resilience/recovery | Yes / No / Unknown |  |
| Technical debt/lifecycle | Yes / No / Unknown |  |

## Capability Planning Check

Use when the work creates, changes, consolidates, or retires a business capability.

| Question | Answer / Notes |
| --- | --- |
| What current capability exists today? |  |
| What target capability is needed? |  |
| Is the capability differentiating, standard, duplicated, fragile, or obsolete? |  |
| Which systems support it? |  |
| Which data domains support it? |  |
| Which teams/processes own it? |  |
| Which vendors or partners are involved? |  |
| What investment, sequencing, or retirement decision is needed? |  |

## Operating Model Check

Use when the architecture creates or changes real work, ownership, support, controls, or operating flow.

| Question | Answer / Notes |
| --- | --- |
| Who owns the capability? |  |
| Who performs the work day to day? |  |
| What workflows or processes change? |  |
| What decisions are made where? |  |
| Who handles exceptions? |  |
| Who supports the capability? |  |
| Who owns incidents/escalations? |  |
| Who owns controls and audit evidence? |  |
| What changes from pilot to scale? |  |

## Key Risks and Assumptions

| Risk / Assumption | Impact | Owner | Evidence Needed |
| --- | --- | --- | --- |
|  |  |  |  |

## Minimum-Friction Recommendation

Recommended architecture involvement:

- None required
- Light asynchronous review
- Architecture framing workshop
- Architecture decision record required
- 4+1 view worksheet useful
- Operating model blueprint useful
- Production-readiness review required
- Retirement checklist required

Rationale:

What decision does architecture need to enable?

What can safely emerge during delivery?

What must not be left ambiguous?

## Follow-Up Actions

| Action | Owner | Due Date | Evidence / Notes |
| --- | --- | --- | --- |
|  |  |  |  |

## Related Guidance

- [Architecture Management](https://github.com/RusDavies/docs-management-practices/blob/master/disciplines/ARCHITECTURE_MANAGEMENT.md)
- [Architecture Decision Record](https://github.com/RusDavies/docs-management-practices/blob/master/templates/architecture-decision-record.md)
- [4+1 Architecture View Worksheet](https://github.com/RusDavies/docs-management-practices/blob/master/templates/four-plus-one-architecture-view-worksheet.md)
- [Risk Register](https://github.com/RusDavies/docs-management-practices/blob/master/templates/risk-register.md)

## Usage Notes

- Use early to decide how much architecture attention a change needs.
- Lightweight answers are fine; the point is to expose material decisions before delivery is boxed in.
- Escalate to an ADR, 4+1 worksheet, or readiness checklist only when the scan shows meaningful impact.
- Revisit when scope, data, vendor, operating model, or risk changes.

## Example

For a new customer self-service portal, use the checklist to spot changed capabilities, data flows, support model, vendor dependencies, security boundaries, and whether a formal ADR or production-readiness review is needed.
