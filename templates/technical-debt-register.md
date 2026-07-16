# Technical Debt Register

## Purpose

Use this register to track technical debt that has a known consequence, owner, decision path, and review cadence.

Do not use this as a dumping ground for every untidy line of code. A register full of vague complaints is not governance. It is an anxiety spreadsheet with columns.

## Scope

Product, platform, service, capability, team, or estate covered by this register:

## Register Owner

Person or forum accountable for keeping this register current:

## Review Cadence

How often this register is reviewed, and by whom:

## Debt Entries

| ID | Title | Debt Class | Affected Area | Owner | Status | Severity | Consequence | Decision | Review Date |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TD-001 |  | Architecture / Code / Dependency / Data / Security defect / Operational / Platform / Documentation / Vendor-tooling / Other |  |  | Proposed / Accepted / Planned / In remediation / Mitigated / Remediated / Retired | Low / Medium / High / Critical |  | Remediate / Mitigate / Accept / Defer / Replace / Retire |  |

## Debt Detail

Use one section per material debt item.

### Debt ID: TD-001

| Field | Value |
| --- | --- |
| Title |  |
| Debt class |  |
| Affected product/service/system |  |
| Owner |  |
| Accountable decision forum |  |
| Date identified |  |
| Status |  |
| Severity |  |
| Related risk ID |  |
| Related architecture/decision record |  |
| Related incident/finding/CVE/ticket |  |

### Current State

What exists now?

### Needed State

What state is needed for safe, reliable, maintainable, secure, cost-effective delivery?

### Consequence

What happens if this debt remains?

Consider:

- delivery drag
- operational burden
- security/privacy exposure
- customer/user impact
- cost
- resilience/recovery impact
- data quality/reporting impact
- vendor/platform lock-in
- compliance/audit impact

### Evidence

Links to evidence:

- code/design review:
- incident/post-review:
- scanner/finding:
- architecture decision:
- operational metric:
- support/customer evidence:
- other:

### Decision

Current decision:

- remediate
- mitigate
- accept
- defer
- replace
- retire
- investigate further

Rationale:

Decision owner:

Review trigger/date:

## Prioritization View

| ID | Impact | Urgency | Remediation Effort | Reversibility | Exposure Window | Priority | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TD-001 | Low / Medium / High / Critical | Low / Medium / High / Immediate | Low / Medium / High / Unknown | High / Medium / Low |  | P0 / P1 / P2 / P3 / Watch |  |

## Closure Evidence

When closing a debt item, capture:

- remediation/mitigation summary
- tests/checks passed
- reviewer/approver
- production/release evidence where relevant
- residual risk
- follow-up items

## Usage Notes

- Track only debt with a consequence and owner.
- Use debt classes from the technical debt management guide so items route to the right forum.
- Link accepted debt to a debt acceptance record or risk acceptance where the consequence is material.
- Review stale accepted/deferred debt; deferral without review is just neglect with nicer stationery.

## Example

A dependency debt entry might record an unsupported runtime version, affected services, security/support consequence, owner, planned migration window, exposure window, accepted interim mitigation, and the review date when deferral must be reconsidered.
