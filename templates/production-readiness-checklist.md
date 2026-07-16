# Production-Readiness Checklist

## Purpose

Use this checklist before production launch, major rollout, or material production change.

Production readiness asks whether the system, service, platform, workflow, or capability can be operated, observed, secured, supported, recovered, paid for, and owned after launch. Launch is not success if Operations immediately inherits a mystery box with invoices.

## Readiness Summary

| Field | Value |
| --- | --- |
| System / service / capability |  |
| Launch / rollout date |  |
| Business owner |  |
| Product/service owner |  |
| Technical owner |  |
| Operations/support owner |  |
| Security/privacy contact |  |
| Architecture reviewer |  |
| Production change lead / change owner |  |
| Change implementer / technical executor |  |
| Reviewer / verifier |  |
| Rollback / pause decision authority |  |
| Support handoff owner |  |
| Readiness status | Not ready / Ready with conditions / Ready |
| Decision owner |  |

## Scope

What is going to production?

- 

What is not included in this launch?

- 

Which users/customers/stakeholders are affected?

- 

## Ownership and Operating Model

| Area | Owner / Status | Evidence / Notes |
| --- | --- | --- |
| Business capability owner |  |  |
| Product/service owner |  |  |
| Technical owner |  |  |
| Production change lead / change owner |  |  |
| Change implementer / technical executor |  |  |
| Reviewer / verifier |  |  |
| Day-to-day operator |  |  |
| Support owner |  |  |
| Support handoff owner |  |  |
| Incident owner/path |  |  |
| Data owner |  |  |
| Security/privacy/control owner |  |  |
| Cost owner |  |  |
| Vendor/platform owner |  |  |
| Lifecycle/retirement owner |  |  |

## Architecture and Dependencies

| Check | Status | Evidence / Notes |
| --- | --- | --- |
| Architecture decision records complete where needed | Pass / Fail / N/A |  |
| Critical dependencies identified | Pass / Fail |  |
| Integration contracts documented | Pass / Fail / N/A |  |
| Data ownership and source of truth clear | Pass / Fail |  |
| Operating model defined | Pass / Fail |  |
| Known architectural risks accepted or mitigated | Pass / Fail |  |
| Technical debt introduced by launch is recorded | Pass / Fail / N/A |  |

## Security, Privacy, and Controls

| Check | Status | Evidence / Notes |
| --- | --- | --- |
| Threat model / security review complete where needed | Pass / Fail / N/A |  |
| Access controls configured | Pass / Fail |  |
| Secrets/credentials handled securely | Pass / Fail |  |
| Data classification confirmed | Pass / Fail |  |
| Privacy/retention requirements addressed | Pass / Fail / N/A |  |
| Audit/control evidence available | Pass / Fail / N/A |  |
| Vulnerability/dependency findings reviewed | Pass / Fail / N/A |  |
| Security incident path known | Pass / Fail |  |

## Reliability and Recovery

| Check | Status | Evidence / Notes |
| --- | --- | --- |
| Availability/reliability expectations defined | Pass / Fail |  |
| Backup/restore or recovery path tested where relevant | Pass / Fail / N/A |  |
| Rollback plan exists | Pass / Fail |  |
| Rollback / pause decision authority named | Pass / Fail |  |
| Post-change verification owner named | Pass / Fail |  |
| Failure modes understood | Pass / Fail |  |
| Capacity/scaling assumptions tested or accepted | Pass / Fail |  |
| Disaster recovery / business continuity needs addressed | Pass / Fail / N/A |  |
| Maintenance windows or change constraints known | Pass / Fail / N/A |  |

## Observability and Operations

| Check | Status | Evidence / Notes |
| --- | --- | --- |
| Monitoring exists for critical health signals | Pass / Fail |  |
| Alerts are actionable and routed | Pass / Fail |  |
| Logs/traces/metrics available to operators | Pass / Fail |  |
| Dashboards or runbooks exist where useful | Pass / Fail / N/A |  |
| On-call/support coverage known | Pass / Fail / N/A |  |
| Service desk/support process updated | Pass / Fail / N/A |  |
| Support handoff owner and timing confirmed | Pass / Fail / N/A |  |
| Operational documentation complete enough | Pass / Fail |  |

## Customer / Stakeholder Readiness

| Check | Status | Evidence / Notes |
| --- | --- | --- |
| Customer/stakeholder communication prepared | Pass / Fail / N/A |  |
| Support/customer-success teams briefed | Pass / Fail / N/A |  |
| Known limitations documented | Pass / Fail |  |
| Escalation path for customer-impacting issues exists | Pass / Fail |  |
| Training or enablement complete where needed | Pass / Fail / N/A |  |

## Cost and Capacity

| Check | Status | Evidence / Notes |
| --- | --- | --- |
| Cost owner named | Pass / Fail |  |
| Expected run cost understood | Pass / Fail |  |
| Budget/cost center confirmed | Pass / Fail / N/A |  |
| Scaling cost exposure reviewed | Pass / Fail / N/A |  |
| Vendor/platform commercial constraints reviewed | Pass / Fail / N/A |  |

## Launch Decision

Decision:

- Ready
- Ready with conditions
- Not ready
- Defer launch

Conditions:

Accepted risks:

Decision owner:

Rollback / pause decision authority:

Decision date:

## Follow-Up Actions

| Action | Owner | Due Date | Required Before Launch? | Evidence / Notes |
| --- | --- | --- | --- | --- |
|  |  |  | Yes / No |  |

## Post-Launch Review

Review date:

Signals to inspect:

- incidents
- customer/stakeholder feedback
- support volume
- support handoff quality
- operational toil
- cost
- performance/reliability
- security/privacy/control issues
- follow-up actions

## Related Guidance

- [Architecture Management](https://github.com/RusDavies/docs-management-practices/blob/master/disciplines/ARCHITECTURE_MANAGEMENT.md)
- [Change Management](https://github.com/RusDavies/docs-management-practices/blob/master/disciplines/CHANGE_MANAGEMENT.md)
- [Incident Response Management](https://github.com/RusDavies/docs-management-practices/blob/master/disciplines/INCIDENT_RESPONSE_MANAGEMENT.md)
- [Risk Register](https://github.com/RusDavies/docs-management-practices/blob/master/templates/risk-register.md)
- [Architecture Decision Record](https://github.com/RusDavies/docs-management-practices/blob/master/templates/architecture-decision-record.md)
- [Service / System Ownership Map](https://github.com/RusDavies/docs-management-practices/blob/master/templates/service-ownership-map.md)

## Usage Notes

- Use before production launch, major rollout, or material production change.
- “Ready with conditions” is acceptable only when conditions, owners, and risks are explicit.
- Involve operations/support/security/privacy/data/cost owners early enough to matter.
- Name the production change lead, implementer, reviewer/verifier, rollback authority, and support handoff owner before the launch window.
- Keep evidence links rather than relying on verbal assurances.

## Example

Before launching a new API, confirm owners, dependencies, security controls, monitoring, runbooks, recovery path, support readiness, cost owner, technical debt, and launch/rollback decision authority.
