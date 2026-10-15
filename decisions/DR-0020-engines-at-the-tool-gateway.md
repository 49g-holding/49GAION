# DR-0020 · 49GAION — Engines at the tool gateway

- **Date:** 2026-10-16
- **Decided by:** the governing seat (GOV) of 49GAION (holder in the private holders register)
- **Source:** the direction of the governing seat (GOV) of 49GAION of 2026-10-16: "In 49GAION, add to the Standard the parts of these that belong in the Standard; add to the Protocol, in the language of the Protocol, the parts that belong there; and in the Library name all these AIOCs and place them: they are here so far. That is, fully complete and update, up to here, the matching of the three main 49GAION repositories with what has been achieved here." (translated). On the proposals drafted in the writing repository of the Target Operating Model (its `upstream/PROPOSALS.md`, items 6 and 7), from its review of a design stage that draws several engines for every check.
- **Relation:** builds on DR-0007 and DR-0010; it supersedes nothing.
- **Number:** this record takes the next free number at merge, after DR-0019

## Decision

1. **The engine register.** The tool gateway holds a register of the engines it may bind: for each, its family, the version it serves, its confidentiality ceiling, its retention and use terms, and the seats it may serve. The register changes only under `change-gateway-policy` (Standard §4.4, item 11).
2. **The engine served.** The gateway logs, for every call, the engine it bound and the engine that served; a call served by another engine is void. No item is sent to an engine whose ceiling is below its confidentiality level.
3. **Binding an engine is not a change of filler.** The engine a bot's calls run on is bound by the gateway under the register; binding or changing it is gateway policy, not `change-filler`. An engine serves a Cell only after passing that Cell's fixed test at its current version (Standard §3.2, item 2; §4.4, item 4).
4. **Version.** Unreleased `v1.6.0`, as DR-0019.

Powered by 49GAION
