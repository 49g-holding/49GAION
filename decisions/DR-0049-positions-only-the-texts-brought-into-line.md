# DR-0049 · 49GAION — positions only: the texts brought into line with the complete definition `v2.1.0`

- **Date:** 2026-10-28
- **Decided by:** the governing seat (GOV) of 49GAION (holder in the private holders register)
- **Source:**
  - DR-0048: the complete definition `v2.1.0`, §1 item 5 and §6. The system recognises two kinds of actor only, AI organised in AIOCs and human positions carrying a HOAC label. No natural person and no person's name is recorded in it. Each organisation's own mechanism, outside the system, decides how its positions are assigned and administered and who holds them.
  - The audit of the texts of 28 October 2026, which found the places that still set the mechanism behind a position.
  - The governing seat's words of 28 October 2026 (translated): "As long as any work of 49GAION remains, we do not go to [the organisation's AION]. Go and set all those works right too."
  - The record is prepared by the AI hub; the governing seat's merge is the decision.
- **Relation:**
  - It carries out DR-0048 in the Standard, the Naming Standard, the unit register form, the Human Floor signature list and the entry texts. The Operating Protocol, the AIOC definition and the Library's mother blueprints follow by their own pull requests, citing this record.
  - It supersedes, where they set the mechanism behind a human position:
    - DR-0007 (acting filler, deputies, the holders register, the decision rule of a body behind a label);
    - DR-0010 (signature referral to a deputy, the holder's backup);
    - DR-0011 (arranging power, occupancy and handover entries);
    - DR-0012 (the Solo and Team models, the occupancy rules);
    - DR-0013 and DR-0015 (the link kept by top management).
  - Those records are frozen and are read with this one.
- **Number:** this record takes the next free number at merge, after DR-0048.

## Decision

1. **Withdrawn from 49GAION: the organisation's own mechanism.** Each item below leaves 49GAION. Its terms stay in the glossary, marked withdrawn. The former wording is listed verbatim in the annex "Superseded wording, by version" of each text.
   - The HOAC Arrangement Models Solo and Team, and the arranging power.
   - The register entry labels `arrangement`, `occupancy` and `handover`, and occupant and person IDs anywhere in the system.
   - The acting filler of a human Cell, and the signature type `appoint-acting-filler`.
   - The deputies of human seats, and signature referral to a deputy.
   - The decision rule of a body behind a label. A HOAC label is held by one position, and the governance seat is a single position.
   - The holders register as a store 49GAION defines.
   - The form of a compensating control for one person behind several positions.
   - "The governance seat appoints Top Management directly", and "GOV appoints the first TM".
2. **Kept, restated by position.**
   - **The Overseen link.** A higher position can stop or override a lower one, pre or post. This is a link between positions. If the overseeing position is empty, the position above it may clear or stop the held action; it never passes automatically.
   - **`succeeded_by`.** A link between positions.
   - **The duty deputy.** An AI Cell.
   - **Two positions, two parties.**
   - **Empty seats.** A seat is filled when the organisation's mechanism has a credential in force for it, and empty when it has none.
   - **Signatures.** A signature is the position's. It is made under its Cell code with the credential the organisation's mechanism issued for it and a fresh live sign-in (HF-10). The tool gateway verifies that credential and stamps the position code and time. It holds no person's identity and no reference to one; any record of who stood behind a signature is the organisation's own, outside the system.
   - **Personal signatures.** A personal signature waits for the seat's own signature. With no answer the action stays held and the hold is raised along the accountability path, where a higher position may stop it; no other seat signs in its place. While the seat is empty, a type it marked personal stays held; the delegating position does not sign it.
   - **Access.** Access opens for an AI Cell whose filler passed its fixed test, or for a human position with a credential in force.
   - **`change-filler`.** It applies to AI Cells.
3. **Independence (HF-19).** Distinct positions are not, by themselves, independent. Where the law or a check needs independence in fact, the governance seat attests it for the organisation's mechanism with its own signature, and the system records the attestation against the position, never the person. Where the law requires two positions to be held by different natural persons, meeting it is the organisation's own mechanism's duty, outside the system.
4. **Position Chief of Staff.** "Holder Chief of Staff" is renamed. Every position that carries a HOAC label has its own Chief of Staff, attached to that position's Cell.
5. **The signature list.**
   - The type `appoint-acting-filler` leaves `upstream/human-floor-signature-types.json`.
   - The floor's removal list under `.github/` named it first, in a pull request of its own. That changed the Standard §4.4, item 6, which had said "with the matching change to `signature-types-floor` in the same PR". The required check `github-separation` makes that impossible, so the two changes go in two steps.
6. **What changes:**
   - `upstream/49GAION-UPSTREAM.md`: the opening; §1.1 items 7, 9 and 10; §1.2; §1.3; §1.5; §3.1; §4.1 items 2, 3, 5 and 10 to 15; §4.2 items 4, 5 and 7; §4.4 items 1 to 6, 11, 12 and 15; §5.1 item 7; §5.2; the glossary; the annex.
   - `standards/49GAION-NAMING-STANDARD.md`: R14, item 4.
   - `registers/HOAC-REGISTER.md`.
   - `upstream/human-floor-signature-types.json`.
   - `README.md`, `49GAION.md` and `CONTRIBUTING.md`.
   - This record, its index row, and one unreleased line in `STATE.md`.
7. **Version.**
   - Unreleased `v2.1.0`, with DR-0048. The labels and `state.json` stay at `v2.0.0`.
   - The Guide (DR-0043) follows at its next version, where it repeats these points.

Powered by 49GAION
