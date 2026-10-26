"""no-removal: every heading, section/rule/decision id, term and key concept of the 49GAION
hub baseline is still present. Presence only, never definition text.

Baseline: the file named by NO_REMOVAL_BASELINE; by default the baseline of the release the texts
are at (state.json): .github/no-removal/v2.0-baseline.tsv from v2.0.0 on, generated from the clean
texts (DR-0047), and v1.4-baseline.tsv before it (taken from v1.4.0, carrying every v1.2.0 entry). A term that holds the token HOAC must
stand on its own place: a heading, the first cell of a table row (a glossary row) or the
bold lead of a definition line. The token anywhere else in the file does not count, so its
expansion may still change by decision while the term itself cannot be dropped."""
import os, re, sys, pathlib
root = pathlib.Path(os.environ.get("NO_REMOVAL_ROOT", "."))
def default_baseline():
    """The baseline of the release the texts are at: v2.0 from the clean version on (DR-0047),
    v1.4 before it. Read from state.json; v1.4 if it cannot be read."""
    d = pathlib.Path(os.environ.get("NO_REMOVAL_DIR", root / ".github/no-removal"))
    try:
        import json
        v = json.load(open(root / "state.json"))["version"].lstrip("v")
        major = int(v.split(".")[0])
    except Exception:
        major = 1
    return d / ("v2.0-baseline.tsv" if major >= 2 else "v1.4-baseline.tsv")
lst = pathlib.Path(os.environ["NO_REMOVAL_BASELINE"]) if os.environ.get("NO_REMOVAL_BASELINE") else default_baseline()
cache = {}
def text(p):
    if p not in cache:
        f = root / p
        cache[p] = f.read_text(encoding="utf-8") if f.exists() else None
    return cache[p]
def norm(s): return re.sub(r"\s+", " ", s).strip()
def places(t):
    """Headings, first cells of table rows and bold leads of definition lines."""
    out = [norm(m) for m in re.findall(r"^#{1,6}\s+(.*\S)\s*$", t, re.M)]
    for line in t.splitlines():
        s = line.strip()
        if s.startswith("|") and not re.match(r"^\|[\s:|-]+\|?$", s):
            out.append(norm(s.split("|")[1].replace("**", "")))
        m = re.match(r"^(?:[-*]\s+|\d+\.\s+)?\*\*(.+?)\*\*", s)
        if m:
            out.append(norm(m.group(1)))
    return out
alltext = "\n".join(p.read_text(encoding="utf-8") for p in root.rglob("*.md") if ".git" not in p.parts)
missing = []
for line in lst.read_text(encoding="utf-8").splitlines():
    if not line or line.startswith("#"): continue
    parts = line.split("\t"); path, kind, value = parts[0], parts[1], parts[2]
    if kind == "concept":
        if not re.search(value, alltext): missing.append(f"concept {parts[3]}")
        continue
    t = text(path)
    if t is None: missing.append(f"{path}: file missing"); continue
    heads = [norm(m) for m in re.findall(r"^#{1,6}\s+(.*\S)\s*$", t, re.M)]
    if kind == "heading": ok = norm(value) in heads
    elif kind == "id" and value.startswith("Heading "):
        n = value[8:]; ok = any(re.match(re.escape(n) + r"[.\s]", h + " ") for h in heads)
    elif kind == "id": ok = norm(value) in norm(t)
    elif "HOAC" in value:
        pat = re.compile(r"(?<![\w-])" + r"\s+".join(map(re.escape, value.split())) + r"(?![\w-])")
        ok = any(pat.search(p) for p in places(t))
        if not ok: missing.append(f"{path}: term {value} (HOAC-TERM-NOT-ON-HEADING-OR-GLOSSARY-ROW)"); continue
    else: ok = re.search(r"\s+".join(map(re.escape, value.split())), t) is not None
    if not ok: missing.append(f"{path}: {kind} {value}")
for m in missing: print(m)
if missing:
    print("::error::Items of the baseline are missing (listed above). Changes must be strictly additive; keep superseded wording with a label.")
    sys.exit(1)
print(f"no-removal: every baseline item is present ({lst.name})")
