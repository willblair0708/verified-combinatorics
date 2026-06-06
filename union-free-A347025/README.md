# `union-free-A347025/` — maximum union-free families of subsets

[OEIS A347025](https://oeis.org/A347025): **a(n) = maximum size of a family of nonempty
subsets of {1,…,n} such that no member is the union of some sub-collection of the others.**
Known: a(0..6) = 0, 1, 2, 4, 7, 13, 24.

## Result: a(7) = 44 (resolving the open gap 44 ≤ a(7) ≤ 45)

Prior state on OEIS (since April 2022): a(7) ≥ 44 (Jon E. Schoenfield) and a(7) ≤ 45
(Jinyuan Wang). This settles it to **a(7) = 44**.

- **Witness** (`a347025_n7_size44.txt`): an explicit union-free family of 44 subsets of {1..7}.
  Checkable in milliseconds by `verify.py` (pure Python, no dependencies), whose validity test
  matches the OEIS A347025 program exactly.
- **Optimality** (no family of size 45 exists): proven by exhaustive constraint search,
  OR-Tools CP-SAT, `search_optimality.py`. Two independent guards:
  1. **Calibration** — the same model reproduces a(4)=7, a(5)=13, a(6)=24, each `OPTIMAL`,
     matching the externally-computed OEIS values.
  2. **Two independent encodings** — a coverage-reification encoding (`cov`) and a
     private-element encoding (`private`) of the same constraint. Both reproduce the
     calibration terms as `OPTIMAL`; the `cov` encoding proves a(7)=44 `OPTIMAL`.

## Reproduce

```
python3 verify.py a347025_n7_size44.txt          # check the 44-family witness
python3 search_optimality.py cov                 # a(4..6) optimal + a(7)=44 optimal (CP-SAT)
python3 search_optimality.py private 7 7200       # independent encoding, n=7
```

These sets are released into the public domain (CC0); any OEIS contribution derived from them
is under the OEIS Contributor's License Agreement.
