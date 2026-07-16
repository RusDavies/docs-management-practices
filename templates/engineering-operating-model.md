# Engineering Operating Model

## Purpose

Define how engineering work is organized, owned, prioritized, reviewed, delivered, operated, and improved. Use this as the management-layer companion to the software-product lifecycle in `docs-software-product-process`.

## Scope

- Organization / product / platform / team:
- Operating-model owner:
- Engineering leader:
- Product / business counterpart:
- Review cadence:
- Last reviewed:

## Team and Ownership Model

| Team / role | Mission | Owned systems / services / capabilities | Customers / users served | Out of scope | Escalation owner |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Work Intake and Lifecycle Alignment

| Work type | Intake path | Product-process hook | Review / approval needed | Done evidence | Owner |
| --- | --- | --- | --- | --- | --- |
| Product / feature work |  | Product framing, requirements, UX, architecture, QA, release |  |  |  |
| Architecture / platform work |  | Architecture guidance / ADR |  |  |  |
| Security / vulnerability work |  | Security guidance / release security gate |  |  |  |
| Operational / reliability work |  | Operations / observability guidance |  |  |  |
| Technical debt / refactoring |  | Technical debt and quality guidance |  |  |  |
| AI-agent operation / automation |  | Governance and AI-agent operation guidance |  |  |  |

## Decision Rights and Interfaces

| Decision area | Engineering owner | Partner input required | Approval / escalation trigger | Record location |
| --- | --- | --- | --- | --- |
| Technical design |  | Product / architecture / security / operations |  |  |
| Release readiness |  | Product / QA / security / support |  |  |
| Risk acceptance |  | Human risk owner / security / compliance |  |  |
| Build / buy / reuse |  | Product / procurement / security / finance |  |  |
| Operational ownership |  | Support / operations / platform |  |  |

## Engineering Health and Review Cadence

| Signal | Source | Review cadence | Threshold / concern | Owner |
| --- | --- | --- | --- | --- |
| Delivery flow |  |  |  |  |
| Quality / defect trend |  |  |  |  |
| Security / dependency exposure |  |  |  |  |
| Operational load / toil |  |  |  |  |
| Build / test reliability |  |  |  |  |
| Team health / capacity |  |  |  |  |

## Usage Notes

- Keep this at the management-system level; detailed product lifecycle gates belong in `docs-software-product-process`.
- Use the product-process hooks to avoid inventing duplicate release, security, QA, architecture, and operations gates.
- Review when team topology, ownership, product class, production exposure, or AI-agent operating boundaries change.

## Example

A SaaS product engineering group may define product-aligned teams, platform ownership, security-review triggers, release evidence expectations, product operational estate ownership, incident participation, and which product-process artifacts must exist before Class 4 releases.
