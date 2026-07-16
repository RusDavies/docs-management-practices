# Risk Management

## Purpose

Risk management is the discipline of identifying, understanding, prioritizing, owning, mitigating, accepting, monitoring, and escalating uncertainty that could affect outcomes.

It is the management system for asking: what could go wrong, what could go unexpectedly right, what matters, who owns it, what are we doing about it, and when do we need a decision?

Risk management sits beside strategy, portfolio management, product management, delivery, operations, security, compliance, finance, procurement, vendor management, incident response, quality, and people management. It should connect those disciplines rather than become a separate spreadsheet monastery where risks go to become stale and lonely.

Good risk management helps an organization:

- see material uncertainty early enough to act
- distinguish risk from issues, assumptions, dependencies, and fears
- assign ownership for meaningful risks
- make mitigation, contingency, acceptance, and escalation choices explicit
- connect risk to decision-making, not just reporting
- avoid both reckless optimism and bureaucratic paralysis
- learn from incidents, misses, near misses, and surprises
- maintain evidence for accepted risks and mitigation decisions

Risk management is not the art of coloring boxes red, amber, and green until executives feel something has happened. The colors are optional. The decisions are not.

## Core Responsibilities

Risk management is responsible for ensuring there is a working system for:

- identifying risks from multiple sources
- describing risks clearly
- assessing likelihood, impact, exposure, urgency, and uncertainty
- assigning accountable risk owners
- selecting treatment: avoid, reduce, transfer, accept, monitor, or exploit where appropriate
- defining mitigations, contingencies, triggers, and escalation paths
- tracking actions and residual risk
- reviewing risks on a cadence matched to their volatility
- connecting risk decisions to planning, delivery, governance, and operations
- recording risk acceptances and review dates
- learning from realized risks, incidents, defects, losses, and missed opportunities

Risk management should help people make better decisions. If it only produces a register nobody uses, it has become documentation cosplay.

## Risk vs Issue vs Assumption vs Dependency

These terms are related but different.

- **Risk:** an uncertain future event or condition that could affect outcomes.
- **Issue:** a problem already happening.
- **Assumption:** something believed true for planning purposes but not yet proven.
- **Dependency:** something another person, team, supplier, system, or event must provide.
- **Constraint:** a fixed boundary such as budget, date, regulation, contract, capacity, or technology choice.

A useful risk process connects them. A dependency may create a risk. A failed assumption may become an issue. A constraint may increase impact. Throwing all of them into one undifferentiated register is how management creates a junk drawer with severity scores.

## Risk Sources

Risk can come from many places:

- strategy and market changes
- customer commitments and expectations
- product fit and adoption
- delivery uncertainty
- technical debt and architecture choices
- security exposure
- privacy, legal, regulatory, and compliance obligations
- vendor and supplier dependence
- operational fragility
- financial constraints
- people, capability, retention, and succession gaps
- data quality or reporting weakness
- AI tools, agents, models, providers, prompts, retrieval sources, and automation
- public reputation and stakeholder trust
- external events, policy changes, economic conditions, or geopolitical disruption

Risk reviews should draw from real operating evidence: incidents, customer escalations, support data, delivery slippage, audit findings, security scans, financial variance, staff turnover, vendor performance, and near misses. Vibes can start a conversation. Evidence should finish it.

## Writing Useful Risk Statements

A good risk statement is specific enough to support action.

Useful pattern:

> If [uncertain event/condition] occurs, then [impact] may happen because [cause/context].

Examples:

- If the payment provider migration is not completed before contract expiry, then customer billing may be interrupted because the legacy provider will no longer support required authentication.
- If the support team continues to absorb custom onboarding requests without product or implementation ownership, then response time and renewal trust may degrade because specialist capacity is being consumed by undocumented exceptions.
- If privileged access reviews remain manual and owner mappings are stale, then inappropriate access may persist because reviewers cannot reliably determine who still needs which roles.

Weak risk statements:

- “Vendor risk.”
- “Engineering may be delayed.”
- “Compliance concerns.”
- “AI is risky.”

Those are labels, not risks. Labels do not tell anyone what to do, although they do look confident in a slide deck.

## Assessment and Prioritization

Risk assessment should be good enough to guide action. It does not need fake mathematical precision.

Consider:

- likelihood or plausibility
- impact type and magnitude
- time horizon
- exposure window
- detectability
- reversibility
- uncertainty/confidence in the assessment
- velocity: how quickly harm could unfold
- concentration: how many outcomes depend on the same weak point
- control effectiveness
- stakeholder/customer/regulatory sensitivity

Use the smallest useful decision format.

For most management reviews, state overall risk as **High / Medium / Low** with clear definitions. The label is only shorthand. Each material risk should also include:

- a short rationale for the rating
- owner
- current treatment path
- next action
- review date
- confidence or uncertainty in the assessment

Add dollar exposure when the financial impact is material and defensible, such as revenue loss, contract penalties, remediation cost, insurance exposure, fraud loss, or required investment. Do not invent a dollar value just to make the risk look adult. A weak estimate can be useful if clearly labelled as a range or assumption; fake precision is worse than honest uncertainty.

Use domain-specific impact measures when money would hide the real issue. Examples include:

- customer trust or churn exposure
- regulatory or legal exposure
- safety impact
- security exposure
- operational downtime
- service-level breach
- data loss or privacy exposure
- reputation damage
- staff burnout or capability loss
- strategic delay or missed market window

A useful risk statement may therefore combine formats: “High risk; plausible within this quarter; impact is customer-trust loss and potential SLA breach; financial exposure not yet estimated; confidence medium; owner and mitigation named.” That is more useful than either “High” by itself or “$50k” pretending to explain everything.

A five-by-five matrix with decimal seriousness is often theatre with gridlines.

## Risk Appetite and Tolerance

Risk appetite defines the amount and type of risk the organization is willing to take in pursuit of its objectives.

Clarify appetite by domain where useful:

- customer trust and safety
- security and privacy
- regulatory/compliance exposure
- financial loss
- delivery uncertainty
- product experimentation
- operational availability
- reputation
- people and culture
- vendor dependence
- AI/data exposure

Not all risks deserve the same posture. A product experiment can tolerate learning failure. Payroll accuracy cannot. A prototype can accept rough edges. A public security control cannot accept vibes.

Risk tolerance should include thresholds for escalation. If a risk exceeds the team’s authority, it must move to the decision forum that can accept, mitigate, fund, delay, or stop the work.

## Risk Ownership

Every material risk needs an owner.

A risk owner is accountable for:

- understanding the risk
- ensuring it is assessed honestly
- selecting or recommending treatment
- tracking mitigation and contingency actions
- escalating when thresholds are crossed
- reviewing residual risk
- ensuring acceptance is explicit when mitigation is not chosen

Risk ownership should sit where authority exists. Do not assign ownership to someone who can only worry elegantly. Worry is not a control.

## Risk Treatment

Common treatment options:

- **Avoid:** stop or change the activity so the risk no longer applies.
- **Reduce:** add controls, mitigation, design changes, training, review, capacity, tests, monitoring, or process changes.
- **Transfer/share:** use insurance, contractual terms, outsourcing, partnership, or vendor responsibility where appropriate.
- **Accept:** explicitly decide to live with the risk, with owner, rationale, review date, and evidence.
- **Monitor:** track signals until action is justified.
- **Exploit or pursue:** for opportunity risk, act to increase upside while managing downside.

Treatment should be connected to action. “Mitigate” is not a plan. “Security lead to remove public admin endpoint before beta launch; release blocked if not complete by 15 July” is closer to a plan.

## Mitigation and Contingency

Mitigations reduce likelihood, impact, exposure, or uncertainty before the risk materializes.

Contingencies define what happens if the risk becomes an issue.

For significant risks, define:

- mitigation actions
- contingency actions
- trigger conditions
- decision owner
- communication path
- required evidence
- review date

Example:

Risk: key supplier may miss integration deadline.

Mitigation:

- weekly supplier milestone review
- confirm test environment access by date
- identify internal fallback integration path

Contingency:

- defer launch scope
- use manual operational workaround for first customer cohort
- escalate commercial/legal route if supplier misses contractual milestone

## Risk Acceptance

Accepted risks must be explicit.

A risk acceptance should record:

- risk description
- affected objective, customer, system, process, or obligation
- assessment and evidence
- rationale for acceptance
- residual risk
- compensating controls
- approving authority
- review/expiry date
- trigger for reopening

Accepted risk is not ignored risk. It is a decision. Decisions need owners and memory. Otherwise acceptance becomes a polite word for losing the note.

## Escalation

Escalate risks when:

- impact exceeds team authority
- treatment requires resources the owner cannot allocate
- acceptance would set a precedent
- customer, legal, regulatory, security, financial, or reputational exposure is material
- risk is worsening or nearing trigger conditions
- disagreement cannot be resolved at the current level
- the decision deadline is approaching

Escalation should include the decision needed. “FYI this is bad” is weaker than “Approve launch delay, accept residual risk, or fund mitigation by Friday.”

## Risk Cadence

Risk review cadence should match volatility.

Examples:

- daily/weekly for active delivery, incident, migration, or launch risks
- monthly for operational, vendor, security, or customer health risks
- quarterly for portfolio, strategic, compliance, and financial risks
- event-triggered for major changes, incidents, audit findings, customer escalations, reorganizations, or external shocks

A stale risk register is worse than no register because it creates the aroma of control without the calories.

## Enterprise, Portfolio, and Team Risk

Risk appears at different levels.

### Team / Project Risk

Focus:

- delivery uncertainty
- dependencies
- quality/security defects
- capacity
- stakeholder alignment
- customer commitments
- operational readiness

### Product / Service Risk

Focus:

- customer adoption
- product-market fit
- roadmap tradeoffs
- supportability
- reliability
- data exposure
- lifecycle decisions
- commercial commitments

### Portfolio / Program Risk

Focus:

- investment concentration
- sequencing
- dependency chains
- capacity conflicts
- strategic alignment
- benefits realization
- major vendor or platform dependence

### Enterprise Risk

Focus:

- strategic, financial, legal, regulatory, operational, cyber, people, supplier, reputational, and market risk
- appetite and tolerance
- executive/board oversight
- material residual risk
- aggregated exposure across the organization

The levels should connect. Team-level risks can reveal enterprise patterns. Enterprise risk appetite should shape team decisions. If those two never meet, the risk system has become decorative plumbing.

## Interfaces with Other Disciplines

Risk management connects to:

- **Strategy and portfolio management:** investment choices, concentration, sequencing, and benefits risk.
- **Product management:** customer value, roadmap, market, adoption, lifecycle, and commitment risks.
- **Project/program/delivery management:** scope, schedule, dependency, quality, and readiness risks.
- **Security management:** vulnerability, access, dependency, threat, and incident-prevention risks.
- **Compliance management:** obligations, control gaps, evidence, audit findings, and regulatory change.
- **Operations management:** continuity, capacity, reliability, process, and service risks.
- **Procurement/vendor management:** supplier performance, lock-in, contract, concentration, data, and security risks.
- **People/team/succession management:** capability, retention, workload, leadership, and single-point-of-failure risks.
- **Quality management:** defect, process, release, supplier, and customer-quality risks.
- **AI landscape management:** model/provider/tool, prompt, retrieval, data exposure, agent permission, and evaluation risks.

Risk management should be the connective tissue, not the department that arrives after decisions with a form and a haunted expression.

## Risk Reporting

Risk reporting should support decisions.

Useful reporting includes:

- top material risks
- changes since last review
- risks needing a decision
- accepted risks approaching review/expiry
- overdue mitigations
- emerging patterns
- realized risks and lessons
- risks outside appetite
- evidence confidence
- owner and next action

Avoid reporting that hides all nuance behind color. Red without a decision path is panic branding. Green without evidence is optimism laundering.

## Learning from Realized Risk

When a risk becomes an issue, incident, loss, delay, customer escalation, audit finding, defect, or missed opportunity, review it.

Ask:

- Was the risk identified?
- Was it assessed honestly?
- Were triggers visible?
- Did mitigation work?
- Was escalation timely?
- Was acceptance explicit?
- What control, ownership, evidence, or decision process should change?
- Did incentives encourage people to hide or understate the risk?

The goal is not blame. The goal is a risk system that gets less surprised over time.

## Disagree and Commit

Risk management requires productive disagreement.

People should be able to say:

- the risk is understated
- the mitigation is not credible
- the owner lacks authority
- the accepted risk exceeds appetite
- the evidence is weak
- the score is tidy nonsense
- the deadline changes the exposure
- the customer/regulatory/security impact is being minimized

After a decision is made, teams should commit to the treatment path: mitigate, monitor, escalate, accept, transfer, avoid, or pursue. If new evidence changes the risk, reopen the decision. Do not maintain private disagreement as a shadow risk register in chat.

## Common Artifacts

Common risk management artifacts include:

- [risk register](../templates/risk-register.md)
- [risk appetite statement](../templates/risk-appetite-statement.md)
- [risk assessment rubric](../templates/risk-assessment-rubric.md)
- [risk acceptance record](../templates/risk-acceptance-record.md)
- [mitigation and contingency plan](../templates/risk-mitigation-contingency-plan.md)
- dependency and assumption log
- issue log
- escalation note
- [risk review agenda/minutes](../templates/risk-review-agenda.md)
- enterprise/portfolio risk summary
- control/evidence map
- lessons-learned review

Artifacts should make risk decisions visible. They should not become a museum of concerns nobody intends to act on.

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

In risk management, AI tooling will scan signals, draft risk statements, cluster incidents, monitor controls, propose mitigations, and assemble evidence for reviews. It can make weak signals visible sooner.

The risk is quantified theatre: risks scored neatly from incomplete assumptions, or mitigations accepted because the generated packet looks adult. Risk owners still own appetite, acceptance, escalation, mitigation choices, and the decision to act before certainty arrives.

AI can help find patterns, summarize evidence, and propose risk language. It should not become the authority that accepts risk, sets appetite, or declares weak evidence sufficient because the bullets were nicely aligned.

## Anti-Patterns

Watch for these failure modes:

- maintaining a risk register nobody uses for decisions
- scoring risks precisely from vague assumptions
- confusing issues with risks and then wondering why nothing is early
- assigning risk ownership to people without authority
- treating mitigation labels as mitigation plans
- accepting risk without owner, evidence, rationale, or review date
- escalating risk without saying what decision is needed
- hiding bad news until it becomes an incident
- treating all risks as equally important because the process cannot prioritize
- using color-coded dashboards to replace judgment
- letting risk management become compliance theatre detached from work
- overreacting to every risk until teams stop raising them
- using AI-generated risk summaries without validating sources, context, and missing evidence

## Practical Starting Point

For a team, product, function, or project with weak risk management, start with:

1. List the top risks in plain language.
2. Rewrite each as “if/then/because.”
3. Name the owner with authority to act or escalate.
4. Decide treatment: reduce, accept, monitor, transfer, avoid, or pursue.
5. Add one concrete next action and review date.
6. Identify risks that exceed the team’s authority.
7. Escalate those with a specific decision request.
8. Review what changed since last time, not just whether the row still exists.

Good risk management is not about predicting everything. It is about noticing enough, early enough, with enough ownership, that decisions improve before reality sends the invoice.
