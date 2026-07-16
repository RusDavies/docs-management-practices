# Debt Acceptance Record

## Purpose

Use this record when technical debt will be consciously accepted, deferred, or mitigated instead of remediated now.

Acceptance is a decision, not a bin. If nobody owns it, nobody accepted it. They just looked away in a room with chairs.

## Acceptance Summary

| Field | Value |
| --- | --- |
| Acceptance ID | DA-001 |
| Related debt ID |  |
| Title |  |
| Debt class | Architecture / Code / Dependency / Data / Security defect / Operational / Platform / Documentation / Vendor-tooling / Other |
| Affected product/service/system |  |
| Business owner |  |
| Technical owner |  |
| Risk/control owner |  |
| Decision owner |  |
| Date accepted |  |
| Review/expiry date |  |
| Status | Proposed / Accepted / Accepted with conditions / Rejected / Superseded / Closed |

## Debt Being Accepted

Describe the current technical debt or defect:

## Reason for Acceptance

Why is this not being remediated now?

Examples:

- remediation cost is disproportionate to current impact
- replacement/retirement is planned
- mitigation reduces risk enough for now
- dependency upgrade requires larger compatibility work
- release timing requires temporary acceptance
- further evidence is needed before remediation choice

## Consequence and Risk

What consequence is being accepted?

| Area | Impact / Notes |
| --- | --- |
| Customer/user impact |  |
| Delivery impact |  |
| Operational impact |  |
| Security/privacy impact |  |
| Compliance/audit impact |  |
| Cost impact |  |
| Resilience/recovery impact |  |
| Reputation/trust impact |  |

## Mitigations / Compensating Controls

| Mitigation | Owner | Evidence | Expiry / Review |
| --- | --- | --- | --- |
|  |  |  |  |

## Conditions of Acceptance

Acceptance applies only if:

- 
- 
- 

Acceptance must be revisited if:

- exposure changes
- customer/user impact increases
- a related incident occurs
- remediation becomes cheaper
- replacement/retirement slips
- a release/security gate requires review
- the review/expiry date arrives

## Options Considered

| Option | Summary | Why not selected now? |
| --- | --- | --- |
| Remediate now |  |  |
| Mitigate |  |  |
| Replace |  |  |
| Retire |  |  |
| Accept/defer |  |  |

## Decision

Decision:

Rationale:

Accepted by:

Date:

Review/expiry date:

## Follow-Up Actions

| Action | Owner | Due Date | Status |
| --- | --- | --- | --- |
|  |  |  |  |

## Usage Notes

- Use this for material accepted/deferred debt, especially where risk, security exposure, customer impact, cost, or operational burden matters.
- Name the person or forum authorized to accept the consequence.
- Add an expiry/review date; permanent temporary exceptions are how systems acquire folklore and grudges.
- Link this record from the technical debt register, risk register, release decision, or architecture decision as needed.

## Example

A team may accept a brittle legacy integration for one quarter because a replacement platform is approved and funded. The record should name the accepted outage/support risk, compensating monitoring, the replacement milestone, and the date acceptance expires if migration slips.
