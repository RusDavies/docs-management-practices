# AI Evaluation Report

## Purpose

Use this report to document whether an AI use case, model, agent, retrieval system, vendor feature, or workflow is good enough for its intended context.

The report should produce decision evidence, not vibes with a chart. If the conclusion is "approved," a reasonable reviewer should be able to see what was tested, what passed, what failed, what risk remains, and who accepted it.

## Evaluation Summary

| Field | Value |
| --- | --- |
| Evaluation ID |  |
| AI use-case / system name |  |
| AI landscape register ID |  |
| Intake / assessment reference |  |
| Prompt / retrieval-source register reference |  |
| Evaluated capability type | Model / Agent / Copilot / RAG / Workflow / Vendor feature / Other |
| Business owner |  |
| Technical owner |  |
| Evaluator(s) |  |
| Evaluation date |  |
| Target decision date |  |
| Lifecycle stage | Proposed / Experiment / Approved / Production / Restricted / Retiring |
| Decision requested | Approve / Approve with conditions / Restrict / Reject / Retest / Retire |

## Scope

### Intended Use

What is the AI capability expected to do?

### Intended Users

Who will use it?

### Data and System Boundaries

What data, systems, tools, repositories, vendors, or environments were in scope?

### Out of Scope

What was not tested?

Be explicit. Untested does not mean safe. It means untested. Stunning concept, yet somehow still controversial.

## Acceptance Criteria

Define pass/fail criteria before interpreting results.

| Criterion | Threshold / Expected Result | Required? | Result | Evidence |
| --- | --- | --- | --- | --- |
| Functional correctness |  | Yes / No | Pass / Fail / Partial / Not tested |  |
| Accuracy / quality |  | Yes / No |  |  |
| Retrieval quality |  | Yes / No / N/A |  |  |
| Hallucination/fabrication control |  | Yes / No |  |  |
| Safety / refusal behavior |  | Yes / No |  |  |
| Privacy / data leakage |  | Yes / No |  |  |
| Security / prompt injection resistance |  | Yes / No |  |  |
| Tool-use safety |  | Yes / No / N/A |  |  |
| Human review effectiveness |  | Yes / No |  |  |
| Bias / representational harm |  | Yes / No / N/A |  |  |
| Performance / latency |  | Yes / No |  |  |
| Cost per useful outcome |  | Yes / No |  |  |
| Monitoring/audit evidence |  | Yes / No |  |  |

## Test Set and Baseline

| Test Set / Dataset | Purpose | Source | Size | Data Sensitivity | Approved for Use? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Public / Internal / Confidential / Regulated / Customer-sensitive / Employee-sensitive / Security-sensitive | Yes / No |  |

Baseline or comparison method:

- previous manual process
- previous model/provider
- non-AI workflow
- rules-based system
- expert review
- golden answer set
- synthetic test set
- red-team/adversarial cases
- other:

## Evaluation Method

Describe how the evaluation was run.

| Area | Method | Tools / Commands | Evidence Location |
| --- | --- | --- | --- |
| Accuracy / quality |  |  |  |
| Retrieval quality |  |  |  |
| Hallucination/fabrication |  |  |  |
| Privacy / leakage |  |  |  |
| Security / prompt injection |  |  |  |
| Tool-use safety |  |  |  |
| Human review |  |  |  |
| Cost / performance |  |  |  |

## Results Summary

| Area | Result | Evidence | Decision Impact |
| --- | --- | --- | --- |
| Accuracy / quality | Pass / Fail / Partial / Not tested |  |  |
| Retrieval quality | Pass / Fail / Partial / N/A |  |  |
| Hallucination/fabrication | Pass / Fail / Partial / Not tested |  |  |
| Privacy / leakage | Pass / Fail / Partial / Not tested |  |  |
| Security / prompt injection | Pass / Fail / Partial / Not tested |  |  |
| Tool-use safety | Pass / Fail / Partial / N/A |  |  |
| Bias / representational harm | Pass / Fail / Partial / N/A |  |  |
| Human review | Pass / Fail / Partial / Not tested |  |  |
| Cost / performance | Pass / Fail / Partial / Not tested |  |  |
| Monitoring / audit | Pass / Fail / Partial / Not tested |  |  |

Overall result:

- Pass
- Pass with conditions
- Partial / restricted use only
- Fail / do not approve
- Inconclusive / more evidence required

## Accuracy and Quality Results

Summarize correctness, usefulness, and quality.

| Metric / Observation | Result | Threshold | Notes |
| --- | --- | --- | --- |
|  |  |  |  |

Examples to capture:

- answer correctness
- task completion rate
- reviewer acceptance rate
- false positives
- false negatives
- unsupported claims
- formatting or workflow errors
- output consistency
- domain-specific quality failures

## Retrieval Quality

Use this section for RAG, knowledge assistants, search, or tools that depend on retrieval.

| Test | Result | Evidence / Notes |
| --- | --- | --- |
| Relevant sources retrieved |  |  |
| Irrelevant sources suppressed |  |  |
| Source attribution present |  |  |
| Stale sources identified |  |  |
| Restricted sources excluded |  |  |
| Answer grounded in retrieved evidence |  |  |
| Retrieval failure behavior acceptable |  |  |

## Hallucination and Fabrication Risk

| Scenario | Expected Behavior | Observed Behavior | Pass? | Notes |
| --- | --- | --- | --- | --- |
| Missing information | Say unknown / ask for more context |  |  |  |
| Ambiguous prompt | Ask clarifying question / state assumptions |  |  |  |
| Conflicting sources | Identify conflict / avoid false certainty |  |  |  |
| Unsupported claim request | Refuse or qualify appropriately |  |  |  |
| Citation/source request | Provide accurate source or state unavailable |  |  |  |

## Privacy and Data Leakage Checks

| Check | Result | Evidence / Notes |
| --- | --- | --- |
| Test data approved for evaluation |  |  |
| Sensitive data excluded or controlled |  |  |
| Prompt/file upload exposure reviewed |  |  |
| Provider retention/training posture confirmed |  |  |
| Logs/traces reviewed for sensitive data |  |  |
| Output does not leak restricted data |  |  |
| Tenant/customer/user isolation preserved |  |  |
| Deletion/retention obligations understood |  |  |

## Security and Prompt-Injection Checks

| Check | Result | Evidence / Notes |
| --- | --- | --- |
| Prompt-injection attempts handled safely |  |  |
| System/developer instructions not exposed |  |  |
| Retrieval-source injection considered |  |  |
| Tool call abuse prevented |  |  |
| Unauthorized data access blocked |  |  |
| External URL/content handling safe |  |  |
| Secrets/credentials not exposed |  |  |
| Security findings handled without weaponized detail where required |  |  |

## Tool-Use and Agent Safety

Use this section when the evaluated capability can call tools, write data, send messages, deploy, delete, or affect systems.

| Check | Result | Evidence / Notes |
| --- | --- | --- |
| Agent permission matrix reviewed |  |  |
| Read/write boundaries enforced |  |  |
| Human approval gates tested |  |  |
| Destructive actions blocked or approval-gated |  |  |
| External communication blocked or approval-gated |  |  |
| Production-impacting actions blocked or approval-gated |  |  |
| Audit trail captures actions |  |  |
| Rollback/kill switch tested |  |  |

## Bias, Fairness, and Representational Harm

Use where the AI capability affects people, content, prioritization, access, employment, customer treatment, or reputation.

| Check | Result | Evidence / Notes |
| --- | --- | --- |
| Affected groups identified |  |  |
| Test examples reviewed for skew/stereotype patterns |  |  |
| Negative examples do not disproportionately assign failure to protected or culturally diverse personas |  |  |
| Human review exists for consequential outputs |  |  |
| Escalation path exists for harmful output |  |  |

## Human Review Effectiveness

If human review is part of the control model, test whether it actually works.

| Question | Answer | Evidence / Notes |
| --- | --- | --- |
| Who reviews outputs? |  |  |
| What are they expected to catch? |  |  |
| Do reviewers have enough context? |  |  |
| Is review mandatory or optional? |  |  |
| Can review be bypassed? |  |  |
| Were intentionally flawed outputs detected? |  |  |
| Is reviewer workload sustainable? |  |  |

Human review is not a magic spell. If reviewers lack time, skill, context, or authority, the control is theatre with chairs.

## Cost and Performance

| Metric | Result | Threshold / Budget | Notes |
| --- | --- | --- | --- |
| Average latency |  |  |  |
| Peak latency |  |  |  |
| Cost per request/task |  |  |  |
| Monthly cost estimate |  |  |  |
| Failure/retry cost |  |  |  |
| Human review cost |  |  |  |
| Operational support cost |  |  |  |

## Known Failure Modes

| Failure Mode | Trigger | Impact | Detection | Mitigation | Owner |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Residual Risk

| Residual Risk | Rationale | Owner | Accepted By | Review Date |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Approval Recommendation

Recommendation:

- Approve
- Approve with conditions
- Restrict to limited users/data/use
- Experiment only
- Retest required
- Reject
- Retire/decommission

Rationale:

Conditions:

Required monitoring:

Required follow-up:

## Approval Evidence

| Approval Area | Required? | Approver / Forum | Status | Evidence / Notes |
| --- | --- | --- | --- | --- |
| Business owner | Yes |  |  |  |
| Technical owner | Yes / No |  |  |  |
| Security | Yes / No |  |  |  |
| Privacy / legal | Yes / No |  |  |  |
| Procurement / vendor management | Yes / No |  |  |  |
| Architecture | Yes / No |  |  |  |
| Product / customer owner | Yes / No |  |  |  |
| Operations / support | Yes / No |  |  |  |
| Risk owner | Yes / No |  |  |  |

## Monitoring and Retest Plan

| Trigger | Retest / Review Required? | Owner | Notes |
| --- | --- | --- | --- |
| Model/provider changes | Yes |  |  |
| Prompt/system instruction changes | Yes / No |  |  |
| Retrieval-source changes | Yes / No / N/A |  |  |
| Agent tool/permission changes | Yes / No / N/A |  |  |
| New data class introduced | Yes |  |  |
| User group changes | Yes / No |  |  |
| Incident/near miss | Yes |  |  |
| Cost materially changes | Yes / No |  |  |
| Scheduled review | Yes |  |  |

## Follow-Up Actions

| Action | Owner | Due Date | Evidence / Notes |
| --- | --- | --- | --- |
|  |  |  |  |

## Related Guidance

- [AI Landscape Management](https://github.com/RusDavies/docs-management-practices/blob/master/disciplines/AI_LANDSCAPE_MANAGEMENT.md)
- [AI Use-Case Intake and Data Exposure Assessment](https://github.com/RusDavies/docs-management-practices/blob/master/templates/ai-use-case-intake-and-data-exposure-assessment.md)
- [AI Landscape Register](https://github.com/RusDavies/docs-management-practices/blob/master/templates/ai-landscape-register.md)
- [AI Agent Permission Matrix](https://github.com/RusDavies/docs-management-practices/blob/master/templates/ai-agent-permission-matrix.md)
- [AI Prompt and Retrieval-Source Register](https://github.com/RusDavies/docs-management-practices/blob/master/templates/ai-prompt-and-retrieval-source-register.md)
- [Risk Register](https://github.com/RusDavies/docs-management-practices/blob/master/templates/risk-register.md)
- [Incident Response Management](https://github.com/RusDavies/docs-management-practices/blob/master/disciplines/INCIDENT_RESPONSE_MANAGEMENT.md)

## Usage Notes

- Define acceptance criteria before looking at results.
- Keep failed tests and known limitations visible; they are decision evidence.
- Use the report for approval, restriction, retest, or retirement decisions.
- Re-run evaluation after material model, prompt, retrieval-source, permission, data, or workflow changes.

## Example

For a customer-support summarization tool, test against real-but-sanitized ticket examples, compare against human summaries, measure factual omissions, check privacy leakage, estimate cost per useful summary, and record whether human review remains required.
