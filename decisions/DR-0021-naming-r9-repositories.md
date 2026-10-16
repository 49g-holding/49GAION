# DR-0021 · 49GAION — Naming Standard R9: visibility, where a repository is recorded, mother and instance

- **Date:** 2026-10-16
- **Decided by:** the governing seat (GOV) of 49GAION (holder in the private holders register)
- **Source:** the direction of the governing seat (GOV) of 49GAION of 2026-10-16: "In 49GAION, add to the Standard the parts of these that belong in the Standard; add to the Protocol, in the language of the Protocol, the parts that belong there; and in the Library name all these AIOCs and place them: they are here so far. That is, fully complete and update, up to here, the matching of the three main 49GAION repositories with what has been achieved here." (translated). On the proposal drafted in the writing repository of the Target Operating Model (its `upstream/PROPOSALS.md`, item 3).
- **Relation:** builds on DR-0019, item 5; it supersedes nothing.
- **Number:** this record takes the next free number at merge, after DR-0020

## Decision

1. **Visibility.** The writing repository of an AIOC may be public only when it holds no organisation's data. Its `-records` and `-records-restricted` repositories are never public.
2. **Where it is recorded.** A repository is recorded before it is created, as an event on the AIOC's entry in the unit register, with its name, its visibility and its platform.
3. **Mother and instance.** Where an AIOC's writing repository also holds a Library mother blueprint, the mother holds no organisation's data, and the Library register pins it; the organisation's own values live in its records repository.
4. **Version.** Unreleased `v1.6.0`, as DR-0019.

Powered by 49GAION
