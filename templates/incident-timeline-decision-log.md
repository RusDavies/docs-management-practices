# Incident Timeline and Decision Log

Use this log during an active incident to keep facts, decisions, actions, assumptions, and communications inspectable. It is informed by ITIL/ITSM record discipline, SRE incident timelines, and security incident response evidence practices.

The goal is not beautiful paperwork. The goal is to prevent everyone from reconstructing reality from memory while tired, defensive, and surrounded by Slack archaeology.

## Incident Metadata

- incident title:
- incident ID/reference:
- severity:
- incident commander:
- scribe:
- declared time:
- closed time:
- affected service/process/customer/group:
- coordination channel/location:

## Current State Snapshot

Update this section at major state changes.

- current status:
- current impact:
- affected population/scope:
- containment status:
- recovery status:
- next planned update:
- main open risks:

## Timeline

Record material events in chronological order. Include what changed, who observed it, and source/evidence where available.

| Time | Event | Source/evidence | Notes |
| --- | --- | --- | --- |
|  | incident declared |  |  |
|  |  |  |  |

## Decisions

Record decisions that affect impact, risk, communications, recovery, legal/security/privacy handling, customer commitments, or business trade-offs.

| Time | Decision | Decider | Rationale | Risks/assumptions | Follow-up |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

Useful decision prompts:

- Why this option rather than the alternative?
- What evidence supports the decision?
- What are we assuming?
- What risk are we accepting?
- Who has authority to accept that risk?
- What would make us reverse or change this decision?

## Actions

Track response actions until complete or deliberately abandoned.

| Action | Owner | Created | Due/next check | Status | Notes |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

Status values:

- not started
- in progress
- blocked
- complete
- cancelled
- deferred

## Communications Log

Record material internal, customer, executive, vendor, public, legal, regulatory, or status-page updates.

| Time | Audience | Owner | Message/source | Next update | Notes |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

Do not paste sensitive personal, credential, customer, regulated, privileged, or security details into broad logs. Link to restricted evidence where needed.

## Evidence and Artifacts

| Artifact/evidence | Location | Owner | Access restrictions | Notes |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

Examples:

- monitoring graph
- deployment/change record
- log bundle
- customer report
- vendor ticket
- support ticket sample
- security alert
- forensic evidence
- communication copy
- decision approval

## Open Questions

| Question | Owner | Needed by | Status | Notes |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Risk and Assumption Register

| Risk/assumption | Impact if wrong | Owner | Mitigation/recheck | Status |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Closure Notes

Do not close the incident only because the dashboard looks friendlier.

- immediate harm contained:
- service/process/customer impact restored to acceptable state:
- monitoring in place:
- stakeholders updated:
- residual risks documented:
- follow-up owners assigned:
- post-incident review required:
- post-incident review date:

Closure decision and rationale:

>

## Usage Notes

- Start during the incident, not after everyone is tired and creatively remembering things.
- Record facts, assumptions, decisions, actions, owners, and communications.
- Use timestamps and evidence links where possible.
- Preserve the log for post-incident review and compliance/security evidence where relevant.

## Example

At 10:14, alert fires; 10:18 incident declared; 10:25 rollback decision made by incident commander; 10:40 customer update sent; each entry records source, owner, rationale, and follow-up.
