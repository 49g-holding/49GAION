#!/usr/bin/env python3
"""ci-selftest (hub): must-fail and must-pass cases for the checks of this repository.
Each case builds a throwaway git repository, runs the check as it stands in this change,
and asserts the exit status and, for a must-fail case, the named error code in the output.
A must-fail case counts only when it fails on its own rule with that code."""
import json, os, pathlib, re, shutil, subprocess, sys, tempfile

HUB = pathlib.Path(__file__).resolve().parents[2]
S = HUB / ".github/scripts"
results = []

def sh(cwd, *a, env=None, check=True):
    r = subprocess.run(list(a), cwd=cwd, capture_output=True, text=True, env={**os.environ, **(env or {})})
    if check and r.returncode:
        raise RuntimeError(f"{a}: {r.stderr}")
    return r

def repo():
    d = pathlib.Path(tempfile.mkdtemp())
    sh(d, "git", "init", "-q", "-b", "main")
    sh(d, "git", "config", "user.email", "ci@example.invalid"); sh(d, "git", "config", "user.name", "ci")
    return d

def commit(d, msg="c"):
    sh(d, "git", "add", "-A"); sh(d, "git", "commit", "-q", "--allow-empty", "-m", msg)
    return sh(d, "git", "rev-parse", "HEAD").stdout.strip()

def expect(name, r, code=None):
    out = r.stdout + r.stderr
    if code is None:
        ok = r.returncode == 0
    else:
        ok = r.returncode != 0 and code in out
    results.append((name, ok, code or "pass"))
    print(f"{'ok  ' if ok else 'FAIL'} {name}: expected {'exit 0' if code is None else 'failure with ' + code}")
    if not ok:
        print("    " + out.replace("\n", "\n    "))

# ---------- dr-frozen ----------
def dr_case(name, mutate, code=None, base_mutate=None):
    d = repo()
    shutil.copytree(HUB / "decisions", d / "decisions")
    if base_mutate: base_mutate(d)
    base = commit(d, "base")
    mutate(d)
    commit(d, "head")
    expect("dr-frozen: " + name, sh(d, sys.executable, str(S / "check_dr_frozen.py"), base, check=False), code)

def idx(d): return d / "decisions/README.md"
def sub(p, a, b):
    t = p.read_text(encoding="utf-8"); assert a in t, a; p.write_text(t.replace(a, b, 1), encoding="utf-8")
def add_row(d, n, status):
    sub(idx(d), "\n\nPowered by", f"\n| [`{n}`]({n}-x.md) | 2026-10-14 | x | {status} |\n\nPowered by")
    (d / f"decisions/{n}-x.md").write_text(f"# {n}\n", encoding="utf-8")

# Record numbers follow the tree under test, so the cases hold as records are added.
# The next number is derived as dr-frozen derives it: from the highest number in the base index
# rows and record files (the base here is this tree's decisions/, i.e. main on a push run).
_idx = (HUB / "decisions/README.md").read_text(encoding="utf-8")
_nums = [int(n) for n in re.findall(r"^\| \[`DR-(\d{4})`\]", _idx, re.M)]
_nums += [int(f.name[3:7]) for f in (HUB / "decisions").glob("DR-[0-9][0-9][0-9][0-9]*.md")]
NEXT, SKIP, MISSING = (f"DR-{max(_nums) + k:04d}" for k in (1, 2, 4))

dr_case("unchanged tree passes", lambda d: None)
dr_case("edit DR-0004 fails", lambda d: (d / "decisions/DR-0004-49gaion-v1-3-0-hoac-cells-pods.md").open("a").write("x\n"), "DR-FROZEN-EDITED")
dr_case("delete DR-0001 fails", lambda d: (d / "decisions/DR-0001-49gaion-v1-0-0-day-zero.md").unlink(), "DR-FROZEN-DELETED")
dr_case("rename DR-0002 fails", lambda d: (d / "decisions/DR-0002-49gaion-v1-1-0-two-hubs-composition.md").rename(d / "decisions/DR-0002-renamed.md"), "DR-FROZEN-RENAMED")
dr_case("new record with next number passes", lambda d: add_row(d, NEXT, "proposed"))
dr_case("status flip proposed -> in force passes", lambda d: sub(idx(d), "| x | proposed |", "| x | in force |"), None, lambda d: add_row(d, NEXT, "proposed"))
dr_case("supersede with the newer record in the same change passes",
        lambda d: (add_row(d, NEXT, "proposed"), sub(idx(d), "loop of Self-Improvement | in force |", "loop of Self-Improvement | superseded by " + NEXT + " |")))
dr_case("supersede naming a missing record fails",
        lambda d: sub(idx(d), "loop of Self-Improvement | in force |", "loop of Self-Improvement | superseded by " + MISSING + " |"), "DR-INDEX-SUPERSEDER-MISSING")
dr_case("status flip in force -> proposed fails",
        lambda d: sub(idx(d), "loop of Self-Improvement | in force |", "loop of Self-Improvement | proposed |"), "DR-INDEX-STATUS-CHANGE")
dr_case("deleting an index row fails",
        lambda d: idx(d).write_text("\n".join(l for l in idx(d).read_text().splitlines() if "DR-0002" not in l) + "\n"), "DR-INDEX-ROW-DELETED")
dr_case("changing a row's date fails", lambda d: sub(idx(d), "| 2026-10-11 |", "| 2026-10-10 |"), "DR-INDEX-ROW-CHANGED")
dr_case("changing a row's title fails", lambda d: sub(idx(d), "day zero", "day one"), "DR-INDEX-ROW-CHANGED")
dr_case("new record skipping a number fails", lambda d: add_row(d, SKIP, "proposed"), "DR-NUMBER-SKIPPED")
dr_case("new record skipping past an index-only number fails",
        lambda d: add_row(d, SKIP, "proposed"), "DR-NUMBER-SKIPPED")
dr_case("new record reusing the highest number fails",
        lambda d: (d / f"decisions/DR-{max(_nums):04d}-another-subject.md").write_text(f"# DR-{max(_nums):04d}\n"), "DR-NUMBER-REUSED")
dr_case("new record reusing a number fails", lambda d: (d / "decisions/DR-0005-another-subject.md").write_text("# DR-0005\n"), "DR-NUMBER-REUSED")
dr_case("unreadable index fails closed", lambda d: idx(d).unlink(), "failing closed")

# ---------- no-removal ----------
def nr_case(name, mutate, code=None, script=S / "check_no_removal.py"):
    d = pathlib.Path(tempfile.mkdtemp())
    for p in ("49GAION.md", "49GAION-FRAMEWORK.md", "AGENTS.md", "README.md", "STATE.md", "state.json", "decisions", "guide", "references", "registers", "standards", "upstream"):
        src = HUB / p
        if src.exists():
            (shutil.copytree if src.is_dir() else shutil.copy)(src, d / p)
    mutate(d)
    # The check picks the baseline of the release the texts are at (state.json): v2.0 from v2.0.0 on, v1.4 before.
    env = {"NO_REMOVAL_ROOT": str(d), "NO_REMOVAL_DIR": str(HUB / ".github/no-removal")}
    expect("no-removal: " + name, sh(d, sys.executable, str(script), env=env, check=False), code)

def drop_hoac_lead(d):
    sub(d / "49GAION.md", "- **HOAC = Human", "- **H.O.A.C. = Human")
    assert "HOAC" in (d / "49GAION.md").read_text()
nr_case("current tree passes", lambda d: None)
nr_case("HOAC term taken off its definition lead (token left elsewhere) fails", drop_hoac_lead, "HOAC-TERM-NOT-ON-HEADING-OR-GLOSSARY-ROW")
nr_case("HOAC glossary row renamed (token left elsewhere) fails",
        lambda d: sub(d / "upstream/49GAION-UPSTREAM.md", "| **Human hub / `[ORG]HOAC-TM`** |", "| **Human hub** |"), "HOAC-TERM-NOT-ON-HEADING-OR-GLOSSARY-ROW")
nr_case("heading of v1.4.0 removed fails", lambda d: sub(d / "upstream/49GAION-UPSTREAM.md", "### 4.1 The HOAC", "### 4.1 The label"), "4.1 The HOAC")
nr_case("the stop line of the Human Floor deleted fails (review PA2)",
        lambda d: sub(d / "upstream/49GAION-UPSTREAM.md", "- **HF-12** The stop button\n", ""), "clause **HF-12** The stop button")
nr_case("'more human, never less' reworded in the guide fails (review PA2)",
        lambda d: sub(d / "guide/THE-49GAION-GUIDE-VERSION-2.md", "Organisations can be more human, never less", "Organisations can be more or less human"), "clause Organisations can be more human, never less")
def move_to_annex(d):
    p = d / "49GAION-FRAMEWORK.md"; t = p.read_text(encoding="utf-8")
    t = t.replace("HF-12 the stop; ", "", 1); t = t.replace("\nPowered by 49GAION", "\n- HF-12 the stop; \n\nPowered by 49GAION")
    p.write_text(t, encoding="utf-8")
nr_case("a protected clause moved to the list of superseded wording fails", move_to_annex, "clause HF-12 the stop")

# ---------- signature-types-floor ----------
STD = json.loads((HUB / "upstream/human-floor-signature-types.json").read_text())
FLOOR = [t["id"] for t in STD["decision_types"]]
def full(extra=(), **kw):
    return {"title": "x", "decision_types": [dict({"id": i}, **kw) for i in FLOOR] + [{"id": e} for e in extra]}

def sig_case(name, files, code=None, std=None, event="pull_request", tag=True, head_std=None, head_script=None, base_files=None):
    d = repo()
    (d / "upstream").mkdir()
    (d / "upstream/human-floor-signature-types.json").write_text(json.dumps(std or STD, indent=1))
    for p, body in (base_files or {}).items():
        (d / p).parent.mkdir(parents=True, exist_ok=True)
        (d / p).write_text(body if isinstance(body, str) else json.dumps(body, indent=1))
    base = commit(d, "base")
    if tag:
        sh(d, "git", "tag", "v1.4.0"); sh(d, "git", "tag", "vtest")
    if head_std is not None:
        (d / "upstream/human-floor-signature-types.json").write_text(json.dumps(head_std, indent=1))
    for p, body in files.items():
        (d / p).parent.mkdir(parents=True, exist_ok=True)
        (d / p).write_text(body if isinstance(body, str) else json.dumps(body, indent=1))
    script = S / "check_signature_types_floor.py"
    if head_script:  # the change also edits the script; the trusted copy from base still judges it
        (d / ".github/scripts").mkdir(parents=True); (d / ".github/scripts/check_signature_types_floor.py").write_text(head_script)
    commit(d, "head")
    env = {"EVENT": event, "BASE_SHA": base if event == "pull_request" else ""}
    expect("signature-types-floor: " + name, sh(d, sys.executable, str(script), env=env, check=False), code)
    if head_script:
        r = sh(d, sys.executable, ".github/scripts/check_signature_types_floor.py", env=env, check=False)
        print(f"     (the edited head copy would exit {r.returncode}; it never runs as the check)")

yaml_full = "decision_types:\n" + "".join(f"  - id: {i}\n" for i in FLOOR)
nostd = dict(STD, decision_types=[t for t in STD["decision_types"] if t["id"] != "restart-stopped-unit"])
sig_case("the Standard's own list passes", {})
sig_case("a full [ORG]AION list passes", {"org-aion-signature-types/acme.json": full(["approve-budget"])})
sig_case("a full YAML list passes", {"org-aion-signature-types/acme.yaml": yaml_full})
sig_case("a unit card citing one floor ID under tests/ passes",
         {"tests/cards/valid-card.json": {"code": "TenCELL-TMS", "signs": ["sign-contract"]}})
sig_case("restart-stopped-unit is not mistaken for a stop", {"x.signature-types.json": full()})
sig_case("a file outside the allowed paths holding one floor ID fails",
         {"config/policy.json": {"needs_signature": ["sign-contract"]}}, "SIG-FLOOR-ID-OUTSIDE-ALLOWED-PATH")
sig_case("a YAML list outside the allowed paths fails", {"config/types.yaml": yaml_full}, "SIG-FLOOR-ID-OUTSIDE-ALLOWED-PATH")
sig_case("a TOML file outside the allowed paths fails", {"config/types.toml": 'ids = ["commit-money"]\n'}, "SIG-FLOOR-ID-OUTSIDE-ALLOWED-PATH")
sig_case("a YAML list missing a type fails",
         {"org-aion-signature-types/acme.yml": yaml_full.replace("  - id: legal-filing\n", "")}, "SIG-LIST-MISSING-TYPE")
sig_case("an extra key enforced: false fails", {"org-aion-signature-types/acme.json": full(enforced=False)}, "SIG-KEY-NOT-ALLOWED")
sig_case("a top-level exempt_units key fails",
         {"org-aion-signature-types/acme.json": dict(full(), exempt_units=["TenCELL-TMS"])}, "SIG-KEY-NOT-ALLOWED")
sig_case("a list holding types under another key fails",
         {"org-aion-signature-types/acme.json": {"types": FLOOR}}, "SIG-LIST-NO-DECISION-TYPES")
for nh in ("stop-unit", "disconnect-port", "revoke-ai-access", "narrow-ai-access", "raise-to-human"):
    sig_case(f"a list naming the never-held '{nh}' fails", {"org-aion-signature-types/acme.json": full([nh])}, "SIG-NEVER-HELD-TYPE-LISTED")
sig_case("removing a type from the Standard's file fails", {}, "SIG-TYPE-REMOVED-FROM-STANDARD", head_std=nostd)
sig_case("a change that edits the script and removes a type fails (base copy judges)", {},
         "SIG-TYPE-REMOVED-FROM-STANDARD", head_std=nostd, head_script="import sys\nprint('edited: always clean')\nsys.exit(0)\n")
sig_case("push to main reads the floor from the release tag, not from head", {},
         "SIG-TYPE-REMOVED-FROM-STANDARD", head_std=nostd, event="push")
sig_case("push to main with no release tag fails closed", {}, "SIG-FLOOR-UNREADABLE", event="push", tag=False)
# Removal by the trusted removal list (DR-0049): the list on base names the type and its record.
RML = ".github/signature-types-floor-removals.tsv"
rml = "# note\nid\tdr\treason\nrestart-stopped-unit\tDR-9001\ttest\n"
REC = "# DR-9001 · removal\n\n- **Decided by:** the governing seat (GOV) of 49GAION.\n\n1. `restart-stopped-unit` leaves the list.\n"
sig_case("a type named on base's removal list, with its record in the tree, leaves the floor",
         {"decisions/DR-9001-removal.md": REC}, None, head_std=nostd, base_files={RML: rml})
sig_case("a type named on base's removal list without its record in the tree stays in the floor",
         {}, "SIG-TYPE-REMOVED-FROM-STANDARD", head_std=nostd, base_files={RML: rml})
sig_case("a removal list added in the same change does not count (base judges)",
         {RML: rml, "decisions/DR-9001-removal.md": REC}, "SIG-TYPE-REMOVED-FROM-STANDARD", head_std=nostd)
sig_case("push to main with the removal list and its record passes",
         {"decisions/DR-9001-removal.md": REC}, None, head_std=nostd, event="push", base_files={RML: rml})
sig_case("a directory named like the record does not count as the record",
         {"decisions/DR-9001-removal.md/keep": "x"}, "SIG-TYPE-REMOVED-FROM-STANDARD", head_std=nostd, base_files={RML: rml})
sig_case("with the record present but the type still in the Standard, an [ORG]AION list must keep it",
         {"decisions/DR-9001-removal.md": REC,
          "org-aion-signature-types/acme.json": {"title": "x", "decision_types": [{"id": i} for i in FLOOR if i != "restart-stopped-unit"]}},
         "SIG-LIST-MISSING-TYPE", base_files={RML: rml})
sig_case("a malformed removal list fails closed", {}, "SIG-FLOOR-UNREADABLE",
         base_files={RML: "id\tdr\treason\nrestart-stopped-unit\n"})
sig_case("a removal list without its header fails closed", {}, "SIG-FLOOR-UNREADABLE",
         base_files={RML: "restart-stopped-unit\tDR-9001\ttest\n"})
sig_case("a removal list in the tree is not a signature list and cites no floor ID out of place",
         {RML: rml}, None)
sig_case("a removal row citing a record that does not name the type fails, and the type stays (DR-0052)",
         {"decisions/DR-9001-removal.md": REC.replace("restart-stopped-unit", "some-other-type")}, "SIG-REMOVAL-RECORD-MISMATCH",
         head_std=nostd, base_files={RML: rml})
sig_case("a removal row citing a record that is not the governing seat's fails (DR-0052)",
         {"decisions/DR-9001-removal.md": REC.replace("the governing seat (GOV) of 49GAION", "the AI hub")}, "SIG-REMOVAL-RECORD-MISMATCH",
         head_std=nostd, base_files={RML: rml})
sig_case("a removal row citing an unrelated older record fails (review PA1)",
         {"decisions/DR-0001-day-zero.md": "# DR-0001\n\n- **Decided by:** the governing seat (GOV) of 49GAION.\n\n1. The starting point.\n"},
         "SIG-REMOVAL-RECORD-MISMATCH", head_std=nostd,
         base_files={RML: "id\tdr\treason\nrestart-stopped-unit\tDR-0001\tplanted\n"})
pol = dict(STD, type_fields=sorted(set(STD.get("type_fields", [])) | {"related_floor"}), decision_types=[dict(t, related_floor=["HF-12"]) if t["id"] == "restart-stopped-unit" else t for t in STD["decision_types"]])
sig_case("the Standard declaring a policy field in the same change passes", {}, None, head_std=pol)
# A base Standard with no declared policy fields, whatever the tree under test declares.
nodecl = dict({k: v for k, v in STD.items() if k != "type_fields"},
              decision_types=[{k: v for k, v in e.items() if k in ("id", "human_floor", "label", "note")} for e in STD["decision_types"]])
sig_case("a list using a policy field the base Standard has not declared fails",
         {"org-aion-signature-types/acme.json": full(related_floor=["HF-12"])}, "SIG-KEY-NOT-ALLOWED", std=nodecl)
sig_case("a list using a policy field the base Standard declares passes",
         {"org-aion-signature-types/acme.json": full(related_floor=["HF-12"])}, None, std=pol)

# ---------- ref-check: escaped section sign in schema text ----------
deps = os.environ.get("REF_DEPS")
if not deps or not pathlib.Path(deps, "protocol").is_dir() or not pathlib.Path(deps, "aioc").is_dir():
    results.append(("ref-check: the reference inputs (REF_DEPS) are present", False, "REF_DEPS"))
    print("FAIL ref-check: REF_DEPS is missing; the selftest fails, it never skips (DR-0052)")
else:
    for name, body, code in (("a valid escaped reference passes", "see Standard \\u00a74.4", None),
                             ("a broken escaped reference fails", "see Standard \\u00a799.9", "§99.9 does not exist")):
        d = pathlib.Path(tempfile.mkdtemp())
        shutil.copytree(HUB, d / "hub", ignore=shutil.ignore_patterns(".git", ".deps"))
        sh(d / "hub", "git", "init", "-q"); (d / "hub/upstream/probe.schema.json").write_text('{"description": "%s"}\n' % body)
        sh(d / "hub", "git", "add", "-A")
        env = {"HUB_DIR": ".", "PROTOCOL_DIR": f"{deps}/protocol", "AIOC_DIR": f"{deps}/aioc", "BASE_SHA": ""}
        expect("ref-check: " + name, sh(d / "hub", sys.executable, str(S / "check_refs.py"), env=env, check=False), code)

# ---------- no-persian (DR-0052) ----------
def np_case(name, files, code=None, msg="c", env=None):
    d = repo(); (d / "a.md").write_text("clean\n"); base = commit(d, "base")
    for p, body in files.items():
        (d / p).parent.mkdir(parents=True, exist_ok=True); (d / p).write_text(body, encoding="utf-8")
    commit(d, msg)
    expect("no-persian: " + name, sh(d, sys.executable, str(S / "no_persian.py"), env={"BASE": base, **(env or {})}, check=False), code)
np_case("a clean tree passes", {"b.md": "plain English\n"})
np_case("one letter of the Arabic block fails", {"b.md": "x \u0627 y\n"}, "PERSIAN-SCRIPT file: b.md:1")
np_case("one presentation-form letter fails", {"b.md": "x \ufb50 y\n"}, "PERSIAN-SCRIPT file: b.md:1")
np_case("one letter of Arabic Supplement fails", {"b.md": "x \u0750 y\n"}, "PERSIAN-SCRIPT file: b.md:1")
np_case("one letter of Arabic Extended-A fails", {"b.md": "x \u08a0 y\n"}, "PERSIAN-SCRIPT file: b.md:1")
np_case("a file name with one letter fails", {"\u0627.md": "plain\n"}, "PERSIAN-SCRIPT file name")
np_case("a new commit message with one letter fails", {"b.md": "plain\n"}, "PERSIAN-SCRIPT commit", msg="note \u0627")
np_case("a pull request title with one letter fails", {"b.md": "plain\n"}, "PERSIAN-SCRIPT pull request title", env={"PR_TITLE": "t \u0627"})
np_case("a branch name with one letter fails", {"b.md": "plain\n"}, "PERSIAN-SCRIPT branch name", env={"HEAD_REF": "oco/\u0627"})

# ---------- no-org-names: written variants (DR-0052) ----------
_v = pathlib.Path(tempfile.mkdtemp()) / "variants.md"
_v.write_text("a 49 G b\nFO\u200b49G\nForty Nine Group\nthe Founder\u2019s Office\nF049G\n49-G\n", encoding="utf-8")
_r = sh(HUB, "bash", str(S / "no-org-names.sh"), "--lines", str(_v), check=False)
results.append(("no-org-names: six written variants are flagged", len(_r.stdout.splitlines()) == 6, "6"))
print(f"{'ok  ' if len(_r.stdout.splitlines()) == 6 else 'FAIL'} no-org-names: six written variants are flagged ({len(_r.stdout.splitlines())})")
_g = pathlib.Path(tempfile.mkdtemp()) / "good.md"; _g.write_text("a disk of 49 GB\n", encoding="utf-8")
_r = sh(HUB, "bash", str(S / "no-org-names.sh"), "--lines", str(_g), check=False)
results.append(("no-org-names: a size in GB is not flagged", _r.stdout.strip() == "", "pass"))

# ---------- links (DR-0052) ----------
def ln_case(name, files, code=None):
    d = repo()
    for p, body in files.items():
        (d / p).parent.mkdir(parents=True, exist_ok=True); (d / p).write_text(body, encoding="utf-8")
    commit(d)
    expect("links: " + name, sh(d, sys.executable, str(S / "check_links.py"), check=False), code)
ln_case("a link to a file of the repository passes", {"a.md": "see [b](docs/b.md#x)\n", "docs/b.md": "b\n"})
ln_case("a link to a missing file fails", {"a.md": "see [the guide](guide/OLD.md)\n"}, "LINK-DEAD guide/OLD.md")
ln_case("a link under a heading of superseded wording is followed (DR-0054)",
        {"a.md": "body\n\n## Superseded wording, by version\n\n- [old](guide/OLD.md)\n"}, "LINK-DEAD guide/OLD.md")

# ---------- withdrawn-wording (DR-0054) ----------
WL = HUB / ".github/withdrawn-wording.tsv"
def wd_case(name, files, code=None, lst=None):
    d = repo()
    for p, body in files.items():
        (d / p).parent.mkdir(parents=True, exist_ok=True); (d / p).write_text(body, encoding="utf-8")
    commit(d)
    expect("withdrawn-wording: " + name, sh(d, sys.executable, str(S / "check_withdrawn_wording.py"), str(lst or WL), check=False), code)
wd_case("a text without withdrawn wording passes", {"a.md": "One person may hold every position; the positions stay distinct.\n"})
wd_case("the phrase one-person organisation fails", {"a.md": "49GAION never speaks of a one-person organisation.\n"}, "WITHDRAWN-WORDING one-person-organisation")
wd_case("the phrase in a code span still fails", {"a.md": "`one person organization`\n"}, "WITHDRAWN-WORDING one-person-organisation")
wd_case("the phrase in a decision record passes", {"decisions/DR-9001-x.md": "never a one-person organisation\n", "a.md": "clean\n"})
wd_case("a list of superseded wording fails", {"a.md": "body\n\n## Superseded wording, by version\n\n- old\n"}, "WITHDRAWN-WORDING superseded-wording-list")
_e = pathlib.Path(tempfile.mkdtemp()) / "empty.tsv"; _e.write_text("# no rows\n", encoding="utf-8")
wd_case("an empty list fails closed", {"a.md": "clean\n"}, "WITHDRAWN-WORDING-LIST", lst=_e)

# ---------- human-floor-gate, the detector (DR-0053) ----------
def fg_case(name, mutate, needed, base_mutate=None):
    d = repo()
    (d / "upstream").mkdir(); (d / ".github/no-removal").mkdir(parents=True)
    std = json.loads(json.dumps(STD)); std["type_fields"] = list(std.get("type_fields", [])) + ["floor", "quorum"]
    for t in std["decision_types"]: t["floor"] = "fixed"
    if base_mutate: base_mutate(std)
    (d / "upstream/human-floor-signature-types.json").write_text(json.dumps(std, indent=1))
    (d / ".github/no-removal/v2.0-baseline.tsv").write_text("x.md\tclause\tOrganisations can be more human, never less.\tHuman Floor\n")
    (d / ".github/signature-types-floor-removals.tsv").write_text("id\tdr\treason\n")
    base = commit(d, "base")
    mutate(d, std); commit(d, "head")
    r = sh(d, sys.executable, str(S / "check_floor_gate.py"), base, check=False, env={"GITHUB_OUTPUT": str(d / "out.txt")})
    got = (d / "out.txt").read_text() if (d / "out.txt").exists() else ""
    ok = r.returncode == 0 and f"needed={'true' if needed else 'false'}" in got
    results.append(("human-floor-gate: " + name, ok, "needed" if needed else "pass"))
    print(f"{'ok  ' if ok else 'FAIL'} human-floor-gate: {name}: expected needed={needed}")
    if not ok: print("    " + (r.stdout + r.stderr + got).replace("\n", "\n    "))
def w(d, std): (d / "upstream/human-floor-signature-types.json").write_text(json.dumps(std, indent=1))
fg_case("an ordinary change needs no approval", lambda d, s: (d / "a.md").write_text("x\n"), False)
fg_case("adding a type needs no approval", lambda d, s: w(d, dict(s, decision_types=s["decision_types"] + [{"id": "approve-x", "floor": "org-choice"}])), False)
fg_case("removing a type needs the approval", lambda d, s: w(d, dict(s, decision_types=s["decision_types"][1:])), True)
def flip(d, s):
    s = json.loads(json.dumps(s)); s["decision_types"][0]["floor"] = "org-choice"; w(d, s)
fg_case("turning a fixed type into org-choice needs the approval", flip, True)
def lowerq(d, s):
    s = json.loads(json.dumps(s)); s["decision_types"][0]["quorum"] = 1; w(d, s)
fg_case("lowering a quorum needs the approval", lowerq, True, base_mutate=lambda s: s["decision_types"][0].__setitem__("quorum", 2))
fg_case("changing the removal list needs the approval",
        lambda d, s: (d / ".github/signature-types-floor-removals.tsv").write_text("id\tdr\treason\nsign-contract\tDR-9001\tx\n"), True)
fg_case("changing a protected clause needs the approval",
        lambda d, s: (d / ".github/no-removal/v2.0-baseline.tsv").write_text("x.md\tclause\tOrganisations can be more human.\tHuman Floor\n"), True)
STDF = dict(STD, type_fields=list(STD.get("type_fields", [])) + ["floor", "quorum"], decision_types=[dict(t, floor="fixed") for t in STD["decision_types"]])
sig_case("the Standard's own list with floor fixed on every type passes", {}, None, std=STDF)
sig_case("a floor value other than fixed or org-choice fails",
         {"org-aion-signature-types/acme.json": full(floor="maybe")}, "SIG-FLOOR-VALUE", std=STDF)
sig_case("a quorum of zero fails", {"org-aion-signature-types/acme.json": full(quorum=0)}, "SIG-FLOOR-VALUE", std=STDF)
sig_case("a type of the Standard's own list not fixed fails", {}, "SIG-STD-FLOOR-NOT-FIXED",
         head_std=dict(STDF, decision_types=[dict(t, floor="org-choice") for t in STD["decision_types"]]), std=STDF)

# ---------- dr-source (DR-0053) ----------
def ds_case(name, body, code=None):
    d = repo(); (d / "decisions").mkdir(); (d / "decisions/README.md").write_text("x\n"); base = commit(d, "base")
    (d / "decisions/DR-9001-x.md").write_text(body); commit(d, "head")
    expect("dr-source: " + name, sh(d, sys.executable, str(S / "check_dr_source.py"), base, check=False), code)
GOOD = "# DR-9001\n\n- **Date:** 2026-10-29\n- **Decided by:** the governing seat (GOV) of 49GAION.\n- **Source:** the governing seat's words (translated): \"Confirmed.\"\n\n## Decision\n"
ds_case("a record with quoted words and a date passes", GOOD)
ds_case("a record citing its list by path and commit passes", GOOD.replace("the governing seat's words (translated): \"Confirmed.\"", "the list `upstream/PROPOSALS.md@0123abc` approved whole"))
ds_case("a record with no Source fails", GOOD.replace("- **Source:**", "- **Basis:**"), "DR-SOURCE-MISSING")
ds_case("a record whose Source quotes nothing fails", GOOD.replace(": \"Confirmed.\"", " in the chat"), "DR-SOURCE-NO-WORDS")
ds_case("a record with no date fails", GOOD.replace("- **Date:** 2026-10-29\n", ""), "DR-SOURCE-NO-DATE")

# ---------- person-names (fictional name; the real list is never used here) ----------
expect("person-names: selftest cases", subprocess.run([sys.executable, str(pathlib.Path(__file__).resolve().parent / "person_names_selftest.py")], capture_output=True, text=True))

bad = [n for n, ok, _ in results if not ok]
print(f"\nci-selftest: {len(results) - len(bad)}/{len(results)} cases as expected")
if bad:
    print("::error::ci-selftest: cases not as expected: " + "; ".join(bad)); sys.exit(1)
