# DR-0014 · 49GAION — Process and Position Design, a Library part after the target operating model

- **Date:** 2026-10-15
- **Decided by:** the governing seat (GOV) of 49GAION (holder in the private holders register)
- **Source:** the directions of the governing seat (GOV) of 49GAION of 2026-10-15. First: "This is a separate AIOC. Its input is the target operating model itself, not Source Lifecycle; it is linked to the target operating model itself, because, as we said, that model may have defects and go back and forth. I do not want to merge it with the target operating model or with the stage after it." Then, on the proposal of the AI hub: "Good, yes. Only its full version, that of 49GAION: write its full name in the Library of 49GAION now, write that too, add its description to my Standard, and let us continue." (translated)
- **Relation:** builds on DR-0011 and DR-0013; it supersedes nothing.
- **Number:** this record takes the next free number at merge, after DR-0013

## Decision

1. **The part.** **49GAION Process and Position Design** is a Library part, with its card in `49GAION-protocol` (`library/cards/process-and-position-design.part-card.json`, `DRAFT`, `last_result` `NOT_RUN`) and its rules in Protocol §17. In an `[ORG]AION` it is the AIOC `[ORG]AIOC-PPD`.
2. **A part of its own.** It is never merged with the part that designs the target operating model, or with the stage after it.
3. **Linked directly to the target operating model.** It takes the decided target operating model release by reference (ID, version and hash) from the part that made it, not through Source Lifecycle. It never edits that release: every defect it finds goes back to that part as a return, and the two parts may go back and forth until the release holds.
4. **Other sources.** Every other source comes only from Source Lifecycle, and what is missing is asked through Source Lifecycle.
5. **One stage, processes first.** It designs the organisation's processes, with their steps, decisions, hand-offs and measures, and then the positions that carry them. Every position is built from the steps and decisions it holds, and its job description is generated from them.
6. **Positions only.** It designs positions, never people (DR-0013). It makes no choice of what fills a position; that belongs to a later stage.
7. **Decided and filed.** Every element is decided by the organisation before release. The release is frozen, filed into Source Lifecycle as a source, and handed to the next stage by reference.
8. **Where it sits.** The Standard carries the part in §3.1, item 3, and in the terms table; the Protocol in §17, with the card and its fixed test, TEST-PROCESS-AND-POSITION-DESIGN v1. Its mother blueprint is written on the AIOC template in its own writing repository, generalised, with no organisation data.
9. **Version.** The texts sit on main under the unreleased `v1.6.0`. The version labels and `state.json` stay at `v1.5.0` until GOV releases.

## Not decided here

- The Library card and Protocol section of the part that designs the target operating model.
- Whether the position register carries job families and levels.

Powered by 49GAION
