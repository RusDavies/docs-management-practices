# AI Use Register and Disclosure Posture

Use this guidance when AI tools, copilots, agents, or model-assisted workflows contribute to management guidance, drafting, review, summarization, research synthesis, quality checks, publication preparation, or repository maintenance.

The goal is not to staple a confession label onto every spellcheck-level assist. The goal is to keep meaningful AI use visible enough for accountability, source review, privacy review, publication decisions, and later correction.

## Scope

This posture covers AI assistance used for:

- drafting or rewriting management guidance
- summarizing notes, transcripts, sources, reviews, or decision discussions
- generating examples, templates, checklists, review questions, or test cases
- reviewing documents for consistency, style, coverage, bias, privacy, security, or publication readiness
- maintaining repository navigation, link checks, backlog items, or evidence packets
- preparing public, employment-facing, customer-facing, governance, compliance, or personal-brand material
- agentic work that reads files, edits files, runs checks, commits, opens pull requests, sends messages, or creates artifacts

It does not require logging trivial commodity assistance such as local spelling correction, grammar hints, formatting autocomplete, or search suggestions unless that assistance materially changes content, evidence, decisions, or publication posture.

## Classification

Classify AI use by materiality.

| Level | Description | Register required? | Disclosure decision required? |
| --- | --- | --- | --- |
| Incidental | Spellcheck, formatting suggestions, local autocomplete, non-substantive phrasing help | No | No |
| Drafting support | AI proposes wording, structure, examples, summaries, or checklists that a human reviews and edits | Yes for durable/public-facing docs; optional for low-risk internal notes | Context-dependent |
| Review support | AI checks coverage, style, links, consistency, bias, risk, security, or publication readiness | Yes when the review result affects a decision or release | Usually internal disclosure/evidence, public only if relevant |
| Evidence synthesis | AI summarizes sources, transcripts, findings, reviews, or decision records | Yes | Yes for publication-sensitive or decision-critical use |
| Agentic maintenance | AI reads/edits files, runs checks, updates TODOs, commits, pushes, sends messages, or creates artifacts | Yes | Usually internal disclosure/evidence |
| Decision support | AI output materially influences hiring, performance, promotion, discipline, accommodation, legal, compliance, financial, security, customer, or public-positioning decisions | Yes | Yes; human decision owner must be explicit |
| Prohibited / needs approval | AI would process confidential/private data, protected-class-sensitive content, legal/medical/HR-sensitive material, secrets, third-party restricted content, or externally publish/send material without approval | Do not proceed without approval | Approval and disclosure posture required |

## Register Rule

Create or update an AI use register entry when AI assistance is material enough that a later reviewer would reasonably ask:

- What tool or agent helped produce this?
- What did it do?
- What data, files, sources, or prompts did it use?
- What did a human review?
- Were claims, examples, quotes, facts, legal/compliance implications, and publication-sensitive material checked?
- Is disclosure needed for the intended audience?
- Who owns correction if the AI-assisted material is wrong?

Use [AI Use Register](templates/ai-use-register.md) for repository-level or project-level tracking.

## Disclosure Posture

Use disclosure where it improves trust, legal/compliance posture, customer/user understanding, publication integrity, or decision accountability.

Do not use disclosure as performative theatre. A vague "AI was used" label can be less useful than clear ownership, source notes, and review evidence.

### Usually No Disclosure Needed

Disclosure is usually unnecessary for:

- internal rough notes that are not decision records
- spelling, grammar, formatting, or style cleanup
- low-risk internal drafting where a human substantially reviews and owns the final wording
- mechanical repository maintenance such as link checks or navigation updates, unless the work is being audited

### Internal Evidence Recommended

Keep internal evidence when AI is used for:

- management guidance drafting or restructuring
- consistency, publication, or optics review
- source synthesis or summarization
- template generation
- navigation/backlog/repository maintenance by an agent
- security, privacy, compliance, HR, legal, customer, or public-facing review support

Internal evidence can live in the register, a review record, a commit message, a PR description, or a project-local evidence packet. Pick the smallest thing that will still make sense later.

### Public / Audience Disclosure Recommended

Consider visible disclosure when AI-assisted content is:

- published externally under a personal, company, product, educational, legal, compliance, or employment-facing brand
- presented as research, benchmark, factual analysis, market intelligence, customer guidance, policy, or governance material
- used in hiring, performance, promotion, discipline, accommodation, or other people-impacting decisions
- used for legal, medical, financial, security, safety, or regulated-domain content
- generated at substantial scale where readers may reasonably expect to know the production method
- not substantially human-edited or independently fact-checked
- derived from AI summaries of sources that readers cannot inspect

A useful disclosure says what AI helped with and what humans owned. Example:

> AI tools assisted with drafting structure and consistency review. Human reviewers selected the final content, checked factual claims, and approved publication.

For sensitive material, include the owner, review gate, source/evidence basis, and any limits. Do not disclose private prompts, confidential files, secrets, or privileged review details.

## Human Ownership

AI can assist with drafting and review. It does not own the conclusion.

A named human owner remains accountable for:

- final wording
- factual accuracy
- source attribution
- privacy and confidentiality handling
- legal/compliance review routing
- publication decision
- corrections or retractions
- people-impacting decisions

For this repository, AI-assisted changes should still pass the normal Git workflow, review gates, link/orphan checks, and publication decision gates where relevant.

## Privacy and Data Boundaries

Before using AI assistance, check:

- whether inputs contain confidential, private, privileged, regulated, HR-sensitive, health, legal, financial, security-sensitive, customer, or third-party restricted material
- whether the tool/provider is approved for that data class
- whether prompts, files, outputs, logs, or retrieval sources are retained or used for training
- whether public disclosure would reveal private context by accident
- whether generated examples could create stereotype, protected-trait, or persona-optics problems

When in doubt, reduce the data, anonymize carefully, use approved local/private tooling, or ask for approval. Do not solve uncertainty by pasting more context into the machine. That is how tiny convenience becomes a privacy piñata.

## Review Checklist

Before publishing, approving, or relying on material AI-assisted content:

- [ ] AI use has been classified by materiality.
- [ ] Register entry exists where required.
- [ ] Inputs and data classes were appropriate for the tool/provider.
- [ ] Factual claims were checked against sources.
- [ ] Quotes, citations, and paraphrases were checked for accuracy and permissions.
- [ ] Sensitive examples were reviewed for privacy, stereotype, and publication risk.
- [ ] People-impacting, legal, compliance, security, medical, financial, or public-brand material received the right human review.
- [ ] Disclosure decision was recorded.
- [ ] Correction owner/path is clear.

## Related Guidance

- [Repository Conventions](REPOSITORY_CONVENTIONS.md)
- [AI Tooling Evolution for Management Disciplines](AI_TOOLING_EVOLUTION.md)
- [AI Landscape Management](disciplines/AI_LANDSCAPE_MANAGEMENT.md)
- [Publication Decision Gates](PUBLICATION_DECISION_GATES.md)
- [Source and Permissions Register](SOURCE_AND_PERMISSIONS_REGISTER.md)
- [Review and Maintenance Checklist](REVIEW_AND_MAINTENANCE_CHECKLIST.md)
- [AI Use Register](templates/ai-use-register.md)
