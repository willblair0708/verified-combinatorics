#!/usr/bin/env python3
"""Reproduce A347025(n) by exhaustive constraint search (OR-Tools CP-SAT).

a(n) = max family of nonempty subsets of {1..n} with no member a union of others.
Two independent encodings of the same constraint are provided:
  enc='cov'     : reify, per element e of s, "e is covered by a chosen proper subset of s";
                  forbid x_s AND all-covered.
  enc='private' : per s, require a "private" element e in s with NO chosen proper subset
                  containing e.
Both reproduce a(4)=7, a(5)=13, a(6)=24 (OPTIMAL) and a(7)=44 (OPTIMAL).
Usage: python3 search_optimality.py [enc] [n] [time_s]
"""
import sys
from ortools.sat.python import cp_model

def solve(n, enc="cov", tlimit=3600, workers=15):
    U=list(range(1,1<<n)); m=cp_model.CpModel(); x={s:m.NewBoolVar(f"x{s}") for s in U}
    for s in U:
        elems=[e for e in range(n) if s&(1<<e)]
        if len(elems)<2: continue
        if enc=="cov":
            cov=[]
            for e in elems:
                rs=[r for r in U if r!=s and (r&s)==r and (r&(1<<e))]
                c=m.NewBoolVar(f"c{s}_{e}"); m.AddMaxEquality(c,[x[r] for r in rs]); cov.append(c)
            m.AddBoolOr([x[s].Not()]+[c.Not() for c in cov])
        else:
            sel=[]
            for e in elems:
                se=m.NewBoolVar(f"s{s}_{e}")
                for r in U:
                    if r!=s and (r&s)==r and (r&(1<<e)): m.AddBoolOr([se.Not(),x[r].Not()])
                sel.append(se)
            m.AddBoolOr([x[s].Not()]+sel)
    m.Maximize(sum(x.values()))
    sv=cp_model.CpSolver(); sv.parameters.num_search_workers=workers; sv.parameters.max_time_in_seconds=tlimit
    st=sv.Solve(m)
    fam=[[e+1 for e in range(n) if s&(1<<e)] for s in U if sv.Value(x[s])==1]
    return int(sv.ObjectiveValue()), sv.StatusName(st), fam

if __name__=="__main__":
    enc=sys.argv[1] if len(sys.argv)>1 else "cov"
    if len(sys.argv)>2:
        n=int(sys.argv[2]); t=float(sys.argv[3]) if len(sys.argv)>3 else 3600
        v,s,fam=solve(n,enc,t); print(f"a({n}) [{enc}] = {v}  status={s}  (|family|={len(fam)})")
    else:
        for n in (4,5,6,7):
            v,s,_=solve(n,enc,3600); print(f"a({n}) [{enc}] = {v}  status={s}")
