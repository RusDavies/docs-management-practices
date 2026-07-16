# Quality Management

<!-- doctrine:id=quality-management -->

## Purpose

Quality management defines how an organization decides what good means, prevents defects where practical, detects problems before they hurt customers or operations, remediates issues when they escape, and learns from failures without turning every mistake into theatre.

It overlaps with product management, delivery, operations, support, security, data and analytics, procurement, supplier management, customer management, compliance, finance, and leadership. That overlap is exactly why quality needs explicit management guidance: otherwise quality becomes something everyone values, nobody owns, and somebody discovers at the end while holding a release checklist and blinking rapidly.

Good quality management helps an organization:

- define quality expectations before work is done
- connect quality to customer/user outcomes and business risk
- build prevention into process and design
- operate practical QA and test models
- govern acceptance criteria and release quality gates
- classify and triage defects consistently
- learn from defects, incidents, complaints, and rework
- manage supplier/customer quality implications
- improve processes without drowning people in process
- decide consciously between prevention, detection, remediation, and accepted risk

## Scope

Quality management may cover:

- quality strategy
- quality standards and expectations
- acceptance criteria discipline
- QA/test operating model
- defect taxonomy and triage
- release and change quality gates
- process quality and continuous improvement
- product/service/data/operational quality
- supplier and outsourced-service quality
- customer-facing quality commitments
- quality metrics and reviews
- quality risk acceptance
- quality evidence and auditability

Quality management is not the same as testing. Testing is one detection mechanism. Quality management is the wider operating discipline that asks whether the organization is building, buying, changing, supporting, and learning in ways that make bad outcomes less likely.

## Quality Strategy

Quality strategy should explain what level of quality matters, where, and why.

Clarify:

- critical products, services, processes, and data
- customer/user expectations
- safety, security, privacy, legal, compliance, or financial obligations
- reliability and availability needs
- acceptable and unacceptable defect classes
- tolerance for rework, downtime, complaints, and operational burden
- cost of prevention vs cost of failure
- quality ownership model
- evidence required before release or acceptance

Not everything needs the same quality bar. A payroll system, medical device, internal experiment, marketing landing page, customer support workflow, and draft prototype do not need identical controls. They do need conscious choices.

Quality strategy is not "zero defects." That is usually slogan-shaped lying. The real question is which defects are intolerable, which are acceptable temporarily, and who is allowed to make that call.

## Quality Dimensions

Quality is multi-dimensional.

Consider:

- correctness
- reliability
- usability
- accessibility
- performance
- security
- privacy
- safety
- maintainability
- operability
- supportability
- compliance
- data quality
- documentation quality
- customer experience
- process consistency
- cost and waste

The relevant dimensions depend on the work. A service may be technically correct and still poor quality if users cannot understand it, support cannot troubleshoot it, or operations must sacrifice a goat every Tuesday to keep it alive.

## Acceptance Criteria Discipline

Acceptance criteria define what must be true for work to be accepted.

Good acceptance criteria are:

- tied to the intended outcome
- clear enough to test or inspect
- understandable by delivery and business stakeholders
- explicit about non-functional expectations where relevant
- linked to risks and constraints
- agreed before final acceptance
- updated when scope changes

Acceptance criteria may cover:

- functional behavior
- user workflow completion
- error handling
- performance thresholds
- security/privacy expectations
- operational readiness
- support/documentation readiness
- data/reporting behavior
- accessibility
- compliance evidence
- rollback or recovery requirements

Weak acceptance criteria:

> Works as expected.

Better acceptance criteria:

> A support manager can filter unresolved high-priority tickets by customer tier, export the list, and see data no more than 15 minutes old. Access is limited to support managers and audited.

The second version can be tested. The first version is an argument seed.

## QA and Test Operating Model

A QA/test operating model should define how quality is checked and who owns which checks.

Clarify:

- who writes and maintains tests/checks
- who performs exploratory, regression, user acceptance, operational, security, data, and compliance checks
- what is automated vs manual
- when testing happens in the lifecycle
- required environments and test data
- defect reporting and triage paths
- release/blocking criteria
- evidence captured
- residual risk approval

Testing should shift left where practical, but not as a slogan. Some issues are best prevented in design, some found through automated checks, some found through exploratory review, and some only appear in production signals. Mature quality management uses multiple nets instead of arguing that one net is morally superior.

## Prevention, Detection, Remediation, and Acceptance

Quality work has four broad modes.

### Prevention

Prevent problems through:

- good requirements and acceptance criteria
- design review
- architecture review
- standards and reusable patterns
- training/coaching
- supplier qualification
- automation and guardrails
- code review/change review
- data validation
- process simplification

### Detection

Detect problems through:

- automated tests/checks
- manual testing
- peer review
- inspections
- monitoring and observability
- audits
- support ticket analysis
- customer feedback
- data-quality checks
- incident/problem review

### Remediation

Remediate through:

- defect fixing
- rollback
- customer remediation
- process correction
- supplier corrective action
- data repair
- control improvement
- documentation/training updates

### Acceptance

Accept residual quality risk only when:

- the risk is explicit
- the owner has authority
- mitigation or monitoring is defined where needed
- the time horizon is clear
- the decision is revisited

Unaccepted quality risk is just drift with a nicer haircut.

## Defect Taxonomy and Triage

Defects should be classified consistently.

Useful classification dimensions:

- severity: consequence if the defect occurs
- priority: urgency to address
- impact: customers/users/processes affected
- scope: isolated vs systemic
- source: requirement, design, implementation, supplier, data, process, training, environment, documentation
- detectability: how likely controls are to catch it
- recurrence: first-time vs repeated pattern
- exposure: internal, customer-facing, public, regulated, security-sensitive
- status: new, confirmed, mitigated, accepted, remediated, verified, closed

Severity and priority are not the same thing.

Example:

- high severity / low immediate priority: serious issue in a dormant test environment with no active users
- lower severity / high priority: minor customer-facing defect affecting a launch demo tomorrow

Triage should decide:

- immediate containment needed?
- customer/user communication needed?
- release blocked?
- workaround available?
- owner assigned?
- root-cause review needed?
- prevention change required?

## Release and Change Quality Gates

Quality gates should be decision gates, not paperwork gates.

Useful gates may include:

- requirements/acceptance readiness
- design/architecture review
- security/privacy review
- test plan readiness
- test evidence review
- defect threshold review
- operational readiness
- support readiness
- documentation/training readiness
- rollback/recovery readiness
- compliance/legal evidence review
- business/product acceptance

A gate should answer:

- What decision is being made?
- What evidence supports it?
- What defects/risks remain?
- Who can accept those risks?
- What changes if the gate fails?

A quality gate that cannot stop or change anything is not a gate. It is a ceremonial archway.

## Process Quality and Continuous Improvement

Process quality asks whether the way work is done creates reliable outcomes.

Review:

- recurring defects
- rework and escaped defects
- unclear ownership
- late requirement changes
- handoff failures
- supplier defects
- support/contact drivers
- incident and problem records
- audit findings
- customer complaints
- data-quality issues
- cycle time and bottlenecks

Continuous improvement should focus on root causes and constraint removal, not motivational posters. Useful changes may include:

- simplifying steps
- clarifying ownership
- improving acceptance criteria
- adding targeted automation
- removing duplicated handoffs
- changing supplier controls
- improving training
- updating standards/templates
- making quality evidence easier to collect

If the improvement process creates more waste than the defects it prevents, congratulations, the cure has become a subscription product.

## Supplier and Outsourced Quality

Suppliers, vendors, partners, and outsourced teams can create or reduce quality risk.

Manage:

- quality expectations in contracts/statements of work
- acceptance criteria
- deliverable review and acceptance
- service levels
- defect response obligations
- evidence requirements
- audit/inspection rights where appropriate
- corrective-action process
- handoff and documentation quality
- data/security/privacy quality implications

Do not outsource accountability. You can outsource work. The customer will still blame you, because the customer is annoyingly correct.

## Customer-Facing Quality

Customer-facing quality includes more than absence of defects.

Consider:

- fit to promised use case
- reliability of service
- clarity of communication
- supportability
- onboarding experience
- documentation accuracy
- accessibility and usability
- response to issues
- consistency between sales/marketing promises and delivered reality
- fairness and trustworthiness where decisions affect people

Customer quality signals include:

- complaints
- support tickets
- churn/cancellation reasons
- adoption drop-offs
- refunds/credits
- renewal objections
- NPS/CSAT/CES with caveats
- public reviews/community feedback
- incident communications

Do not reduce customer quality to satisfaction surveys. People can be satisfied for the wrong reason, dissatisfied because of honest constraints, or too exhausted to answer the survey because the product has already eaten their afternoon.

## Quality Metrics

Quality metrics should connect to outcomes and decisions.

Useful metrics may include:

- escaped defects
- defect severity mix
- defect recurrence
- time to detect
- time to remediate
- rework rate
- release rollback rate
- change failure rate
- support/contact drivers
- customer-impacting incidents
- test/check coverage for critical paths
- acceptance criteria quality/completeness
- audit findings
- supplier defect rate
- data-quality defects
- process bottlenecks causing quality risk

Use metrics carefully. Teams optimize what leadership rewards. If you reward fewer reported defects, you may get fewer reported defects. This is not the same as higher quality; it is a very small crime against visibility.

## Quality Reviews and Operating Cadence

Quality should be reviewed at the right cadence.

Examples:

- sprint/iteration review of acceptance and defects
- release readiness review
- monthly defect trend review
- support/contact-driver review
- supplier quality review
- incident/problem review
- quarterly process-quality review
- annual standard/control review

Reviews should ask:

- What quality risks are increasing?
- What defects are recurring?
- What prevention would reduce the most pain?
- Are gates finding issues early enough?
- Are teams hiding risk to hit dates?
- Are customers experiencing quality differently than internal metrics suggest?

## Level-Specific Notes

### Team leads and frontline managers

- clarify acceptance criteria before work is considered done
- make defects visible without blame theatre
- coach prevention and review habits
- use testing/checks appropriate to the work
- escalate repeated defects and systemic blockers
- protect time for quality work when quality risk is real

### Managers of managers

- standardize quality expectations across teams where useful
- review defect trends and escaped issues
- ensure release/support/operations readiness gates work
- remove incentives that reward hiding defects
- coordinate quality improvements across handoffs

### Directors and senior leaders

- define quality strategy and risk tolerance
- align quality investment with customer/business/regulatory risk
- review systemic quality signals across product, support, operations, suppliers, and data
- approve material quality risk acceptance
- fund prevention where repeated remediation is wasting capacity

### Executives

- avoid demanding speed while punishing teams for predictable quality failures
- make quality tradeoffs explicit
- sponsor quality foundations for critical products/services/processes
- ask whether metrics reflect customer reality
- treat severe quality failures as management-system failures, not only team failures

## Common Artifacts

- quality strategy
- quality standards
- acceptance criteria checklist
- QA/test strategy
- release quality gate checklist
- defect taxonomy
- defect triage log
- quality risk acceptance record
- root-cause/problem review
- corrective and preventive action plan
- supplier quality scorecard
- customer quality signal review
- quality metrics dashboard
- process improvement backlog

## Practitioner Counterpart

For hands-on test design, exploratory/regression testing, test data, harnesses, reproducibility, defect evidence, and quality signals, see [QA / Test Practitioner](https://github.com/RusDavies/docs-practitioner-practices/blob/master/roles/qa-test-practitioner.md). This management guide owns quality strategy, acceptance-risk framing, release gates, and governance.

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

In quality management, AI tooling will draft acceptance criteria, generate test ideas, inspect defects, cluster root causes, monitor quality signals, and assemble release evidence. The practical opportunity is earlier detection and better prevention.

The risk is quality by generated checklist: many checks, weak judgment, and false confidence. Quality leaders still own quality strategy, release gates, defect classification, residual risk acceptance, and deciding whether evidence is strong enough to proceed.

## Anti-Patterns

- treating quality as the tester's problem
- discovering acceptance criteria at acceptance time
- using gates that cannot affect decisions
- rewarding teams for hiding or reclassifying defects
- confusing testing volume with quality confidence
- fixing escaped defects without addressing recurrence
- shipping poor quality because support can absorb it
- accepting supplier deliverables without evidence
- using customer satisfaction as the only quality signal
- applying the same heavy process to every risk level
- letting deadlines silently overrule quality thresholds
- treating quality documentation as proof of quality

## Review Questions

- What does good mean for this product, service, process, or data?
- Which quality dimensions matter most here?
- Are acceptance criteria clear and testable?
- Which defects would block release or acceptance?
- What quality risks are being prevented, detected, remediated, or accepted?
- Who can accept remaining quality risk?
- Are defect severity and priority being classified consistently?
- Are quality gates tied to real decisions and evidence?
- What recurring defects or rework indicate a process problem?
- Are suppliers and outsourced teams meeting quality expectations?
- Do internal quality metrics match customer/user experience?
