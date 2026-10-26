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
    for p in ("49GAION.md", "49GAION-FRAMEWORK.md", "AGENTS.md", "README.md", "STATE.md", "state.json", "decisions", "references", "registers", "standards", "upstream"):
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

# ---------- signature-types-floor ----------
STD = json.loads((HUB / "upstream/human-floor-signature-types.json").read_text())
FLOOR = [t["id"] for t in STD["decision_types"]]
def full(extra=(), **kw):
    return {"title": "x", "decision_types": [dict({"id": i}, **kw) for i in FLOOR] + [{"id": e} for e in extra]}

def sig_case(name, files, code=None, std=None, event="pull_request", tag=True, head_std=None, head_script=None):
    d = repo()
    (d / "upstream").mkdir()
    (d / "upstream/human-floor-signature-types.json").write_text(json.dumps(std or STD, indent=1))
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
pol = dict(STD, type_fields=["related_floor"], decision_types=[dict(t, related_floor=["HF-12"]) if t["id"] == "restart-stopped-unit" else t for t in STD["decision_types"]])
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
if deps:
    for name, body, code in (("a valid escaped reference passes", "see Standard \\u00a74.4", None),
                             ("a broken escaped reference fails", "see Standard \\u00a799.9", "§99.9 does not exist")):
        d = pathlib.Path(tempfile.mkdtemp())
        shutil.copytree(HUB, d / "hub", ignore=shutil.ignore_patterns(".git", ".deps"))
        sh(d / "hub", "git", "init", "-q"); (d / "hub/upstream/probe.schema.json").write_text('{"description": "%s"}\n' % body)
        sh(d / "hub", "git", "add", "-A")
        env = {"HUB_DIR": ".", "PROTOCOL_DIR": f"{deps}/protocol", "AIOC_DIR": f"{deps}/aioc", "BASE_SHA": ""}
        expect("ref-check: " + name, sh(d / "hub", sys.executable, str(S / "check_refs.py"), env=env, check=False), code)

# ---------- person-names (fictional name; the real list is never used here) ----------
expect("person-names: selftest cases", subprocess.run([sys.executable, str(pathlib.Path(__file__).resolve().parent / "person_names_selftest.py")], capture_output=True, text=True))

bad = [n for n, ok, _ in results if not ok]
print(f"\nci-selftest: {len(results) - len(bad)}/{len(results)} cases as expected")
if bad:
    print("::error::ci-selftest: cases not as expected: " + "; ".join(bad)); sys.exit(1)
