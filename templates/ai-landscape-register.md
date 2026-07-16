# AI Landscape Register

## Purpose

Use this register to track AI systems, tools, agents, models, vendors, embedded AI features, data exposure, controls, costs, lifecycle state, and retirement decisions.

The register is not the control. It is the map. The control comes from ownership, approved paths, process gates, technical guardrails, monitoring, and decisions people can actually enforce without needing a ceremonial spreadsheet drum circle.

## Scope

Organization, product, business unit, programme, platform, or team covered by this register:

## Register Owner

Name the person or forum accountable for keeping this register current:

## Review Cadence

How often this register is reviewed, and by whom:

## Landscape Entries

| ID | Name | Type | Purpose | Owner | Users | Customer-Facing? | Provider / Hosting | Data Sensitivity | Status | Risk Level | Cost Owner | Review Date |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AI-001 |  |  |  |  |  | No |  |  | Proposed |  |  |  |

## Entry Types

Use the most specific useful type:

- Internal AI application
- External model/API
- Enterprise copilot
- AI coding assistant
- Workflow agent
- Autonomous or semi-autonomous agent
- Retrieval-augmented generation system
- Embedded SaaS AI feature
- Customer-facing chatbot/assistant
- Employee-facing chatbot/assistant
- AI analytics/classification/recommendation tool
- Model evaluation/monitoring tool
- Prompt, retrieval-source, vector-store, or agent-tooling component
- Shadow/unapproved AI tool
- Other

## Lifecycle Status

- Proposed
- Experiment
- Approved
- Production
- Restricted
- Retiring
- Retired

## Data Exposure Assessment

| ID | Data Types Used | Data Sensitivity | Prompt/File Upload? | Provider Retention | Training on Submitted Data? | Logs / Audit Location | Data Owner Approval | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AI-001 |  | Public / Internal / Confidential / Regulated / Customer-sensitive / Employee-sensitive / Security-sensitive / Legal / Strategic | No |  | No / Disabled / Unknown |  |  |  |

## Data Sensitivity Categories

Use one or more:

- Public
- Internal
- Confidential
- Regulated
- Customer-sensitive
- Employee-sensitive
- Security-sensitive
- Legally privileged
- Trade-secret / strategic

## Provider, Vendor, and Dependency Details

| ID | Provider / Vendor | Contract / Procurement Status | Model(s) / Feature(s) | Hosting Region | Subprocessors Known? | Security Review | Privacy / Legal Review | Exit Path | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AI-001 |  | Not started / In review / Approved / Exception / Not required |  |  | Unknown |  |  |  |  |

## Evaluation Posture

| ID | Evaluation Required? | Evaluation Type | Baseline / Test Set | Last Evaluation Date | Key Results | Known Failure Modes | Human Review Required? | Next Evaluation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AI-001 | Yes | Accuracy / Safety / Security / Privacy / Bias / Cost / UX / Tool-use / Retrieval quality |  |  |  |  |  |  |

## Controls and Guardrails

| ID | Approved Use | Restricted Use | Prohibited Use | Access Controls | Technical Guardrails | Human Approval Gates | Monitoring / Logging | Incident Path |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AI-001 |  |  |  |  |  |  |  |  |

Examples of guardrails:

- approved tool only
- blocked sensitive data classes
- disabled provider training on submitted data
- domain or repository allowlist
- agent read/write boundary
- human approval before external send, production change, deletion, permission change, customer-impacting action, or risk acceptance
- prompt/file upload restrictions
- audit logging
- cost limit
- rate limit
- egress restrictions
- retrieval-source allowlist

## Agent Permissions

Use this section for AI agents or tools that can take actions, call tools, access systems, or write data.

| ID | Agent / Tool | Identity Used | Read Access | Write Access | External Communication? | Production Access? | Approval Required For | Audit Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AI-001 |  |  |  |  | No | No |  |  |

## Cost and Value Tracking

| ID | Cost Owner | Pricing Model | Current Spend | Trend | Value Hypothesis | Evidence of Value | Duplication / Overlap | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AI-001 |  | Licence / Token / Usage / Fixed / Included |  | Stable / Rising / Falling / Unknown |  |  |  | Continue / Expand / Restrict / Consolidate / Retire |

## Risk, Exceptions, and Approvals

| ID | Risk / Exception | Rationale | Approved By | Approval Date | Review Date | Conditions | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AI-001 |  |  |  |  |  |  |  |

Use this for:

- restricted use approval
- temporary shadow-AI exception
- data exposure exception
- vendor/procurement exception
- agent permission exception
- production use before full evaluation
- residual risk acceptance

## Lifecycle and Retirement

| ID | Lifecycle State | Next Decision | Retirement Trigger | Replacement / Migration Plan | Data Retention / Deletion | Access Removal | Closure Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AI-001 | Proposed |  |  |  |  |  |  |

## Review Questions

At each review, ask:

- Is this AI capability still used?
- Does it still have an accountable owner?
- Is the approved use still accurate?
- Has the provider, model, feature, prompt, retrieval source, or permission set changed?
- Has data exposure changed?
- Are evaluation results still valid?
- Are incidents, complaints, failures, or near misses emerging?
- Is cost justified by value?
- Is there duplication with another approved tool?
- Should this be approved, restricted, consolidated, replaced, or retired?

## Escalation Rules

Escalate when:

- customer, employee, regulated, legal, security-sensitive, or strategic data exposure is unclear or unapproved
- an AI tool or agent can affect customers, production systems, money, access, legal obligations, HR decisions, or security posture
- a vendor AI feature changes data flow or model behaviour materially
- an unapproved tool becomes operationally important
- evaluation evidence is missing for a material use case
- monitoring or audit evidence is unavailable
- cost growth is material or unexplained
- ownership is unclear
- an incident or near miss occurs

## Related Guidance

- [AI Landscape Management](https://github.com/RusDavies/docs-management-practices/blob/master/disciplines/AI_LANDSCAPE_MANAGEMENT.md)
- [AI Use-Case Intake and Data Exposure Assessment](https://github.com/RusDavies/docs-management-practices/blob/master/templates/ai-use-case-intake-and-data-exposure-assessment.md)
- [AI Agent Permission Matrix](https://github.com/RusDavies/docs-management-practices/blob/master/templates/ai-agent-permission-matrix.md)
- [AI Prompt and Retrieval-Source Register](https://github.com/RusDavies/docs-management-practices/blob/master/templates/ai-prompt-and-retrieval-source-register.md)
- [AI Evaluation Report](https://github.com/RusDavies/docs-management-practices/blob/master/templates/ai-evaluation-report.md)
- [Architecture Management](https://github.com/RusDavies/docs-management-practices/blob/master/disciplines/ARCHITECTURE_MANAGEMENT.md)
- [Technical Debt Management](https://github.com/RusDavies/docs-management-practices/blob/master/disciplines/TECHNICAL_DEBT_MANAGEMENT.md)
- [Risk Management](https://github.com/RusDavies/docs-management-practices/blob/master/disciplines/RISK_MANAGEMENT.md)
- [Procurement Management](https://github.com/RusDavies/docs-management-practices/blob/master/disciplines/PROCUREMENT_MANAGEMENT.md)
- [Vendor and Partner Management](https://github.com/RusDavies/docs-management-practices/blob/master/disciplines/VENDOR_AND_PARTNER_MANAGEMENT.md)
- [Incident Response Management](https://github.com/RusDavies/docs-management-practices/blob/master/disciplines/INCIDENT_RESPONSE_MANAGEMENT.md)

## Usage Notes

- Maintain this as the source of truth for approved, experimental, restricted, shadow, and retired AI capabilities.
- Review entries with business, technical, security/privacy, vendor, and cost owners.
- Do not use the register as a substitute for actual controls; use it to route controls.
- Add shadow/unapproved AI tools when discovered instead of pretending discovery is endorsement.

## Example

An entry for an enterprise copilot might show owner, user population, provider, data classes exposed through prompts/files, retention/training posture, approval state, cost owner, review date, and retirement trigger.
