# DR-0009 · Supplement to DR-0008 — signing delegation, gateway reading, after-the-fact review of OCO's commits

- **Date:** 2026-10-14
- **Decided by:** the governing seat (GOV) of 49GAION (holder in the private holders register)
- **Source:** the advisory review of 2026-10-14, for the governing seat, of DR-0008 (`49g-holding/49GAION` pull request 57) and of `49g-holding/49GAION-protocol` pull request 28, which found their content sound; this pull request, merged by the governing seat
- **Relation:** supplements DR-0008. It does not supersede it; DR-0008 stays frozen and in force.
- **Number:** this record takes the next free number at merge, after DR-0008

## Decision

1. **Signing delegation.** Where Standard §1.5 binds a Human Floor type to a seat, that seat signs, unless it has delegated the type through the `authority_scope` of another labelled human Cell, which then signs within that scope (Standard §4.4, item 8; Protocol §4.9, item 5; Protocol §4.10, item 11). The signatures named in DR-0008 item 4 are read with this rule.
2. **Gateway reading.** "Outside every AIOC" (DR-0007 item 8) is read with the root rule (Standard §1.7, item 13): the tool gateway is held in the Charter, outside every other AIOC. The reading notes added by `49g-holding/49GAION` pull request 56 and `49g-holding/49GAION-protocol` pull request 27 say the same. "The tool gateway" in DR-0008 item 4 is read the same way.
3. **After-the-fact review of OCO's commits.** Three commits by OCO reached main and the `v1.5.0` release before an independent review:
   - `f0c8f67` in `49g-holding/49GAION`;
   - `745accd` in `49g-holding/49GAION-protocol`;
   - `2a7266a` in `49g-holding/49GAION-aioc`.

   The advisors of the governing seat reviewed them on 2026-10-14 and kept them. The fix in `745accd` was proven by a run on its parent commit.
4. **Open item.** Whether HF-07 needs a separate listed type, `change-accountable-to`, stays an open item. This record does not decide it.
5. **Nothing else changes.** The text of DR-0008 stays as merged. The Source Lifecycle card stays `DRAFT`, with `last_result` `NOT_RUN`. The `v1.6.0` row of the Protocol CHANGELOG stays Unreleased, and `state.json` and the version labels stay at `v1.5.0`.

Powered by 49GAION
