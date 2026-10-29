# TEST-COLD-READ v1 · the complete definition `v2.2.0` · raw record · 29 October 2026

The test of `references/2026-10-25-test-cold-read.md`, run on the complete definition before the release of `v2.2.0` (`49GAION/DR-0053`, item 7). Run by the AI hub through the station's reviewer relay, 02:45 to 05:54 UTC, in five rounds: the first on the text of `v2.1.1` as prepared, the second and third on corrected drafts, the fourth on the text with DR-0051 written in, the fifth on the text of this release, with the governing seat's ruling of that morning on the Chief of Staff and on the record of the HOAC Assignment Model written in (`49GAION/DR-0053`, items 11 and 12).

**The numbers of the records.** In rounds 1 to 3 the inputs named two records by the numbers they had while they were prepared: the two reviews of `v2.1.0` as DR-0051, and the review room's designs as DR-0052. Between rounds 3 and 4 the governing seat merged another record first, the HOAC Assignment Model, which took DR-0051; the two records then took DR-0052 and DR-0053. The answers below are kept verbatim, with the numbers their inputs carried; this record's own text uses the numbers as merged.

## How it was run

- **The input.** One prompt: the eleven questions of the test, its instructions, and the body of the definition, Parts A to F, with its opening and its test paragraph and without the annex "Superseded wording, by version". Every reader of a round was given the same input, byte for byte; each input is named by its SHA-256 below, and the hash of each prompt as sent was checked against it from the session's own log.
- **Readers.** Four engines from four providers, each cold, with no other context: `openai / gpt-6.1-sol`, `claude / claude-opus-5-5` (a fresh instance of the engine that wrote the text), `gemini / gemini-4-argon` and `grok`. The reply limit was 8,000 tokens, except where noted.
- **Grok.** In rounds 1 and 3 its call passed the relay's 60-second limit with no answer, as on 28 October 2026; it was not asked again in rounds 4 and 5. It gave no answer in this test.
- **The judgment.** A reader's last line is its own verdict and is kept as written. Each point a reader raised is judged below: changed in the text, or not a gap, with the reason. The governing seat may judge otherwise.

| Round | Text | Input SHA-256 |
|---|---|---|
| 1 | the definition `v2.1.1` as prepared, before DR-0051 | `3120408356c1bf212afc2b5cc2d099854913d9a4fc9860ffa0513814f6cbe0f0` |
| 2 | a draft with the first corrections | `3bc391373b648a9628cda4faac51a9cc639c727e5411c1c3964b2d1c1fac2ad2` |
| 3 | a draft with the second corrections | `9f3ad7c21c27a70c133f7e7f155259e0fb2445fa511c186e6f44abe49df08383` |
| 4 | a draft with DR-0051 written in | `ad3c7f10816e859e85d3d6534a133ec1b3d9b262c264b87aa31920075fa31dee` |
| 5 | the definition `v2.2.0` as released, with DR-0053, items 11 and 12, except its test paragraph | `135ae1e6f7fa50f54b4fe865f9cee971495576d8d03543f5cca678e454628dd8` |

The released text differs from the input of round 5 in one place: its test paragraph, which now records this result.

## Result: PASS

### Round 1, on the text of `v2.1.1`

- `openai`: VERDICT COMPLETE.
- `claude`: VERDICT GAPS, four points.
- `gemini`: VERDICT COMPLETE. Its answer was not kept whole: it was lost from the working session before this record was written. The working notes keep its verdict and its question 11: the detailed rules in the other texts, the organisation's own mechanism for its human side, and the owner named in `LICENSE.md`, each outside the definition by design.
- `grok`: no answer within the relay's limit.

The four points of `claude`, judged:

1. **The Chief of Staff's right to sign** read as at odds with HF-10 and with the gateway's human signature. **Changed** (§7, §16): the position signs each grant itself with a fresh live sign-in; a standing grant covers only what a standing approval covers; a listed decision and the work the Human Floor keeps human stay with the position and need its own signature. This is the governing seat's decision of `49GAION/DR-0052` written plainly; the Standard already said it (§4.4, item 8: no bot signs a listed type).
2. **How a request is brought.** **Changed** (§10, item 1): a pointer to the hub's page for an adopting organisation, `ADOPTING.md`.
3. **Who checks success and Top Management's reports.** **Changed** (§13, item 3; §15, capability 2, item 4): a party other than the core, or independent of Top Management, that the governance seat names. The Standard (§1.3, item 1) is brought into line.
4. **49GAION's liability for a faulty edition.** Not a gap: a commercial and legal term, outside the definition; the licence's terms are in `LICENSE.md`.

### Round 2, on the corrected draft

- `gemini`: VERDICT COMPLETE.
- `openai`: VERDICT GAPS, one point: the first contact is set out in `ADOPTING.md`, which was not given.
- `claude`: VERDICT GAPS, six points.

Judged:

1. **What a listed decision is.** **Changed** (§20, item 3): a decision of a type on the organisation's Human Floor signature list, which at the handover holds every type on 49GAION's own list and afterwards changes only by a human approval (Standard §4.4, item 20).
2. **What the founding configuration is.** **Changed** (§10, item 4): fixed with the intake and accepted by the governance seat with the edition; the settings in force from the first day, such as who decides in place of a conflicted seat and how an empty seat is filled (Standard §4.2, item 10; §4.4, item 21).
3. **What happens to the intake's data.** **Changed** (§10, item 7): the raw sources are returned to the organisation and deleted from Edition Maker, which keeps no data of the organisation after the handover; the rule already stood in Edition Maker's requirements.
4. **The terms of what is given back.** **Changed** (§11, item 4): under the licences of item 5, as `CONTRIBUTING.md` already says.
5. **The dial at the handover.** **Changed** (§14, item 3): until the seat has signed a dial there is none, and every change needs its signature; this follows from the dial being a signed standing approval.
6. **How a request is brought,** and **who owns 49GAION.** Not gaps: `ADOPTING.md` and `LICENSE.md` hold them, and the definition points to each.

### Round 3, on the draft with the second corrections

- `gemini`: VERDICT COMPLETE.
- `openai`: VERDICT GAPS, two points.
- `claude`: VERDICT GAPS, four points. Its first call, with a reply limit of 6,000 tokens, was cut off inside question 10 and is kept below as well; the second call, at 8,000, is its answer.
- `grok`: no answer within the relay's limit.

Every reader answered questions 1 to 10 from the text, with section citations, and the three agree in substance on each: the product, the path from the request to the operation, who decides what, positions not persons, the Human Floor, the gateway and the stop, Structural Adaptation, ownership and "Powered by 49GAION", and one framework from a single position to a group. The points raised, judged:

1. **How a request is brought today** (all three). Not a gap: it is operational and changes over time; §10, item 1, points to `ADOPTING.md`, which holds it.
2. **The full list of listed types** (`openai`, `claude`). Not a gap: the definition now says what a listed decision is and what the list holds at the handover; the list itself is a rule in detail and stays in the Standard (`upstream/human-floor-signature-types.json`), as the definition's opening says.
3. **Who verifies the gateway and the stop before they are trusted, and who keeps them after the handover** (`claude`). Not a gap in the definition: the Standard holds it (§1.8, `49GAION/DR-0053`): an implementation is conformant only when its own trace of the conformance scenarios passes the checker, and an `[ORG]AION` is proven only after one end-to-end acceptance run; after the handover the gateway and the stop are the organisation's own (§10, item 7), and any change to them is guarded (§20, item 8).
4. **What happens to the operation when the gateway fails closed** (`claude`). Left on purpose: "if it fails, no AI acts" is the safeguard itself (§20, item 3), a stop is never blocked, and how the organisation recovers is its own and its AI's at the time.
5. **A reading note** (`claude`, the call that was cut off): 49GAION "records" an organisation's own work (§11, item 2) while it keeps no data of the organisation (§10, item 7). Not a conflict: item 2 is about attribution, how a work is shown, not about keeping the organisation's data.

### Round 4, on the text with DR-0051

Before round 4 the governing seat's record DR-0051, the HOAC Assignment Model, was merged into the hub and written into the complete definition (§6, item 4; Part F). Round 4 reads the text with it.

- `gemini`: VERDICT COMPLETE.
- `openai`: VERDICT GAPS, three points.
- `claude`: VERDICT GAPS, six points.

Every reader answered questions 1 to 10 from the text, with section citations, and the three agree in substance on each: the product, the path from the request to the operation, who decides what, positions not persons and the HOAC Assignment Model, the Human Floor, the gateway and the stop, Structural Adaptation, ownership and "Powered by 49GAION", and one framework from a single position to a group. The points raised, judged:

1. **How a request is brought today** (`openai`, `claude`). Not a gap: it is operational and changes over time; §10, item 1, points to `ADOPTING.md`, which holds it.
2. **The full list of listed types** (`openai`, `claude`). Not a gap: the definition says what a listed decision is and what the list holds at the handover (§20, item 3); the list itself is a rule in detail and stays in the Standard (`upstream/human-floor-signature-types.json`), as the definition's opening says.
3. **Evidence that it works in operation** (`openai`). Not a definition matter: the Standard (§1.8, DR-0053) says that a text proves nothing by itself and that every claim reads "unverified" until an implementation's own trace passes and one end-to-end acceptance run is judged.
4. **Who owns 49GAION** (`claude`). Not a gap: §11, item 5, points to `LICENSE.md`, which names the owner.
5. **The range of assignment models** (`gemini`, `claude`). Left on purpose by the governing seat: DR-0051, item 6, makes the assignment protocol future work of the Top Management Group.
6. **Where the record of the HOAC Assignment Model lives** (`claude`). §6, item 4, keeps it in the Top Management Group, as an internal human matter that no AI reads; §1, item 5, says that no person and no person's name is recorded in the system; §6, item 2, places the organisation's mechanism for its human side outside the system. DR-0051 keeps both and says so in its relation to DR-0048. The text does not say in so many words whether that record is part of the system. **Raised to the governing seat;** the AI hub does not change the wording of DR-0051. The seat settled it the same morning: the record is kept on the human half of the Top Management Group (DR-0053, item 12); §6, item 4, now says so, and round 5 reads it.
7. **49GAION's liability for a faulty edition** (`claude`). Not a gap: a commercial and legal term, outside the definition.

### Round 5, on the text of `v2.2.0` as released

Before round 5 the governing seat ruled on the Chief of Staff and on the record of the HOAC Assignment Model (`49GAION/DR-0053`, items 11 and 12), and both were written into the complete definition (§6, item 4; §7; §16; §20, item 3). Round 5 reads the text with them.

- `gemini`: VERDICT COMPLETE.
- `openai`: VERDICT GAPS, two points.
- `claude`: VERDICT GAPS, three points.

Every reader answered questions 1 to 10 from the text, with section citations, and the three agree in substance on each, the Chief of Staff's grant included: a position may give its own Chief of Staff any reach, up to signing a listed decision, and what the Chief of Staff signs under it is the position's own decision. The points raised, judged:

1. **How a request is brought today** (`openai`, `claude`). Not a gap: §10, item 1, points to `ADOPTING.md`, which holds it.
2. **The full list of listed types** (`openai`). Not a gap: §20, item 3, says what a listed decision is and what the list holds at the handover; the list itself stays in the Standard (`upstream/human-floor-signature-types.json`).
3. **The range of assignment models** (`claude`). Left on purpose by the governing seat: DR-0051, item 6.
4. **Where the record of the HOAC Assignment Model is kept before the Top Management Group is formed** (`claude`). Not a gap: §6, item 4, places the record in the organisation's own mechanism for its human side (§6, item 2), which operates outside the system from the start; once the Top Management Group is formed, its human half keeps it.
5. **Concentration of authority, with one person in every position and a Chief of Staff of full reach** (`claude`, `openai`, as a risk). A risk the governing seat took on purpose (DR-0053, item 11), and the text answers it: each grant is signed by the position with a fresh live sign-in and revocable at once (§16); the decision and the accountability stay the position's (§7, §16); the stop and the protected routes never pass through any AI (§16, §20); and where the law or a check needs independence it is held by a position independent in fact (§6, item 3).
6. **Liability, price and service terms** (`claude`). Outside the definition.

**Verdict of the record:** PASS. The one point raised to the governing seat (item 6 of round 4) was settled by the seat (DR-0053, item 12). What 49GAION is, what makes it special, how it is carried out and whether it can be carried out are answered from the text alone by every reader that answered; no point left open is one the definition must close without the governing seat's word.

## The raw answers

### Round 1 · input `3120408356c1bf21…`

#### Reader 1 · openai / gpt-6.1-sol · 02:47 UTC

[openai / gpt-6.1-sol]

1. **What it is and what is received.** 49GAION is a framework for designing organisations from interchangeable AI units and human positions, starting from the required output rather than existing jobs. An organisation receives its own independent, living `[ORG]AION`: initially a governance-level core, its first Standard and Blueprint, its own Library, access to 49GAION’s knowledge, and an installed gateway and stop—not a finished operational design. (§§1, 3, 10, 12–13)

2. **What makes it special.** It starts from outputs and AI capabilities, adding humans where needed, rather than adding AI to human-designed jobs. Its organisation-specific AI continuously designs and updates the organisation instead of installing a fixed design. Reusable parts share cards, typed ports and tests; human accountability and checks remain distinct from AI production. The `[ORG]AION` proposes organisational changes; humans authorise them, and Top Management implements them operationally. (§§3–5, 9, 12, 16, 19–20)

3. **How an organisation starts.**
   1. Submit the request to Edition Maker.
   2. Supply purpose, governance, outputs, quality, constraints, resources and success criteria.
   3. Under a human edition engineer, one engine works and two challenge every step.
   4. Receive the initial core, rules, gateway and stop.
   5. Governance accepts; fresh keys replace all Edition Maker keys.
   6. The core proposes a small organisation; governance approves or requests revision.
   7. Governance mandates Top Management.
   8. Top Management builds and runs operations, with provisional fixed tests ready before work begins.  
   Existing organisations transition output by output. (§§10, 13, 15, 19–20; Part E)

4. **Required parts, functions and builders.** Edition Maker supplies the governance core, initial rules, gateway and stop. The core holds the organisation’s Standard, Blueprint, Library and governance panel; its AI designs and proposes. Top Management’s AIOC builds and runs operations. Every AIOC has a versioned blueprint, coded control panel, AI back office and API-connected engines; Cells and Pods organise its actors. Human positions carry authority and accountability. The gateway enforces permissions; external stops revoke credentials and cancel work. Top Management builds or arranges operational tooling; detailed construction is delegated to AI at the time. Gateway/stop changes require a human signature and a party other than the constrained AI. (§§10, 13, 16–20)

5. **Who decides what.** 49GAION’s GOV approves its framework materials. After handover, the organisation’s governance seat has ultimate authority: purpose, strategy, success measures, capital, risk, mandates and reserved decisions. Top Management decides and operates within its mandate. `[ORG]AION` designs, reviews and proposes; it may reject proposals and apply changes within a signed standing approval. Operational AI units execute granted work. Chiefs of Staff may receive signing authority, but cannot take Human Floor duties. AI cannot hold human positions, accept legal accountability, grant itself authority, perform reserved human decisions or override the external controls. (§§6–8, 12, 14–16, 18–20)

6. **Human control and accountability.** Every output has an accountable human position. Delegation is bounded by mandates and authority ceilings; unclear authority means no action. Reserved approvals require fresh live sign-in, while standing approvals cover only reversible, non-expanding changes. Humans retain root keys, emergency access, stops and final test judgment. The external gateway checks signatures and logs calls; direct reporting bypasses AI. Governance can veto, replace decisions or revoke mandates. Changes preserve the deciding position’s words and reasons; independent checks and conflict procedures constrain governance itself. After handover, maintaining these safeguards belongs to the organisation, within the law. (§§3, 6–7, 14–15, 18, 20)

7. **Keeping current and changing size.** `[ORG]AION` monitors new 49GAION materials and proposes adoption; governance decides what enters. It also learns from operational records and Top Management’s achievements, updating the organisation’s own rules and Library. Structural Adaptation proposes splitting overloaded processes into separate AIOCs or merging shrinking work, weighs costs and preserves separation from checking functions. Humans decide changes, subject to the signed dial for limited reversible changes. Detailed designs evolve with AI rather than being fixed beforehand. (§§4, 12, 14–15)

8. **Ownership and attribution.** The organisation owns its `[ORG]AION`, rules, records and organisation-specific knowledge, retains local copies of acquired Library material, and can continue without 49GAION or close its AION. Nothing is published without its choice or legal requirement; contributions are voluntary and working data never enters the shared Library. Edition Maker remains with 49GAION, which retains its framework and central resources but no post-handover access or authority. Using even one 49GAION idea or element makes all organisational products “Powered by 49GAION” under its stated rule. Texts use CC BY 4.0, code Apache 2.0; names and marks are not licensed. (§§10–12, 14)

9. **One task through to company groups.** Yes: every request produces the same basic form—an `[ORG]AION`—while size changes. A small operation can share processes within one AIOC, and one natural person may hold multiple distinct human positions where lawful; genuinely independent checks still need actual independence. Growth adds nested AIOCs through Structural Adaptation. A company group has one group governance seat, with separate company governance seats where legally required; acts are signed by positions of the company acting. (§§6, 10, 12, 15–16)

10. **Executability, strengths and risks.** Executable in principle; the definition is not evidence of operational performance.

   **Three strengths:** reusable, versioned parts and interfaces; a staged handover-to-operation path with assigned responsibilities; externally enforced authority and evidence-based acceptance. (§§8–10, 13, 17, 19–20)

   **Three risks:**  
   - Confident AI errors: answered with cross-engine challenges, fixed tests and human judgment—not guaranteed elimination. (§§3, 20)  
   - Authority escalation or control failure: answered with external gateway/stops, signatures, guarded code and authority ceilings. (§20)  
   - Human overload, conflicts or weak accountability: answered with mandates, Chiefs of Staff, direct reporting, independent checks and recusals. (§§6–7, 15–16)

   Concrete configurations are deliberately left to the organisation’s AI.

11. **What remains for a newcomer to ask.** No definition-level omission is identifiable. Questions such as “Which models, tools, deployment arrangement, staffing pattern, detailed workflow and organisation-specific tests should we use?” await Edition Maker’s intake and the organisation’s AI by design, with human approval—not missing framework answers. Who occupies legal positions is explicitly governed by the organisation’s external human-side mechanism. Prices and contractual service terms are outside the requested definition. The text supplies an execution model, not a claim that every implementation will succeed. (§§4, 6, 10, 13, 15–17, 19–20)

VERDICT: COMPLETE

#### Reader 2 · claude / claude-opus-5-5 · 02:48 UTC

[claude / claude-opus-5-5]

**1. What it is**
49GAION is an organisation design framework for building organisations from interchangeable AI and human parts. It designs AI-native organisations that are "live", meaning they keep redesigning themselves. An organisation receives its own `[ORG]AION`, the living AION that holds its design and keeps building it. This arrives as an edition handed over by Edition Maker, containing:
- the core (first AIOC), made from the 49GAION Charter part;
- the gateway and the stop;
- the first version of its own Standard and Blueprint;
- its own Library;
- open access to the 49GAION Library.

It receives no finished design or configuration. (§1, §4, §10.5–6, §12, §13.1)

**2. What makes it special**
- **Where design starts.** It starts from the output and from what AI can do, then adds people where needed. Conventional design starts from people and jobs and bolts AI on. (§3, §5)
- **It replaces structures built around human limits.** One complete record, continuous work, multi-skill AI units, AI that brings humans only decisions, and one shared queue. Power-dividing checks stay human. (§3)
- **It is live.** The organisation's own AI designs and updates it, so it does not fall behind like an installed system. (§4)
- **It draws on a growing Library** and uses interchangeable "puzzle" parts. (§9, §16)
- **Only positions are recorded, never persons.** (§1.5, §6)

**3. How to start**
1. Make a request to Edition Maker. A human edition engineer leads, and three engines work every step. (§10.1–3)
2. Intake covers identity, governance seat, outputs, quality, inputs, musts, money, time, success and gaps. (§10.4)
3. The edition is formed: the core, the first Standard and Blueprint, and the gateway and stop. (§10.5, §13.1)
4. Handover happens on the governance seat's acceptance. Keys are reissued and 49GAION's keys revoked. A rejected edition goes back with reasons. (§10.7)
5. The core gives several proposals. Nothing is built until one is approved. (§13.2)
6. The seat gives Top Management a mandate. (§15.2.3)
7. The Top Management Group builds and runs the operation. (§19, Part E)

How someone actually submits the first request (channel, hub address) is NOT IN THE TEXT.

**4. Parts and builders**

| Part | What it does | Who builds it |
|---|---|---|
| Core | Root AIOC: serves the governance seat, holds the rules, panel, gateway and stop | 49GAION, via Edition Maker (§13.1) |
| Gateway | Holds credentials and engines, logs every call, fails closed | 49GAION hands it over; later changes need a signature and a party other than the constrained AI (§20.3, §20.8) |
| Stop | Human port outside every AI | Same as the gateway (§20.2, §20.8) |
| Top Management Group | First AIOC under the core; hub of the operation | The `[ORG]AION` designs it (§12.1); Top Management builds and runs everything operational (§19) |
| Each AIOC | Blueprint, panel (code interface) and back office (AI workspace) | Unit layout is left to AI at the time (§16, §17) |
| Cells, Pods, Chiefs of Staff | Inside AIOCs | As above (§16) |

Who writes panel code is not stated explicitly.

**5. Who decides what**
- **Governance seat:** approves proposals, rule changes and new 49GAION versions. Holds purpose, strategy, measures, risk appetite, capital, the dial, the veto and emergency stop. (§12.5, §14.3, §15.2.2–7)
- **Top Management:** runs the operation within the mandate and envelope. Requests anything beyond the envelope through the gate. (§15.2.3, §15.2.6, §18)
- **`[ORG]AION`:** designs, proposes and reviews. May reject alone. Applies changes only with a signature or within the dial. Plans the operation but never runs it. (§12.1, §14.3)
- **AI units:** act only within granted authority and the original requester's authority. (§20.1, §20.9)

**AI can never:**
- accept accountability;
- hold Human Floor work (HF-01–19), such as granting itself power or holding the stop;
- run a listed decision without a human signature. (§3, §7, §20.3)

**6. Human control and accountability**
- A human position is accountable for every output. (§3)
- Every signature needs a fresh live sign-in. (§7 HF-10)
- The gateway runs listed decisions only with a valid human signature, and fails closed. (§20.3)
- The stop sits outside every AI and is never blocked. Restart is by a human only. (§20.2, §20.4)
- Reports, objections and stops reach humans directly, never through AI. (§15.2.4, §16, §18)
- Chiefs of Staff may order information but never drop or delay it. The raw record stays open. (§16)
- Every rule change is recorded with the deciding position's own words. (§14.5)
- Success is checked by a party other than the core. (§13.3)

**Unresolved:** a Chief of Staff (AI) may be granted the right to sign. This sits uneasily with HF-10 and with the gateway's requirement for a *human* signature. (§16, §7, §20.3)

**7. Staying current; growing and shrinking**
- **Following AI's progress:** details and ways of working are decided and changed by AI at the time, as AI improves. (§4)
- **Following 49GAION's progress:** the `[ORG]AION` watches 49GAION's Standard, Blueprint and Library and proposes what to take. The seat decides. (§12.5)
- **Learning from inside:** anyone may propose changes, and Top Management sends its achievements up so the rules grow from experience. (§14.2, §14.4)
- **49GAION itself** improves via Self-Improvement and pull requests merged by its GOV. (§8)
- **Growing and shrinking:** Structural Adaptation starts small, with processes sharing one AIOC. It proposes splits as work grows and merges as it shrinks, never merging a part with its checker. A human decides each change. (§15.1)
- **Bigger steps:** growing beyond the envelope goes through the gate. (§15.2.6)

**8. Ownership and "Powered by"**
- **The organisation owns** its `[ORG]AION`, its Standard, Blueprint and Library (as its IP), its records and its data. It may stop or close the `[ORG]AION` at any time. Nothing is published unless it chooses or the law requires. (§12.4, §14.1)
- **49GAION keeps** Edition Maker, its own Standard, Blueprint and Library, and its names and marks, which are not licensed. Its texts are CC BY 4.0 and its code is Apache 2.0. Gifts back to its Library are voluntary, and working data never enters. (§10.1, §11.4–5)
- **"Powered by 49GAION":** if an organisation uses even one 49GAION item (an idea, part, blueprint or the Standard), all its products carry the label, even after upgrades. In practice this is always the case. (§11.1–3)

**9. One person to a group of companies**
Yes. Every request goes through Edition Maker and becomes an `[ORG]AION`: "the size changes, the shape does not." (§10.1)
- **One person:** they hold several or all positions under the organisation's own mechanism. The positions stay distinct parties. It is never called a "one-person organisation". Checks that need real independence, such as internal audit, come from outside. (§6.3–4)
- **Small start:** processes share one AIOC. (§15.1)
- **Group of companies:** it is one organisation with one governance seat over the group. A company whose law requires its own governing body gets a seat for that company alone, and every act is signed by the acting company's position. (§12.6)
- **Size:** AIOCs nest to any depth. (§16)

**10. Executability**

*Strongest reasons it can work:*
1. Hard, AI-independent controls: a code gateway that fails closed, an external stop, and signatures. (§20.2–3, §20.8)
2. Starting is cheap: Library reuse and a small first organisation. (§9, §13.2)
3. A clear authority chain with mandate, envelope, gate and veto. (§15.2)

*Biggest risks:*
1. **AI design quality.** Answered: humans decide, outputs are challenged by other engines, fixed tests are required, and success is checked independently. (§13.3, §20.5–6)
2. **Floor erosion after handover.** Left to the organisation on purpose ("hand over, then let go"), within the law. (§7)
3. **Chief of Staff signing authority versus HF-10.** Not resolved in the text. (§16, §7)

**11. What the text cannot answer**
- **How to submit the first request:** the channel or hub address is NOT IN THE TEXT. (§10, §11.5)
- **Chief of Staff signatures:** what a Chief of Staff may sign, given that every signature needs a fresh live human sign-in and the gateway demands a human signature, is NOT IN THE TEXT. (§7, §16, §20.3)
- **Who checks success and reports:** who the "party other than the core" and the independent report checker are is NOT IN THE TEXT. (§13.3, §15.2.4)
- **Liability for a faulty edition:** what 49GAION is liable for if a handed-over edition is faulty is NOT IN THE TEXT.

**Not gaps:** engine choice, hosting and unit layout are left to the organisation's AI on purpose. Price is a commercial term and outside the definition.

VERDICT: GAPS

### Round 2 · input `3bc391373b648a96…`

#### Reader 1 · gemini / gemini-4-argon · 02:59 UTC

[gemini / gemini-4-argon]

**1. What is 49GAION, in two sentences, and what exactly does an organisation receive from it?**
49GAION is an organisation design framework for building live, AI-native organisations from interchangeable AI and human parts. Instead of installing a static system, it gives the ongoing design and configuration of the organisation to AI, while keeping humans in control and accountable. An organisation receives its own `[ORG]AION`—starting with the core AIOC (made from the 49GAION Charter), its governance panel, the one tool gateway, the stop, the first version of its own Standard and Blueprint, and open access to the 49GAION Library. (Sections 1, 3, 4, 10, 12, 13)

**2. What makes it special: what does it do that a conventional way of designing an organisation, or of adding AI to one, does not?**
Conventional design starts from human jobs and adds AI to them, retaining structures built around human limits (tiredness, short memory, limited skills). 49GAION is AI-native and live: it starts from the desired output and what AI can do, adding humans only where needed to cover AI's gaps, hold legal accountability, and govern. Instead of human-centric structures, it uses one complete record, continuous work, multi-skilled AI units, AI that brings humans only decisions, and one shared work queue. Furthermore, it never hands over a finished, static design; the organisation’s own `[ORG]AION` continuously designs, configures, and adapts the organisation as AI improves. (Sections 1, 3, 4, 5, 6, 10)

**3. How does an organisation start with it: step by step, from the first request to a running operation?**
1. **Request & Intake:** The request goes to 49GAION Edition Maker, supervised by a human edition engineer (using three engines: one works, two challenge), to take in the organisation's identity, outputs, musts, and limits.
2. **Handover:** Edition Maker builds and hands over the `[ORG]AION` core, linked to the Library, with its initial Standard, Blueprint, gateway, and stop. The governance seat accepts it, issues fresh gateway keys, and revokes Edition Maker's keys.
3. **First Proposal:** The core takes the governance seat's brief, proposes a small organisation from Library patterns, and the governance seat approves it.
4. **Mandate & Operation:** The governance seat delegates the operation via a mandate to Top Management, whose Top Management Group builds and runs the operation. (Sections 10, 13, 15, 19, Part E)

**4. How is it carried out in practice: which parts must exist, what does each do, and who builds them?**
- **Edition Maker (with human edition engineer):** Builds and hands over the initial `[ORG]AION` core, initial Standard/Blueprint, tool gateway, and stop.
- **The Core (`[ORG]AION`):** Sits at the governance level; designs the organisation in design, keeps its Standard, Blueprint, and Library, and later serves as the central hub of reporting and oversight.
- **Tool Gateway & Stop:** Code running beside the core outside AI's reach; the gateway holds credentials/engines, logs calls, and enforces human signatures; the stop revokes credentials and halts work.
- **Human Positions (`[ORG]HOAC-GOV`, `-TM`, `-ACS`):** Hold authority and accountability; assigned via the organisation's own human-side mechanism.
- **Top Management Group & operational AIOCs:** Each has a versioned blueprint, code panel, AI chat back office, Cells/Pods, and a Chief of Staff. Built in design by `[ORG]AION` and built/run in operation by Top Management. (Sections 6, 10, 12, 13, 14, 16, 17, 18, 19, 20)

**5. Who decides what: the governance seat, Top Management, the organisation's `[ORG]AION`, and the AI units? What can AI never do?**
- **Governance seat (`[ORG]HOAC-GOV`):** Decides purpose, strategy, success measures, human-side mechanism, risk appetite, capital/resource balance, conflicts of interest, and rule/design changes (or sets a standing approval "dial"). Holds veto power.
- **Top Management (`[ORG]HOAC-TM`):** Decides operational matters within its mandate's envelope and builds the operation.
- **`[ORG]AION`:** Designs, proposes changes, and rejects bad internal proposals; applies small reversible changes within the governance seat's dial.
- **AI units / Chief of Staff:** Execute tasks within granted authority; a Chief of Staff may sign for its position only under a signed grant for non-listed, reversible actions.
- **What AI can never do:** Hold legal personhood or accountability, fill a human position, act without granted authority, run the operation (for `[ORG]AION`), block a stop/report, or perform the 19 Human Floor items (e.g., delegating authority, granting AI budget/access, judging final tests, holding root keys/break-glass access, signing listed decisions). (Sections 3, 6, 7, 12, 14, 15, 16, 18, 19, 20)

**6. How does a human stay in control and accountable?**
Every human acts through a legal position (`HOAC`), never as a natural person inside the system, holding accountability for every output. Control is enforced by the Human Floor (19 functions kept strictly human, requiring a fresh live sign-in `HF-10` for every signature) and technical safeguards: a single tool gateway outside AI's reach that fails closed and requires valid human signatures for listed decisions or widening authority; and a non-AI "stop" door on every unit that revokes credentials immediately. Furthermore, reports, objections, and stops have a direct, protected route to human positions that never passes through any AI, and no step relies on a single AI engine without challenge and human-signed fixed tests. (Sections 1, 3, 6, 7, 13, 15, 16, 18, 20)

**7. How does it stay current as AI improves, and how does the organisation grow or shrink over time?**
49GAION stays current through its Self-Improvement process and a growing Library of parts and patterns contributed by 49GAION and participating organisations. The organisation's `[ORG]AION` continuously watches 49GAION’s Standard, Blueprint, and Library for updates, proposing useful upgrades to the governance seat, and records operational achievements from Top Management into its own Library. Over time, the organisation grows or shrinks through **Structural Adaptation**: it starts small with several processes sharing one AIOC; `[ORG]AION` watches the operational record against costs and needs, proposing to split processes into new AIOCs when they outgrow their home or merge them when work shrinks (never merging a part with the part that checks it), with a human position deciding each change. (Sections 4, 8, 9, 12, 14, 15, 19)

**8. What does the organisation own, what stays with 49GAION, and when is a product "Powered by 49GAION"?**
- **Organisation owns:** Its `[ORG]AION`, its own Standard, Blueprint, and Library (as its IP), its operational records, and its working data (which never enters the 49GAION Library; sharing built parts back is optional). After handover, 49GAION has no access or authority.
- **Stays with 49GAION:** The 49GAION framework, Edition Maker, its central Standard, Blueprint, Protocol, Library, and its names and marks (which are not licensed; texts are CC BY 4.0, code is Apache 2.0).
- **"Powered by 49GAION":** Under 49GAION's rule, if an organisation uses even one 49GAION item—an idea, Library part, blueprint, or the Standard—all its products are "Powered by 49GAION", and its `[ORG]AION` is shown as "`<Brand>` AION, Powered by 49GAION". (Sections 1, 8, 9, 10, 11, 12, 14, Part F)

**9. Does the same framework fit one person with one task and a group of companies? How?**
Yes. Every request to Edition Maker becomes an `[ORG]AION`—the size changes, the shape does not.
- **One person with one task:** 49GAION never uses the term "one-person organisation"; instead, the system defines only legal positions, and under the organisation's human-side mechanism, one natural person may hold several or all positions where the law allows. Each position remains a distinct party in the record, and if a check requires factual independence (like internal audit), an outside independent holder is used.
- **A group of companies:** Treated as one organisation with one governance seat over the group. Where company law requires a separate governing body for a subsidiary, that body holds a governance seat for that company alone, and every act is signed by a position of the acting company. (Sections 6, 10, 12, Part F)

**10. Is it executable? The three strongest reasons it can work and the three biggest risks, and whether the text answers each risk or leaves it to the organisation's AI on purpose.**
Yes, it is executable.
- **Three reasons:** (1) It starts from a pre-populated Library of reusable parts/blueprints rather than a blank slate; (2) It starts small and scales organically via Structural Adaptation and mutual panel/back-office coverage; (3) Hard technical boundaries (external tool gateway, fail-closed design, non-AI stop) enforce governance.
- **Three risks & text's response:**
  1. *Confident AI errors or prompt injection:* Answered by the text—"one engine writes, two challenge", human-signed fixed tests on real outputs, and treating outside text strictly as data, never instructions.
  2. *Single-human bottleneck/fatigue:* Answered by the text—standing approval "dials" and Chief of Staff standing grants for reversible, non-widening actions, plus AI filtering.
  3. *Granular workflow and tooling design:* Left on purpose to the organisation's AI at the time, so the system stays live as AI improves. (Sections 3, 4, 7, 9, 10, 14, 15, 16, 17, 20)

**11. What would a new organisation ask that the text cannot answer?**
**NOT IN THE TEXT:** While commercial terms are outside the definition and operational/workflow details are intentionally left to AI at the time, a new organisation would still ask:
1. **Practical onboarding steps:** How to actually submit the initial request and what to prepare first (the text points to an external file, `ADOPTING.md`, in Section 10.1).
2. **Detailed technical specifications and rules:** The exact technical schemas for typed ports, cards, and protocol hand-offs, which the preamble states are kept in external documents (`upstream/49GAION-UPSTREAM.md`, the Naming Standard, the Operating Protocol, and the AIOC definition).
3. **Human-side legal mechanism:** How to legally structure and administer human positions and credentials outside the system, which 49GAION explicitly leaves to the organisation's own mechanism (Section 6.2).
4. **Full licensing terms and owner identity:** Kept in `LICENSE.md` (Section 11.5).

VERDICT: COMPLETE

#### Reader 2 · openai / gpt-6.1-sol · 03:01 UTC

[openai / gpt-6.1-sol]

1. **What it is and what is received.** 49GAION is an organisation-design framework that builds live, AI-native organisations from interchangeable AI units and human legal positions, starting from required outputs rather than existing jobs. An organisation receives its own independent `[ORG]AION`: a governance-level core, initial organisation-specific Standard and Blueprint, Library access, governance panel, tool gateway and stop—not a finished operational design—which subsequently designs and improves the organisation under human approval. (§§1, 3–4, 10, 12–13)

2. **What makes it special.** It starts with outputs and AI capabilities, adding humans where necessary, rather than adding AI to human-designed jobs. The organisation’s own AI continuously designs and reconfigures it instead of receiving a fixed external installation. Interchangeable, tested parts, a shared Library and recorded hand-offs support reuse; structural adaptation proposes splits and mergers as demand changes. Human authority, accountability and independent checks remain distinct from AI production. These are the text’s claimed differentiators, not demonstrated comparisons with every conventional approach. (§§3–5, 8–9, 15–20)

3. **Starting, step by step.**
   1. Submit a request to Edition Maker; **NOT IN THE TEXT:** the actual submission channel and initial adopter instructions are deferred to `ADOPTING.md`.
   2. A human edition engineer supervises intake; one engine works and two challenge each step.
   3. Edition Maker prepares the core, initial rules, knowledge links, gateway and stop.
   4. Governance accepts; fresh keys replace all Edition Maker keys.
   5. The core takes governance’s brief and proposes a small organisation; governance approves or requests revision.
   6. Governance mandates Top Management.
   7. Top Management builds and runs operations; `[ORG]AION` follows results and proposes improvements. (§§10, 13, 15, 19; Part E)

4. **Practical parts and builders.** Edition Maker supplies the core from the Library’s Charter, including gateway and stop. The core holds governance, its panel, and the organisation’s Standard, Blueprint and Library. `[ORG]AION` designs; the Top Management Group builds and operates the approved organisation. Each AIOC requires a versioned blueprint, coded panel, AI back office and fixed test; engines connect through APIs. Human positions have Chiefs of Staff. Typed ports and recorded, tested hand-offs connect parts. Gateway and stop run outside AI; changes require a human signature and a party other than the constrained AI. Detailed arrangements are deliberately decided by AI at the time. (§§8, 10, 13–14, 16–20)

5. **Who decides what.** 49GAION’s GOV approves its framework assets; the organisation’s governance seat holds ultimate authority after handover, setting purpose, strategy, risk, resources and Top Management’s mandate. Top Management runs operations within that mandate. `[ORG]AION` designs, reviews and proposes; it may reject proposals and apply changes within signed standing approval. AI units execute authorised work; Chiefs of Staff may exercise limited signed grants. AI cannot occupy human positions, accept accountability, take Human Floor decisions, enlarge its own authority or bypass human signatures and the external gateway/stop. Governance may veto operational decisions. (§§6–8, 10, 12, 14–16, 18–20)

6. **Human control and accountability.** Every output has an accountable human position. Authority is delegated through recorded mandates; signatures require fresh live sign-in, with narrowly bounded standing grants. Humans retain reserved decisions, root keys, access grants and restart authority. An external gateway enforces permissions and signatures; external stops revoke credentials and cancel work. Raw records remain accessible, and reports, objections and stops reach humans without AI mediation. Independent checks cover reporting, audit and governance conflicts. Natural-person appointments and credentials are administered through the organisation’s own lawful mechanism. After handover, maintaining these safeguards becomes the organisation’s responsibility. (§§3, 6–7, 10, 14–16, 18, 20)

7. **Staying current and resizing.** `[ORG]AION` watches new framework standards, blueprints and Library material, proposing adoption; governance decides, and nothing upstream enters automatically. Internal proposals and operational learning update the organisation’s own rules and Library, with versioned reasons and approvals. Structural Adaptation starts small, sharing an AIOC across processes, then proposes splitting growing processes or merging shrinking ones according to demand, resources and cost. It cannot merge a function with its checker. Humans decide structural changes; Top Management implements and runs them. Detailed methods evolve with AI rather than being fixed beforehand. (§§4, 8–9, 12, 14–15, 19)

8. **Ownership and attribution.** The organisation owns its `[ORG]AION`, rules, records and organisation-specific Standard, Blueprint and Library; downloaded Library material remains locally available. 49GAION retains its framework assets and Edition Maker, but no organisational authority or access after handover. Contributions back are voluntary; working data never enters its Library. Under 49GAION’s stated rule, using even one framework idea or element makes all organisational products “Powered by 49GAION,” including after modification. Texts use CC BY 4.0, code Apache 2.0; names and marks are not licensed. The broader branding rule is explicitly separate from the legal licence terms. (§§8–12, 14)

9. **Small and large organisations.** Yes: every request becomes an `[ORG]AION`; size changes, not the basic shape. One person may hold all legally compatible positions, but positions remain distinct and required independence must be real, using an external holder where necessary. Small operations can share one AIOC; units can later split, merge or nest to any depth. A corporate group has a group governance seat, while companies retain legally required governance bodies and sign acts through positions of the acting company. (§§6, 10, 12, 15–16)

10. **Executability, strengths and risks.** Executable as an architectural specification; deployment success is not established here.

   **Three strongest reasons:** modular, versioned parts with interfaces; a staged handover-to-operation path with named responsibilities; enforceable permissions, tests and external stops. (§§8–10, 13, 17–20)

   **Three biggest risks:**
   - **Wrong or correlated AI judgments:** addressed through cross-engine challenge, real-output tests and human sign-off; effectiveness is not proven. (§20)
   - **Unauthorised action or capture of oversight:** addressed through external controls, authority ceilings, independent checks and direct reporting. (§§15–16, 20)
   - **Poor operational design or costly adaptation:** deliberately left to the organisation’s AI to resolve case by case, under human approval and resource limits. (§§4, 15, 19)

11. **What a newcomer still cannot obtain here.** **NOT IN THE TEXT:** the concrete first-contact route—where or how to submit the initial request and what the adopter must do first. Section 10 explicitly places those instructions in `ADOPTING.md`, which is not supplied. By contrast, the organisation’s eventual structure, tools, configuration and detailed workflows are intentionally assigned to its AI, not missing answers. Its human appointment mechanism is explicitly its own responsibility, with authority and legal constraints specified. Commercial terms are excluded from this assessment. (§§4, 6, 10, 15–19; Part E)

VERDICT: GAPS

#### Reader 3 · claude / claude-opus-5-5 · 03:03 UTC

[claude / claude-opus-5-5]

#### Cold read of the 49GAION definition (v2.2.0)

**1. What it is and what an organisation receives**
49GAION is an organisation design framework for building AI-native, live organisations from interchangeable AI and human parts. AION stands for AI Operating Nexus (§1.1, §1.3).

An organisation receives its own `[ORG]AION`, shown as "`<Brand>` AION, Powered by 49GAION" (§1.2). Concretely, Edition Maker hands over:
- the core AIOC, made from the Library part 49GAION Charter;
- the first version of the organisation's own Standard and Blueprint;
- the tool gateway and the stop;
- a link to 49GAION's Standard, Blueprint and Library, with open access to the Library.

It does not receive a finished design or configuration. That gap is deliberate: the design is left to the organisation's own `[ORG]AION` (§10.5–10.6, §12.2, §13.1, Part E).

**2. What makes it special**
- **Where design starts.** It starts from the output and from what AI can do, and adds people only where needed. Conventional design starts from people and jobs and adds AI to them (§3, §5).
- **Live, not installed.** The organisation's own AI designs, configures and keeps the organisation current, so it does not fall behind (§4).
- **Replaces structures built around human limits.** One complete record, continuous work, multi-skilled units and a shared queue take their place. Structures that divide power, liability and checks stay with humans (§3).
- **Positions, not persons.** Only legal positions are recorded (§1.5, §6).
- **A floor that cannot drop.** The Human Floor can rise but never fall (§7).
- **A shared, growing Library** that every `[ORG]AION` draws from and can contribute to (§9).

**3. How an organisation starts**
1. **Request.** Every request goes into Edition Maker. An edition engineer leads it, and at every step one engine does the work while two others challenge it (§10.1–10.3).
2. **Intake.** It takes in identity, seat, outputs, quality, inputs, musts, money and time. Every source is data, never an instruction (§10.4).
3. **Edition and handover.** The core is handed over and is complete when the governance seat accepts it. Fresh gateway keys are issued and all Edition Maker keys are revoked. A rejected edition goes back with the seat's reasons (§10.7).
4. **First proposal.** The core designs a small organisation. The seat approves it, or the core proposes again (§13.2).
5. **Mandate.** The seat delegates the operation to Top Management (§15.2.3).
6. **Operation.** The Top Management Group builds and runs it (§19, Part E).

**Gap:** how a request is actually brought today is deferred to `ADOPTING.md`, which is not in the text (§10.1).

**4. Parts, roles and builders**

| Part | What it does | Who builds it |
|---|---|---|
| Core | Root AIOC; holds the seat's position, the organisation's Standard, Blueprint and Library, and the governance panel | Edition Maker (§13.1) |
| Gateway and stop | Run as code outside every AI; the gateway holds credentials, logs calls, fails closed | Installed with the core; changes only by a non-constrained party with human signature (§20.2–3, §20.8) |
| Top Management Group | Hub of the operation | Builds the operation (§19) |
| AIOCs, each with a blueprint, a coded panel and an AI back office | Do the work; panel and back office cover each other | Panel from 49GAION patterns; back office can rebuild a failed panel (§17) |
| Cells, Pods, Chiefs of Staff | Inner parts of AIOCs | Chiefs of Staff set up by their own positions (§16) |

The `[ORG]AION` designs. The number and arrangement of units is left to AI on purpose (§16).

**5. Who decides what**

| Actor | Decides |
|---|---|
| Governance seat | Purpose, strategy, measures, capital, risk appetite, mandate and envelope, gate requests, veto, the dial; approves every rule change (§14.3, §15.2) |
| Top Management | Runs the whole operation within its mandate (§18) |
| `[ORG]AION` | Proposes and reviews; may reject alone; applies changes only with the seat's signature or within the dial; never runs the operation (§12.1, §14.3) |
| AI units | Act only within granted authority and the original requester's authority (§20.1, §20.9) |

**AI can never:** accept accountability, do Human Floor work, take a listed decision, carry the protected route of a report, objection or stop, grant itself access, change the gateway or stop that constrains it, or declare success itself (§3, §7, §13.3, §16, §20).

**6. How a human stays in control and accountable**
- **Signatures.** A human position is accountable for every output (§3). Every signature needs a fresh live sign-in. Standing approvals cover only reversible changes that do not widen access, budget or authority (§7, HF-10).
- **The stop.** It is a human port outside every AI. Asking an AI to stop is never the stop (§20.2).
- **The gateway.** It fails closed, but never blocks a stop (§20.3).
- **Tighten and loosen.** Tightening is free; loosening needs a signature (§20.4).
- **Direct routes.** Reports, objections and stops bypass all AI (§15.2.4, §18).
- **Chiefs of Staff.** They never drop or delay anything, and the raw record stays open to their position (§16).
- **Evidence and checks.** Done means visible evidence (§20.6). Reports are checked independently (§15.2.4). Conflicted seats are handled as set out in §15.2.8.
- **Records.** Every rule change records the deciding position's own words, the reason and the version replaced (§14.5).

**7. Staying current, growing and shrinking**
- **Following 49GAION.** The `[ORG]AION` watches 49GAION's Standard, Blueprint and Library for new versions and proposes what to take. Nothing enters without the seat's decision (§12.5).
- **Learning from operation.** Details and ways of working are decided by AI at the time and change as AI improves (§4). What Top Management learns in operation flows into the organisation's rules (§14.4).
- **Growing and shrinking.** Through Structural Adaptation, the organisation starts small with processes sharing one AIOC, then splits AIOCs when processes outgrow them and merges them when work shrinks. Costs are weighed, and a part is never merged with the part that checks it. A human position decides each change (§15.1).
- **Growth beyond the envelope** goes through the gate (§15.2.6).

**8. Ownership and "Powered by 49GAION"**
- **The organisation owns:** its `[ORG]AION`, its Standard, Blueprint and Library, which it treats as its IP, and its records and rules. It may stop or close the `[ORG]AION` at any time (§12.4, §14.1).
- **49GAION keeps:** the framework, its own Library, and its names and marks, which are unlicensed. It retains no access after handover (§10.7, §11.5).
- **Licences.** The texts are CC BY 4.0 and the code is Apache 2.0 (§11.5).
- **"Powered by 49GAION"** applies to all of an organisation's products if it uses even one 49GAION item: an idea, a Library part, a blueprint or the Standard (§11.1–11.3).
- **Contributions** to the Library are voluntary, and working data never enters it (§11.4).

**Gap:** the licensing or ownership terms of what an organisation gives back are not stated.

**9. One person with one task versus a group of companies**
Yes, the same framework fits both. Every request, from a single position with one task to a group of companies, becomes an `[ORG]AION`: the size changes, the shape does not (§10.1).

- **One person.** That person may hold several or all positions where the law allows. The positions stay distinct parties, and 49GAION never calls this a "one-person organisation". Where a check needs independence, it comes from outside the organisation (§6.3–6.4).
- **A group of companies.** It is one organisation with one governance seat. A company whose law requires its own governing body gets a seat for that company alone, and every act is signed by a position of the acting company (§12.6).

**10. Executability**

*Three strongest reasons it can work:*
1. Its controls are code outside AI: a gateway that fails closed, a human stop, and an authority ceiling (§20).
2. It starts small by reusing the Library rather than designing from nothing (§9, §13.2).
3. It works through existing law: legal positions, accountability and the Human Floor (§6, §7).

*Three biggest risks:*
1. **AI designs badly or is wrong with confidence.** Answered by challenge from other engines, fixed tests and human signatures (§20.5–6). The design detail is left to AI on purpose.
2. **One person holding every seat weakens checks.** Answered by requiring independence in fact and a conflict rule (§6.3, §15.2.8).
3. **After handover the organisation may loosen safeguards.** Deliberately accepted: "hand over, then let go", bounded only by law (§7, §20).

**11. What a new organisation would ask that the text cannot answer**
NOT IN THE TEXT:
- How to actually submit a request and whom to contact. This is deferred to `ADOPTING.md` (§10.1).
- What counts as a "listed decision", who sets the list, and where the "founding configuration" comes from. Both are used in §7, §16, §15.2.8 and §20.3 but never defined.
- What happens to intake data at Edition Maker after handover. Only keys are said to be revoked (§10.7).
- The terms governing contributions to the Library.
- Who owns 49GAION. This is deferred to `LICENSE.md`.
- The dial's default setting at handover.

VERDICT: GAPS

### Round 3 · input `9f3ad7c21c27a70c…`

#### Reader 1 · gemini / gemini-4-argon · 03:07 UTC

[gemini / gemini-4-argon]

**1. What is 49GAION, in two sentences, and what exactly does an organisation receive from it?**
49GAION is an organisation design framework for building live, AI-native organisations from interchangeable AI and human parts (1, 3, 4). Rather than delivering a finished design, it gives the design and ongoing configuration of the organisation to AI, while keeping accountability and authority in human legal positions (3, 4, 6). 

An organisation receives its own independent `[ORG]AION`—specifically, the core (its first AIOC at the governance level), made from the 49GAION Charter (10, 12, 13). This handover package includes the first version of the organisation's own Standard and Blueprint, the governance panel, the tool gateway and the stop (running as code beside the core), and open access to the 49GAION Library (10, 12, 13, Part E).

**2. What makes it special: what does it do that a conventional way of designing an organisation, or of adding AI to one, does not?**
Conventional human-native organisations start from people and their jobs and add AI to them, retaining structures built around human limits like tiredness, short memory, and limited skills (3). 49GAION is AI-native: it designs backward from the desired output and what AI can do, adding humans only where needed for legal accountability, oversight, and covering AI gaps (3, 5). It replaces human-limited structures with one complete record, continuous work, multi-skilled AI units, AI that brings humans only decisions, and one shared work queue (3). Furthermore, instead of installing a static system designed elsewhere that quickly falls behind, the organisation's own `[ORG]AION` designs, configures, and continuously adapts the organisation live as AI improves (3, 4, 15).

**3. How does an organisation start with it: step by step, from the first request to a running operation?**
1. **Request & Intake:** The request goes to 49GAION Edition Maker (led by a human edition engineer, using a three-engine challenge at every step) to take in the organisation's purpose, outputs, musts, and founding configuration (10, Part E). Existing organisations start from how they work today and move to AI-native output by output (10).
2. **Handover:** Edition Maker forms and hands over the `[ORG]AION` core, gateway, stop, and initial Standard/Blueprint; the governance seat accepts it, issues fresh gateway keys, and 49GAION deletes its raw data and revokes its keys (10, 13, Part E).
3. **First Proposal:** The core takes the governance seat's brief and proposes a small initial organisation; the seat approves (13, Part E).
4. **Mandate & Operation:** The governance seat delegates the operation via a mandate to Top Management, whose Group builds and runs the operation (15, 19, Part E).

**4. How is it carried out in practice: which parts must exist, what does each do, and who builds them?**
- **Edition Maker** (belongs to 49GAION) builds and hands over the **core** (first AIOC, holding the organisation's Standard, Blueprint, Library, and governance panel) alongside the **tool gateway** (holds credentials/engines, logs calls, enforces signatures) and the **stop** (human port to revoke credentials/cancel work), both made from the 49GAION Charter (10, 13, 20).
- **The `[ORG]AION`** builds the organisation *in design*, proposing rules and structural changes, and later serves as the oversight hub (12, 13, 14).
- **The Top Management Group** (first AIOC under the core) builds and runs everything *in the operation* (12, 19).
- **AIOCs** (built from **Cells** and **Pods**, led by a **Chief of Staff**) have a **panel** (code interface) and **back office** (AI chat workspace) built from a versioned **blueprint**, taking and personalising parts from the **Library** (9, 16, 17).
- **Human positions** (`HOAC-GOV`, `-TM`, `-ACS`) are assigned via the **organisation's own mechanism** (6, 18).

**5. Who decides what: the governance seat, Top Management, the organisation's `[ORG]AION`, and the AI units? What can AI never do?**
- **Governance seat (`[ORG]HOAC-GOV`):** Top authority. Accepts the edition, approves organisational designs, rule changes, and new 49GAION versions, sets the dial (standing approval), delegates the operation via mandate, decides beyond-envelope requests, exercises the veto, and keeps purpose, strategy, success measures, human-side mechanism authority, risk appetite, capital/resource balance, and emergency stops (10, 12, 14, 15, 18).
- **Top Management (`[ORG]HOAC-TM`):** Runs and builds the operation within its mandate and envelope (15, 18, 19).
- **`[ORG]AION`:** Designs, proposes, reviews proposals, rejects bad ones, and applies small reversible changes within the governance seat's signed dial (12, 14, 15).
- **AI units / Chief of Staff:** Produce outputs, lead agents, summarise/order decisions for humans, and act/sign only within granted authority (3, 16, 20).
- **What AI can never do:** Hold legal personhood or accountability, fill human positions, perform the 19 Human Floor tasks (e.g., sign listed decisions, widen access/budget/authority, hold root keys, judge final tests), run the operation (for `[ORG]AION`), declare the organisation successful, or block/intercept reports, objections, or stops (3, 6, 7, 12, 13, 16, 20).

**6. How does a human stay in control and accountable?**
Every output and unit is tied to a human legal position (`HOAC-GOV`, `-TM`, `-ACS`), which holds legal accountability and signs via credentials verified by the system (3, 6, 18). The Human Floor (HF-01 to HF-19) reserves critical powers—like granting authority/budget, final test judgment, root keys, and live sign-ins (HF-10)—exclusively to humans (7). Control is enforced outside every AI by the **tool gateway** (which holds credentials, logs calls, fails closed, enforces the requester's authority ceiling, and blocks listed decisions without a valid human signature) and the **stop** (an external human port that revokes credentials and halts work immediately) (13, 20). Furthermore, reports, objections, and stops bypass all AI (including the Chief of Staff and core) to reach human positions directly, and humans always have open access to raw records (13, 15, 16, 18).

**7. How does it stay current as AI improves, and how does the organisation grow or shrink over time?**
49GAION stays current through 49GAION Self-Improvement and a growing Library of shared patterns and parts (4, 8, 9). The organisation's `[ORG]AION` watches 49GAION's Standard, Blueprint, and Library for updates and proposes what to adopt to the governance seat (12). Internally, any unit or position can propose changes, and Top Management sends operational achievements back to the governance level to update the organisation's own Standard, Blueprint, and Library (14).

The organisation grows or shrinks through **Structural Adaptation** (15, 19). Starting small with multiple processes sharing one AIOC, the `[ORG]AION` monitors the operational record against costs and resources: when a process outgrows its AIOC, `[ORG]AION` proposes splitting it into a new AIOC; when work shrinks, it proposes merging AIOCs (never merging a part with the part that checks it), and a human position decides (15).

**8. What does the organisation own, what stays with 49GAION, and when is a product "Powered by 49GAION"?**
- **Organisation owns:** Its `[ORG]AION`, its own Standard, Blueprint, and Library (including copies of parts taken from 49GAION), its records, working data, and raw intake sources (returned and deleted from Edition Maker at handover) (9, 10, 11, 12, 14). After handover, 49GAION has no authority or access (10, 12).
- **Stays with 49GAION:** The 49GAION framework, Edition Maker, its central Standard, Blueprint, Protocol, and Library, and its names and marks (which are not licensed; texts are CC BY 4.0 and code is Apache 2.0) (1, 8, 10, 11).
- **"Powered by 49GAION":** By 49GAION's rule (beyond the legal licence floor), if an organisation uses even one 49GAION item—an idea, Library part, blueprint, or Standard—all its products are "Powered by 49GAION", which in practice applies to everything it builds (1, 11, Part F).

**9. Does the same framework fit one person with one task and a group of companies? How?**
Yes, every request from a single position with one task to a group of companies becomes an `[ORG]AION` of the same shape, differing only in size (10). 
- **One person:** 49GAION never uses the term "one-person organisation"; instead, the system defines only legal positions, and under the organisation's human-side mechanism, one natural person may hold several or all positions where the law allows (6, Part F). Each position remains a distinct party in the record, though legally required independent checks (like internal audit, HF-19) must be held by a party independent in fact from outside the organisation (6, 7).
- **Group of companies:** Treated as one organisation with one governance seat over the group; where local law requires a company to have its own governing body, that body holds a governance seat for that company alone, and a position of the acting company signs every act (12).

**10. Is it executable? The three strongest reasons it can work and the three biggest risks, and whether the text answers each risk or leaves it to the organisation's AI on purpose.**
Yes, it is executable.
**Three strongest reasons:**
1. **Architectural enforcement:** The tool gateway and stop run as code outside all AI, failing closed and enforcing human signatures and authority ceilings (13, 20).
2. **Pre-built foundation:** Organisations do not start from scratch; they draw tested parts, blueprints, and patterns from the 49GAION Library, with resilient dual interfaces (panel and back office) (9, 12, 17).
3. **Incremental scaling:** Organisations start small (or transition output by output) and scale via Structural Adaptation (10, 15).

**Three biggest risks & how the text handles them:**
1. **Confident AI error / prompt injection:** Answered by the text—mitigated by multi-engine challenges ("one writes, two challenge"), fixed tests on real outputs signed by humans, and treating outside text strictly as data (3, 10, 20).
2. **Human bottlenecking:** Answered by the text—mitigated by the dial (standing approval) and Chief of Staff grants for reversible, non-widening actions (7, 14, 16).
3. **Governance seat conflict of interest or compromise after handover:** Partially answered—pre-handover, the founding configuration requires an independent substitute or second signature for conflicts, enforced at the gateway (10, 15); post-handover, the organisation holds full authority to amend principles and safeguards within the law ("hand over, then let go") (4, 7, 12). Detailed operational workflows are left to AI at the time (4, Part E).

**11. What would a new organisation ask that the text cannot answer?**
At the level of definition, there are no unaddressed conceptual gaps (commercial terms are outside the definition, and operational/technical details at the time are purposefully left to the `[ORG]AION` under sections 4, 10, 16, and Part E). However, a new organisation reading this text cold would ask practical onboarding and reference questions that live in external documents cited by the text rather than in the text itself (**NOT IN THE TEXT**):
1. What are the exact step-by-step instructions to submit an initial request today? (Located in `ADOPTING.md`, section 10).
2. Who is the legal owner of 49GAION, and what are the full legal terms of the licences? (Located in `LICENSE.md`, section 11).
3. What are the detailed technical rules, protocols, and naming conventions? (Located in `upstream/49GAION-UPSTREAM.md`, the Naming Standard, the Operating Protocol, and the AIOC definition, Preamble).

VERDICT: COMPLETE

#### Reader 2 · openai / gpt-6.1-sol · 03:09 UTC

[openai / gpt-6.1-sol]

1. **What it is and what is received.** 49GAION is an organisation-design framework that builds AI-native organisations from interchangeable AI units and human positions, starting with outputs rather than existing jobs. An organisation receives its own independent, living `[ORG]AION`: initially a governance-level core with its first Standard and Blueprint, a governance panel, gateway and stop, and access to 49GAION’s knowledge and Library—not a finished organisational design. (§§1, 3–4, 10, 12–13)

2. **What makes it special.** Instead of adding AI to human jobs, it designs backwards from the required output and AI’s capabilities, adding humans for accountability and necessary human work. Its own AI continually redesigns the organisation, drawing on a shared Library of reusable parts; humans approve changes, while Top Management builds and runs operations. Design is therefore an ongoing organisational capability rather than a completed installation. These are the text’s distinguishing claims, not independently demonstrated superiority. (§§3–5, 9, 12, 19)

3. **Starting, step by step.**
   1. Send a request to Edition Maker.
   2. Supply purpose, outputs, quality, constraints, resources and founding governance settings.
   3. A human edition engineer supervises construction; one engine works and two challenge each step.
   4. Governance accepts the core; fresh keys replace Edition Maker’s keys, and intake data is returned and deleted.
   5. The core proposes a small organisation; governance approves.
   6. Governance mandates Top Management.
   7. Top Management builds and runs operations, with tests ready before work begins.

   **NOT IN THE TEXT:** the actual submission channel and adopter’s first practical action; these are deferred to `ADOPTING.md`. (§§10, 13, 15, 19–20)

4. **Required parts and builders.** Framework-side components are the governing seat, Standard/Naming Standard, Blueprint, Library, Protocol, Self-Improvement and Edition Maker. Organisation-side components include the governance core, its rules and Library, governance panel, external gateway and stop, and Top Management’s AIOC. Every AIOC has a versioned blueprint, code panel and AI back office; Cells and Pods compose its internals. Edition Maker supplies the initial core under a human engineer. The `[ORG]AION` designs subsequent arrangements; Top Management builds operational components. Changes to gateway/stop code require a human signature and a party other than the constrained AI. (§§8–10, 13, 16–20)

5. **Who decides what.** 49GAION’s governing seat approves framework changes. The organisation’s governance seat controls purpose, strategy, risk, capital, design approvals and Top Management’s mandate; it can veto or stop operations. Top Management runs operations within that mandate. The `[ORG]AION` designs, reviews and proposes, applying changes only with approval or a valid standing dial. AI units execute granted work. AI never holds human positions, accepts legal accountability, performs Human Floor decisions, widens its own authority, or substitutes for required human signatures. The organisation can amend its inherited rules after handover, but not override law. (§§6–8, 12, 14–16, 18–20)

6. **Human control and accountability.** Every output has an accountable human position. Delegated authority is bounded; missing authority blocks action. Human-held approvals, root keys and break-glass access sit alongside an external, fail-closed gateway and stops that revoke credentials and cancel work. Listed decisions require valid human signatures; each signature requires fresh live sign-in. Humans receive direct reports, objections and stops without AI mediation, retain access to raw records, and approve test changes. Independent checking, audit and conflict-of-interest arrangements support oversight. These safeguards are guaranteed at handover; afterwards, maintaining them is the organisation’s responsibility within law. (§§3, 6–7, 13–16, 18, 20)

7. **Staying current and resizing.** The `[ORG]AION` watches updates to 49GAION’s Standard, Blueprint and Library and proposes adoption; governance decides. It also learns from operational achievements recorded in the organisation’s own rules and Library. Structural Adaptation starts small, watches workload and resources, and proposes splitting growing processes into AIOCs or merging shrinking ones, weighing costs and preserving separation from checking functions. Humans decide structural changes. Detailed arrangements are intentionally determined by AI at the time, not prescribed in advance. (§§4, 12, 14–15, 19)

8. **Ownership and attribution.** The organisation owns its `[ORG]AION`, records, rules and organisation-specific Standard, Blueprint and Library; it retains local copies of Library material under its licences. 49GAION retains its framework, Edition Maker, central resources and unlicensed names/marks—not organisational authority, access keys or working data after handover. Giving work back is optional. Under 49GAION’s attribution rule, using even one framework idea or component makes all the organisation’s products “Powered by 49GAION,” including after modification. That broader rule is expressly distinguished from the legal licence obligations: CC BY 4.0 for texts and Apache 2.0 for code. (§§10–12, 14)

9. **One task through corporate groups.** Yes: every request produces an `[ORG]AION`; scale changes, the basic shape does not. One natural person may hold all legally compatible human positions, but positions and their recorded decisions remain distinct. Required independence must exist in fact, using outside holders where necessary. Small workloads share an AIOC; growth can produce nested AIOCs. A corporate group has group governance, with company-specific governance seats where law requires and signatures belonging to the company acting. (§§6, 10, 12, 15–16)

10. **Executability: strongest reasons and risks.** It is specified as executable, not empirically proven by this text.

   **Three reasons:** (1) a defined handover-to-operation sequence; (2) reusable, versioned components and recorded handoffs; (3) bounded authority, external controls and output tests. (§§8–10, 13, 17, 19–20)

   **Three risks:** (1) confidently wrong AI or correlated challengers—addressed through cross-engine challenge, evidence and human judgement, not eliminated; (2) authority abuse or control compromise—addressed through signatures, ceilings, independent controls and stops; (3) unsuitable or obsolete designs—deliberately left to ongoing organisation-specific AI design, subject to human approval. Security, supplier and cost dependencies are acknowledged; their detailed treatment is intentionally local. (§§3–4, 14–15, 20)

11. **Questions the text cannot answer.**
   - **NOT IN THE TEXT:** “Where exactly do we submit our request, and what do we do first today?” The answer is located in `ADOPTING.md`, not supplied here. (§10.1)
   - **NOT IN THE TEXT:** “What is the complete mandatory signature-type list our gateway must enforce at handover?” The text requires inclusion of 49GAION’s own list but does not reproduce that list; the Human Floor supplies principles, not an explicit complete gateway list. (§§7, 20.3)

   Detailed organisational design, staffing arrangements and implementation choices assigned to the organisation’s AI are intentional decisions, not missing answers. (§§4, 10.6, 16)

VERDICT: GAPS

#### Reader 3 · claude / claude-opus-5-5 · 03:19 UTC

[claude / claude-opus-5-5]

**1. What it is and what an organisation receives** (§1, §10.5, §13.1, Part E)

49GAION is a framework for designing organisations from interchangeable AI and human parts. It designs AI-native, live organisations.

An organisation receives its own `[ORG]AION`, an edition handed over by Edition Maker. The edition contains:
- **The core:** the first AIOC, made from the Library part "49GAION Charter".
- **The governance seat position and the governance panel.**
- **The first versions of the organisation's own Standard and Blueprint**, plus its own Library.
- **The tool gateway and the stop.**
- **The founding configuration.**
- **Open access to the 49GAION Library.**

It is shown as "`<Brand>` AION, Powered by 49GAION".

**2. What makes it special** (§3, §4, §6, §7, §9, §10.6, §20)

- **Where design starts.** It starts from the output and from what AI can do, then adds humans where needed. Conventional design starts from people and jobs, then adds AI.
- **No finished design.** The organisation's own AI designs, configures and keeps the organisation current as AI improves.
- **A shared Library** grows from what every `[ORG]AION` builds.
- **Positions, not persons.** Only legal positions are recorded; no natural person is.
- **A Human Floor** of 19 items stays human, enforced in code.
- **Safeguards sit outside every AI:** the gateway, the stop, fail-closed behaviour and challenge by other engines.

**3. How an organisation starts** (§10, §13.2, §15.2.3, Part E)

1. The request goes to Edition Maker, led by a human edition engineer. At every step, one engine works and two challenge.
2. The intake captures purpose, outputs, quality, inputs, musts, money, time and gaps. The founding configuration is fixed here.
3. The governance seat accepts the edition. Keys are reissued, Edition Maker's keys are revoked, and the organisation's data is returned and deleted.
4. The core takes the seat's brief and proposes a small organisation. If rejected, it re-proposes from the seat's reasons.
5. The seat approves and grants Top Management its mandate and envelope.
6. The Top Management Group builds and runs the operation.

How a request is brought in practice is deferred to `ADOPTING.md`, which is NOT IN THE TEXT.

**4. Which parts must exist and who builds them** (§10, §13, §16–§20)

| Part | What it does | Who builds it |
|---|---|---|
| Core | Holds the seat, the rules and the governance panel | Edition Maker |
| Gateway | Holds credentials and engines, logs calls, enforces signatures | Edition Maker |
| Stop | A human port outside every AI | Edition Maker |
| Top Management Group | The operation's hub | Proposed by the `[ORG]AION`, approved by the seat |
| AIOCs | The only unit kind (Cells, Pods inside), each with blueprint, panel and back office | Top Management in operation; the `[ORG]AION` designs; AI at the time decides the specifics |
| Chiefs of Staff | Serve each human position | The position sets up its own |
| HOAC positions | Human accountability (GOV, TM, ACS) | Filled by the organisation's own mechanism |

Gateway and stop code may be changed only by a party other than the AI they constrain (§20.8).

**5. Who decides what** (§7, §12.1, §14.3, §15.2, §16, §20)

- **Governance seat:** purpose, strategy, measures, risk appetite, capital and resource balance, conflicts, approvals, the dial, the mandate, the veto, emergency stop.
- **Top Management:** runs the operation within the envelope. It requests anything beyond the envelope through the gate.
- **`[ORG]AION`:** designs and proposes. It may reject proposals alone. It applies changes only with the seat's signature or within the signed dial. It never runs the operation.
- **AI units:** act only within granted authority and the original requester's authority.

AI never accepts accountability or holds Human Floor work. It never signs listed decisions, never is the stop, never alters its own gateway, and never carries the protected report, objection or stop route.

**6. How a human stays in control and accountable** (§3, §6, §7, §14.5, §15.2.4, §16, §18, §20)

- **Every output has a human owner.** A human position is accountable for every output.
- **Signatures are live.** Every signature needs a fresh live sign-in (HF-10). Standing approvals cover only undoable, non-widening changes.
- **The gateway enforces signatures** and fails closed.
- **The stop sits outside every AI** and is never blocked.
- **Reports, objections and stops** go directly to humans, never through any AI.
- **Chiefs of Staff cannot drop or delay** anything, and the raw record stays open to the position.
- **Reports are checked independently.**
- **Every rule change is recorded** with the deciding position's own words.
- **Silence is never consent.**

Which natural person holds a position is decided by the organisation's own mechanism. The text leaves this outside the system on purpose.

**7. Staying current; growing and shrinking** (§4, §8, §12.5, §14, §15.1, §15.2.6, §16)

**Staying current:**
- 49GAION Self-Improvement updates the framework.
- The `[ORG]AION` watches new versions of the Standard, Blueprint and Library and proposes what to take. The seat decides.
- Details are decided and changed by AI as AI improves. This is deliberate.

**Growing and shrinking:**
- Structural Adaptation starts small, with processes sharing one AIOC. It proposes splits when a process outgrows its home and merges when work shrinks, weighing cost. It never merges a part with its checker.
- A human decides each change.
- Moves beyond the envelope pass the gate.
- Parts can switch between AI and human above the Floor.

**8. Ownership and "Powered by 49GAION"** (§11, §12.4, §14.1, §10.7)

**The organisation owns:** its `[ORG]AION`, its Standard, Blueprint and Library (treated as its IP), its records and rules, and copies of what it took from the Library. It may stop its `[ORG]AION` at any time.

**49GAION keeps:** the framework, Edition Maker, its own Library, and its names and marks, which are not licensed. It keeps no access to and no data of the organisation after handover.

**Licences:** texts are CC BY 4.0 and code is Apache 2.0.

**"Powered by 49GAION":** applies if the organisation uses even one 49GAION idea, part, blueprint or Standard element. In practice this is always.

**9. One person with one task versus a group of companies** (§6.3–6.4, §10.1, §12.6)

Yes, the same framework fits both. Every request becomes an `[ORG]AION`; the size changes, the shape does not.

- **One person:** the person holds all positions, where the law allows. The positions stay distinct parties. It is never called a "one-person organisation". Where independence is needed, such as the internal audit, it must come from outside.
- **A group of companies:** one organisation with one governance seat over the group. A company whose law requires its own governing body holds a company-level seat, and each act is signed by a position of the company that acts.

**10. Is it executable?**

**Strengths:**
1. Hard controls in code outside AI: the gateway, the stop and fail-closed behaviour (§20).
2. Clear position-based accountability (§6, §7).
3. An incremental start from Library patterns, which also suits existing organisations (§9, §10.8, §15.1).

**Risks:**
1. **AI design errors.** Answered by challenge from other engines, fixed tests and human signatures (§20.5–6). The specifics are left to AI on purpose.
2. **Signature overload or rubber-stamping.** Partly answered by the dial, Chief of Staff grants and "silence is never consent" (§7, §14.3, §16).
3. **Gateway integrity as a single trust point.** Changes are guarded (§20.8), but independent verification of the initial gateway is not stated.

**11. What a new organisation would ask that the text cannot answer**

All of the following are NOT IN THE TEXT:
- **How to actually submit a request.** The text defers this to `ADOPTING.md` (§10.1).
- **The contents of 49GAION's Human Floor signature list.** The list of listed decision types is referenced but not given (§20.3).
- **Who verifies the delivered gateway and stop code before trust is placed in it,** and who maintains it after handover (§13.1, §20.8).
- **What happens to operational continuity when the gateway fails closed** (§20.3).

Pricing is not asked, because commercial terms are outside the definition.

VERDICT: GAPS

#### Reader 3, first call, cut off at 6,000 tokens · 03:13 UTC

[claude / claude-opus-5-5]

**1. What it is and what an organisation receives**

49GAION is an organisation design framework for building organisations from interchangeable AI and human parts. Its product is `[ORG]AION`: the living AION of one organisation, which holds that organisation's design and keeps building it. (§1)

The organisation receives an edition, made by Edition Maker and accepted by its governance seat. The edition contains:
- the core AIOC, made from the 49GAION Charter part;
- the governance-seat position;
- the first version of its own Standard (the 49GAION Standard plus its own musts), Blueprint and Library;
- the governance panel;
- the tool gateway and the stop;
- a link to 49GAION's Library;
- the founding configuration;
- fresh gateway keys.

It does not receive a finished design. (§10.4–10.7, §13.1)

**2. What makes it special**

- **Starting point.** It starts from the output and from what AI can do, then adds humans where they are needed. A conventional approach starts from people and jobs and bolts AI on. (§3, §5)
- **Live design.** Design is not installed from outside. The organisation's own `[ORG]AION` designs it and keeps it current with AI's progress. (§4)
- **Shared Library.** A growing Library works as a marketplace of parts and whole-organisation patterns. (§9)
- **Positions, not persons.** Only AIOCs and legal positions exist in the system, never named persons. (§1.5, §6)
- **Interchangeable parts.** Parts are built like a puzzle: any Cell can move between AI and a human position. (§16)
- **Enforced safeguards.** The Human Floor and the safeguards are enforced by code outside every AI (the gateway and the stop). (§7, §20)

**3. How an organisation starts**

1. **Request** to Edition Maker. How to submit one in practice is NOT IN THE TEXT; it is deferred to `ADOPTING.md`. (§10.1)
2. **Intake** of purpose, governance seat, outputs, quality, inputs, musts, money and time, success measures and gaps. The founding configuration is fixed here. (§10.4)
3. **Edition** built, with one engine working and two challenging at every step, under the edition engineer. (§10.2–3)
4. **Handover** when the seat accepts. Keys are reissued and the organisation's data is returned and deleted. If the seat rejects, the edition goes back with reasons. (§10.7)
5. **First proposal.** The core offers several designs for a small organisation, reproposing until one is approved. (§13.2)
6. **Mandate** handing the operation to Top Management. (§15.2.3)
7. **Operation** run by the Top Management Group. (Part E, §19)

**4. Which parts must exist and who builds them**

| Part | What it does | Who builds it |
|---|---|---|
| Core AIOC | Root of the organisation; holds the seat, the organisation's rules and the governance panel | Edition Maker, at handover (§13) |
| Tool gateway | Holds credentials and engines, logs every call, requires signatures for listed decisions, fails closed | Installed by Edition Maker; later changes signed and made by a party other than the AI it constrains (§20.3, §20.8) |
| Stop | A human port that revokes a unit's credentials | Same as the gateway (§20.2, §20.8) |
| AIOCs | Each has a blueprint, a code-written panel, a back office (AI chat workspace) and a fixed test | Designed by `[ORG]AION`, approved by humans (§16–17, §20.6) |
| Cells, Pods, Chief of Staff | Inside AIOCs; the Chief of Staff leads agents and surfaces decisions | Each Chief of Staff is set up by its own position (§16) |
| Top Management Group | Builds the operation | Top Management (§19) |

Engine choice and the exact arrangement of units are left to AI on purpose (§16, Part E).

**5. Who decides what**

- **Governance seat:** decides on purpose, strategy, success measures, risk appetite, capital and its balance with resources, and conflicts. It also handles owners' rights, the mandate and envelope, the gate, and veto and emergency stop. It approves every change to the organisation's rules and holds the dial. (§14.3, §15.2)
- **Top Management:** runs the whole operation within its mandate and requests anything beyond the envelope. (§15.2.3, §15.2.6, §18)
- **`[ORG]AION`:** designs and proposes. It may reject on its own, but applying a change needs the seat's signature or must fall within the dial. It never runs the operation. (§12.1, §14.3)
- **AI units:** act only within granted authority. (§20.1)

**AI never:**
- accepts accountability (§3);
- does Human Floor work (§7);
- signs a listed decision (§16, §20.3);
- grants itself access or power (HF-11);
- is the stop (§20.2);
- changes the gateway or stop that constrains it (§20.8);
- exceeds the original requester's authority (§20.9).

**6. How a human stays in control and accountable**

- **Accountability.** A human position is accountable for every output. (§3)
- **Signatures.** Every signature needs a fresh live sign-in. The gateway blocks unsigned listed decisions and fails closed. (§7 HF-10, §20.3)
- **The stop.** It sits outside every AI and is never blocked. (§20.2–4)
- **Direct routes.** Reports, objections and stops reach humans directly, never through AI. (§15.2.4, §16, §18)
- **Unfiltered record.** A Chief of Staff never drops or delays anything, and the raw record stays open to its position. (§16)
- **Independent checks.** Top Management's reports and the judgment of success are checked by independent parties. (§13.3, §15.2.4)
- **Evidence.** "Done" means visible evidence and fixed tests signed by humans. (§20.6)
- **Decision record.** Every rule change is recorded with the deciding position's own words. (§14.5)
- **Credentials.** Credentials are issued by the organisation's own mechanism. (§6.2)

**7. Staying current, growing and shrinking**

- **Staying current.** Details are decided and changed by AI at the time, as AI improves (§4). The `[ORG]AION` watches 49GAION's new versions and proposes what to take, and the seat decides (§12.5). 49GAION itself is kept current through Self-Improvement (§8).
- **Learning from the operation.** Top Management sends its achievements to the governance level, so the organisation's own rules grow from experience. (§14.4, §19)
- **Growing and shrinking.** Structural Adaptation starts small, with several processes sharing one AIOC. It proposes splits when a process outgrows its home and merges when work shrinks, weighed against cost. It never merges a part with the part that checks it, and a human decides each change. (§15.1)
- **Scope.** Growth beyond the envelope passes the gate. (§15.2.6)

**8. Ownership and "Powered by 49GAION"**

- **The organisation owns:** its `[ORG]AION`, its Standard, Blueprint and Library (including what it took from 49GAION), its records and its rules. It may stop or close its `[ORG]AION` at any time, and nothing is published without its choice or a legal requirement. (§12.4, §14.1)
- **49GAION keeps:** the framework, Edition Maker, its own Library, and its names and marks, which are not licensed. It keeps no access or data after handover. (§10.1, §10.7, §11.5)
- **Licences:** texts are CC BY 4.0; code is Apache 2.0. (§11.5)
- **"Powered by 49GAION":** if an organisation uses even one 49GAION item, all its products carry the label, and it persists after upgrades or changes of edition. (§11.1–3)

Minor tension: 49GAION "records" an organisation's own work (§11.2) yet keeps no organisation data (§10.7).

**9. One person with one task versus a group of companies**

Yes, the same framework fits both. The size changes, the shape does not: every request becomes an `[ORG]AION`. (§10.1)

- **One person:** they hold all the positions. The positions stay distinct parties, and each decision is recorded under the position that takes it. (§6.3–4) The organisation starts with processes sharing one AIOC (§15.1). Where independence is required, such as the internal audit or a conflicted seat, it comes from outside (§6.3, §15.2.8).
- **A group of companies:** one organisation with one governance seat over the group. A company whose law requires its own governing body gets a seat for that company alone, and every act is signed by a position of the acting company. (§12.6)

**10. Is it executable?**

**Strengths:**
1. Hard controls in code outside every AI: the gateway, the stop and fail-closed behaviour. (§20)
2. Starting small from Library parts and patterns, so work begins at once. (§9, §12.2, §13.2)
3. A clear chain of accountability through positions, signatures and independ

### Round 4 · input `ad3c7f10816e859e…`

#### Reader 1 · gemini / gemini-4-argon · 03:37 UTC

[gemini / gemini-4-argon]

**1.** 49GAION is an organisation design framework for building live, AI-native organisations from interchangeable AI and human parts, starting from the desired output and what AI can do. An organisation receives its own `[ORG]AION`—a living core linked to 49GAION's Standard, Blueprint, and Library, complete with the first version of the organisation's own Standard and Blueprint, a governance panel, a tool gateway, and a stop mechanism. (Sections 1, 3, 4, 10, 13, Part E)

**2.** Conventional approaches start from human jobs and limits (like memory, tiredness, and single locations) or install static systems that quickly fall behind. 49GAION is AI-native and live: it designs backwards from the output and AI capabilities, replacing human-limit structures with one complete record, continuous work, multi-skilled AI units, and a shared queue. Furthermore, the organisation's own AI (`[ORG]AION`) continuously designs, configures, and updates the organisation as AI improves. Finally, it records only legal positions (`HOAC`) and AI units (`AIOC`), never natural persons or their names. (Sections 1, 3, 4, 5, 6)

**3.** 
1. **Request & Intake:** The request goes to 49GAION Edition Maker (supervised by a human edition engineer using a three-engine challenge), which takes in the organisation's purpose, outputs, musts, and founding configuration.
2. **Handover:** Edition Maker builds and hands over the `[ORG]AION` core (with the gateway and stop). The governance seat accepts it, revokes 49GAION's keys, and takes full authority.
3. **First Proposal:** The core takes the governance seat's brief and proposes a small organisation design; the seat approves it.
4. **Mandate & Operation:** The governance seat delegates the operation to Top Management via a mandate; the Top Management Group builds and runs the operation. (Sections 10, 13, 15, 19, Part E)

**4.** 
- **Edition Maker** (built by 49GAION, led by a human edition engineer) builds and hands over the initial **Core** (made from the 49GAION Charter).
- The **Core / `[ORG]AION`** holds the governance seat (`[ORG]HOAC-GOV`), the organisation's Standard, Blueprint, and Library, and the governance panel. It designs, proposes, and oversees the organisation.
- **Tool gateway and Stop:** Installed with the core (running as code outside AI reach) to log calls, hold credentials, enforce human signatures, and revoke access.
- **Top Management Group:** The first AIOC under the core (`[ORG]HOAC-TM` plus its AIOC). It builds and runs the operational units.
- **AIOCs, Pods, Cells, Panels, Back Offices, and Chiefs of Staff:** Operational parts built by Top Management and `[ORG]AION` from blueprints. (Sections 10, 12, 13, 16–20)

**5.** 
- **Governance seat (`[ORG]HOAC-GOV`):** Decides purpose, strategy, success measures, risk, capital/resource balance, structural changes, rule updates, and new 49GAION versions; grants Top Management's mandate and holds veto power.
- **Top Management (`[ORG]HOAC-TM`):** Decides how to build and run the operation within its mandate's envelope.
- **`[ORG]AION`:** Proposes designs and adaptations, rejects bad internal proposals, and applies small, reversible changes only if granted a signed "dial" by the governance seat.
- **AI units (and Chiefs of Staff):** Execute work within granted authority and bring decisions to humans.
- **What AI can never do:** Hold legal personhood or accountability, fill a human position, perform Human Floor tasks (HF-01 to HF-19, e.g., sign listed decisions, widen access/budget, hold root keys), or control the gateway/stop. (Sections 3, 6, 7, 12–16, 18–20)

**6.** Humans hold all legal positions (`HOAC`), and a human position is accountable for every output. Control is enforced structurally:
- **The Human Floor (HF-01 to HF-19):** Reserves critical duties (accountability, delegation, budget/access grants, root keys) strictly to humans.
- **The Tool Gateway:** Exists outside AI reach, fails closed, and requires a fresh live human sign-in (HF-10) for any listed decision or widening of authority.
- **The Stop:** A human-only port outside AI reach that revokes credentials and halts work; only a human can restart it.
- **Direct Routes & Veto:** Reports of wrongdoing, objections, and stops bypass all AI (including Chiefs of Staff and the core) to reach humans directly, and the governance seat can veto any decision. (Sections 3, 6, 7, 13, 15, 16, 18, 20)

**7.** 
- **Staying current:** 49GAION updates its Library via 49GAION Self-Improvement. The organisation's `[ORG]AION` watches 49GAION's Standard, Blueprint, and Library, proposing new updates to the governance seat. Internally, Top Management sends operational achievements to the governance level to update the organisation's own Library, and any unit can propose improvements.
- **Growing and shrinking:** Through **Structural Adaptation**, `[ORG]AION` starts the organisation small (several processes sharing one AIOC) and monitors the operational record. When a process outgrows its AIOC, `[ORG]AION` proposes splitting it into a new AIOC; when work shrinks, it proposes merging (never merging a part with the part that checks it). A human position decides every change. (Sections 4, 8, 12, 14, 15)

**8.** 
- **Organisation owns:** Its `[ORG]AION`, its own Standard, Blueprint, and Library (as its IP), its records, working data, and parts copied into its Library. At handover, 49GAION revokes its keys and deletes the organisation's intake data.
- **Stays with 49GAION:** The 49GAION framework, Edition Maker, the central Standard, Blueprint, Protocol, Library, and its names/marks (texts are licensed under CC BY 4.0, code under Apache 2.0).
- **"Powered by 49GAION":** Applies to all products of an organisation if it uses even one idea, Library part, blueprint, or Standard from 49GAION (which in practice is everything it builds). (Sections 8, 10, 11, 12, 14)

**9.** Yes, every request—from one person with one task to a group of companies—becomes an `[ORG]AION` with the same shape, changing only in size. 
- **One person:** Under the HOAC Assignment Model, one natural person can hold every distinct HOAC position (where the law allows, though independent checks like internal audit must be held by an outside independent position). The processes simply share a small number of AIOCs.
- **Group of companies:** Treated as one organisation with one governance seat over the whole group. Where the law requires a subsidiary to have its own governing body, that body holds a governance seat for that company alone, and company acts are signed by a position of that company. (Sections 6, 10, 12, 15, Part F)

**10.** Yes, it is executable.
- **Three reasons it works:** (1) Immediate bootstrap via the 49GAION Library and Charter rather than building from scratch; (2) Hard, code-level safeguards outside AI reach (fail-closed gateway, non-AI stop, authority ceiling); (3) Mutual resilience between the coded panel and AI chat back office, plus multi-engine verification ("one writes, two challenge") against fixed tests.
- **Three risks and how they are handled:** (1) *AI hallucination/overreach:* Answered by the text via the multi-engine challenge, fixed tests on real outputs, fail-closed gateway, and authority ceiling; (2) *Single-human conflict of interest or self-auditing:* Answered by the text by requiring external independent positions for checks (HF-19) and pre-set conflict-of-interest recusal rules in the founding configuration; (3) *Sub-optimal operational task division:* Left on purpose to the organisation's AI at the time via Structural Adaptation and human approval. (Sections 3, 4, 6, 7, 9, 13, 15, 17, 20)

**11.** **NOT IN THE TEXT:** While commercial terms are outside the definition and operational details are intentionally left to AI at the time, the text explicitly defers external documentation and future protocols that a new organisation would ask for:
1. The practical steps to submit an initial request today (deferred to `ADOPTING.md`, Section 10.1).
2. The range of possible human-to-position assignment models (explicitly noted as "a separate assignment protocol of the Top Management Group, to be defined later", Section 6.4).
3. The identity of the legal owner of 49GAION and full licensing terms (deferred to `LICENSE.md`, Section 11.5).
4. The detailed rules of the Standard, Naming Standard, Operating Protocol, and AIOC definition (deferred to `upstream/49GAION-UPSTREAM.md` and other texts, Preamble).

VERDICT: COMPLETE

#### Reader 2 · openai / gpt-6.1-sol · 03:39 UTC

[openai / gpt-6.1-sol]

1. **What it is and what is received.** 49GAION is an organisation-design framework for building live, AI-native organisations from interchangeable AI units and human positions. An organisation receives its own independent `[ORG]AION`: a governance-level core linked to 49GAION’s knowledge, initial organisation-specific Standard and Blueprint, Library access, governance interface, tool gateway and stop—not a finished operational design. (§§1, 10, 12–13)

2. **What makes it special.** It starts with the required output and AI’s capabilities, adding humans where needed, rather than adding AI to existing human jobs. Its organisation-specific AI continually designs and proposes improvements to the organisation itself; human positions authorise them. Reusable Library parts, interchangeable components and evidence-based tests support adaptation, while legal accountability, oversight and separation of powers remain human. These are the text’s stated distinctions, not evidence that no conventional approach shares them. (§§3–5, 9, 16, 20)

3. **Starting, step by step.**
   1. Submit a request to Edition Maker.
   2. Supply purpose, governance, outputs, quality, constraints, resources and success criteria; fix founding settings.
   3. A human edition engineer supervises production, with one engine working and two challenging each step.
   4. Governance accepts the core and initial rules; fresh keys replace Edition Maker’s keys.
   5. The core proposes a small organisation; governance approves.
   6. Governance mandates Top Management.
   7. Top Management builds and runs operations, with tests ready before work begins.

   **NOT IN THE TEXT:** the actual submission channel; §10.1 refers to `ADOPTING.md`. (§§10, 13, 15, 19–20; Part E)

4. **Practical components and builders.** Edition Maker supplies the core, initial rules, gateway and stop under human supervision. The core holds governance, design knowledge and the governance panel. The `[ORG]AION` designs and maintains the organisation; the Top Management Group builds operational units and tools. Each AIOC has a versioned blueprint, coded control panel, AI chat back office and API-connected engines, with Cells/Pods as needed. Human positions carry accountability. Units require interfaces, recorded handoffs, tests and stops. Gateway/stop changes require a human signature and a party other than the constrained AI. Detailed implementation and unit arrangement are deliberately decided at the time. (§§8, 10, 13, 16–20)

5. **Who decides what.** Governance retains purpose, strategy, success measures, risk appetite, capital/resource balance, reserved matters and ultimate intervention. Top Management runs operations within its delegated envelope. The `[ORG]AION` designs, reviews and proposes changes; it may reject proposals and apply changes within signed standing approval. Operational AI units execute granted work. AI cannot occupy human positions, accept accountability, exercise reserved Human Floor functions, grant itself authority, bypass signatures or act without clear permission. The `[ORG]AION` never runs operations. These are handover constraints; afterwards the organisation controls its rules, subject to law. (§§6–7, 12, 14–16, 18–20)

6. **Human control and accountability.** Every output has an accountable human position. Authority is delegated explicitly and bounded by both executor and original requester. An external gateway enforces permissions and required signatures; signatures require fresh live sign-in, with narrowly bounded standing grants. Humans have external stops, direct reporting routes, raw-record access and independent checks. Governance can veto management and revoke mandates. Decisions, reasons and versions are recorded. Position-holder assignment and credentials come from the organisation’s human mechanism; independence must be real where required. After handover, maintaining these safeguards is the organisation’s responsibility. (§§3, 6–7, 14–16, 18, 20)

7. **Keeping current and resizing.** The `[ORG]AION` monitors new 49GAION Standards, Blueprints and Library material, proposing adoption for governance approval; updates never enter automatically. Operational experience also feeds the organisation’s own rules and Library. Structural Adaptation starts with shared processes, proposes separate AIOCs when work grows, and mergers when it shrinks, weighing costs and never merging a function with its checker. Human positions decide structural changes; Top Management implements operationally. Detailed arrangements are intentionally left to AI at the time. (§§4, 12, 14–15, 19)

8. **Ownership and attribution.** The organisation owns its `[ORG]AION`, records and organisation-specific rules, Blueprint and Library; retained Library copies support independence. At handover, 49GAION loses access and deletes organisation data from Edition Maker. 49GAION retains its framework, central Library and Edition Maker; contributions back are voluntary and exclude working data. Texts are CC BY 4.0, code Apache 2.0, and names/marks unlicensed. Under 49GAION’s stated rule, using even one idea or component makes all the organisation’s products “Powered by 49GAION”; that broader rule is expressly distinguished from the licence’s legal requirements. (§§8–12, 14)

9. **One task through company groups.** Yes: every request produces an `[ORG]AION`; size changes, not the basic shape. Small operations can share one operational AIOC, and one person may hold multiple distinct human positions where lawful. Required independence still needs an actually independent holder, potentially external. Larger operations expand through nested AIOCs. A company group has group governance, while companies retain their own governance seats where legally required, and acts are signed by positions of the acting company. (§§6, 10, 12, 15–16)

10. **Executability, strengths and risks.** Architecturally executable, but not demonstrated operationally here.

   **Three strongest reasons:** reusable blueprints and typed interfaces; explicit intake-to-operation responsibilities; enforceable permissions, stops and evidence-based acceptance. (§§8–10, 13, 17, 19–20)

   **Three biggest risks:**
   - **Wrong or correlated AI judgments:** addressed through challenges, output tests and human approval, not eliminated. (§20)
   - **Authority abuse or compromised controls:** addressed through external gateways/stops, signatures, independent checks and conflict rules. (§§6, 15, 20)
   - **Unsuitable implementation, costs or suppliers:** detailed solutions deliberately left to organisational AI within human-approved constraints; no implementation benchmark or operating proof is supplied. (§§3–4, 10, 15)

11. **Questions the text cannot answer.**
   - “Where exactly do we submit our first request today?” **NOT IN THE TEXT:** the channel/instructions are delegated to external `ADOPTING.md`. (§10.1)
   - “What is the exhaustive inherited list of decision types requiring human signatures?” **NOT IN THE TEXT:** the Human Floor gives categories, but the referenced 49GAION signature list itself is not reproduced. (§§7, 20.3)
   - “What measured operating results demonstrate this works?” **NOT IN THE TEXT:** the introduction reports definition-reading tests, not operational deployment results. (§§2, 13.3, 20.6)

   Organisation-specific designs intentionally await its AI; those are not gaps.

VERDICT: GAPS

#### Reader 3 · claude / claude-opus-5-5 · 03:41 UTC

[claude / claude-opus-5-5]

**1. What 49GAION is and what an organisation receives**

49GAION is an organisation design framework for building AI-native organisations from interchangeable AI and human parts. AION stands for AI Operating Nexus. It sets principles and a few safeguards, and AI designs the rest.

An organisation receives its own `[ORG]AION`, shown as "`<Brand>` AION, Powered by 49GAION". This is the living AION that holds and keeps building the organisation's design. Edition Maker hands it over as a core AIOC containing:
- the first version of the organisation's own Standard and Blueprint;
- its own Library;
- the governance panel;
- the gateway and the stop;
- open access to the 49GAION Library.

It does not receive a finished design.

§1, §4, §10.5–10.6, §12–13, Part E

---

**2. What makes it special**

- **Design starts elsewhere.** It starts from the output and from what AI can do, then adds people where needed. Conventional design starts from people and jobs, then adds AI.
- **It is live.** The organisation's own AI designs, configures and keeps it current. Nothing is designed elsewhere and installed as it is.
- **It replaces structures built around human limits.** One record, continuous work, multi-skilled units and one shared queue take their place.
- **Positions, not persons.** Only legal positions and AIOCs are actors.
- **There is a hard Human Floor** of 19 items.
- **Safeguards sit outside every AI.** These include the stop, the tool gateway and a challenge by another engine.
- **It draws on a shared, growing Library.**

§3–7, §9, §20

---

**3. How an organisation starts**

1. **Request.** The request goes to Edition Maker, which an edition engineer leads. At every step one engine works and two others challenge it.
2. **Intake.** This covers purpose, governance seat, outputs, quality, inputs, musts, money, time and success. The organisation fixes its founding configuration, including the conflicted-seat and empty-seat rules.
3. **Handover.** The edition is handed over when the governance seat accepts it. Fresh keys are issued, Edition Maker's keys are revoked and the organisation's data is returned and deleted.
4. **First proposal.** The core gives several proposals for a small organisation. The seat approves, or rejects with reasons.
5. **Mandate.** The seat hands the operation to Top Management.
6. **Operation.** The Top Management Group builds and runs it.

How the first request is actually submitted is only referenced to `ADOPTING.md`. That is **NOT IN THE TEXT**.

§10, §13.2, §15.2, §19, Part E

---

**4. Which parts must exist and who builds them**

| Part | What it does | Who builds it |
|---|---|---|
| Core (first AIOC) | Holds the seat's position, the rules, the governance panel, the gateway and the stop | Edition Maker, from the Library part 49GAION Charter |
| Tool gateway (one per organisation) | Holds credentials, logs every call, fails closed | Code outside every AI; changes made by a party other than the AI it constrains |
| Stop | Revokes a unit's credentials and cancels its work | Same as the gateway |
| Top Management Group | Builds and runs the operation | Top Management position with its AIOC |
| AIOCs, Cells, Pods, Chiefs of Staff | Do and lead the work | Proposed by the `[ORG]AION`, approved by a human |
| Panel, back office, blueprint, fixed test (per AIOC) | Interface, AI workspace, source file, readiness check | Built from the unit's blueprint |

The number and arrangement of units are left to AI at the time.

§13, §16–17, §19–20

---

**5. Who decides what**

- **Governance seat (GOV):** Approves designs, rule changes, the dial and the mandate. It keeps purpose, strategy, capital, risk appetite and conflicts. It holds the veto and the stop.
- **Top Management (TM):** Runs the operation within the envelope and requests anything beyond it.
- **`[ORG]AION`:** Designs and proposes. It may reject proposals alone, but applies changes only with the seat's signature or within a signed dial. It never runs the operation.
- **AI units:** Act only within the authority granted to them.

**AI can never:**
- be accountable or hold a human position;
- do Human Floor work;
- sign a listed decision;
- serve as the stop;
- widen its own access;
- route a report, objection or stop;
- declare its own success.

§7, §12–16, §18, §20

---

**6. How a human stays in control and accountable**

- **Accountability:** A human position is accountable for every output.
- **Signatures:** Every signature needs a fresh live sign-in (HF-10).
- **Widening:** Any grant or widening of access, budget or authority needs a signature.
- **Standing approvals:** These cover only changes that can be undone and do not widen anything.
- **Stop and gateway:** The stop and the gateway sit outside every AI. The gateway fails closed.
- **Direct routes:** Reports, objections and stops reach the human above directly, never through AI.
- **Chief of Staff:** It cannot drop or delay anything, and the raw record stays open to its position.
- **Checked reports:** Top Management's reports are checked by an independent party.
- **Recorded decisions:** Every rule change records the deciding position's own words.
- **Authority ceiling:** No act may exceed the original requester's authority.

§3, §7, §13.3, §14.5, §15, §16, §20

---

**7. Staying current and changing size**

**49GAION itself** stays current through 49GAION Self-Improvement. Its Library grows from contributions, each approved by its governing seat.

**Each organisation** stays current in two ways:
- Its `[ORG]AION` watches 49GAION's Standard, Blueprint and Library and proposes updates. Nothing enters without the seat's decision.
- Details are re-decided by AI as AI improves.

**Growing and shrinking** happens through Structural Adaptation. The organisation starts small, with processes sharing one AIOC. The `[ORG]AION` proposes splits when a process outgrows its home and merges when work shrinks. It weighs cost and never merges a part with its checker. A human decides each change.

Top Management's lessons feed the organisation's own Standard, Blueprint and Library.

§4, §8, §12.5, §14.4, §15.1

---

**8. Ownership and "Powered by 49GAION"**

**The organisation owns:**
- its `[ORG]AION`;
- its Standard, Blueprint and Library, treated as its IP;
- its records;
- its copies of Library parts.

It may stop its `[ORG]AION` or give back to the 49GAION Library by choice. Its working data never enters that Library.

**49GAION keeps:**
- the framework and Edition Maker;
- its names and marks, which are unlicensed.

It keeps no access and no organisation data after handover. Its texts are CC BY 4.0 and its code is Apache 2.0. The owner of 49GAION is named only in `LICENSE.md`, which is **NOT IN THE TEXT**.

**"Powered by 49GAION"** applies to all of an organisation's products once it uses any 49GAION item: an idea, a Library part, a blueprint or the Standard.

§10.7, §11, §12.4, §14

---

**9. Does it fit one person and a group of companies?**

Yes. Every request, from a single position with one task to a group of companies, goes through Edition Maker and becomes an `[ORG]AION`. The size changes; the shape does not.

- **One person:** Under the HOAC Assignment Model, which 49GAION promotes, one person can hold every position. The positions stay distinct parties.
- **Independence:** Where independence is needed, for example internal audit, it comes from outside the organisation.
- **A group of companies:** It is one organisation with one governance seat. A company whose law requires its own governing body gets a seat for that company alone. Acts are signed by a position of the company that acts.

§6.3–6.4, §10.1, §12.6

---

**10. Is it executable?**

**Strongest reasons it can work:**
1. A ready Library means work starts at once.
2. Hard safeguards sit outside every AI: the gateway, the stop, failing closed and the authority ceiling.
3. A clear human chain runs from the seat through the mandate to Top Management, with direct reporting routes.

**Biggest risks:**
1. **AI misdesign.** Answered: AI only proposes; engines challenge each other; fixed tests apply; humans sign.
2. **One person holding every position weakens checks.** Partly answered by outside independence, HF-18 and HF-19. The assignment protocol is "to be defined later", which is a 49GAION gap, not an AI choice.
3. **The organisation loosening safeguards after handover.** Answered on purpose: "hand over, then let go", within the law.

§6, §7, §9, §13, §15, §20

---

**11. What a new organisation would ask that the text cannot answer**

- **How to actually submit a request and what to do first.** The text points to `ADOPTING.md`.
- **Who owns or operates 49GAION.** The text points to `LICENSE.md`.
- **The range of HOAC assignment models.** These are "to be defined later".
- **Where the HOAC Assignment Model is recorded.** §6.4 records it in the Top Management Group, an AIOC, but says no AI reads it. §1.5 says no person's name is in the system. Where the person-to-position record lives is therefore unclear.
- **What is on 49GAION's own Human Floor signature list.** It is referenced but not given.
- **Who is liable if a handed-over edition is defective.**

§1.5, §6.4, §10.1, §11.5, §20.3

---

VERDICT: GAPS

### Round 5 · input `135ae1e6f7fa50f5…`

#### Reader 1 · gemini / gemini-4-argon · 05:50 UTC

[gemini / gemini-4-argon]

**1. What is 49GAION, in two sentences, and what exactly does an organisation receive from it?**
49GAION is an organisation design framework for building live, AI-native organisations from interchangeable AI and human parts. Instead of installing a static, pre-configured design, it delegates ongoing organisational design and adaptation to the organisation's own AI, while keeping authority and accountability in legal human positions. 

An organisation receives its own independent `[ORG]AION`—starting as a "core" AIOC made from the 49GAION Charter. This package includes the governance panel, the external tool gateway and stop mechanisms, the first version of the organisation's own Standard and Blueprint (incorporating its founding configuration and musts), and open access to the 49GAION Library. *(Sections 1, 3, 4, 10, 12, 13, Part E)*

**2. What makes it special: what does it do that a conventional way of designing an organisation, or of adding AI to one, does not?**
Conventional methods start with human jobs and bolt AI onto structures built around human limits (e.g., short memory, fatigue, single skills). 49GAION is "AI-native": it starts from the desired output and what AI can do, adding humans only where needed for power, gaps, and accountability. It replaces human-limit structures with one complete record, continuous multi-skill AI units, a shared work queue, and AI that brings humans only decisions. Furthermore, it is "live"—the organisation's own `[ORG]AION` continuously designs and reconfigures it as AI improves—and it records only legal human positions (`HOAC`), never natural persons or names, inside the system. *(Sections 1, 3, 4, 5, 6)*

**3. How does an organisation start with it: step by step, from the first request to a running operation?**
1. **Request & Intake:** The request goes to 49GAION Edition Maker (led by a human edition engineer, using a three-engine challenge rule) to capture identity, outputs, musts, and founding configuration.
2. **Handover:** Edition Maker forms the `[ORG]AION` core. The governance seat accepts it, issues fresh gateway keys, and 49GAION revokes its keys and deletes intake data.
3. **First Proposal:** The core takes the governance seat's brief and proposes a small initial organisation; the seat approves (or rejects for re-proposal).
4. **Mandate:** The governance seat delegates the operation to Top Management within a defined resource/cost envelope.
5. **Operation:** The Top Management Group builds and runs the operation, sending achievements back to governance. *(Sections 10, 13, 15, 19, Part E)*

**4. How is it carried out in practice: which parts must exist, what does each do, and who builds them?**
- **The Core (`[ORG]AION`):** Built by Edition Maker from the 49GAION Charter. Holds the governance seat (`[ORG]HOAC-GOV`), governance panel, and the organisation's Standard, Blueprint, and Library. It designs the organisation, proposes adaptations, and oversees reporting.
- **Gateway and Stop:** Delivered with the core by Edition Maker, running as code outside all AI. The gateway holds credentials, logs calls, and enforces signatures; the stop revokes credentials and halts units.
- **Top Management Group:** The first AIOC under the core, holding `[ORG]HOAC-TM`. It builds, plans, and runs all operational units (AIOCs, Pods, Cells) and tools.
- **Panels and Back Offices:** Built for every AIOC from its versioned blueprint (using Library patterns) for task control and AI workspace chat, covering each other if one fails. *(Sections 10, 12, 13, 16, 17, 18, 19, 20)*

**5. Who decides what: the governance seat, Top Management, the organisation's `[ORG]AION`, and the AI units? What can AI never do?**
- **Governance Seat (`[ORG]HOAC-GOV`):** Decides purpose, strategy, success measures, capital/resource balance, risk appetite, human-side mechanisms, rule/design approvals (or sets a standing "dial" for reversible, non-widening changes), and exercises veto/stop powers.
- **Top Management (`[ORG]HOAC-TM`):** Decides operational execution and builds operational units within its mandate's envelope.
- **`[ORG]AION` (Core):** Never runs operations; it proposes designs/changes, applies small changes within a signed dial, and may reject proposals on its own (since rejecting opens nothing).
- **AI Units / Chief of Staff:** Execute within granted authority. A Chief of Staff may act and sign for its human position under a signed grant, which legally remains the human position's decision.
- **What AI can never do:** Hold legal personhood or accountability, fill a Human Floor role (HF-01 to HF-19), widen its own authority/budget/access, alter the gateway/stop code, or intercept direct human reports, objections, or stops. *(Sections 3, 6, 7, 12, 13, 14, 15, 16, 18, 20)*

**6. How does a human stay in control and accountable?**
Every output and decision rests on a legal human position (`HOAC`). The Human Floor (HF-01 to HF-19) reserves critical functions—accountability, oversight, root keys, audit, and stopping—exclusively to humans. Control is enforced by hard technical safeguards outside AI's reach: a single fail-closed tool gateway (requiring valid signatures with fresh live sign-ins for listed decisions or authority widening) and external stop doors on every unit. AI acts only within explicit grants and the original requester's authority ceiling; human silence is never consent. Reports, objections, and stops bypass all AI to reach human positions directly, and human words are recorded separately from AI text in rule changes. *(Sections 3, 6, 7, 13, 14, 15, 16, 18, 20)*

**7. How does it stay current as AI improves, and how does the organisation grow or shrink over time?**
49GAION leaves operational details to AI at the time rather than freezing them in advance. The `[ORG]AION` continuously monitors 49GAION's central Standard, Blueprint, and Library for updates, and also receives internal operational achievements from Top Management and proposals from any unit, proposing upgrades to the governance seat. 

The organisation grows or shrinks through **Structural Adaptation**: it starts small with multiple processes sharing one AIOC. The `[ORG]AION` monitors operational records against costs; when a process outgrows its AIOC, it proposes splitting it into a new AIOC, and when work shrinks, it proposes merging units (never merging a part with the part that checks it). A human position decides every change. *(Sections 4, 8, 12, 14, 15, 19)*

**8. What does the organisation own, what stays with 49GAION, and when is a product "Powered by 49GAION"?**
- **Organisation owns:** Its `[ORG]AION`, its own Standard, Blueprint, and Library (its IP), its working data, operational records, and any copies taken from the 49GAION Library. At handover, 49GAION revokes its keys and deletes intake data.
- **Stays with 49GAION:** The 49GAION framework, Edition Maker, its central Standard, Blueprint, Protocol, Library, and its unlicensed names/marks (texts are CC BY 4.0; code is Apache 2.0).
- **"Powered by 49GAION":** Under 49GAION's rule, if an organisation uses even a single 49GAION idea, Library part, blueprint, or Standard, all its products are "Powered by 49GAION" (which in practice is always, as everything built rests in part on 49GAION). *(Sections 8, 9, 10, 11, 12, 14)*

**9. Does the same framework fit one person with one task and a group of companies? How?**
Yes. Every request to Edition Maker becomes an `[ORG]AION`—"the size changes, the shape does not." Because the system deals strictly with legal human positions (`HOAC`) rather than natural persons, one person can hold every distinct HOAC position in a single-task setup (recorded outside AI in the Top Management Group's HOAC Assignment Model, except where factual independence is required, like internal audit). Conversely, a group of companies operates as one organisation under one group governance seat, with local governance seats added for individual subsidiary companies where the law requires, and AIOCs nesting to any depth via Structural Adaptation. *(Sections 6, 10, 12, 15, 16, Part F)*

**10. Is it executable? The three strongest reasons it can work and the three biggest risks, and whether the text answers each risk or leaves it to the organisation's AI on purpose.**
Yes, it is executable.
- **Three reasons:** (1) Bootstrapping from a rich Library (49GAION Charter, patterns, templates) rather than a blank slate; (2) Hard technical containment (external fail-closed gateway, non-AI stop doors, multi-engine challenges); (3) Modularity (uniform typed ports/cards, dual panel/back-office interfaces that cover each other).
- **Three risks & text's response:** 
  1. *Over-delegation to a Chief of Staff (rubber-stamping listed decisions):* Answered by the text via HF-01/Section 16 (strict human legal accountability remains, fresh sign-in required for the grant, instant revocability) and left to the human's discretion.
  2. *Single-person holding all positions compromises checks:* Answered by the text (Section 6.3/HF-19 require factually external independent holders where law or checks demand independence, and Section 15.8 blocks conflicted governance signatures at the gateway).
  3. *Granular technical orchestration of APIs/ workflows:* Left on purpose to the organisation's AI at the time (Section 4) and upstream technical standards. *(Sections 4, 6, 7, 9, 13, 15, 16, 17, 20)*

**11. What would a new organisation ask that the text cannot answer?**
At the level of a complete framework definition (excluding commercial terms and matters intentionally left to the organisation's AI at the time), there are no missing conceptual answers. For practical execution, a new organisation would ask operational and legal onboarding questions that the text explicitly points to external documents to answer:
1. **Practical onboarding steps:** How to submit the initial request today (pointed to `ADOPTING.md`, Section 10.1).
2. **Exact technical specifications and schemas:** Detailed rules for cards, ports, and protocols (pointed to `upstream/49GAION-UPSTREAM.md`, Naming Standard, Operating Protocol, and AIOC definition, Preamble).
3. **Human-side assignment options:** The range of possible HOAC assignment models (left to a separate Top Management Group protocol "to be defined later", Section 6.4) and full license owner details (`LICENSE.md`, Section 11.5).

VERDICT: COMPLETE

#### Reader 2 · openai / gpt-6.1-sol · 05:53 UTC

[openai / gpt-6.1-sol]

1. **What it is and what the organisation receives.**  
49GAION is an organisation-design framework for assembling AI-native organisations from interchangeable AI units and human legal positions, starting with the required output rather than existing jobs (§§1–3). The organisation receives its own independent, living `[ORG]AION`: a governance-level core linked to 49GAION’s knowledge, initial organisation-specific Standard and Blueprint, its own Library, and the gateway and stop—not a finished operational design (§§10, 12–13; Part E).

2. **What makes it special.**  
It designs backwards from outputs and AI capabilities, adding humans where needed rather than adding AI to existing human jobs. Its organisation-specific AI continually redesigns the organisation using reusable Library parts, operational evidence and improving AI capabilities; humans approve changes. Design and governance remain separate from operational execution, while modular units can split, merge or change between AI and human provision subject to human-only duties. These are the text’s stated distinctions, not evidence that no conventional approach shares individual features (§§3–5, 12, 15–16).

3. **How an organisation starts.**  
1. Submit a request to Edition Maker.  
2. Under a human edition engineer, supply purpose, governance, outputs, quality, constraints, resources and founding settings; each production step receives two independent engine challenges.  
3. Receive the core, initial rules, gateway and stop.  
4. Governance accepts the edition; keys rotate and Edition Maker deletes organisational data.  
5. The core proposes a small organisation; governance approves or requests revision.  
6. Governance mandates Top Management.  
7. Top Management builds and runs the operation, with fixed tests ready before work begins.  

The actual submission channel is **NOT IN THE TEXT**; §10.1 refers to `ADOPTING.md` (§§10, 13, 15, 19–20; Part E).

4. **Required parts, functions and builders.**  
49GAION supplies its Standard, Blueprint, Library, Protocol and Edition Maker. Edition Maker, supervised by the human edition engineer, delivers the governance core and initial safeguards. The core holds governance, organisational rules, Library and governance panel; `[ORG]AION` designs and proposes. The Top Management Group builds and runs operations. Operational parts are AIOCs containing Cells or Pods, with Chiefs of Staff serving human positions. Each AIOC has a versioned blueprint, coded panel, AI-workspace back office and API-connected engines. The gateway and stops run outside AI; changes to their code require a human signature and a party other than the constrained AI (§§8–10, 13, 16–20).

5. **Who decides what; AI’s limits.**  
Governance retains purpose, strategy, success measures, risk appetite, capital, resource balance and ultimate authority; it approves organisational changes and delegates operations. Top Management runs operations within its mandate, seeking governance approval beyond its envelope. `[ORG]AION` designs, reviews, proposes and oversees—it never runs operations. AI units execute authorised work. AI cannot hold human positions, assume legal accountability, originate authority or exceed grants. A position’s own Chief of Staff may nevertheless sign—even listed decisions—under an expressly signed grant; the text attributes those acts to the human position, not independent AI decision-making (§§6–7, 12, 14–16, 18–20).

6. **Human control and accountability.**  
Every output has an accountable human position. Delegation has explicit limits; governance can veto, replace decisions, revoke mandates or stop operations. External gateways enforce authority and signatures; human-controlled stops revoke credentials without passing through AI. Reports, objections and stops have direct human routes, supported by independent audit and report checking. Humans approve tests and rule changes, with decision histories preserved. Each Chief-of-Staff grant requires fresh human sign-in and is revocable, although individual acts under a standing grant need not receive fresh human approval. These safeguards are handed over complete; subsequent stewardship belongs to the organisation (§§3, 7, 14–16, 18, 20).

7. **Keeping current; growing and shrinking.**  
`[ORG]AION` watches improvements in 49GAION’s Standard, Blueprint and Library, proposes adoption, and learns from operational achievements recorded in the organisation’s own rules and Library. Governance decides what enters; a signed dial can pre-authorise limited reversible changes that do not widen authority, access or budget. Structural Adaptation starts with shared processes, proposes separate AIOCs when work grows, and mergers when it shrinks, weighing costs and never merging a function with its checker. Top Management implements approved operational arrangements within its mandate (§§4, 12.5, 14–15, 19).

8. **Ownership and attribution.**  
The organisation owns its `[ORG]AION`, records and organisation-specific Standard, Blueprint and Library; copied upstream material remains under its applicable licence. It controls disclosure and optional contributions back. 49GAION retains its framework, central Library and Edition Maker—not organisational access or data after handover. Texts use CC BY 4.0, code Apache 2.0; names and marks are not licensed. Under 49GAION’s stated rule, using even one idea or component makes all the organisation’s products “Powered by 49GAION,” including after modification; the text expressly distinguishes that broader rule from enforceable licence terms (§§10.7, 11–12, 14).

9. **One task through a corporate group.**  
Yes. Every request produces an `[ORG]AION`; scale changes, the basic shape does not. A small operation can share processes within one AIOC, and one person may hold multiple distinct human positions where lawful. Required independence must remain real, using an outside holder when necessary. Larger organisations nest AIOCs and split or merge them as needs change. A corporate group has group governance, while companies retain their own governance seats where legally required, and acts are signed by positions of the acting company (§§6, 10.1, 12.6, 15–16).

10. **Executability: three strengths and three risks.**  
**Executable in principle, not demonstrated operationally here.**

**Three strongest reasons:**  
- A defined delivery-to-operation sequence assigns builders and decision-makers (§§10, 13, 19; Part E).  
- Versioned modular parts, interfaces and tests support assembly (§§8–9, 16–17, 20).  
- External gateways, stops and bounded mandates constrain execution (§§15, 20).

**Three biggest risks:**  
- Confident or correlated AI errors: addressed through challenges, output tests and human judgment, not eliminated (§§3, 20).  
- Concentrated human authority or broad Chief-of-Staff grants: addressed through grants, revocation, independent checks and conflict rules; residual risk remains (§§6–7, 15–16).  
- Integration, security and supplier failures: partly addressed by gateways and fallback interfaces; implementation details deliberately belong to organisational AI (§§3–4, 17, 20).

11. **What newcomers could ask that this text cannot answer.**  
- “Where exactly do I send my first request, and what are today’s submission instructions?” **NOT IN THE TEXT**: §10.1 sends readers to `ADOPTING.md`.  
- “What is the complete baseline list of decision types requiring gateway signatures?” **NOT IN THE TEXT**: §20.3 incorporates 49GAION’s own list without reproducing it; §7 supplies Human Floor categories but not that complete list.

By contrast, the eventual architecture, configurations, workflows and unit count are deliberately assigned to the organisation’s AI, not missing definition-level answers (§§4, 10.6, 16, 19; Part E). Commercial terms are excluded.

VERDICT: GAPS

#### Reader 3 · claude / claude-opus-5-5 · 05:54 UTC

[claude / claude-opus-5-5]

**1. What it is**
49GAION is an organisation design framework for building AI-native organisations from interchangeable AI parts (AIOCs) and human positions (HOAC). It sets principles and safeguards, then gives the design itself to AI (§1, §3, §4). An organisation receives its own `[ORG]AION`: the core AIOC, which contains:
- the first version of its own Standard and Blueprint,
- the governance panel,
- the gateway and the stop,
- access to the 49GAION Library.

The `[ORG]AION` holds the organisation's design and keeps building it. It is shown as "`<Brand>` AION, Powered by 49GAION" (§1.2, §10.5, §12, §13.1).

**2. What makes it special**
- It designs from the output and from what AI can do, adding people only where needed. Conventional design starts from people and jobs and adds AI (§3, §5).
- It is live, not a finished design installed from outside. The organisation's own `[ORG]AION` designs and updates it as AI improves (§4, §10.6).
- It draws on a shared, growing Library (§9).
- Only positions are recorded, never persons (§6).
- A fixed Human Floor applies (§7).
- The gateway and stop run as code outside every AI (§13.1, §20).
- Every step is challenged by other engines (§20.5).

**3. How to start**
1. A request goes to Edition Maker. Intake covers identity, governance seat, outputs, quality and a founding configuration (§10.1, §10.4).
2. The edition is formed, with each step done by one engine and challenged by two (§10.3, §10.5).
3. Handover happens when the governance seat accepts. 49GAION's keys are revoked and its data deleted. A rejected edition returns with the seat's reasons (§10.7).
4. The core proposes a small organisation, and the seat approves or rejects (§13.2).
5. The seat gives the mandate to Top Management (§15.2.3).
6. The Top Management Group builds and runs the operation (§19, Part E).

How a request is actually submitted sits in `ADOPTING.md`, outside the text (§10.1).

**4. Parts and builders**
| Part | What it does | Who builds it |
|---|---|---|
| Core | Governance root: holds the seat, rules, panel, gateway and stop | Edition Maker, from the Charter Library part (§13.1) |
| Gateway | Holds credentials, logs every call, checks signatures, fails closed (§20.3) | Installed with the core; changes need a human signature and a non-constrained party (§20.8) |
| Stop | Human port outside every AI (§20.2) | Installed with the core |
| Top Management Group | Hub of the operation | Builds the operation itself (§19) |
| Every AIOC | Blueprint, a code panel, and an AI back office that can rebuild the panel (§17) | Designed by the `[ORG]AION` (§12.1) |
| Chief of Staff | Serves each human position | Set up by that position (§16) |

Unit counts and arrangement are left to AI on purpose (§16).

**5. Who decides**
- **Governance seat (GOV):** decides on proposals, rules, purpose, strategy, capital, risk appetite, the envelope and gate requests. It holds the veto and the dial (§14.3, §15.2).
- **Top Management (TM):** runs the operation under its mandate (§15.2.3, §18).
- **`[ORG]AION`:** proposes, designs and plans, but never runs the operation. It may reject proposals alone, but applying needs a signature (§12.1, §14.3).
- **AI units:** act only within granted authority (§20.1, §20.9).

AI never:
- accepts accountability,
- holds a human position,
- grants itself access, budget or power,
- decides; whatever the Chief of Staff signs is the position's decision,
- holds the stop,
- carries reports, objections or stops on the protected route (§3, §7, §16, §20).

**6. Human control**
- Every output has an accountable human position (§3).
- The Human Floor (HF-01 to HF-19) applies (§7).
- Each signature needs a fresh live sign-in, and every widening needs a new signature (§7, §20.4).
- The stop sits outside AI and a restart needs a human decision. The gateway fails closed (§20.2, §20.3).
- Reports, objections and stops reach humans directly (§15.2.4, §18).
- The raw record is always open to the position (§16).
- Each change records the deciding position and its own words (§14.5).
- Reports are checked independently (§15.2.4).
- Chief of Staff grants can be narrowed or revoked at any time (§16).

**7. Staying current and changing size**
- The `[ORG]AION` watches 49GAION's Standard, Blueprint and Library and proposes updates. Nothing enters without the seat's decision (§12.5).
- Details change as AI improves (§4).
- Structural Adaptation proposes splits when a process outgrows its home and merges when work shrinks. A part is never merged with the part that checks it, and a human decides each change (§15.1).
- The gate handles growth beyond the envelope (§15.2.6).
- The rules grow from Top Management's experience (§14.4).
- 49GAION itself keeps current through Self-Improvement (§8).

**8. Ownership**
The organisation owns:
- its `[ORG]AION`,
- its Standard, Blueprint and Library, treated as its intellectual property,
- copies of the Library parts it has taken,
- its records and data, which are returned at handover (§10.7, §12.4, §14.1).

It may close its `[ORG]AION` at any time (§12.4).

49GAION keeps Edition Maker, its own Standard, Blueprint and Library, and its names and marks, which are not licensed. Its texts are under CC BY 4.0 and its code under Apache 2.0 (§10.1, §11.5).

"Powered by 49GAION" applies to all of an organisation's products if it uses any 49GAION item, even an idea. This is 49GAION's own rule, sitting above the licence (§11.1, §11.5).

**9. Scale**
Yes. Every request, "from a single position with one task to a group of companies," becomes an `[ORG]AION`; "the size changes, the shape does not" (§10.1).
- **One person:** may hold every position, which 49GAION promotes. The positions stay distinct parties, and the person works through each position's Chief of Staff (§6.3, §6.4, §16). Where independence is required, such as the internal audit (HF-19), it comes from outside the organisation (§6.3).
- **A group of companies:** one organisation with one governance seat. Companies whose law requires their own governing body get a seat for that company alone (§12.6).
- **Small to large:** Structural Adaptation starts with several processes in one AIOC and splits them as they grow (§15.1).

**10. Executability**
Strengths:
- Safeguards are enforced in code outside AI: the gateway, stop and fail-closed design (§20).
- It reuses an existing Library and starts small. Existing organisations move output by output (§9, §10.8, §15.1).
- It relies on multi-engine challenge, fixed tests and human signatures (§20.5, §20.6).

Risks:
- **AI design errors.** Answered by challenge, tests and human approval (§12.1, §20).
- **Concentration.** One person can hold every position and give the Chief of Staff full signing power. The text answers only with accountability and outside independence (§6.3, §16), so practical oversight is weak.
- **After handover, safeguards become amendable by the organisation.** This is left to the organisation on purpose, within the law (§4, §7).

**11. Open questions**
- **How to submit a request:** NOT IN THE TEXT. It is referred to `ADOPTING.md` (§10.1).
- **The range of assignment models:** NOT IN THE TEXT. The assignment protocol is "to be defined later" (§6.4).
- **Where the HOAC assignment record is kept before the Top Management Group exists:** NOT IN THE TEXT. The record lives only on the Top Management Group (§6.4), but that group is formed only after the first proposal and mandate (§13.2, Part E).
- Liability, price and service terms are outside the definition (commercial terms, or `LICENSE.md`).
- Engines, vendors and unit counts are left to AI on purpose, so they are not gaps.

VERDICT: GAPS

Powered by 49GAION
