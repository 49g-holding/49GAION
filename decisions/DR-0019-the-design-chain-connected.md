# DR-0019 · 49GAION — The design chain connected; the Library register; one release notice contract

- **Date:** 2026-10-16
- **Decided by:** the governing seat (GOV) of 49GAION (holder in the private holders register)
- **Source:** the direction of the governing seat (GOV) of 49GAION of 2026-10-16: "In 49GAION, add to the Standard the parts of these that belong in the Standard; add to the Protocol, in the language of the Protocol, the parts that belong there; and in the Library name all these AIOCs and place them: they are here so far. That is, fully complete and update, up to here, the matching of the three main 49GAION repositories with what has been achieved here." (translated); and, the same day, to connect the design chain so that the blueprints, engineering and documents of the human cycle are complete. On the work of the mother blueprints of the Target Operating Model (version 0.5.0), Process and Position Design (version 0.4.0) and Delivery and Implementation (version 0.1.1).
- **Relation:** builds on DR-0008, DR-0014, DR-0016, DR-0017 and DR-0018; it supersedes nothing.
- **Number:** this record takes the next free number at merge, after DR-0018

## Decision

1. **The design chain.** Source Lifecycle, then Target Operating Model, then Process and Position Design, then Delivery and Implementation. Each is a Library part of its own and stands alone; no stage waits for a later one. The Protocol section The design chain sets how they connect: one home for every release, in Source Lifecycle; a release notice to the next stage on every filing; returns to the stage that made the release, under one contract, each ending in one of four ways; no loop; each link a signed connection; the same independent assurance in every stage after Source Lifecycle; positions only.
2. **One release notice contract.** Every design stage announces a decided release to the stage after it under one Library contract, `library/contracts/release-notice.schema.json` in `49GAION-protocol`: by reference, with the releases it rests on, the filed copy, the final-status decision and the returns it answers; never release text or the name of a person. A stage's own notice contract may narrow a field; it never adds or removes one.
3. **Source Lifecycle serves the design stages.** Needs requests and their answers, the published sockets contract, the fields of a reference, pinned snapshots, a filing scope for each design stage (its own origin kind and design reports only) and notices are set in its Protocol section. Asking and filing stay with Source Lifecycle; a source that stands beside it is read only.
4. **Source Lifecycle in the Standard.** The Standard names Source Lifecycle among the Library's parts (§3.1, item 7), as DR-0008 and its Protocol section already hold it.
5. **The Library register.** The Library names every part once, in one register (`library/README.md` in `49GAION-protocol`): its card, its Protocol section, its place in the Standard, its fixed test and, for an AIOC part, its mother blueprint. A mother blueprint is written in its own writing repository for any organisation; the Library holds it by pin (repository, path, version, commit, SHA-256), never by a second copy. A new version reaches the Library only by a pull request that moves the pin.
6. **Cards and tests.** The cards of Source Lifecycle, Target Operating Model and Delivery and Implementation move to v2, and that of Process and Position Design to v3, each with its added cases; TEST-DESIGN-CHAIN v1 tests the chain as a whole. Every card stays `DRAFT`, with `last_result` `NOT_RUN`.
7. **Version.** The texts sit on main under the unreleased `v1.6.0`. The version labels and `state.json` stay at `v1.5.0` until GOV releases.

## Not decided here

- A mother blueprint of Source Lifecycle for any organisation: its first instance is private and holds an organisation's data; a mother is to be written from it and pinned.
- The pin of the mother blueprint of Product Core.

Powered by 49GAION
