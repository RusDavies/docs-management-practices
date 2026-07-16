# Security Exposure Assessment

## Purpose

Use this assessment to decide how exposed a security defect, vulnerability, misconfiguration, weak control, dependency issue, or insecure design actually is.

Scanner severity is an input. It is not the whole answer. Treating every finding as equally urgent is how security programmes produce dashboards instead of risk reduction. Very decorative dashboards, admittedly.

## Assessment Summary

| Field | Value |
| --- | --- |
| Assessment ID | SEA-001 |
| Related debt/finding ID |  |
| Title |  |
| Affected product/service/system |  |
| Defect/finding type |  |
| Source | Scanner / Code review / Incident / Pentest / Threat model / Dependency advisory / AI-agent review / Other |
| Assessor |  |
| Business owner |  |
| Technical owner |  |
| Security owner |  |
| Date assessed |  |
| Status | Draft / Reviewed / Approved / Superseded |

## Finding / Defect Description

Describe the security issue in plain language:

## Affected Assets and Boundaries

| Asset / Component | Environment | Internet Exposed? | Auth Required? | Data Sensitivity | Owner |
| --- | --- | --- | --- | --- | --- |
|  | Dev / Test / Staging / Production / Mixed | Yes / No / Unknown | None / User / Admin / Service / Unknown | Public / Internal / Confidential / Regulated / Customer-sensitive / Employee-sensitive / Security-sensitive |  |

## Reachability and Exploitability

| Question | Answer | Evidence / Notes |
| --- | --- | --- |
| Is the vulnerable code/path/component present? | Yes / No / Unknown |  |
| Is it reachable in deployed environments? | Yes / No / Unknown |  |
| Is authentication required? | Yes / No / Unknown |  |
| Is authorization enforced? | Yes / No / Unknown |  |
| Can an external attacker reach it? | Yes / No / Unknown |  |
| Can an internal user/service reach it? | Yes / No / Unknown |  |
| Is user-controlled input involved? | Yes / No / Unknown |  |
| Is exploit code or public PoC available? | Yes / No / Unknown |  |
| Is active exploitation observed or likely? | Yes / No / Unknown |  |
| Are compensating controls present? | Yes / No / Unknown |  |

## Exposure Window

| Field | Value |
| --- | --- |
| Earliest known exposure date |  |
| Discovery date |  |
| Expected remediation/mitigation date |  |
| Current exposure window |  |
| Exposure-window owner |  |

## Impact Assessment

| Impact Area | Rating | Notes |
| --- | --- | --- |
| Confidentiality | None / Low / Medium / High / Critical |  |
| Integrity | None / Low / Medium / High / Critical |  |
| Availability | None / Low / Medium / High / Critical |  |
| Privacy | None / Low / Medium / High / Critical |  |
| Compliance/legal | None / Low / Medium / High / Critical |  |
| Customer/user trust | None / Low / Medium / High / Critical |  |
| Operational recovery | None / Low / Medium / High / Critical |  |

## Risk Classification

Initial severity:

Adjusted exposure severity:

Rationale for adjustment:

Decision:

- emergency remediation
- scheduled remediation
- mitigation now, remediation later
- accepted risk
- false positive / not applicable
- needs more evidence

## Required Actions

| Action | Owner | Due Date | Evidence Required | Status |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Evidence Links

- scanner/advisory:
- code path/reachability evidence:
- deployment/environment evidence:
- logs/monitoring evidence:
- compensating control evidence:
- test evidence:
- decision/approval evidence:

## Usage Notes

- Use this before deciding whether a security defect blocks release, needs emergency remediation, can be scheduled, or can be accepted with mitigation.
- Pair severity with reachability, exploitability, asset exposure, data sensitivity, and compensating controls.
- Unknown exposure should usually increase urgency until evidence improves. “Unknown” is not “fine,” despite the long and tragic history of pretending otherwise.
- Link the result to the technical debt register, remediation plan, risk register, release gate, or debt acceptance record.

## Example

A dependency advisory may be critical in general but low exposure for a service if the vulnerable package is present only in a build tool and not deployed. Conversely, a medium scanner finding may be high exposure if it affects an internet-facing authenticated workflow handling customer data with weak authorization.
