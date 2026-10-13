"""no-removal: every heading, section/rule/decision id, term and key concept of the 49GAION
v1.2.0 hub baseline (.github/no-removal/v1.2-baseline.tsv) is still present. Presence only,
never definition text. HOAC terms match on the token HOAC, so its expansion may change."""
import re, sys, pathlib
root = pathlib.Path(".")
lst = root / ".github/no-removal/v1.2-baseline.tsv"
cache = {}
def text(p):
    if p not in cache:
        f = root / p
        cache[p] = f.read_text(encoding="utf-8") if f.exists() else None
    return cache[p]
def norm(s): return re.sub(r"\s+", " ", s).strip()
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
    elif "HOAC" in value: ok = "HOAC" in t
    else: ok = re.search(r"\s+".join(map(re.escape, value.split())), t) is not None
    if not ok: missing.append(f"{path}: {kind} {value}")
for m in missing: print(m)
if missing:
    print("::error::Items of the v1.2.0 baseline are missing (listed above). Changes must be strictly additive; keep superseded wording with a label.")
    sys.exit(1)
print("no-removal: every v1.2.0 baseline item is present")
