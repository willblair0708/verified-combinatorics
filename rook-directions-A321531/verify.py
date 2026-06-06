#!/usr/bin/env python3
"""Standalone verifier for A321531 (max distinct rook directions). No deps.
Counts distinct direction classes of a permutation, and (optionally) re-confirms a(n) for small n."""
import sys, itertools
from math import gcd
def directions(perm):                       # perm: 0-based list (column per row)
    n=len(perm); s=set()
    for i in range(n):
        for j in range(i+1,n):
            da=j-i; db=abs(perm[j]-perm[i]); g=gcd(da,db)
            s.add((min(da//g,db//g), max(da//g,db//g)))
    return s
def amax(n):
    best=0
    for p in itertools.permutations(range(n)):
        c=len(directions(p)); best=max(best,c)
    return best
def load(path):
    for ln in open(path):
        ln=ln.strip()
        if ln and not ln.startswith('#'):
            return [int(x)-1 for x in ln.split()]
if __name__=="__main__":
    p=load(sys.argv[1] if len(sys.argv)>1 else "a321531_n11_directions28.txt")
    d=directions(p)
    print(f"witness n={len(p)}: {len(d)} distinct direction classes")
    print(f"  classes: {sorted(d)}")
    print(f"=> a(11) >= {len(d)} (witness valid: {len(d)==28})")
    print("calibration (exhaustive, must match OEIS A321531 a(2..10)=1,2,4,6,8,11,14,18,23):")
    known=[1,2,4,6,8,11,14,18,23]
    for n in range(2,11):
        v=amax(n); print(f"  a({n})={v}  {'OK' if v==known[n-2] else 'MISMATCH'}")
