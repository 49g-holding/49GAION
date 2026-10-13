# DR-0006 · 49GAION v1.4.1 — decision records frozen; how a change reaches main

- **Date:** 2026-10-13
- **Decided by:** the governing seat (GOV) of 49GAION (holder in `registers/HOAC-REGISTER.md`)
- **Source:** internal and external reviews, 2026-10-13, of hub 69a3e81, and the decision of the governing seat (GOV) of 49GAION on them

## Decision

1. **Decision records are frozen.** A decision record on main is never edited, renamed or deleted. A new record takes the next free number in merge order, with no gap and no reuse. A row of the index (`decisions/README.md`) changes only in its Status cell: from proposed to in force, or from in force to superseded by a newer record on main or in the same change. The required check `dr-frozen` enforces this and fails closed when the index cannot be read (Standard §2.2, item 3).
2. **How a change reaches main.** Every change reaches main as a pull request approved and merged by the governing seat (GOV) of 49GAION, with the required checks passing; the main-protection rules have no bypass actor. Changes under `.github/` are their own pull requests and land, and run green on main, before the content that needs them (required check `github-separation`). Each check judges a change with its copy on main (Standard §2.2, item 4).
3. **Code owners.** Each repository carries `.github/CODEOWNERS`, naming the governing seat's account for the paths it decides. It is documentation: the gate is the governing seat's recorded approval and the required checks.
4. **The signature-type check.** `signature-types-floor` reads its floor from main for a pull request and from the latest release tag for a change on main; it finds lists by content in any `.json`, `.yaml`, `.yml` or `.toml` file outside the allowed paths; it accepts only the keys `decision_types`, `id`, `human_floor`, `label`, `note` and the policy fields that the Standard's own list declares; and it fails a list that names a stop, a disconnection, narrowing or revoking AI access, or raising a matter to a human (Standard §4.4, item 6).
5. **No-removal baseline.** The no-removal baseline moves to the v1.4.0 release and keeps every v1.2.0 entry; a HOAC term must stand on its own heading, glossary row or definition.
6. **Removal of types.** The removal path of DR-0005 item 1 stays in force: a type of the 49GAION list is removed only by a decision of the governing seat (GOV) of 49GAION, recorded in a new decision record, with the matching change to the check in the same pull request. A type that an `[ORG]AION` added to its own list is removed only by its `[ORG]HOAC-GOV`, in a recorded decision.
7. **Version.** The 49GAION Standard moves to `v1.4.1`.

Powered by 49GAION
