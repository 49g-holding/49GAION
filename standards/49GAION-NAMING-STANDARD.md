# The 49GAION Naming Standard

**Version `v1.0.0` · approved by Iman Tajik (Founder).** Part of the 49GAION Standard.

## 1. Purpose and scope

1. **One name per thing, and as few codes as possible.** Every code is a future collision and a future migration. Codes are given only to units (AIOCs and HOACs) and to the product (`[ORG]AION`).
2. **Scope.** The framework (`49GAION`), its product (`[ORG]AION`), 49GAION documents and capabilities, AIOCs, HOACs, releases and repositories.
3. **Out of scope.** Positions and each organisation's own document series (kept in its `[ORG]AION`). Capabilities take plain names (R3).

## 2. The rules

### R1. 49GAION is the framework; `[ORG]AION` is its product
- `49GAION` is the organisation design framework, written `49GAION`, never "AION" alone. AION stands for AI Operating Nexus.
- 49GAION documents and capabilities are "49GAION [Full Name]" ("49GAION Standard", "49GAION Operating Protocol", "49GAION Self-Improvement"). **They take no code.** "49GAION-SL" is wrong.
- The product of 49GAION is `[ORG]AION`, one per organisation, shown as "`<Brand>` AION, Powered by 49GAION" (for example "Nike AION, Powered by 49GAION").
- 49GAION is the framework itself, not an `[ORG]AION`.

### R2. AIOCs: `[ORG]AIOC-[INITIALS]`
- An AIOC's code is the organisation's prefix, `AIOC`, a hyphen and the initials of its full name: "Source Lifecycle" → `[ORG]AIOC-SL`; "Self-Improvement" → `[ORG]AIOC-SI`.
- Nothing that is not an AIOC may begin with `[ORG]AIOC`.
- Full grammar: `[ORG]AIOC-[MODULE]-[OPTIONAL SUBSCOPE]-R[NNN]`. A subscope is used only for a real specialisation.

### R3. Capabilities have plain English names
- Office, Chief of Staff, Executive assistant, Input socket, Panel, and every functional capability an AIOC adds, are capabilities, not units. Their name is the plain English word and nothing else: no code, no prefix, no branding.
- Prose may say whose capability it is: "the Chief of Staff of `[ORG]AIOC-SL`".
- Machine references use two separate fields, never a joined string:
  ```yaml
  aioc: "[ORG]AIOC-SL"
  capability: Chief of Staff
  ```

### R4. Nothing else gets a code
Position codes are entries in a register, never appended to a unit code. No code with a hard-coded `49` prefix exists (R13).

### R5. Retired codes are never reused
The codes in §4 are retired and never issued again, for any meaning.

### R6. Check before you name
No new AIOC code is used before the collision check in §5 is done and recorded.

### R7. Versions
- 49GAION texts use semantic version tags: `v<major>.<minor>.<patch>`. The current version is `v1.0.0`.
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
4. **HOAC.** The 49GAION Human Oversight & Accountability Centre has the code family `[ORG]HOAC-<TYPE>`: `GOV` (Governing Body), `TM` (Top Management), `ACS` (Accountability Seat). "HOAC" is chosen for symmetry with `AIOC`.

## 3. Capability names

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

## 4. Retired codes

`[ORG]AIOC-EO`, `[ORG]AIOC-COS`, `[ORG]AIOC-EA`, `[ORG]AIOC-RC`, `[ORG]AIOC-PR`, `[ORG]AIOC-EB`, `49AIIN`, `49AIB`, the `CORE` segment for anything new, and the placeholders `{OFFICE}`, `{COS}`, `{EA}`, `{RC}`, `{PR}`, `{IN}`, `{UD}`.

## 5. Collision check for a new AIOC code

Before a new code is used, check that it:
1. does not recreate `[ORG]AIOC`, `[ORG]AION` or `49GAION` in its initials;
2. does not match an existing module code in the organisation's register;
3. does not read as a version suffix (`RC`) or a common acronym that misleads (`PR`);
4. is recorded, with the check, before first use.
