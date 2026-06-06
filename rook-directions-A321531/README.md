# `rook-directions-A321531/` — maximum distinct directions among non-attacking rooks

[OEIS A321531](https://oeis.org/A321531): **a(n) = maximum number of distinct directions between
n non-attacking rooks on an n X n board.** A direction is taken up to scaling and the dihedral
action of the square, i.e. the class `sorted(|Δcol|, |Δrow|) / gcd`. Known: a(1..10) = 0, 1, 2, 4,
6, 8, 11, 14, 18, 23.

## Result: a(11) = 28

- **Witness** (`a321531_n11_directions28.txt`): the permutation `1 10 3 11 8 6 7 9 4 5 2` places 11
  non-attacking rooks realizing **28 distinct direction classes**. Checkable instantly by `verify.py`.
- **Optimality**: exhaustive search over all 11! = 39,916,800 placements (`search_exhaustive.py`,
  parallel) confirms no placement exceeds 28.
- **Calibration**: the same exhaustive routine reproduces a(2..10) = 1,2,4,6,8,11,14,18,23 exactly
  (the externally-known terms), validating the direction-class definition and the search.

## Reproduce
```
python3 verify.py                  # witness (28 classes) + exhaustive calibration a(2..10)
python3 search_exhaustive.py       # full exhaustive proof of a(11)=28 (parallel)
```
CC0; OEIS contributions under the OEIS Contributor's License Agreement.
