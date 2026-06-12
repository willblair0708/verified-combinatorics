# The m* hand attack (pen-and-paper lane) — opened 2026-06-12

**Target theorem (would prove #617 r = 5 by counting, and unlike a SAT
certificate, generalizes structurally toward other r):**

> Every graph G on 26 vertices with α(G) ≤ 5 and every 6-set spanning ≤ 11
> edges has e(G) ≥ 66.

Work in the complement H (= Ḡ): **K₆-free, every 6-set spans ≥ 4 edges**;
equivalently show e(H) ≤ 259.  Known: e(H) ≤ T(26,5) = 270 (Turán), and the
Turán graph itself fails the 4-edge condition (its size-6 part is an
independent 6-set), so e(H) ≤ 269 already; the game is the remaining ten.

## Foothold 1 — the hole-budget inequality

For any vertex u and any 5-set P ∌ u, the 6-set {u} ∪ P gives

    deg_P(u) ≥ 4 − e(P).

Against an internally-sparse 5-set, every outside vertex must carry ≥ 4 of
its 5 possible cross edges; "holes" (missing cross pairs) are globally
budgeted at ≤ 1 + e(P) per (vertex, 5-set P) pair.  Sparse parts are
expensive for *everyone else*.

## Foothold 2 — blocking systems for internal edges

Fix any 5-partition of V(H) with parts P₀ (size 6), P₁..P₄ (size 5).  The
6-set P₀ alone forces e(P₀) ≥ 4 internal edges.  K₆-freeness demands that
for EVERY internal edge uv and every transversal (w₁,…,w₄) ∈ P₁×…×P₄ that
is complete and fully joined to u, v — none exists; i.e. the hole systems
of u, v and the parts must hit all 5⁴ = 625 transversals.

Checked and honest: the naive greedy/counting refutation FAILS at the
boundary — u and v's holes (≤ 4 each per Foothold 1 with empty parts, each
killing ≤ 125 transversals) have just enough capacity (≤ 1000 ≥ 625) to
block everything.  So there is no two-line contradiction; the content is
quantitative:

* every hole spent on blocking creates a sparser cross-pattern that
  re-invokes Foothold 1 on new 6-sets ({u} ∪ P now has fewer cross edges,
  so P needs internal edges, which need their own blocking systems, …);
* ≥ 4 internal edges in P₀ must SHARE the hole budgets of their endpoints
  (a vertex's holes are fixed once), and distinct internal edges with
  disjoint endpoints need near-disjoint blocking;
* dense parts (e(P) ≥ 4) free outside hole budgets but spend the global
  edge budget directly and create their own K₆ pressure.

## Programme

1. Formalize the cascade as an accounting identity: charge every edge of
   deficit 270 − e(H) to (holes) + (internal edges), and lower-bound the
   holes forced per internal edge GIVEN the shared-budget constraint.
   First milestone: a hand proof of e(H) ≤ 265 (m* ≥ 60) — would already
   beat the trivial bound and validate the method.
2. Use the verified witnesses (artifacts/mstar_witness_E92..124) as the
   adversary's best plays: every inequality in the cascade must be tight
   against some witness or it is provably improvable.  The witnesses are
   clique-block unions — the accounting should expose exactly which budget
   they exhaust.
3. Escalate to the stability frame of case1_structure.md (Füredi-type:
   K₆-free with ≥ 260 edges ⟹ ≤ 10 deletions from 5-partite) so the
   partition in Foothold 2 is not an assumption but a consequence.
   (Verify the stability constant before leaning on it.)
4. Whatever rung the hand proof reaches, the certified ladder
   (certify_mstar_lb.py) covers the residue; if the hand proof reaches 66,
   the ladder is scaffolding and the r=5 proof is human-readable.

Status: footholds proven (elementary); cascade accounting OPEN — this is
the active pen-and-paper front of the campaign.
