# OEIS A347025 — proposed edit (READY TO SUBMIT, 2026-06-06)

**Result.** a(7) = 44. This resolves the recorded gap (a(7) ≥ 44, Schoenfield; a(7) ≤ 45,
Jinyuan Wang). The maximum union-free family of subsets of {1..7} has size 44.

**Verification status: COMPLETE.** Both independent CP-SAT encodings (coverage-reification and
private-element) prove a(7)=44 OPTIMAL, and both reproduce a(4)=7, a(5)=13, a(6)=24 as optima
(calibration against the externally-known terms). The %H package is pushed and the link resolves.
Ready for the human OEIS edit.

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

## To submit (yours, under your OEIS account)
1. ✓ DONE: `union-free-A347025/` is pushed; the %H link resolves; both encodings confirm OPTIMAL.
2. oeis.org/A347025 → edit → append `, 44` to DATA → paste the %C comment + %H link above → Save
   Changes → Submit for review. (Two separate buttons: "Save Changes" then "Submit for review".)
3. Editors here (Schoenfield, Jinyuan Wang) set the 44/45 bounds and will check carefully — the
   witness + calibrated two-encoding search is the evidence. Frame it as "exhaustive constraint
   search," not a hand proof.
