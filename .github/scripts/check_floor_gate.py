"""human-floor-gate, the detector (DR-0053; Standard §4.4, item 20). Decides whether a change must
wait for a human approval of the review environment `human-floor` before it can merge.

Read from git, base against head, never from the working tree, so a change cannot alter what judges
it. The change needs the gate when it:
  - removes a type from the Standard's signature list (upstream/human-floor-signature-types.json),
    or from an [ORG]AION list kept here;
  - turns a type's floor from fixed into org-choice, or lowers a type's quorum, or drops `floor` or
    `quorum` from type_fields;
  - changes the trusted removal list (.github/signature-types-floor-removals.tsv);
  - removes or changes a protected clause (a row of kind clause) of a no-removal baseline
    (.github/no-removal/*.tsv).
The quorum the gate needs is the highest quorum among the types the change touches (1 by default),
read from the base. An unreadable base list fails closed: the gate is needed.
Output: lines `needed=true|false` and `quorum=N` appended to $GITHUB_OUTPUT when set, and the reasons
printed. Usage: check_floor_gate.py <base-rev> [<head-rev>]."""
import json, os, re, subprocess, sys

STD = "upstream/human-floor-signature-types.json"
REMOVALS = ".github/signature-types-floor-removals.tsv"
LIST_RE = re.compile(r"^(org-aion-signature-types/.+|(.*/)?[^/]+\.signature-types)\.json$")

def git(*a):
    r = subprocess.run(["git", *a], capture_output=True, text=True)
    return r.returncode, r.stdout

def show(rev, path):
    rc, out = git("show", f"{rev}:{path}")
    return out if rc == 0 else None

def files(rev):
    rc, out = git("ls-tree", "-r", "--name-only", rev)
    return set(out.splitlines()) if rc == 0 else set()

def types(text):
    doc = json.loads(text)
    return {t["id"]: t for t in doc["decision_types"]}, set(doc.get("type_fields") or [])

base = sys.argv[1]
head = sys.argv[2] if len(sys.argv) > 2 else "HEAD"
reasons, quorum = [], 1
bfiles, hfiles = files(base), files(head)
lists = sorted(p for p in bfiles if p == STD or LIST_RE.match(p))
for path in lists:
    b = show(base, path)
    try:
        btypes, bfields = types(b)
    except Exception:
        reasons.append(f"{path}: the base list cannot be read; the gate is needed (fail closed)")
        continue
    h = show(head, path)
    if h is None:
        reasons.append(f"{path}: the list is deleted")
        quorum = max([quorum] + [t.get("quorum", 1) for t in btypes.values() if isinstance(t.get("quorum", 1), int)])
        continue
    try:
        htypes, hfields = types(h)
    except Exception:
        continue  # signature-types-floor fails it; nothing is removed by an unreadable head
    for i, t in btypes.items():
        q = t.get("quorum", 1) if isinstance(t.get("quorum", 1), int) else 1
        if i not in htypes:
            reasons.append(f"{path}: type {i} is removed"); quorum = max(quorum, q); continue
        ht = htypes[i]
        if t.get("floor") == "fixed" and ht.get("floor") != "fixed":
            reasons.append(f"{path}: type {i} turns from fixed to {ht.get('floor')!r}"); quorum = max(quorum, q)
        hq = ht.get("quorum", 1)
        if isinstance(hq, int) and hq < q:
            reasons.append(f"{path}: the quorum of type {i} falls from {q} to {hq}"); quorum = max(quorum, q)
    for f in ("floor", "quorum"):
        if f in bfields and f not in hfields:
            reasons.append(f"{path}: type_fields drops {f}")
if show(base, REMOVALS) != show(head, REMOVALS):
    reasons.append(f"{REMOVALS} changes")
for path in sorted(p for p in bfiles if p.startswith(".github/no-removal/") and p.endswith(".tsv")):
    def clauses(text):
        return {tuple(l.split("\t")[:3]) for l in (text or "").splitlines() if not l.startswith("#") and len(l.split("\t")) > 2 and l.split("\t")[1] == "clause"}
    gone = clauses(show(base, path)) - clauses(show(head, path))
    for c in sorted(gone):
        reasons.append(f"{path}: the protected clause of {c[0]} is removed or changed: {c[2][:80]}")
needed = bool(reasons)
for r in reasons:
    print(f"::notice::human-floor-gate: {r}")
print(f"human-floor-gate: {'the human approval is needed' if needed else 'no Human Floor change; no approval needed'} (quorum {quorum})")
out = os.environ.get("GITHUB_OUTPUT")
if out:
    with open(out, "a") as fh:
        fh.write(f"needed={'true' if needed else 'false'}\nquorum={quorum}\n")
