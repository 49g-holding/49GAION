# The 49GAION Naming Standard

**Version `v1.6.0` · approved by the governing seat (GOV) of 49GAION.** Part of the 49GAION Standard.

## 1. Purpose and scope

1. **One name per thing, and as few codes as possible.** Every code is a future collision and a future migration. Codes are given only to AIOCs, Pods and Cells, and to the product (`[ORG]AION`). A HOAC label is written `[ORG]HOAC-<TYPE>` but is a label on a card, never a code.
2. **Scope.** The framework (`49GAION`), its product (`[ORG]AION`), 49GAION documents and capabilities, AIOCs, Pods, Cells, HOAC labels, releases and repositories.
3. **Out of scope.** Positions and each organisation's own document series (kept in its `[ORG]AION`). Capabilities take plain names (R3).

## 2. The rules

### R1. 49GAION is the framework; `[ORG]AION` is its product
- `49GAION` is the organisation design framework, written `49GAION`, never "AION" alone. AION stands for AI Operating Nexus.
- 49GAION documents and capabilities are "49GAION [Full Name]" ("49GAION Standard", "49GAION Operating Protocol", "49GAION Self-Improvement"). **They take no code.** "49GAION-SL" is wrong.
- The product of 49GAION is `[ORG]AION`, one per organisation, shown as "`<Brand>` AION, Powered by 49GAION" (for example "Ten AION, Powered by 49GAION").
- 49GAION is the framework itself, not an `[ORG]AION`.

### R2. AIOCs: `[ORG]AIOC-[INITIALS]`
- An AIOC's code is the organisation's prefix, `AIOC`, a hyphen and the initials of its full name: "Source Lifecycle" → `[ORG]AIOC-SL`; "Self-Improvement" → `[ORG]AIOC-SI`.
- Nothing that is not an AIOC may begin with `[ORG]AIOC`.
- Full grammar: `[ORG]AIOC-[MODULE]-[OPTIONAL SUBSCOPE]-R[NNN]`. A subscope is used only for a real specialisation.
- **Reading note (DR-0007).** R[NNN] is a release identifier written beside the code, never part of it (R14). AIOC initials are 2 to 5 upper-case letters.

### R3. Capabilities have plain English names
- Office, Chief of Staff, Executive assistant, Input socket, Panel, and every functional capability an AIOC adds, are capabilities, not units. Their name is the plain English word and nothing else: no code, no prefix, no branding.
- Prose may say whose capability it is: "the Chief of Staff of `[ORG]AIOC-SL`".
- **Addition (DR-0007).** The capability keeps its plain name; the Cell or Pod that performs it has its own code (R15).
- Machine references use two separate fields, never a joined string:
  ```yaml
  aioc: "[ORG]AIOC-SL"
  capability: Chief of Staff
  ```

### R4. Nothing else gets a code
Position codes are entries in a register, never appended to a code. Nothing is appended to a code to show where a part sits or what it belongs to (R14). No code with a hard-coded `49` prefix exists (R13).

### R5. Retired codes are never reused
The codes in §4 are retired and never issued again, for any meaning.

### R6. Check before you name
No new AIOC code is used before the collision check in §5 is done and recorded.

### R7. Versions
- 49GAION texts use semantic version tags: `v<major>.<minor>.<patch>`. The current version of this Standard is `v1.6.0`.
- Blueprint version and deployment release are different dimensions: `v1.4` is not `R003`. A `build_id` is separate from the version.

### R8. Identifiers and display names are separate
The full identifier controls in manifests, records and registers; the display name may be simplified for people.

### R9. Repositories
| Asset | Form |
|---|---|
| AIOC | `<org>aioc-<abbr>`, with `-records` and `-records-restricted` as needed |
| 49GAION hub and companions | `49GAION`, `49GAION-protocol`, `49GAION-aioc` |
| An `[ORG]AION` | named by its organisation, in its own space |
| A code project | the same name as its writing repository |

Names are kept; changing a name is a governed migration. A repository is recorded before it is created.

**Addition (DR-0021).**
1. **Visibility.** The writing repository of an AIOC may be public only when it holds no organisation's data. Its `-records` and `-records-restricted` repositories are never public.
2. **Where it is recorded.** A repository is recorded before it is created, as an event on the AIOC's entry in the unit register, with its name, its visibility and its platform.
3. **Mother and instance.** Where an AIOC's writing repository also holds a Library mother blueprint, the mother holds no organisation's data, and the Library register pins it (Standard §3.1, item 9); the organisation's own values live in its records repository.

**Addition (DR-0024).**
4. **A mother repository.** Where the writing repository of a Library part's first instance holds an organisation's data, the part's mother blueprint lives in its own public repository, named `49GAION-<part>` (the part's name after "49GAION", in lower case, words joined by hyphens), beside the hub companions. It holds the mother only; the instance keeps its private writing repository and names the mother by pin.

### R10. Signed identities never change name silently
An identity migration is a separate governed act. A new asset is born on the R2 grammar.

### R11. Outside text
Outside text names the organisation's `[ORG]AION` or AIOC and adds only "Powered by 49GAION".

### R12. 49GAION capabilities are named by function
At the 49GAION level a capability is "49GAION [Function]" or a plain name, with no code (for example **49GAION Self-Improvement**, **AION Builder**). In an `[ORG]AION` it becomes that organisation's AIOC (`[ORG]AIOC-SI`). 49GAION's own instance keeps its 49GAION name.

### R13. The prefix comes from the organisation's brand; HOAC
1. **Brand-derived prefix.** A code's prefix comes from the brand of the organisation that owns the `[ORG]AION`. Centrally it is written `[ORG]`; the AION Builder fills it. The prefix keeps the brand's registered case; `AION`, `AIOC` and `HOAC` are always upper case. Example for an organisation named Ten: `TenAION`, `TenAIOC-SL`, `TenHOAC-GOV`.
2. **Initials of the unit's own name.** "AI" appears in a code only when it is part of the unit's name.
3. **No hard-coded `49`.** Central texts never use `49` as a code prefix; they write `[ORG]`.
4. **HOAC.** The 49GAION Human Oversight & Accountability Control label is written `[ORG]HOAC-<TYPE>`: `GOV` (Governing Body), `TM` (Top Management), `ACS` (Accountability Seat). "HOAC" is chosen for symmetry with `AIOC`.

### R14. A unit's place is a field, never part of its code
1. Every AIOC, Pod and Cell keeps one fixed code wherever it sits and however deep it is nested. The code never changes when the part moves or its filler changes. This applies within an `[ORG]AION`; 49GAION-level seats, which belong to no `[ORG]AION`, take no code (`registers/HOAC-REGISTER.md`).
2. Its place is the `parent` field of its card and its register entry: the code of the AIOC, Pod or Cell that holds it, or `none` at the top of the organisation.
3. Moving a part changes its `parent` field, never its code. No code is a path, and no code carries a suffix naming its parent or its seat. A subscope (R2) names a specialisation, never a parent.
4. A change of `parent` changes the part's line of authority, so it needs the approval of the human seat over that part; `[ORG]AIOC-OCO` cannot make it alone (Standard §1.7, item 8).
5. *Superseded (DR-0004):* seat codes formed by adding the seat's initials to a HOAC label. Each seat is a Cell with its own code (R15), and the HOAC label is a field on its card.

### R15. Pods and Cells
1. **Pod.** A Pod's code is the organisation's prefix, `POD`, a hyphen and the initials of the Pod's own name, 2 to 8 upper-case letters or digits: "Review" → `[ORG]POD-RV`.
2. **Cell.** A Cell's code is the organisation's prefix, `CELL`, a hyphen and the initials of the Cell's own name, 2 to 8 upper-case letters or digits: "Source Lifecycle Chief of Staff" → `[ORG]CELL-SLCS`; "Top Management Seat" → `[ORG]CELL-TMS`.
3. **One register, one code.** Every Pod and Cell code is unique in the organisation's unit register and passes the collision check in §5 before first use. Retired codes are never reused (R5).
4. **Not the filler.** A Cell's code names the seat, never its filler: a person's name or an agent's name never appears in a code. A person's AI assistants are separate AI Cells, each with its own code, attached to that person's Cell.
5. **Prefix.** Central text writes `[ORG]`; the prefix is filled in each organisation's own `[ORG]AION` (R13).

### R16. The Chief of Staff, written COS (DR-0028)
1. **The short form.** "COS" is the one short form of "Chief of Staff". It may stand for it wherever a short form is needed: in display names, Panels, tables and prose, as "COS of `[ORG]AIOC-DI`" or, in a display name, "COS DI". The capability's name stays "Chief of Staff" (§3); COS names the capability, never a unit.
2. **In a Cell's code.** The Chief of Staff Cell of an AIOC takes the code `[ORG]CELL-COS<initials>`, where `<initials>` are the initials of that AIOC's code: the Chief of Staff Cell of `[ORG]AIOC-DI` is `[ORG]CELL-COSDI`; of `[ORG]AIOC-SL`, `[ORG]CELL-COSSL`. This is the one exception to the initials of R15, item 2. As in R15's own example ("Source Lifecycle Chief of Staff" → `[ORG]CELL-SLCS`), the AIOC's initials are part of the Cell's own name, the AIOC it serves; R14, item 3 is read with this item.
3. **An Office.** Where an Office holds more than one Chief of Staff of the same AIOC, the second and each later one adds a digit: `[ORG]CELL-COSDI2`. Where a code would pass eight characters, the Cell takes its initials under R15, item 2, recorded with the collision check (§5).
4. **Never a unit.** COS never forms an AIOC or a Pod code. `[ORG]AIOC-COS` and the placeholder `{COS}` stay retired (§4).
5. **Codes already issued.** A code never changes in place (R14, item 1). A mother blueprint moves its Chief of Staff Cell to its COS code at its next version: the old code is retired (R5) and recorded in the card's lineage. In an `[ORG]AION`, an installed Chief of Staff Cell moves only by entries in the unit register that retire the old code and issue the new one, under the Standard's rules for creating and retiring a part.

## 3. Capability names

**Reading note (DR-0007).** "A single-function Chief of Staff of the assisting kind" below reads as a connecting agent (Standard §5.2).

| Capability | The only name | Wrong |
|---|---|---|
| A set of agents that analyses the reports and performance of other agents and leads them | **Chief of Staff** | `[ORG]AIOC-COS` |
| What forms when a position needs more than one Chief of Staff | **Office** | `[ORG]AIOC-EO` |
| A single-function Chief of Staff of the assisting kind | **Executive assistant** | `[ORG]AIOC-EA` |
| The 49GAION capability that builds `[ORG]AION` products | **AION Builder** | `[ORG]AIOC-EB` |
| The input check every AIOC has | **Input socket** | `49AIIN`, "External Bridge" |
| The AIOC's operating face | **Panel** | `[ORG]AIOC-PF` |
| The role-card template | **Role card** | `[ORG]AIOC-RC` |
| The register of positions | **Position Register** | `[ORG]AIOC-PR` |

**Reading note (DR-0028).** The short form of "Chief of Staff" is COS (R16). `[ORG]AIOC-COS` stays wrong: COS never names a unit.

## 4. Retired codes

`[ORG]AIOC-EO`, `[ORG]AIOC-COS`, `[ORG]AIOC-EA`, `[ORG]AIOC-RC`, `[ORG]AIOC-PR`, `[ORG]AIOC-EB`, `49AIIN`, `49AIB`, the `CORE` segment for anything new, and the placeholders `{OFFICE}`, `{COS}`, `{EA}`, `{RC}`, `{PR}`, `{IN}`, `{UD}`.

## 5. Collision check for a new AIOC code

The same check applies to a new Pod or Cell code. Before a new code is used, check that it:
1. does not recreate `[ORG]AIOC`, `[ORG]AION` or `49GAION` in its initials;
2. does not match an existing module code in the organisation's register;
3. does not read as a version suffix (`RC`) or a common acronym that misleads (`PR`);
4. is recorded, with the check, before first use.
