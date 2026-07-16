# Incident Response Management

<!-- doctrine:id=incident-response-management -->

## Purpose

Incident response management is the discipline of leading the organization when something material has gone wrong: a service outage, security event, customer-impacting defect, data issue, operational failure, safety concern, public mistake, or serious internal breakdown.

It is related to risk management, but it is not the same thing. Risk management asks what might go wrong, how likely it is, how severe it would be, and what controls or acceptances are appropriate. Incident response management starts when the risk is no longer theoretical and everyone would very much like the building to stop being on fire.

It overlaps with operations, customer management, security, legal, communications, engineering, people management, vendor management, and executive leadership. The point is not to create a ceremonial emergency bureaucracy. The point is to make ownership, severity, decisions, communications, recovery, and learning explicit before panic starts freelancing.

## Core Responsibilities

Incident response management is responsible for:

- defining what counts as an incident
- classifying severity and impact
- assigning incident command and decision rights
- coordinating responders across functions
- protecting people, customers, assets, data, and operations
- containing harm and restoring service or stability
- communicating clearly with internal and external stakeholders
- escalating legal, regulatory, customer, security, safety, or executive concerns
- tracking decisions, actions, evidence, and open risks during the incident
- closing the incident deliberately rather than by exhaustion
- running a post-incident review and converting learning into prevention, resilience, and operating improvements

## Incident Types

Organizations should decide which incident classes require formal response. Common classes include:

- service outage or major degradation
- security breach, suspicious access, malware, credential exposure, or data leak
- privacy or compliance event
- customer-impacting defect or failed deployment
- safety issue or workplace emergency
- financial, billing, or payment processing failure
- vendor or supplier failure
- operational process breakdown
- public communications or reputation incident
- serious people, ethics, harassment, or conduct issue

Not every problem needs a full incident process. Every serious problem needs clear ownership.

## Severity and Triage

Severity levels should be simple enough to use under pressure.

A useful severity model considers:

- customer impact
- people/safety impact
- data/security/privacy impact
- financial impact
- legal/regulatory exposure
- operational disruption
- reputation risk
- duration and spread
- executive or board relevance

Good triage answers:

- What happened?
- Who or what is affected?
- How bad is it right now?
- Is it getting worse?
- Who is incident commander?
- What is the immediate containment action?
- Who needs to know now?
- What must be preserved as evidence?

Avoid severity theatre. If every incident is critical, nothing is.

## Incident Command

During a significant incident, one person should own coordination. That person does not need to be the most senior expert. They need authority, clarity, calm, and enough context to drive the response.

The incident commander owns:

- current incident state
- response cadence
- role assignment
- decision tracking
- escalation
- communication coordination
- closure criteria

Specialists own technical, operational, legal, security, customer, or people-management decisions within their expertise. The incident commander keeps the machine moving so responders do not become a flock of highly educated pigeons.

## Response Roles

Common response roles include:

- **Incident commander:** coordinates the response and decision cadence
- **Technical/operational lead:** diagnoses and executes recovery actions
- **Communications lead:** manages internal, customer, public, or executive updates
- **Scribe:** records timeline, actions, decisions, owners, and evidence
- **Customer/stakeholder lead:** coordinates account-specific impact and commitments
- **Security/privacy/legal lead:** handles regulated, privileged, sensitive, or evidentiary matters
- **Executive sponsor:** removes organizational blockers and handles major business decisions

Small teams may combine roles. Combining roles is fine; leaving roles implicit is how chaos gets promoted.

## Response Cadence

A useful incident cadence includes:

1. declare the incident
2. assign severity and command
3. create a single coordination space
4. establish impact, scope, and immediate risks
5. assign response roles
6. contain harm
7. communicate initial status
8. restore service or stability
9. monitor for recurrence
10. decide closure criteria
11. run post-incident review
12. track follow-up actions to completion

The cadence should be lightweight, repeatable, and visible. Incident response fails when every incident is managed as a unique improvisational jazz piece.

## Communications

Incident communications should be honest, timely, and appropriately constrained.

Good incident updates include:

- current status
- known impact
- actions underway
- what is not yet known
- expected next update time
- customer or stakeholder instructions where relevant
- owner/contact for escalation

Bad updates include vague reassurance, invented root cause, blame, unexplained silence, and executive poetry about resilience while customers are still broken.

Communication should be coordinated with legal, security, privacy, customer, and executive stakeholders when the incident has regulatory, contractual, reputational, or customer-impacting consequences.

## Evidence, Records, and Decision Logs

Significant incidents need a record.

Track:

- incident declaration time
- severity changes
- known impact
- timeline of material events
- decisions and rationale
- actions and owners
- communications sent
- evidence preserved
- assumptions made under uncertainty
- open risks accepted during recovery
- closure decision

The record is not decorative paperwork. It protects learning, accountability, compliance, and memory when everyone is tired and pretending they remember exactly what happened.

## Closure

Do not close an incident merely because the most visible symptom stopped.

Closure should confirm:

- immediate harm has been contained
- service, operation, or safety has been restored to an acceptable state
- monitoring is in place
- stakeholders have been updated
- known residual risks are documented
- ownership exists for follow-up work
- post-incident review is scheduled where appropriate

## Post-Incident Review

Post-incident review should be blameless without being accountability-free.

A good review asks:

- What happened?
- What was the impact?
- How did we detect it?
- What made response faster or slower?
- What decisions mattered?
- What assumptions were wrong?
- What controls failed or were missing?
- What should change in systems, process, ownership, documentation, training, staffing, monitoring, vendor management, or decision rights?
- Which actions are worth doing, by whom, and by when?

The goal is better operating capability, not ritualized sorrow.

## Relationship to Other Disciplines

Incident response management connects to:

- **Risk management:** risk registers, controls, thresholds, acceptance, and prevention
- **Operations management:** monitoring, runbooks, service restoration, continuity, and resilience
- **Customer management:** customer communications, commitments, escalations, and recovery
- **Vendor and partner management:** supplier failures, third-party escalation, contractual duties, and dependency risk
- **People management:** responder load, psychological safety, conduct issues, and accountability
- **Knowledge management:** runbooks, lessons learned, decision logs, and institutional memory
- **Change management:** controlled recovery changes and post-incident process changes

## Disagree and Commit

Incidents create pressure and disagreement:

- Should we roll back, patch, disable, or wait?
- Should we notify customers now or after more confirmation?
- Is this security/privacy/legal exposure?
- Is the severity high enough for executive involvement?
- Do we accept degraded operation to restore partial service?
- Should we pause launches or other work?

Healthy teams surface disagreement quickly, decide explicitly, record the rationale, and commit to the chosen response. During an incident, private second-guessing plus public hesitation is not healthy skepticism. It is multiplayer paralysis.

## Common Artifacts

- incident response policy
- [severity model](../templates/incident-severity-model.md)
- [incident declaration checklist](https://github.com/RusDavies/docs-management-practices/blob/master/templates/incident-declaration-checklist.md)
- [incident role roster](../templates/incident-role-roster.md)
- [escalation matrix](../templates/incident-escalation-matrix.md)
- [incident command runbook](../templates/incident-command-runbook.md)
- [stakeholder update template](https://github.com/RusDavies/docs-management-practices/blob/master/templates/incident-stakeholder-update.md)
- [incident timeline and decision log](https://github.com/RusDavies/docs-management-practices/blob/master/templates/incident-timeline-decision-log.md)
- customer impact log
- [evidence preservation checklist](../templates/incident-evidence-preservation-checklist.md)
- [post-incident review template](https://github.com/RusDavies/docs-management-practices/blob/master/templates/post-incident-review.md)
- [corrective-action tracker](../templates/incident-corrective-action-tracker.md)
- [incident metrics dashboard](../templates/incident-metrics-dashboard.md)

## Practitioner / Operator Counterpart

For hands-on response-task execution, timeline and evidence capture, incident scribe support, communications support, impact/scope evidence, corrective-action tracking, and post-incident handoff support, see [Incident Response Practitioner](https://github.com/RusDavies/docs-practitioner-practices/blob/master/roles/incident-response-practitioner.md).

This management guide owns incident declaration, severity, command structure, response cadence, escalation, communications approval, closure, risk acceptance, and organizational learning. The practitioner role keeps assigned work and evidence moving without silently becoming incident command.

## Related Audience-Level Guides

Use the audience-level guides to adapt this discipline to the manager's scope, authority, and operating context:

- [Team Leads and Frontline Managers](https://github.com/RusDavies/docs-management-practices/blob/master/TEAM_LEADS_AND_FRONTLINE_MANAGERS.md) — day-to-day execution, coaching, coordination, and local accountability.
- [Managers of Managers](https://github.com/RusDavies/docs-management-practices/blob/master/MANAGERS_OF_MANAGERS.md) — consistency across teams, manager enablement, and cross-team operating cadence.
- [Directors and Senior Leaders](https://github.com/RusDavies/docs-management-practices/blob/master/DIRECTORS_AND_SENIOR_LEADERS.md) — multi-team strategy, prioritization, risk, and organizational health.
- [Executives and Founders](https://github.com/RusDavies/docs-management-practices/blob/master/EXECUTIVES_AND_FOUNDERS.md) — enterprise direction, culture, investment choices, and accountability systems.
- [Cross-Functional and Matrix Management](https://github.com/RusDavies/docs-management-practices/blob/master/CROSS_FUNCTIONAL_AND_MATRIX_MANAGEMENT.md) — shared ownership, influence, and decision-making without clean reporting lines.
- [Managing Up](https://github.com/RusDavies/docs-management-practices/blob/master/MANAGING_UP.md) — upward communication, expectation-setting, escalation, and decision framing.
- [Remote and Hybrid Management](https://github.com/RusDavies/docs-management-practices/blob/master/REMOTE_AND_HYBRID_MANAGEMENT.md) — distributed communication, trust, documentation, and inclusion.

## AI Tooling Evolution

Use [AI Tooling Evolution](../AI_TOOLING_EVOLUTION.md) for the shared model.

In incident response, AI tooling will reconstruct timelines, summarize logs/chats/tickets, draft stakeholder updates, suggest runbook steps, correlate signals, and prepare post-incident review material.

The risk is speed without command discipline: generated updates or actions can outrun facts, authority, or containment needs. Incident leaders still own severity, command structure, communications approval, evidence preservation, and final decisions during uncertainty.

## Anti-Patterns

- no one knows who is in charge
- severity is decided by whoever sounds most alarmed
- technical responders also improvise all stakeholder communications
- executives bypass incident command and create side channels
- customer updates are delayed until perfect certainty arrives, which it never does
- every incident becomes a blame hunt
- blamelessness is misused to avoid accountability for neglected controls
- postmortems generate action items that no one owns
- incidents are closed when dashboards improve but customers are still affected
- legal, security, privacy, or compliance stakeholders are pulled in too late
- vendor failures are treated as surprises despite visible dependency risk
- responders are burned out and then praised as heroes instead of protected by sane operating design
