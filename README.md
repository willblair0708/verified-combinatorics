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
| 16 | 503 | 472 |
| 17 | 712 | 662 |
| 18 | 1010 | 864 |
| 19 | 1397 | (none) |
| 20 | 1941 | (none) |
| 21 | 2694 | (none) |
| 22 | 3770 | (none) |

These improve the lower bounds recorded on OEIS; they are not claimed to be optimal, nor
exhaustively checked against unrecorded constructions in the literature. They are consistent
with the page's conjecture `a(n) ~ 2^(n/2+1)` (each sits just below the corresponding power of
two). Files for n=17, 21, 22 include an earlier, smaller set as well; the table uses the larger.

## `b3-binary/` — binary B_3 sets

A set is a `B_3` set iff all sums of three elements `a + b + c` (with repetition) are distinct.
Every `B_3` set is also a `B_2` set, so its size is at most the corresponding A309370 value.
The maximum sizes for small `n`, each proven optimal by an integer-program search and verified
here, are:

| n | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| max size | 1 | 2 | 3 | 4 | 6 | 8 | 11 |

a(6) = 11 is proven optimal (the size-12 case is infeasible, shown by an integer-program search
with hyperoctahedral symmetry breaking). `a(7) >= 14` is a search lower bound, not proven optimal.
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
