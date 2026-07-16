# AI Agent Permission Matrix

## Purpose

Use this matrix before approving, operating, or reviewing an AI agent that can read data, call tools, write changes, communicate externally, or affect production systems.

Agents need sharper control than ordinary chat tools because they can act. A chatbot can hallucinate. An agent can hallucinate and then press buttons. Humanity, ever inventive, found a way to give autocomplete a change window.

## Scope

Agent, workflow, product, platform, team, or environment covered by this matrix:

## Matrix Owner

Person or forum accountable for maintaining this matrix:

## Review Cadence

How often permissions are reviewed, and by whom:

## Agent Summary

| Field | Value |
| --- | --- |
| Agent name |  |
| Agent ID / system reference |  |
| AI landscape register ID |  |
| AI use-case intake / assessment reference |  |
| Prompt / retrieval-source register reference |  |
| Business owner |  |
| Technical owner |  |
| Security/privacy contact |  |
| Purpose |  |
| User group |  |
| Environment | Local / Dev / Test / Staging / Production / Mixed |
| Lifecycle state | Proposed / Experiment / Approved / Production / Restricted / Retiring / Retired |
| Approval status | Pending / Approved / Approved with conditions / Rejected / Restricted |

## Permission Summary

| Permission Area | Current State | Target State | Owner | Evidence / Notes |
| --- | --- | --- | --- | --- |
| Identity used |  |  |  |  |
| Authentication method |  |  |  |  |
| Human operator role |  |  |  |  |
| Read access |  |  |  |  |
| Write access |  |  |  |  |
| Tool access |  |  |  |  |
| Network / external access |  |  |  |  |
| Production access |  |  |  |  |
| External communication |  |  |  |  |
| Destructive action access |  |  |  |  |
| Cost/rate limits |  |  |  |  |
| Audit logging |  |  |  |  |
| Rollback path |  |  |  |  |

## Identity and Authentication

| Question | Answer | Evidence / Notes |
| --- | --- | --- |
| Does the agent use a dedicated service identity? | Yes / No / N/A |  |
| Is the identity separate from human user accounts? | Yes / No / N/A |  |
| Is access least-privilege? | Yes / No / Unknown |  |
| Are credentials/tokens stored securely? | Yes / No / Unknown |  |
| Are credentials rotated? | Yes / No / N/A |  |
| Is MFA or equivalent control required where applicable? | Yes / No / N/A |  |
| Can the identity be disabled quickly? | Yes / No / Unknown |  |

## Tool Access Inventory

| Tool / System | Purpose | Read Scope | Write Scope | Environment | Approval Required? | Owner | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | None / Limited / Broad | None / Limited / Broad | Local / Dev / Test / Staging / Production | Yes / No |  |  |

Examples:

- browser automation
- source-code repository
- CI/CD system
- package/artifact repository
- ticketing system
- cloud console/API
- Kubernetes/cluster access
- database/query tool
- messaging/email/Discord/Slack
- file system
- secrets manager
- monitoring/logging platform
- procurement/vendor system

## Read Boundaries

| Data / System | Allowed? | Scope | Data Sensitivity | Controls | Notes |
| --- | --- | --- | --- | --- | --- |
| Public docs | Yes |  | Public |  |  |
| Internal docs | Yes / No / Restricted |  | Internal |  |  |
| Source code | Yes / No / Restricted |  | Internal / Confidential / Security-sensitive |  |  |
| Customer data | No / Restricted |  | Customer-sensitive / Regulated |  |  |
| Employee data | No / Restricted |  | Employee-sensitive |  |  |
| Production logs | No / Restricted |  | Security-sensitive / Customer-sensitive |  |  |
| Secrets/credentials | No |  | Secrets |  | Normally prohibited. |

## Write and Action Boundaries

| Action Type | Allowed Without Approval? | Approval Required? | Approver / Forum | Evidence / Notes |
| --- | --- | --- | --- | --- |
| Create draft content | Yes / No |  |  |  |
| Edit local files | Yes / No |  |  |  |
| Commit code | Yes / No |  |  |  |
| Push code | No / Restricted | Yes |  |  |
| Open pull request | Yes / No |  |  |  |
| Merge pull request | No / Restricted | Yes |  |  |
| Run tests/builds/scans | Yes / No |  |  |  |
| Deploy to dev/test | No / Restricted |  |  |  |
| Deploy to staging | No / Restricted | Yes |  |  |
| Deploy to production | No | Yes |  |  |
| Change permissions/access | No | Yes |  |  |
| Modify security/privacy/legal/financial settings | No | Yes |  |  |
| Delete data/resources | No | Yes |  |  |
| Send external messages | No / Restricted | Yes |  |  |
| Publish public content | No | Yes |  |  |
| Accept residual risk | No | Yes | Risk owner |  |

## External Communication Controls

| Channel | Allowed? | Conditions | Approval Required? | Audit Evidence |
| --- | --- | --- | --- | --- |
| Internal chat | Yes / No / Restricted |  |  |  |
| External email | No / Restricted |  | Yes |  |
| Customer support system | No / Restricted |  | Yes |  |
| Public social/web publishing | No |  | Yes |  |
| Vendor portal | No / Restricted |  | Yes |  |
| Open source issue/PR | No / Restricted |  | Yes where disclosure or reputation risk exists |  |

## Human Approval Gates

| Gate | Trigger | Required Approver | Evidence Required | Timeout / Expiry |
| --- | --- | --- | --- | --- |
| Production-impacting change | Any production change or deployment |  | Change summary, rollback, tests |  |
| Sensitive data access | Customer/employee/security/legal/regulated data |  | Data scope, purpose, approval |  |
| External communication | Message leaves organization or controlled channel |  | Draft, recipient, purpose |  |
| Destructive action | Delete, overwrite, revoke, terminate, disable |  | Impact, rollback, owner approval |  |
| Security/privacy/legal change | Control, policy, access, evidence, or legal posture change |  | Risk assessment, owner approval |  |
| Cost-increasing action | Material compute/API/vendor spend increase |  | Cost estimate, owner approval |  |
| Risk acceptance | Residual risk is accepted or deferred | Risk owner | Risk record, review date |  |

## Monitoring and Audit Evidence

| Evidence Type | Required? | Location | Owner | Retention |
| --- | --- | --- | --- | --- |
| Prompt/instruction versions | Yes / No |  |  |  |
| Tool calls/actions | Yes |  |  |  |
| Approval records | Yes |  |  |  |
| Input/output logs | Yes / Restricted |  |  |  |
| Errors/failures | Yes |  |  |  |
| Cost/usage logs | Yes / No |  |  |  |
| Access review records | Yes |  |  |  |
| Incident records | Yes / N/A |  |  |  |

## Failure, Rollback, and Kill Switch

| Question | Answer | Evidence / Notes |
| --- | --- | --- |
| Can the agent be disabled quickly? | Yes / No / Unknown |  |
| Who can disable it? |  |  |
| How are credentials revoked? |  |  |
| How are in-progress actions stopped? |  |  |
| How are changes rolled back? |  |  |
| How are affected users/systems notified? |  |  |
| What incident path applies? |  |  |

## Permission Review

At each review, ask:

- Does the agent still need each permission?
- Are read scopes still correct?
- Are write/action scopes still correct?
- Are production and external communication restrictions still enforced?
- Are approval gates working in practice?
- Are audit logs sufficient to reconstruct actions?
- Have prompts, tools, models, providers, or workflows changed?
- Have any incidents, near misses, or policy exceptions occurred?
- Can permissions be reduced?
- Should the agent be restricted, redesigned, or retired?

## Risk and Exception Record

| Exception / Risk | Rationale | Approved By | Date | Review Date | Conditions | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |

## Decision

Permission decision:

- Approved
- Approved with conditions
- Restricted
- Deferred pending evidence
- Rejected
- Retire/decommission

Rationale:

Conditions:

Review date:

AI landscape register ID:

## Follow-Up Actions

| Action | Owner | Due Date | Evidence / Notes |
| --- | --- | --- | --- |
|  |  |  |  |

## Related Guidance

- [AI Landscape Management](https://github.com/RusDavies/docs-management-practices/blob/master/disciplines/AI_LANDSCAPE_MANAGEMENT.md)
- [AI Use-Case Intake and Data Exposure Assessment](https://github.com/RusDavies/docs-management-practices/blob/master/templates/ai-use-case-intake-and-data-exposure-assessment.md)
- [AI Landscape Register](https://github.com/RusDavies/docs-management-practices/blob/master/templates/ai-landscape-register.md)
- [AI Prompt and Retrieval-Source Register](https://github.com/RusDavies/docs-management-practices/blob/master/templates/ai-prompt-and-retrieval-source-register.md)
- [AI Evaluation Report](https://github.com/RusDavies/docs-management-practices/blob/master/templates/ai-evaluation-report.md)
- [Risk Management](https://github.com/RusDavies/docs-management-practices/blob/master/disciplines/RISK_MANAGEMENT.md)
- [Incident Response Management](https://github.com/RusDavies/docs-management-practices/blob/master/disciplines/INCIDENT_RESPONSE_MANAGEMENT.md)
- [Security-Defect Remediation Prompt Pack](https://github.com/RusDavies/docs-management-practices/blob/master/templates/security-defect-remediation-prompt-pack.md)

## Usage Notes

- Complete this before granting an agent new read/write/tool permissions.
- Use it during periodic access reviews, not only at initial approval.
- Treat unknown permission scope as a risk, not a neutral placeholder.
- Link it to the AI landscape register, intake assessment, prompt/source register, and evaluation report where available.

## Example

For a code-review agent, record repository read access, pull-request comment permissions, CI log access, whether it can open branches or commits, whether human approval is required before merges, and where audit logs are retained.
