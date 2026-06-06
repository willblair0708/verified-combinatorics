# OEIS A347025 — proposed edit (draft, not yet submitted)

**Result.** a(7) = 44. This resolves the recorded gap (a(7) ≥ 44, Schoenfield; a(7) ≤ 45,
Jinyuan Wang). The maximum union-free family of subsets of {1..7} has size 44.

**DATA** — extend by one term:
```
0, 1, 2, 4, 7, 13, 24  ->  0, 1, 2, 4, 7, 13, 24, 44
```
(remove keyword `more` if a(7) is the last desired term; keep `hard`.)

**COMMENT to add:**
```
%C A347025 a(7) = 44, resolving the bounds 44 <= a(7) <= 45. The maximum was determined by an
exhaustive constraint search (OR-Tools CP-SAT), with the model independently reproducing
a(4)=7, a(5)=13, a(6)=24 as optima, and confirmed by a second independent encoding. An explicit
44-set witness and a standalone verifier are in the Blair link. - _William Blair_, Jun 2026
```

**LINK to add:**
```
%H A347025 William Blair, <a href="https://github.com/willblair0708/verified-combinatorics/tree/main/union-free-A347025">Maximum union-free family for n=7 (witness of size 44) and verifier/search</a>
```

## Before submitting (yours, under your OEIS account)
1. Push `union-free-A347025/` to the public repo so the %H link resolves.
2. Optimality is a CP-SAT exhaustive result. Editors here (Schoenfield, Jinyuan Wang) set the
   44/45 bounds and will check carefully — the witness + the calibrated, two-encoding search is
   the evidence. State it as "exhaustive constraint search," not a hand proof.
3. Only submit once the second (private-element) encoding has also proved a(7)=44 OPTIMAL (the
   long confirmation run); until then the result rests on encoding 1 + calibration.
