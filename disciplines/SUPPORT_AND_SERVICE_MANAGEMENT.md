# Support and Service Management

<!-- doctrine:id=support-and-service-management -->

## Purpose

Support and service management defines how an organization receives, triages, resolves, communicates, learns from, and improves customer or internal service requests without turning every ticket queue into a haunted warehouse of unresolved promises.

It sits between customer management, operations, incident response, product management, sales, engineering, knowledge management, vendor management, and leadership. Support is where product reality, customer expectation, operational quality, and organizational honesty meet each other in a cramped room and try not to throw chairs.

Good support and service management helps an organization:

- give users and customers clear ways to get help
- triage work based on impact, urgency, entitlement, and risk
- resolve issues predictably and visibly
- escalate the right problems at the right time
- communicate clearly during service issues
- maintain useful support knowledge
- prepare support teams before launches and changes
- feed recurring problems back into product, operations, training, and process improvement
- distinguish support work from incident response, customer success, and account management
- measure quality without pretending ticket closure is the same thing as customer value

## Scope

Support and service management may cover:

- support channels and intake
- service catalog and request types
- severity, priority, and triage rules
- response and resolution expectations
- SLAs, SLOs, and service commitments
- queue ownership and workload management
- escalation paths
- customer/user communication
- knowledge base ownership
- support readiness for launches and changes
- support tooling and reporting
- handoffs to engineering, operations, product, sales, customer success, vendors, or partners
- recurring-problem analysis
- outsourced or partner-delivered support
- support quality, coaching, and staffing

The discipline applies to external customer support, internal IT/service desks, platform support, product support, partner support, and specialist support teams. The details differ; the management problems rhyme like badly behaved poetry.

## Support vs Service vs Incident Response

These terms overlap, but they are not identical.

- **Support** handles user/customer questions, issues, defects, access problems, how-to requests, and case resolution.
- **Service management** defines the operating model for repeatable services: catalog, intake, ownership, levels, expectations, workflows, and improvement.
- **Incident response** handles exceptional events where urgency, coordination, risk, customer impact, or operational disruption exceeds normal support flow.
- **Customer success** focuses on adoption, value realization, retention, and expansion readiness.
- **Account management** owns the commercial/account relationship.

Small organizations may combine these roles. Combining roles is fine. Confusing which mode you are in is not.

## Service Catalog and Intake

Users and customers need to know where to go and what to expect.

A useful service catalog defines:

- supported products, systems, or services
- request types
- support channels
- hours of coverage
- eligibility or entitlement
- expected response/resolution targets
- required information for intake
- self-service options
- escalation route
- out-of-scope work

Intake should capture enough information to act without turning the first contact into a tax audit.

Good intake captures:

- requester/customer/account
- affected product/service/environment
- issue summary
- business/customer impact
- urgency and deadline
- error messages/screenshots/logs where relevant
- steps to reproduce
- recent changes
- entitlement/contract context where relevant
- security/privacy/safety/regulatory flags

## Triage and Prioritization

Triage should combine impact, urgency, customer/account context, risk, and service commitments.

Useful triage factors:

- number of users/customers affected
- severity of business/customer impact
- production vs non-production environment
- workaround availability
- contractual or service-level commitment
- security/privacy/compliance risk
- customer escalation state
- revenue/renewal risk
- recurrence or systemic pattern
- internal capacity and specialist availability

Priority should not be determined only by who shouts loudest, has the biggest title, or owns the most dramatic punctuation.

### Severity vs Priority

Severity describes impact. Priority describes order of work.

Example:

- high severity, high priority: production outage affecting many customers
- high severity, lower immediate priority: severe issue in a dormant test environment with no deadline
- lower severity, high priority: small access issue blocking an executive demo tomorrow
- lower severity, lower priority: cosmetic issue with workaround

Keep the distinction visible. Otherwise every ticket becomes P1 because someone discovered adjectives.

## SLAs, SLOs, and Service Commitments

Service expectations should be explicit.

Define:

- response target
- update cadence
- resolution or restoration target where appropriate
- support hours
- escalation rules
- exclusions
- measurement method
- reporting cadence
- approval path for exceptions

Avoid promising resolution times for work that depends on unknown root cause, third-party vendors, customer action, or product changes. Promise response, ownership, investigation, workaround pursuit, communication, and escalation honestly.

SLOs can be better than rigid SLAs for internal services because they focus on operational health and learning rather than contractual punishment.

## Queue Ownership and Workload Management

Support queues need owners.

Define:

- who monitors each queue
- who assigns work
- what happens when work is stale
- handoff rules between teams
- escalation thresholds
- after-hours coverage where relevant
- backlog review cadence
- aging-ticket thresholds
- capacity and staffing assumptions

Unowned queues are organizational compost. Things decay in there.

## Escalation

Escalation should be a workflow, not a panic ritual.

Escalate when:

- impact exceeds normal support authority
- SLA/SLO risk is material
- customer/account risk is high
- safety/security/privacy/regulatory risk appears
- engineering/product/operations/vendor help is required
- customer communication needs senior ownership
- repeated failures indicate systemic issue

An escalation should include:

- issue summary
- customer/user impact
- current status
- timeline
- workarounds
- decisions needed
- owner
- requested help
- next update time

Escalation is not failure. Late, vague, performative escalation is failure with theatre lighting.

## Customer and User Communication

Communication should be clear, timely, and calibrated to the audience.

Good communication:

- acknowledges the issue
- states known impact
- avoids speculation pretending to be certainty
- gives next update time
- explains workaround if available
- names owner or support path
- distinguishes investigation, mitigation, resolution, and prevention
- closes the loop when resolved

Bad communication:

- silence until asked three times
- defensive blame
- vague reassurance
- unexplained status changes
- technical detail that hides the point
- promising root cause before investigation

For major incidents, use incident response communication practices. Support should not improvise a crisis comms strategy while alarms are already eating the furniture.

## Handoffs

Support often depends on other teams.

Common handoffs:

- support to engineering for defects
- support to operations for service degradation
- support to product for feature gaps or usability patterns
- support to customer success/account management for relationship risk
- support to sales for expectation mismatch or expansion context
- support to vendor/partner for third-party dependency
- support to security/privacy/legal for sensitive issues

Good handoffs include:

- problem summary
- customer/user impact
- evidence gathered
- reproduction steps
- logs/screenshots/config details where appropriate
- urgency and due dates
- customer communication state
- suspected owner or component
- what has already been tried

Handoff should transfer accountability clearly. It should not become "we threw it over a wall and now everyone is surprised by gravity."

## Knowledge Management

Support quality depends heavily on knowledge quality.

Support knowledge should cover:

- common issues and fixes
- how-to guidance
- troubleshooting trees
- known limitations
- escalation criteria
- product/service changes
- customer-specific exceptions where appropriate
- incident workarounds
- internal runbooks
- customer-facing articles

Knowledge base ownership should include:

- who creates articles
- who approves them
- when they expire or require review
- how usage and feedback are tracked
- how product/support changes update knowledge
- how outdated articles are retired

A knowledge base full of stale articles is just misinformation with a search box.

## Support Readiness for Launches and Changes

Support must be ready before changes reach customers or users.

Readiness should include:

- what is changing
- expected user/customer impact
- known limitations
- common questions
- troubleshooting guidance
- escalation path
- support staffing/capacity expectations
- updated knowledge articles
- customer communication plan where relevant
- rollback or workaround information
- success/support metrics to watch

Launch readiness without support readiness is optimism outsourcing.

## Recurring Problems and Feedback Loops

Support is a signal system.

Track patterns:

- repeated defects
- confusing workflows
- missing documentation
- onboarding friction
- unsupported but common use cases
- fragile integrations
- training gaps
- configuration errors
- vendor dependency problems
- account-specific special cases

Feedback loops should connect support to:

- product roadmap and discovery
- engineering defect prioritization
- operations reliability work
- customer success adoption work
- sales enablement and expectation-setting
- knowledge management
- training and onboarding
- vendor management

Do not treat every ticket as isolated. Repeated papercuts eventually become a customer-shaped lawsuit against your process.

## Outsourced, Vendor, and Partner Support

When support is outsourced or shared with vendors/partners, define:

- scope of outsourced support
- escalation and handback rules
- service levels
- quality expectations
- access and data boundaries
- customer communication authority
- knowledge sharing
- training and certification
- reporting
- audit and review cadence
- exit/transition plan

Outsourcing support does not outsource accountability. It just adds another place for confusion to breed unless managed.

## Metrics

Useful support metrics may include:

- intake volume by type/channel
- response time
- time to resolution/restoration
- backlog age
- reopen rate
- escalation rate
- SLA/SLO performance
- customer satisfaction/CSAT where useful
- first-contact resolution where appropriate
- defect vs how-to vs request mix
- repeated issue count
- knowledge article usage and deflection
- support load by product/customer segment
- support-driven product improvements

Use metrics carefully. A team can improve closure time by closing badly, improve deflection by hiding contact channels, or improve CSAT by surveying only happy people. Humans remain undefeated at gaming badly designed scoreboards.

## Level-Specific Notes

### Team leads and frontline managers

- coach triage quality and communication clarity
- review aging/stale tickets
- protect focus for high-impact work
- maintain queue hygiene
- identify recurring issues
- ensure handoffs include enough evidence
- support the humans doing emotionally expensive work

### Managers of managers

- define support operating model and queue ownership
- standardize severity/priority rules
- coordinate with product, engineering, operations, customer success, sales, and vendors
- review capacity and staffing patterns
- remove systemic blockers
- improve knowledge and launch-readiness processes

### Directors and senior leaders

- align support model with product/customer strategy
- approve service commitments and escalation models
- review support economics, quality, and risk
- decide when recurring support load requires product/process investment
- ensure customer-impacting support failures are visible in operating reviews

### Executives and founders

- avoid making customer promises the support model cannot satisfy
- fund support capacity before heroic burnout becomes the operating plan
- treat support signals as strategic evidence
- define what service quality means for the business
- model honest customer communication during hard moments

## Common Artifacts

- service catalog
- support intake form
- severity/priority matrix
- SLA/SLO definition
- escalation matrix
- queue review agenda
- support handoff checklist
- launch support readiness checklist
- knowledge article template
- troubleshooting guide
- customer communication template
- recurring-problem review
- support metrics dashboard
- outsourced support operating agreement

## Practitioner Counterpart

For hands-on customer/user support triage, ticket handling, service-level execution, knowledge-base feedback, escalation evidence, and support/service handoffs, see [Support / Service Practitioner](https://github.com/RusDavies/docs-practitioner-practices/blob/master/roles/support-service-practitioner.md). This management guide owns support operating model, service accountability, escalation paths, and improvement decisions.

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

In support and service management, AI tooling will classify tickets, suggest responses, summarize histories, draft knowledge articles, detect recurring problems, route escalations, and monitor SLA/SLO risk. The practical opportunity is faster triage and better feedback loops.

The risk is deflection theatre: bots closing conversations, hiding contact paths, or producing confident answers from stale knowledge. Support leaders still own service quality, escalation policy, customer communication, knowledge freshness, and deciding when empathy beats automation.

## Anti-Patterns

- treating support as a dumping ground for every unclear ownership problem
- measuring support only by ticket closure
- allowing stale queues with no owner
- using priority labels as emotional volume controls
- promising resolution targets without knowing what drives resolution
- launching products without support readiness
- hiding repeated product defects as isolated tickets
- letting sales or executives promise service levels without support/operations approval
- outsourcing support without retaining accountability
- letting knowledge bases rot
- escalating too late or without a clear ask
- confusing customer success, account management, and support responsibilities

## Review Questions

- Do users/customers know where to get help?
- Are request types, ownership, and support scope clear?
- Are severity and priority rules evidence-based?
- Are SLA/SLO commitments realistic and approved?
- Are aging tickets reviewed before they become fossils?
- Do escalations include impact, status, owner, decision needed, and next update?
- Does support have launch/change readiness input?
- Are recurring issues fed back to product, engineering, operations, and knowledge management?
- Are support metrics improving quality or merely improving optics?
- Are support staff protected from becoming the shock absorbers for every upstream management failure?
