# GPT Pro prompt #4 — extend the cross-part-triangle method to the remaining part-shapes

> Paste below the line into the same GPT Pro chat. Your aggregation lemma closed the
> triangle-free residue for ONE part-shape, (6,5,5,5,5). A completeness check found
> the gap: the walled set at q=8,9,10 spans several other shapes that the method has
> not touched. This asks you to close those too — which, with the clique-core and
> packing lemmas, would close rungs 8,9,10 entirely by hand (m* ≥ 66, no solver).

---

Your cross-part-triangle aggregation is **certified for shape (6,5,5,5,5)** (five
size-5 parts, defect d=0). But the admissible part-shapes at rungs q=8,9,10 are:

```
q=8,9:  (8,5,5,5,3) (8,5,5,4,4) (7,5,5,5,4) (6,6,5,5,4) (6,5,5,5,5)
q=10:   + (7,6,5,5,3) (7,6,5,4,4)
```

Your lemma only covers the last one. **Extend the same machinery to all the others.**
The setup is identical (26 vertices partitioned into the shape's parts; holes = absent
cross-pairs; min_holes is the least holes making the complement K_6-free with every
6-set spanning ≥ 4 edges; a config is closed at rung q iff min_holes > cap), with two
differences per shape:

**(1) The cap is lower (this helps you).** cap = I + q − d, where the defect
d = Σ_parts C(n_i,2) − 55 is now positive:

| shape | d | cap at q=10 = I+10−d |
|---|---:|---|
| (7,5,5,5,4) | 2 | I+8 |
| (6,6,5,5,4) | 1 | I+9 |
| (8,5,5,5,3) | 6 | I+4 |
| (8,5,5,4,4) | 5 | I+5 |
| (7,6,5,5,3) | 4 | I+6 |
| (7,6,5,4,4) | 3 | I+7 |

So these shapes have **smaller caps to beat than (6,5,5,5,5)** — the aggregation bound
has more margin, and they should be *easier*, not harder.

**(2) The empty parts are no longer all size 5.** The aggregation's local constants
depend on the sizes of the empty parts (the parts with no internal edges, over which
the K_6 completions run). You proved, for size-5 empty parts:
- local matching budget: ≤ 1 hole per vertex per empty part (Füredi cut on {v}∪E);
- MATCH_BLOCK(3,2,2)=∞, MATCH_BLOCK(2,2,2)=6; ρ_3=6, ρ_2=1, ρ_1=0.

Re-derive the analogues when an empty part has **size 4 or size 3**:
- the local matching budget for a size-n empty part E comes from the Füredi cut on a
  6-set (6−n outside vertices) ∪ E — derive the per-vertex hole bound for n=4 and n=3;
- the corresponding MATCH_BLOCK / ρ constants for grids whose empty-part dimensions are
  4 or 3 instead of 5 (finite blocking computations, same style as before).

**Leverage already in hand (use, don't re-derive):**
- The campaign's **Lemma D**: an internal edge + an *empty* size-4 part + three *empty*
  size-5 parts forces a K_6, so that whole family is dead at every cap. This kills most
  concentrated configs of (7,5,5,5,4) outright; check which of the new shapes it covers.
- Your certified size-5 constants (ρ_3=6, ρ_2=1, MATCH_BLOCK as above).
- A K_6 inside a size-≥6 part (the 6-, 7-, 8-parts can themselves contain dense
  triangle-free graphs like K_{2,3}, K_{3,3}, K_{2,4}) — but triangle-containing cases
  are already delegated to the clique-core lemmas; assume the loaded parts are
  triangle-free.

## Deliverable

For each shape above, and each concentrated triangle-free internal configuration:
1. The aggregation bound `min_holes ≥ B_agg(config)` with the correct per-empty-part-size
   constants, proven by the same single-triple-forcing + no-overlap-collapse argument.
2. A **core-scan / finite verifier** (same shape as your (6,5,5,5,5) scan) showing
   `B_agg > cap = I + q − d` for every config, at q = 8, 9, 10. Where Lemma D already
   kills a family, say so and skip it.
3. A **precise coverage statement per shape**: closed by hand vs. genuine remainder.
4. For any bound you claim, give the exact **fix-core assertion** I can machine-check
   (pin the core, solve the full model at cap, expect UNSAT) — the same protocol that
   certified the (6,5,5,5,5) lemma.

Same verification contract: every constant reduces to a finite check; mark any unproven
sub-claim; never assert a proof you can't verify; if a shape resists, name the exact
configuration and why (where the per-empty-part budget or anchor count falls short of
the cap).

If all shapes close, then with the clique-core lemmas (triangle-bearing) and the
fractional packing (≥3-part diffuse spreads), **rungs 8, 9, 10 are closed by hand and
m\* ≥ 66 follows with no solver sweep at all.**
