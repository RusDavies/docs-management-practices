# Role Definition

## Purpose

Define a role clearly enough that people, teams, and downstream agent-specialist artifacts understand its scope, authority, evidence, outputs, boundaries, and failure modes.

Use this template when a role may be confused with an adjacent management, practitioner, operator, or hybrid role in the same domain.

## Role Identity

- Role name:
- Domain:
- Discipline:
- Role scope: management / practitioner / operator / hybrid
- Owning organization / team:
- Primary audience:
- Related roles:
- Source documents / references:
- Last reviewed:

## Role Summary

Briefly describe what this role exists to do:

> 

## Work This Role Does

| Work area | Description | Typical cadence | Evidence / artifact |
| --- | --- | --- | --- |
|  |  |  |  |

## Work This Role Must Not Do

| Out-of-scope work | Why it is out of scope | Correct owner / handoff |
| --- | --- | --- |
|  |  |  |

## Authority Boundary

| Decision / commitment | Can decide independently? | Can recommend? | Requires approval from | Notes |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Decisions and Commitments This Role Can Make

- 

## Decisions and Commitments Requiring Approval

| Decision / commitment | Approval owner | Evidence required | Timing / gate |
| --- | --- | --- | --- |
|  |  |  |  |

## Inputs and Evidence Needed

| Input / evidence | Source | Required? | Quality bar |
| --- | --- | --- | --- |
|  |  |  |  |

## Outputs and Artifacts Produced

| Output / artifact | Audience | Review / approval | Retention / location |
| --- | --- | --- | --- |
|  |  |  |  |

## Spec Profile

Describe what "good work" means for this role.

| Spec area | Definition |
| --- | --- |
| Outcomes this role is accountable for |  |
| Constraints this role must respect |  |
| Standards / policies this role follows |  |
| Quality bar |  |
| Human approval gates |  |
| Escalation triggers |  |

## Verifier Profile

Describe how this role's work is checked.

| Verifier | What it checks | Evidence | Failure response |
| --- | --- | --- | --- |
| Human review |  |  |  |
| Automated check / test |  |  |  |
| Peer / cross-functional review |  |  |  |
| Audit / compliance review |  |  |  |
| Outcome / operational signal |  |  |  |

## Environment Profile

Describe the systems, data, tools, constraints, and operating context for the role.

| Environment area | Detail |
| --- | --- |
| Systems / tools used |  |
| Data accessed |  |
| Data this role must not access |  |
| Permissions / access level |  |
| Operating cadence |  |
| Communication channels |  |
| Legal / security / privacy constraints |  |
| Dependency / escalation paths |  |

## Collaboration Boundaries

| Adjacent role | This role owns | Adjacent role owns | Handoff / escalation rule |
| --- | --- | --- | --- |
|  |  |  |  |

## Common Failure Modes

| Failure mode | Why it happens | Prevention / control |
| --- | --- | --- |
| Role silently crosses from recommendation into approval |  |  |
| Role performs execution without required oversight |  |  |
| Role provides oversight without understanding execution evidence |  |  |
| Adjacent roles duplicate work or leave a gap |  |  |
| Hybrid role fails to declare active authority scope |  |  |

## Role-Scope Check

- [ ] Role scope is explicitly labelled as management, practitioner, operator, or hybrid.
- [ ] Work performed by the role is separate from work it must not do.
- [ ] Independent decisions are separate from recommendations and approval-required decisions.
- [ ] Inputs, outputs, evidence, and artifacts are inspectable.
- [ ] Spec / Verifier / Environment profile is role-specific, not copied from the domain in general.
- [ ] Collaboration boundaries name adjacent roles and handoff rules.
- [ ] Failure modes include authority-boundary mistakes.

## Usage Notes

- Use this template before generating or revising agent-specialist artifacts from role guidance.
- A domain is not a role. Software engineering, quality, HR, security, support, and operations can each contain management, practitioner, operator, and hybrid roles.
- Hybrid roles are allowed, but the active authority boundary must be explicit. Otherwise "hybrid" becomes a polite word for confused.

## Example

A QA/Test Practitioner role may own test design, regression execution, exploratory testing, defect reproduction, and evidence production. It may recommend release risk, but the Quality Management role or release authority may own acceptance criteria, release-gate approval, and risk acceptance.
