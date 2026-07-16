# AI Prompt and Retrieval-Source Register

## Purpose

Use this register to track prompts, system instructions, retrieval sources, vector stores, embeddings, source owners, sensitivity, freshness, access boundaries, evaluation impact, and change-review triggers for AI systems.

Prompts and retrieval sources are part of the system. If they change, behaviour can change. Treating them as informal notes is how organizations end up explaining production incidents with "someone edited the prompt, probably." Inspiring, in the way a fire alarm is inspiring.

## Scope

AI system, tool, agent, workflow, product, or business area covered by this register:

## Register Owner

Person or forum accountable for keeping this register current:

## Review Cadence

How often the register is reviewed, and by whom:

## Related Records

| Record Type | Reference |
| --- | --- |
| AI landscape register ID |  |
| AI use-case intake / data exposure assessment |  |
| AI evaluation report |  |
| AI agent permission matrix |  |
| Architecture decision record |  |
| Risk / exception record |  |

## Prompt and Instruction Inventory

| ID | Name | Type | Purpose | Owner | Version | Lifecycle State | Sensitivity | Last Changed | Review Date |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PR-001 |  | System instruction / Developer instruction / User prompt template / Tool instruction / Retrieval instruction / Safety instruction / Output format instruction |  |  |  | Draft / Experiment / Approved / Production / Restricted / Retiring / Retired | Public / Internal / Confidential / Security-sensitive |  |  |

## Prompt / Instruction Detail

Use one section per prompt or instruction where detail is needed.

### Prompt ID: PR-001

| Field | Value |
| --- | --- |
| Name |  |
| Type |  |
| Owner |  |
| Current version |  |
| Storage location |  |
| Used by |  |
| Environment | Dev / Test / Staging / Production / Mixed |
| Lifecycle state | Draft / Experiment / Approved / Production / Restricted / Retiring / Retired |
| Approval status | Pending / Approved / Approved with conditions / Rejected / Retired |

Purpose:

Allowed use:

Prohibited use:

Known limitations:

Required output format:

Human review requirement:

## Prompt Version History

| Prompt ID | Version | Change Summary | Changed By | Date | Evaluation Required? | Approval Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| PR-001 | v1.0 |  |  |  | Yes / No |  |

## Retrieval Source Inventory

| Source ID | Source Name | Source Type | Purpose | Owner | System of Record? | Sensitivity | Freshness / Update Cadence | Access Boundary | Status | Review Date |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RS-001 |  | Documentation / Knowledge base / Database / Ticketing / Code repo / Contract repository / Logs / Search index / Vector store / Other |  |  | Yes / No | Public / Internal / Confidential / Regulated / Customer-sensitive / Employee-sensitive / Security-sensitive / Legal / Strategic |  |  |  | Proposed / Approved / Production / Restricted / Retiring / Retired |  |

## Retrieval Source Detail

### Source ID: RS-001

| Field | Value |
| --- | --- |
| Source name |  |
| Source type |  |
| Source owner |  |
| System of record? | Yes / No |
| Storage / connection location |  |
| Used by AI capability |  |
| Data sensitivity |  |
| Access control model |  |
| Update cadence |  |
| Last indexed / refreshed |  |
| Retention / deletion obligations |  |
| Approval status |  |

What the source should support:

What the source should not be used for:

Known stale/problem areas:

Restricted content handling:

## Vector Store and Embedding Inventory

| Vector Store ID | Name | Source IDs | Embedding Model | Owner | Hosting / Provider | Data Sensitivity | Refresh Cadence | Access Boundary | Review Date |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| VS-001 |  |  |  |  |  |  |  |  |  |

## Access Boundaries

| Prompt / Source / Vector ID | Who Can Use It? | Tool / Agent Access | Environment | Restrictions | Approval Evidence |
| --- | --- | --- | --- | --- | --- |
|  |  |  | Dev / Test / Staging / Production |  |  |

Examples of restrictions:

- internal-only use
- no customer data
- no employee-sensitive data
- no security vulnerability details
- no legal privileged material
- no production write actions
- approved agent only
- read-only retrieval
- human review before output use
- source attribution required

## Sensitivity and Data Exposure

| ID | Data Classes Present | Prompt/File Upload Exposure? | Retrieval Exposure? | Provider Retention / Training Risk | Controls |
| --- | --- | --- | --- | --- | --- |
|  | Public / Internal / Confidential / Regulated / Customer-sensitive / Employee-sensitive / Security-sensitive / Legal / Strategic | Yes / No / Restricted | Yes / No / Restricted |  |  |

## Freshness and Source Quality

| Source ID | Freshness Requirement | Current Freshness | Quality Concerns | Owner Action Required? | Notes |
| --- | --- | --- | --- | --- | --- |
| RS-001 |  |  |  | Yes / No |  |

Quality concerns may include:

- stale documentation
- conflicting sources
- missing ownership
- unclear source authority
- low-quality generated content
- unreviewed public content
- sensitive data accidentally indexed
- missing deletion propagation
- source attribution gaps

## Change Review Triggers

A prompt, instruction, retrieval source, vector store, or embedding change should trigger review when it affects:

- system/developer instructions
- safety/refusal behavior
- tool-use rules
- external communication rules
- production-impacting actions
- data classes available to the AI system
- retrieval source ownership or authority
- vector-store contents
- embedding model
- provider/model
- access permissions
- regulated/customer/employee/security-sensitive data exposure
- output format used by downstream automation
- evaluation baseline or acceptance criteria

## Change Log

| Change ID | Affected ID(s) | Change Type | Summary | Risk Level | Evaluation Required? | Approval Required? | Changed By | Date | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CH-001 |  | Prompt / Instruction / Source / Vector store / Embedding / Access / Model / Provider |  | Low / Medium / High | Yes / No | Yes / No |  |  |  |

## Evaluation and Retest Impact

| Change ID | Retest Required? | Evaluation Report ID | Acceptance Criteria Affected | Known Failure Mode Affected? | Approval Status |
| --- | --- | --- | --- | --- | --- |
| CH-001 | Yes / No |  |  | Yes / No | Pending / Approved / Rejected |

## Incident / Near-Miss Linkage

| Incident / Near Miss | Related Prompt / Source / Vector ID | Summary | Corrective Action | Evidence |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Retirement and Cleanup

| ID | Retirement Trigger | Replacement | Access Removed? | Source / Vector Data Deleted? | Register Updated? | Closure Evidence |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  | Yes / No | Yes / No / N/A | Yes / No |  |

## Review Questions

At each review, ask:

- Are prompts and system instructions still owned?
- Are production prompts versioned and approved?
- Have prompts changed since the last evaluation?
- Are retrieval sources still authoritative?
- Are retrieval sources fresh enough for the use case?
- Has sensitive data entered prompts, sources, logs, traces, or vector stores?
- Are access boundaries still correct?
- Has a model, provider, embedding, or vector-store change affected behaviour?
- Do changes require retesting?
- Are retired prompts/sources actually removed?

## Related Guidance

- [AI Landscape Management](https://github.com/RusDavies/docs-management-practices/blob/master/disciplines/AI_LANDSCAPE_MANAGEMENT.md)
- [AI Landscape Register](https://github.com/RusDavies/docs-management-practices/blob/master/templates/ai-landscape-register.md)
- [AI Use-Case Intake and Data Exposure Assessment](https://github.com/RusDavies/docs-management-practices/blob/master/templates/ai-use-case-intake-and-data-exposure-assessment.md)
- [AI Evaluation Report](https://github.com/RusDavies/docs-management-practices/blob/master/templates/ai-evaluation-report.md)
- [AI Agent Permission Matrix](https://github.com/RusDavies/docs-management-practices/blob/master/templates/ai-agent-permission-matrix.md)
- [Risk Register](https://github.com/RusDavies/docs-management-practices/blob/master/templates/risk-register.md)

## Usage Notes

- Use this when prompts, retrieval sources, vector stores, or system instructions affect production behaviour.
- Version prompts and retrieval sources like system components, not casual notes.
- Trigger review when source freshness, access boundaries, prompt wording, or evaluation results change.
- Link prompt/source changes to evaluation evidence where behaviour may shift.

## Example

For a RAG assistant, register the system prompt, retrieval instructions, vector store, source documentation owners, freshness cadence, sensitivity level, access boundary, last evaluation, and change triggers.
