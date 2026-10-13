"""signature-types-floor: every [ORG]AION signature-type list contains every decision type ID
of the Standard's Human Floor signature list (upstream/human-floor-signature-types.json on
the base branch, main). Extra types pass. Compared by type ID only, never by label. A change
that removes a type ID from the Standard's own file also fails."""
import json, os, subprocess, sys, pathlib

STD = "upstream/human-floor-signature-types.json"
GLOBS = ["org-aion-signature-types/**/*.json", "**/*.signature-types.json"]
base = os.environ.get("BASE_REF", "main")

def ids(doc, where):
    try:
        return {t["id"] for t in doc["decision_types"]}
    except (KeyError, TypeError):
        print(f"::error file={where}::not a signature-type list (needs decision_types[].id)"); sys.exit(1)

try:
    base_text = subprocess.run(["git", "show", f"origin/{base}:{STD}"], check=True, capture_output=True, text=True).stdout
except subprocess.CalledProcessError:
    base_text = pathlib.Path(STD).read_text(encoding="utf-8")
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
if not lists:
    print("no [ORG]AION signature-type lists in this tree")
if fail:
    print("::error::An [ORG]AION may add decision types to the Human Floor signature list; it never removes one.")
    sys.exit(1)
print("signature-types-floor: clean")
