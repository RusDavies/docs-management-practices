# Security Management

<!-- doctrine:id=security-management -->

## Purpose

Security management is the discipline of protecting the organization, its customers, users, systems, data, operations, people, products, and reputation from avoidable harm caused by misuse, abuse, accident, weakness, compromise, or hostile action.

It overlaps with technical debt, risk management, incident response, AI landscape management, procurement, vendor management, architecture, operations, compliance, privacy, product, data, people management, and executive leadership. That overlap is exactly why security management deserves its own discipline guide: security work is too cross-functional to be safely hidden inside engineering tickets, audit checklists, or an annual awareness slideshow featuring stock-photo hackers in hoodies.

Security management is not only cyber security, though cyber security is a major part of it. It includes the management system for identifying security responsibilities, setting security expectations, making risk tradeoffs, assigning control ownership, preventing issues, detecting weaknesses, responding to incidents, and ensuring remediation actually happens.

Good security management helps an organization:

- define who owns security decisions and controls
- prevent avoidable exposure before it becomes an incident
- manage vulnerabilities, dependencies, access, secrets, data exposure, and configuration risk
- integrate security into architecture, delivery, operations, procurement, vendor, AI, and product processes
- make security-risk tradeoffs explicit and approved by the right people
- maintain evidence for security decisions, controls, remediation, and exceptions
- reduce time-to-detect, time-to-triage, and time-to-remediate
- distinguish real security risk from performative security theatre
- build a culture where people can raise concerns before the breach report writes itself

Security is not the department that says no. Security is the management discipline that helps the organization say yes safely, no when necessary, and “not like that, you magnificent liability” when enthusiasm outruns control.

## Scope

Security management may cover:

- security program ownership
- security strategy and risk appetite
- vulnerability management
- security scanning governance
- secure delivery and release gates
- access governance
- identity, authentication, authorization, and privileged access
- secrets and key management
- data protection and exposure control
- dependency, supply-chain, and vendor security risk
- cloud, infrastructure, endpoint, application, product, and operational security
- security architecture and secure design
- security awareness and behaviour
- security exception handling
- remediation ownership and evidence
- incident prevention and readiness
- security metrics and reporting
- AI-enabled security and security of AI systems

The scope should be scaled. A small project does not need enterprise ceremony. A regulated, customer-facing, internet-exposed, data-rich, AI-enabled, vendor-dependent organization does not get to pretend a quarterly spreadsheet is a security program.

## Standalone or Split Across Other Disciplines?

Security management should be a standalone discipline in this corpus.

The reason is not that security is separate from everything else. It is because security is embedded in almost everything else and therefore needs a clear management spine.

Security work should still be distributed:

- technical debt management handles security defects, vulnerable dependencies, remediation economics, and exposure windows
- risk management handles appetite, acceptance, escalation, and enterprise risk posture
- incident response handles security events once harm or suspected compromise is active
- AI landscape management handles AI-specific security, model/provider/tool risks, prompt and retrieval exposure, and agent permissions
- procurement and vendor management handle supplier security review and third-party obligations
- architecture management handles secure design, boundaries, trust zones, and systemic control choices
- operations management handles secure operations, monitoring, patching, backup, continuity, and change control
- compliance management handles evidence, obligations, control mapping, and audit readiness

But none of those replaces the need for an explicit security management discipline. Without it, ownership fragments and security becomes everyone’s concern in the traditional sense: universally admired, locally avoided, and eventually discovered by a scanner at 2 a.m.

## Security Program Ownership

Security needs accountable ownership.

Clarify:

- who owns the security program
- who owns security risk acceptance
- who owns each major control family
- who owns security engineering and operational security work
- who owns product/application security decisions
- who owns identity and access governance
- who owns supplier and SaaS security review
- who owns security incident readiness and response interfaces
- who owns reporting to executives, customers, auditors, or regulators

In small organizations, one person may coordinate many of these areas. That is fine if the accountability is explicit. It is not fine if security is “owned by engineering” until a legal question appears, then “owned by legal” until a patch is needed, then “owned by operations” until nobody can explain why the dependency is still vulnerable.

## Security Strategy and Risk Appetite

Security strategy should explain what the organization is trying to protect and what tradeoffs it is willing to make.

Define:

- crown-jewel systems, data, customers, processes, and capabilities
- threat model at the right level of detail
- business-critical security outcomes
- risk appetite and unacceptable risks
- minimum control baseline
- security investment priorities
- security decision forums
- escalation triggers
- evidence expectations
- review cadence

Good security strategy is specific. “We take security seriously” is not strategy; it is the mating call of the unprepared press release.

## Vulnerability Management

Vulnerability management is the repeatable process for discovering, triaging, remediating, mitigating, accepting, and verifying weaknesses.

A practical vulnerability management model defines:

- discovery sources: scanners, code review, dependency alerts, penetration tests, bug reports, threat intel, vendor advisories, incidents, and internal findings
- asset and ownership mapping
- severity and exploitability criteria
- exposure and reachability analysis
- remediation SLAs or targets by risk class
- exception and risk-acceptance route
- fix verification
- regression/security test expectations
- evidence packet requirements
- reporting and escalation

Treat scanner output as input, not truth. A listed CVE may be unreachable. An unlisted code flaw may be critical. A patched package may break a production surface. Vulnerability management should combine tooling, context, ownership, and evidence rather than worshipping whichever dashboard has the most alarming shade of red.

Use tighter default remediation targets when AI-assisted analysis and remediation are available:

| Risk class | Default target |
| --- | --- |
| Critical | fix or verified mitigation ready within 1 hour; publish/push to production within 12 hours |
| High | fix, verified mitigation, or approved exception within 1 day |
| Moderate | fix, verified mitigation, or approved exception within 3 days |
| Low | fix, verified mitigation, or backlog decision within 7 days |

These are default operating targets, not a substitute for judgment. A valid mitigation path is to make the vulnerable path unreachable, provided the reachability change is verified, monitored, documented, and reviewed. Do not quietly relabel a reachable vulnerability as low risk because the direct upgrade is inconvenient. That is not risk management; it is optimism with a ticket number.

## Security Scanning Governance

Security scanning needs governance because scanners affect delivery, risk, operations, and trust.

Define:

- which scanners are authoritative for which asset classes
- what input formats and ecosystems are covered
- how findings are de-duplicated
- how false positives are handled
- how exceptions, VEX statements, and compensating controls are recorded
- when scans block release
- when scans create backlog work
- how scanner rules are updated
- how scan evidence is retained
- who can override a finding
- how fix-in-place remediation is represented when dependency versions cannot move safely

The goal is not “zero findings.” The goal is reliable security signal that leads to correct decisions. A scanner that blocks everything becomes ignored. A scanner that blocks nothing becomes wallpaper.

For AI-assisted remediation workflows, scanner findings should be analyzed in function/method/resource/package chunks with surrounding call, dependency, deployment, ownership, and test context rather than as isolated rows or whole-repository prompt dumps.

## Secure Delivery and Release Gates

Security should be embedded into delivery, not stapled onto the end while everyone waits for the release train to leave.

Security release gates may include:

- threat model or abuse-case review for high-risk changes
- secure design review
- data exposure review
- dependency and container/image scans
- static and dynamic analysis where useful
- secrets scanning
- access/permission review
- penetration testing or targeted security testing for material surfaces
- remediation evidence for high-risk findings
- exception approval for accepted risk
- rollback and incident-readiness checks

Release gates should be scaled to risk. A typo fix does not need the same gate as a new payment integration, AI agent with tool access, authentication change, customer-data export, admin permission model, or internet-exposed service. Context: apparently still undefeated.

## Access Governance

Access governance makes sure the right people, services, agents, and vendors have the right access for the right reasons, for the right duration.

Manage:

- identity sources and joiner/mover/leaver processes
- role and permission models
- privileged access
- production access
- service accounts and machine identities
- third-party and vendor access
- emergency access
- periodic access reviews
- segregation of duties where needed
- logging and monitoring of sensitive access
- approval and revocation workflows

Access decisions should be understandable. If nobody can explain what a role permits, why someone has it, or how to remove it safely, the role is not a permission model; it is folklore with admin rights.

## Secrets and Key Management

Secrets and keys need lifecycle management.

Define:

- approved secret storage locations
- prohibited storage locations
- generation and rotation rules
- owner for each secret or key family
- access and audit expectations
- emergency rotation process
- leaked-secret response
- retirement/deletion process
- treatment for API keys, signing keys, encryption keys, SSH keys, certificates, tokens, and credentials

Secrets should not live in source code, tickets, chat, spreadsheets, screenshots, personal notes, or “temporary” files that survive three reorganizations and an office move.

## Dependency and Supply-Chain Security

Modern systems inherit risk through dependencies, packages, images, build tools, hosted services, SaaS platforms, model providers, plugins, extensions, contractors, and vendors.

Dependency and supply-chain security should address:

- approved package sources and registries
- dependency review and update cadence
- lockfiles and provenance where relevant
- build and release integrity
- signed artifacts where needed
- vulnerable or abandoned dependency handling
- transitive dependency visibility
- vendor security reviews
- open source license/security interfaces
- container/base image ownership
- AI model, tool, plugin, and provider dependencies

The management question is not merely “is there a CVE?” It is “what do we depend on, who owns it, how exposed are we, how quickly can we change it, and what evidence proves the current decision?”

## Security Control Ownership

Controls need owners and operating routines.

For each major security control, define:

- control purpose
- accountable owner
- operating team
- frequency or trigger
- evidence produced
- failure mode
- escalation path
- exception route
- dependency on tools, vendors, or systems
- review cadence

Security controls without owners decay. They may still appear in diagrams, because diagrams are merciful and do not check production.

## Exception Handling and Risk Acceptance

Security exceptions happen. They must be visible, time-bound, and approved by the right authority.

A security exception should record:

- finding, control, or requirement affected
- affected asset, system, product, team, customer, or data
- reason for exception
- exposure and exploitability context
- compensating controls
- expiry date
- remediation plan
- accountable risk owner
- approving authority
- evidence and review date

Exceptions should not become untracked security debt. If the same exception keeps renewing, either fix the issue, change the standard, retire the thing, or admit the organization has accepted the risk. The spreadsheet should not have to carry the moral burden alone.

## Incident Prevention and Readiness

Security management should reduce incident likelihood and improve readiness.

Prevention and readiness include:

- threat-informed control priorities
- hardening baselines
- monitoring and alerting
- logging and evidence preservation
- backup and recovery expectations
- tabletop exercises
- incident playbooks
- credential compromise response
- data exposure response
- vulnerability emergency response
- customer/regulator communication interfaces
- lessons learned from incidents and near misses

Incident response starts when something has happened. Security management owns much of the discipline that makes that moment less frequent and less chaotic.

## Awareness and Security Culture

Security awareness should help people make better decisions, not merely complete training.

Good security culture means:

- people can ask security questions without being mocked or punished
- teams know which decisions require review
- reporting suspected issues is easy
- managers model secure behaviour
- security controls are explained in operational terms
- near misses produce learning, not reflexive blame
- shortcuts are examined as system-design feedback

Training matters when it changes behaviour. If the entire programme is an annual phishing quiz and a poster telling people not to click links, the organization is mostly managing vibes.

## Cross-Functional Security-Risk Tradeoffs

Security tradeoffs should be explicit.

Common tensions include:

- faster release vs security evidence
- customer commitment vs secure design
- operational convenience vs access control
- vendor capability vs supplier risk
- AI productivity vs data exposure
- dependency upgrade vs product compatibility
- compliance deadline vs engineering capacity
- incident transparency vs legal/reputation concern
- usability vs authentication strength

Good management makes the tradeoff visible, names the owner, records the decision, sets review dates, and ensures the people carrying the risk know they are carrying it.

## Metrics and Reporting

Security metrics should inform action.

Useful measures may include:

- critical asset ownership coverage
- vulnerability age by risk class
- mean time to triage/remediate high-risk findings
- exposed secrets detected and rotation time
- access-review completion and revocation outcomes
- privileged-access exceptions
- release gate exceptions
- high-risk vendor reviews due/overdue
- security incident trends and near misses
- repeat findings
- remediation evidence completeness
- control failures and overdue reviews

Avoid metrics that reward hiding work. If teams are punished for reporting findings, the metric will improve while security gets worse. Humans: still hackable, mostly by dashboards.

## Disagree and Commit

Security decisions need honest disagreement before commitment.

Healthy disagreement means:

- security explains threat, exposure, likelihood, consequence, and control purpose clearly
- product, engineering, operations, sales, legal, and finance explain constraints honestly
- risk owners understand what is being accepted or delayed
- security requirements are challenged when they are disproportionate or unclear
- exceptions are documented with expiry and review
- once a decision is made, teams commit to the control, remediation, or accepted-risk path

The goal is not for security to win every argument. The goal is for the organization to make conscious decisions with named owners and no secret parallel reality.

## Common Artifacts

Common security management artifacts include:

- security strategy
- [security control owner map](../templates/security-control-owner-map.md)
- asset and data criticality register
- vulnerability management policy
- [vulnerability triage record](../templates/vulnerability-triage-record.md)
- [remediation evidence packet](../templates/ai-agent-remediation-evidence-packet.md)
- release security gate checklist
- [security exception/risk acceptance record](../templates/security-exception-risk-acceptance-record.md)
- [access review record](../templates/access-review-record.md)
- privileged-access register
- [secrets/key register](../templates/secrets-key-register.md)
- threat model or abuse-case review
- supplier security review record
- security metrics dashboard
- [incident readiness checklist](../templates/security-incident-readiness-checklist.md)
- security awareness plan

Artifacts should serve decisions. If an artifact exists only because a template escaped captivity, retire it humanely.

## Practitioner Counterparts

For hands-on security-control evidence, alert/vulnerability workflow support, access-review preparation, and exception evidence, see [Security Operations Practitioner](https://github.com/RusDavies/docs-practitioner-practices/blob/master/roles/security-operations-practitioner.md). For fix-in-place vulnerability remediation evidence and remediation execution, see [Security Vulnerability Remediation Practitioner](https://github.com/RusDavies/docs-practitioner-practices/blob/master/roles/security-vulnerability-remediation-practitioner.md). This management guide owns security program accountability, risk acceptance, control ownership, and escalation.

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

In security management, AI tooling can help triage scanner findings, cluster vulnerabilities, draft threat models, propose remediation plans, generate regression/security tests, summarize security evidence, review configurations, detect anomalous access patterns, and prepare exception or risk-acceptance drafts.

AI can also create new security risk through code generation, agent tool access, prompt injection, retrieval leakage, data exposure, model/provider dependency, autonomous action, and false confidence. Security management therefore has two AI responsibilities:

- use AI safely to improve security work
- secure AI systems, tools, agents, workflows, and providers through the AI landscape and related controls

Required controls include source-grounded analysis, human approval for material risk decisions, reproducible evidence, tool permission boundaries, secure handling of sensitive data, model/provider intake, evaluation against known failure modes, and rollback/incident plans.

AI should help reduce exposure windows and evidence drag. It should not become a magical vulnerability oracle that invents CVEs, patches production unaudited, or explains to auditors that “the model seemed confident.”

## Anti-Patterns

Watch for these failure modes:

- treating security as an engineering-only backlog
- measuring security by scanner counts without exposure context
- accepting vulnerabilities forever because upgrade work is inconvenient
- blocking releases with unclear or disproportionate requirements
- letting exceptions renew indefinitely
- assigning control ownership to security when operating teams own the real work
- relying on annual training while ignoring unsafe processes
- reviewing vendors after contracts are signed
- treating AI-generated security analysis as authoritative without evidence
- confusing compliance evidence with actual security effectiveness
- failing to connect security incidents back to prevention, architecture, access, vendor, or delivery controls
- hiding security risk because reporting it makes a metric worse

## Practical Starting Point

For a small or growing organization, start with:

1. Name the security owner and decision forum.
2. List critical systems, data, suppliers, and identities.
3. Define minimum controls for access, secrets, dependencies, backups, logging, and release gates.
4. Establish vulnerability triage and remediation rules.
5. Create a time-bound exception process.
6. Add security review to material architecture, product, AI, vendor, and release decisions.
7. Track a small set of metrics that lead to action.
8. Run at least one incident tabletop before reality runs one for you.

Start small, but make the ownership real. Security maturity is not purchased in a platform. It is built through repeated decisions that make the safe path easier and the risky path visible.
