# Machine Change Folder

## Purpose

Create a traceable folder for a machine-level change so the implementer can show the approved plan, exact execution script, rollback path where one exists, and current state.

Use this when changing a server, workstation, virtual machine, appliance-like host, or other managed machine. Filter the detail by risk. The folder should make execution safer and more reviewable; it should not become ceremonial paperwork for a harmless one-line change.

## Folder Location

In the central repository of changes:

```text
changes/
  YYYYMMDDHHMM_short_slug/
    PLAN.md
    STATE.md
    implement.sh
    rollback.sh
```

Use platform-appropriate script names, for example:

- `implement.sh` and `rollback.sh` for Linux or Mac shell-based changes
- `implement.ps1` and `rollback.ps1` for Windows PowerShell changes
- a more specific name when multiple scripts are needed, such as `01_precheck.sh`, `02_apply.sh`, or `rollback_dns_change.ps1`

Mirror the relevant change folder onto the target machine before execution:

- Linux or Mac: `/root/changes/YYYYMMDDHHMM_short_slug/`
- Windows: `C:\Users\admin\changes\YYYYMMDDHHMM_short_slug\`

If the target uses a different privileged administration path, record the exception in `PLAN.md`.

## Naming

Use:

```text
YYYYMMDDHHMM_short_slug
```

Examples:

- `202607061135_rotate_nginx_cert`
- `202607061420_disable_legacy_tls`
- `202607061505_update_backup_schedule`

The timestamp should reflect when the change folder was created or scheduled, using the team's agreed timezone. The slug should be short, lowercase, and specific enough that someone can identify the change without opening every file like a disappointed archaeologist.

## PLAN.md

```markdown
# Change Plan: <short title>

## Summary

- Change folder:
- Target machine(s):
- Environment:
- Change lead / owner:
- Change implementer:
- Reviewer / verifier:
- Rollback / pause authority:
- Scheduled window:
- Approval / reference:

## Objective

What is changing and why?

## Scope

- In scope:
- Out of scope:

## Prerequisites

- Access confirmed:
- Backup / snapshot / export:
- Maintenance window or user notice:
- Dependencies:
- Required files or secrets:

## Implementation

- Script:
- Dry run available:
- Expected duration:
- Commands or steps:

## Validation

- Pre-change checks:
- Post-change checks:
- Evidence to capture:

## Rollback

- Reversible: Yes / No
- Rollback script:
- Rollback trigger:
- Rollback validation:
- If not reversible, containment path:

## Risks and Exceptions

- Known risks:
- Accepted exceptions:
- Escalation path:

## Target Mirror Location

- Linux or Mac: `/root/changes/<change-folder>/`
- Windows: `C:\Users\admin\changes\<change-folder>\`
- Exception path, if any:
```

## STATE.md

```markdown
# Change State: <short title>

Current state: PENDING

## State History

| Timestamp | State | Actor | Reason / evidence |
| --- | --- | --- | --- |
| 2026-07-06 11:35 EDT | PENDING |  | Change folder created |
```

Allowed states:

- `PENDING` - planned but not currently applying
- `APPLYING` - implementation has started
- `SUCCESS` - implementation and validation succeeded
- `FAIL` - implementation or validation failed; include short reason and containment/next action
- `REVERTED` - rollback or reversal completed; include short reason and evidence

Update `STATE.md` before execution starts, after validation, and after any rollback or failure decision.

## Implementation Script Expectations

The implementation script should:

- declare the target platform and assumptions
- fail clearly when prerequisites are missing
- avoid interactive prompts during the approved window
- log material commands, outputs, and timestamps where appropriate
- avoid hiding destructive steps behind vague wrapper names
- be repeatable or explicitly say when it is not
- exit non-zero on failure

## Rollback Script Expectations

If the change is reversible, the rollback script should:

- describe what it restores
- check that rollback is safe to run
- preserve evidence before changing state again
- restore the prior configuration, package, service state, file, permission, route, rule, or setting where practical
- run rollback validation checks
- exit non-zero on failure

If rollback is impossible or unsafe, do not fake it. Record the no-rollback rationale in `PLAN.md` and define containment, escalation, restore-from-backup, rebuild, or forward-fix options.

## Usage Notes

- Keep the central repository as the source of planning and evidence.
- Mirror the change folder to the machine so execution does not depend on a chat transcript, browser tab, or someone's heroic memory.
- Do not store secrets in the change folder unless the repository and target path are approved for that sensitivity.
- For high-risk production changes, include captured pre-checks, approvals, peer verification, backup/snapshot evidence, and post-change logs.
- For low-risk changes, keep the folder lean. The goal is disciplined implementation, not paperwork breeding in captivity.
