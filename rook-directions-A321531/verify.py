#!/usr/bin/env python3
"""Standalone verifier for A321531 (max distinct rook directions). No deps.
Counts distinct direction classes of a witness permutation, and re-confirms a(n) for small n
by exhaustive search (calibration against the externally-known OEIS terms a(2..10))."""
import sys, itertools
from math import gcd

def directions(perm):                       # perm: 0-based list (row per column)
    n = len(perm); s = set()
    for i in range(n):
        for j in range(i + 1, n):
            da = j - i; db = abs(perm[j] - perm[i]); g = gcd(da, db)
            s.add((min(da // g, db // g), max(da // g, db // g)))
    return s

def amax(n):
    best = 0
    for p in itertools.permutations(range(n)):
        c = len(directions(p)); best = max(best, c)
    return best

def load(path):
    for ln in open(path):
        ln = ln.strip()
        if ln and not ln.startswith('#'):
            return [int(x) - 1 for x in ln.split()]

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "a321531_n12_directions33.txt"
    p = load(path)
    n = len(p)
    assert sorted(p) == list(range(n)), "witness is not a permutation (rooks must be non-attacking)"
    d = directions(p)
    print(f"witness n={n}: {len(d)} distinct direction classes  (non-attacking: OK)")
    print(f"  classes: {sorted(d)}")
    print(f"=> a({n}) >= {len(d)}")
    print("calibration (exhaustive, must match OEIS A321531 a(2..10)=1,2,4,6,8,11,14,18,23):")
    known = [1, 2, 4, 6, 8, 11, 14, 18, 23]
    for m in range(2, 11):
        v = amax(m); print(f"  a({m})={v}  {'OK' if v == known[m - 2] else 'MISMATCH'}")
    print("\nNote: optimality of a(11)=28 and a(12)=33 is proven by the exhaustive branch-and-bound")
    print("solver search_bb.c (cc -O3 -o s search_bb.c; ./s calib; ./s 12). This Python verifier")
    print("re-checks the witness count and the small-n calibration with an independent code path.")
