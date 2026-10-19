# DR-0030 · 49GAION — Five readings from the Charter mother

- **Date:** 2026-10-19
- **Decided by:** the governing seat (GOV) of 49GAION (holder in the private holders register)
- **Source:** the direction of the governing seat (GOV) of 49GAION of 2026-10-19 (translated): "Do it", on the Operating Core Office's report that five drafts of the Charter mother, `github.com/49g-holding/49GAION-charter`, `upstream/PROPOSALS.md`, wait for GOV's word.
- **Relation:** builds on DR-0007 (the root; the tool gateway), DR-0028 (R16) and DR-0029 (the Charter in the Library). It supersedes nothing. It reads R16, item 2, "the one exception to the initials of R15, item 2", as one of two exceptions (item 1 below).
- **Number:** this record takes the next free number at merge, after DR-0029

## Decision

1. **"GOV" in a Cell's code.** The Cell that carries the unscoped `[ORG]HOAC-GOV` may take the code `[ORG]CELL-GOV`. GOV is the Standard's own short form of the governing seat, as COS is of the Chief of Staff. The Library has used this code since `v1.5.0`. This is a reading note to Naming Standard R15, item 2.
2. **The ports of the part that holds the gateway.** For the Charter, `enforcement: shared-gateway-outside-unit` reads as enforced by the gateway's own policy, changed only under `change-gateway-policy`, with its log reviewed by the internal-audit line (Standard §4.4, item 11). This is a description in the Protocol's port card schema; no value changes.
3. **Two acts for the signature list.** An addition to an `[ORG]AION`'s own signature list is `change-org-standard-or-signature-list` (Standard §4.4, item 6). Loading the list with that addition at the gateway is `change-gateway-policy` (item 11). They are two acts, and the gateway applies the addition only after both.
4. **The Charter's own parts.** Every installation, change or retirement of a Pod or Cell of the Charter is a change of the Charter. The Cell carrying the unscoped `[ORG]HOAC-GOV` signs it (Standard §1.7, item 13), even where the part is accountable to the Cell carrying `[ORG]HOAC-TM`. In the Protocol, `hoac_over` returns that Cell for the types `create-or-install-unit`, `retire-unit`, `change-parent`, `set-or-move-hoac-label`, `approve-change-or-promote-challenger` and `restore-or-rollback` on such a part. If that Cell's `authority_scope` does not cover the type, it returns nothing, and the action is held.
5. **The restart of a stopped Charter.** The Cell carrying `[ORG]HOAC-GOV` is inside the Charter, and nothing is above it, so no seat of the `[ORG]AION` can sign the Charter's restart (Standard §4.3, items 4 and 7). A stop of the whole Charter is lifted as the organisation's constituting documents set, outside the `[ORG]AION`. The restart is then recorded in the unit register. No AI and no part of the `[ORG]AION` restarts it.
6. **Where it sits.**
   - **Hub:** a reading note to Naming Standard R15; an addition to Standard §1.7, item 13 (items 4 and 5); an addition to §4.4, item 11 (item 3).
   - **Protocol:** an addition to §4.10, item 11 (`hoac_over`, item 4), and the description of `enforcement` in `spec/schemas/port-card.schema.json` (item 2), in a pull request after this merges.
   - **Reference organisations:** one query that tests item 4.
   - **The Charter mother:** its exceptions of blueprint §11 that these items settle are closed at its next version.
7. **Version.** The texts sit on main under the unreleased `v1.7.0`. The version labels and `state.json` stay at `v1.6.0` until GOV releases.

Powered by 49GAION
