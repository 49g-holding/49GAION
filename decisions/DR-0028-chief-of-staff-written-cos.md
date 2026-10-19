# DR-0028 · 49GAION — The Chief of Staff, written COS

- **Date:** 2026-10-19
- **Decided by:** the governing seat (GOV) of 49GAION (holder in the private holders register)
- **Source:** the direction of the governing seat (GOV) of 49GAION of 2026-10-19 (translated): "The Chief of Staff, which has so many uses: put a rule in the Standard that its abbreviation is shown as COS; for example, COS so-and-so. This is the abbreviation of Chief of Staff."
- **Relation:** builds on DR-0004 (Cells and Pods; R15) and DR-0007 (the Cell that performs a capability has its own code); it supersedes nothing. `[ORG]AIOC-COS` and the placeholder `{COS}` stay retired.
- **Number:** this record takes the next free number at merge, after DR-0027

## Decision

1. **The short form.** "COS" is the one short form of "Chief of Staff", in display names, Panels, tables and prose. The capability's name stays "Chief of Staff"; COS names the capability, never a unit (Naming Standard R16, item 1).
2. **In a Cell's code.** The Chief of Staff Cell of an AIOC takes the code `[ORG]CELL-COS<initials>`, with that AIOC's initials: `[ORG]CELL-COSDI` for `[ORG]AIOC-DI`. This is the one exception to the initials of R15, item 2 (R16, items 2 and 3).
3. **Never a unit.** COS never forms an AIOC or a Pod code (R16, item 4).
4. **Codes already issued** never change in place. A mother blueprint moves at its next version, retiring the old code; an installed Cell moves only by entries in the unit register (R16, item 5).
5. **The machine form.** The `served_by` field of the unit card schema in `49GAION-protocol` accepts the same Cell codes as every other Cell field, 2 to 8 upper-case letters or digits, in its own pull request after this merges.
6. **Version.** The texts sit on main under the unreleased `v1.7.0`. The version labels and `state.json` stay at `v1.6.0` until GOV releases.

Powered by 49GAION
