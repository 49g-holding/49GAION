"""make_no_removal_baseline: generate the no-removal baseline of a release from the texts as they stand.

Usage: make_no_removal_baseline.py <previous-baseline.tsv> <output.tsv> <file>...

For each named file, every heading, every section or rule id (§n.n, HF-nn, Rn) and, where
the file has a glossary table, every term in its first column, are written as items, in the
kinds check_no_removal.py reads (heading, id, term). Numbered headings also give a
"Heading n.n" id. Entries of the previous baseline for files not named are carried over
unchanged, as are its concepts. Presence only, never definition text (DR-0047, item 4)."""
import re, sys, pathlib
prev, out, files = sys.argv[1], sys.argv[2], sys.argv[3:]
def norm(s): return re.sub(r"\s+", " ", s).strip()
rows = []
carried = [l for l in pathlib.Path(prev).read_text(encoding="utf-8").splitlines()
           if l and not l.startswith("#") and (l.split("\t")[0] == "*" or l.split("\t")[0] not in files)]
for f in files:
    t = pathlib.Path(f).read_text(encoding="utf-8")
    seen = set()
    def add(kind, value, note=""):
        key = (kind, value)
        if value and key not in seen:
            seen.add(key); rows.append(f"{f}\t{kind}\t{value}" + (f"\t{note}" if note else ""))
    for h in re.findall(r"^#{1,6}\s+(.*\S)\s*$", t, re.M):
        add("heading", norm(h))
        m = re.match(r"^(\d+(?:\.\d+)*)[.\s]", norm(h))
        if m: add("id", "Heading " + m.group(1))
    for i in sorted(set(re.findall(r"§\d+(?:\.\d+)*", t))): add("id", i)
    for i in sorted(set(re.findall(r"\bHF-\d{2}\b", t))): add("id", i)
    if "NAMING-STANDARD" in f:
        for i in sorted(set(re.findall(r"\bR\d{1,2}\b", t)), key=lambda s: int(s[1:])): add("id", i)
    glossary = re.search(r"^## Glossary\s*$(.*?)(?=^## |\Z)", t, re.M | re.S)
    if glossary:
        for line in glossary.group(1).splitlines():
            s = line.strip()
            if s.startswith("|") and not re.match(r"^\|[\s:|-]+\|?$", s):
                raw = s.split("|")[1].strip()
                m = re.match(r"^\*\*(.+?)\*\*", raw)
                cell = norm(m.group(1) if m else raw.replace("**", ""))
                if cell and cell.lower() != "term": add("term", cell)
# Terms of the previous baseline for regenerated files are carried as long as they still stand in the file.
prev_rows = [l.split("\t") for l in pathlib.Path(prev).read_text(encoding="utf-8").splitlines() if l and not l.startswith("#")]
for f in files:
    t = pathlib.Path(f).read_text(encoding="utf-8")
    for r in prev_rows:
        if r[0] == f and r[1] == "term" and r[2] in t and f"{f}\tterm\t{r[2]}" not in rows:
            rows.append(f"{f}\tterm\t{r[2]}" + (f"\t{r[3]}" if len(r) > 3 else ""))
header = ["# no-removal baseline of v2.0.0, generated from the clean texts by .github/scripts/make_no_removal_baseline.py (DR-0047).",
          "# Columns: path, kind (heading | id | term | concept), value, note. Presence only, never definition text.",
          "# Entries for files not regenerated are carried from the previous baseline."]
pathlib.Path(out).write_text("\n".join(header + rows + carried) + "\n", encoding="utf-8")
print(f"{out}: {len(rows)} generated, {len(carried)} carried")
