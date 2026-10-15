# DR-0022 · 49GAION — Method catalogues in the Library; the reference-model catalogue

- **Date:** 2026-10-16
- **Decided by:** the governing seat (GOV) of 49GAION (holder in the private holders register)
- **Source:** the direction of the governing seat (GOV) of 49GAION of 2026-10-16: "In 49GAION, add to the Standard the parts of these that belong in the Standard; add to the Protocol, in the language of the Protocol, the parts that belong there; and in the Library name all these AIOCs and place them: they are here so far. That is, fully complete and update, up to here, the matching of the three main 49GAION repositories with what has been achieved here." (translated). On the proposal drafted in the writing repository of the Target Operating Model (its `upstream/PROPOSALS.md`, item 9), whose design stage reads reference models as methods only, as its governing seat directed when it took them up.
- **Relation:** builds on DR-0016 and DR-0019; it supersedes nothing.
- **Number:** this record takes the next free number at merge, after DR-0021

## Decision

1. **Method catalogues.** The Library also holds the method catalogues that blueprints read. A method catalogue holds no organisation's data, copies no text, and is never evidence about an organisation (Standard §3.1, item 1).
2. **The reference-model catalogue.** `library/reference-models/reference-model-catalogue.json` in `49GAION-protocol`, version `v0.1.0`, status `draft`, with its schema and its README: seven operating-model patterns, each with its typical capabilities, decision rights by role-type, typical hand-offs, when it fits and when it does not, and its known risks. It names role-types only, never a person or a position.
3. **Taken into use by pin.** A part reads it only at a version it has pinned by commit and SHA-256, as a tested change of that part; until then the part declares it unavailable.
4. **Version.** Unreleased `v1.6.0`, as DR-0019.

Powered by 49GAION
