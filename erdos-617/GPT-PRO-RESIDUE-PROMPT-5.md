# GPT Pro prompt #5 — prove the bucket decomposition is EXHAUSTIVE (completeness)

> Paste below the line into the same GPT Pro chat (or a fresh one — it's
> self-contained on this question). This is the load-bearing completeness check: even
> if every individual lemma is right, m* ≥ 66 only follows if the lemmas together cover
> EVERY walled config with nothing slipping between them.

---

To prove m* ≥ 66 we must kill rungs q=8,9,10: every "walled" configuration (a 5-partition
of 26 vertices into one of the admissible part-shapes, with a triangle-free... no — with
ANY internal graph, I ≤ q) must be infeasible at its cap = I + q − d. The plan partitions
all such configs into three buckets, each closed by a different tool:

- **(C) clique-bearing** — some part's internal graph contains a triangle (or K_4, K_5):
  closed by the clique-core lemmas. Triangle in a part with ≥ 3 *other empty size-5 parts*
  ⟹ holes ≥ 15; K_4 with ≥ 2 empty ⟹ ≥ 9; K_5 with ≥ 1 empty ⟹ ≥ 5.
- **(D) diffuse triangle-free** — triangle-free, internal edges spread across ≥ 3 parts:
  closed by an explicit fractional K_6-packing.
- **(T) concentrated triangle-free** — triangle-free, edges in ≤ 2 parts: closed by the
  cross-part-triangle aggregation lemma (per shape).

**Your task: prove these three buckets are exhaustive AND that each bucket's lemma actually
applies to every config in it — find every gap.** The subtle risks:

1. **(C) has conditions.** The triangle lemma needs ≥ 3 *empty size-5 parts*. A config can
   contain a triangle but NOT have 3 empty size-5 parts available (e.g. the triangle sits in
   a shape like (8,5,5,4,4) where some "other" parts are size 4, or other parts are also
   loaded). Does the clique-core bound still hold, or is there a triangle-bearing config that
   *no* clique lemma closes? Characterize exactly which triangle-bearing configs are covered,
   and prove the uncovered ones (if any) are still infeasible (or hand them to bucket T/the
   machine explicitly).
2. **The boundary I ≤ 2 vs ≥ 3 loaded parts** between (T) and (D): is every config cleanly in
   one? What about a config with edges in exactly 2 parts where one part is the size-8 part
   (so the "concentration" is in a large part) — is that (T), and does the aggregation cover
   it?
3. **Mixed cases** — a config that is triangle-free in the 5-parts but has a triangle only in
   a large part, or edges split as (clique in one part) + (triangle-free in another). Which
   bucket owns it, and is it closed?

## Deliverable

A **decision procedure**: given any (shape, internal graph) walled config, it lands in exactly
one of C / D / T (or an explicitly named residual set R), and a proof that C, D, T close
their members. The output that matters most: **the residual set R** — the configs that no
current lemma closes. If R is empty, the hand proof of m* ≥ 66 is complete (modulo the
per-shape aggregation of prompt #4). If R is non-empty, enumerate its defining conditions
precisely — that is exactly the set that still needs the machine, and its size sets the
compute cost.

Same contract: every claim reduces to a finite check or an explicit elementary argument;
mark gaps; do not assert completeness you cannot justify. A correct small R with airtight
boundaries beats a confident "R is empty" that misses a family.
