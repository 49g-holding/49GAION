# DR-0029 · 49GAION — The Charter in the Library, with three Pods of shared services

- **Date:** 2026-10-19
- **Decided by:** the governing seat (GOV) of 49GAION (holder in the private holders register)
- **Source:** the direction of the governing seat (GOV) of 49GAION of 2026-10-19 (translated): "Yes, I approve", on the proposal "49GAION Charter, a Library part with three Pods" (Operating Core Office, 18 October 2026). The proposal found four pieces of shared infrastructure whose rules are in the Standard and the Protocol but which have no Library part: the tool gateway, the numbering service, the records home and the shared Work Item queue.
- **Relation:** builds on DR-0007 (the root; the tool gateway held in the Charter), DR-0020 (engines at the tool gateway), DR-0024 (mother repositories) and DR-0026 (Engine Room); it supersedes nothing.
- **Number:** this record takes the next free number at merge, after DR-0028

## Decision

1. **A Library part.** The 49GAION Library holds **49GAION Charter**, the part from which the root AIOC of every `[ORG]AION` is made (Standard §1.7, item 13). In an `[ORG]AION` it is the AIOC `[ORG]AIOC-CH`.
2. **What it holds.** The human Cells that carry `[ORG]HOAC-GOV` and `[ORG]HOAC-TM`, and their Offices, as the Standard already sets; and three Pods of shared services:
   - **Gateway:** the tool gateway (Standard §4.4, item 11; Protocol §4.9), with its signature gate, its engine register (DR-0020), its log, the stop door and the human surface;
   - **Records:** the registry of record types, the one numbering service, the event store that serves every part's record home, the projections and their daily check, and the restricted partition (Protocol §14);
   - **Work:** the shared queue of Work Items with its watchdog (Protocol §4), the routing data (Protocol §6), and wake (Protocol §7).
3. **One of each.** An `[ORG]AION` has one tool gateway, one numbering service and one shared queue. No other part keeps its own. Each part writes only its own records and its own Work Items.
4. **Who changes it.** The Charter is installed and changed only on GOV's signature, never by `[ORG]AIOC-OCO` alone (Standard §1.7, item 13). Its gateway policy changes only under `change-gateway-policy` (§4.4, item 11). `[ORG]AIOC-OCO` writes the mother blueprint and keeps the routing data, and dispatches no work.
5. **With Engine Room.** Engine Room supplies the engines that the gateway binds, and never replaces the gateway (DR-0026, item 3).
6. **Where it sits.** The Standard carries the part in §3.1, item 15, and in the terms table. The Protocol carries it in a section of its own, named for the part, with the part card `library/cards/charter.part-card.json` (`DRAFT`, `last_result` `NOT_RUN`) and its fixed test TEST-CHARTER v1, in a pull request after this merges. Its mother blueprint is written in its own public mother repository, `49GAION-charter` (DR-0024), recorded before it is created.
7. **No text of another part changes.** "The shared queue" and "the tool gateway" in every other part read as the Charter's Work and Gateway Pods.
8. **Version.** The texts sit on main under the unreleased `v1.7.0`. The version labels and `state.json` stay at `v1.6.0` until GOV releases.

Powered by 49GAION
