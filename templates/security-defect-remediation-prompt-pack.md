# Security-Defect Remediation Prompt Pack

Use these prompts to direct AI agents through security-defect discovery, exposure analysis, remediation planning, safe patch preparation, testing, evidence capture, upstream open source dependency contribution, and human approval gates.

These prompts are for defensive work on systems you own, are authorized to assess, or are explicitly permitted to review. They are not for probing third-party systems, generating weaponized exploit instructions, or doing the usual internet raccoon routine in someone else's infrastructure.

## How to Use This Pack

Use one prompt at a time. The output from one stage should feed the next stage.

Recommended sequence:

1. discovery
2. scanner-listed CVE handling, when the input is a tool/exported CVE list
3. reachability and exposure analysis
4. exploitability and business-risk classification
5. remediation planning
6. smallest safe patch proposal
7. regression and security test generation
8. upstream open source dependency fix proposal, where applicable
9. evidence packet generation
10. human approval gate
11. follow-up routing

Do not ask an agent to "fix all security issues" unless the desired outcome is a confident mess with a diff attached. Give it scope, evidence, constraints, and approval rules.

## Shared Context Block

Paste this block at the start of each prompt and fill it in.

```text
You are assisting with authorized defensive security remediation.

Repository/system:
- name:
- path or URL:
- primary languages/frameworks:
- deployment context:
- affected service/component/dependency:
- environment: local / dev / staging / production / unknown

Known finding or concern:
- source of finding:
- scanner/rule/CVE/manual report:
- affected files/packages/configs:
- suspected weakness:
- known affected versions:
- current evidence:

Scanner-listed CVE input, if applicable:
- scanner/export file:
- listed CVEs:
- affected packages and installed versions:
- scanner-recommended fixed versions:
- known API/GUI/deployment compatibility constraints:
- downstream surfaces we do not control:
- whether opportunistic unlisted-CVE discovery is in scope:

Constraints:
- do not make production changes
- do not access third-party systems
- do not publish exploit details
- do not change public APIs without approval
- preserve existing behaviour unless remediation requires otherwise
- prefer smallest safe fix first
- generate tests/evidence for any proposed fix
- identify human approval gates explicitly

Output requirements:
- separate facts from assumptions
- cite files, functions, packages, config keys, or commands inspected
- state confidence level
- state what evidence would change the assessment
- list residual risks
```

## Prompt 1: Defect Discovery

Use when the agent needs to search for possible security defects across code, configuration, infrastructure, dependencies, or deployment metadata.

```text
Using the shared context, inspect the repository/system for security defects related to [scope: dependency risk / injection / authz / secrets / insecure config / unsafe deserialization / cryptography / data exposure / IaC / container images / other].

Tasks:
1. Identify candidate defects with file/package/config references.
2. Separate confirmed evidence from suspicions.
3. Explain the weakness category in practical terms.
4. Identify whether each candidate is local code, configuration, infrastructure, dependency, or vendor/tooling related.
5. Prioritize candidates for reachability/exposure analysis.
6. Do not produce exploit instructions. If proof is needed, describe a safe validation approach.

Return:
- candidate defect list
- evidence references
- confidence per candidate
- recommended next analysis step
```

## Prompt 2: Scanner-Listed CVE Handling

Use when a scanning tool provides a list of specific CVEs. The agent must handle the listed CVEs, but must not treat the scanner list as complete truth.

```text
Using the shared context and scanner-listed CVE input, analyze and plan remediation for the listed CVEs.

Tasks:
1. Parse the scanner/exported CVE list and identify each listed CVE, package, installed version, recommended fixed version, and affected file/lockfile/build reference.
2. Confirm whether each listed CVE appears applicable to this repository or deployment from local evidence. Do not assume scanner output is perfect.
3. Identify whether a direct dependency upgrade would change public API, GUI behaviour, deployment/runtime contracts, plugin surfaces, generated artifacts, or downstream code we do not control.
4. If a direct upgrade risks breaking a surface we do not control, prefer a smallest safe fix-in-place or compatibility-preserving mitigation. Explain why this is safer than a blind upgrade.
5. If a safe non-breaking upgrade exists, prefer it and document compatibility evidence.
6. Inspect nearby dependency usage, lockfiles, manifests, advisories, and vulnerable APIs for additional known CVEs not present in the scanner list.
7. For unlisted CVEs discovered opportunistically, fix them if safely in scope; otherwise report them clearly with evidence, risk, and recommended follow-up.
8. Identify tests that prove the listed CVEs are fixed and that compatibility-sensitive surfaces still behave as expected.
9. Identify human approval gates for dependency forks, patched artifacts, public API/GUI changes, or residual risk acceptance.

Return:
- listed CVE handling matrix
- applicability evidence per CVE
- upgrade-vs-fix-in-place decision per CVE
- compatibility surfaces protected
- unlisted CVEs discovered and disposition
- proposed tests/evidence
- residual risks and approval gates
```

## Prompt 3: Reachability and Exposure Analysis

Use after a finding exists. This prompt tries to answer whether the defect matters in this deployment context.

```text
Using the shared context and the candidate defect below, analyze reachability and exposure.

Candidate defect:
[paste finding]

Tasks:
1. Determine whether the affected code/config/dependency is used in this repository or deployment.
2. Trace entry points, call paths, routes, jobs, handlers, permissions, or dependency imports where feasible.
3. Identify whether the defect is reachable by:
   - unauthenticated external users
   - authenticated users
   - privileged users/admins
   - internal services
   - CI/CD actors
   - local operators
   - attackers with prior foothold
4. Identify data, secrets, systems, privileges, or customers potentially exposed.
5. Identify compensating controls.
6. Identify uncertainty and what evidence would reduce it.

Return:
- reachable / not reachable / unknown
- exposed / not exposed / unknown
- affected assets
- call path or configuration path evidence
- compensating controls
- confidence
- recommended remediation urgency
```

## Prompt 4: Exploitability and Business-Risk Classification

Use only after reachability/exposure analysis. Do not ask for weaponized exploitation.

```text
Using the shared context, the finding, and the reachability/exposure analysis, classify realistic risk.

Inputs:
Finding:
[paste finding]

Reachability/exposure analysis:
[paste analysis]

Tasks:
1. Classify exploitability without providing weaponized exploit steps.
2. Consider asset criticality, data sensitivity, privilege impact, network exposure, tenant/customer impact, regulatory relevance, and operational blast radius.
3. Distinguish scanner severity from system-specific risk.
4. Identify likely false-positive or low-materiality cases.
5. Recommend remediation SLA or urgency using these AI-assisted defaults unless stricter incident, legal, customer, regulatory, or exploit context applies: Critical: fix or verified mitigation within 1 hour and publish/push to production within 12 hours; High: 1 day; Moderate: 3 days; Low: 7 days.
6. Identify whether risk can be temporarily mitigated, including whether the vulnerable path can be made unreachable.
7. Identify who must approve risk acceptance if remediation is deferred.

Return:
- risk rating: critical / high / moderate / low / informational
- rationale
- exposure window concern
- recommended SLA/urgency
- temporary mitigations
- reachability-removal option and evidence needed
- human approval required
```

## Prompt 5: Remediation Plan

Use before patching. The goal is to compare options and choose the smallest safe path.

```text
Using the shared context and validated risk analysis, propose a remediation plan.

Inputs:
Validated defect and risk:
[paste]

Tasks:
1. Propose the smallest safe remediation.
2. Propose any broader structural remediation if the small fix only treats the symptom.
3. Identify dependencies, compatibility concerns, migration issues, or behaviour changes.
4. Identify tests needed to prove the fix.
5. Identify deployment and rollback considerations.
6. Identify whether an upstream open source dependency fix should be proposed.
7. If the defect is in an open source dependency and no safe upgrade is immediately available, assess whether a controlled patch-in-place path is appropriate: pull the exact source version, apply a minimal local fix, build locally, publish the patched artifact through an approved internal artifact repository/proxy such as JFrog Artifactory, and consume that approved artifact locally until upstream remediation is available.
8. If the safest path is to make the vulnerable route, feature, dependency path, network path, identity path, or deployment path unreachable, identify the exact reachability change and the verification evidence needed.
9. Identify human approval gates.

Return:
- recommended remediation option
- alternatives considered
- trade-offs
- files/packages/configs likely affected
- dependency artifact/provenance plan, if applicable
- reachability-removal plan, if applicable
- test plan
- rollout/rollback notes
- approval gates
```

## Prompt 6: Smallest Safe Patch Proposal

Use when the agent may prepare a patch or PR. Keep scope tight.

```text
Using the approved remediation plan, prepare the smallest safe patch.

Approved remediation plan:
[paste]

Rules:
- preserve existing behaviour unless the security fix requires a change
- avoid broad refactors
- include tests where feasible
- do not hide uncertainty
- do not modify unrelated files
- document residual risk

Tasks:
1. Identify exact files/configs/packages to change.
2. Prepare a minimal patch or patch plan.
3. Explain why the patch addresses the defect.
4. Add or describe tests that should fail before the fix and pass after it.
5. Identify any follow-up work that should not be included in the small patch.

Return:
- patch summary
- changed files
- test additions
- validation commands
- residual risks
- follow-up items
```

## Prompt 7: Regression and Security Test Generation

Use to make the fix verifiable.

```text
Using the defect, remediation plan, and proposed patch, generate regression and security tests.

Inputs:
Defect:
[paste]

Patch summary:
[paste]

Tasks:
1. Identify the smallest test that proves the defect is fixed.
2. Identify negative tests and boundary cases.
3. Add dependency/config/IaC validation tests where relevant.
4. Avoid tests that require unsafe third-party probing.
5. Identify commands to run locally or in CI.
6. Explain which tests would have caught the defect earlier.

Return:
- proposed tests
- test file names/locations
- validation commands
- expected before/after behaviour
- coverage gaps
```

## Prompt 8: Upstream Open Source Dependency Fix Proposal

Use when the defect appears to be in an open source dependency, not just local application code.

This prompt should consider three tracks:

1. **Consume a safe upstream version** — upgrade when a suitable fixed version exists.
2. **Contribute upstream responsibly** — private report, issue, failing test, or pull request depending on disclosure status and project policy.
3. **Patch in place under governance** — when no safe upstream version exists yet and exposure cannot wait, pull the exact source version, apply the smallest local fix, build a patched artifact locally, publish it through an approved internal artifact repository/proxy such as JFrog Artifactory, and consume that approved artifact until the upstream fix can replace it.

All external dependencies should be consumed through an approved dependency-management path, ideally an internal artifact repository/proxy with approvals, scanning, provenance, immutability/versioning, and retirement tracking. JFrog Artifactory is one common example. The important point is the control plane, not the logo on the invoice.

```text
Using the shared context and validated defect analysis, assess whether an upstream open source dependency fix should be proposed.

Dependency:
- package/project:
- version in use:
- upstream repository:
- security policy / disclosure process:
- existing issue/advisory/fix status:

Tasks:
1. Confirm whether the defect is in the upstream dependency or in local usage/configuration.
2. Check whether upstream has already fixed or documented the issue.
3. Recommend local mitigation, safe upgrade path, or controlled patch-in-place path.
4. If patch-in-place is considered, identify:
   - exact upstream source version to fetch
   - source authenticity/provenance checks
   - minimal local patch
   - build command and reproducibility expectations
   - patched artifact naming/versioning convention
   - internal repository/proxy publication path, such as JFrog Artifactory
   - approval, scanning, signing, and retention requirements
   - traceability from original defect/finding to patched source commit, build job, artifact digest/version, scan results, test results, and consuming application lockfile/build reference
   - evidence that the specific defect is no longer present in the patched source and built artifact, not merely that a build succeeded
   - dependency-lockfile or build-system changes needed to consume the patched artifact
   - rollback and retirement plan once upstream remediation is available
5. If appropriate, draft a responsible upstream issue, security report, or pull request plan.
6. Include a minimal reproduction or failing test plan where safe.
7. Avoid publishing exploit details if the issue is sensitive and not already public.
8. Identify whether legal/security approval is needed before contacting upstream or distributing patched artifacts internally.
9. Identify how to retire local forks, patches, patched artifacts, or mitigations once upstream remediation is available.

Return:
- upstream involvement recommendation: none / issue / private security report / PR / wait for advisory / vendor escalation
- local protection plan
- patch-in-place recommendation: not needed / recommended / emergency-only / rejected
- patched artifact and internal repository plan, if applicable
- defect-absence traceability evidence, if patch-in-place is used
- responsible disclosure notes
- draft upstream summary or PR plan
- human approvals required
- follow-up tracking plan
```

## Prompt 9: Evidence Packet Generation

Use when preparing a remediation record, PR evidence, audit packet, or risk review.

```text
Using all prior outputs, create a security-defect remediation evidence packet.

Inputs:
- finding:
- reachability/exposure analysis:
- risk classification:
- remediation plan:
- patch summary:
- test results:
- upstream dependency notes, if any:

Tasks:
1. Summarize the original defect.
2. Summarize reachability, exposure, and exploitability without weaponized detail.
3. Describe the remediation and why it is sufficient.
4. Include tests, scans, or commands run.
5. Identify before/after evidence.
6. For patched open source dependencies, include traceability from original finding to patched source, build job, artifact digest/version, internal repository/proxy record, consuming lockfile/build reference, scan results, test results, and evidence that the specific defect is no longer present.
7. Identify residual risk and accepted risk owner, if any.
8. Identify follow-up work.
9. Identify human approvals completed or still required.

Return:
- executive summary
- technical summary
- evidence table
- validation commands and results
- patched dependency traceability, if applicable
- residual risk
- follow-up actions
- approval status
```

## Prompt 10: Human Approval Gate

Use before production-impacting or sensitive changes.

```text
Using the remediation evidence packet, determine whether this change is ready for human approval.

Tasks:
1. Identify whether the change affects production, auth/authz, cryptography, privacy, data handling, customer behaviour, public APIs, vendor dependencies, or compliance obligations.
2. Identify whether tests and evidence are sufficient.
3. Identify rollback and monitoring readiness.
4. Identify unresolved uncertainty.
5. Identify who should approve: engineering owner, security, privacy, legal, product, operations, architecture, vendor manager, or executive/risk owner.
6. Recommend approve / approve with conditions / reject / defer for more evidence.

Return:
- approval recommendation
- required approvers
- conditions
- blockers
- residual risks
- review date if risk is accepted
```

## Prompt 11: Follow-Up Routing

Use when the issue is not only a patch.

```text
Using the remediation evidence packet, identify follow-up routing.

Tasks:
1. Determine whether follow-up belongs to:
   - architecture management
   - technical debt management
   - risk management
   - incident response management
   - operations management
   - product management
   - procurement/vendor management
   - AI landscape management
   - upstream open source dependency maintainer process
2. Identify whether the defect indicates a recurring pattern.
3. Recommend preventive controls, standards, tests, monitoring, dependency policy, architecture change, or procurement/vendor action.
4. Create concise follow-up backlog items with owner, rationale, and evidence.

Return:
- follow-up routing table
- recommended backlog items
- owners/forums
- evidence links
- urgency
```

## Verification Notes

To verify these prompts, use a controlled defect corpus rather than production systems. The corpus should contain small, deliberately vulnerable examples in multiple languages and frameworks, with known ground-truth defects, expected reachability/exposure classifications, intended fixes, tests, and evidence expectations.

A useful corpus should include:

- local application defects
- dependency defects
- configuration defects
- infrastructure-as-code defects
- container/image defects
- false positives
- unreachable defects
- reachable but low-impact defects
- reachable high-impact defects
- defects requiring upstream open source dependency handling
- scanner-listed CVE lists where direct dependency upgrades would break public API, GUI, runtime, or downstream surfaces
- additional known CVEs intentionally omitted from the scanner list to test opportunistic discovery and reporting

The point is not to train agents to perform party tricks on toy vulnerabilities. The point is to measure whether the prompt workflow can separate scanner noise from real exposure, propose safe remediation, generate useful tests, preserve evidence, and route human decisions correctly.

## Usage Notes

- Use these prompts only for authorized defensive review and remediation.
- Run stages in sequence when evidence matters: discovery, reachability, risk, remediation, tests, evidence, approval.
- Keep human approval gates explicit for production, public API, dependency, or security-sensitive changes.
- Validate agent output with tests, source inspection, and reviewer judgment.
- For scanner-driven workflows, analyze findings in function/method/resource/package chunks with surrounding context; do not rely on isolated scanner rows or whole-repository prompt dumps.

## Example

For a reported dependency CVE, provide repository context, affected package/version, deployment exposure, compatibility constraints, and the scanner/exported CVE list. Run scanner-listed CVE handling before remediation planning so the agent decides between safe upgrade, fix-in-place, or report-only handling with evidence instead of blindly bumping a dependency and breaking someone else's GUI. Tiny mercy.
