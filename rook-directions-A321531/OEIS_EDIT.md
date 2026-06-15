# OEIS A321531 — proposed edit (ready to submit)

**Result.** a(11) = 28, a(12) = 33, a(13) = 38 (all previously unrecorded; previous last term
a(10) = 23). Maximum number of distinct directions among n non-attacking rooks, by exhaustive search.

**DATA** — append three terms:
```
0, 1, 2, 4, 6, 8, 11, 14, 18, 23  ->  0, 1, 2, 4, 6, 8, 11, 14, 18, 23, 28, 33, 38
```

**COMMENT to add** (date format `Mon DD YYYY`, zero-padded):
```
a(11) = 28, a(12) = 33, and a(13) = 38, determined by an exhaustive branch-and-bound search; the
same search reproduces a(2)..a(10). Explicit optimal placements and a standalone verifier are in the
Blair link. - _William Blair_, Jun 06 2026
```

**LINK to add** — IMPORTANT: insert ALPHABETICALLY by surname (Blair goes before Kagey):
```
William Blair, <a href="https://github.com/willblair0708/verified-combinatorics/tree/main/rook-directions-A321531">Optimal 11-, 12-, and 13-rook placements (28, 33, 38 directions) and exhaustive verifier</a>
```

**EXTENSIONS** — add (required when adding terms):
```
a(11)-a(13) from _William Blair_, Jun 06 2026
```

## Evidence / how it was verified
- Witnesses: `a321531_n11_directions28.txt` (`1 10 3 11 8 6 7 9 4 5 2`),
  `a321531_n12_directions33.txt` (`1 4 3 12 5 11 6 9 10 8 2 7`), and
  `a321531_n13_directions38.txt` (`1 6 3 12 5 13 9 11 10 8 4 7 2`).
- Optimality: `search_bb.c` (exhaustive DFS, column by column, with an exact upper-bound prune on
  the number of still-realizable direction classes). The prune is a valid upper bound, so the search
  is complete; rerunning with the symmetry reduction disabled gives the identical answer.
- Calibration: the solver reproduces a(2..10) = 1,2,4,6,8,11,14,18,23 exactly.
- `python3 verify.py <witness>` re-counts the witness directions via an independent code path.

## Style notes (learned from the A347025 edit)
- Links must be alphabetical by author surname.
- Signature date is zero-padded: `Jun 06 2026`, not `Jun 6 2026`.
- Adding term(s) requires an EXTENSIONS line.

---
## Re-verification 2026-06-15 (independent)
`search_bb.c` recompiled and re-run from scratch: calibration reproduces
OEIS a(2..10)=1,2,4,6,8,11,14,18,23 exactly, and the new terms
**a(11)=28, a(12)=33, a(13)=38** are reconfirmed as full exhaustive maxima
(witnesses printed by the solver). a(14)≥43 is a verified lower-bound witness
only (n=14 exhaustive proof not completed) — do NOT submit a(14) as an exact
term; it may be mentioned as `a(14) >= 43` in a comment if desired.
**Submission = the three terms a(11..13); OEIS still ends at a(10)=23,
keyword `more`.** Submit via the OEIS web editor (oeis.org, propose changes
to A321531) under a registered account.
