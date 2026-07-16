# AI Landscape Management

## Purpose

AI landscape management is the discipline of identifying, governing, operating, evaluating, monitoring, funding, securing, and retiring the AI systems, tools, agents, models, providers, workflows, and data flows used across an organization.

It exists because AI rarely enters an organization through one tidy programme with a neat steering committee and a commemorative lanyard. It arrives through vendor features, developer tools, copilots, chatbots, analytics platforms, workflow automation, prototypes, browser extensions, SaaS add-ons, personal subscriptions, internal experiments, and enthusiastic people trying to save time.

The risk is not only in board approvals or policy documents. It is in everyday work:

- a prompt typed into a tool
- a file uploaded because it was convenient
- a vendor feature enabled by default
- a model embedded inside a workflow nobody has mapped
- an agent granted access because it seemed harmless
- a shortcut taken because the safe path was slower

Governance alone does not change behaviour. AI landscape management makes safe, approved, observable paths easier to use than unsafe, invisible ones.

## What Counts as AI in the Landscape

Do not restrict the landscape to internally built models. That misses most of the estate.

Include:

- internal AI applications
- externally hosted models and APIs
- enterprise copilots
- AI coding assistants
- workflow agents
- autonomous or semi-autonomous agents
- retrieval-augmented generation systems
- AI features embedded in SaaS tools
- AI analytics, summarization, search, classification, and recommendation tools
- customer-facing chatbots or assistants
- employee-facing chatbots or knowledge assistants
- AI-enabled security, operations, HR, finance, legal, sales, and support tooling
- model evaluation, monitoring, and observability tooling
- datasets, vector stores, prompts, system instructions, fine-tunes, embeddings, and agent tool permissions
- shadow AI tools used outside approved channels

If a tool can transform, infer from, summarize, classify, generate, decide, recommend, act, or automate using machine learning or generative AI, assume it belongs in the landscape until proven otherwise.

## Core Responsibilities

AI landscape management is responsible for:

- maintaining a register of AI systems, tools, agents, models, providers, and embedded AI features
- assigning owners and accountable decision forums
- classifying data exposure and acceptable use
- defining approved, restricted, and prohibited AI use cases
- creating practical operating rules for everyday work
- ensuring AI tools are procured, configured, monitored, and retired deliberately
- governing model, provider, vendor, and dependency risk
- managing prompts, retrieval sources, vector stores, tool permissions, and agent actions
- connecting AI usage to architecture, security, privacy, procurement, vendor, risk, product, operations, and incident-response processes
- measuring value, cost, adoption, failure modes, and duplication
- reducing shadow AI by making approved paths usable
- ensuring human approval gates exist where AI output or action creates material risk

The goal is not to ban useful tools because a policy PDF developed anxiety. The goal is to make AI use visible, governed, safe enough for context, and worth the risk taken.

## Four Layers of Control

Effective AI control needs four layers.

### 1. Governance

Governance answers:

- Who owns AI risk?
- Who approves use cases?
- What uses are acceptable, restricted, or prohibited?
- What risk thresholds require escalation?
- What evidence is needed before production use?
- Who can accept residual risk?

Governance should produce decision rights, standards, review forums, and accountability. It should not pretend that a policy alone controls behaviour.

### 2. Operating Model

The operating model answers:

- How are teams expected to use AI day to day?
- Where do people request approved tools?
- Who supports tool selection, configuration, and evaluation?
- How are prompts, retrieval sources, model choices, and tool permissions managed?
- How are exceptions handled?
- How do product, engineering, security, privacy, procurement, legal, and operations collaborate?

The operating model turns governance into work people can actually do.

### 3. Process

Process answers:

- Where are checks, reviews, and escalation points embedded?
- How is data exposure assessed before use?
- How are vendors reviewed?
- How are AI features tested before launch?
- How are incidents handled?
- How are costs reviewed?
- How are tools retired?

Good process catches risk at useful moments. Bad process appears after launch and asks everyone to remember who approved the thing six months ago. Very forensic. Not very helpful.

### 4. System Guardrails

System guardrails answer:

- What does the technology allow or block by default?
- Which tools are approved and available?
- Which data types cannot be uploaded?
- Which domains, APIs, repositories, or systems can agents access?
- What logging, monitoring, retention, and audit controls exist?
- What dependency, vendor, identity, and access controls enforce the policy?

People follow paths of least resistance. If the safe path is harder than the unsafe path, the unsafe path will win unless the organization is staffed entirely by saints and auditors. It is not.

## AI Landscape Register

The organization should maintain an AI landscape register. It does not need to be ornate. It needs to be current enough to support decisions.

Record at minimum:

- name
- owner
- business purpose
- user group
- internal/external/customer-facing status
- system/tool/agent/model/vendor classification
- provider and hosting model
- data types used
- data sensitivity
- prompt/file-upload exposure
- retrieval sources and vector stores
- model or provider dependencies
- agent tool permissions and action scope
- approval status
- evaluation status
- monitoring and logging posture
- cost owner and cost trend
- lifecycle state: proposed / experiment / approved / production / restricted / retiring / retired
- review date
- retirement or replacement plan

The register is not the control. It is the map. A bad map still lets everyone walk into the swamp, but at least afterward they can claim cartographic ambition.

## Ownership and Lifecycle

Every AI system or tool should have an owner. Ownership means someone is accountable for:

- purpose
- acceptable use
- data exposure
- configuration
- access
- evaluation
- monitoring
- cost
- incidents
- vendor/provider relationship
- lifecycle decisions

Lifecycle states should be explicit.

### Proposed

The use case is being considered. The main questions are value, risk, data exposure, and whether an approved tool already exists.

### Experiment

The use case is being tested with controlled data, limited users, and clear exit criteria. Experiments should not quietly become production because nobody wanted another meeting.

### Approved

The tool or use case is approved for defined users, data types, and purposes.

### Production

The AI capability affects real work, customers, operations, decisions, or workflows. Monitoring, support, incident response, and ownership must be real.

### Restricted

The tool or use case may be allowed only under special controls: limited data, limited users, legal review, security approval, or human approval gates.

### Retiring

The organization has decided to remove, replace, or consolidate it.

### Retired

Access is removed, data retention is handled, vendor obligations are closed, documentation is updated, and the register is closed.

## Data Exposure and Everyday Work Risk

AI risk often starts with ordinary behaviour.

Examples:

- uploading a customer contract to a public chatbot
- pasting source code into an unapproved coding assistant
- asking a model to summarize HR notes containing sensitive employee information
- connecting an agent to a repository without limiting branch or write access
- enabling a SaaS AI feature without checking data retention
- sending confidential strategy documents to a vendor model through a browser extension

Classify data before use:

- public
- internal
- confidential
- regulated
- customer-sensitive
- employee-sensitive
- security-sensitive
- legally privileged
- trade-secret or strategic

For each AI tool or use case, define:

- what data may be used
- what data may not be used
- whether files can be uploaded
- whether prompts and outputs are retained by the provider
- whether training on submitted data is disabled
- where logs are stored
- who can access outputs
- whether human review is required before use

The useful question is not "Is AI allowed?" It is "Allowed for what data, by whom, through which tool, under what controls?"

## Approved, Restricted, and Prohibited Use

Create clear use categories.

### Approved

Approved uses are available through standard tooling and documented guidance.

Examples:

- summarizing internal public documentation with an approved enterprise tool
- drafting low-risk internal text
- coding assistance in approved repositories under configured data protections
- support-answer drafting with human review and approved knowledge sources

### Restricted

Restricted uses require extra approval, controls, or review.

Examples:

- regulated data
- customer-impacting recommendations
- security analysis touching sensitive vulnerabilities
- HR, legal, medical, financial, or employment decisions
- agents with write access
- automated actions affecting customers, money, access, legal obligations, or production systems

### Prohibited

Prohibited uses should be blocked where possible.

Examples:

- uploading secrets, credentials, privileged legal material, or sensitive personal data to unapproved tools
- using AI to make final employment, credit, medical, legal, or similarly consequential decisions without authorized process
- connecting unapproved agents to production systems
- bypassing procurement, security, or privacy review through personal accounts
- using AI outputs as verified facts without validation where accuracy matters

Do not make every rule a moral lecture. Make the allowed path clear enough that people do not need a séance to find it.

## AI Agents and Tool Permissions

Agents are different from passive chat tools because they can act.

For agents, manage:

- identity and authentication
- allowed tools
- read/write boundaries
- environment boundaries
- approval gates
- rate limits and cost limits
- audit logging
- rollback paths
- human supervision
- prompt and instruction provenance
- memory and state retention
- external communication permissions
- production access restrictions

Agent actions that should normally require human approval include:

- production changes
- deletion or destructive actions
- sending external messages
- publishing content
- changing access or permissions
- modifying security, privacy, legal, financial, HR, or customer-impacting settings
- accepting risk
- bypassing normal dependency/procurement controls

Agents should accelerate work, not become a creative way to route accountability into a log file.

## Evaluation and Monitoring

AI systems need evaluation before and after use.

Evaluate:

- accuracy
- relevance
- hallucination/fabrication risk
- bias and representational harm where applicable
- privacy and data leakage
- security behaviour
- prompt-injection resistance
- tool-use safety
- retrieval quality
- refusal and escalation behaviour
- cost per useful outcome
- user experience
- operational reliability

Monitoring should include:

- usage volume
- user groups
- costs
- failure reports
- incident signals
- data exposure events
- model/provider changes
- retrieval-source changes
- agent action logs
- approval-gate bypass attempts
- customer or employee complaints

Evaluation is not one heroic test before launch. Models, providers, prompts, data, users, and workflows change. The landscape moves. Pretending otherwise is how brittle controls become archaeological exhibits.

## Cost, Duplication, and Value

AI tools can create silent cost sprawl.

Manage:

- duplicate tools solving the same problem
- unused licences
- runaway token/API costs
- multiple teams buying overlapping vendor features
- experiments that never close
- custom builds where a governed standard tool would work
- standard tools forced into use cases they cannot safely support

Review value as well as cost:

- What work is faster or better?
- What risk is reduced?
- What new risk is introduced?
- What human review remains necessary?
- What capability is strategically important?
- What should be consolidated, expanded, restricted, or retired?

Cheap AI that creates expensive rework is not cheap. It is just invoiced creatively.

## Vendor and Provider Management

AI vendors and providers should be reviewed through procurement, vendor management, security, privacy, legal, and architecture as appropriate.

Review:

- data retention
- training-on-customer-data defaults
- subprocessors
- hosting regions
- security certifications and evidence
- breach notification
- model/provider change controls
- audit logging
- tenant isolation
- access controls
- deletion and export rights
- pricing model
- service-level expectations
- lock-in and exit path
- support model
- acceptable-use restrictions

AI features embedded in existing SaaS tools still need review. "We already have the vendor" is not the same as "this new data flow and model behaviour are approved." Tiny distinction. Huge consequences.

## Architecture and Integration

AI landscape management should connect to architecture management.

Architecture questions:

- Is this AI capability part of a product, platform, workflow, or vendor tool?
- Where are the trust boundaries?
- What data crosses them?
- Which systems does the AI tool read from or write to?
- What happens when the model/provider is unavailable?
- What happens when output is wrong?
- What human approval gates exist?
- How is retrieval controlled?
- How are prompts, model versions, and evaluation results versioned?
- How does the capability retire?

AI architecture is not just model selection. It is data movement, identity, permissions, evidence, operations, and failure modes.

## Technical Debt and Security Exposure

AI creates and inherits technical debt.

Examples:

- unowned prototypes in production
- prompts nobody versioned
- vector stores with stale or sensitive content
- agents with overbroad permissions
- undocumented vendor AI features
- duplicated tools
- missing evaluation baselines
- dependency exposure in AI tooling
- security defects found but not remediated
- manual review steps that everyone assumes someone else performs

Security defects in AI tools, dependencies, or workflows should be handled through technical debt and security-defect remediation processes. AI agents can help analyze, patch, test, and capture evidence, but approval remains human where risk is material.

## Incident Response

AI incidents should be routed through incident response when they create material operational, customer, privacy, security, legal, financial, or reputational impact.

Examples:

- sensitive data submitted to an unapproved tool
- model output sent to customers without required review
- agent performs unauthorized action
- prompt injection causes data leakage or tool misuse
- vendor AI feature changes behaviour unexpectedly
- hallucinated information causes customer harm
- AI-generated code introduces exploitable defect
- cost runaway affects budget materially

Incident preparation should define:

- who can declare an AI incident
- how to preserve prompts, outputs, logs, tool actions, and data-flow evidence
- when to involve security, privacy, legal, product, operations, vendor management, and communications
- how to stop or contain an AI system or agent
- how affected users/customers are assessed
- how corrective actions are tracked

## Common Artifacts

Useful artifacts include:

- [AI landscape register](https://github.com/RusDavies/docs-management-practices/blob/master/templates/ai-landscape-register.md)
- approved AI tool list
- restricted/prohibited use guide
- [AI use-case intake and data exposure assessment](https://github.com/RusDavies/docs-management-practices/blob/master/templates/ai-use-case-intake-and-data-exposure-assessment.md)
- [AI use register and disclosure posture](https://github.com/RusDavies/docs-management-practices/blob/master/AI_USE_REGISTER_AND_DISCLOSURE.md)
- [AI use register](https://github.com/RusDavies/docs-management-practices/blob/master/templates/ai-use-register.md)
- model/provider/vendor review record
- AI architecture decision record
- [AI agent permission matrix](https://github.com/RusDavies/docs-management-practices/blob/master/templates/ai-agent-permission-matrix.md)
- [AI prompt and retrieval-source register](https://github.com/RusDavies/docs-management-practices/blob/master/templates/ai-prompt-and-retrieval-source-register.md)
- [AI evaluation report](https://github.com/RusDavies/docs-management-practices/blob/master/templates/ai-evaluation-report.md)
- AI monitoring dashboard
- AI incident evidence packet
- AI retirement checklist

Artifacts should support decisions. If nobody reads the register until audit season, it is not governance. It is seasonal paperwork migration.

## How the AI Artifacts Fit Together

Use the artifacts as a workflow, not as independent paperwork islands.

1. **Intake first** — use the [AI use-case intake and data exposure assessment](https://github.com/RusDavies/docs-management-practices/blob/master/templates/ai-use-case-intake-and-data-exposure-assessment.md) before approving, buying, enabling, experimenting with, or building an AI capability.
2. **Register the estate** — create or update the [AI landscape register](https://github.com/RusDavies/docs-management-practices/blob/master/templates/ai-landscape-register.md) once the use case, tool, model, agent, or vendor feature is material enough to track.
3. **Register material assistance** — use the [AI use register](https://github.com/RusDavies/docs-management-practices/blob/master/templates/ai-use-register.md) when AI materially assists drafting, review, synthesis, repository maintenance, decision support, or agentic work.
4. **Constrain agents** — use the [AI agent permission matrix](https://github.com/RusDavies/docs-management-practices/blob/master/templates/ai-agent-permission-matrix.md) whenever the AI capability can act, call tools, write data, communicate externally, or touch production-like systems.
5. **Version prompts and retrieval** — use the [AI prompt and retrieval-source register](https://github.com/RusDavies/docs-management-practices/blob/master/templates/ai-prompt-and-retrieval-source-register.md) when behaviour depends on prompts, system instructions, retrieval sources, vector stores, embeddings, or source freshness.
6. **Evaluate before approval** — use the [AI evaluation report](https://github.com/RusDavies/docs-management-practices/blob/master/templates/ai-evaluation-report.md) to record acceptance criteria, test evidence, failure modes, residual risk, and approval evidence.
7. **Review on change** — changes to model, provider, prompt, retrieval source, data class, tool permissions, user group, or production impact should trigger review and, where material, retesting.
8. **Retire deliberately** — when an AI capability is retired, update the register, remove access, handle retention/deletion, close vendor obligations, and record closure evidence.

This sequence is deliberately boring. Boring is good. Boring is how governance survives contact with busy humans and avoids becoming a panic archaeology project after the incident.

## Decision Gates

Use decision gates for material AI use.

### Intake Gate

Before a new AI tool, feature, or use case starts:

- purpose is clear
- owner is named
- data types are classified
- approved tool path is checked
- vendor/provider path is identified
- risk level is estimated
- experiment boundaries are defined

### Experiment Gate

Before testing:

- test data is safe
- user group is limited
- evaluation criteria exist
- cost limit exists
- failure and escalation path exists
- no production/customer impact occurs without approval

### Production Gate

Before production use:

- data exposure is approved
- architecture is reviewed where needed
- security/privacy/legal/procurement/vendor reviews are complete where needed
- evaluation evidence is sufficient
- monitoring exists
- incident path exists
- human approval gates are defined
- lifecycle owner accepts responsibility

### Change Gate

When model, provider, prompt, retrieval source, agent tools, permissions, or major workflow changes:

- expected behaviour is retested
- new data exposure is assessed
- cost/risk impact is reviewed
- users are informed where needed
- documentation is updated

### Retirement Gate

When retiring:

- access is removed
- data retention/deletion is handled
- vendor commitments are closed
- integrations are removed
- documentation and register are updated
- users are migrated or informed

## Disagree and Commit

AI decisions often involve real trade-offs: speed vs review, convenience vs data exposure, automation vs human accountability, experimentation vs control, vendor feature adoption vs architectural coherence.

Before deciding:

- surface objections explicitly
- separate policy preference from actual risk
- identify who owns residual risk
- document rejected options
- state what evidence would change the decision

After deciding:

- communicate the allowed path
- make controls practical
- monitor outcomes
- revisit decisions when evidence changes
- avoid quiet local exceptions that become shadow policy

Disagree and commit does not mean pretending concerns vanished. It means the concern is recorded, ownership is clear, and the organization proceeds deliberately.

## Practitioner Counterpart

For hands-on AI tooling, inventory, evaluation-support, monitoring-evidence, cost-signal, data-exposure, and vendor-dependency work, see [AI Operations Practitioner](https://github.com/RusDavies/docs-practitioner-practices/blob/master/roles/ai-operations-practitioner.md). This management guide owns governance, operating model, lifecycle, approval boundaries, risk acceptance, and accountability; the practitioner role owns execution support and evidence within those boundaries.

## Related Audience-Level Guides

Use the audience-level guides to adapt this discipline to the manager's scope, authority, and operating context:

- [Team Leads and Frontline Managers](https://github.com/RusDavies/docs-management-practices/blob/master/TEAM_LEADS_AND_FRONTLINE_MANAGERS.md) — day-to-day execution, coaching, coordination, and local accountability.
- [Managers of Managers](https://github.com/RusDavies/docs-management-practices/blob/master/MANAGERS_OF_MANAGERS.md) — consistency across teams, manager enablement, and cross-team operating cadence.
- [Directors and Senior Leaders](https://github.com/RusDavies/docs-management-practices/blob/master/DIRECTORS_AND_SENIOR_LEADERS.md) — multi-team strategy, prioritization, risk, and organizational health.
- [Executives and Founders](https://github.com/RusDavies/docs-management-practices/blob/master/EXECUTIVES_AND_FOUNDERS.md) — enterprise direction, culture, investment choices, and accountability systems.
- [Cross-Functional and Matrix Management](https://github.com/RusDavies/docs-management-practices/blob/master/CROSS_FUNCTIONAL_AND_MATRIX_MANAGEMENT.md) — shared ownership, influence, and decision-making without clean reporting lines.
- [Managing Up](https://github.com/RusDavies/docs-management-practices/blob/master/MANAGING_UP.md) — upward communication, expectation-setting, escalation, and decision framing.
- [Remote and Hybrid Management](https://github.com/RusDavies/docs-management-practices/blob/master/REMOTE_AND_HYBRID_MANAGEMENT.md) — distributed communication, trust, documentation, and inclusion.

## AI Tooling Evolution

Use [AI Tooling Evolution](../AI_TOOLING_EVOLUTION.md) for the shared model.

AI landscape management is both a discipline and the control plane for AI tooling evolution elsewhere. Tooling will help discover AI use, maintain registers, classify data exposure, evaluate outputs, monitor cost/risk, and assemble approval evidence.

The risk is recursive governance theatre: AI systems assessing AI systems without enough independent evidence, human review, or operational visibility. Leaders still own acceptable use, approval gates, provider/tool risk, and deciding where AI should not be used.

## Anti-Patterns

Avoid:

- policy-only governance: rules exist, behaviour does not change
- spreadsheet-as-control: the register exists but approvals, tooling, and guardrails do not
- tool sprawl: every team buys its own favourite assistant
- shadow AI normalization: unapproved tools become standard because approved paths are unusable
- vendor-default trust: AI features are enabled because the vendor added a button
- agent overpermissioning: agents get broad access because scoping is annoying
- permanent experiments: pilots become production without ownership or monitoring
- human review theatre: everyone says outputs are reviewed, nobody knows by whom
- data exposure denial: prompts and uploaded files are treated as if they are not data movement
- model mysticism: decisions are justified by AI output without evidence or accountability
- cost blindness: usage grows until finance discovers the invoice and begins speaking in capital letters

## Related Guides

- [Architecture Management](https://github.com/RusDavies/docs-management-practices/blob/master/disciplines/ARCHITECTURE_MANAGEMENT.md)
- [Technical Debt Management](https://github.com/RusDavies/docs-management-practices/blob/master/disciplines/TECHNICAL_DEBT_MANAGEMENT.md)
- [Procurement Management](https://github.com/RusDavies/docs-management-practices/blob/master/disciplines/PROCUREMENT_MANAGEMENT.md)
- [Vendor and Partner Management](https://github.com/RusDavies/docs-management-practices/blob/master/disciplines/VENDOR_AND_PARTNER_MANAGEMENT.md)
- [Risk Management](https://github.com/RusDavies/docs-management-practices/blob/master/disciplines/RISK_MANAGEMENT.md)
- [Incident Response Management](https://github.com/RusDavies/docs-management-practices/blob/master/disciplines/INCIDENT_RESPONSE_MANAGEMENT.md)
- [Security-Defect Remediation Prompt Pack](https://github.com/RusDavies/docs-management-practices/blob/master/templates/security-defect-remediation-prompt-pack.md)
