# Unit register (file name kept for links)

## HOAC register (49GAION level)

The single unit register of 49GAION itself, and the form every `[ORG]AION` uses for its own (Standard §4.4). One entry per AIOC, Pod or Cell. The register is append-only: entries are never edited or deleted; a retired entry stays, marked "Retired", and its code is never reused. A change of filler or of parent is a recorded event on the existing entry, never a new entry.

Write rights are split: `[ORG]AIOC-OCO` writes the records of AI Cells; `[ORG]HOAC-TM` writes the records of human Cells. An event of a type on the Human Floor signature list (Standard §4.4, item 6), such as granting or widening access or changing a parent, is written only with that seat's signature; `[ORG]AIOC-OCO` cannot write it alone. Access opens only for an active, filled Cell whose filler has passed the seat's fixed test, and closes automatically when the filler changes or the Cell is retired. Within a Pod access does not pool. When one person fills several human Cells, each signature is recorded with that Cell's code, and dual approval by the same person is flagged.

An empty seat returns accountability to whoever delegated it, suspends any AI authority tied to it, and fails every Human Floor test bound to it (Standard §4.1, §1.5).

## Entries

| Seat | Code | Kind | Type | HOAC | Parent | Filler | Current filler kind (column formerly "Filler kind") | Delegated by (and scope) | Date | Record | Status | Signature ID | accountable_to | Entity | Valid from | Valid to |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 49GAION owner | none (49GAION-level seats take no code) | CELL | Human Seat | GOV | none | Iman Tajik (Founder) | human | Owner of 49GAION (constituting authority) | 2026-10-11 | `49GAION/DR-0001` | Filled | | | | | |

## Events

| Code or seat | Event (filler change, parent change, retirement; `connected` or `disconnected` for an external port) | From | To | Approved by | Date | Record |
|---|---|---|---|---|---|---|

**New columns (DR-0007).** Signature ID, accountable_to, Entity, Valid from and Valid to are added without backfill. A blank value in these columns on an entry made before v1.5.0 means "recorded before this rule". The column "Filler kind" is now headed "Current filler kind": it records the kind of the present filler, while the card's `filler_kind` records the kind the seat allows.

## Event types

The register records these events (DR-0007), each with its date, the signature ID where the type is listed, and the record:

- label assigned, moved or removed;
- delegation granted, varied, revoked or expired;
- acting start and acting end;
- absent and returned;
- stopped and restarted;
- filler-kind changed;
- test passed or failed;
- entity changed;
- succeeded-by;
- port connected or disconnected;
- compensating control recorded, reviewed or ended (Standard §4.4, item 12).

## Status and lifecycle state

| Register Status | Schema `lifecycle_state` (Protocol unit card) |
|---|---|
| Active | `joined` or `live` |
| Filled | `live` (a human Cell with a filler) |
| Empty | `designed` or `built` (no filler) |
| Retired (earlier: Ended) | `retired` |
| Replaced | `replaced` |

## Holders

For every entry added from v1.5.0 on, names of fillers are kept in a separate holders register keyed by Cell code, in a private store outside this repository; the unit register carries structure only, and points to that store by its location (Standard §4.4, item 3). The existing GOV row stays as it is.

Columns: **Seat** (name of the seat), **Code** (the fixed code of the AIOC, Pod or Cell; Naming Standard R14, R15), **Kind** (AIOC, POD, CELL), **Type** (the card type, from the organisation's open list), **HOAC** (GOV, TM, ACS or none), **Parent** (the code of the part that holds it, or `none` at the top), **Filler** (person, agent, or "empty"; for a Pod or AIOC, "none"), **Filler kind** (human or AI), **Delegated by** (the seat that delegated it, and what was delegated), **Date** (from), **Record** (decision record and quote ID), **Status** (Filled, Empty, Active, Retired; Ended, the earlier name, equals Retired).
