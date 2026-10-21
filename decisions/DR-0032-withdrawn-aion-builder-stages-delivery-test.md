# DR-0032 · 49GAION — Withdrawn: the AION Builder, its six stages, the delivery test and two tests at v3

- **Date:** 2026-10-21
- **Decided by:** the governing seat (GOV) of 49GAION (holder in the private holders register)
- **Source:** the direction of the governing seat (GOV) of 49GAION of 2026-10-21 (translated), after the v1.7.0 release. From it:
  - "The AION Builder and its six stages are not something at all: everything has changed, and the Ionizer has changed too. These are what we want to build now."
  - "Delete that AION Builder. I have not named such a thing yet, and I do not know where it comes from. Its stages are our agenda now. Delete it entirely. Delete the Ionizer entirely too."
  - "The delivery test: I do not know what it is. For now we do not want it."
  - On the two tests at v3 named in the v1.7.0 release notes: "I do not know what they are."
- **Relation:** it supersedes DR-0001, item 1, as far as it names the AION Builder as a part, DR-0007, item 10 (the delivery test line D-4), and DR-0007, item 11 (c), as far as the delivery test result points to compensating controls. It closes three known limits of the v1.7.0 release: the AION Builder's stages, the delivery test in the `org-aion-record` schema, and the two tests at v3. It changes nothing in DR-0031.
- **Number:** this record takes the next free number at merge, after DR-0031

## Decision

1. **The AION Builder is withdrawn.** It is not a part of 49GAION, and no rule in force names it.
   - 49GAION has five parts: the governing seat (GOV), the 49GAION Standard, the 49GAION Protocol, the 49GAION Library and 49GAION Self-Improvement.
   - How 49GAION builds an organisation is stated in `49GAION.md`, section 2.3 (DR-0031). How that building is carried out is the work now in hand, and a later decision will set it.
2. **Its six stages and Ionize are withdrawn.** The six stages were Intake, TOM, Job descriptions and responsibilities, Ionize, Build AIOCs and Panels, and Assemble and connect. None of them is in force, and neither is any Ionize or Ionizer.
   - The design chain of the Library does not change. Source Lifecycle, Target Operating Model, Process and Position Design, and Delivery and Implementation stay as they are.
3. **The delivery test is withdrawn**, with its four lines, D-1 to D-4.
   - **The rules it checked stay in force on their own:**
     - each `[ORG]AION` has its own `[ORG]HOAC-GOV` (Standard §1.3, item 2);
     - the Human Floor (Standard §1.5);
     - the stop door of every AIOC, Pod and Cell (Standard §4.3);
     - the accountability chain (Standard §1.7, items 12 and 13).
   - **Two rules carried over.** Two rules were stated only in the lines of the test, and they are kept where they belong: the accountability chain is acyclic, ends at the Cell carrying the unscoped `[ORG]HOAC-GOV` and passes at least one human Cell carrying a HOAC label (an addition to Standard §1.7, item 12); and a Human Floor test that cannot be automated is a recorded human check by the bound seat (an addition to Standard §1.5, Tests).
   - **The reference organisations.** The Protocol's reference organisations are still checked against these rules, no longer as lines of a delivery test.
4. **The two tests at v3 are withdrawn.**
   - TEST-AION-BUILDER v3 goes with the AION Builder.
   - The Self-Improvement card names TEST-ORG-AION-SI v2, the version the Library register lists. Its v3 is withdrawn.
   - No other test changes.
5. **How it is removed.**
   - **49GAION-protocol.** The cards of the AION Builder (part and bot, v2 and v3) and its row in the Library register are removed. The `org-aion-record` schema loses its stages and its delivery test. Every text in force that named them is changed.
   - **49GAION-aioc.** The two sentences that named the AION Builder and the delivery test are removed.
   - **This repository.** The text that named them is removed. The headings and terms of this repository's no-removal list stay, each marked withdrawn. The ids D-1 to D-4 stay as rows marked withdrawn, because earlier records cite them. The full earlier text is in release v1.7.0. The places:
     - **the Standard:** §1.1, item 8; §1.2; §1.3, items 1 and 6; §1.4; §1.5, Tests (an addition); an example in §1.6; §1.7, item 12 (an addition); §4.4, items 6, 10, 11 and 12, with the reading note of item 12; §6.1, items 1 and 6; the glossary rows "AION Builder", "Delivery test" and "Unit";
     - **the Naming Standard:** R12, R13 and the table of section 3, Capability names;
     - **`49GAION.md`:** sections 1 and 6;
     - **the no-organisation-names fixture:** its example line on the AION Builder.
6. **Version.** The texts sit on main under the unreleased `v1.8.0`. The version labels and `state.json` stay at `v1.7.0` until GOV releases.

Powered by 49GAION
