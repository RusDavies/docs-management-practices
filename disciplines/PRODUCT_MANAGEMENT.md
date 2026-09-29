# Product Management

<!-- doctrine:id=product-management -->

## Purpose

Product management makes sure the organization builds the right thing, for the right users or customers, with a credible path to adoption, value, and sustained operation.

It sits between customer reality, business strategy, technical feasibility, delivery execution, operations, commercial motion, and go-to-market. Which is a fancy way of saying product management gets blamed by everyone unless it is unusually clear.

Good product management helps an organization:

- understand customers, users, buyers, and market context
- frame problems before prescribing solutions
- choose product outcomes worth pursuing
- prioritize based on value, risk, effort, timing, strategy, and learning
- create roadmaps that communicate intent and tradeoffs
- partner with design, engineering, operations, security, legal, finance, sales, customer success, support, and marketing
- prepare products for launch, adoption, support, and learning
- manage product lifecycle decisions after launch
- stop work that no longer deserves investment

Product management is not idea collection with a nicer title. It is the discipline of making product bets explicit, testable, deliverable, and accountable.

## When to Use Product Management

Use product-management discipline when work involves:

- customer or user problems
- product strategy or roadmap decisions
- feature prioritization
- market, segment, or buyer choices
- product discovery and validation
- pricing, packaging, or commercial input
- launch readiness and go-to-market coordination
- product analytics and feedback loops
- product lifecycle decisions: grow, maintain, reposition, deprecate, sunset

The discipline applies to commercial products, internal platforms, shared services, data products, AI tools, documentation products, operational tooling, and employee-facing systems. If people use it, depend on it, pay for it, operate it, or complain about it in oddly specific terms, product management probably belongs somewhere in the conversation.

## Core Responsibilities

Product management is accountable for clarifying:

- target users, buyers, customers, and stakeholders
- problem/opportunity framing
- product strategy and intended outcomes
- discovery and validation approach
- priority decisions and tradeoffs
- roadmap intent
- requirements and acceptance criteria at the right level
- delivery partnership and scope decisions
- launch scope and readiness
- adoption, feedback, and success metrics
- lifecycle and retirement decisions

Product management does not own every activity alone. It is responsible for ensuring the product decision system works.

## What Good Looks Like

Healthy product management usually shows these signs:

- customer/user problems are specific and evidenced
- strategy explains tradeoffs, not just ambition
- discovery reduces uncertainty before major commitments
- roadmap decisions connect to outcomes and constraints
- delivery teams understand the problem, not only the requested feature
- launch readiness includes sales, support, operations, security/privacy, and customer-success needs where relevant
- metrics show adoption, value, quality, and learning
- product decisions are documented when they affect scope, customer commitments, risk, or strategy
- feedback changes the roadmap when evidence warrants it
- lifecycle decisions are active, including deprecation and sunset

Good product management does not make everyone happy. It makes better product choices and explains why the other attractive-but-wrong choices were not chosen. Charming, in a mildly career-limiting way.

## Product Strategy

Good product strategy clarifies:

- who the product is for
- what problem it solves
- why now
- why this organization can win or serve well
- what tradeoffs are intentional
- what success means
- what will not be pursued
- what constraints matter

### Strategy Inputs

Useful inputs include:

- customer/user evidence
- market and competitor signals
- business strategy
- revenue, retention, cost, or mission objectives
- technical capability and constraints
- operational/support model
- regulatory/security/privacy context
- vendor/platform dependencies
- current product performance
- organization capacity

### Strategy Example

Product: self-service customer onboarding portal

Strategic choice:

- serve mid-market customers who need predictable onboarding more than bespoke implementation
- reduce manual onboarding work before expanding sales capacity
- prioritize repeatable workflow, supportability, and measurable time-to-value over highly customized enterprise workflows
- exclude complex enterprise migration tooling from the first release

That is a strategy because it says yes and no. A strategy that only says yes is usually a wish list wearing a blazer.

## Problem Framing

Product work should start with problem clarity.

Good problem framing answers:

- Who has the problem?
- What are they trying to do?
- What pain, risk, cost, delay, or missed opportunity exists?
- How often does it occur?
- How severe is it?
- What workaround exists today?
- What evidence supports this?
- Why should the organization care now?

Weak framing:

> Customers want a dashboard.

Better framing:

> Operations managers cannot see onboarding bottlenecks until customers complain. The current workaround is a weekly spreadsheet assembled manually by Customer Success. This delays intervention by 3-5 days and contributes to missed onboarding commitments for larger customers.

The second one still might lead to a dashboard. It might also lead to workflow alerts, process changes, reporting cleanup, or fewer spreadsheet goblins.

## Discovery and Validation

Product discovery should reduce uncertainty before large commitments.

Use:

- customer/user interviews
- problem validation
- prototype tests
- usability testing
- market and competitor research
- technical feasibility review
- operational/support review
- pricing and willingness-to-pay signals where relevant
- data analysis of adoption, usage, churn, support tickets, sales loss reasons, or process defects

### Discovery Questions

Ask:

- Is this a real problem?
- Is it painful enough to matter?
- Who experiences it and who buys/approves the solution?
- What alternatives or workarounds exist?
- What would success look like to the user/customer?
- What constraints could make a solution fail?
- What is the smallest credible test?
- What must be learned before a larger investment?

### Validation Examples

For a new reporting feature:

- interview operations managers about decisions they make from reports
- review support tickets requesting data exports
- prototype the report with realistic data
- test whether users can answer key questions without help
- verify data freshness and ownership with data/engineering teams
- validate whether sales is promising the feature to specific customers

For an internal AI assistant:

- validate the actual workflow pain
- identify data classes exposed through prompts/files
- test answer quality against known cases
- evaluate hallucination/fabrication risk
- confirm human review requirements
- measure time saved per useful outcome

Discovery is not a ceremonial preface to the feature someone already decided to build. If discovery cannot change the decision, call it what it is: theatre with interview notes.

## Prioritization

Prioritization should explain why one thing matters more than another.

Inputs:

- customer/user value
- business value
- strategic fit
- risk reduction
- learning value
- effort and complexity
- urgency and timing
- dependencies
- technical/operational constraints
- revenue, retention, cost, or mission impact
- regulatory/security/compliance needs

### Prioritization Patterns

Useful patterns:

- outcome-based prioritization: which work best advances the product outcome?
- risk-first prioritization: which uncertainty must be reduced before commitment?
- opportunity sizing: how many users/customers are affected and how badly?
- cost-of-delay thinking: what is the cost of waiting?
- dependency-aware sequencing: what unlocks other valuable work?
- product-health prioritization: where reliability, usability, support burden, or technical debt threatens value?

Avoid prioritization models that produce a number nobody trusts but everyone pretends is science. Scoring is useful when it supports judgment. It is ridiculous when it replaces judgment.

## Roadmap Management

A roadmap should communicate intent, sequencing, assumptions, and tradeoffs. It should not be a fantasy delivery calendar laminated for stakeholder comfort.

A useful roadmap shows:

- outcomes or themes
- major bets or initiatives
- current/next/later sequencing
- known constraints
- key dependencies
- discovery/investment decisions
- confidence level
- review cadence

### Roadmap Example

Theme: reduce onboarding time-to-value

- Now: simplify intake workflow, add onboarding status visibility, measure handoff delays
- Next: automate routine customer notifications, pilot support readiness checklist, improve account setup integration
- Later: evaluate advanced self-service configuration for larger customers after adoption data confirms demand

This roadmap tells a story of learning and sequencing. It does not pretend the future signed a contract.

## Requirements and Acceptance Criteria

Product requirements should describe the outcome, user need, constraints, and acceptance criteria clearly enough for delivery partners to solve the problem.

Good requirements include:

- user/customer problem
- target user/persona or role
- desired outcome
- scope and non-scope
- functional needs
- non-functional needs where relevant: performance, security, privacy, accessibility, reliability, supportability
- acceptance criteria
- analytics/measurement needs
- rollout/launch considerations
- open questions

Avoid requirements that are just UI instructions written before anyone understands the work. That is not product management. That is premature interior decorating.

## Delivery Partnership

Product management does not throw requirements over a wall. It partners with delivery teams to clarify outcomes, constraints, tradeoffs, and acceptance criteria.

Good delivery partnership includes:

- shared understanding of problem and outcome
- feasibility review before commitment
- architecture and operational implications considered early
- scope tradeoffs discussed openly
- delivery risks surfaced without punishment
- customer commitments made visible
- launch/adoption needs considered before the end
- decisions recorded when material

Product, design, engineering, operations, security, and support are not sequential filing cabinets. They are collaborators protecting different parts of the outcome.

## Go-To-Market and Launch Readiness

Product management should cover the go-to-market end of the wedge: not by replacing marketing, sales, or customer success, but by ensuring the product is launchable, explainable, sellable, supportable, and able to learn from market response.

Product management owns or strongly contributes to:

- ideal customer profile / target user clarity
- market and segment understanding
- positioning inputs
- value proposition and differentiation
- pricing and packaging inputs
- launch scope and readiness criteria
- beta/pilot learning goals
- sales and customer-success enablement inputs
- onboarding/adoption requirements
- product analytics and feedback loops
- post-launch adoption, retention, and expansion signals

Product management usually does not solely own:

- brand strategy
- demand generation execution
- sales execution
- PR and communications
- customer success operations
- revenue targets without shared commercial ownership

### Launch Readiness Questions

Before launch, product should be able to answer:

- Who is this for?
- What problem does it solve?
- Why should the buyer/user care now?
- What is included and excluded from this release?
- What must be true for sales, support, and operations to succeed?
- What objections are expected?
- What feedback will be collected after launch?
- What signals decide whether to continue, change, or stop?
- What support and escalation paths are ready?
- What security/privacy/legal/compliance review is required?
- What analytics are in place?
- What launch risks are accepted, and by whom?

### Launch Readiness Example

Product: customer onboarding status dashboard

Launch scope:

- show onboarding stages and blockers for Customer Success and Operations
- pilot with 12 mid-market accounts
- exclude enterprise custom implementation workflows

Readiness checks:

- Support has troubleshooting script
- Customer Success has pilot customer selection and talking points
- Sales knows not to sell it as a real-time enterprise implementation dashboard
- Operations has owner for workflow-stage definitions
- Engineering has monitoring for data freshness
- Product has adoption and task-completion metrics
- Privacy confirms no sensitive implementation notes are exposed

Expected objections:

- customers may ask for export/reporting features
- enterprise sales may request custom fields
- operations may dispute workflow-stage naming

Feedback loop:

- pilot review after four weeks
- measure active usage, onboarding delay reduction, support questions, and customer feedback
- decide whether to expand, revise, or stop

## Beta, Pilot, and Rollout Management

Use beta/pilot/rollout stages to learn and reduce risk, not to hide unfinished work behind nicer labels.

Clarify:

- pilot purpose
- target participants
- entry criteria
- exit criteria
- support path
- feedback channels
- known limitations
- rollback/withdrawal path
- decision after pilot

### Pilot Example

Pilot objective: determine whether self-service onboarding reduces setup calls without increasing support defects.

Participants: 10 customers with simple onboarding paths.

Exit criteria:

- at least 70% complete onboarding without live support
- no high-severity support defects
- average time-to-value reduced by at least 30%
- customer feedback indicates instructions are understandable

Decision:

- expand to broader segment, revise onboarding flow, or return to discovery

## Pricing and Packaging Input

Product management often provides input to pricing and packaging even when Finance, Sales, or Commercial leadership owns the final decision.

Product should contribute:

- customer value evidence
- segment differences
- willingness-to-pay signals
- feature/package boundaries
- competitive alternatives
- adoption and retention signals
- support/operating cost implications
- risk of packaging complexity

Avoid pricing decisions based only on competitor screenshots and executive vibes. Competitor screenshots are data, but they are not prophecy.

## Product Analytics and Feedback Loops

Use metrics that connect to actual outcomes:

- activation
- adoption
- retention
- engagement quality
- conversion
- support burden
- customer satisfaction
- revenue or mission impact
- churn/loss reasons
- task success
- time-to-value
- error/defect rate
- expansion/renewal signals

### Metric Hygiene

Good metrics:

- connect to decisions
- distinguish activity from value
- have owners
- are reviewed at a useful cadence
- include qualitative feedback where needed
- are interpreted with context

Bad metrics:

- page views presented as adoption
- signups presented as value
- revenue presented without churn/support cost
- support tickets treated only as nuisance, not product evidence
- dashboards nobody uses except during quarterly panic

## Customer, User, and Market Evidence

Product evidence comes from multiple sources:

- interviews
- usability tests
- product analytics
- support tickets
- customer-success feedback
- sales win/loss analysis
- churn/loss reasons
- market research
- competitor analysis
- advisory boards or user councils
- operational data

Do not let one loud customer, one charismatic salesperson, or one executive anecdote become the whole market. Anecdotes are signals. They are not a census.

## Lifecycle Management

Products need active decisions after launch:

- improve
- scale
- reposition
- maintain
- integrate
- deprecate
- sunset

Lifecycle reviews should ask:

- Is the product still delivering value?
- Is usage growing, stable, declining, or unhealthy?
- Are support/operating costs justified?
- Does the product still fit strategy?
- Are customers/users depending on it in ways we understand?
- Is technical debt or operational risk increasing?
- Should we invest, maintain, integrate, restrict, or retire?

Neglect is also a lifecycle decision, just a cowardly one.

## Deprecation and Sunset

Deprecation and sunset are product decisions, not merely engineering cleanup.

Plan:

- reason for deprecation/sunset
- affected users/customers
- contractual/customer commitments
- alternatives or migration path
- communication plan
- support plan
- timeline
- data/export needs
- operational shutdown
- final decision owner

Do not sunset something by hoping users stop noticing it exists. Users are annoyingly observant when their workflows break.

## Risk, Compliance, Security, and Operations

Product decisions often affect risk posture.

Involve relevant owners when the product affects:

- customer data
- employee data
- regulated workflows
- security controls
- financial reporting
- legal obligations
- AI/automation decisions
- production reliability
- operational support
- vendor dependencies

Product management should not become the control owner for everything. It should ensure control owners are involved early enough that launch is not derailed by a late and entirely predictable objection.

## Level-Specific Notes

### Team Leads and Frontline Managers

Focus on:

- understanding the user/customer problem
- clarifying acceptance criteria
- surfacing delivery and support risks
- giving feedback on feasibility and usability
- keeping implementation aligned to intended outcome

### Managers of Managers

Focus on:

- cross-team dependencies
- roadmap tradeoffs across teams
- product/engineering/design/operations collaboration
- repeated delivery or adoption problems
- team capacity against product commitments

### Directors and Senior Leaders

Focus on:

- portfolio/product strategy alignment
- resource allocation
- market/customer segment choices
- lifecycle decisions
- commercial, operational, and risk tradeoffs
- launch and adoption accountability

### Executives and Founders

Focus on:

- strategic product bets
- market/category choices
- investment levels
- product lines to start, scale, reposition, or stop
- enterprise/customer risk acceptance
- avoiding surprise product direction changes from drive-by enthusiasm

A founder's product instinct can be valuable. It can also become an organizational weather system. Write decisions down. Spare the villagers.

## Common Product Scenarios

### Sales Requests a Feature for a Deal

Signals:

- one deal is framed as market proof
- date is urgent
- delivery impact is unclear
- support/operations implications are unknown

Response:

- capture customer, contract, revenue, and commitment context
- validate whether the need generalizes
- assess scope/date/risk
- identify whether it fits strategy
- decide whether to build, defer, customize, partner, or decline
- record customer commitment if accepted

### Customers Ask for a Solution, Not the Problem

Signals:

- request is specific but rationale is vague
- multiple customers ask for different solutions to similar pain
- product team starts designing before understanding the workflow

Response:

- interview for underlying job/problem
- map current workaround
- size pain and frequency
- test alternative solution concepts
- prioritize based on outcome and evidence

### Launch Is Technically Ready but Commercially Unready

Signals:

- feature works but sales/support cannot explain it
- no onboarding path
- pricing/packaging unclear
- feedback loop missing

Response:

- pause full launch if needed
- define launch scope
- prepare enablement, support, analytics, and messaging inputs
- pilot with controlled segment
- review adoption and support evidence before expansion

### Product Has Users but No Owner

Signals:

- support burden exists
- roadmap is unclear
- technical team maintains it by inertia
- nobody owns lifecycle decisions

Response:

- assign product/business owner
- assess value, risk, cost, and usage
- decide invest/maintain/reposition/retire
- document lifecycle plan

## Common Artifacts

Use the smallest useful set:

- product brief or opportunity assessment
- customer/user interview notes
- problem statement
- roadmap
- requirements/specification
- decision record
- launch readiness checklist
- positioning brief
- pricing/packaging input note
- customer commitment register
- adoption metrics review
- risk register
- production-readiness checklist
- deprecation/sunset plan

Relevant product-brief templates:

- [Product Brief Template Family](https://github.com/RusDavies/project-document-templates/blob/main/README.md)
- [Product Brief Audience Model](https://github.com/RusDavies/project-document-templates/blob/main/docs/product-brief-audience-model.md)
- [Source Product Brief](https://github.com/RusDavies/project-document-templates/blob/main/templates/product-brief/source-product-brief.md)
- [Executive Product Brief](https://github.com/RusDavies/project-document-templates/blob/main/templates/product-brief/executive-product-brief.md)
- [Delivery Product Brief](https://github.com/RusDavies/project-document-templates/blob/main/templates/product-brief/delivery-product-brief.md)
- [Market Product Brief](https://github.com/RusDavies/project-document-templates/blob/main/templates/product-brief/market-product-brief.md)
- [Assurance Product Brief](https://github.com/RusDavies/project-document-templates/blob/main/templates/product-brief/assurance-product-brief.md)

Related local templates:

- [Project Brief Template](https://github.com/RusDavies/docs-management-practices/blob/master/templates/project-brief.md)
- [Decision Record Template](https://github.com/RusDavies/docs-management-practices/blob/master/templates/decision-record.md)
- [Customer Commitment Register](https://github.com/RusDavies/docs-management-practices/blob/master/templates/customer-commitment-register.md)
- [Risk Register](https://github.com/RusDavies/docs-management-practices/blob/master/templates/risk-register.md)
- [Production-Readiness Checklist](https://github.com/RusDavies/docs-management-practices/blob/master/templates/production-readiness-checklist.md)
- [Disagree and Commit Record](https://github.com/RusDavies/docs-management-practices/blob/master/templates/disagree-and-commit-record.md)
- [Architecture Framing Checklist](https://github.com/RusDavies/docs-management-practices/blob/master/templates/architecture-framing-checklist.md)
- [AI Use-Case Intake and Data Exposure Assessment](https://github.com/RusDavies/docs-management-practices/blob/master/templates/ai-use-case-intake-and-data-exposure-assessment.md)
- [AI Evaluation Report](https://github.com/RusDavies/docs-management-practices/blob/master/templates/ai-evaluation-report.md)

## Disagree and Commit

Product work creates legitimate disagreement: customer need, market timing, technical cost, revenue impact, support burden, risk, and strategic fit.

Healthy product management makes these disagreements explicit before decisions and then expects honest commitment after the decision.

Good product disagreement:

- states evidence
- separates customer need from proposed solution
- identifies tradeoffs
- names decision owner
- records accepted risk
- defines review trigger

Use a disagree-and-commit record when a product decision is material and unresolved disagreement should be preserved without continuing to block execution.

## AI Tooling Evolution

Use [AI Tooling Evolution](../AI_TOOLING_EVOLUTION.md) for the shared model.

In product management, AI tooling will synthesize customer interviews, support tickets, sales-loss notes, usage data, competitor signals, and roadmap options. It will draft problem statements, requirements, acceptance criteria, launch inputs, and experiment designs.

The risk is faster product fiction: plausible summaries from biased inputs, generated requirements without real discovery, and roadmap recommendations that optimize for available data rather than strategic judgment. Product managers still own problem framing, prioritization, tradeoffs, customer promises, and deciding what not to build.

## Anti-Patterns

Call these out early:

- building stakeholder requests instead of solving user problems
- treating sales anecdotes as the whole market
- treating user research as decorative permission
- shipping without adoption planning
- confusing roadmap certainty with leadership
- launching without support, enablement, or feedback loops
- asking engineering to estimate vague ideas and then treating the estimate as commitment
- using prioritization scores as fake objectivity
- hiding lifecycle neglect behind “maintenance mode”
- making customer commitments outside product/delivery reality
- treating launch as success before adoption is known
- adding features to compensate for unclear positioning
- letting executive preference overrule evidence without recording the tradeoff

## Review Questions

Use these during strategy, discovery, roadmap review, launch readiness, or lifecycle review:

- Who is this for?
- What problem are we solving?
- What evidence says the problem matters?
- Why now?
- What are we intentionally not doing?
- What must be learned before larger investment?
- What tradeoff does this priority imply?
- What customer/user commitment are we making?
- What must sales, support, operations, security/privacy, and customer success know before launch?
- What metric will show adoption or value?
- What signal would tell us to stop or change direction?
- Who owns the product after launch?
- What lifecycle decision is being avoided?

## Practitioner Counterpart

For hands-on product discovery support, backlog/artifact upkeep, customer/problem evidence synthesis, launch-readiness support, and handoffs to product management, see [Product Practitioner](https://github.com/RusDavies/docs-practitioner-practices/blob/master/roles/product-practitioner.md). This management guide owns product direction, prioritization, release/accountability decisions, and cross-functional trade-offs.

## Related Audience-Level Guides

- [Team Leads and Frontline Managers](https://github.com/RusDavies/docs-management-practices/blob/master/TEAM_LEADS_AND_FRONTLINE_MANAGERS.md)
- [Managers of Managers](https://github.com/RusDavies/docs-management-practices/blob/master/MANAGERS_OF_MANAGERS.md)
- [Directors and Senior Leaders](https://github.com/RusDavies/docs-management-practices/blob/master/DIRECTORS_AND_SENIOR_LEADERS.md)
- [Executives and Founders](https://github.com/RusDavies/docs-management-practices/blob/master/EXECUTIVES_AND_FOUNDERS.md)
- [Cross-Functional and Matrix Management](https://github.com/RusDavies/docs-management-practices/blob/master/CROSS_FUNCTIONAL_AND_MATRIX_MANAGEMENT.md)
- [Managing Up](https://github.com/RusDavies/docs-management-practices/blob/master/MANAGING_UP.md)
- [Remote and Hybrid Management](https://github.com/RusDavies/docs-management-practices/blob/master/REMOTE_AND_HYBRID_MANAGEMENT.md)

## Related Discipline Guides

- [Project Management](https://github.com/RusDavies/docs-management-practices/blob/master/disciplines/PROJECT_MANAGEMENT.md)
- [Program Management](https://github.com/RusDavies/docs-management-practices/blob/master/disciplines/PROGRAM_MANAGEMENT.md)
- [Portfolio Management](https://github.com/RusDavies/docs-management-practices/blob/master/disciplines/PORTFOLIO_MANAGEMENT.md)
- [Customer Management](https://github.com/RusDavies/docs-management-practices/blob/master/disciplines/CUSTOMER_MANAGEMENT.md)
- [Stakeholder Management](https://github.com/RusDavies/docs-management-practices/blob/master/disciplines/STAKEHOLDER_MANAGEMENT.md)
- [Architecture Management](https://github.com/RusDavies/docs-management-practices/blob/master/disciplines/ARCHITECTURE_MANAGEMENT.md)
- [Technical Debt Management](https://github.com/RusDavies/docs-management-practices/blob/master/disciplines/TECHNICAL_DEBT_MANAGEMENT.md)
- [AI Landscape Management](https://github.com/RusDavies/docs-management-practices/blob/master/disciplines/AI_LANDSCAPE_MANAGEMENT.md)
- [Risk Management](https://github.com/RusDavies/docs-management-practices/blob/master/disciplines/RISK_MANAGEMENT.md)

## Related Software Product Process Guidance

For software products, use these companion process documents from [docs-software-product-process](https://github.com/RusDavies/docs-software-product-process/blob/master/README.md) when product management needs more detailed delivery, release, or evidence expectations:

- [Product Framing Guidance](https://github.com/RusDavies/docs-software-product-process/blob/master/PRODUCT_FRAMING_GUIDANCE.md) — problem definition, users/stakeholders, non-goals, assumptions, security/privacy/abuse notes, and framing-ready criteria.
- [Requirements Guidance](https://github.com/RusDavies/docs-software-product-process/blob/master/REQUIREMENTS_GUIDANCE.md) — product, functional, non-functional, security, privacy, operational, and acceptance requirements.
- [UX Guidance](https://github.com/RusDavies/docs-software-product-process/blob/master/UX_GUIDANCE.md) — user workflows, trust UX, accessibility, validation, and UX readiness.
- [Software Product Development Process](https://github.com/RusDavies/docs-software-product-process/blob/master/SOFTWARE_PRODUCT_DEVELOPMENT_PROCESS.md) — full lifecycle gates from opportunity framing to operation and improvement.
- [Release Guidance](https://github.com/RusDavies/docs-software-product-process/blob/master/RELEASE_GUIDANCE.md) — launch/release readiness, rollback, support, documentation, monitoring, and post-launch review.
- [Tailoring Guide](https://github.com/RusDavies/docs-software-product-process/blob/master/TAILORING_GUIDE.md) — selecting a lightweight or full process based on project risk and target profile.

Use those links when product decisions need concrete software-product artifacts. Keep this guide focused on product-management judgment: customer reality, strategy, prioritization, launch readiness, feedback, and lifecycle choices.

## Bottom Line

Product management is the discipline of choosing, shaping, launching, learning from, and eventually stopping product investments.

It should connect customer reality, business strategy, delivery feasibility, operational readiness, and market response. If product management becomes only backlog grooming, the organization is not managing product. It is sorting tickets in hope of enlightenment.
