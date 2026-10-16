# DR-0024 · 49GAION — A mother repository for a Library part whose first instance holds an organisation's data

- **Date:** 2026-10-16
- **Decided by:** the governing seat (GOV) of 49GAION (holder in the private holders register)
- **Source:** the direction of the governing seat (GOV) of 49GAION of 2026-10-16 (translated): "Now that we have come this far, build these two as well, the public mother blueprint of Source Lifecycle and the mother version of Product Core, and add them"; and its choice, the same day, of where the two mothers live: "two new public repositories".
- **Relation:** builds on DR-0019 (the Library register) and DR-0021 (mother and instance); it supersedes nothing.
- **Number:** this record takes the next free number at merge, after DR-0023

## Decision

1. **Where the mother lives.** Where the writing repository of a Library part's first instance holds an organisation's data, the part's mother blueprint is written in a repository of its own, the part's **mother repository**. It is public, holds the mother only and no organisation's data, and is laid out and checked as a writing repository (the writing-repository guide of `49GAION-aioc`).
2. **Its name.** `49GAION-<part>`, where `<part>` is the part's name after "49GAION", in lower case, its words joined by hyphens; it stands beside the hub companions (Naming Standard R9, addition 4).
3. **The instance stays where it is.** The first instance keeps its own writing repository, private, and names the mother it is made from by pin. An instance's history is never made public to make a mother.
4. **Pinned like any mother.** The Library register pins the mother by repository, path, version, commit and SHA-256 (Standard §3.1, item 9). A new version reaches the Library only by a pull request that moves the pin.
5. **The first two.** 49GAION Source Lifecycle, in `49GAION-source-lifecycle`; 49GAION Product Core, in `49GAION-product-core`.
6. **Version.** Unreleased `v1.6.0`, as DR-0019.

Powered by 49GAION
