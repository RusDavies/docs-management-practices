# Incident Declaration Checklist

Use this checklist when a material problem may need formal incident response. It is informed by ITIL/ITSM incident ownership and closure discipline, SRE-style incident command practice, and security incident response patterns. It is not a claim of framework compliance. That way lies audit theatre and laminated despair.

## Incident Summary

- incident title:
- incident ID/reference:
- declared by:
- declaration time:
- current severity:
- incident commander:
- coordination channel/location:
- affected service/process/customer/group:
- current status:

## 1. Decide Whether This Is an Incident

Declare an incident if any of the following are true:

- customers, users, employees, or partners are materially affected
- a critical service, process, supplier, or system is unavailable or degraded
- sensitive, regulated, customer, employee, or financial data may be exposed
- security compromise is suspected
- safety, legal, compliance, or regulatory exposure may exist
- operational impact is spreading or unclear
- executive, customer, regulator, public, or board communication may be required
- normal ownership is unclear and coordination is needed

If in doubt, declare at a lower severity and downgrade later. It is easier to stand down a response than to reconstruct the first hour from chat fragments and optimism.

## 2. Initial Severity Assessment

Assess severity using current known impact, not emotional volume.

| Area | Current assessment |
| --- | --- |
| customer/user impact |  |
| people/safety impact |  |
| data/security/privacy impact |  |
| financial impact |  |
| legal/regulatory exposure |  |
| operational disruption |  |
| reputation/public exposure |  |
| duration and spread |  |
| executive/board relevance |  |

Initial severity:

- [ ] critical
- [ ] high
- [ ] medium
- [ ] low
- [ ] under assessment

Severity rationale:

> 

## 3. Assign Core Roles

Small teams may combine roles. Do not leave them implicit.

| Role | Owner | Notes |
| --- | --- | --- |
| incident commander |  | coordinates response and decisions |
| technical/operational lead |  | diagnoses and restores service/stability |
| communications lead |  | manages internal/external updates |
| scribe |  | records timeline, actions, decisions, evidence |
| customer/stakeholder lead |  | manages affected relationship context |
| security/privacy/legal lead |  | engaged if exposure may exist |
| executive sponsor |  | engaged for major business decisions/blockers |

## 4. Establish Coordination

- [ ] single coordination channel created
- [ ] bridge/call created if needed
- [ ] incident timeline/decision log started
- [ ] responders invited
- [ ] noisy side channels redirected or summarized
- [ ] next update time set

Coordination details:

> 

## 5. Immediate Triage Questions

- What happened?
- When did it start?
- How was it detected?
- Who or what is affected?
- Is impact still growing?
- What is the safest immediate containment action?
- What evidence must be preserved?
- Who needs to know now?
- What must not be said yet because it is still unknown?

Known facts:

> 

Unknowns:

> 

Immediate risks:

> 

## 6. Containment and Stabilization

Initial containment actions:

| Action | Owner | Time | Status |
| --- | --- | --- | --- |
|  |  |  |  |

Risks introduced by containment:

> 

Rollback/undo path:

> 

## 7. Communication Decision

Initial communication required?

- [ ] internal only
- [ ] affected customers/users
- [ ] all customers/users
- [ ] executives
- [ ] legal/security/privacy/compliance
- [ ] vendor/partner
- [ ] regulator/public authority
- [ ] public/status page/media
- [ ] not yet; reason documented below

Communication rationale:

> 

Next update due:

> 

## 8. Evidence and Sensitive Handling

Use this section if security, privacy, legal, employment, safety, or regulated data may be involved.

- [ ] preserve logs/evidence before destructive recovery where feasible
- [ ] restrict access to sensitive evidence
- [ ] avoid sharing personal, customer, credential, or regulated data in broad channels
- [ ] involve legal/privacy/security owner
- [ ] document assumptions and uncertainty
- [ ] record who approved risky containment or recovery actions

Evidence notes:

> 

## 9. Declaration Decision

Incident declared?

- [ ] yes
- [ ] no; handled as normal issue/request/problem
- [ ] monitor and reassess by:

Decision rationale:

> 

Initial next actions:

| Action | Owner | Due/next check | Notes |
| --- | --- | --- | --- |
|  |  |  |  |

## Usage Notes

- Use when a material problem may need coordinated response.
- Declare early if impact, spread, or ownership is unclear; severity can be adjusted later.
- Assign roles explicitly even in small teams.
- Start the timeline/decision log immediately once declared.

## Example

A payment outage affecting checkout should trigger declaration, severity assessment, incident commander assignment, coordination channel, stakeholder-update owner, and first customer-impact statement.
