# `rook-directions-A321531/` — maximum distinct directions among non-attacking rooks

[OEIS A321531](https://oeis.org/A321531): **a(n) = maximum number of distinct directions between
n non-attacking rooks on an n X n board.** A direction is taken up to scaling and the dihedral
action of the square, i.e. the class `sorted(|Δcol|, |Δrow|) / gcd`. Known: a(1..10) = 0, 1, 2, 4,
6, 8, 11, 14, 18, 23.

## Results: a(11) = 28, a(12) = 33, a(13) = 38

- **a(11) = 28** — witness `a321531_n11_directions28.txt`: `1 10 3 11 8 6 7 9 4 5 2`.
- **a(12) = 33** — witness `a321531_n12_directions33.txt`: `1 4 3 12 5 11 6 9 10 8 2 7` (33 of 42
  possible classes, so the bound is genuine, not saturated).
- **a(13) = 38** — witness `a321531_n13_directions38.txt`: `1 6 3 12 5 13 9 11 10 8 4 7 2` (38 of 46
  possible classes).
- **Optimality**: the exhaustive branch-and-bound solver `search_bb.c` proves no placement of n
  non-attacking rooks exceeds the stated value (n = 11, 12, 13). The prune is a valid upper bound on
  the number of still-realizable direction classes, so the search is complete; a run with the
  symmetry reduction disabled gives the identical answer (guards against a reflection bug).
- **Calibration**: the same solver reproduces a(2..10) = 1,2,4,6,8,11,14,18,23 exactly (the
  externally-known terms), validating the direction-class definition and the search.
- Runtimes (Apple Silicon, single thread): a(12) ~23s, a(13) ~5m40s.

## Reproduce
```
cc -O3 -o s search_bb.c
./s calib                          # reproduces a(2..10) and a(11)=28 (must match OEIS)
./s 12                             # full exhaustive proof of a(12)=33 (~25s)
./s 13                             # full exhaustive proof of a(13)=38 (~6 min)
python3 verify.py a321531_n13_directions38.txt   # independent witness re-count + small-n calibration
python3 search_exhaustive.py       # legacy parallel-Python exhaustive proof of a(11)=28
```
CC0; OEIS contributions under the OEIS Contributor's License Agreement.
