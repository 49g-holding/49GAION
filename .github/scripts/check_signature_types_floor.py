"""signature-types-floor: every [ORG]AION signature-type list contains every decision type ID
of the Standard's Human Floor signature list (upstream/human-floor-signature-types.json on
the base branch, main). Extra types pass. Compared by type ID only, never by label. A change
that removes a type ID from the Standard's own file also fails. Any .json file with an array
holding two or more of the Standard's type IDs must sit at those paths and use the key
decision_types."""
import json, os, subprocess, sys, pathlib

STD = "upstream/human-floor-signature-types.json"
GLOBS = ["org-aion-signature-types/**/*.json", "**/*.signature-types.json"]
base = "main"  # source of truth is always main

def ids(doc, where):
    try:
        return {t["id"] for t in doc["decision_types"]}
    except (KeyError, TypeError):
        print(f"::error file={where}::not a signature-type list (needs decision_types[].id)"); sys.exit(1)

# Floor IDs come only from the main copy of the Standard's file, never from the PR branch.
r = subprocess.run(["git", "show", f"origin/{base}:{STD}"], capture_output=True, text=True)
if r.returncode != 0:
    print(f"::error::cannot read origin/{base}:{STD} (checkout needs fetch-depth: 0)"); sys.exit(1)
base_text = r.stdout
floor = ids(json.loads(base_text), f"origin/{base}:{STD}")
print(f"Standard list ({base}): {sorted(floor)}")
fail = False

head = ids(json.loads(pathlib.Path(STD).read_text(encoding="utf-8")), STD)
for m in sorted(floor - head):
    print(f"::error file={STD}::type ID removed from the Standard's list: {m}"); fail = True

lists = sorted({p for g in GLOBS for p in pathlib.Path(".").glob(g) if ".git" not in p.parts and str(p) != STD})
for p in lists:
    have = ids(json.loads(p.read_text(encoding="utf-8")), str(p))
    missing = sorted(floor - have)
    for m in missing:
        print(f"::error file={p}::missing type ID: {m}")
    print(f"{p}: {'FAIL, ' + str(len(missing)) + ' missing' if missing else 'ok'} ({len(have - floor)} extra)")
    fail |= bool(missing)
# Detect signature-type lists by content, in .json files only: any array holding two or more
# type IDs of the Standard's list (as strings or as values of its objects) marks the file as
# a list. Such a file must sit at one of the paths above and hold its types under the key
# decision_types. The Standard's own file is exempt.
def arrays(x):
    if isinstance(x, list):
        yield x
        for v in x: yield from arrays(v)
    elif isinstance(x, dict):
        for v in x.values(): yield from arrays(v)
def floor_ids_in(arr):
    found = set()
    for e in arr:
        vals = [e] if isinstance(e, str) else [v for v in e.values() if isinstance(v, str)] if isinstance(e, dict) else []
        found |= floor.intersection(vals)
    return found
def uses_key(doc):
    d = doc.get("decision_types") if isinstance(doc, dict) else None
    return isinstance(d, list) and bool(d) and all(isinstance(t, dict) and "id" in t for t in d)
allowed = {str(p) for p in lists}
for p in sorted(pathlib.Path(".").rglob("*.json")):
    if ".git" in p.parts or str(p) == STD:
        continue
    try:
        doc = json.loads(p.read_text(encoding="utf-8"))
    except (ValueError, UnicodeDecodeError):
        continue
    if not any(len(floor_ids_in(a)) >= 2 for a in arrays(doc)):
        continue
    if str(p) not in allowed:
        print(f"::error file={p}::signature-type list outside org-aion-signature-types/ and not named *.signature-types.json"); fail = True
    if not uses_key(doc):
        print(f"::error file={p}::signature-type list must hold its types under the key decision_types"); fail = True

if not lists:
    print("no [ORG]AION signature-type lists in this tree")
if fail:
    print("::error::An [ORG]AION may add decision types to the Human Floor signature list; it never removes one.")
    sys.exit(1)
print("signature-types-floor: clean")
