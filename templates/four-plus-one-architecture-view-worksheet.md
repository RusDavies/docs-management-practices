# 4+1 Architecture View Worksheet

## Purpose

Use this worksheet to describe a system, platform, product, service, or major capability from multiple useful viewpoints.

The 4+1 view model is a thinking structure, not a diagram quota. Use the views that improve decisions. Leave out what does not matter. Architecture does not get extra credit for making everyone tired.

## Summary

| Field | Value |
| --- | --- |
| System / capability |  |
| Worksheet owner |  |
| Date |  |
| Lifecycle stage | Idea / Discovery / Delivery / Production / Evolution / Retiring |
| Business owner |  |
| Technical owner |  |
| Architecture reviewer(s) |  |
| Related ADRs |  |
| Related operating model |  |
| Review trigger |  |

## Scope

What is in scope?

- 

What is out of scope?

- 

What decision or review should this worksheet support?

- 

## +1: Scenarios / Use Cases

Use scenarios to anchor the views in real behaviour.

| Scenario | Actor / User | Trigger | Expected Outcome | Criticality | Notes |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  | High / Medium / Low |  |

Include scenarios for:

- normal use
- high-volume or peak use
- failure/recovery
- security/privacy-sensitive use
- operational support
- exception handling
- customer or stakeholder escalation where relevant

## Logical View

The logical view explains domain structure and responsibilities.

Capture:

- domain concepts
- components/modules/services
- responsibilities
- ownership boundaries
- business capability alignment
- key abstractions

| Element | Responsibility | Owner | Related Capability | Notes |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

Decision questions:

- Are responsibilities clear?
- Are boundaries coherent?
- Is business capability alignment visible?
- Are duplicated responsibilities intentional?

## Process View

The process view explains runtime behaviour.

Capture:

- workflows
- event flows
- synchronous/asynchronous behaviour
- concurrency
- latency-sensitive paths
- failure and recovery behaviour
- scaling assumptions

| Flow / Process | Trigger | Systems / Components | Failure Mode | Recovery / Mitigation |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

Decision questions:

- What happens under real use, load, failure, and recovery?
- Which paths are customer-impacting or operationally critical?
- Where are bottlenecks or fragile dependencies?

## Development View

The development view explains how the system is built and owned.

Capture:

- code/module/package structure
- team ownership
- dependency direction
- build/release structure
- test strategy
- shared libraries/platform dependencies

| Code / Build Element | Owner | Dependency | Change Risk | Notes |
| --- | --- | --- | --- | --- |
|  |  |  | High / Medium / Low |  |

Decision questions:

- Can teams change this safely?
- Are ownership and dependency boundaries clear?
- Are there dependency directions that will create future pain?

## Physical / Deployment View

The physical view explains where the system runs.

Capture:

- environments
- hosting/runtime platform
- network boundaries
- identity/access boundaries
- storage
- deployment topology
- observability
- operational constraints

| Environment / Runtime | Components | Network / Identity Boundary | Operational Owner | Notes |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

Decision questions:

- Can the system be deployed, monitored, secured, scaled, and recovered?
- Are environment differences intentional?
- Are operational owners and support paths clear?

## Data View

Use this optional view when data ownership, quality, lineage, reporting, privacy, or AI/analytics use matters.

| Data Domain / Object | Source of Truth | Owner | Consumers | Sensitivity | Retention / Notes |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  | Public / Internal / Confidential / Regulated / Customer-sensitive / Employee-sensitive / Security-sensitive |  |

Decision questions:

- Who owns the data?
- Where is it created, transformed, stored, and consumed?
- What privacy, retention, audit, or quality constraints apply?

## Operating Model View

Use this optional view when the architecture creates or changes a function, line of business, platform, service, or major capability.

| Operating Area | Owner / Decision | Notes |
| --- | --- | --- |
| Capability owner |  |  |
| Day-to-day operator |  |  |
| Support model |  |  |
| Incident / escalation path |  |  |
| Change/release owner |  |  |
| Data owner |  |  |
| Control owner |  |  |
| Cost owner |  |  |
| Lifecycle / retirement owner |  |  |

Decision questions:

- Does the architecture have an owner in real operations?
- Are exceptions, incidents, and support handled?
- Are controls and costs owned?

## Key Decisions and Open Questions

| Item | Type | Owner | Due Date | Notes |
| --- | --- | --- | --- | --- |
|  | Decision / Open question / Risk |  |  |  |

## Minimum-Friction Check

Before adding more detail, ask:

- What decision does this view support?
- Who will use it?
- What risk does it reduce?
- What would be harmful to leave ambiguous?
- What can safely emerge during delivery?

If nobody can answer, stop drawing. The diagram has begun feeding on attention.

## Related Guidance

- [Architecture Management](https://github.com/RusDavies/docs-management-practices/blob/master/disciplines/ARCHITECTURE_MANAGEMENT.md)
- [Architecture Decision Record](https://github.com/RusDavies/docs-management-practices/blob/master/templates/architecture-decision-record.md)
- [Architecture Framing Checklist](https://github.com/RusDavies/docs-management-practices/blob/master/templates/architecture-framing-checklist.md)
- [Production-Readiness Checklist](https://github.com/RusDavies/docs-management-practices/blob/master/templates/production-readiness-checklist.md)

## Usage Notes

- Use when one view of the system is not enough to support a decision.
- Fill only the views that help the decision; empty diagram theatre is still theatre.
- Anchor the views in scenarios so the architecture describes real behaviour.
- Link resulting decisions to ADRs or readiness checks where needed.

## Example

For a claims-processing platform, describe customer submission scenarios, logical domain components, runtime/process interactions, deployment topology, implementation modules, and how each view affects reliability and support.
