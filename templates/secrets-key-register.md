# Secrets / Key Register

## Purpose

Track important secrets, keys, certificates, tokens, and credentials with ownership, storage location, access boundaries, rotation expectations, expiry, emergency procedures, and retirement status.

## Register Context

- Product / service / environment:
- Register owner:
- Review cadence:
- Last reviewed:

## Secret / Key Inventory

| Secret / key ID | Type | Purpose | Owner | Storage location | Access group | Rotation cadence | Expiry | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | API key / signing key / encryption key / SSH key / certificate / token / credential |  |  |  |  |  |  |  |

## Controls and Evidence

| Secret / key ID | Generation process | Rotation evidence | Monitoring / audit | Backup / recovery | Retirement / deletion plan |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Exposure and Emergency Rotation

| Scenario | Detection method | Immediate action | Owner | Communication / escalation | Evidence retained |
| --- | --- | --- | --- | --- | --- |
| Suspected leak |  |  |  |  |  |
| Owner unavailable |  |  |  |  |  |
| Vendor compromise |  |  |  |  |  |
| Certificate expiry risk |  |  |  |  |  |

## Usage Notes

- Do not store secret values in this register. This is a map, not a treasure chest for future attackers. Honestly, humans.
- Record approved storage locations and access groups, not chat messages, tickets, spreadsheets, or somebody’s “temporary” notes.
- Review before expiry dates, after staff/vendor changes, after suspected exposure, and during incident readiness checks.

## Example

A public API service might track TLS certificates, package-signing keys, cloud deployment tokens, database credentials, webhook secrets, and third-party provider API keys without recording the actual secret values.
