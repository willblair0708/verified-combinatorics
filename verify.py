#!/usr/bin/env python3
"""Independent verifier for the sets in this repository (no dependencies, Python 3 only).

A set S of vectors in {0,1}^n, with addition taken componentwise over the integers:
  - S is a B_2 set (Sidon) iff all sums a+b (a, b in S) are distinct as vectors.
  - S is a B_3 set        iff all sums a+b+c (a, b, c in S) are distinct as vectors.
Equivalently, the only solutions to the defining equation are the trivial (multiset-equal) ones.

Usage:
  python3 verify.py                       # verify every witness file in this repo, print a table
  python3 verify.py path/to/set.txt b2    # verify one file as a B_2 (Sidon) set
  python3 verify.py path/to/set.txt b3    # verify one file as a B_3 set

Each witness file lists one vector per line as a 0/1 string (lines beginning with '#' are ignored;
the single vector of {0,1}^0 may be written as '()').
"""
import os
import sys
from itertools import combinations_with_replacement as cwr


def load(path):
    vecs = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if line == "()":
                vecs.append(())
                continue
            vecs.append(tuple(int(c) for c in line))
    return vecs


def is_Bh(vecs, h):
    """Return (ok, num_sums_or_collision). Verifies all h-fold sums are distinct."""
    if not vecs:
        return True, 0
    n = len(vecs[0])
    if any(len(v) != n for v in vecs):
        return False, "ragged vectors"
    if any(any(c not in (0, 1) for c in v) for v in vecs):
        return False, "non-binary entry"
    if len(set(vecs)) != len(vecs):
        return False, "duplicate vector"
    sums = set()
    for combo in cwr(vecs, h):
        s = tuple(sum(combo[t][k] for t in range(h)) for k in range(n))
        if s in sums:
            return False, "sum collision"
        sums.add(s)
    return True, len(sums)


def load_ints(path):
    """Load one integer per line (GF(2)^n element as a bitmask); '#' lines ignored."""
    out = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            out.append(int(line))
    return out


def is_gf2_sidon(elems):
    """GF(2)^n Sidon: all pairwise XORs distinct (no four distinct elements XOR to 0)."""
    if len(set(elems)) != len(elems):
        return False, "duplicate element"
    seen = set()
    for i in range(len(elems)):
        for j in range(i + 1, len(elems)):
            x = elems[i] ^ elems[j]
            if x == 0 or x in seen:
                return False, "XOR collision"
            seen.add(x)
    return True, len(seen)


def verify_all():
    here = os.path.dirname(os.path.abspath(__file__))
    rows = []
    for sub, h, label in [("sidon-A309370", 2, "B_2"), ("b3-binary", 3, "B_3")]:
        d = os.path.join(here, sub)
        if not os.path.isdir(d):
            continue
        for fn in sorted(os.listdir(d)):
            if not fn.endswith(".txt"):
                continue
            vecs = load(os.path.join(d, fn))
            n = len(vecs[0]) if vecs else 0
            ok, info = is_Bh(vecs, h)
            rows.append((fn, label, n, len(vecs), ok, info))
    # GF(2)^n Sidon sets (integers per line, XOR semantics)
    gd = os.path.join(here, "gf2-sidon-A394031")
    if os.path.isdir(gd):
        for fn in sorted(f for f in os.listdir(gd) if f.endswith(".txt")):
            elems = load_ints(os.path.join(gd, fn))
            n = max(elems).bit_length() if elems else 0
            ok, info = is_gf2_sidon(elems)
            rows.append((fn, "GF2", n, len(elems), ok, info))
    print(f"{'file':28s} {'type':5s} {'n':>3s} {'size':>5s}  verified")
    all_ok = True
    for fn, label, n, size, ok, info in rows:
        all_ok &= ok
        print(f"{fn:28s} {label:5s} {n:3d} {size:5d}  {'YES' if ok else 'NO ('+str(info)+')'}")
    print("\nALL VERIFIED:", all_ok)
    return 0 if all_ok else 1


if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.exit(verify_all())
    path = sys.argv[1]
    h = 3 if (len(sys.argv) > 2 and sys.argv[2].lower() == "b3") else 2
    vecs = load(path)
    ok, info = is_Bh(vecs, h)
    print(f"{path}: n={len(vecs[0]) if vecs else 0} size={len(vecs)} "
          f"B_{h} verified={ok} ({info})")
    sys.exit(0 if ok else 1)
