#!/usr/bin/env python3
"""excluded-types-parity (DR-0010, Open items; non-required at first).
The Protocol's excluded-types list (spec/schemas/action-class.schema.json, decision_types
items 'not.enum', RULE-CLASS-EXCLUDED-TYPES) and the Standard's signature list
(upstream/human-floor-signature-types.json) must agree:
  1. every excluded type exists in the signature list;
  2. commit-money, grant-or-widen-access and every type bound to HF-01, HF-02 or HF-15 is excluded.
PROTOCOL_DIR points at a checkout of 49GAION-protocol (main)."""
import json, os, sys
proto = os.environ.get("PROTOCOL_DIR", ".deps/protocol")
sig = json.load(open("upstream/human-floor-signature-types.json"))
types = {t["id"]: t.get("human_floor") for t in sig["decision_types"]}
schema = json.load(open(os.path.join(proto, "spec/schemas/action-class.schema.json")))
excluded = set(schema["properties"]["decision_types"]["items"]["not"]["enum"])
need = {"commit-money", "grant-or-widen-access"} | {i for i, hf in types.items() if hf in ("HF-01", "HF-02", "HF-15")}
errors = [f"excluded type '{t}' is not in the signature list" for t in sorted(excluded - set(types))]
errors += [f"type '{t}' must be excluded from a standing action class but is not" for t in sorted(need - excluded)]
for e in errors:
    print("::error::" + e)
if errors:
    sys.exit(1)
print(f"excluded-types-parity: {len(excluded)} excluded types agree with the signature list.")
