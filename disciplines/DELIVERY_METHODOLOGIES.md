# Delivery Methodologies

<!-- doctrine:id=delivery-methodologies -->

## Purpose

Delivery methodology guidance helps managers choose an execution model that fits the work instead of forcing every project through the fashionable ritual of the month.

Waterfall, agile, Scrum, Kanban, staged delivery, hybrid models, and ad hoc delivery all have places where they are useful. They also have places where they become expensive theatre.

The management responsibility is not to worship a methodology. It is to choose and operate a delivery approach that matches uncertainty, constraints, risk, stakeholder needs, feedback speed, and the cost of change.

## First Principle

Choose the method based on the nature of the work:

- How well-known are the requirements?
- How fixed are scope, budget, and schedule?
- How costly is late change?
- How fast can the team get feedback?
- How risky is failure?
- How many stakeholders must coordinate?
- How much discovery remains?
- How regulated, contractual, or safety-critical is the work?
- How much interruption or reactive work will arrive during delivery?
- How easily can the work be sliced into useful increments?

A methodology is a management tool. If it becomes an identity, congratulations, you have invented a tiny religion with standups.

## Method Selection by Context

Do not ask, "Are we agile?" Ask what the work needs.

### High Certainty / High Change Cost

Examples:

- office move or data-centre migration with fixed outage windows
- regulatory evidence remediation with known control gaps
- hardware rollout with procurement and installation dependencies
- customer migration where rollback windows and communication dates are fixed

Usually prefer:

- waterfall or staged delivery
- explicit phase gates
- detailed dependency planning
- formal change control
- early test/acceptance planning

Use agile practices inside the work where helpful, but do not pretend the whole effort is flexible if the deadline, cutover, or regulatory date is immovable.

### High Uncertainty / Fast Feedback

Examples:

- new product feature discovery
- internal tool where users can test weekly
- customer onboarding improvement
- AI workflow prototype with unknown quality thresholds
- analytics/reporting product where stakeholders need to see examples before deciding

Usually prefer:

- agile delivery
- Scrum where a stable cross-functional team and product owner exist
- short feedback loops
- discovery, prototypes, demos, and iteration
- adaptive scope

The management question is whether evidence changes the plan. If feedback cannot change anything, the process is not really agile; it is a demo-shaped status meeting.

### Continuous Intake / Operational Flow

Examples:

- production support queue
- platform maintenance
- security triage
- data-quality issue queue
- customer-service process improvements
- small enhancement requests competing with interrupts

Usually prefer:

- Kanban or flow-based delivery
- work-in-progress limits
- explicit classes of service
- triage policies
- blocked-work escalation
- cycle-time review

Do not force sprint commitments onto a team whose work is mostly interrupts unless you are also controlling the interrupts. Otherwise the sprint plan is just a decorative lie with burndown charts.

### Mixed Discovery and Governance

Examples:

- regulated digital product
- enterprise system implementation
- major vendor/SaaS rollout
- AI-enabled customer workflow
- payment, identity, or personal-data platform change
- large modernization programme with funding checkpoints

Usually prefer:

- hybrid or stage-gated agile
- governance gates for decision evidence
- iterative delivery inside stages
- explicit risk, security, privacy, compliance, and operational reviews
- regular stakeholder demos tied to real decisions

The healthy hybrid keeps learning loops while satisfying governance. The unhealthy hybrid combines the paperwork of waterfall with the predictability of a raccoon in a ceiling cavity.

## Common Delivery Approaches

### Waterfall / Sequential Delivery

Best considered when:

- requirements are well understood and stable
- scope, budget, and schedule are fixed or contractually constrained
- dependencies require ordered phases
- late change is expensive
- approval gates are mandatory
- regulated, construction-like, hardware, migration, or compliance-heavy work requires evidence at defined stages

Good use:

- upfront requirements and design are real, not decorative
- change control is explicit
- stakeholders understand tradeoffs
- testing and acceptance are planned early
- phase gates reduce risk rather than merely delay work
- the plan includes rollback, transition, and operational readiness where relevant

Example:

A payroll-system migration with a statutory deadline, controlled data conversion, vendor dependencies, parallel-run testing, employee communications, and go/no-go gates should use staged delivery. Agile ceremonies may help the team manage work, but the overall effort needs sequencing, evidence, cutover governance, and change control.

Anti-patterns:

- pretending uncertain work is certain because leadership wants a date
- using waterfall to avoid customer/user feedback
- freezing bad requirements because the document was signed
- discovering quality only at the end
- treating change control as a punishment system rather than a decision mechanism

### Agile Delivery

Best considered when:

- requirements are uncertain or evolving
- user/customer feedback is available and valuable
- the product can be delivered incrementally
- learning matters more than pretending to know everything upfront
- priorities may shift as evidence emerges
- the cost of change is manageable

Good use:

- teams deliver small increments
- feedback changes decisions
- product ownership is active
- quality practices are built in
- scope is adaptable within real constraints
- stakeholders accept that discovery may change the plan
- outcomes are reviewed, not only ticket throughput

Example:

A team building a self-service customer portal may know the broad business goal but not the best user journey. Agile delivery fits if the team can release or demo increments, observe user behaviour, refine priorities, and adjust scope as evidence emerges.

Anti-patterns:

- fixed scope, fixed budget, fixed schedule, but calling it agile because meetings happen every two weeks
- using agile vocabulary to avoid planning
- treating story points as contractual productivity units
- changing priorities constantly and blaming the team for lack of predictability
- shipping fragments without coherent product outcomes
- confusing activity with learning

### Scrum

Best considered when:

- a cross-functional team can work in short iterations
- there is a real product owner or equivalent decision-maker
- backlog refinement and prioritization can happen continuously
- the team can inspect and adapt its work
- sprint boundaries help focus and learning
- interruptions can be managed or deliberately reserved as capacity

Good use:

- sprint goals are meaningful
- retrospectives produce real changes
- product ownership is present
- the team is protected from random interruption
- increments are potentially releasable or at least inspectable
- sprint planning reflects capacity, dependencies, and uncertainty honestly

Example:

A product team improving onboarding conversion can use Scrum well if it has design, engineering, analytics, and product decision-making close enough to deliver small increments, review real funnel/user evidence, and adapt sprint goals.

Anti-patterns:

- cargo-cult ceremonies without empowered decisions
- daily standups as manager status extraction
- sprint commitments treated as punishment contracts
- Scrum imposed on work that is mostly reactive operations
- Scrum master as calendar priest instead of impediment remover
- product owner as backlog secretary with no decision rights

### Kanban / Flow-Based Delivery

Best considered when:

- work arrives continuously
- priorities shift frequently
- cycle time and throughput matter
- operations, support, maintenance, triage, or platform work dominates
- limiting work in progress would improve delivery
- service classes differ by urgency or impact

Good use:

- work-in-progress limits are real
- flow metrics are reviewed
- bottlenecks are addressed
- classes of service are explicit
- blocked work is visible
- intake and replenishment are deliberate
- aging work is reviewed before it quietly fossilizes

Example:

A platform team handling access requests, small infrastructure improvements, incident follow-ups, dependency updates, and operational tickets is often better served by Kanban than Scrum. The team can manage flow, limit WIP, triage urgent work, and improve cycle time without pretending every two-week box is predictable.

Anti-patterns:

- a board that is just a graveyard of sticky notes
- no WIP limits
- no ownership of blocked work
- using Kanban to avoid prioritization
- measuring only throughput while high-risk work ages in a corner
- letting every requester define their own emergency

### Hybrid / Stage-Gated Agile

Best considered when:

- governance requires milestones or approvals
- discovery and iterative delivery are still valuable
- external commitments require defined checkpoints
- the organization needs both learning loops and executive visibility
- security, privacy, compliance, procurement, architecture, or operational readiness reviews are material

Good use:

- stage gates define decisions and evidence, not fake certainty
- teams still iterate inside stages
- change control is honest
- stakeholder reviews are tied to real risk and investment decisions
- governance roles are clear
- evidence is generated during work, not assembled during ritual panic week

Example:

A regulated AI-assisted support workflow may need iterative design and evaluation with support agents, but also privacy review, security review, model/provider approval, quality evaluation, operational readiness, training, and executive signoff before production rollout. Hybrid delivery fits: iterate inside clear governance stages.

Anti-patterns:

- worst-of-both-worlds: waterfall commitments plus agile chaos
- pretending every sprint is flexible while the contract says otherwise
- governance gates that review paperwork instead of decision-quality evidence
- stage gates so heavy that teams hide real learning until too late
- agile teams forced to maintain two parallel realities: working backlog and executive theatre plan

## Fixed Scope, Budget, and Schedule

If scope, budget, and schedule are all fixed, the project is not meaningfully agile in the usual sense.

That does not mean agile practices are useless. Short iterations, demos, retrospectives, automated testing, backlog visibility, and frequent feedback can still improve execution.

But management should be honest:

- call the delivery model constrained/staged/iterative, not fully agile
- define which constraint can move if reality disagrees
- manage changes through explicit tradeoffs
- do not sell adaptability while refusing to adapt
- document who owns tradeoff decisions

The anti-pattern is avoiding planning and calling it agile.

## Choosing Between Scrum and Kanban

Scrum and Kanban are often confused because both may use boards and short conversations. The management difference is the work pattern.

Prefer Scrum when:

- a stable team can pursue a sprint goal
- work can be planned for an iteration
- product ownership is active
- feedback at iteration boundaries is valuable
- interruptions are limited or deliberately budgeted

Prefer Kanban when:

- work arrives unpredictably
- request classes have different urgency
- flow and cycle time matter more than sprint goals
- interruption is part of the job
- bottleneck management is the main improvement lever

Use both carefully when needed. A product team might use Scrum for feature delivery and a Kanban lane for urgent production defects. Make the policy explicit; otherwise the urgent lane becomes a trapdoor under every sprint.

## Method Selection Guide

Use waterfall or staged delivery when:

- requirements are known
- change is expensive
- commitments are contractual
- compliance evidence matters
- phase approval is necessary

Use agile/Scrum when:

- requirements are uncertain
- feedback can change the answer
- incremental delivery is possible
- product ownership is active
- scope can adapt

Use Kanban when:

- work is continuous or interrupt-driven
- flow, WIP, and cycle time matter
- planning by sprint would add friction without value

Use hybrid when:

- governance and learning both matter
- stakeholders need stage gates
- teams still need iteration inside those gates

Do not select a method because it sounds mature, modern, safe, or fashionable. Select it because the assumptions match the work.

## Management Responsibilities

Managers should:

- choose the delivery model explicitly
- explain why it fits the work
- identify constraints honestly
- define decision rights and change rules
- inspect whether the method is helping
- adapt the method when evidence shows a mismatch
- protect teams from methodology churn
- ensure stakeholders understand what the selected method can and cannot promise

Managers should not:

- impose methodology as fashion
- hide fixed commitments behind agile language
- use process vocabulary to avoid hard tradeoffs
- punish teams for constraints leadership created
- demand predictability while changing priorities without tradeoffs
- outsource delivery-method decisions to consultants, tools, or certification slogans

## Disagree and Commit

Methodology selection should allow real disagreement before the decision.

People should be able to say:

- the requirements are not actually stable
- the delivery date is fiction
- the budget cannot support the scope
- the team cannot absorb uncontrolled change
- the chosen method does not fit the work
- the governance burden exceeds the actual risk
- the organization wants agile feedback but not agile tradeoffs

Once the delivery model is chosen, the team should commit to operating it honestly. If the assumptions break, re-open the decision with evidence rather than quietly mutating the method into nonsense.

## Common Artifacts

- delivery approach decision record
- project brief
- roadmap or milestone plan
- backlog or work queue
- risk/issue/dependency register
- change-control record
- sprint/iteration plan where applicable
- flow metrics where applicable
- retrospective notes
- release/readiness checklist
- dependency map
- decision log for method changes


### Template Pack

Use these starter templates when delivery-method guidance needs to become explicit decisions, operating rules, and review evidence:

- [Delivery Approach Decision Record](../templates/delivery-approach-decision-record.md) — records why a delivery model fits the work, what it can and cannot promise, and when to revisit the choice.
- [Delivery Method-Fit Checklist](../templates/delivery-method-fit-checklist.md) — assesses uncertainty, constraints, feedback speed, interruption load, governance, and team shape before selecting a method.
- [Change-Control Record](../templates/change-control-record.md) — records material changes to scope, schedule, budget, quality, risk, governance, or delivery model.
- [Flow Metrics Review](../templates/flow-metrics-review.md) — reviews WIP, cycle time, blocked work, aging items, classes of service, bottlenecks, and improvement actions.
- [Sprint / Iteration Health Review](../templates/sprint-iteration-health-review.md) — checks whether iteration-based work is producing focus, feedback, quality, and sustainable delivery.

These templates are methodology-neutral by design. Use the lightest artifact that makes the delivery tradeoff visible; do not force every team to cosplay as a project-management certification exam.

## Adjacent Practitioner / Operator Handoffs

Delivery-method execution is handled through adjacent roles rather than a standalone delivery-method practitioner. Use [Project Coordinator / Operator](https://github.com/RusDavies/docs-practitioner-practices/blob/master/roles/project-coordinator-operator.md), [Program Coordinator / Operator](https://github.com/RusDavies/docs-practitioner-practices/blob/master/roles/program-coordinator-operator.md), [Product Practitioner](https://github.com/RusDavies/docs-practitioner-practices/blob/master/roles/product-practitioner.md), and [Operations Operator](https://github.com/RusDavies/docs-practitioner-practices/blob/master/roles/operations-operator.md) for the execution evidence that supports delivery-method decisions.

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

In delivery methodology, AI tooling will help translate work between briefs, tickets, tests, release notes, retrospectives, and evidence packets. It can also inspect flow, detect bottlenecks, propose WIP or sequencing changes, summarize risks, and generate checks for acceptance criteria.

The leverage is useful: AI can reduce artifact drag and make inconsistent plans more visible.

The risk is methodology laundering: AI makes a bad delivery model look coherent by producing tidy artifacts. Managers still own choosing the right delivery approach, exposing constraints honestly, and deciding when evidence should change the plan.

## Anti-Patterns

Watch for these failure modes:

- agile-in-name-only for fixed-scope/fixed-budget/fixed-schedule work
- waterfall-in-denial for work with major uncertainty
- Scrum ceremonies without product ownership
- Kanban boards without WIP limits or flow management
- hybrid delivery that combines all overhead and no learning
- methodology chosen by executive fashion rather than work characteristics
- story points used as productivity surveillance
- velocity treated as a promise rather than a planning signal
- retrospectives that produce no management action
- change control used to punish learning rather than govern tradeoffs
- governance gates that reward polished evidence over true readiness
- delivery dashboards that hide blocked, risky, or aging work
- consultants imposing a branded method without adapting to the work
- teams forced to report one method while operating another to survive

## Practical Starting Point

For a new piece of work, ask:

1. What is known, unknown, fixed, and negotiable?
2. Who can give useful feedback, and how often?
3. What is the cost of late change?
4. What evidence, approvals, or governance gates are required?
5. How much interruption or reactive work will arrive?
6. Which delivery model best fits those facts?
7. What would prove the selected model is wrong?
8. When will the team review whether the method is helping?

The answer does not need to be fashionable. It needs to be honest enough that people can manage the work instead of managing the fiction around the work.
