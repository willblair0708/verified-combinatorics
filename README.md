# verified-combinatorics

Independently verifiable extremal combinatorial sets, with a standalone checker. Each result
here is a concrete object (a set of vectors) plus a short program that confirms it satisfies
its defining property. The intent is that anyone can reproduce the verification in seconds,
without trusting the search that produced the set.

Vectors live in `{0,1}^n`. Addition is **componentwise over the integers** (not modulo 2), so a
sum of two vectors lies in `{0,1,2}^n` and a sum of three lies in `{0,1,2,3}^n`.

```
python3 verify.py            # checks every set in this repo and prints a table
```

## `sidon-A309370/` — binary Sidon (B_2) sets

A set is **Sidon** (a `B_2` set) iff all pairwise sums `a + b` are distinct. These sets give
lower bounds for [OEIS A309370](https://oeis.org/A309370), *Maximum size of a Sidon subset of
{0,1}^n*. Each was found by computer search and is verified here by recomputing all
`C(m,2) + m` pairwise sums and checking they are distinct.

| n | size (lower bound) | prior recorded on OEIS |
|---|--------------------|------------------------|
| 8 | 33 | 32 |
| 9 | 47 | 45 |
| 10 | 66 | 63 |
| 16 | 505 | 472 |
| 17 | 712 | 662 |
| 18 | 1010 | 864 |
| 19 | 1435 | (none) |
| 20 | 1989 | (none) |
| 21 | 2694 | (none) |
| 22 | 3770 | (none) |
| 23 | 5179 | (none) |
| 24 | 7179 | (none) |

These improve the lower bounds recorded on OEIS; they are not claimed to be optimal, nor
exhaustively checked against unrecorded constructions in the literature. They are consistent
with the page's conjecture `a(n) ~ 2^(n/2+1)` (each sits just below the corresponding power of
two). Several n include an earlier, smaller set as well (e.g. n=16 also has size 503, n=19 size
1397, n=20 size 1941, n=9 size 46); the table always uses the larger, and every set listed is
checked by `verify.py`.

The n=16/19/20 bounds (505, 1435, 1989) and the n=23/24 bounds (5179, 7179) come from the Canopus
loop (an Opus 4.8 proposer under an incremental kick-out local search); the n=8/9/10 sets come
from an iterated local search, improving a(8) >= 32, a(9) >= 45, a(10) >= 63 to 33, 47, 66. These
are the witnesses referenced by the corresponding A309370 comments; each is checkable in seconds
by `verify.py`.

## `b3-binary/` — binary B_3 sets

A set is a `B_3` set iff all sums of three elements `a + b + c` (with repetition) are distinct.
Every `B_3` set is also a `B_2` set, so its size is at most the corresponding A309370 value.
The maximum sizes for small `n`, each proven optimal by an integer-program search and verified
here, are:

| n | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| max size | 1 | 2 | 3 | 4 | 6 | 8 | 11 |

a(6) = 11 is proven optimal (the size-12 case is infeasible, shown by an integer-program search
with hyperoctahedral symmetry breaking). `a(7) >= 15` and `a(8) >= 19` are search lower bounds
(iterated local search), not proven optimal; both are verified B_3 sets (all 3-element sums distinct).
`b3_search.py` is the search program (requires OR-Tools); `verify.py` needs only Python 3.

## `gf2-sidon-A394031/` — Sidon sets in GF(2)^n (mod-2)

A set is a Sidon set in GF(2)^n iff all pairwise XOR-sums are distinct (no four distinct elements
XOR to zero). This is the mod-2 analog of the integer Sidon sets above. Elements are written one
integer per line (an n-bit vector). For [OEIS A394031](https://oeis.org/A394031), a(1..10) =
2,3,4,6,7,9,12,18,24,34 are proven. The set here has size 48 in F_2^11.

**This is a reproduction of a known result, not a new one.** Czerwiński & Pott,
[*On large Sidon sets*](https://arxiv.org/abs/2411.12911) (2024), state that size 48 is the best
previously known Sidon set in F_2^11 and that the APN-graph construction "is not an improvement as
it is equal to the best previously known example." We independently re-derived it (graph of the
Gold APN function x -> x^3 over GF(2^5), greedily extended) and verified it (all C(48,2) = 1128
pairwise XORs distinct). It is kept here only as a verified reproduction. The upper bound is
a(11) <= 62 (Brouwer–Tolhuizen). It is **not** submitted to OEIS as a contribution.

## License

All data files and code here are released into the public domain (CC0). The OEIS contributions
derived from them are made under the OEIS Contributor's License Agreement.
