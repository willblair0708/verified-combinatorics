#!/usr/bin/env python3
"""Exact maximum B_3 set in {0,1}^n via CP-SAT (for a legitimate, exact OEIS new-sequence submission).

A set S in {0,1}^n is a B_3 set iff all 3-element multiset sums a+b+c (componentwise integer addition,
a,b,c in S, repetition allowed) are DISTINCT. Maximize |S|.

Encoding: pack each coordinate into a 2-bit field (a 3-sum coord is in {0,1,2,3}, fits with no carry), so
spread(point) = sum_i coord_i << (2i), and the 3-sum's code = spread(a)+spread(b)+spread(c). B_3 <=> all
3-multiset codes distinct. ILP: for each code value reached by >=2 multisets, at most one may be fully
selected (linearized AND indicators). Maximize sum of selected points. CP-SAT proves optimality where it
can (status OPTIMAL); otherwise reports best found (a lower bound).
"""
from __future__ import annotations

import sys
import itertools
from collections import defaultdict
from ortools.sat.python import cp_model


def spread(vec, n):
    return sum((vec[i] & 1) << (2 * i) for i in range(n))


def exact_b3(n, time_s=60):
    pts = list(itertools.product((0, 1), repeat=n)) if n > 0 else [()]
    P = len(pts)
    sp = [spread(p, n) for p in pts]
    # group 3-multisets (i<=j<=k) by their summed code
    groups = defaultdict(list)
    for i in range(P):
        for j in range(i, P):
            sij = sp[i] + sp[j]
            for k in range(j, P):
                groups[sij + sp[k]].append((i, j, k))

    m = cp_model.CpModel()
    x = [m.NewBoolVar(f"x{i}") for i in range(P)]
    for code, ms in groups.items():
        if len(ms) < 2:
            continue  # unique 3-multiset for this code: never a collision, no constraint needed
        ys = []
        for (i, j, k) in ms:
            y = m.NewBoolVar("")
            # y = AND(x_i, x_j, x_k)  (only the >= direction is needed to forbid double-selection)
            m.Add(y >= x[i] + x[j] + x[k] - 2)
            m.Add(y <= x[i]); m.Add(y <= x[j]); m.Add(y <= x[k])
            ys.append(y)
        m.Add(sum(ys) <= 1)   # at most one selected 3-multiset realizes this sum
    m.Maximize(sum(x))
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = time_s
    solver.parameters.num_search_workers = 8
    st = solver.Solve(m)
    sel = [pts[i] for i in range(P) if solver.Value(x[i])]
    status = "OPTIMAL" if st == cp_model.OPTIMAL else ("feasible" if st == cp_model.FEASIBLE else "none")
    return len(sel), status, sel


def _independent_check(S, n):
    """Re-verify S is genuinely B_3: all 3-multiset componentwise-integer sums distinct."""
    sums = set()
    for i in range(len(S)):
        for j in range(i, len(S)):
            for k in range(j, len(S)):
                s = tuple(S[i][t] + S[j][t] + S[k][t] for t in range(n))
                if s in sums:
                    return False
                sums.add(s)
    return True


if __name__ == "__main__":
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    print("n  B_3(n)  status     verified")
    terms = []
    for n in range(0, nmax + 1):
        t = 90 if n <= 5 else 300
        size, status, sel = exact_b3(n, time_s=t)
        ok = _independent_check(sel, n)
        terms.append((n, size, status, ok))
        print(f"{n}  {size:5d}  {status:9s}  {ok}", flush=True)
    print("\nExact-proven terms (OPTIMAL only):",
          ", ".join(str(s) for (nn, s, st, ok) in terms if st == "OPTIMAL" and ok))
    print("All best-found (>= lower bounds):",
          ", ".join(str(s) for (nn, s, st, ok) in terms if ok))
