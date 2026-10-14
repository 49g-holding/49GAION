# DR-0010 · 49GAION — fifty-five mechanisms adopted from practice

- **Date:** 2026-10-14
- **Decided by:** the governing seat (GOV) of 49GAION (holder in the private holders register)
- **Source:** the direction of the governing seat (GOV) of 49GAION of 2026-10-14, on a report of the mechanisms found in the working practice of a pilot organisation's engineering AIOC (source key `SRC-ENG-MECHANISMS-2026-10-14`, `references/SOURCE-KEYS.md`; frozen copy `ARC-0001` of 2026-10-14 in the pilot organisation's private archive), read in full against 49GAION v1.5.0
- **Number:** DR-0010. This number is final. DR-0009 is the supplement to DR-0008, merged before this record.

## Decision

1. **Adopted.** Fifty-five mechanisms are adopted into 49GAION. Each is framework-level, of the same kind as the Cell, the Pod, the Chief of Staff, the Office, the Work Item and the stop door, and usable by any AIOC of any organisation in any field. Mechanisms particular to one organisation stay in that organisation's `[ORG]AION`.

2. **Where they sit.** Rules go in the Standard. Working mechanisms go in the Operating Protocol, with their schemas, fixtures and Library part cards. The AIOC matters go in the AIOC definition and its blueprint template. Capabilities keep plain names and take no code (Naming Standard R3).

3. **The Standard.** The following items are added, each marked "(DR-0010)":
   - §1.5: sensitivity class;
   - §1.7: items 14 and 15 (assignment, temporary parts);
   - §2.1: items 11 to 13 (intake from failures, reversal triggers, the Reserve);
   - §2.4: items 7 to 9 (measures that cannot be gamed, rule promotion, advice from several providers);
   - §3.2: items 10 to 15 (discriminating evidence, check placement, silence is failure, fresh instance and duty carriage, verification by a non-author, the mechanism register);
   - §4.1: items 13 to 15 (load and coverage, signature referral, the human-point contract);
   - §4.3: items 9 to 11 (graded pause, planned halt, fenced cut-off);
   - §4.4: items 14 to 19 (tighten freely and loosen only signed, restricted partition, signers by risk label, standing action class, custody and disposal, harm precedence and soft containment);
   - §5.1: items 8 and 9 (runtime contract and engine binding, spend);
   - §5.2: the windowed position, the delegation ladder, completed staff work, the assistance contract, the duty deputy and the intent envelope;
   - §6.1: items 7 and 8 (the signing pack, a chat as a Panel view);
   - fourteen glossary rows.

4. **The Operating Protocol.** The Protocol gains the working form of these mechanisms:
   - the coordination log and leases;
   - move-on and stub debt;
   - the stuck-item watchdog and the loop breaker;
   - the dispute exit;
   - the decision request;
   - the readiness verdict, validate before show and the two-party line;
   - the receivability check;
   - zero-cost wake and the delegation ladder in `unattended_action`;
   - the evidence class, the verdict record, the completion ladder, staleness and source precedence;
   - the runtime contract and spend;
   - the fresh-instance test, the deterministic executor and check placement;
   - a records section;
   - the halt, the pause and the cut-off at work;
   - the class signature.

   Its schemas and fixtures change to match:
   - the verdict record and the standing action class get new schemas;
   - the Work Item and the unit card get optional fields.

   Four Library part cards are added: the duty deputy, the outside inspector, the advisory council and reference comparison.

5. **The AIOC definition and template.** The standard capabilities, the Cell and Pod definitions and the template carry the AIOC parts of the same mechanisms. The template gains Configuration rows for their values.

6. **Seven readings and changes.** The governing seat decided seven points:
   - (a) **Recommendation and the assistance contract.** A Chief of Staff recommends on routine decisions. For a decision of a listed type, or of the highest sensitivity class, the assistance contract governs and no pick or score sits on the item.
   - (b) **The dispute exit.** At the bounce limit, a dispute in a class the `[ORG]AION` names as sensitive goes to the accountable human with a recommendation. Any other dispute may proceed labelled disputed. An objection held by a human is never passed.
   - (c) **A chat as a Panel view.** A chat may be a Panel view for reading and unsigned writes only. It is never the route of an HU port, a stop door, a signature prompt or the accountability path.
   - (d) **Disposal.** Disposing of records or data is the new listed type `dispose-records-or-data`, added to the signature file (item 7).
   - (e) **Lifting a hold.** A hold that a human placed is lifted only by a human seat. A hold on a part or its work is lifted with `restart-stopped-unit`; a containment hold on a resource, a flow or an outside effect, which stops no part, is lifted with `restore-or-rollback` (Standard §4.3, item 9; §4.4, item 19).
   - (f) **Class signature.** A standing action class is signed once, for reversible actions only, as the new listed type `sign-standing-action-class`, added to the signature file (item 7). It never covers `commit-money`, `grant-or-widen-access` or a type bound to HF-01, HF-02 or HF-15.
   - (g) **Model change.** A model change within the tier the seat signed re-runs the fixed test. A change of tier, or below the floor, is `change-filler`.

7. **The signature list.** This decision adds two decision types to the signature file `upstream/human-floor-signature-types.json`:
   - `sign-standing-action-class` (HF-11, related HF-03), added;
   - `dispose-records-or-data` (HF-06, related HF-17), added.

   The file's `standard` field cites them as "items 17 and 18 (DR-0010)". Every existing type is kept unchanged.

8. **Version.** The texts sit on main under the unreleased `v1.6.0`. The version labels and `state.json` stay at `v1.5.0` until GOV releases. Any CI check for these rules goes in its own `.github` pull request, and becomes required only after it runs green on main.

Powered by 49GAION
