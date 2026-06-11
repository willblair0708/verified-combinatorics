# Erdős Problem #617 — the r = 5 case (K_26)

**Problem** ([erdosproblems.com/617](https://www.erdosproblems.com/617),
Erdős–Gyárfás [ErGy99]): let r ≥ 3. If the edges of K_{r²+1} are r-coloured,
must there exist r+1 vertices whose induced K_{r+1} misses at least one
colour?  Proved for r = 3, 4 by Erdős–Gyárfás; **open for r ≥ 5**.  The first
open case is r = 5: does K_26 admit a *balanced* 5-colouring, i.e. one in
which every 6-set of vertices sees all 5 colours on its 15 edges?  The
conjecture says no.

## Status of this directory

This directory attacks the single sharpest control point left in the
"61-edge colour class" route, namely the **pass-20 hitset-pair finite
decision problem** (see `NOTES.md` for the full provenance and the
conditional structure):

> Find or rule out a graph B on 19 vertices with e(B)=40, Δ(B)≤6, α(B)≤4,
> at most 11 edges on every 6-set, complement K₅-saturated and not
> 4-partite, τ₄(B)=4, together with the Case I or Case II hitset pair
> (P,Q) — see `solve_hitset_pair.py` docstring for the exact spec.

**IMPORTANT — what is and is not proven.**  The reduction of the 61-edge
colour-class boundary to this finite problem was produced across ~20 earlier
working passes whose artifacts were never committed to this repository.
Those reductions are **imported, unverified claims** here (itemised in
`NOTES.md`).  Consequences derived in this directory that depend on them are
marked *conditional*.  Unconditional facts (the elementary balanced-colouring
constraints, witness checks, SAT/UNSAT verdicts about the stated finite
problem itself) are verifiable from the code and certificates in
`artifacts/`.

Erdős #617 itself remains **open** in both directions; nothing here claims a
full solution.

## Files

| file | purpose |
|---|---|
| `solve_hitset_pair.py` | CNF encoder + CaDiCaL CEGAR solver for the finite problem (Case I, Case II k=0..4) |
| `check_witness.py` | independent full-spec checker for any SAT witness (no pysat, no shared code) |
| `certify_unsat.py` | replays a dumped CNF with Glucose 4.2 proof logging and verifies the DRAT proof with drat-trim |
| `search_balanced_k26.py` | direct SAT search for a balanced 5-colouring of K_26 (counterexample hunt; SAT direction only) |
| `check_balanced.py` | independent checker for a claimed balanced colouring |
| `NOTES.md` | provenance, imported claims, independent verification of the pass-20 §3 derivations, results |
| `artifacts/` | logs, result JSONs, dumped CNFs, DRAT certificates, SHA256 manifest |
