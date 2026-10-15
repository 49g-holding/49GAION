#!/usr/bin/env python3
"""position-fields, arrangement structure (GOV 15 October 2026; non-required at first).
Structure only; no model name is hard-coded. In every YAML or JSON file read (on a pull request
the files it changes, BASE_SHA set; otherwise every tracked file), wherever an object has:
- an "arrangement" object: it has a "position"; its holder count ("holders": a number or a list)
  is at least 1; with more than one holder it records a non-empty "signing_rule";
- an "overseen" link inside an arrangement: it names its overseeing position ("by"), which must
  exist (a HOAC label [ORG]HOAC-..., or a position code declared in a "position" entry of a file
  read), and records a timing form ("timing": pre or post); an arrangement for a GOV position
  (code ending in HOAC-GOV) with an overseen link is rejected, since every other position is lower;
- a "decision_stamp" object (an instance or a schema with "properties"): it carries the field
  "accountable_member".
Self-test: .github/tests/position_fields_selftest.sh."""
import json, os, re, subprocess, sys
try:
    import yaml
except ImportError:
    yaml = None
def files():
    base = os.environ.get("BASE_SHA", "").strip()
    if base:
        out = subprocess.run(["git", "diff", "--name-only", "--diff-filter=AM", base + "...HEAD"], capture_output=True, text=True, check=True).stdout
    else:
        out = subprocess.run(["git", "ls-files"], capture_output=True, text=True, check=True).stdout
    return [f for f in out.split() if not f.startswith(".github/") and f.endswith((".yaml", ".yml", ".json"))]
def load(f):
    try:
        text = open(f, encoding="utf-8").read()
        if f.endswith(".json"):
            return [json.loads(text)]
        if yaml is None:
            print(f"::warning file={f}::PyYAML not available; YAML not read"); return []
        return [d for d in yaml.safe_load_all(text)]
    except Exception:
        return []
def walk(o):
    if isinstance(o, dict):
        yield o
        for v in o.values(): yield from walk(v)
    elif isinstance(o, list):
        for v in o: yield from walk(v)
docs = [(f, d) for f in files() for d in load(f)]
known = set()
for f, d in docs:
    for o in walk(d):
        p = o.get("position")
        if isinstance(p, dict) and isinstance(p.get("code"), str): known.add(p["code"])
        elif isinstance(p, str) and "arrangement" not in o and o.get("entry") == "position": known.add(p)
bad = 0
def err(f, msg):
    global bad
    print(f"::error file={f}::{msg}"); bad += 1
def exists(code):
    return isinstance(code, str) and (code.startswith("[ORG]HOAC-") or code in known or code.startswith("<"))
for f, d in docs:
    for o in walk(d):
        a = o.get("arrangement")
        if isinstance(a, dict):
            pos = a.get("position", o.get("position"))
            if isinstance(pos, dict): pos = pos.get("code")
            if not isinstance(pos, str) or not pos: err(f, "arrangement must name its position")
            h = a.get("holders")
            n = len(h) if isinstance(h, list) else h if isinstance(h, int) and not isinstance(h, bool) else None
            if n is None or n < 1: err(f, f"arrangement for {pos}: holder count must be at least 1")
            elif n > 1 and not str(a.get("signing_rule") or "").strip(): err(f, f"arrangement for {pos}: more than one holder needs a recorded signing_rule")
            ov = a.get("overseen")
            if ov is not None:
                if not isinstance(ov, dict): err(f, f"arrangement for {pos}: overseen must be an object"); continue
                if not exists(ov.get("by")): err(f, f"arrangement for {pos}: overseeing position {ov.get('by')!r} does not exist")
                if ov.get("timing") not in ("pre", "post"): err(f, f"arrangement for {pos}: overseen needs timing pre or post")
                if isinstance(pos, str) and pos.endswith("HOAC-GOV"): err(f, "GOV overseen by a lower position is rejected (no loops)")
        s = o.get("decision_stamp")
        if isinstance(s, dict):
            fields = s.get("properties", s) if isinstance(s.get("properties"), dict) else s
            if "accountable_member" not in fields: err(f, "decision_stamp lacks the accountable_member field")
if bad:
    print(f"::error::{bad} arrangement structure problem(s)."); sys.exit(1)
print("position-fields: arrangement structure is complete.")
