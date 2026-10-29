# Adopting 49GAION

**One page for an organisation that will run on 49GAION: what to do first, and with which text.** Where this page and the complete definition differ, the definition governs (`49GAION-FRAMEWORK.md`).

## Before you start

- **A governance seat.** One position, `[ORG]HOAC-GOV`, whatever stands behind it: a board, its representative or the owner, as the organisation's own arrangement sets (the complete definition, §6).
- **Your own mechanism for your human side.** Who holds each position, and the credentials with which a position signs, are yours, within the law and outside the system. 49GAION knows positions only.
- **The law.** Every act is signed by a position of the legal entity that acts. Drafts with legal effect go to a qualified professional of that jurisdiction.

## Ten steps

1. **Read** the Guide (`guide/THE-49GAION-GUIDE-VERSION-2.md`), then the complete definition. They take about an hour together.
2. **Bring the request to Edition Maker.** Every request starts there (the complete definition, §10). Its requirements are in `49g-holding/49GAION-protocol`, `library/edition-maker/PRD.md`. It is specified, not yet built: until it is, an edition is prepared by hand to the same requirements.
3. **The intake.** What the organisation is for, its outputs and their quality, its inputs, its musts, its money and time, and the measures of success. Fix the measures now: the organisation will be judged by them (Standard §1.8, item 3).
4. **The founding configuration.** Name the governance seat's substitute for a conflict or an empty seat, the waiting period for a new credential of GOV or TM if you want one, the quorum of any listed type above one, and the times after which a held matter is raised (Standard §4.4, items 20 and 21).
5. **The core.** It is made from the Library part 49GAION Charter (`49g-holding/49GAION-charter`). The tool gateway and the stop come with it and run as code beside it, outside the reach of every AI. At the handover the organisation issues fresh keys, and every key Edition Maker used is revoked.
6. **The signature list.** Start from 49GAION's list at its latest release (`upstream/human-floor-signature-types.json`); add your own types as `org-choice`. At the handover the list holds every `fixed` type.
7. **The first proposal and the mandate.** The core proposes a small organisation; the governance seat approves it and hands the operation to Top Management by a mandate; the Top Management Group, the first AIOC under the core, builds and runs it.
8. **Parts from the Library,** each pinned by version, commit and SHA-256 (`49g-holding/49GAION-protocol`, `library/README.md`). A part changes only when its pin moves.
9. **Prove it.** Run the conformance scenarios of the Operating Protocol (its section on the event record) on your gateway and core, and one end-to-end acceptance run. Until both pass, say "unverified" (Standard §1.8).
10. **Keep a record.** Every change is a new version with a decision record, never an edit of a decided text; your releases carry tags.

Powered by 49GAION
