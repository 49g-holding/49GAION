#!/usr/bin/env bash
# Must-fail and must-pass cases for check_position_fields.py, run in a scratch repository.
set -eu
sd="$(cd "$(dirname "$0")/../scripts" && pwd)"; script="$sd/check_position_fields.py"
t=$(mktemp -d); cd "$t"; git init -q; mkdir decisions
run() { git add -A >/dev/null; if python3 "$script" >/dev/null 2>&1; then echo pass; else echo fail; fi; }
printf 'cell:\n  accountable_to: "[ORG]CELL-GOV"\n  label_holder: "<code of the human Cell>"\n  attached_to: "TenCELL-TMS"\n' > a.yaml
printf -- '- **Decided by:** the governing seat (GOV)\n' > decisions/DR-9999-x.md
[ "$(run)" = pass ] || { echo "FAIL must-pass: position codes"; exit 1; }
printf 'cell:\n  accountable_to: "Jane Example"\n' > b.yaml
[ "$(run)" = fail ] || { echo "FAIL must-fail: a name in accountable_to"; exit 1; }
rm b.yaml; printf -- '- **Decided by:** Jane Example\n' > decisions/DR-9998-y.md
[ "$(run)" = fail ] || { echo "FAIL must-fail: a name in Decided by"; exit 1; }
# Arrangement structure (check_arrangements.py), in a fresh scratch repository.
t2=$(mktemp -d); cd "$t2"; git init -q
arun() { git add -A >/dev/null; if python3 "$sd/check_arrangements.py" >/dev/null 2>&1; then echo pass; else echo fail; fi; }
expect() { [ "$(arun)" = "$1" ] || { echo "FAIL $1 expected: $2"; exit 1; }; rm -f c.json; }
printf '{"entry":"position","position":"[ORG]CELL-QA"}\n' > p.json
printf '{"arrangement":{"position":"[ORG]CELL-ENG","holders":3,"signing_rule":"majority","overseen":{"by":"[ORG]CELL-QA","timing":"pre"}},"decision_stamp":{"properties":{"accountable_member":{}}}}\n' > c.json
expect pass "complete arrangement"
printf '{"arrangement":{"position":"[ORG]CELL-ENG","holders":0}}\n' > c.json; expect fail "zero holders"
printf '{"arrangement":{"position":"[ORG]CELL-ENG","holders":2}}\n' > c.json; expect fail "two holders, no signing rule"
printf '{"decision_stamp":{"position":"x","occupants":[]}}\n' > c.json; expect fail "stamp without accountable member"
printf '{"arrangement":{"position":"[ORG]CELL-ENG","holders":1,"overseen":{"by":"[ORG]CELL-NONE","timing":"pre"}}}\n' > c.json; expect fail "overseer does not exist"
printf '{"arrangement":{"position":"[ORG]CELL-ENG","holders":1,"overseen":{"by":"[ORG]CELL-QA"}}}\n' > c.json; expect fail "no timing form"
printf '{"arrangement":{"position":"[ORG]HOAC-GOV","holders":1,"overseen":{"by":"[ORG]HOAC-TM","timing":"post"}}}\n' > c.json; expect fail "GOV overseen by a lower position"
echo "position-fields self-test: all cases behave as expected."
