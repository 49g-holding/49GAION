# DR-0002 · 49GAION v1.1.0 — two hubs, shared Self-Improvement, composition

- **Date:** 2026-10-12
- **Decided by:** the governing seat (GOV) of 49GAION (holder in `registers/HOAC-REGISTER.md`)
- **Source:** board discussion, 2026-10-12, about 02:30 Dubai time

## Decision

1. **Composition.** Any unit, AIOC or HOAC, may be composed of smaller units of either kind, to any depth. From outside, a composite unit is one unit: one card, its ports and its stop door. Every HOAC has a card like an AIOC. This replaces the earlier limit of two levels.
2. **Self-Improvement.** Self-Improvement is not a separate part of an `[ORG]AION`. It is a process shared by humans and AI inside `[ORG]HOAC-TM`, carried out by an AIOC within TM. AI or humans may raise needs; AI prepares proposals; the discussion decides nothing; TM decides, including on changes to `[ORG]AIOC-OCO`. The Self-Improvement AIOC reads logs and test results read-only; they are kept where OCO cannot change or delete them. Any change to the Self-Improvement AIOC, including its tests and data access, needs TM approval, even though it is maintained through OCO. At 49GAION level, Self-Improvement is held by the governing seat (GOV) of 49GAION. No unit approves a change to itself.
3. **The human hub.** `[ORG]HOAC-TM` is the human hub: it decides and orders.
4. **The AI hub.** `[ORG]AIOC-OCO` (Organization Core Office) is the AI hub: every AIOC, at any depth, joins, is fixed, maintained and upgraded through it. It gives no orders on what work is done. OCO sits under TM: its authority comes from GOV through the human hub; TM orders OCO, meets its human needs (approvals, live human input, Human Floor steps) and is its accountable seat. TM and GOV may each stop OCO; a stop by TM comes directly through a human port, never through a Panel that OCO built. Delivery test D-3 and Human Floor test HF-12 cover stopping OCO by TM and by GOV, and refuse any attempt by an AI to restart a stopped OCO.
5. **Stop.** Stopping a unit stops every unit inside it. The stop is enforced outside the unit, so no inner unit can bypass it. A human port never passes through an AI unit.
6. **Bootstrap.** `[ORG]HOAC-GOV` from day one, then `[ORG]HOAC-TM`, then `[ORG]AIOC-OCO`; every other unit enters through OCO.
7. **Naming.** Each unit has one fixed code, never changed when it moves. Its place is the `parent` field of its card and register entry. A change of parent changes authority, so it needs approval by the human seat over that unit; OCO cannot make it alone (Naming Standard R14).
8. **Corrections.** The Standard names seats, not people; holders appear only in the HOAC register. The product is defined once (Standard §1.3, item 1). A derived Standard is identical to the 49GAION Standard or stricter, never contradictory. Every unit has one input and one output of each kind, plus the stop door. Where a Human Floor negative test cannot be automated, it is a recorded human check by the bound seat. The relation between customer ownership and the Library harvest is to be written before the first external customer.
9. **Version.** The Standard, the Operating Protocol and the AIOC definition and blueprint template are `v1.1.0`.

Powered by 49GAION
