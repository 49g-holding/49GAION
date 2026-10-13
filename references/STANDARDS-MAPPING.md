# 49GAION terms and external standards

How 49GAION terms relate to terms in external standards and law.

**Reading note (DR-0004).** In the "Code" column, a `[ORG]HOAC-*` entry is a label carried on a part's card, never a unit code.

| 49GAION term | Code | External term | Source clause | Verification |
|---|---|---|---|---|
| Governing Body | `[ORG]HOAC-GOV` | governing body | ISO 37000:2021, 3.3.4 (also cited in CEN CWA 17995:2023) | verified |
| Top Management | `[ORG]HOAC-TM` | top management | ISO 37000:2021, 3.3.4 Note 3; ISO 9000:2015, 3.1.1 ("person or group of people who directs and controls an organization at the highest level"; the ISO management-system harmonized structure, used by ISO 9001:2015, takes this definition) | verified 2026-10-11 (the clause is in ISO 9000:2015, the vocabulary standard that ISO 9001:2015 refers to, not in ISO 9001 itself) |
| Accountability Seat | `[ORG]HOAC-ACS` | accountability (49GAION-coined seat name, not an ISO term) | ISO 37000:2021, 3.2.2 (contrast: responsibility, 3.2.3) | verified |
| GOV above TM | `[ORG]HOAC-GOV`, `[ORG]HOAC-TM` | governing body above top management | ISO 37000:2021, 3.3.4 Note 3 | verified (Standard §4.2) |
| Authority chain | - | delegation | ISO 37000:2021, 3.2.4 | verified |
| Authority record | - | constituting documents | ISO 37000:2021, 3.1.5 | verified |
| No accountability without authority; the delegator stays accountable | - | principle text | ISO 37000:2021, 4.2.2 | verified from the catalogue page |
| Human Oversight (in HOAC); Human Floor HF-03 | `[ORG]HOAC` | human oversight | EU AI Act (Regulation 2024/1689), Art. 14; there the scope is high-risk AI, 49GAION applies it to all AI work | verified (`2026-10-10-references-verified.md` row 2) |
| Stop port (Human Floor HF-12) | - | override and stop | EU AI Act Art. 14(4)(d)-(e) | verified (row 2) |
| Data protection officer (Human Floor HF-17) | - | data protection officer | GDPR (Regulation 2016/679), Art. 37-39 | verified (row 17) |
| Three Lines Model (Human Floor HF-19) | - | Three Lines Model | IIA, "The IIA's Three Lines Model" (2020) | verified (row 19) |
| Work Item; card | - | A2A task; A2A Agent Card | A2A protocol | aligned (Protocol §12) |
| Failure categories answered by the Protocol | - | specification failures, inter-agent misalignment, failed verification | MAST, Cemri et al., arXiv 2503.13657 | verified |
