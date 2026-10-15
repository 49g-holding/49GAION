# DR-0011 · 49GAION — the Position Principle, HOAC Arrangement Models and the holder Chief of Staff acting with approval

- **Date:** 2026-10-15
- **Decided by:** the governing seat (GOV) of 49GAION (holder in the private holders register)
- **Source:** the direction of the governing seat (GOV) of 49GAION of 2026-10-15
- **Relation:** supersedes one line of DR-0010 (item 6 below). DR-0010 stays as merged and in force in every other part.
- **Number:** this record takes the next free number at merge, after DR-0010

## Decision

1. **Position Principle.** A HOAC is always defined as a position, never a person, everywhere: in the Blueprint, in the engine and in the naming rule. Every field that points to a human seat takes a position code only.
   - Who held each position at each moment is recorded, and that history never moves.
   - When the occupant changes, everything the position carries (effects, achievements, losses, commitments and open work) passes in full to the new occupant.
   - The accountability record of who held the position when stays as history.

2. **Arranging power.** Assigning occupants to positions is an option managed by `[ORG]HOAC-TM` under `[ORG]HOAC-GOV`.
   - TM arranges the positions below it.
   - GOV arranges TM and sets its limits.
   - GOV is set by the organisation's founding configuration.
   - No position arranges itself.
   - TM may test arrangement models over periods; its fixed duty is a complete record.

3. **HOAC Arrangement Models.** An open list of named options. A model is not a unit and carries no code. Organisations configure the models they use; the Standard fixes only the shape.
   - **Solo Model:** one person holds every HOAC position.
   - **Team Model:** a team holds a position and decides by its own recorded rule.
   - **Tiered Model:** teams in levels, under a higher team.
   - **Hybrid Model:** some positions are held by individuals and others by teams, in different scopes at once.
   - **Self-Arranging Model:** a team designs and tests its own internal arrangement within the scope TM gives it.

4. **Register entry labels.** In the append-only unit register (DR-0004; Standard §4.4) four entry labels are added. They are labels of entries, not units.
   - **position:** a position and its code. It contains no people and may be public.
   - **arrangement:** the model and arrangement in force for a position. It contains no people and may be public.
   - **occupancy:** who holds a position, by internal person ID. It stays in each organisation's private register copy and never in a public repository.
   - **handover:** a change of occupant, by internal person ID, listing what passed to the new occupant. It stays in the private register copy and never in a public repository.
   - Each signed decision is stamped with the position code and the occupant ID or IDs at that moment.
   - Occupancy entries carry a valid time and a recorded time. A correction is a new entry; no entry is edited.

5. **Where it sits.** The Standard (§5.2), the Operating Protocol and the AIOC definition and template carry these rules, each marked with this record or with the dated direction of 15 October 2026 until this record is on main.

6. **Holder Chief of Staff acting with approval.** This item supersedes only the line "It never signs for the holder" of the holder Chief of Staff rule (DR-0010, Decision item 3; Standard §5.2).
   - The Chief of Staff never acts on its own.
   - With its position's approval, given per action or as a standing grant with a set scope and end date, revocable, and checked and logged at the tool gateway, it may act, including signing, up to what the position allows, as assistant and executive assistant.
   - Types in `upstream/human-floor-signature-types.json` still need the position's own human signature.
   - The DR-0010 file stays unchanged.

7. **Provenance.** The Holder Chief of Staff rule (DR-0010, Decision item 3) was added before merge on instruction of 15 October 2026; it is new content, not a correction.

8. **Version.** The texts sit on main under the unreleased `v1.6.0`. The version labels and `state.json` stay at `v1.5.0` until GOV releases. Any CI check for these rules goes in its own `.github` pull request and becomes required only after it runs green on main.

Powered by 49GAION
