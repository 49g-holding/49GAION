# DR-0005 · 49GAION v1.4.0 — Human Floor signature list: removal path and list location

- **Date:** 2026-10-13
- **Decided by:** the governing seat (GOV) of 49GAION (holder in `registers/HOAC-REGISTER.md`)
- **Source:** board decision, 2026-10-13

## Decision

1. **Removal path.** A type is removed from the Human Floor signature list only by a decision of 49GAION's governing seat (GOV), recorded in a new DR, with the matching change to `signature-types-floor` in the same PR. An `[ORG]AION` never removes a type (Standard §4.4, item 6).
2. **Where a list sits.** An `[ORG]AION` signature list sits under `org-aion-signature-types/` or is named `*.signature-types.json`, and holds its types under the key `decision_types` (Standard §4.4, item 6; Protocol §4.9).
3. **Enforcement.** The `signature-types-floor` check fails a change that drops a type of the Standard's list from any `[ORG]AION` list or from the Standard's own file, or that places a signature list anywhere else (`49g-holding/49GAION` pull request #14).
4. **Where each line sits.** The 49GAION Standard §4.4 item 6 (hub) and the Operating Protocol §4.9 (`49g-holding/49GAION-protocol` pull request #9).
5. **Version.** The 49GAION Standard and the Operating Protocol move to `v1.4.0`.

Powered by 49GAION
