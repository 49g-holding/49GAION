# HOAC register (49GAION level)

## Unit register

The single unit register of 49GAION itself, and the form every `[ORG]AION` uses for its own (Standard §4.4). One entry per AIOC, Pod or Cell. The register is append-only: entries are never edited or deleted; a retired entry stays, marked "Retired", and its code is never reused. A change of filler or of parent is a recorded event on the existing entry, never a new entry.

Write rights are split: `[ORG]AIOC-OCO` writes the records of AI Cells; `[ORG]HOAC-TM` writes the records of human Cells. Access opens only for an active, filled Cell whose filler has passed the seat's fixed test, and closes automatically when the filler changes or the Cell is retired. Within a Pod access does not pool. When one person fills several human Cells, each signature is recorded with that Cell's code, and dual approval by the same person is flagged.

An empty seat returns accountability to whoever delegated it, suspends any AI authority tied to it, and fails every Human Floor test bound to it (Standard §4.1, §1.5).

## Entries

| Seat | Code | Kind | Type | HOAC | Parent | Filler | Filler kind | Delegated by (and scope) | Date | Record | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 49GAION owner | none (49GAION-level seats take no code) | CELL | Human Seat | GOV | none | Iman Tajik (Founder) | human | Owner of 49GAION (constituting authority) | 2026-10-11 | `49GAION/DR-0001` | Filled |

## Events

| Code or seat | Event (filler change, parent change, retirement; `connected` or `disconnected` for an external port) | From | To | Approved by | Date | Record |
|---|---|---|---|---|---|---|

Columns: **Seat** (name of the seat), **Code** (the fixed code of the AIOC, Pod or Cell; Naming Standard R14, R15), **Kind** (AIOC, POD, CELL), **Type** (the card type, from the organisation's open list), **HOAC** (GOV, TM, ACS or none), **Parent** (the code of the part that holds it, or `none` at the top), **Filler** (person, agent, or "empty"; for a Pod or AIOC, "none"), **Filler kind** (human or AI), **Delegated by** (the seat that delegated it, and what was delegated), **Date** (from), **Record** (decision record and quote ID), **Status** (Filled, Empty, Active, Retired).
