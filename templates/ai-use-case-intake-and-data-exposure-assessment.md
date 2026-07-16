# AI Use-Case Intake and Data Exposure Assessment

## Purpose

Use this template before approving, experimenting with, buying, enabling, or building an AI use case.

The goal is to decide whether the use case is valuable, safe enough for context, routed through an approved tool/provider path, and governed by the right controls. It is not to create a ceremonial form that everyone fills in after the tool is already embedded in production and named after a woodland animal.

## Intake Summary

| Field | Value |
| --- | --- |
| Use-case name |  |
| Request ID |  |
| Requestor |  |
| Business owner |  |
| Technical owner |  |
| Security/privacy contact |  |
| Product/service/team |  |
| Date submitted |  |
| Target decision date |  |
| Lifecycle stage | Proposed / Experiment / Approved / Production / Restricted / Retiring |

## Use-Case Description

### Problem or Opportunity

What problem is this AI capability intended to solve?

### Intended Users

Who will use it?

- employees
- managers/leaders
- engineers/operators
- support/sales/customer-success teams
- customers/end users
- vendors/partners
- automated workflows/agents
- other:

### Intended Outcome

What should improve?

- speed
- quality
- consistency
- cost
- risk reduction
- customer experience
- employee experience
- decision support
- automation
- other:

### Out of Scope

What must this use case not do?

## AI Capability Classification

| Question | Answer |
| --- | --- |
| Capability type | Chat assistant / Copilot / Agent / Workflow automation / Classification / Summarization / Search/RAG / Recommendation / Analytics / Code generation / Embedded vendor feature / Other |
| Build/buy/enable path | Build / Buy / Enable existing vendor feature / Use approved internal tool / Experiment only |
| User-facing status | Internal only / Customer-facing / Partner-facing / Mixed |
| Decision impact | Advisory only / Human-reviewed / Automated decision / Automated action |
| Agentic action? | No / Yes, read-only / Yes, write-capable / Yes, external communication / Yes, production-impacting |

## Approved Path Check

Before proposing a new tool or provider, check whether an approved capability already exists.

| Check | Result | Notes |
| --- | --- | --- |
| Existing approved tool can satisfy use case? | Yes / No / Partially / Unknown |  |
| Existing vendor already provides this feature? | Yes / No / Unknown |  |
| Existing provider/model approved for this data class? | Yes / No / Unknown |  |
| Procurement review needed? | Yes / No / Unknown |  |
| Vendor/security/privacy review needed? | Yes / No / Unknown |  |
| Architecture review needed? | Yes / No / Unknown |  |

If the answer is "Unknown" for data, vendor, or architecture questions, treat the use case as not ready for approval. Unknown is not a risk rating. It is a small flag saying "please stop guessing with customer data."

## Data Exposure Assessment

### Data Classes In Scope

| Data class | Used? | Example data | Source system | Owner | Approval needed? | Approval status |
| --- | --- | --- | --- | --- | --- | --- |
| Public | No |  |  |  | No |  |
| Internal | No |  |  |  |  |  |
| Confidential | No |  |  |  |  |  |
| Customer-sensitive | No |  |  |  |  |  |
| Employee-sensitive | No |  |  |  |  |  |
| Regulated | No |  |  |  |  |  |
| Security-sensitive | No |  |  |  |  |  |
| Legally privileged | No |  |  |  |  |  |
| Trade-secret / strategic | No |  |  |  |  |  |
| Secrets / credentials | No |  |  |  | Normally prohibited |  |

### Prompt and File Upload Exposure

| Exposure path | Allowed? | Notes / Controls |
| --- | --- | --- |
| Free-text prompts | Yes / No / Restricted |  |
| File uploads | Yes / No / Restricted |  |
| Source code submission | Yes / No / Restricted |  |
| Customer records | Yes / No / Restricted |  |
| Contracts/legal docs | Yes / No / Restricted |  |
| HR/people data | Yes / No / Restricted |  |
| Security findings/vulnerabilities | Yes / No / Restricted |  |
| Production logs | Yes / No / Restricted |  |
| Secrets/credentials/tokens | No | Should be prohibited except under explicitly approved secure handling. |

### Data Handling Questions

| Question | Answer | Evidence / Notes |
| --- | --- | --- |
| Where will prompts and uploaded files be processed? |  |  |
| Where will prompts, files, outputs, logs, and traces be stored? |  |  |
| How long are prompts/files/outputs retained? |  |  |
| Can provider staff access submitted data? | Yes / No / Unknown |  |
| Is submitted data used for training? | No / Disabled / Yes / Unknown |  |
| Is tenant isolation documented? | Yes / No / Unknown |  |
| Are deletion/export rights documented? | Yes / No / Unknown |  |
| Are logs/audit trails available to us? | Yes / No / Unknown |  |
| Are data residency constraints relevant? | Yes / No / Unknown |  |

## Provider, Vendor, and Dependency Review

| Area | Status | Evidence / Notes |
| --- | --- | --- |
| Provider/vendor identified |  |  |
| Contract/procurement status | Not started / In review / Approved / Exception / Not required |  |
| Security review | Not started / In review / Approved / Exception / Not required |  |
| Privacy/legal review | Not started / In review / Approved / Exception / Not required |  |
| Architecture review | Not started / In review / Approved / Exception / Not required |  |
| Model/provider dependency risk reviewed | Yes / No / Unknown |  |
| Subprocessors reviewed | Yes / No / Unknown |  |
| Exit path identified | Yes / No / Unknown |  |
| Cost model understood | Yes / No / Unknown |  |

## Risk Classification

| Risk dimension | Low | Medium | High | Notes |
| --- | --- | --- | --- | --- |
| Data sensitivity |  |  |  |  |
| Customer impact |  |  |  |  |
| Employee impact |  |  |  |  |
| Legal/regulatory impact |  |  |  |  |
| Security impact |  |  |  |  |
| Operational dependency |  |  |  |  |
| Automation/action risk |  |  |  |  |
| Vendor/provider dependency |  |  |  |  |
| Cost exposure |  |  |  |  |
| Reputational risk |  |  |  |  |

Overall risk rating:

- Low
- Medium
- High
- Restricted / requires formal approval
- Prohibited for proposed data/use path

## Evaluation Plan

What evidence is needed before approval?

| Evaluation area | Required? | Method | Owner | Evidence |
| --- | --- | --- | --- | --- |
| Accuracy / quality | Yes / No |  |  |  |
| Retrieval quality | Yes / No / N/A |  |  |  |
| Hallucination/fabrication risk | Yes / No |  |  |  |
| Bias / representational harm | Yes / No / N/A |  |  |  |
| Privacy / data leakage | Yes / No |  |  |  |
| Security / prompt injection | Yes / No |  |  |  |
| Tool-use safety | Yes / No / N/A |  |  |  |
| Human review effectiveness | Yes / No |  |  |  |
| Cost per useful outcome | Yes / No |  |  |  |
| User acceptance | Yes / No |  |  |  |

Minimum acceptance criteria:

- 

Known failure modes:

- 

## Controls and Guardrails

| Control | Required? | Implementation | Owner | Evidence |
| --- | --- | --- | --- | --- |
| Approved tool/provider path | Yes |  |  |  |
| Access control | Yes / No |  |  |  |
| Data class restrictions | Yes / No |  |  |  |
| Prompt/file upload restrictions | Yes / No |  |  |  |
| Provider training disabled | Yes / No / N/A |  |  |  |
| Logging/audit | Yes / No |  |  |  |
| Monitoring | Yes / No |  |  |  |
| Human review | Yes / No |  |  |  |
| Human approval before action | Yes / No / N/A |  |  |  |
| Cost/rate limits | Yes / No |  |  |  |
| Incident response path | Yes / No |  |  |  |
| Retirement/exit plan | Yes / No |  |  |  |

## Decision Gates

### Intake Gate

| Requirement | Status | Evidence / Notes |
| --- | --- | --- |
| Purpose is clear |  |  |
| Owner is named |  |  |
| Data classes are identified |  |  |
| Approved path checked |  |  |
| Initial risk classification complete |  |  |
| Experiment boundaries defined |  |  |

### Experiment Gate

| Requirement | Status | Evidence / Notes |
| --- | --- | --- |
| Test data is safe |  |  |
| User group is limited |  |  |
| Evaluation criteria exist |  |  |
| Cost limit exists |  |  |
| Failure/escalation path exists |  |  |
| No production/customer impact without approval |  |  |

### Production Gate

| Requirement | Status | Evidence / Notes |
| --- | --- | --- |
| Data exposure approved |  |  |
| Security/privacy/legal/procurement reviews complete where needed |  |  |
| Evaluation evidence sufficient |  |  |
| Monitoring and audit evidence available |  |  |
| Incident path defined |  |  |
| Human approval gates defined |  |  |
| Lifecycle owner accepts responsibility |  |  |

## Approval Routing

| Approval Area | Required? | Approver / Forum | Status | Date | Conditions |
| --- | --- | --- | --- | --- | --- |
| Business owner | Yes |  |  |  |  |
| Technical owner | Yes / No |  |  |  |  |
| Security | Yes / No |  |  |  |  |
| Privacy / legal | Yes / No |  |  |  |  |
| Procurement / vendor management | Yes / No |  |  |  |  |
| Architecture | Yes / No |  |  |  |  |
| Product / customer owner | Yes / No |  |  |  |  |
| Operations / support | Yes / No |  |  |  |  |
| Executive / risk owner | Yes / No |  |  |  |  |

## Decision Record

Decision:

- Approved
- Approved with conditions
- Approved for experiment only
- Restricted
- Deferred pending evidence
- Rejected
- Prohibited for proposed data/use path

Rationale:

Conditions:

Review date:

Register entry created/updated?

- Yes
- No
- N/A

AI landscape register ID:

## Follow-Up Actions

| Action | Owner | Due Date | Evidence / Notes |
| --- | --- | --- | --- |
|  |  |  |  |

## Related Guidance

- [AI Landscape Management](https://github.com/RusDavies/docs-management-practices/blob/master/disciplines/AI_LANDSCAPE_MANAGEMENT.md)
- [AI Landscape Register](https://github.com/RusDavies/docs-management-practices/blob/master/templates/ai-landscape-register.md)
- [AI Agent Permission Matrix](https://github.com/RusDavies/docs-management-practices/blob/master/templates/ai-agent-permission-matrix.md)
- [AI Prompt and Retrieval-Source Register](https://github.com/RusDavies/docs-management-practices/blob/master/templates/ai-prompt-and-retrieval-source-register.md)
- [AI Evaluation Report](https://github.com/RusDavies/docs-management-practices/blob/master/templates/ai-evaluation-report.md)
- [Architecture Management](https://github.com/RusDavies/docs-management-practices/blob/master/disciplines/ARCHITECTURE_MANAGEMENT.md)
- [Risk Management](https://github.com/RusDavies/docs-management-practices/blob/master/disciplines/RISK_MANAGEMENT.md)
- [Procurement Management](https://github.com/RusDavies/docs-management-practices/blob/master/disciplines/PROCUREMENT_MANAGEMENT.md)
- [Vendor and Partner Management](https://github.com/RusDavies/docs-management-practices/blob/master/disciplines/VENDOR_AND_PARTNER_MANAGEMENT.md)
- [Incident Response Management](https://github.com/RusDavies/docs-management-practices/blob/master/disciplines/INCIDENT_RESPONSE_MANAGEMENT.md)

## Usage Notes

- Use this before experimentation, procurement, vendor-feature enablement, or production use.
- Route the use case through approved tools/providers when possible.
- Pay special attention to prompt/file-upload exposure, retention, training-on-data posture, and automated action.
- Use the output to decide whether an evaluation report, permission matrix, or architecture review is needed.

## Example

For an AI meeting-note summarizer, capture user group, data sensitivity, whether recordings/transcripts include customers or employees, provider retention terms, human review expectations, and approval routing before enabling it broadly.
