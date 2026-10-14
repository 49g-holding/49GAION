# DR-0008 · 49GAION Source Lifecycle — the first stage of every source

- **Date:** 2026-10-14
- **Decided by:** the governing seat (GOV) of 49GAION (holder in the private holders register)
- **Source:** the direction of the governing seat (GOV) of 49GAION of 2026-10-14; the advisory review of 2026-10-14 of `49g-holding/49GAION-protocol` pull request 28; that pull request, merged by the governing seat at `d228d3b`
- **Number:** this record takes the next free number at merge, after DR-0007

## Decision

1. **A Library part.** 49GAION Source Lifecycle is a Library part. Its card is `library/cards/source-lifecycle.part-card.json` in `49g-holding/49GAION-protocol`. In an `[ORG]AION` it is the AIOC `[ORG]AIOC-SL` (Naming Standard R2).
2. **The first stage.** It is the first part an organisation receives after the Charter, and the stage through which every source enters. Like every other part, it enters through OCO (Standard §1.7, item 13; §5.3). It works for any organisation, from a single person to a group of entities. Its rules are Protocol §13.
3. **Contributors and secrets.**
   - Each contributor accepts an agreement before the first input.
   - Words become a record only after the contributor approves a preview of the exact text. Silence is never consent.
   - A secret is refused and appears in no record or log.
4. **Sockets and connections.** It has an input socket and an output socket.
   - A connection is approved and scoped by the `[ORG]HOAC-ACS` seat that `[ORG]AIOC-SL` is accountable to, as the listed type `connect-external-port`. A wider scope is `grant-or-widen-access`. No bot approves a connection or sets a scope.
   - That seat, or any seat above it, may revoke a connection. Revocation takes effect at the tool gateway first, is never held or blocked, and invalidates the token at the source service.
   - Every source connection runs through the tool gateway.
   - Each connection has its own token, with least privilege. A token is never written to any file, record or log.
   - Every connection, scope change and revocation is recorded in the unit register.
5. **Replaceable in later stages.** In the stages after the first, another source of documents or knowledge may replace it or stand beside it. Such a source must use the same sockets, follow the same connection rules and pass the joining test.
6. **Its data.** The organisation's sources are its own data and never enter the 49GAION Library (Standard §1.3, item 9).
7. **Test and status.** TEST-SOURCE-LIFECYCLE has one case for every rule of Protocol §13. The card stays `DRAFT`, with `last_result` `NOT_RUN`, until the test has run once with recorded evidence.
8. **Version.** The Protocol text sits on main under the unreleased `v1.6.0` row of its CHANGELOG. `state.json` and the version labels stay at `v1.5.0` until GOV releases. A later CI check for these rules goes in its own `.github` pull request, and becomes required only after it runs green on main.

Powered by 49GAION
