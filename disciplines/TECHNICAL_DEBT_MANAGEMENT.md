# Technical Debt Management

## Purpose

Technical debt management is the discipline of identifying, classifying, owning, prioritizing, accepting, reducing, and preventing the technical liabilities that accumulate as systems are built, changed, operated, scaled, secured, and eventually retired.

Technical debt is not simply "code I dislike." It is a gap between the current technical state and the state needed for safe, reliable, maintainable, secure, cost-effective delivery over time.

Some debt is intentional. A team may take a shortcut to learn quickly, meet a real deadline, or avoid over-engineering before the problem is understood. Some debt is accidental: unclear ownership, weak architecture, rushed delivery, poor testing, old dependencies, missing observability, neglected security defects, stale data models, or infrastructure nobody wants to admit still exists.

Debt is not automatically bad. Unmanaged debt is bad. Debt that nobody owns, measures, prices, revisits, or remediates becomes a quiet tax on delivery and eventually a risk event with a calendar invite.

## The Debt Metaphor Has Limits

The technical debt metaphor is useful, but it is not sacred. Ward Cunningham introduced the metaphor to explain why shipping quickly with known design compromises can create later refactoring pressure. Used carefully, that is still a useful idea.

The critique is also useful. Ralf Westphal argued that there is no such thing as technical debt, partly because most so-called technical debt does not behave like financial debt:

- there is often no clear moment when the debt is incurred
- the amount owed is rarely measurable
- the interest rate is not explicit
- there is often no repayment schedule
- nobody acts like a real creditor forcing repayment

That critique should not make managers abandon the term. It should make them use it precisely.

There is also an equivocation risk in the critique. If the argument is "technical debt is not exactly like financial debt, therefore technical debt does not exist," it rejects the metaphor by demanding literal equivalence. That does not follow. A term can fail to map perfectly to financial debt and still label a real phenomenon: technical conditions that impose future cost, reduce delivery capacity, increase operational burden, or extend security exposure.

Not every mess is debt. Not every maintenance task is debt. Not every old system is debt. Not every engineer preference deserves a repayment plan.

A technical issue becomes debt in the management sense when there is:

- a known gap between current state and needed state
- a practical consequence if the gap remains
- an owner or accountable decision forum
- an estimated cost, risk, exposure, or delivery drag
- a decision to remediate, mitigate, accept, defer, replace, or retire
- a review point when the decision should be revisited

Without those elements, "technical debt" becomes a vague complaint bucket. With them, it becomes a way to manage consequences.

The useful position is not "technical debt exists" or "technical debt does not exist." The useful position is: define the liability, name the consequence, assign ownership, and decide what to do about it. Otherwise the term becomes a polite label for systems developing personality disorders.

## Core Responsibilities

Technical debt management is responsible for:

- defining what counts as technical debt
- classifying debt by type, severity, impact, and reversibility
- assigning ownership
- connecting debt to delivery, risk, cost, customer impact, security exposure, and operational burden
- deciding when debt can be accepted, when it must be remediated, and when it must block delivery
- tracking debt through lifecycle states
- making debt visible in architecture, product, delivery, portfolio, risk, and operations forums
- reducing exposure windows for security defects and other high-risk weaknesses
- using automation and AI agents to accelerate discovery, analysis, remediation, testing, and evidence capture
- preventing recurring debt through better architecture, standards, tooling, review, and feedback loops

Technical debt management should not become a shame ledger. The point is not to scold teams for every compromise. The point is to make consequences explicit and keep compromises from becoming permanent infrastructure by accident.

## Debt Classes

Debt should be classified well enough to route it to the right owner and decision forum.

### Architectural Debt

Architectural debt appears when system structure no longer fits the work.

Examples:

- wrong boundaries between services, modules, or domains
- brittle integration patterns
- excessive coupling
- missing abstraction where change is frequent
- over-abstraction where change is rare
- unplanned platform fragmentation
- hard-to-reverse technology choices
- data ownership that no longer matches business reality

Architectural debt usually needs architecture and engineering involvement. It often cannot be fixed by asking one team to tidy a file.

### Code Debt

Code debt appears when implementation choices make code harder to change, test, reason about, or operate.

Examples:

- complex or duplicated logic
- unclear naming and responsibility
- low cohesion and high coupling
- unsafe error handling
- fragile concurrency
- inconsistent patterns
- missing tests around important behaviour

Code debt should be connected to concrete consequences. "This is ugly" is weak. "This makes payment-state changes risky because three inconsistent code paths update the same state" is useful.

### Dependency Debt

Dependency debt appears when libraries, packages, frameworks, runtimes, images, or third-party components become obsolete, vulnerable, unsupported, incompatible, or difficult to update.

Examples:

- unsupported runtime versions
- vulnerable dependencies
- abandoned libraries
- pinned versions without upgrade path
- container base images with known exposure
- dependency trees that make patching slow or risky

Dependency debt often has a security dimension. It also has an operational one: the longer updates are deferred, the more every future update becomes archaeology with a build log.

### Data Debt

Data debt appears when data structures, ownership, quality, lineage, retention, or meaning are unclear or wrong.

Examples:

- duplicated sources of truth
- unclear domain ownership
- weak data quality controls
- undocumented transformations
- missing lineage
- stale or inconsistent reporting definitions
- privacy/retention gaps
- schemas that no longer match business reality

Data debt becomes especially expensive when analytics, compliance, AI, customer reporting, or operational automation depends on the data.

### Security Defect Debt

Security defect debt appears when known or discoverable weaknesses remain unresolved in systems, dependencies, configurations, identities, data flows, or operational practices.

Examples:

- vulnerable dependencies or base images
- exposed secrets
- broken access controls
- missing authorization checks
- insecure defaults
- unsafe deserialization or injection paths
- weak cryptography or key handling
- internet-exposed administrative surfaces
- misconfigured storage, networks, identity, or logging
- stale accounts and excessive privileges

Security defect debt is not just another backlog category. It carries an exposure window: the time between discovery or reasonable discoverability and remediation or accepted mitigation.

The old operating model treated many security defects as a vast manual backlog: scan everything, produce thousands of findings, route them to low-cost remediation teams, and let the queue grind slowly forward. That model is dead, or should be. It leaves exposure windows open while everyone admires the dashboard.

AI agents should change the remediation economics. They can help discover defects, analyze reachability and exposure, classify realistic risk, propose fixes, generate tests, prepare patches, and capture evidence much faster than manual triage alone. Humans should still own judgment, approval, risk acceptance, and production responsibility. The point is not autonomous recklessness. The point is reducing the time a known weakness remains exploitable.

For scanner-driven AI remediation, keep scanner intake, chunking, exception/VEX records, artifact repository integration, expiry/review rules, and evidence packets disciplined.

### Operational Debt

Operational debt appears when systems are difficult to deploy, monitor, support, recover, scale, secure, or retire.

Examples:

- missing observability
- noisy or absent alerts
- weak runbooks
- manual deployment steps
- poor rollback paths
- unknown production ownership
- fragile backups or recovery
- missing capacity signals
- inconsistent environment management

Operational debt usually shows up during incidents, which is the least charming time to discover how much of the system depends on Greg remembering a command.

### Platform and Infrastructure Debt

Platform and infrastructure debt appears when hosting, networking, identity, CI/CD, environments, cloud accounts, virtualization, Kubernetes, storage, or shared tooling becomes fragile or inconsistent.

Examples:

- unmanaged cloud resources
- inconsistent tagging and ownership
- outdated images or runtimes
- snowflake environments
- untracked self-service VMs
- brittle CI/CD pipelines
- platform standards nobody follows
- missing cleanup for temporary resources

This debt should connect to architecture inventory and CMDB discipline. If the organization cannot tell what exists, who owns it, and whether it should still be running, it has both technical debt and a search problem.

### Documentation and Knowledge Debt

Documentation debt appears when important system knowledge exists only in heads, chat logs, old tickets, or abandoned diagrams.

Examples:

- missing decision records
- stale architecture diagrams
- undocumented operational procedures
- unclear ownership
- no onboarding path for critical systems
- unavailable rationale for past decisions

Documentation debt is not solved by writing more documents. It is solved by making the right knowledge findable, current enough, and attached to the workflows where people need it.

### Vendor and Tooling Debt

Vendor and tooling debt appears when external tools, SaaS platforms, contracts, integrations, or vendor dependencies become hard to change, risky, duplicated, expensive, or poorly owned.

Examples:

- tool sprawl
- duplicate platforms
- vendor lock-in without conscious acceptance
- unsupported integrations
- unclear contract ownership
- unmanaged renewals
- poor exit paths
- suppliers with unresolved security or reliability issues

Vendor debt belongs in both technical debt management and vendor/procurement management. It is still debt even if the invoice has nicer branding.

## Debt Lifecycle

Technical debt should move through explicit states.

### 1. Identify

Debt may be found through:

- engineering review
- architecture review
- security scanning
- incident review
- customer impact
- delivery friction
- operational metrics
- cost analysis
- dependency analysis
- AI-agent discovery
- audit or compliance review

### 2. Classify

Classify debt by:

- debt type
- affected system/service/data domain
- owner
- impact
- likelihood or frequency
- reversibility
- exposure window
- customer or operational consequence
- security/privacy/compliance relevance
- remediation complexity
- evidence quality

Classification should be useful enough to drive action. A thousand unclassified findings are not a control. They are a haystack with login credentials.

### 3. Prioritize

Prioritization should consider:

- risk exposure
- delivery drag
- customer impact
- operational burden
- security exploitability
- architectural leverage
- cost of delay
- remediation effort
- dependency on other work
- opportunity to fix while adjacent work is already open

Do not prioritize only by technical irritation. The best engineers can be annoyed by the wrong thing with impressive precision.

### 4. Decide

Possible decisions:

- remediate now
- remediate in a planned window
- remediate as part of adjacent work
- contain or mitigate
- accept risk temporarily
- accept risk long-term with explicit owner
- replace or retire the affected system
- reject as not material or not actually debt

### 5. Remediate

Remediation should define:

- owner
- scope
- expected outcome
- risk of change
- tests or validation
- deployment path
- rollback/recovery path
- evidence required
- approval gate, if needed

### 6. Verify

Verification may include:

- tests
- security scans
- exploit/reachability reassessment
- architecture review
- operational metrics
- customer validation
- incident simulation
- production monitoring

### 7. Close or Reclassify

Close debt only when the underlying issue has been addressed or consciously accepted. Do not close it because the ticket became emotionally inconvenient.

If remediation reveals a broader issue, reclassify and route it appropriately.

## Decision Gates

Technical debt needs gates where decisions are made deliberately.

### Debt Acceptance Gate

Use when a team proposes to carry debt intentionally.

Check:

- What debt is being accepted?
- Why is acceptance better than remediation now?
- Who owns the risk?
- What is the expected cost of delay?
- What would trigger reconsideration?
- When will it be reviewed?

### Security Exposure Gate

Use for known or suspected security defects.

Check:

- Is the affected asset internet-exposed, customer-facing, privileged, or connected to sensitive data?
- Is the defect reachable?
- Is exploitation plausible?
- Are compensating controls present?
- Is active exploitation known or likely?
- What is the remediation SLA?
- Who accepts residual risk?

### Architecture Impact Gate

Use when debt affects system boundaries, data ownership, platform standards, integration patterns, or hard-to-reverse decisions.

Check:

- Is this local debt or architectural debt?
- Does remediation require design change across teams?
- Does the current debt constrain future delivery or product strategy?
- Does it increase operational, security, or vendor risk?

### Production Change Gate

Use when remediation may affect live systems.

Check:

- What is the change risk?
- What testing supports the fix?
- What rollback path exists?
- What monitoring confirms success?
- Who needs to be informed?

### Retirement or Replacement Gate

Use when debt is better solved by retiring or replacing the system.

Check:

- Is remediation economically sensible?
- What depends on the system?
- What data must be migrated, archived, or deleted?
- What contracts, integrations, jobs, users, or reports must be addressed?
- What is the risk of keeping the system alive?

## Security Defect Debt and Exposure Windows

Security defect management should focus on exposure windows, not just ticket counts.

Important measures include:

- time from detection to triage
- time from triage to reachability/exposure assessment
- time from assessment to patch or mitigation
- time from patch to deployment
- time from deployment to verification
- number of known exposed critical/high defects
- number of defects with accepted risk and review date
- number of repeatedly reopened findings

A vulnerability backlog is not inherently useful. A backlog can show volume while hiding exposure. A smaller set of reachable, exploitable, internet-exposed defects may matter far more than hundreds of theoretical findings in unreachable code.

Good security defect debt management separates:

- **finding:** scanner, review, report, or agent detected a possible issue
- **confirmed defect:** issue is real enough to track
- **reachable defect:** affected code/configuration can be exercised in context
- **exposed defect:** reachable from meaningful attacker, user, network, tenant, or data position
- **exploitable defect:** plausible exploit path exists
- **business-critical defect:** exploit affects important asset, data, customer, service, or obligation
- **mitigated defect:** compensating control reduces immediate risk
- **remediated defect:** underlying issue fixed and verified
- **accepted risk:** remaining risk explicitly owned and reviewed

This distinction matters because remediation capacity should go where exposure and consequence are real. It also matters because false precision creates bad management decisions. CVSS alone does not tell you whether the defect matters in your system.

## AI-Agent-Accelerated Remediation

AI agents can materially change technical debt management, especially for security defects and dependency debt.

Useful agent-assisted workflows include:

1. **Discovery:** search code, configs, dependencies, infrastructure, logs, IaC, and service inventories for defect patterns.
2. **Exposure analysis:** determine whether affected code, services, endpoints, permissions, or configurations are reachable in real deployment contexts.
3. **Risk classification:** combine severity, exploitability, asset criticality, data exposure, compensating controls, and business impact.
4. **Remediation planning:** propose the smallest safe fix, larger structural options, tests, rollout path, and rollback plan.
5. **Patch preparation:** generate code/configuration changes in a branch or pull request.
6. **Test generation:** add regression, unit, integration, security, or configuration tests that prove the fix and reduce recurrence.
7. **Upstream contribution:** when the defect is in an open source dependency, assess whether a responsible upstream issue, patch, test, or pull request can be proposed so the fix helps the wider community rather than living only in a private fork.
8. **Evidence capture:** record before/after scans, changed files, rationale, test output, residual risk, and owner sign-off.
9. **Follow-up routing:** escalate architectural, product, operational, vendor, upstream maintainer, or risk decisions that cannot be safely resolved inside the patch.

This is where the old manual model breaks. A low-context team working through thousands of issues can close tickets while leaving the important exposure open. AI agents, used well, should compress the loop between detection, understanding, fix, proof, and approval.

Used badly, AI agents can generate confident patches that break behaviour, hide risk, or create new vulnerabilities with excellent formatting. The workflow needs gates.

## Open Source Dependency Upstream Fixes

When the issue is in an open source dependency, remediation should consider both local exposure and community repair.

A practical sequence is:

1. protect the local system if exposure is material
2. confirm the defect against the upstream source where feasible
3. check whether the issue is already reported or fixed upstream
4. prepare a minimal reproduction, failing test, or evidence summary
5. propose a responsible upstream issue or pull request if disclosure rules allow it
6. avoid publishing exploit details prematurely for sensitive security defects
7. track the upstream fix, local patch, vendor package, or version upgrade path
8. remove local forks or temporary mitigations when upstream remediation is available and verified

Helping upstream is not charity theatre. It reduces future maintenance burden, improves the ecosystem, and may remove the need to carry private patches forever. Private forks are sometimes necessary. They are also where fixes go to become someone else's archaeology.

Security-sensitive upstream work should respect the project's disclosure process. If the project has a security policy, use it. If there is no clear policy, involve the right security/legal owner before dropping a fully weaponized bug report into a public issue tracker like a raccoon in a server room.

## Human Approval Gates for AI Remediation

AI agents may prepare work. Humans remain accountable for meaningful decisions.

Human approval should be required for:

- risk acceptance
- production-impacting changes
- authentication, authorization, cryptography, privacy, or data-handling changes
- broad architectural changes
- dependency upgrades with significant compatibility risk
- changes affecting customer commitments, legal/regulatory obligations, or service availability
- remediation that changes product behaviour
- any case where the agent cannot produce credible evidence

Low-risk, well-tested, reversible changes may be batched or fast-tracked. The goal is not to make humans click approve on every semicolon. The goal is to route human judgment to the decisions where judgment matters.

## Ownership and Forums

Technical debt needs owners and forums.

Possible ownership model:

- delivery teams own local code and test debt
- platform teams own platform and shared infrastructure debt
- data owners own data debt
- security owners govern security defect standards and exposure analysis
- architects govern architectural debt classification and cross-system decisions
- product owners help decide user/customer trade-offs
- operations owners govern production readiness and support debt
- executives or portfolio owners accept major risk, cost, or strategic trade-offs

Useful forums include:

- sprint/team planning for local debt
- architecture review for structural debt
- risk review for accepted or material exposure
- security review for exploitable defects
- portfolio review for large remediation investments
- incident review for debt revealed by failures
- operational review for production burden and reliability debt

## Remediation Economics

Debt decisions should consider cost of delay.

Questions:

- What does this debt cost every month?
- What delivery work does it slow down?
- What operational load does it create?
- What risk or exposure window does it leave open?
- What future change will become more expensive if this remains?
- Is remediation cheaper while adjacent work is already happening?
- Is replacement cheaper than repair?
- Is retirement the right answer?

Some debt is best paid down opportunistically. Some needs a funded remediation effort. Some should be accepted. Some should trigger replacement. Some should block release.

The management failure is pretending all debt is equivalent. It is not. A messy helper function and an internet-exposed auth bypass are not cousins.

## Common Artifacts

- [Technical Debt Register](https://github.com/RusDavies/docs-management-practices/blob/master/templates/technical-debt-register.md)
- debt classification model
- architecture decision record
- [Debt Acceptance Record](https://github.com/RusDavies/docs-management-practices/blob/master/templates/debt-acceptance-record.md)
- security defect register
- [Security Exposure Assessment](https://github.com/RusDavies/docs-management-practices/blob/master/templates/security-exposure-assessment.md)
- [Technical Debt Remediation Plan](https://github.com/RusDavies/docs-management-practices/blob/master/templates/technical-debt-remediation-plan.md)
- corrective-action tracker
- dependency update report
- production-readiness checklist
- incident post-review action list
- CMDB/configuration inventory
- service ownership map
- [AI-Agent Remediation Evidence Packet](https://github.com/RusDavies/docs-management-practices/blob/master/templates/ai-agent-remediation-evidence-packet.md)

## Relationship to Other Disciplines

Technical debt management connects to:

- **Architecture management:** structural decisions, lifecycle, system boundaries, 4+1 views, CMDB, and architectural debt
- **Risk management:** exposure, accepted risk, control gaps, business consequence, and risk review
- **Incident response management:** incidents reveal debt; post-incident reviews create debt remediation actions
- **Operations management:** observability, reliability, supportability, recovery, and production burden
- **Product management:** trade-offs between customer value, roadmap commitments, and debt reduction
- **Project/program management:** planning, sequencing, dependencies, and remediation execution
- **Portfolio management:** large remediation investments, rationalization, and strategic lifecycle choices
- **Procurement management:** tool/vendor decisions that create or reduce debt
- **Vendor and partner management:** supplier risk, third-party defects, managed service issues, and support obligations
- **AI landscape management:** AI systems, agent workflows, model/tool dependencies, AI-assisted remediation, and AI-specific risk
- **Knowledge management:** decision records, runbooks, debt rationale, and lessons learned

Debt is where these disciplines meet after reality has had opinions.

## Disagree and Commit

Technical debt decisions create real disagreement:

- Should we fix this now or ship?
- Is this actual debt or just an aesthetic preference?
- Should security exposure block release?
- Should we patch, mitigate, replace, or retire?
- Should product roadmap capacity be used for invisible remediation?
- Who owns risk when delivery wants to defer the fix?
- Is the AI-generated patch good enough, or does it need deeper redesign?

Healthy teams argue about debt through evidence: impact, exposure, cost, reversibility, delivery drag, customer consequence, and risk. After the decision, the owner, review date, and rationale should be visible.

Disagree and commit does not mean pretending deferred debt stopped mattering. It means the organization has consciously accepted the consequence and knows when to revisit it.

## Adjacent Practitioner Handoffs

Technical-debt evidence and remediation should be handled through adjacent roles rather than a generic technical-debt practitioner. Use [Software Engineering Practitioner](https://github.com/RusDavies/docs-practitioner-practices/blob/master/roles/software-engineering-practitioner.md), [Architecture Practitioner](https://github.com/RusDavies/docs-practitioner-practices/blob/master/roles/architecture-practitioner.md), [Security Vulnerability Remediation Practitioner](https://github.com/RusDavies/docs-practitioner-practices/blob/master/roles/security-vulnerability-remediation-practitioner.md), [Operations Operator](https://github.com/RusDavies/docs-practitioner-practices/blob/master/roles/operations-operator.md), and [Product Practitioner](https://github.com/RusDavies/docs-practitioner-practices/blob/master/roles/product-practitioner.md) for domain-specific execution and evidence.

## Related Audience-Level Guides

Use the audience-level guides to adapt this discipline to the manager's scope, authority, and operating context:

- [Team Leads and Frontline Managers](https://github.com/RusDavies/docs-management-practices/blob/master/TEAM_LEADS_AND_FRONTLINE_MANAGERS.md) — day-to-day execution, coaching, coordination, and local accountability.
- [Managers of Managers](https://github.com/RusDavies/docs-management-practices/blob/master/MANAGERS_OF_MANAGERS.md) — consistency across teams, manager enablement, and cross-team operating cadence.
- [Directors and Senior Leaders](https://github.com/RusDavies/docs-management-practices/blob/master/DIRECTORS_AND_SENIOR_LEADERS.md) — multi-team strategy, prioritization, risk, and organizational health.
- [Executives and Founders](https://github.com/RusDavies/docs-management-practices/blob/master/EXECUTIVES_AND_FOUNDERS.md) — enterprise direction, culture, investment choices, and accountability systems.
- [Cross-Functional and Matrix Management](https://github.com/RusDavies/docs-management-practices/blob/master/CROSS_FUNCTIONAL_AND_MATRIX_MANAGEMENT.md) — shared ownership, influence, and decision-making without clean reporting lines.
- [Managing Up](https://github.com/RusDavies/docs-management-practices/blob/master/MANAGING_UP.md) — upward communication, expectation-setting, escalation, and decision framing.
- [Remote and Hybrid Management](https://github.com/RusDavies/docs-management-practices/blob/master/REMOTE_AND_HYBRID_MANAGEMENT.md) — distributed communication, trust, documentation, and inclusion.

## Related Software Product Process Guidance

For software products, use these companion process documents from [docs-software-product-process](https://github.com/RusDavies/docs-software-product-process/blob/master/README.md) when technical debt needs to be connected to product-development controls, release gates, and evidence:

- [Implementation Planning Guidance](https://github.com/RusDavies/docs-software-product-process/blob/master/IMPLEMENTATION_PLANNING_GUIDANCE.md) — backlog structure, sequencing, verification gates, security/operations tasks, and risk registers.
- [Architecture Guidance](https://github.com/RusDavies/docs-software-product-process/blob/master/ARCHITECTURE_GUIDANCE.md) — architecture decisions and system-shaping debt around boundaries, data, deployment, security, observability, and operational estate.
- [QA Guidance](https://github.com/RusDavies/docs-software-product-process/blob/master/QA_GUIDANCE.md) — verification strategy and quality gates for remediation work.
- [Security Guidance](https://github.com/RusDavies/docs-software-product-process/blob/master/SECURITY_GUIDANCE.md) — security/privacy design and defect-prevention expectations.
- [Release Security Gate](https://github.com/RusDavies/docs-software-product-process/blob/master/RELEASE_SECURITY_GATE.md) — release-time security review and accepted-risk evidence.
- [Operations Guidance](https://github.com/RusDavies/docs-software-product-process/blob/master/OPERATIONS_GUIDANCE.md) — operational debt around runbooks, maintenance, automation, support, and incident handling.

Use those documents when debt remediation is part of a software-product delivery or release path. This guide covers the management discipline: classification, ownership, prioritization, acceptance, remediation economics, and review cadence.

## AI Tooling Evolution

Use [AI Tooling Evolution](../AI_TOOLING_EVOLUTION.md) for the shared model.

In technical debt management, AI tooling will discover debt signals, classify defect families, propose remediations, generate tests, prepare evidence packets, and reduce exposure windows for security and dependency defects. The practical opportunity is governed acceleration, not autonomous code churn.

The risk is mass-produced remediation without context: fixes that pass local checks while breaking contracts, suppressing scanner truth, or hiding residual risk. Humans still own approval, prioritization, production responsibility, risk acceptance, and evidence standards.

## Anti-Patterns

- treating all technical debt as code cleanup
- using technical debt as a vague complaint category
- tracking huge debt backlogs without ownership, prioritization, or decision forums
- treating vulnerability counts as security risk without exposure analysis
- letting known security defects sit open while remediation capacity crawls through a queue
- outsourcing security remediation to low-context teams without system ownership or architecture understanding
- accepting risk without an accountable owner or review date
- closing findings because the scanner is noisy rather than proving materiality
- fixing symptoms while leaving architectural causes intact
- using AI agents to generate patches without tests, evidence, or human gates
- making every AI-assisted remediation wait for the same manual process as a hand-written patch
- allowing temporary exceptions to become permanent policy
- letting product roadmaps consume all capacity while debt quietly taxes every future roadmap
- discovering operational debt during incidents and then forgetting it after service returns
- measuring debt only by ticket count instead of exposure, cost, delivery drag, and risk
