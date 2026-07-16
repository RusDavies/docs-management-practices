# Data and Analytics Management

## Purpose

Data and analytics management defines how an organization owns, understands, protects, improves, uses, reports, retires, and learns from data.

It overlaps with architecture, product, operations, finance, security, privacy, legal, risk, AI, engineering, customer management, support, marketing, and executive leadership. That overlap is why the discipline needs explicit management guidance: otherwise every dashboard becomes a local religion and every spreadsheet becomes a tiny unregulated database with opinions.

Good data and analytics management helps an organization:

- define data ownership and accountability
- decide sources of truth deliberately
- improve data quality where it matters
- make reporting and analytics trustworthy
- govern metrics and definitions
- manage lineage, retention, access, and privacy/security boundaries
- prioritize analytics work against business value and risk
- prepare data for AI and automation without pretending messy data becomes wise because a model touched it
- retire stale reports, duplicated datasets, and misleading metrics

## Scope

Data and analytics management may cover:

- data domains and ownership
- source-of-truth decisions
- data definitions and glossaries
- data quality management
- lineage and provenance
- reporting and dashboard governance
- metric definition and review
- analytics prioritization
- data access and entitlement models
- privacy, security, legal, compliance, and retention interfaces
- data architecture and integration patterns
- operational, product, customer, financial, risk, and marketing analytics
- experimentation and decision support
- AI-readiness and model/data-use governance
- data lifecycle, archival, and retirement

Architecture management should usually own structural data architecture choices. Data and analytics management should own whether the data is meaningful, trusted, usable, governed, and connected to decisions. In small organizations, these may be the same mammal wearing two hats and carrying one emotionally fragile spreadsheet.

## Data Domains and Ownership

Data needs named owners.

Useful ownership defines:

- data domain
- accountable business owner
- technical/system owner
- data steward or operational maintainer
- source systems
- key consumers
- quality expectations
- access rules
- retention expectations
- escalation path for defects or disputes

Examples of data domains:

- customer/account data
- product/catalog data
- order/transaction data
- employee/HR data
- supplier/vendor data
- financial data
- support/service data
- security/risk data
- operational telemetry
- marketing and campaign data

Ownership does not mean the owner personally fixes every row. It means someone is accountable for meaning, priority, and decision-making when the data is wrong, contested, or risky.

## Source-of-Truth Decisions

A source of truth is not the system people like best. It is the agreed authoritative source for a defined data concept in a defined context.

Clarify:

- authoritative source for each major data object
- allowed derived sources
- synchronization and replication rules
- conflict resolution rules
- ownership of corrections
- timing/latency expectations
- downstream reporting implications
- retirement path for duplicate sources

Avoid vague statements like "CRM is the source of truth" unless the organization has defined for what. Customer legal name, billing entity, account owner, renewal date, entitlement, support tier, and product usage may all live in different authoritative places.

A source-of-truth map should prevent the classic management ritual where three dashboards disagree and the meeting becomes archaeology with pie charts.

## Data Definitions and Glossary

Key terms need shared definitions.

Define:

- metric names
- business terms
- calculation logic
- inclusion/exclusion rules
- time windows
- segmentation rules
- owner
- approved use
- known caveats

Examples:

- active customer
- monthly recurring revenue
- qualified lead
- resolved ticket
- churn
- adoption
- incident
- employee headcount
- gross margin
- production defect

If a metric can change meaning between departments, it is not a metric. It is a negotiation wearing decimal places.

## Data Quality Management

Data quality should focus on data that affects decisions, customers, operations, compliance, security, financial results, AI use, or automation.

Common quality dimensions:

- accuracy
- completeness
- timeliness
- consistency
- uniqueness
- validity
- lineage/provenance
- availability
- fitness for purpose

Manage quality by:

- identifying critical data elements
- assigning owners/stewards
- defining quality thresholds
- monitoring defects
- triaging issues by impact
- fixing root causes, not only symptoms
- tracking exceptions and accepted defects
- communicating caveats to consumers

Do not boil the ocean. Also do not ignore the swamp because the ocean is large.

## Lineage and Provenance

Lineage shows where data came from, how it changed, and where it went.

Track lineage for data that supports:

- financial reporting
- regulatory/compliance obligations
- customer commitments
- security and risk decisions
- executive dashboards
- AI/ML models
- automated decisions
- operational controls

Useful lineage captures:

- source system
- extraction/ingestion path
- transformation logic
- enrichment or matching logic
- downstream datasets/reports/models
- owners
- refresh cadence
- known limitations

Lineage is not only for auditors. It is also for the day someone asks why the number changed and everyone suddenly discovers the dashboard was fed by a script named `final_final_really_use_this_one.py`.

## Reporting and Dashboard Governance

Reports and dashboards should have purpose, ownership, and trust levels.

Manage:

- report owner
- business purpose
- audience
- source datasets
- metric definitions
- refresh cadence
- quality caveats
- access rules
- review date
- retirement criteria

Dashboard trust levels can help:

- **Certified:** approved definitions, known sources, reviewed quality, suitable for management decisions.
- **Operational:** useful for day-to-day monitoring, may have known caveats.
- **Exploratory:** analysis in progress; not official.
- **Deprecated:** still accessible temporarily but should not guide new decisions.

A dashboard without an owner is a haunted mirror. It reflects something. Nobody is sure what.

## Metric Governance

Metrics shape behavior. Govern them accordingly.

For important metrics, define:

- decision supported
- owner
- calculation
- source data
- update frequency
- target or threshold
- interpretation guidance
- known failure modes
- gaming risks
- review cadence

Good metrics connect to outcomes, decisions, or risk.

Bad metric patterns include:

- measuring what is easy instead of what matters
- changing definitions without notice
- comparing teams using incompatible data
- rewarding volume over value
- using lagging indicators as if they were steering wheels
- treating one number as complete truth

Metrics are signals. They are not a substitute for judgment. If they were, management could be replaced by a spreadsheet and a small fan to blow papers around dramatically.

## Analytics Prioritization

Analytics demand usually exceeds capacity.

Prioritize by:

- decision value
- customer/user impact
- operational risk
- financial impact
- regulatory/compliance need
- urgency
- data availability and quality
- repeatability
- reuse potential
- complexity and maintenance burden

Analytics work should produce one or more of:

- a decision
- a behavior change
- operational visibility
- risk reduction
- customer/product insight
- validated learning
- automation input
- compliance evidence

If nobody can say what decision or action the analysis supports, the request may be curiosity. Curiosity is allowed. It just should not always cut the line.

## Decision Support and Analysis Quality

Analysis should make uncertainty visible.

Good analysis includes:

- question being answered
- data sources
- method
- assumptions
- caveats
- uncertainty/confidence
- sensitivity to definitions
- alternative explanations
- recommended decision or next step

Bad analysis hides uncertainty behind polished charts. A beautiful chart can still be nonsense with kerning.

## Data Access and Entitlements

Data access should match purpose, sensitivity, role, and risk.

Manage:

- access request and approval paths
- role-based or attribute-based access
- least privilege
- sensitive-data handling
- customer/employee/security/legal data boundaries
- audit logs
- periodic access review
- emergency access
- offboarding and access removal
- third-party/vendor access

Data democratization should not mean every person gets every table because "collaboration." That is not democracy. That is a breach waiting for a calendar invite.

## Privacy, Security, Legal, and Compliance Interfaces

Data management must connect to control functions early.

Coordinate on:

- data classification
- lawful basis/consent where relevant
- data minimization
- purpose limitation
- cross-border transfer
- retention and deletion
- legal hold
- subject/access rights
- regulated data
- audit evidence
- encryption/access controls
- incident response
- vendor/subprocessor data handling

Privacy, security, and legal controls are much cheaper before the data lake becomes a swamp with customer records and executive enthusiasm floating in it.

## AI-Readiness

AI-readiness depends on data readiness.

Assess:

- approved data sources
- data sensitivity and permitted use
- quality and representativeness
- lineage and provenance
- consent/licensing/contract restrictions
- retention and deletion obligations
- bias and coverage gaps
- evaluation datasets
- prompt/retrieval exposure
- model training/fine-tuning permissions
- monitoring and drift detection

AI does not turn unclear data into clear truth. It turns unclear data into confident output, which is worse because now the nonsense has posture.

## Data Lifecycle, Retention, and Retirement

Data should have a lifecycle.

Manage:

- creation/capture
- use and update
- sharing/replication
- archival
- retention
- deletion/anonymization
- migration
- retirement of reports/datasets
- evidence of disposal where needed

Retire:

- stale dashboards
- duplicate datasets
- orphaned extracts
- unauthorized local copies
- unused pipelines
- outdated metric definitions
- old experimental datasets

Archive or delete according to legal, regulatory, contractual, operational, and business needs. Do not preserve every dataset forever because storage is cheap. Storage is cheap; confusion, breach scope, discovery obligations, and bad decisions are not.

## Data Operating Cadence

Useful cadence may include:

- data-domain owner reviews
- critical data quality review
- dashboard/report certification review
- metric definition review
- analytics prioritization forum
- access review
- retention/deletion review
- AI/data-use review
- incident/problem review for data defects

Keep the cadence proportional. Not every spreadsheet needs a council. Some absolutely do, because they secretly run payroll, billing, or executive compensation. Find those before they find you.

## Level-Specific Notes

### Team leads and frontline managers

- know which data your team creates, changes, and relies on
- document local definitions and caveats
- report data defects that affect customers, operations, or decisions
- avoid creating unofficial sources of truth without visibility
- review dashboards before using them to steer work

### Managers of managers

- assign domain owners and stewards
- standardize important definitions
- prioritize quality fixes and analytics requests
- maintain cross-team reporting trust
- ensure access, retention, and privacy/security interfaces are working

### Directors and senior leaders

- decide authoritative sources and ownership for major domains
- govern critical metrics and executive reporting
- fund data quality and platform work where it affects strategy/risk
- connect analytics priorities to operating and product decisions
- challenge dashboard theatre

### Executives

- avoid demanding numbers without definition discipline
- approve enterprise data ownership and source-of-truth decisions
- hold leaders accountable for quality of critical data
- use metrics as signals, not shields
- sponsor data foundations before demanding AI miracles from a warehouse full of mystery columns

## Common Artifacts

- data domain map
- data ownership register
- source-of-truth map
- business glossary
- critical data element register
- data quality dashboard
- lineage map
- report/dashboard inventory
- metric definition catalog
- analytics intake/prioritization backlog
- access-control matrix
- data retention schedule
- AI data-readiness assessment
- data incident/problem log
- dataset/report retirement log

## Practitioner Counterpart

For hands-on data extraction, analysis, dashboard/report production, data-quality investigation, lineage/evidence capture, and privacy-bound execution support, see [Data / Analytics Practitioner](https://github.com/RusDavies/docs-practitioner-practices/blob/master/roles/data-analytics-practitioner.md). This management guide owns data accountability, source-of-truth decisions, prioritization, governance, and risk acceptance.

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

In data and analytics management, AI tooling will generate queries, explain dashboards, profile data, detect anomalies, map lineage, draft metric definitions, and help users explore data. The practical opportunity is broader analytical access with better evidence trails.

The risk is democratized confusion: everyone gets answers faster from data they do not understand. Data leaders still own sources of truth, definitions, quality thresholds, access boundaries, privacy/security constraints, and whether a dataset is fit for AI or decision use.

## Anti-Patterns

- no named owner for critical data
- every department maintaining its own source of truth
- dashboards with no definitions or caveats
- changing metric definitions silently
- treating data quality as an IT-only problem
- building AI on data nobody understands
- preserving stale reports forever
- over-restricting data until nobody can do useful analysis
- under-restricting data until everybody can see everything
- rewarding teams based on metrics they can game
- using analytics teams as a ticket queue for executive curiosity
- fixing reports instead of fixing broken upstream processes

## Review Questions

- Who owns this data domain?
- What is the authoritative source for this data concept?
- Which decisions depend on this report or metric?
- Are definitions, sources, refresh cadence, and caveats documented?
- What quality level is required for the decision being made?
- Can we trace the data from source to report/model/decision?
- Are access, privacy, security, legal, and retention requirements satisfied?
- Is this dashboard certified, operational, exploratory, or deprecated?
- What behavior will this metric encourage?
- Is the data suitable for AI/automation use, or merely available?
- What should be retired because it is stale, duplicated, or misleading?
