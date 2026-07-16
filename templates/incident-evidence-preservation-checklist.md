# Incident Evidence Preservation Checklist

## Purpose

Preserve useful evidence during incidents without spreading sensitive data into places where it does not belong.

## Evidence Context

- Incident title / ID:
- Evidence owner:
- Legal / security / privacy owner, if applicable:
- Preservation start time:
- Access restriction:
- Evidence repository / location:

## Evidence to Consider

| Evidence type | Needed? | Owner | Location | Preservation notes |
| --- | --- | --- | --- | --- |
| Monitoring graphs / alerts |  |  |  |  |
| Application logs |  |  |  |  |
| Infrastructure / platform logs |  |  |  |  |
| Security alerts / detections |  |  |  |  |
| Deployment / change records |  |  |  |  |
| Configuration snapshots |  |  |  |  |
| Support tickets / customer reports |  |  |  |  |
| Vendor tickets / notices |  |  |  |  |
| Chat / coordination transcript |  |  |  |  |
| Communications sent |  |  |  |  |
| Screenshots / exports |  |  |  |  |
| Access / identity records |  |  |  |  |
| Data samples or affected-record lists |  |  |  |  |

## Sensitive Handling

| Check | Status | Notes |
| --- | --- | --- |
| Personal, customer, credential, regulated, or privileged data identified |  |  |
| Broad channels avoided for sensitive evidence |  |  |
| Access restricted to appropriate responders |  |  |
| Legal hold or retention requirement assessed |  |  |
| Evidence integrity / chain of custody considered where needed |  |  |
| Redaction or minimization applied where appropriate |  |  |
| Destructive recovery actions reviewed before execution |  |  |

## Evidence Log

| Time | Evidence | Collected by | Source | Storage location | Access restriction |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Usage Notes

- Preserve enough to support recovery, learning, contractual duties, regulatory assessment, and later review.
- Do not turn every incident into a forensic museum. Preserve proportionately to severity, sensitivity, and legal/security relevance.
- Pair with the incident timeline/decision log, security/privacy/legal lead, and post-incident review template.

## Example

Before rotating credentials or rebuilding a compromised host, responders may preserve relevant logs, alerts, access records, configuration state, and timestamps in a restricted evidence location.
