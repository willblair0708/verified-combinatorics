#!/usr/bin/env python3
"""Standalone verifier for A347025 union-free family witnesses (Python 3, no deps).

A347025(n) = max size of a family of nonempty subsets of {1..n} such that NO member is
the union of some sub-collection of the others. Semantics exactly match the OEIS A347025
program: a family is INVALID iff some member s equals the bitwise-OR (union) of all other
members that are subsets of s.  Usage:  python3 verify.py a347025_n7_size44.txt
"""
import sys

def parse(path):
    sets=[]
    for ln in open(path):
        ln=ln.strip()
        if not ln or ln.startswith("#"): continue
        sets.append(tuple(sorted(int(t) for t in ln.split())))
    return sets

def to_mask(s): 
    m=0
    for e in s: m|=1<<(e-1)
    return m

def is_union_free(masks):
    for s in masks:
        allrest=0
        for r in masks:
            if r!=s and (r & s)==r:        # r is a (proper) subset of s
                allrest|=r
        if allrest==s:                     # s is the union of some others -> INVALID
            return False, s
    return True, None

def main():
    path=sys.argv[1] if len(sys.argv)>1 else "a347025_n7_size44.txt"
    sets=parse(path)
    n=max((e for s in sets for e in s), default=0)
    masks=[to_mask(s) for s in sets]
    distinct = len(set(masks))==len(masks)
    nonempty = all(m!=0 for m in masks)
    ok,bad = is_union_free(masks)
    print(f"file: {path}")
    print(f"n (ground set size): {n}")
    print(f"family size: {len(sets)}   distinct: {distinct}   all nonempty: {nonempty}")
    print(f"union-free: {ok}" + ("" if ok else f"   (violation: member {bad:#b} is a union of others)"))
    valid = ok and distinct and nonempty
    print(f"=> VALID union-free family of size {len(sets)} on " + "{1.."+str(n)+"}: " + str(valid))
    sys.exit(0 if valid else 1)

if __name__=="__main__": main()
