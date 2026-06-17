# A321531 — extension draft (for review before submitting to OEIS)

**This is a draft prepared for a human to review and submit. Nothing here has
been sent to OEIS. The bounds are lower bounds, not proven maxima — read the
"What to claim" section before submitting.**

## The sequence

A321531: *a(n) is the maximum number of distinct directions between n
non-attacking rooks on an n X n chessboard.* OEIS lists exact terms (both the
data field and the b-file) only through **a(10) = 23**.

## What the discovery engine found

`vela campaign search rook_directions --n N` runs a deterministic seeded search
(steepest-ascent 2-opt over the column permutation) and frozen-verifies every
result with `vela-verify`. It reproduces **every listed OEIS term exactly**:

| n | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|----|----|
| a(n), OEIS | 4 | 6 | 8 | 11 | 14 | 18 | 23 |
| engine | 4 | 6 | 8 | 11 | 14 | 18 | 23 |

and then extends past the sequence's known range with **verified lower bounds**:

| n | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|---|----|----|----|----|----|----|----|----|----|----|
| a(n) ≥ | 28 | 33 | 38 | 43 | 49 | 56 | 62 | 70 | 77 | 86 |

Each bound is an explicit rook placement in `a321531_n<N>_directions<count>.txt`
(one line: the 1-based column permutation). Re-verify from scratch:

```
vela reproduce examples/open-constructions/witnesses   # in the vela repo
```

## What to claim

These are **lower bounds**. The engine finds the proven maximum for every n it
can be checked against (n ≤ 10), which is strong evidence the local search is
hitting optima for this problem — but it does **not prove** optimality for
n ≥ 11. The true a(n) could be larger.

So the honest, submittable contribution is **lower bounds**:

> a(11) >= 28, a(12) >= 33, a(13) >= 38, a(14) >= 43, a(15) >= 49, a(16) >= 56,
> a(17) >= 62, a(18) >= 70, a(19) >= 77, a(20) >= 86, each realized by an
> explicit non-attacking rook placement (witnesses + an independent checker at
> github.com/willblair0708/verified-combinatorics, rook-directions-A321531/).

To upgrade any of these to an **exact** b-file term, confirm it is the maximum
by an exhaustive or branch-and-bound search at that n (out of scope for the
heuristic engine).

## Draft comment text (adapt as you see fit)

> Lower bounds for n = 11..20 from explicit non-attacking rook placements,
> each verified by an independent checker: a(11) >= 28, a(12) >= 33,
> a(13) >= 38, a(14) >= 43, a(15) >= 49, a(16) >= 56, a(17) >= 62, a(18) >= 70,
> a(19) >= 77, a(20) >= 86. Placements and a from-scratch verifier:
> github.com/willblair0708/verified-combinatorics (rook-directions-A321531).

Submitting and any %H link edit is the account holder's action.
