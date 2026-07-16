# Role Corpus Architecture

## Purpose

This note defines the corpus-level split between management/leadership practices and practitioner/operator practices.

The distinction matters because these documents are not merely context to feed into an agent. They define roles, domains, authority, workflows, evidence expectations, and boundaries. Downstream agent-specialist artifacts must inherit those distinctions instead of blending management accountability with practitioner execution.

## Corpus Boundary

`docs-management-practices` is the canonical corpus for management and leadership disciplines.

It covers:

- ownership of outcomes, standards, risk, capacity, and operating cadence
- decision rights, approvals, escalation, and accountability
- governance across teams, functions, suppliers, customers, and stakeholders
- management artifacts such as operating reviews, decision records, approval gates, risk registers, succession plans, and post-incident actions
- guidance for leaders adapting practice to team, department, portfolio, executive, or matrix contexts

Practitioner/operator roles need a separate corpus boundary.

That separate corpus should cover:

- hands-on practitioner workflows
- operator runbooks and execution practices
- craft-specific constraints, tools, checks, and evidence
- task-level outputs and verification expectations
- role-native Spec / Verifier / Environment profiles

The practitioner/operator corpus lives in [docs-practitioner-practices](https://github.com/RusDavies/docs-practitioner-practices). `docs-worker-practices` was considered, but is less precise. "Practitioner" better covers professional craft roles, operational roles, and specialist execution without making the corpus sound like an HR classification exercise escaped from a filing cabinet.

Governance/advisory roles need a third corpus boundary.

That separate corpus covers board members, advisors, committee/council members, sponsor/stewards, governance evidence, decision records, advice notes, conflict/recusal declarations, committee charters, and follow-up registers. These roles may advise, approve, oversee, escalate, or hold management accountable, but they should not be blurred into management execution or practitioner/operator work.

The governance/advisory corpus lives in [docs-governance-practices](https://github.com/RusDavies/docs-governance-practices). This management corpus may cross-reference that guidance where executives, sponsors, portfolios, programs, or management forums interface with governance bodies, but it should not host board-member, advisor, committee/council, or governance-steward role files.

## Why Separate the Corpora

A domain can contain both management and practitioner roles. Software engineering, quality, HR, security, operations, procurement, and support all have this shape.

The work differs by role:

- management roles set direction, allocate responsibility, approve trade-offs, govern risk, and ensure outcomes
- governance/advisory roles challenge, advise, approve, oversee, or escalate within a charter without default ownership of day-to-day management execution
- practitioner roles perform specialist work, produce domain artifacts, run checks, and provide evidence
- operator roles execute repeatable operational workflows, monitor state, follow runbooks, and escalate exceptions
- hybrid roles combine scopes, but must still name which authority they are exercising at a given moment

If the corpora blur these roles, generated specialists can quietly cross authority boundaries. That produces the bad kind of helpfulness: agents approving their own work, managers pretending oversight is execution, or practitioners making governance decisions without authority.

## Terminology

**Management role:** A role accountable for outcomes, direction, standards, prioritization, resource allocation, approval boundaries, risk acceptance, escalation, and organizational learning. A management role may understand practitioner work deeply, but its primary responsibility is not hands-on execution.

**Governance/advisory role:** A role that advises, challenges, oversees, approves, escalates, or holds management accountable within a defined charter. It may shape decisions or require evidence, but it does not automatically own management execution or practitioner work.

**Practitioner role:** A specialist role that performs craft work in a domain. It designs, builds, tests, analyzes, investigates, advises, or produces artifacts within defined constraints. It may recommend decisions, but does not automatically own management approval or organizational risk acceptance.

**Operator role:** A role that runs defined operational workflows, monitors state, performs repeatable procedures, handles queues, executes runbooks, and escalates exceptions. Operator work may be skilled and judgment-heavy, but its authority is usually bounded by procedure, service level, escalation path, and control requirements.

**Hybrid role:** A role that legitimately combines management, practitioner, or operator responsibilities. Hybrid roles must still label the active scope and authority boundary. "I can do both" is not the same as "I can approve both."

**Domain:** The subject area or operating area, such as software engineering, quality, HR, security, finance, procurement, customer success, or operations.

**Discipline:** A coherent body of practice within a domain. A discipline can have management and practitioner variants. For example, quality management and QA/test practice share a domain, but they do different work.

**Authority boundary:** The line between work a role may do independently, work it may recommend, work requiring approval, and work it must not do. Authority boundaries include decision rights, approval gates, risk acceptance, legal/security/privacy constraints, customer commitments, budget authority, and personnel decisions.

## Role Scope Examples

### Software Engineering

Software engineering management owns team outcomes, standards, ownership, delivery risk, quality posture, staffing, approval boundaries, and trade-offs across delivery, operations, product, architecture, security, and capacity.

Software engineering practice owns implementation, code behavior, tests, architecture conformance, runtime constraints, deployment readiness evidence, maintainability, and technical recommendations.

### Quality

Quality management owns quality strategy, acceptance risk, release gates, defect governance, accountable approval, measurement, and cross-functional quality improvement.

QA/test practice owns test design, exploratory testing, regression testing, test data, harnesses, reproducibility, defect evidence, and quality signals.

### HR

HR management owns policy, workforce planning, role design, employee-relations governance, compliance posture, organizational risk, and management decision support.

HR operations practice owns onboarding workflows, records, benefits operations, interview logistics, case processing, employee support workflows, and operational evidence.

## Downstream Agent-Specialist Rule

Every generated specialist must declare its scope:

- management-scoped
- governance/advisory-scoped
- practitioner-scoped
- operator-scoped
- hybrid-scoped

Generated specs, verifiers, environments, tasks, retrieval chunks, evaluation scenarios, and review gates must be role-specific.

Agents must not silently cross from practitioner execution into management approval, or from management oversight into practitioner execution. If a task requires crossing the boundary, the artifact should say so explicitly and require the correct approval, handoff, or escalation.

## Initial Implementation Decision

This repository should receive:

- this architecture note
- role-scope terminology
- management-side cross-references
- TODOs for the role-definition template, initial examples, practitioner corpus creation, and downstream agent-specialist propagation

The separate practitioner corpus has been created and seeded with a small number of examples rather than attempting a broad rewrite.

Use [Role Definition](templates/role-definition.md) when defining management, practitioner, operator, or hybrid roles for either corpus. Use [Role Scope Split Examples](ROLE_SCOPE_SPLIT_EXAMPLES.md) for initial software engineering, quality, and HR boundary examples.

Do not rewrite the whole management corpus in one pass. First establish the structure, language, and examples clearly enough that future discipline files can follow the pattern.
