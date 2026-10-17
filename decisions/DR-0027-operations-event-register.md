# DR-0027 · 49GAION — The Operations Event Register; Organisation Memory

- **Date:** 2026-10-17
- **Decided by:** the governing seat (GOV) of 49GAION (holder in the private holders register)
- **Source:** the directions of the governing seat (GOV) of 49GAION of 2026-10-17 (translated):
  - on a registry office, through which every incoming and outgoing letter passes so that its origin is known: "extend it as far as possible: every e-mail and letter in and out, the organisation's posts, between the companies, between divisions, between AI units through the hub and the gateway, and the code hosts' merge numbers; every unit with an inbox and an outbox; the history and the living brain of the whole system";
  - "not inside Source Lifecycle: a new AIOC, with a proper name, extended to almost every action. Source Lifecycle covers every need for knowledge and sources; this one covers the live operation, ever more complete, so that it can tell each part what it had and what it lacked";
  - on the reviewed proposal (name, fields of activity, and the boundary "acts, not activity"): "I approve all of it. Do all its work."
- **Review:** three independent reviewers, one each for the role in an `[ORG]AION` and the architecture; governance, data protection and labour law; and product, connectors and name. All three agreed, on one condition: acts, not activity.
- **Relation:** builds on DR-0019 (the Library register), DR-0023 (the work as it runs), DR-0024 (mother repositories) and DR-0025 (Parts and Products). It supersedes nothing. Item 4 is a reading note on DR-0023, item 2.
- **Number:** this record takes the next free number at merge, after DR-0026.

## Decision

1. **The part.** The 49GAION Library holds **49GAION Operations Event Register**, an AIOC part (Standard §3.1, item 13). In an `[ORG]AION` it is `[ORG]AIOC-OER` (Naming Standard R2). Its mother blueprint is written in its own public mother repository, `49GAION-operations-event-register` (DR-0024). Its Protocol section and its part card follow in `49GAION-protocol`. It is also offered alone, as a product of its own (DR-0025).

2. **What it is.** It gives every formal act and crossing of an organisation's units and positions, on any work surface, one number in one append-only, hash-chained register, by reference to where the content lives. From that register it tells each unit and each process what was recorded, linked, answered and sourced, and what was not. It decides nothing, carries nothing and says nothing about a person.

3. **How it works.**
   - **Record, don't carry.** Every item stays in its home: mail in the mail system, code on the code host, Work Items in the shared queue, AI traffic in the gateway log, posts on their platform. The register keeps one entry per crossing: its number, its parties as unit or position codes, its times, a reference to its home, the SHA-256 of its content, and its follow-up state.
   - **The gateway gates; the register records.** "Register first" for a formal outgoing item is a policy of the tool gateway (`change-gateway-policy`). The register never authorises, sends or refuses on merit, so that one AI never both authorises and records the same act (HF-18).
   - **Never in the accountability path, and never blocking.** A stop, revocation, objection, critique, skip report or signature prompt never waits on the register; each is registered afterwards from the gateway log. If the register is down, work goes on and is registered later, marked late.
   - **Every unit has an inbox and an outbox**: Panel views of the entries at its ports. An address is an entity, a unit or a position, never a natural person.

4. **Acts, not activity (reading note on DR-0023, item 2).** "No part watches work" stays in force. Recording the formal acts and crossings of units and positions, by reference and hash, is not watching work.
   - **Watching work** means recording or measuring a person's activity. It covers a sweep of a mailbox or chat, read or response times, presence, recordings of calls, and a count, rate or history of a human position's acts over time. The register does none of these.
   - **AI positions.** Every act of an AI Cell is recorded, as metadata and references; payloads stay hashed at the gateway (§4.4, item 11). A Cell that acts for a holder mirrors a human position (a Chief of Staff, an attached assistant, a duty deputy). Of such a Cell, only the acts that leave the holder's sphere are recorded: Work Items sent, signed actions carried out, formal outgoing items. The exchange between the holder and the Cell is never recorded.
   - **Human positions.** Only their formal acts are recorded. For a human position, the register shows only the live state of its own open items, to that position, and never a measure of it.
   - **Parties.** A party is the Cell code the gateway stamps on an act, or the unit or position that owns the address (a functional mailbox, a formal channel, a Work Item's port); otherwise it reads `not attributed`. The register never receives, holds or infers an identifier of a natural person.
   - **Feedback.** It is given by entity, unit, process and AI Cell. A figure drawn from the acts of fewer human positions than a minimum group size rolls up to the parent unit.
   - **A fixed list.** The register's projections and measures are fixed in its Protocol section. A new one, or a new class or purpose, runs only after a new impact assessment, a decision of `[ORG]HOAC-TM` and the consultation the law requires. The internal-audit line reviews the register's use every year.
   - **This note governs the Operations Event Register.** It changes no other text.

5. **What a human decides.** Before each surface is connected:
   - the scope, by the Cell carrying `[ORG]HOAC-TM`: which surfaces, entities and classes of act count as formal, and for what stated purpose;
   - an impact assessment and a lawful basis per entity, decided by the position that holds data protection (HF-17), never on staff consent;
   - the connection itself, `connect-external-port`.

   Register-first at the gateway is `change-gateway-policy`. Retention and legal hold are decided under HF-01, and disposal is `dispose-records-or-data`.

6. **Beside Source Lifecycle.** Source Lifecycle keeps what the organisation knows; the Operations Event Register keeps what it did. Three things cross between them:
   - an entry a position asks to keep is filed into Source Lifecycle as a source of origin kind `correspondence`, fixed as received;
   - the register's projection of the work as it runs, by role-type and process, is filed as an `export` after its HF-17 decision. It is the producer the activity profile of DR-0023 waits for;
   - work done without a source reaches Source Lifecycle as a gap signal.

7. **The second assembly: 49GAION Organisation Memory.** Source Lifecycle and the Operations Event Register, placed side by side and connected as item 6 says, with one shared test (Standard §3.1, item 14).
   - **Its features.** What the organisation knows and what it did, in one memory.
   - **With Organisation Design and Delivery.** Placed beside the first assembly, it closes the loop of an AI-native operation: the design runs, the register records it, and the next design starts from the record.
   - **Named now, built later.** Its parts are `DRAFT`, `NOT_RUN`.

8. **What changes.**
   - Standard §3.1: items 13 and 14 (new).
   - The terms rows "Operations Event Register / `[ORG]AIOC-OER`", "Register entry", "Formal act" and "49GAION Organisation Memory".
   - The index row.

   After this merges:
   - in `49GAION-protocol`: the Protocol section of the part, its part card and fixed test, the addition to Source Lifecycle, and the Library register rows;
   - in `49GAION-source-lifecycle`: the origin kind `correspondence`;
   - in `49GAION-operations-event-register`: the first mother blueprint.

9. **Version.** Unreleased `v1.6.0`, as DR-0019.

Powered by 49GAION
