#!/usr/bin/env python3
"""no-removal: every section ID and glossary term listed in .github/no-removal/v1.2-ids.txt
must still be present in the 49GAION Standard (upstream/49GAION-UPSTREAM.md).
Sections are matched against numbered headings; terms against glossary rows."""
import re, sys, pathlib
std = pathlib.Path("upstream/49GAION-UPSTREAM.md").read_text(encoding="utf-8")
secs = set(re.findall(r"^#{2,3}\s+([0-9]+(?:\.[0-9]+)*)\.?\s", std, re.M))
gl = std[std.index("## Glossary"):] if "## Glossary" in std else ""
terms = set(re.findall(r"^\| \*\*(.+?)\*\* \|", gl, re.M))
missing = []
for line in pathlib.Path(".github/no-removal/v1.2-ids.txt").read_text(encoding="utf-8").splitlines():
    line = line.strip()
    if not line or line.startswith("#"):
        continue
    kind, _, value = line.partition(" ")
    if (kind == "section" and value not in secs) or (kind == "term" and value not in terms):
        missing.append(line)
if missing:
    print("\n".join(missing))
    print("::error::Sections or glossary terms of v1.2.0 are missing from the Standard (listed above). Changes must be strictly additive; keep superseded wording with a label.")
    sys.exit(1)
print("no-removal: every v1.2.0 section and glossary term is present")
