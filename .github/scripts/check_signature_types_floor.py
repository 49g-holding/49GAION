"""signature-types-floor (hub). Guards the Standard's own Human Floor signature list
(upstream/human-floor-signature-types.json) and any [ORG]AION signature list kept in this
repository. Each [ORG]AION runs the same check in its own repositories as part of D-2.

Reading (DR-0042, item 1). The floor guards 49GAION's own Standard and every edition at the
handover. After the handover an organisation keeps its own floor list by its own rules, within
the law; the delivery test named above is withdrawn (DR-0032).

Trusted inputs. The workflow runs this script as taken from the base branch, never from the
head of the pull request, so a change cannot alter the check that judges it.
Floor. The floor (the set of type IDs nobody may drop) is read with git, never from the
working tree: on a pull request from its base commit (BASE_SHA); on a push or a manual run
from the highest release tag v<digits>... reachable from HEAD. Unreadable floor: fail closed.
Rules, each failing with the code shown:
  SIG-TYPE-REMOVED-FROM-STANDARD  the Standard's file lost a floor ID
  SIG-LIST-MISSING-TYPE           an [ORG]AION list lacks a floor ID
  SIG-LIST-NO-DECISION-TYPES      a list does not hold its types under decision_types[].id
  SIG-LIST-UNPARSEABLE            a list cannot be read
  SIG-KEY-NOT-ALLOWED             a key outside the allowlist (for example enforced, exempt_units)
  SIG-NEVER-HELD-TYPE-LISTED      a stop, a disconnection, narrowing or revoking AI access, or
                                  raising a matter to a human appears as a listed type
  SIG-FLOOR-ID-OUTSIDE-ALLOWED-PATH  a .json/.yaml/.yml/.toml file holding even one floor ID
                                  sits outside the allowed paths
  SIG-REMOVAL-RECORD-MISMATCH     a removal row cites a record that does not name the type, or
                                  that is not a decision of the governing seat (DR-0051)
Removal (DR-0049). A type leaves the floor only when the trusted removal list
.github/signature-types-floor-removals.tsv names it with the decision record that removes it, and
that record exists in the tree under test, is a decision of the governing seat (its "Decided by"
line names the governing seat (GOV)) and names the type's ID (DR-0005, item 1; DR-0051). A row
whose record exists but does not name the type, or is not the governing seat's, fails, and the
type stays in the floor. The list is read with git: on a pull request from its
base commit, so it must reach main first, in a .github pull request of its own; otherwise from
HEAD. A listed removal whose record is not yet in the tree waits, with a warning. The list is
tab-separated text, not a .json/.yaml/.yml/.toml file, so a copy of this check that predates it does
not read it as a signature list: lines starting with # are notes; the first other line is the header
id<TAB>dr<TAB>reason; each further line is one removal.
Lists sit under org-aion-signature-types/ or are named *.signature-types.(json|yaml|yml|toml).
Allowed paths where a file may cite a floor ID without being a list: ALLOWED_CITE below.
Key allowlist: top level TOP_KEYS; per type ENTRY_KEYS, widened only by the policy fields the
base Standard file declares in type_fields (the Standard's own file may declare them in the
same change), drawn from POLICY_VOCAB."""
import json, os, re, subprocess, sys, tomllib
try:
    import yaml  # PyYAML, pinned in the workflow
except ImportError:
    yaml = None

STD = "upstream/human-floor-signature-types.json"
EXT = (".json", ".yaml", ".yml", ".toml")
LIST_RE = re.compile(r"^(org-aion-signature-types/.+|(.*/)?[^/]+\.signature-types)\.(json|ya?ml|toml)$")
ALLOWED_CITE = ("tests/", ".github/tests/", "library/cards/", "registers/")
TOP_KEYS = {"decision_types", "title", "standard", "rule", "note", "type_fields"}
ENTRY_KEYS = {"id", "human_floor", "label", "note"}
POLICY_VOCAB = {"related_floor", "min_signer", "signers_required", "max_validity", "never_held"}
NEVER_HELD = re.compile(r"(^|-)(stop|halt|disconnect|disconnection)(-|$)|(^|-)(narrow|revoke|reduce)(-.*)?-access(-|$)|(^|-)(raise|escalate)(-.*)?-(to-)?human(-|$)")

errs = []
def err(code, where, msg):
    errs.append(f"::error file={where}::{code}: {msg}")

def git(*a):
    r = subprocess.run(["git", *a], capture_output=True, text=True)
    return r.returncode, r.stdout

def fail_closed(msg):
    print(f"::error::SIG-FLOOR-UNREADABLE: {msg}; failing closed."); sys.exit(1)

def load(path, data):
    if path.endswith(".json"): return json.loads(data)
    if path.endswith(".toml"): return tomllib.loads(data)
    if yaml is None: raise ValueError("PyYAML not installed")
    return yaml.safe_load(data)

def floor_rev():
    if os.environ.get("FLOOR_REV"): return os.environ["FLOOR_REV"]
    if os.environ.get("EVENT") == "pull_request":
        b = os.environ.get("BASE_SHA")
        if not b: fail_closed("pull request without BASE_SHA")
        return b
    rc, out = git("tag", "--merged", "HEAD", "--list", "v[0-9]*", "--sort=-v:refname")
    tags = [t for t in out.split() if re.fullmatch(r"v\d+\.\d+\.\d+", t)]
    if rc or not tags: fail_closed("no release tag v<major>.<minor>.<patch> reachable from HEAD")
    return tags[0]

rev = floor_rev()
rc, base_text = git("show", f"{rev}:{STD}")
if rc: fail_closed(f"cannot read {rev}:{STD}")
try:
    base_doc = json.loads(base_text)
    floor = {t["id"] for t in base_doc["decision_types"]}
except (ValueError, KeyError, TypeError):
    fail_closed(f"{rev}:{STD} is not a signature-type list")
if not floor: fail_closed(f"{rev}:{STD} holds no types")
declared = set(base_doc.get("type_fields") or []) & POLICY_VOCAB

REMOVALS = ".github/signature-types-floor-removals.tsv"
def removals_rev():
    if os.environ.get("EVENT") == "pull_request":
        return os.environ.get("BASE_SHA") or ""
    return "HEAD"
removed = set()
rrev = removals_rev()
rc, rtext = git("show", f"{rrev}:{REMOVALS}") if rrev else (1, "")
if rc == 0:
    rows = [ln.split("\t") for ln in rtext.splitlines() if ln.strip() and not ln.startswith("#")]
    if not rows or rows[0][:2] != ["id", "dr"]:
        fail_closed(f"{rrev}:{REMOVALS} is not a removal list (no header id, dr, reason)")
    for e in rows[1:]:
        tid, dr = (e[0].strip(), e[1].strip()) if len(e) >= 2 else (None, None)
        if not (isinstance(tid, str) and isinstance(dr, str) and re.fullmatch(r"DR-\d{4}", dr)):
            fail_closed(f"{rrev}:{REMOVALS} holds a malformed entry: {e!r}")
        _, tracked_recs = git("ls-files", "-s", "--", "decisions/")
        recs = [ln.split("\t", 1)[1] for ln in tracked_recs.splitlines()
                if ln.startswith("100644 ") and re.fullmatch(r"decisions/" + re.escape(dr) + r"-[^/]+\.md", ln.split("\t", 1)[1])]
        if tid not in floor:
            continue
        if recs:
            body = open(recs[0], encoding="utf-8", errors="replace").read()
            names = re.search(r"(?<![\w-])" + re.escape(tid) + r"(?![\w-])", body)
            by_gov = re.search(r"^\s*-\s*\*\*Decided by:\*\*[^\n]*governing seat \(GOV\)", body, re.M)
            if names and by_gov:
                removed.add(tid); print(f"floor: {tid} may leave the Standard's list, by {dr} ({recs[0]})")
            else:
                why = "does not name the type" if not names else "is not a decision of the governing seat (GOV)"
                err("SIG-REMOVAL-RECORD-MISMATCH", REMOVALS, f"the removal of {tid} cites {dr} ({recs[0]}), which {why}; {tid} stays in the floor")
        else:
            print(f"::warning::the removal of {tid} waits for its record {dr}, which is not in this tree")
print(f"floor from {rev}: {sorted(floor)}")

def check_list(path, doc, extra_fields=frozenset()):
    if not isinstance(doc, dict) or not isinstance(doc.get("decision_types"), list) or \
       not all(isinstance(t, dict) and isinstance(t.get("id"), str) for t in doc["decision_types"]):
        err("SIG-LIST-NO-DECISION-TYPES", path, "types must sit under decision_types, each with an id"); return set()
    for k in sorted(set(doc) - TOP_KEYS):
        err("SIG-KEY-NOT-ALLOWED", path, f"top-level key '{k}' is not allowed")
    tf = doc.get("type_fields")
    if tf is not None and path != STD:
        err("SIG-KEY-NOT-ALLOWED", path, "only the Standard's own file declares type_fields")
    allowed = ENTRY_KEYS | declared | (extra_fields & POLICY_VOCAB)
    ids = set()
    for t in doc["decision_types"]:
        ids.add(t["id"])
        for k in sorted(set(t) - allowed):
            err("SIG-KEY-NOT-ALLOWED", path, f"key '{k}' on type '{t['id']}' is not allowed")
        if NEVER_HELD.search(t["id"]):
            err("SIG-NEVER-HELD-TYPE-LISTED", path, f"'{t['id']}' is never listed and never held (a stop, a disconnection, narrowing or revoking AI access, raising to a human)")
    return ids

# 1. The Standard's own file
try:
    std_doc = json.loads(open(STD, encoding="utf-8").read())
except (OSError, ValueError):
    err("SIG-LIST-UNPARSEABLE", STD, "cannot read the Standard's list"); std_doc = None
if std_doc is not None:
    have = check_list(STD, std_doc, frozenset(std_doc.get("type_fields") or []) if isinstance(std_doc, dict) else frozenset())
    for m in sorted((floor - removed) - have):
        err("SIG-TYPE-REMOVED-FROM-STANDARD", STD, f"type ID removed from the Standard's list: {m}")

# A removed type that the Standard's file still lists keeps its full protection below.
std_have = have if std_doc is not None else set()
floor = (floor - removed) | (removed & std_have)

# 2. Every tracked machine-readable file
rc, out = git("ls-files", "-z")
tracked = [p for p in out.split("\0") if p.endswith(EXT) and p != STD]
tok = {i: re.compile(r"(?<![\w-])" + re.escape(i) + r"(?![\w-])") for i in floor}
nlists = 0
for p in sorted(tracked):
    try:
        raw = open(p, encoding="utf-8").read()
    except (OSError, UnicodeDecodeError):
        continue
    if LIST_RE.match(p):
        nlists += 1
        try:
            doc = load(p, raw)
        except Exception as e:
            err("SIG-LIST-UNPARSEABLE", p, str(e).splitlines()[0]); continue
        have = check_list(p, doc)
        missing = sorted(floor - have)
        for m in missing:
            err("SIG-LIST-MISSING-TYPE", p, f"missing type ID: {m}")
        print(f"{p}: {'FAIL' if missing else 'ok'} ({len(have - floor)} extra)")
        continue
    hits = sorted(i for i, r in tok.items() if r.search(raw))
    if hits and not p.startswith(ALLOWED_CITE):
        err("SIG-FLOOR-ID-OUTSIDE-ALLOWED-PATH", p, f"holds floor ID(s) {hits} outside the allowed paths; a signature list sits under org-aion-signature-types/ or is named *.signature-types.json")

print(f"{nlists} [ORG]AION list(s) in this tree")
for e in errs: print(e)
if errs:
    print("::error::An [ORG]AION may add decision types to the Human Floor signature list; it never removes one.")
    sys.exit(1)
print("signature-types-floor: clean")
