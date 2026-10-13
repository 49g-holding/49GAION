#!/usr/bin/env python3
"""dr-frozen: decision records never change once on main.

Compared by number and path between the base (main) and the head of the change:
1. A record file DR-####-*.md that is on the base never changes: an edit, a rename or a
   deletion fails.
2. A new record takes the next free number: numbers run on from the highest on the base
   with no gap; a number already used fails.
3. The index (decisions/README.md) keeps every row. A row changes only in its Status cell,
   and only from "proposed" to "in force", or from "in force" to "superseded by DR-xxxx"
   where DR-xxxx is a newer record present on the base or in the same change.
   New rows must name a record file present in the head.
4. An index that cannot be read, on either side, fails closed.
Usage: check_dr_frozen.py <base-rev> [<head-rev>]   (head defaults to HEAD; both are commits)."""
import re, subprocess, sys

DIR = "decisions"
INDEX = f"{DIR}/README.md"
REC = re.compile(r"^decisions/(DR-(\d{4}))-[^/]+\.md$")
ROW = re.compile(r"^\|\s*\[?`?(DR-\d{4})`?\]?(?:\([^)]*\))?\s*\|(.*)\|\s*$")


def git(*a):
    r = subprocess.run(["git", *a], capture_output=True, text=True)
    return r.returncode, r.stdout


def files(rev):
    rc, out = git("ls-tree", "-r", "--name-only", rev, "--", DIR)
    if rc:
        fail_closed(f"cannot list {DIR}/ at {rev}")
    return {p: REC.match(p) for p in out.split() if REC.match(p)}


def blob(rev, path):
    rc, out = git("rev-parse", f"{rev}:{path}")
    return out.strip() if rc == 0 else None


def text(rev, path):
    rc, out = git("show", f"{rev}:{path}")
    return out if rc == 0 else None


def fail_closed(msg):
    print(f"::error::dr-frozen: {msg}; failing closed.")
    sys.exit(1)


def index(rev):
    t = text(rev, INDEX)
    if t is None:
        fail_closed(f"index {INDEX} unreadable at {rev}")
    rows = {}
    for line in t.splitlines():
        m = ROW.match(line)
        if m:
            cells = [c.strip() for c in m.group(2).split("|")]
            if m.group(1) in rows:
                fail_closed(f"index row {m.group(1)} appears twice")
            rows[m.group(1)] = (line.split("|")[1].strip(), cells)
    if not rows:
        fail_closed(f"index {INDEX} has no record rows at {rev}")
    return rows


def status(cells):
    return cells[-1].strip().strip("*").strip()


def main():
    base = sys.argv[1]
    head = sys.argv[2] if len(sys.argv) > 2 else "HEAD"
    errs = []
    bf, hf = files(base), files(head)
    bnum = {m.group(1): p for p, m in bf.items()}
    hnum = {}
    for p, m in hf.items():
        hnum.setdefault(m.group(1), []).append(p)
    # 1. frozen files
    for p, m in sorted(bf.items()):
        if p not in hf:
            moved = [q for q in hnum.get(m.group(1), [])]
            errs.append(f"DR-FROZEN-RENAMED {p} -> {moved[0]}" if moved else f"DR-FROZEN-DELETED {p}")
        elif blob(base, p) != blob(head, p):
            errs.append(f"DR-FROZEN-EDITED {p}")
    # 2. numbering
    # The next number follows the highest number on the base, in its record files or its index rows.
    top = max([int(n[3:]) for n in bnum] + [int(n[3:]) for n in index(base)], default=0)
    new = sorted({n for p, m in hf.items() if p not in bf for n in [m.group(1)]})
    for n, ps in sorted(hnum.items()):
        if len(ps) > 1:
            errs.append(f"DR-NUMBER-REUSED {n}: {', '.join(sorted(ps))}")
    for n in new:
        if n in bnum and bnum[n] not in hf:
            continue  # reported as a rename
        if n in bnum:
            errs.append(f"DR-NUMBER-REUSED {n}: already used by {bnum[n]}")
    fresh = sorted(int(n[3:]) for n in new if n not in bnum)
    for i, k in enumerate(fresh):
        if k != top + 1 + i:
            errs.append(f"DR-NUMBER-SKIPPED DR-{k:04d}: the next free number is DR-{top + 1 + i:04d}")
            break
    # 3. index
    bi, hi = index(base), index(head)
    have = set(hnum) | set(bnum)
    for n, (first, cells) in sorted(bi.items()):
        if n not in hi:
            errs.append(f"DR-INDEX-ROW-DELETED {n}")
            continue
        hfirst, hcells = hi[n]
        if hfirst != first or hcells[:-1] != cells[:-1] or len(hcells) != len(cells):
            errs.append(f"DR-INDEX-ROW-CHANGED {n}: only the Status cell may change")
            continue
        old, cur = status(cells), status(hcells)
        if old == cur:
            continue
        if old == "proposed" and cur == "in force":
            continue
        sm = re.fullmatch(r"superseded by `?(DR-\d{4})`?", cur)
        if old == "in force" and sm:
            tgt = sm.group(1)
            if tgt in have and int(tgt[3:]) > int(n[3:]):
                continue
            errs.append(f"DR-INDEX-SUPERSEDER-MISSING {n}: {tgt} is not a newer record on main or in this change")
            continue
        errs.append(f"DR-INDEX-STATUS-CHANGE {n}: '{old}' -> '{cur}' is not allowed")
    for n in sorted(set(hi) - set(bi)):
        if n not in hnum:
            errs.append(f"DR-INDEX-ROW-WITHOUT-RECORD {n}")
    for e in errs:
        print(f"::error::{e}")
    if errs:
        print("::error::Decision records are frozen (decisions/README.md). Add a new record; never edit, rename or delete one.")
        sys.exit(1)
    print(f"dr-frozen: clean ({len(bf)} frozen records, {len(fresh)} new)")


main()
