# OEIS A321531 — proposed edit (ready to submit)

**Result.** a(11) = 28 (was unrecorded; previous last term a(10)=23). Maximum distinct directions
among 11 non-attacking rooks, by exhaustive search over all 11! placements.

**DATA** — append one term:
```
0, 1, 2, 4, 6, 8, 11, 14, 18, 23  ->  0, 1, 2, 4, 6, 8, 11, 14, 18, 23, 28
```

**COMMENT to add** (date format `Mon DD YYYY`, zero-padded):
```
a(11) = 28, determined by exhaustive search over all 11! = 39916800 placements; the same search
reproduces a(2)..a(10). An explicit optimal placement and a standalone verifier are in the Blair
link. - _William Blair_, Jun 06 2026
```

**LINK to add** — IMPORTANT: insert ALPHABETICALLY by surname (Blair goes before Kagey):
```
William Blair, <a href="https://github.com/willblair0708/verified-combinatorics/tree/main/rook-directions-A321531">Optimal 11-rook placement (28 directions) and exhaustive verifier</a>
```

**EXTENSIONS** — add (required when adding a term):
```
a(11) from _William Blair_, Jun 06 2026
```

## Style notes (learned from the A347025 edit)
- Links must be alphabetical by author surname.
- Signature date is zero-padded: `Jun 06 2026`, not `Jun 6 2026`.
- Adding a term requires an EXTENSIONS line.
