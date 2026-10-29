# DR-0053 · 49GAION — the review room's designs: `v2.2.0`

- **Date:** 2026-10-29
- **Decided by:** the governing seat (GOV) of 49GAION.
- **Source:**
  - The review room's review of the eleven public repositories, 29 October 2026, whose designs go beyond the corrections of DR-0052 and add rules or mechanisms. The AI hub weighed each against the complete definition and the governing seat's earlier decisions; the triage is kept by the AI hub.
  - The governing seat's words of 29 October 2026 (translated from Persian): "This new work they proposed: if you agree, and it is right, and it contradicts what I want nowhere, do the real request."
  - The entry of the private decision register that holds these words, by the SHA-256 of the entry as stored (for tracing, not as proof): `3032bf6e8c52fab7a8b2e5097f921cc3c737a1d9616f3c70a89cc484b74271fb`.
  - The record is prepared by the AI hub; the governing seat's merge is the decision.
- **Relation:** it adds to DR-0005 (the floor's removal path), DR-0007 (signatures, the gateway, the register) and DR-0042 (the safeguards that always hold). It removes and weakens nothing.

## Decision

1. **The floor list changes only by a human** (Standard §4.4, item 20). Each listed type carries `floor`, `fixed` or `org-choice`, and may carry `quorum`. Removing a type, turning `fixed` into `org-choice`, or changing a protected sentence of the Human Floor passes a human approval gate, read from the base of the change. In 49GAION's own repositories the gate is the hub's review environment `human-floor`, approved only with the governing seat's own credential; no bot approves it. Every type of 49GAION's list is `fixed`.
2. **A new credential is an event** (§4.4, item 21): recorded at the gateway by position, reported at once to the internal-audit line and the position above; an optional waiting period before a new GOV or TM credential signs a listed type; a stop is never delayed.
3. **Outside input taints the run** (§4.4, item 22): one external read taints the whole run; in it the gateway refuses sends, publications, writes outside the part's space, new targets and changes of permission without a deterministic check or the accountable position's approval; stored content keeps its label; the gateway, not the part, records the taint.
4. **A signature is bound to what it signs** (§4.4, item 23): it names the signing position and the credential, never a claim about the signer; it is bound to its subject by hash, single-use, within its validity, on a fresh sign-in; signer and executor differ by position and by credential.
5. **One event record** (§4.4, item 24; the Operating Protocol, the event record): one append-only, hash-chained record of the gateway's decisions, controls, stops, restarts, taints, clearances, approvals and credentials, each decision with its basis; a profile of the OpenTelemetry semantic conventions for generative AI, with 49GAION's own fields. The Protocol holds its schema, its conformance scenarios as traces that must pass or fail, and the checker; and, informative, how the gateway maps onto the current interfaces of agent tools and agent-to-agent calls.
6. **Conformance and proof** (Standard §1.8): a text proves nothing by itself; an implementation is conformant only when its own trace of the scenarios passes the checker; an `[ORG]AION` is proven only after one end-to-end acceptance run judged by the governance seat's measures; until then, "unverified".
7. **The checks.** The hub gains the gate `human-floor-gate` and `dr-source` (a new record names its source: words quoted, or the list it approves by path and commit, and a date); the signature list check reads `floor` and `quorum`; the Protocol's tests run the traces and the harder signature rules; the Protocol reports each Library pin against the latest release (`pin-lag`). A page for an organisation that adopts 49GAION, `ADOPTING.md`, opens the hub. The cold read of the complete definition is run again with equal inputs, each hashed.
8. **Not taken, with the reason.**
   - Removing the lists of superseded wording from the public texts: it reverses DR-0047, item 3, a decision of the governing seat; it waits for the seat's own word.
   - Renaming the Standard's file and splitting the large texts: every link and pin would move for no change of meaning; not now.
   - Failing commits whose author is the account that opens every pull request: it would block all work; the operating account is a setting of the governing seat.
   - Restating the complete definition's present-tense safeguards as wishes: a normative text states required behaviour, and every release says that nothing has run yet.
9. **Version.** The hub and the Operating Protocol move to `v2.2.0`. The AIOC repository is unchanged by this record. The Library's pins move at each mother's next release, and the Protocol's `pin-lag` report shows the lag until then.
10. **The cold read, and the definition made clearer.** The cold read of 29 October 2026 (`references/2026-10-29-test-cold-read-v2-2-raw.md`) found points of the complete definition unclear. Each is made clear by writing in what the governing seat has already decided or what another text already says, or, where the text was silent on who acts, by naming who decides:
   - a Chief of Staff signs for its position only under a grant the position has signed with a fresh live sign-in, and never a listed decision (DR-0052, item 2; Standard §4.4, item 8);
   - what a listed decision is, and what the founding configuration is;
   - success, and Top Management's reports, are checked by a party the governance seat names; the Standard's §1.3 is brought into line;
   - the raw sources of the intake are returned to the organisation and deleted from Edition Maker at the handover, as Edition Maker's requirements say;
   - what an organisation gives back enters under the licences, as `CONTRIBUTING.md` says;
   - until the governance seat signs a dial, there is none;
   - how a request is brought today is set out in `ADOPTING.md`.
   The test passed on the text as released, with DR-0051 in it; the points it left open, and why each is not a gap, are in the record, with one point raised to the governing seat: whether the record of the HOAC Assignment Model, kept in the Top Management Group, is part of the system (DR-0051, item 6).

Powered by 49GAION
