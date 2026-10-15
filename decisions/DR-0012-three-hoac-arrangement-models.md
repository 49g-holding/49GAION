# DR-0012 · 49GAION — three HOAC Arrangement Models: Solo, Team and Overseen

- **Date:** 2026-10-15
- **Decided by:** the governing seat (GOV) of 49GAION (holder in the private holders register)
- **Source:** the direction of the governing seat (GOV) of 49GAION of 2026-10-15: "Write only what is really a model and gives a different result; don't add the extras, remove them."
- **Relation:** supersedes only the model list of DR-0011 (Decision item 3). DR-0011 stays as merged in every other part; its file is not changed.
- **Number:** this record takes the next free number at merge, after DR-0011

## Decision

1. **Admission test.** An arrangement model stays only if it changes who decides or the result of a decision. A future model is admitted only under the same test. The list stays open under that test.

2. **Three models.** The HOAC Arrangement Models are:
   - **Solo Model:** one holder decides alone.
   - **Team Model:** several holders hold one position and decide by a recorded signing rule: any one, majority, or all. Every decision records one named accountable member in the decision stamp, filled at signing; that member must be a current occupant of the position. Two holders signing together is a Team setting, not a model of its own.
   - **Overseen Model:** a higher position can stop or override the decisions of a position. It is a link that combines with Solo or Team, and it records a timing form:
     - **pre:** the action waits at the tool gateway until the overseeing position clears it, or until a recorded hold window lapses with no stop;
     - **post:** the action runs, and can be reversed only by a new signed decision that references the identifier of the reversed decision. The original decision stays and is marked reversed.

3. **Overseen rules.**
   - A clearance is a stamped decision: the overseeing position, its occupant ID or IDs and the time.
   - A lapse writes the entry "window lapsed, no stop". A lapse counts only if the overseeing position has a holder at that moment and a window is recorded.
   - If the overseeing position is vacant, the held action escalates to the position that set the arrangement (TM, then GOV) and never passes automatically. Escalation ends at GOV. If GOV is vacant, the action stays held until GOV is filled through the founding configuration.
   - An arrangement in which GOV is overseen by a lower position is rejected; no loop is allowed.
   - The tool gateway marks each tool action reversible or not. An irreversible tool action (a sent message, a payment, a deletion) under the Overseen Model always goes through pre, whatever timing form is recorded.

4. **Occupancy, not models.** A temporary occupant, a backup occupant and a rotation among occupants are occupancy rules, not models: each change is already an occupancy entry (DR-0011, Decision item 4).

5. **Withdrawn.** The other names of the DR-0011 list (Tiered, Hybrid, Self-Arranging, Advised, Matrix, Assisted, Federated, Shadow, Pool, Elected, Paired, Interim, Backup and Rotating, as model names) are withdrawn, not renamed. No old name maps to a new one.

6. **Where it sits.** The Standard (§5.2 and the terms table), the Operating Protocol (§4.10) and the AIOC definition carry these rules, each marked with this record or with the dated direction of 15 October 2026 until this record is on main. Superseded lines stay in place and are marked.

7. **Version.** The texts sit on main under the unreleased `v1.6.0`. The version labels and `state.json` stay at `v1.5.0` until GOV releases. Any CI check for these rules goes in its own `.github` pull request and becomes required only after it runs green on main.

Powered by 49GAION
