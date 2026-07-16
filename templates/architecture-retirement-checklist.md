# Architecture Retirement Checklist

## Purpose

Use this checklist when retiring, replacing, consolidating, or decommissioning a system, platform, integration, data store, vendor capability, service, or major architecture pattern.

Retirement is architecture work. The graveyard is part of the estate. Ignore it long enough and it starts billing you, leaking data, blocking change, or appearing in incident calls like an undead dependency with root access.

## Retirement Summary

| Field | Value |
| --- | --- |
| System / service / capability |  |
| Retirement ID |  |
| Business owner |  |
| Technical owner |  |
| Operations/support owner |  |
| Data owner |  |
| Security/privacy contact |  |
| Vendor/contract owner |  |
| Target retirement date |  |
| Status | Proposed / Approved / In progress / Complete / Deferred |

## Retirement Rationale

Why is this being retired?

- obsolete
- duplicated
- replaced by new capability
- unsupported technology
- unacceptable risk
- excessive cost
- vendor exit
- architecture simplification
- business process retired
- other:

Decision record / approval reference:

## Scope

What is being retired?

- 

What is explicitly not being retired?

- 

Replacement / target state:

- 

## Dependency and Usage Discovery

| Area | Status | Evidence / Notes |
| --- | --- | --- |
| Users/customers identified | Pass / Fail / N/A |  |
| Upstream dependencies identified | Pass / Fail / N/A |  |
| Downstream dependencies identified | Pass / Fail / N/A |  |
| Integrations/APIs/events/files identified | Pass / Fail / N/A |  |
| Reports/analytics consumers identified | Pass / Fail / N/A |  |
| Batch jobs/scheduled processes identified | Pass / Fail / N/A |  |
| Monitoring/alerting dependencies identified | Pass / Fail / N/A |  |
| Support/runbook dependencies identified | Pass / Fail / N/A |  |
| Vendor/contract dependencies identified | Pass / Fail / N/A |  |

## Data, Privacy, and Records

| Check | Status | Evidence / Notes |
| --- | --- | --- |
| Data inventory complete | Pass / Fail / N/A |  |
| Data owner approval obtained | Pass / Fail / N/A |  |
| Retention obligations understood | Pass / Fail / N/A |  |
| Migration/export required? | Yes / No |  |
| Migration/export complete | Pass / Fail / N/A |  |
| Deletion/anonymization required? | Yes / No |  |
| Deletion/anonymization complete | Pass / Fail / N/A |  |
| Privacy/legal review complete where needed | Pass / Fail / N/A |  |
| Audit evidence retained | Pass / Fail / N/A |  |

## Security and Access Cleanup

| Check | Status | Evidence / Notes |
| --- | --- | --- |
| User access removed | Pass / Fail / N/A |  |
| Service accounts disabled/removed | Pass / Fail / N/A |  |
| Secrets/credentials revoked | Pass / Fail / N/A |  |
| Network exposure removed | Pass / Fail / N/A |  |
| Certificates/domains cleaned up | Pass / Fail / N/A |  |
| Firewall/security rules removed or updated | Pass / Fail / N/A |  |
| Vulnerability/scanner inventory updated | Pass / Fail / N/A |  |
| CMDB/configuration inventory updated | Pass / Fail / N/A |  |

## Operational Cleanup

| Check | Status | Evidence / Notes |
| --- | --- | --- |
| Monitoring/alerts removed or updated | Pass / Fail / N/A |  |
| Runbooks retired or updated | Pass / Fail / N/A |  |
| Support knowledge base updated | Pass / Fail / N/A |  |
| Incident/escalation paths updated | Pass / Fail / N/A |  |
| Backup jobs stopped or updated | Pass / Fail / N/A |  |
| Scheduled jobs stopped or updated | Pass / Fail / N/A |  |
| Infrastructure/resources removed | Pass / Fail / N/A |  |
| Cost/billing ownership closed | Pass / Fail / N/A |  |

## Vendor / Contract Cleanup

| Check | Status | Evidence / Notes |
| --- | --- | --- |
| Contract termination/renewal decision made | Pass / Fail / N/A |  |
| Notice period handled | Pass / Fail / N/A |  |
| Data return/deletion rights exercised | Pass / Fail / N/A |  |
| Supplier access removed | Pass / Fail / N/A |  |
| Final invoice/cost closure complete | Pass / Fail / N/A |  |
| Vendor records updated | Pass / Fail / N/A |  |

## Stakeholder Communication

| Stakeholder Group | Communication Needed? | Owner | Status / Notes |
| --- | --- | --- | --- |
| Users/customers | Yes / No |  |  |
| Support/operations | Yes / No |  |  |
| Product/business owner | Yes / No |  |  |
| Security/privacy/legal | Yes / No |  |  |
| Finance/procurement/vendor management | Yes / No |  |  |
| Dependent teams | Yes / No |  |  |

## Retirement Decision

Decision:

- Proceed
- Proceed with conditions
- Defer
- Cancel retirement

Conditions:

Accepted risks:

Decision owner:

Decision date:

## Closure Evidence

| Evidence | Location / Reference |
| --- | --- |
| Approval / decision record |  |
| Dependency discovery evidence |  |
| Data migration/deletion evidence |  |
| Access cleanup evidence |  |
| Infrastructure/resource cleanup evidence |  |
| Vendor/contract closure evidence |  |
| CMDB/service catalog update |  |
| Final stakeholder communication |  |

## Follow-Up Actions

| Action | Owner | Due Date | Evidence / Notes |
| --- | --- | --- | --- |
|  |  |  |  |

## Related Guidance

- [Architecture Management](https://github.com/RusDavies/docs-management-practices/blob/master/disciplines/ARCHITECTURE_MANAGEMENT.md)
- [Technical Debt Management](https://github.com/RusDavies/docs-management-practices/blob/master/disciplines/TECHNICAL_DEBT_MANAGEMENT.md)
- [Vendor and Partner Management](https://github.com/RusDavies/docs-management-practices/blob/master/disciplines/VENDOR_AND_PARTNER_MANAGEMENT.md)
- [Risk Register](https://github.com/RusDavies/docs-management-practices/blob/master/templates/risk-register.md)
- [Architecture Decision Record](https://github.com/RusDavies/docs-management-practices/blob/master/templates/architecture-decision-record.md)

## Usage Notes

- Start retirement planning before replacement launch if possible.
- Use evidence for dependencies, data, access, contracts, and operational handoff.
- Treat unknown users or integrations as blockers until investigated or explicitly accepted.
- Keep proof of shutdown, deletion, migration, and owner sign-off.

## Example

For retiring an old reporting database, identify reports, integrations, owners, retained data, export/deletion needs, access removal, monitoring removal, contract impact, and final business/data-owner approval.
