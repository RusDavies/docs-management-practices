# Incident Severity Model

## Purpose

Define severity levels before an incident begins, so impact, escalation, communication, and response cadence are driven by facts instead of whoever sounds most dramatic.

## Severity Levels

| Severity | Summary | Typical impact | Response expectation | Approval / escalation |
| --- | --- | --- | --- | --- |
| SEV-1 / Critical | Major active harm or severe exposure |  | Immediate command, continuous response, executive awareness |  |
| SEV-2 / High | Material customer, operational, security, legal, or business impact |  | Formal incident response and frequent updates |  |
| SEV-3 / Medium | Limited or contained impact requiring coordination |  | Assigned owner, documented actions, scheduled updates |  |
| SEV-4 / Low | Minor impact or near miss needing tracking |  | Normal ownership with light incident record if useful |  |
| Under assessment | Impact unclear |  | Initial triage and reassessment deadline |  |

## Impact Dimensions

| Dimension | Low | Medium | High | Critical |
| --- | --- | --- | --- | --- |
| Customer / user impact |  |  |  |  |
| People / safety impact |  |  |  |  |
| Security / privacy / data impact |  |  |  |  |
| Legal / regulatory exposure |  |  |  |  |
| Financial impact |  |  |  |  |
| Operational disruption |  |  |  |  |
| Reputation / public visibility |  |  |  |  |
| Duration / spread |  |  |  |  |

## Triage Rules

- Start with known impact and credible worst-case exposure.
- Use the highest material dimension as the starting severity.
- Raise severity when impact is spreading, facts are uncertain, or regulated/sensitive exposure is plausible.
- Lower severity only after evidence supports containment and reduced impact.
- Record severity changes in the incident timeline and decision log.

## Response Cadence

| Severity | Command | Internal updates | Customer / stakeholder updates | Review / closure expectation |
| --- | --- | --- | --- | --- |
| SEV-1 / Critical |  |  |  |  |
| SEV-2 / High |  |  |  |  |
| SEV-3 / Medium |  |  |  |  |
| SEV-4 / Low |  |  |  |  |

## Usage Notes

- Severity is a management tool, not a status symbol.
- Err toward declaration and adjustment when facts are unclear. Late incident declaration is how organizations turn uncertainty into archaeology.
- Pair with the incident declaration checklist, escalation matrix, incident role roster, and stakeholder update template.

## Example

A short internal tool outage may be SEV-3 if workarounds exist. The same outage affecting customer billing, data integrity, or contractual service levels may become SEV-2 or SEV-1.
