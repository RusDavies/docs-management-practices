# Role Scope Split Examples

## Purpose

These examples show how one domain can contain distinct management and practitioner/operator roles without merging their authority, work, evidence, or downstream agent-specialist profiles.

Use these as starter patterns when defining role-specific guidance with [Role Definition](templates/role-definition.md). The practitioner/operator examples here are intentionally boundary examples, not a substitute for the future `docs-practitioner-practices` corpus.

## Software Engineering

### Software Engineering Management

- Role scope: management
- Domain: software engineering
- Discipline: software engineering management

Work this role does:

- sets engineering standards, ownership expectations, and delivery-health review cadence
- assigns responsibility for services, systems, technical decisions, quality posture, and operational readiness
- balances product goals, engineering capacity, technical debt, security, architecture, reliability, and staffing
- makes or escalates trade-off decisions about scope, timelines, risk, quality, and resource allocation
- reviews evidence from practitioners and adjacent functions before approval or escalation

Work this role must not do:

- silently override implementation details without engaging the accountable practitioner or technical owner
- approve its own technical evidence when independent review is required
- treat hands-on coding activity as a substitute for staffing, standards, ownership, or delivery-risk management

Authority boundary:

| Can decide | Can recommend | Requires approval |
| --- | --- | --- |
| team ownership model, review cadence, engineering standards within delegated scope | architecture direction, major technical investment, risk acceptance options | material budget changes, contractual/customer commitments, security/privacy exceptions, executive-level delivery trade-offs |

Inputs and evidence:

- delivery health, incident history, defect trends, operational signals, architecture decisions, technical-debt registers, staffing capacity, security findings, product priorities

Outputs and artifacts:

- engineering operating model, service ownership map, technical-debt remediation priorities, quality/release posture, escalation notes, staffing and capacity recommendations

Spec profile:

- good work produces coherent engineering ownership, visible trade-offs, inspectable decision records, and teams that can deliver without heroics as the operating model

Verifier profile:

- delivery outcomes, quality signals, incident trends, review evidence, peer/leader review, audit/security feedback, team health, and follow-through on accepted actions

Environment profile:

- operates across product, engineering, architecture, security, operations, support, finance, and leadership systems

Failure modes:

- turning management into code review theatre
- approving risky delivery because the team is busy
- outsourcing engineering judgment entirely to dashboards or practitioner optimism
- accepting risk without the authority to accept it

### Software Engineering Practitioner

- Role scope: practitioner
- Domain: software engineering
- Discipline: software engineering practice

Work this role does:

- designs, implements, reviews, tests, debugs, documents, and maintains software behavior
- produces technical evidence for architecture, quality, security, deployment, and operational readiness
- identifies implementation risks, technical constraints, and remediation options
- recommends trade-offs based on code, runtime, dependency, data, test, and operational evidence

Work this role must not do:

- accept organizational delivery, budget, staffing, legal, security, privacy, or customer-commitment risk without the correct approval
- bypass management, architecture, security, product, or release gates because implementation is complete
- treat code passing local tests as business approval

Authority boundary:

| Can decide | Can recommend | Requires approval |
| --- | --- | --- |
| implementation approach within approved design and standards, local code/test changes, technical evidence produced | architecture changes, release readiness, remediation sequencing, dependency upgrades | release approval, customer commitments, risk acceptance, production exceptions, staffing or budget changes |

Inputs and evidence:

- requirements, design constraints, architecture guidance, codebase state, test results, logs, dependency data, security findings, runbooks, deployment constraints

Outputs and artifacts:

- code changes, tests, pull requests, design notes, defect reproductions, evidence packets, runbook updates, technical recommendations

Spec profile:

- good work produces correct, maintainable, tested, observable, secure-enough software behavior within agreed constraints

Verifier profile:

- automated tests, code review, static analysis, runtime checks, deployment validation, security review, incident/defect feedback

Environment profile:

- operates in source repositories, CI/CD, runtime environments, issue trackers, observability tools, dependency systems, and documentation

Failure modes:

- making management approval decisions through implementation momentum
- hiding uncertainty in technical language
- optimizing local code quality while ignoring product, security, operational, or customer constraints

## Quality

### Quality Management

- Role scope: management
- Domain: quality
- Discipline: quality management

Work this role does:

- defines quality strategy, acceptance standards, release gates, quality metrics, and governance cadence
- decides how quality risk is surfaced, reviewed, escalated, accepted, or blocked
- coordinates quality responsibilities across product, engineering, operations, support, security, compliance, and leadership
- ensures defect trends and post-release failures produce operating improvements

Work this role must not do:

- pretend release approval is the same as test execution
- make defect severity or acceptance decisions without credible practitioner evidence
- turn QA practitioners into the only owners of quality

Authority boundary:

| Can decide | Can recommend | Requires approval |
| --- | --- | --- |
| quality review cadence, acceptance-risk framing, defect-governance process, release-gate evidence expectations | release go/no-go options, quality investments, process changes | major release risk acceptance, customer-facing commitments, regulatory exceptions, executive trade-offs |

Inputs and evidence:

- test results, defect trends, escaped defects, incident history, customer impact, release readiness evidence, support feedback, compliance obligations

Outputs and artifacts:

- quality strategy, release-readiness criteria, defect governance, quality dashboards, acceptance-risk summaries, corrective-action priorities

Spec profile:

- good work makes quality expectations explicit, evidence-based, and connected to business, customer, regulatory, and operational risk

Verifier profile:

- release outcomes, escaped-defect trends, audit/compliance review, customer impact, defect aging, corrective-action completion, leadership review

Environment profile:

- operates across test management, release governance, incident review, customer feedback, product planning, support, and compliance systems

Failure modes:

- using test counts as quality proof
- approving releases by schedule pressure rather than evidence
- making QA the quality department instead of treating quality as a system property

### QA/Test Practitioner

- Role scope: practitioner
- Domain: quality
- Discipline: QA/test practice

Work this role does:

- designs and executes tests, exploratory sessions, regression checks, crash tests, and reproduction workflows
- builds or maintains test data, test harnesses, fixtures, and evidence
- reports defects with clear reproduction, impact, environment, and confidence notes
- provides release-quality evidence and risk signals

Work this role must not do:

- own final release acceptance unless explicitly delegated by the release authority
- accept business, regulatory, customer, or executive risk alone
- allow test execution volume to stand in for quality judgment

Authority boundary:

| Can decide | Can recommend | Requires approval |
| --- | --- | --- |
| test design within scope, reproduction method, evidence format, exploratory focus | release risk, defect severity, test coverage gaps, automation investment | release approval, risk acceptance, scope reduction, regulatory/customer exception |

Inputs and evidence:

- requirements, acceptance criteria, risk areas, builds, environments, test data, defect history, customer workflows, production signals

Outputs and artifacts:

- test cases, exploratory notes, defect reports, reproduction evidence, regression results, coverage notes, quality-risk recommendations

Spec profile:

- good work provides credible evidence about product behavior, risk, and confidence limits

Verifier profile:

- defect reproducibility, peer review, automation results, escaped-defect feedback, release outcomes, stakeholder review

Environment profile:

- operates in test environments, test management systems, issue trackers, product builds, automation frameworks, logs, and customer workflow references

Failure modes:

- testing only the happy path because it is easier to report
- presenting absence of found defects as proof of quality
- accepting release risk because the practitioner has the clearest evidence

## HR

### HR Management

- Role scope: management
- Domain: HR / people operations
- Discipline: HR management

Work this role does:

- defines HR policy, employee-relations governance, workforce planning, role design, manager enablement, and compliance posture
- advises leaders on people-risk, fairness, legal, performance, hiring, development, and organizational implications
- decides or escalates HR risk, exception handling, investigation pathways, and management accountability
- ensures HR operations produce reliable evidence without turning people into paperwork units

Work this role must not do:

- process sensitive cases without respecting privacy, legal, evidence, and authority boundaries
- let operational convenience override fairness, legal constraints, or employee trust
- treat HR operations execution as policy approval

Authority boundary:

| Can decide | Can recommend | Requires approval |
| --- | --- | --- |
| HR process standards within delegated scope, manager guidance, case-routing expectations, policy interpretation within authority | workforce changes, role design, employee-relations actions, policy changes | termination, compensation changes, legal settlements, regulated accommodations, executive workforce decisions |

Inputs and evidence:

- workforce data, manager input, case history, policy, employment law guidance, compliance obligations, employee feedback, performance evidence, hiring plans

Outputs and artifacts:

- HR policy guidance, workforce plans, role designs, manager enablement, employee-relations recommendations, compliance posture notes, escalation records

Spec profile:

- good work balances organizational need, employee dignity, legal/compliance requirements, fairness, manager accountability, and evidence quality

Verifier profile:

- legal/compliance review, case outcomes, manager/employee feedback, audit evidence, consistency checks, escalation review, workforce outcomes

Environment profile:

- operates across HRIS, case management, performance systems, recruiting, benefits, legal, finance, leadership, and manager channels

Failure modes:

- mistaking policy ownership for unilateral authority over every people decision
- letting managers outsource accountability to HR
- using confidentiality as a blanket excuse for poor decision records

### HR Operations Practitioner

- Role scope: operator / practitioner
- Domain: HR / people operations
- Discipline: HR operations practice

Work this role does:

- runs onboarding, records, benefits, interview logistics, case intake, employee support, documentation, and workflow coordination
- maintains accurate employee and process records within privacy and access rules
- routes cases to managers, HR management, legal, payroll, benefits, or external providers when required
- produces operational evidence for HR processes and service levels

Work this role must not do:

- make policy, legal, disciplinary, compensation, accommodation, or termination decisions without authority
- disclose sensitive employee information outside permitted channels
- treat completion of a workflow step as approval of the underlying people decision

Authority boundary:

| Can decide | Can recommend | Requires approval |
| --- | --- | --- |
| workflow execution steps within procedure, record correction routing, support-ticket handling within policy | process improvements, case-routing concerns, employee-experience friction | policy exceptions, legal/employee-relations decisions, compensation changes, accommodation decisions, termination or discipline |

Inputs and evidence:

- employee records, forms, policy references, manager requests, case notes, benefits data, recruiting schedules, onboarding checklists, access approvals

Outputs and artifacts:

- completed onboarding steps, HRIS updates, case records, benefits transactions, interview schedules, employee support responses, evidence logs

Spec profile:

- good work is accurate, timely, private, consistent, and escalates exceptions rather than improvising authority

Verifier profile:

- record audits, SLA review, privacy/access checks, employee feedback, manager feedback, compliance review, case closure quality

Environment profile:

- operates in HRIS, case management, benefits systems, recruiting tools, document repositories, communication channels, and access workflows

Failure modes:

- making informal policy decisions to keep the queue moving
- over-sharing sensitive information in broad channels
- escalating every exception without triage, or handling serious exceptions without escalation

## Legal

### Legal Management

- Role scope: management
- Domain: legal
- Discipline: legal management

Work this role does:

- defines legal intake, review gates, matter ownership, decision rights, escalation thresholds, and outside-counsel coordination
- ensures qualified legal review happens for contracts, disputes, employment matters, public claims, product/data changes, regulatory exposure, and material commitments
- separates legal advice from business risk acceptance
- manages privilege, confidentiality, legal holds, sensitive matter information, and legal operations visibility

Work this role must not do:

- treat legal advice as automatic business approval
- let urgent commercial, product, or people decisions bypass legal-review gates
- confuse legal operations coordination with qualified legal practice outside delegated competence

Authority boundary:

| Can decide | Can recommend | Requires approval |
| --- | --- | --- |
| legal intake path, review-gate criteria, approved-position routing, matter-status cadence, outside-counsel coordination within delegated scope | legal-risk framing, contract fallback positions, escalation options, matter strategy, playbook improvements | material legal-risk acceptance, settlement, privilege waiver, signature/commitment authority, public/regulator position, outside-counsel spend beyond authority |

Inputs and evidence:

- matter facts, contracts, communications, legal question, jurisdiction, entity, decision owner, approved templates/playbooks, prior advice, risk/compliance/privacy/security/product/people evidence

Outputs and artifacts:

- legal matter intake record, review-gate matrix, legal-risk assessment, clause playbook, outside-counsel brief, matter status register, obligation handoff, risk-acceptance decision record

Spec profile:

- good work gives qualified legal work a clear operating path and gives authorized decision makers enough advice, evidence, and escalation context to accept or reject legal risk deliberately

Verifier profile:

- legal/counsel review, matter outcomes, missed-gate review, contract exception trends, privilege/confidentiality handling, outside-counsel spend review, lessons-learned review

Environment profile:

- operates across matter-management, contract, document, legal research, HR, procurement, security, privacy, product, finance, executive, and outside-counsel systems

Failure modes:

- asking legal after the promise is already made
- copying legal on everything and assuming privilege appeared
- hiding signed obligations from the teams expected to operate them
- using legal as either a department of "no" or a rubber stamp with a law degree

### Legal Practitioner

- Role scope: practitioner
- Domain: legal
- Discipline: legal practice

Work this role does:

- researches legal questions, reviews and drafts contracts or legal materials, supports matters, organizes evidence, prepares issue lists, and produces legal work product
- applies approved templates, clause playbooks, fallback positions, and review standards within delegated scope
- supports outside counsel, disputes, investigations, regulator inquiries, employment matters, IP matters, corporate matters, and obligation handoffs
- escalates missing facts, non-standard positions, privilege issues, and material legal exposure

Work this role must not do:

- accept business, legal, financial, operational, employment, privacy, security, reputational, or delivery risk without the correct approval
- sign contracts, waive privilege, settle matters, authorize commitments, or instruct outside counsel without authority
- give legal advice outside competence, jurisdiction, supervision, authorization, or license constraints

Authority boundary:

| Can decide | Can recommend | Requires approval |
| --- | --- | --- |
| research approach, draft structure, issue-list organization, evidence indexing, approved-template use within delegated scope | legal options, clause language, fallback positions, matter next steps, outside-counsel questions | legal-risk acceptance, settlement, signature/commitment, privilege waiver, public/regulator position, non-standard exception, outside-counsel spend/scope |

Inputs and evidence:

- legal question, facts, documents, communications, jurisdiction, entity, policies, templates, playbooks, prior advice, deadlines, privilege/confidentiality constraints, and reviewer expectations

Outputs and artifacts:

- research memo, contract redline, advice draft, issue list, matter chronology, document index, legal hold support record, outside-counsel packet, obligation handoff note

Spec profile:

- good work is accurate, source-grounded, confidentially handled, reviewable, and explicit about assumptions, caveats, authority limits, and escalation needs

Verifier profile:

- qualified legal review, source check, jurisdiction/competence check, factual review, playbook conformance, privilege/confidentiality review, approval-threshold review

Environment profile:

- operates in legal research tools, document repositories, matter-management systems, contract tools, secure collaboration systems, intake queues, and approved AI-assisted tooling

Failure modes:

- answering the business question instead of the legal question
- treating an old contract as safe precedent without checking context
- sending privileged or sensitive material through unapproved tools
- using AI-generated law, citations, or clause summaries without verification

## Reuse Guidance

When adding future role split examples:

- start with the domain
- define management accountability separately from practitioner/operator execution
- name authority boundaries before describing tasks
- treat Spec / Verifier / Environment as role-native, not domain-generic
- link to the future practitioner corpus for full practitioner guidance once it exists
