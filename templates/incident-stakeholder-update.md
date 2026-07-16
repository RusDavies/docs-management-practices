# Incident Stakeholder Update

Use this template for incident updates to internal stakeholders, customers, executives, vendors, or public/status-page channels. Adapt the level of detail to the audience.

This template is informed by ITIL/ITSM communication discipline, SRE incident update cadence, and security/privacy response constraints. It is not a substitute for legal, privacy, regulatory, or customer-contract review when those apply.

## Update Metadata

- incident title:
- incident ID/reference:
- severity:
- update number:
- update time:
- prepared by:
- approved by, if required:
- audience:
- next update due:

## Short Version

Use for executives, status pages, or internal summaries.

> We are currently investigating/responding to [brief incident description].
>
> Current known impact: [who/what is affected].
>
> Current status: [investigating / identified / containing / recovering / monitoring / resolved].
>
> Next update: [time or condition].

## Full Update

### Current Status

- [ ] investigating
- [ ] impact identified
- [ ] containment in progress
- [ ] recovery in progress
- [ ] monitoring
- [ ] resolved/closed

Status summary:

> 

### Known Impact

Describe what is known. Do not inflate, minimize, or guess.

- affected users/customers/teams:
- affected services/processes:
- start time, if known:
- duration, if known:
- customer/user-visible symptoms:
- current workaround, if any:

Impact summary:

> 

### What We Are Doing

> 

Include only actions that are safe and useful for the audience to know.

Examples:

- investigating the cause
- containing the issue
- rolling back a change
- restoring service
- validating data integrity
- coordinating with a supplier
- reviewing security/privacy exposure
- monitoring for recurrence

### What We Know

> 

### What We Do Not Yet Know

> 

Naming uncertainty is better than inventing certainty. The second option ages badly and usually has witnesses.

### Required Action From Audience

- [ ] no action required
- [ ] use workaround below
- [ ] pause affected activity
- [ ] preserve evidence/logs/messages
- [ ] contact incident owner for affected cases
- [ ] other:

Instructions:

> 

### Next Update

Next update will be sent:

- at:
- or when:
- owner:

## Security, Privacy, Legal, or Sensitive Incident Guardrails

Use when exposure may involve sensitive data, regulated data, credentials, employment matters, safety, legal privilege, or active security investigation.

Before sending, confirm:

- [ ] no sensitive personal/customer/credential/security details are exposed unnecessarily
- [ ] uncertainty is clearly labelled
- [ ] legal/privacy/security owner has reviewed if required
- [ ] contractual or regulatory notification duties have been considered
- [ ] message does not speculate about root cause, attacker, blame, or liability
- [ ] message is consistent with prior updates or explains the change

## Audience-Specific Notes

### Internal Operational Update

Emphasize:

- current status
- operational impact
- owner and coordination channel
- next actions
- what teams should pause, preserve, or avoid

Draft:

> 

### Executive Update

Emphasize:

- business impact
- customer/user impact
- risk exposure
- decisions needed
- expected update cadence
- escalation blockers

Draft:

> 

### Customer/User Update

Emphasize:

- visible impact
- what the organization is doing
- workaround or user action
- next update time
- support/contact route

Avoid internal blame, unnecessary architecture detail, and speculative root cause.

Draft:

> 

### Vendor/Partner Update

Emphasize:

- required supplier action
- affected dependency
- urgency/severity
- evidence supplied
- escalation route
- contractual/support reference if applicable

Draft:

> 

### Public/Status Page Update

Emphasize:

- concise impact
- current status
- next update
- no sensitive details

Draft:

> 

## Final Resolution Update

Use only when closure criteria are met.

> The incident affecting [service/process/customer group] has been resolved as of [time].
>
> Impact summary: [brief summary].
>
> Current status: [service restored / monitoring complete / residual limitation].
>
> Follow-up: [post-incident review / corrective actions / customer follow-up], where appropriate.

Do not call something resolved if customers are still doing interpretive gymnastics around a workaround.

## Usage Notes

- Match detail to audience: executives need impact and decisions; responders need facts; customers need clear status and next update.
- Do not speculate, minimize, or overpromise.
- Keep a cadence even when the update is “still investigating.”
- Get legal/privacy/customer approval where required.

## Example

For a service degradation, send: current status, known customer impact, mitigation underway, workaround if any, next update time, and a plain statement of what is not yet known.
