#!/usr/bin/env python3
"""code-examples: every AIOC or HOAC code example in the 49GAION Standard and the
Naming Standard validates against the unit card schema (code field and the pattern for
its kind). Placeholders (with <...>, [MODULE]-style slots or *) are skipped.
HUB_DIR holds the Standard; SCHEMA is the path of unit-card.schema.json."""
import json, os, re, sys, pathlib
from jsonschema import Draft202012Validator

HUB = pathlib.Path(os.environ.get("HUB_DIR", "."))
schema = json.loads(pathlib.Path(os.environ["SCHEMA"]).read_text(encoding="utf-8"))
Draft202012Validator.check_schema(schema)
code = schema["properties"]["code"]
kind = {}
for rule in schema.get("allOf", []):
    k = rule.get("if", {}).get("properties", {}).get("unit_kind", {}).get("const")
    p = rule.get("then", {}).get("properties", {}).get("code")
    if k and p:
        kind[k] = p
if set(kind) != {"AIOC", "HOAC"}:
    print("::error::unit card schema must define code patterns for AIOC and HOAC"); sys.exit(1)
TOKEN = re.compile(r"[^\s`\"'(),;:]*(?:AIOC|HOAC)-[^\s`\"'(),;:]*")
bad, seen = [], set()
for rel in ("upstream/49GAION-UPSTREAM.md", "standards/49GAION-NAMING-STANDARD.md"):
    for n, line in enumerate((HUB / rel).read_text(encoding="utf-8").splitlines(), 1):
        for span in re.findall(r"`([^`]+)`", line):
            for t in TOKEN.findall(span):
                t = t.rstrip(".")
                if "/" in t or "<" in t or "*" in t or re.search(r"\[(?!ORG\])", t) or t.endswith("-"):
                    continue
                seen.add(t)
                k = "AIOC" if "AIOC-" in t else "HOAC"
                for sch in (code, kind[k]):
                    if not Draft202012Validator(sch).is_valid(t):
                        bad.append(f"{rel}:{n}: {t}"); break
if bad:
    print("\n".join(bad)); print("::error::Code examples that do not validate against the unit card schema (listed above)."); sys.exit(1)
if not seen:
    print("::error::no code examples found"); sys.exit(1)
print("code-examples: all valid:", ", ".join(sorted(seen)))
