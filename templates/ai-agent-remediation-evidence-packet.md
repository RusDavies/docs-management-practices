# AI-Agent Remediation Evidence Packet

## Purpose

Use this packet when an AI agent helps discover, analyze, patch, test, or document technical debt or security-defect remediation.

The goal is not to pretend the agent is magic. The goal is to preserve enough evidence that humans can review what the agent did, what changed, what was tested, what remains risky, and who approved it. Autocomplete with a tool belt still needs adult supervision.

## Packet Summary

| Field | Value |
| --- | --- |
| Evidence packet ID | AIRE-001 |
| Related debt/remediation ID |  |
| Related security exposure ID |  |
| Related AI agent permission matrix |  |
| Agent name / ID |  |
| Human operator |  |
| Business owner |  |
| Technical owner |  |
| Security/risk reviewer |  |
| Repository/system |  |
| Date range |  |
| Status | Draft / Under review / Approved / Rejected / Superseded |

## Agent Scope and Permissions

| Area | Scope / Notes |
| --- | --- |
| Agent role | Discovery / Reachability analysis / Risk classification / Patch proposal / Test generation / Evidence capture / Other |
| Read access |  |
| Write access | None / Draft only / Branch only / Approved paths / Other |
| External communication | None / Internal only / External with approval / Other |
| Production access | None / Read-only / Write-capable with approval / Other |
| Human approval gates |  |
| No-go zones |  |

## Prompt / Instruction Summary

Record the material prompts, instructions, or prompt-register references used:

| Prompt / Instruction | Version / Reference | Purpose | Notes |
| --- | --- | --- | --- |
|  |  |  |  |

## Discovery and Analysis Evidence

| Evidence Type | Summary | Link / Location | Reviewer |
| --- | --- | --- | --- |
| Defect/debt discovery |  |  |  |
| Reachability/exposure analysis |  |  |  |
| Exploitability/risk classification |  |  |  |
| Affected files/components |  |  |  |
| False positives / exclusions |  |  |  |
| Assumptions and unknowns |  |  |  |

## Remediation Proposal

Agent-proposed remediation summary:

Human-reviewed remediation decision:

Rejected alternatives:

Residual risk:

## Change Evidence

| Change | Files / Components | Agent Role | Human Role | Review Evidence |
| --- | --- | --- | --- | --- |
|  |  | Proposed / Generated / Edited / Reviewed / None | Approved / Edited / Rejected / Merged |  |

## Verification Evidence

| Check | Result | Evidence / Link | Notes |
| --- | --- | --- | --- |
| Unit tests | Pass / Fail / N/A |  |  |
| Integration tests | Pass / Fail / N/A |  |  |
| Security tests | Pass / Fail / N/A |  |  |
| Regression tests | Pass / Fail / N/A |  |  |
| Static analysis | Pass / Fail / N/A |  |  |
| Dependency scan | Pass / Fail / N/A |  |  |
| Manual review | Pass / Fail / N/A |  |  |
| Production/release verification | Pass / Fail / N/A |  |  |

## Human Approval

| Approval | Approver | Date | Evidence / Notes |
| --- | --- | --- | --- |
| Remediation approach |  |  |  |
| Code/change approval |  |  |  |
| Security/risk approval |  |  |  |
| Release/production approval |  |  |  |
| Residual risk acceptance |  |  |  |

## Audit Trail

Links to relevant records:

- agent run/session transcript:
- branch/commit/PR:
- test logs:
- scanner output:
- review comments:
- release/change record:
- rollback evidence:
- related decision/risk/debt records:

## Closure Statement

What was fixed or mitigated?

What evidence proves it?

What remains?

Who approved closure?

## Usage Notes

- Use this when AI-agent assistance is material to remediation, especially security, production, dependency, or high-risk technical debt work.
- Keep agent permissions and human approval gates visible.
- Do not accept agent-generated claims without tests, inspection, and reviewer judgment.
- Link this packet to the technical debt register, remediation plan, security exposure assessment, and agent permission matrix where applicable.

## Example

For an AI-assisted authorization fix, the packet should include the prompt/instructions used, reachability analysis, changed authorization checks, generated regression tests, security test results, human code-review approval, release gate approval, and residual-risk statement.
