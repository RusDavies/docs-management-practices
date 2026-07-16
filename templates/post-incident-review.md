# Post-Incident Review

Use this template after a material incident to understand what happened, what the organization learned, and what should change.

This template is informed by ITIL/ITSM closure and continual improvement, SRE-style blameless postmortems, and security incident response lessons-learned practice. It should be blameless without being accountability-free. That distinction matters. Otherwise the review becomes either a witch hunt or a group hug with action items nobody owns.

## Incident Metadata

- incident title:
- incident ID/reference:
- incident date/time:
- review date:
- facilitator:
- incident commander:
- scribe:
- severity:
- affected services/processes/customers/groups:
- related timeline/decision log:
- related tickets/records:

## Review Scope

This review covers:

> 

This review does not cover:

> 

Open separate reviews if there are legal, HR, security, privacy, regulatory, or sensitive customer matters that require restricted handling.

## Executive Summary

Short factual summary of what happened, why it mattered, and what will change.

> 

## Impact Summary

| Impact area | Summary | Evidence/source |
| --- | --- | --- |
| customers/users |  |  |
| operations/service |  |  |
| data/security/privacy |  |  |
| financial |  |  |
| legal/regulatory |  |  |
| reputation/communications |  |  |
| people/team load |  |  |
| vendor/partner |  |  |

## Timeline Summary

Use the detailed timeline/decision log as source. Summarize the important events here.

| Time | Event | Notes |
| --- | --- | --- |
|  |  |  |

## What Happened

Describe the incident in plain language.

- trigger or initiating event:
- contributing factors:
- detection path:
- response path:
- recovery path:
- closure criteria:

Narrative:

> 

## What Worked

Identify strengths worth preserving.

Examples:

- monitoring detected the issue early
- ownership was clear
- rollback path worked
- customer communications were timely
- vendor escalation worked
- prior runbook reduced response time
- responders collaborated well under pressure

Notes:

> 

## What Did Not Work

Identify weaknesses without turning the review into blame theatre.

Examples:

- unclear ownership
- missing runbook
- poor observability
- slow escalation
- incomplete rollback path
- supplier dependency not visible
- communication delay
- alert fatigue
- data needed for diagnosis was unavailable
- decision authority was unclear

Notes:

> 

## Root Causes and Contributing Factors

Avoid stopping at the first technical cause. Ask why the system allowed the incident to happen, spread, or last as long as it did.

| Factor | Type | Evidence | Notes |
| --- | --- | --- | --- |
|  | technical / process / people / vendor / governance / data / communication / tooling |  |  |

Useful prompts:

- What condition made this possible?
- What condition made it worse?
- What condition delayed detection?
- What condition delayed response?
- What condition made the impact larger?
- What assumption turned out to be false?
- What control was missing, weak, bypassed, or misunderstood?

## Decision Review

Review material decisions from the incident.

| Decision | Was it appropriate with information available at the time? | What would improve future decisions? |
| --- | --- | --- |
|  |  |  |

Do not judge decisions only with hindsight. Hindsight is useful for learning and terrible for pretending the past was obvious.

## Communications Review

| Audience | What worked | What failed or was missing | Improvement |
| --- | --- | --- | --- |
| internal teams |  |  |  |
| executives |  |  |  |
| customers/users |  |  |  |
| vendors/partners |  |  |  |
| legal/privacy/security/compliance |  |  |  |
| public/status page |  |  |  |

## Security, Privacy, Legal, or Compliance Notes

Use this section only at an appropriate level of detail for the review audience. Link to restricted records where necessary.

- sensitive exposure considered:
- notification obligations considered:
- evidence preserved:
- legal/privacy/security owner:
- restricted follow-up required:

Notes:

> 

## Corrective Actions

Corrective actions should be specific, owned, and worth doing.

| Action | Owner | Due date | Priority | Success measure | Status |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

Action quality checks:

- [ ] action addresses a real cause or meaningful risk
- [ ] owner has authority or support to complete it
- [ ] due date is realistic
- [ ] success measure is inspectable
- [ ] action is not just “be more careful” wearing a hat

## Accepted Risks and Non-Actions

Not every possible improvement is worth doing. Document deliberate non-actions so future teams do not rediscover the same discussion from scratch.

| Risk/non-action | Rationale | Accepted by | Review date |
| --- | --- | --- | --- |
|  |  |  |  |

## Lessons for Management Disciplines

Capture where the learning belongs.

- risk management:
- operations management:
- incident response management:
- customer management:
- vendor/partner management:
- procurement management:
- people management:
- knowledge management:
- change management:
- project/program/portfolio management:

## Follow-Up Review

- corrective-action review date:
- owner:
- forum/cadence:
- closure criteria for follow-up actions:

## Final Notes

What should a future manager or incident commander know after reading this?

>

## Usage Notes

- Use after material incidents to learn and improve, not to stage a blame pageant.
- Separate triggering event, contributing factors, response quality, impact, and corrective actions.
- Assign owners and due dates to improvements.
- Review whether previous risks or incidents predicted this one.

## Example

After a deployment outage, summarize impact, timeline, what failed in testing/release controls, what worked in response, root/contributing factors, corrective actions, owners, and follow-up review date.
