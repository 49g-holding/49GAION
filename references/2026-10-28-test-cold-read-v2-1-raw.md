# TEST-COLD-READ v1 · the complete definition `v2.1.0` · raw record · 28 October 2026

The test of `references/2026-10-25-test-cold-read.md`, run again on the complete definition `v2.1.0` (`49GAION-FRAMEWORK.md` at hub `main` `3411749`, DR-0048) before its release, as DR-0048, item 10, requires. Run by the AI hub through the station's reviewer relay, 07:40 to 07:50 UTC.

## How it was run

- **The text.** The body of the definition, Parts A to F. The annex "Superseded wording, by version" was left out, as wording no longer in force.
- **Readers.** Three engines from three providers, each cold, in one round, with the eleven questions of the test and no other context:
  1. `openai / gpt-6-astra`: the body, verbatim, without its `Sources:` lines;
  2. `claude / claude-opus-5-5`, a fresh instance of the engine that wrote the text: the body, verbatim, with some lists set inline and its `Sources:` lines left out;
  3. `gemini / gemini-4-argon`: a condensed copy of the body (sections 8, 9, 11, 12, 14 to 17 and 20 shortened). This is a deviation from rule 1 of the test, recorded here.
- A fourth reader, `grok / grok-4.7`, was given the verbatim body twice; both calls passed the relay's 60-second limit with no answer.

## Result: PASS

1. **Questions 1 to 9.** Every reader answered each from the text, with section citations. No reader wrote NOT IN THE TEXT for the substance of these questions. The notes marked NOT IN THE TEXT under them name details the text leaves on purpose to AI at the time (thresholds, cadence, the technology) or to the organisation (the mechanism for its human side, §6.2), and evidence of results, which a definition does not hold.
2. **Agreement.** The three readers agree in substance on every question: the product (the organisation's own `[ORG]AION`, starting as one core), the path (Edition Maker, handover, first proposal, mandate, operation), who decides what, positions not persons (§6), the Human Floor, the stop and the gateway, Structural Adaptation, ownership and "Powered by 49GAION", and one framework from a single position to a group (§10.1, §6.3, §12.6).
3. **Question 10.** The risks named: implementation left to AI at the time (left on purpose, §4, Part E); dependence on engines, data, cost and suppliers (answered in part by the gateway, the stop, fixed tests and the challenge rule, §20, and left to the organisation for the rest); human control after the handover (left to the organisation on purpose, "hand over, then let go", §7, §12.3); signature load on humans (answered in part by the dial, §14.3). None is a gap that the definition must close.
4. **Question 11.** Price, contract and timeline; the technology stack and hosting; how an organisation authenticates and staffs its positions (left to its own mechanism, §6.2); the content of the referenced texts (the Standard, the Protocol and the AIOC definition, which hold the detail); 49GAION's liability and dispute resolution. These are commercial matters or texts outside the definition; none is held to belong in the definition. The governing seat may decide otherwise.

## The raw answers
## Reader 1 · openai / gpt-6-astra · 28 October 2026, 07:42 UTC

### 1. What is it, and what does an organisation receive?
49GAION is an organisation-design framework built from interchangeable AI units and human positions, starting from outputs and AI capabilities rather than existing jobs (§§1.1, 1.5, 3). Its product is the organisation's own living `[ORG]AION`, initially delivered as a governance-level core with its first Standard and Blueprint, governance panel, gateway and stop, and access to 49GAION's knowledge and Library—not a finished organisational design or configuration (§§10.5–10.7, 12.2, 13.1; Part E.1).

### 2. What makes it special?
The stated difference is the starting point: design backwards from the output and AI capabilities, adding humans where needed, rather than starting with human jobs and adding AI (§§3, 5). Its organisation-owned `[ORG]AION` continuously designs, configures and proposes improvements instead of delivering a fixed installation (§4). It combines reusable Library parts, common interfaces, structural splitting/merging, and human-controlled authority (§§9, 15.1, 16, 20).

**NOT IN THE TEXT:** evidence that conventional approaches cannot offer these features, or comparative results demonstrating superiority. The text defines its approach; it does not establish exclusive capabilities.

### 3. How does an organisation start?
1. Request enters Edition Maker; intake gathers purpose, governance, outputs, quality, inputs, constraints, resources and success criteria (§10.1–10.4).
2. A human edition engineer supervises; one engine works and two challenge each step (§10.2–10.3).
3. Edition Maker delivers the core, initial rules, gateway and stop. Governance accepts or returns it; acceptance triggers fresh organisation keys and revocation of Edition Maker's keys (§10.5–10.7; Part E.1).
4. Core proposes a small organisation; governance approves before building (§13.2).
5. Governance mandates Top Management (§15.2.3).
6. Top Management builds and runs operations, reporting learning upwards; fixed tests precede unit operation (§§19, 20.6; Part E).

Detailed execution is decided by AI at the time.

### 4. What must exist, what does each do, and who builds it?
- **Actors:** AIOCs contain AI Cells/Pods; human HOAC positions govern, manage and accept accountability. Each position has a Chief of Staff (§§16, 18).
- **Unit machinery:** versioned blueprint, coded control panel, AI-chat back office and API-connected engines (§17).
- **Controls:** external gateway manages credentials and calls; stops revoke credentials and cancel work (§20.2–20.3).
- **Records:** organisation Standard, Blueprint, Library, versioned decisions, owned work items, acceptance tests and call logs (§§8, 14, 20).
- **Builders:** Edition Maker supplies the core and controls; `[ORG]AION` designs; Top Management builds operations (§§12.1, 13.1, 19).

**NOT IN THE TEXT:** named implementers or detailed construction instructions for every component; control-code changes require a party other than the constrained AI (§20.8).

### 5. Who decides what, and what can AI never do?
- **49GAION GOV:** approves its framework artefacts and Library changes (§8).
- **Organisation GOV:** decides purpose, strategy, success measures, risk, capital, design and budget; delegates operations, approves changes and can veto management (§§14.3, 15.2).
- **Top Management:** runs operations within its mandate; requests anything beyond its envelope (§§15.2.3–15.2.7, 18–19).
- **`[ORG]AION`:** designs, proposes, reviews, may reject proposals, and applies approved changes—including bounded standing approvals; never runs operations (§§12.1, 14.3).
- **AI units:** execute within granted authority and the original requester's authority (§20.1, §20.9).

AI cannot hold human positions, accept accountability, grant itself authority, substitute silence for consent, or control its own stop (§§3, 6.1, 7, 20).

### 6. How does a human remain in control and accountable?
Humans act through legal positions: decisions and signatures identify positions, while the organisation's external mechanism assigns people and issues credentials (§6). Every output has human accountability; GOV, TM and ACS mark governing, executive and accountability positions (§§3, 18).

The Human Floor reserves specified responsibilities and powers to humans, including legal accountability, delegation, tests, root keys and stops (§7). Each signature requires fresh live sign-in; standing approval covers only reversible changes without widened access, budget or authority (§§7, 14.3).

External stops revoke credentials, cancel work and require human restart; protected reports bypass AI (§§18, 20.2). After handover, safeguards become the organisation's responsibility and are amendable within law (§§7, 12.3).

### 7. How does it stay current and resize?
The `[ORG]AION` watches new 49GAION Standards, Blueprints and Library material and proposes adoption; governance decides what enters (§12.5). It also writes organisational rules from experience, incorporates Top Management's learning, and records changes, reasons and replaced versions (§14).

Structural Adaptation starts small, with several processes sharing one AIOC. It monitors operational records, proposes splitting out processes that outgrow their unit, and merging when work shrinks. It weighs costs and never merges a part with its checker; a human decides (§15.1).

**NOT IN THE TEXT:** update frequency, quantitative split/merge thresholds, or detailed migration procedures. Detailed methods are decided by AI at the time (§4; Part E).

### 8. What belongs to whom, and when is the label required?
The organisation owns its independent `[ORG]AION`, rules, records and organisational Standard, Blueprint and Library; downloaded Library material remains locally available if 49GAION disappears (§§12.4, 14.1). At handover, 49GAION loses authority and access (§10.7).

Edition Maker belongs to 49GAION, whose GOV controls its central artefacts and Library (§§8, 10.1). Texts use CC BY 4.0; code uses Apache 2.0; names and marks are not licensed (§11.5).

Using even one 49GAION idea or item makes **all** the organisation's products "Powered by 49GAION" under its stated rule, explicitly beyond—not part of—the licence (§11.1–11.5). Contributions are voluntary; working data never enters its Library (§11.4).

### 9. Does it fit one task and a group of companies?
Yes, by definition: every request—from one position with one task to a group of companies—becomes an `[ORG]AION`; size changes, not shape (§10.1).

One person may hold several or all distinct human positions where law permits. Where genuine independence is required, an independent position must provide it, externally if necessary (§6.3). Small operations can keep multiple processes in one AIOC and split later (§15.1).

A group has one group governance seat; companies retain their own governance seats where legally required, and acts are signed by positions of the acting company (§12.6).

**NOT IN THE TEXT:** demonstrated affordability or practical performance at either extreme.

### 10. Is it executable? Three strengths and three risks
It specifies an operational architecture, not demonstrated execution.

**Strongest reasons it could work:**
1. Explicit handover-to-operation sequence and management mandate (Part E; §15.2.3).
2. Versioned components, interfaces and recorded handoffs (§§8, 16–17).
3. External gateway/stops, engine challenges and signed output tests (§20).

**Biggest text-grounded risks:**
1. **Implementation gap:** detailed construction is left to AI. **Unanswered:** no runnable implementation or deployment evidence is supplied (Part E).
2. **AI error and dependency:** data, security, cost and suppliers can constrain AI (§3). **Partly answered:** challenges, tests and controls; no measured reliability (§20).
3. **Human-control failure:** independence, credentials and post-handover safeguards depend on the organisation. **Partly answered:** assignment, conflict and signature rules; no demonstrated enforcement (§§6–7, 15.2.8).

### 11. What would a new organisation ask that this text cannot answer?
- **What will it cost, and how long will delivery take?** NOT IN THE TEXT: prices, estimates or delivery commitments; intake merely collects money/time constraints (§10.4).
- **What exactly must we deploy?** NOT IN THE TEXT: technology stack, infrastructure requirements and installation instructions (§17; Part E).
- **Who provides hosting, support and maintenance?** NOT IN THE TEXT: service arrangements; operational responsibility alone is assigned (§19).
- **How are people authenticated and positions staffed?** NOT IN THE TEXT: the mechanism is expressly left to the organisation (§6.2).
- **Has this worked, and at what quality/cost?** NOT IN THE TEXT: deployments, benchmarks or measured outcomes; only success criteria and testing requirements are defined (§§13.3, 20.6).
## Reader 2 · claude / claude-opus-5-5 (a fresh instance) · 28 October 2026, 07:46 UTC

**1. What it is and what an organisation receives**
49GAION is an organisation design framework for building organisations from interchangeable AI and human parts. It designs live, AI-native organisations (§1.1, §1.3).
The organisation receives its own `[ORG]AION` (§1.2, §10.1). This is an edition whose core is the first AIOC (§13.1, §10.5, Part E.1). The core holds:
- the first version of the organisation's Standard and Blueprint;
- links to 49GAION's Standard, Blueprint and Library;
- the governance panel;
- the gateway and the stop.

It does not receive a finished design (§10.6).

**2. What makes it special**
- **Design starts from the output and from what AI can do.** Humans are added where needed. A conventional organisation starts from people and jobs and adds AI (§3).
- **Human-limit structures are replaced:** one record, continuous work, multi-skill units and one shared queue (§3).
- **It is live, not installed.** The organisation's own `[ORG]AION` designs it and keeps it current (§4).
- **Authority sits with positions, not persons** (§6).
- **The Library is a shared marketplace** (§9).
- **No result counts on one engine alone** (§20.5).

**3. How an organisation starts**
1. The request enters Edition Maker. Intake covers identity, seat, outputs, quality, inputs, musts, money, time and success (§10.4). An edition engineer leads, and on every step one engine works while two challenge (§10.2–3).
2. Handover happens when the seat accepts. New keys are issued and 49GAION's keys are revoked. A rejected edition goes back with reasons (§10.7).
3. The core gives several proposals. The seat approves, or the core re-proposes (§13.2).
4. The seat gives Top Management a mandate (§15.2.3).
5. The Top Management Group builds and runs the operation (§19, Part E).

Existing organisations move output by output (§10.8).

**4. Which parts must exist and who builds them**
- **Core AIOC:** governance root (§13.1).
- **Top Management Group:** operation hub (§19).
- **AIOCs:** made of Cells, Pods and Chiefs of Staff (§16).
- **Per unit:** blueprint, panel and back office (§17).
- **Human positions:** HOAC-GOV, TM and ACS (§18).
- **Tool gateway and stop:** run outside all AI (§20.2–3).
- **Records and fixed tests** (§14.5, §20.6).

Edition Maker builds the core. `[ORG]AION` designs. The Top Management Group builds the operation (§12.1, §19). Gateway and stop changes are made by a party other than the AI they constrain (§20.8).
NOT IN THE TEXT: concrete engines and technology ("decided by AI at the time").

**5. Who decides what**
- **Governance seat:** purpose, strategy, capital, risk, the mandate, the gate, the veto, and approval of rule changes (§15.2.5–7, §14.3).
- **Top Management:** runs the operation within its envelope and requests anything beyond it (§15.2.3, §15.2.6, §18).
- **`[ORG]AION`:** designs and proposes, and may reject alone. It applies changes only with the seat's signature or within the dial. It plans and never runs (§12.1, §14.3).
- **AI units:** act only within granted authority (§20.1).

AI never accepts accountability (§3). It never holds Human Floor work such as signing, the stop, judging tests or granting itself access (§7). It never sits on report routes (§15.2.4).

**6. How humans stay in control**
- **Positions:** authority rests with legal positions, never with named persons. The organisation's own mechanism assigns holders and credentials (§6.1–2).
- **Human Floor:** HF-01 to HF-19 stay human. Organisations may be more human, never less (§7).
- **Stop:** a human port outside all AI. It revokes credentials, and only a human restarts the unit (§20.2). It is never blocked (§20.3–4).
- **Signatures:** every signature needs a fresh live sign-in (HF-10). The gateway requires them (§20.3). Standing approvals cover only reversible, non-widening changes (§7, §14.3).
- **Direct routes:** reports bypass AI (§16, §18). A conflicted seat must recuse (§15.2.8).

**7. Staying current, growing and shrinking**
- **Staying current:** `[ORG]AION` watches 49GAION's Standard, Blueprint and Library and proposes what to adopt; the seat decides (§12.5). Details are re-decided by AI as AI improves (§4), and organisations may upgrade their edition (§11.3). 49GAION itself uses Self-Improvement (§8).
- **Growing and shrinking:** Structural Adaptation proposes splitting AIOCs as work grows and merging as it shrinks. It never merges a part with its checker, and a human decides (§15.1). Growth beyond the envelope goes through the gate (§15.2.6).

NOT IN THE TEXT: review cadence and thresholds.

**8. Ownership and "Powered by 49GAION"**
- **The organisation owns:** its `[ORG]AION`; its Standard, Blueprint and Library as IP; its records and rules; and local copies of Library items. It may close its `[ORG]AION` at any time (§12.4, §14.1).
- **49GAION keeps:** Edition Maker, its own texts, Library and marks. Marks are unlicensed, and 49GAION has no post-handover access (§10.1, §10.7, §11.5).
- **"Powered by":** applies to all products once even one item is used, which in practice is always (§11.1–2).

Texts are under CC BY 4.0 and code under Apache 2.0. The "Powered by" rule is outside the licence; its enforceability is not stated (§11.5).

**9. One person versus a group of companies**
Yes: "the size changes, the shape does not." Every case becomes an `[ORG]AION` (§10.1).
- **One person:** all positions are assigned to that person but stay distinct. Required independence, such as internal audit, comes from outside (§6.3–4).
- **Group of companies:** one organisation with one seat. Company-level seats exist where law requires, and acts are signed by the acting company's position (§12.6).

NOT IN THE TEXT: how a single person affordably covers HF-17 to HF-19.

**10. Is it executable?**
**Strengths:**
- Hard controls sit outside AI: a fail-closed gateway and a stop (§20.2–3).
- Library reuse means work starts at once (§9, §12.2).
- There is a clear mandate and accountability chain (§15.2, §18).

**Risks:**
- **Implementation is left "to AI at the time"** (§4, Part E). Not answered.
- **Engine, cost and supplier dependence.** Partly answered: fail-closed gateway, panel rebuild (§17.3). No sourcing plan.
- **Signature overload on humans.** Partly answered by the dial (§14.3). Signer capacity is not addressed.

**11. What a new organisation would ask that the text cannot answer**
NOT IN THE TEXT:
- price, contract and timeline;
- 49GAION's liability;
- the technology stack and engines;
- data hosting and protection practice;
- how to fill HF-17 to HF-19 cheaply;
- how the edition engineer is engaged;
- default success measures;
- what happens if Edition Maker fails or the seat never accepts;
- the referenced documents (Standard, Naming Standard, Protocol, AIOC definition, `LICENSE.md`), which are absent;
- dispute resolution.
## Reader 3 · gemini / gemini-4-argon · 28 October 2026, 07:48 UTC

**1. What is 49GAION and what does an organisation receive?**
49GAION (AI Operating Nexus) is a framework for designing live, AI-native organisations from interchangeable AI and human parts (§1.1, §1.3). An organisation receives its own `[ORG]AION`—a living core holding its first Standard and Blueprint, a tool gateway, a stop, and open access to the 49GAION Library—which holds the organisation's design and keeps building it (§1.2, §4, §10.5, Part E).

**2. What makes it special?**
Unlike human-native designs that start with people's jobs and add AI, 49GAION starts from the output and what AI can do, adding humans only where needed (§3, §5). It replaces structures built for human limits with one complete record, continuous work, multi-skill AI units, decision-filtering, and one shared work queue (§3). Rather than installing a static system, it gives the ongoing design and configuration of the organisation to its own AI (§3, §4).

**3. How does an organisation start with it, step by step?**
1. **Intake & Edition Maker:** The request (identity, outputs, musts, etc.) is processed by 49GAION Edition Maker, supervised by a human edition engineer using three AI engines (one works, two challenge) (§10.1–10.4, Part E).
2. **Handover:** The governance seat accepts the core, issues fresh gateway keys, and revokes Edition Maker's keys (§10.7, Part E).
3. **First proposal:** The core takes the brief and proposes a small organisation; the seat approves (§13.2, Part E).
4. **Mandate & Operation:** The seat mandates Top Management, which builds and runs the operation (§15.2, §19, Part E).

**4. Which parts must exist, what do they do, and who builds them?**
* **AIOCs (Cells, Pods, Chief of Staff/Offices):** The only unit kind; produces output and brings decisions to humans (§3, §16). Each has a coded interface (panel) and AI chat workspace (back office) built from a versioned blueprint (§17).
* **Human positions (HOAC):** Legal positions (`GOV`, `TM`, `ACS`) that decide, sign, and hold accountability (§1.5, §6.1, §18).
* **Tools/Code:** One tool gateway (logs calls, holds credentials/engines) and the stop (cancels work) (§13.1, §20.2–20.3).
* **Records:** One complete record, shared queue, versioned rules/tests (§3, §8, §14.5).
* **Builders:** Edition Maker forms the core (§10.1, §13.1); `[ORG]AION` designs the organisation (§12.1); the Top Management Group builds the operation (§12.1, §19).

**5. Who decides what, and what can AI never do?**
* **Governance seat (`[ORG]HOAC-GOV`):** Accepts the edition, approves rules/designs, sets purpose, strategy, risk, and capital, mandates or vetoes Top Management, and holds the core's stop (§10.7, §13.1, §14.3, §15.2).
* **Top Management (`[ORG]HOAC-TM`):** Builds and runs the operation within its mandate envelope (§15.2, §18, §19).
* **`[ORG]AION`:** Proposes designs, rules, and Library intakes; rejects proposals (with reason); decides minor, reversible changes within a signed "dial" (§12.1, §12.5, §14.3, §15.2).
* **AI units:** Decide work details at the time and bring decisions to humans (§4, §16, Part E).
* **What AI can never do:** Accept accountability, hold legal personhood, fill a human position, hold the 19 Human Floor duties, run the operation (for `[ORG]AION`), or control the gateway/stop (§3, §6.1, §7, §12.1, §13.1).

**6. How does a human stay in control and accountable?**
* **Positions:** Authority and accountability rest with legal HOAC positions, never AI or named individuals (§1.5, §6.1).
* **Human Floor:** 19 areas (HF-01 to HF-19)—including accountability, oversight, delegating authority, root keys, and final test judging—must remain human (§7).
* **The stop & direct routes:** A code port outside AI reach revokes credentials and cancels work; restarts require human decision (§13.1, §20.2). Stops, objections, and wrongdoing reports bypass AI completely (§13.3, §15.2, §18).
* **Signatures:** The external tool gateway requires a valid human position signature (with a fresh live sign-in, HF-10) for listed decisions, widening authority/budget, or loosening safeguards (§7, §14.3, §20.3–20.4, §20.8).

**7. How does it stay current, and how does it grow or shrink?**
`49GAION Self-Improvement` keeps the framework current (§8). The `[ORG]AION` continuously reconfigures working details as AI improves, watches 49GAION for updates to propose to the governance seat, and writes the organisation's rules from experience (§4, §12.5, §14.1). To grow or shrink, `[ORG]AION` practices Structural Adaptation: starting small with shared AIOCs, watching the record, weighing costs, and proposing to split outgrowing processes into new AIOCs or merge shrinking ones (never merging a part with its checker) for human decision (§15.1).

**8. What is owned by whom, and when is a product "Powered by 49GAION"?**
* **Organisation owns:** Its `[ORG]AION`, its Standard, Blueprint, and Library (its IP), its working data, and full authority after handover (§10.7, §11.4, §12.4, §14.1).
* **49GAION owns:** The framework, Edition Maker, its Standard, Blueprint, Protocol, Library, and its names/marks (§1.2, §8, §10.1, §11.5).
* **"Powered by 49GAION":** Applies to *all* products of an organisation if it uses even one 49GAION item (idea, Library part, blueprint, or Standard), even after upgrading or changing its edition (§11.1–11.3).

**9. Does it fit one person and a group of companies? How?**
Yes; Edition Maker processes every request from a single position with one task to a group of companies into an `[ORG]AION`—size changes, shape does not (§10.1). For one person, that person holds all distinct legal positions under the organisation's human mechanism (where law allows), never called a "one-person organisation" (§6.3–6.4, Part F). A group of companies is one organisation with one group governance seat, plus company-specific governance seats and signing positions where required by law (§12.6).

**10. Is it executable? Three reasons it works, three risks.**
* **Reasons it works:** (1) Clear unit architecture: versioned blueprints building coded panels and API-connected chat workspaces (§17); (2) Coded enforcement: a fail-closed gateway and stop outside AI reach (§13.1, §20.2–20.3); (3) Recorded hand-offs with typed ports and fixed pre-run tests (§8, §16, §20.6).
* **Risks:** (1) AI can be confidently wrong (§3)—*Answered:* 3-engine challenge, fixed tests, human signatures (§10.3, §20.5); (2) AI dependency on data, security, cost, and suppliers (§3)—*Answered:* gateway logs, cost weighing, envelope limits (§15.1–15.2, §20.3); (3) Post-handover abandonment of the Human Floor and safeguards (§4, §7, §12.3, §20)—*Answered:* Acknowledged as the rule ("hand over, then let go", bound only by law), leaving self-amendment as an unmitigated operational risk.

**11. What would a new organisation ask that is NOT IN THE TEXT?**
NOT IN THE TEXT:
1. Commercial terms: What does it cost to use Edition Maker or access the 49GAION Library, and how long does intake-to-handover take?
2. Technical requirements: Which specific AI engines, APIs, hosting infrastructure, or programming languages are required to run the core, panels, and tool gateway?
3. Detailed rules: The actual contents of the Standard, Naming Standard, Operating Protocol, and AIOC definition referenced as external texts (Preamble, §8).

Powered by 49GAION
