# Knowledge AI Retrieval-Source Register

## Purpose

Track which knowledge sources are eligible for AI retrieval, summarization, or agent use, including ownership, sensitivity, freshness, access boundaries, and evaluation requirements.

## Scope

- AI tool / assistant / retrieval system:
- Register owner:
- Review date:
- Applies to:

## Retrieval-Source Register

| Source / collection | Domain | Owner | Status | Sensitivity | Audience / access boundary | Freshness requirement | Chunking / metadata notes | Eligible? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  | yes / no / restricted |

## Exclusions

| Source | Reason excluded | Review trigger | Owner |
| --- | --- | --- | --- |
|  | stale / sensitive / conflicting / unapproved / low quality / legal hold / other |  |  |

## Retrieval Controls

- Access-control enforcement model:
- Citation requirement:
- Confidence / uncertainty behaviour:
- Human approval requirements:
- Logging / audit requirements:
- Sensitive data handling:
- Deprecated-source handling:
- Fallback when no trusted source exists:

## Evaluation

| Evaluation area | Test / evidence | Owner | Frequency | Result / link |
| --- | --- | --- | --- | --- |
| Source freshness |  |  |  |  |
| Citation quality |  |  |  |  |
| Access-boundary enforcement |  |  |  |  |
| Prompt-injection / retrieval poisoning |  |  |  |  |
| Answer quality for known questions |  |  |  |  |
| Deprecated-source exclusion |  |  |  |  |

## Change Review

| Change | Risk | Approval needed | Owner | Date | Evidence |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Usage Notes

- Use before connecting copilots or agents to organizational knowledge.
- Do not make stale, conflicting, permission-blind, or unapproved content retrieval-eligible because the demo needs answers. Demos are charming little liability engines.
- Pair with the source-of-truth register, content lifecycle policy, and stale-content review list.

## Example

Approved product documentation may be retrieval-eligible for customer-support drafting, while internal incident notes are restricted to authorized operations users and excluded from customer-facing answer generation.
