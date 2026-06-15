# GPT Pro follow-up — certify the aggregation step of the star+triangle-free lemma

> Paste below the line into the SAME GPT Pro chat as the first lemma. It carries
> back the verification result and asks for the one missing piece.

---

I independently verified your "star + triangle-free 5-part ≥ B(F) holes" lemma. Report:

1. **Matching obstruction reproduces.** MATCH_BLOCK(2,2,2)=6, MATCH_BLOCK(3,2,2)=unblockable. Confirmed, and consistent with the prior campaign's blocking numbers.
2. **Core-scan formula reproduces exactly.** B(K_{2,3})=38 at (h=2, |U|=10, 50 active triples); B(C_4)=B(P_4)=36. Your script B is correct.
3. **Ground-truth check is consistent but not conclusive.** I encoded the FULL model independently (not your formula) and minimized true min_holes for star+K_{2,3}. The instance is hard at the boundary: I could only bracket **min_holes ∈ [22, 49]** (proved dual lower bound 22; best feasible found 49; a direct feasibility query at cap 37 did not resolve in 600 s). This is consistent with your ≥38 but does **not** prove it by machine.
4. **Hand audit: I could not break it.** The per-grid forcing is airtight: since MATCH_BLOCK(3,2,2)=∞, each active triple's residual must be ≤2 in every direction, which forces its 3 anchors to spend exactly one hole into each empty part, leaving a 2×2×2 residual needing MATCH_BLOCK(2,2,2)=6 empty-empty holes.

So the lemma is **promising but not yet certified.** The single unresolved step is the **aggregation over overlapping grids**, and that is the entire ask below.

## The gap to close (be rigorous and self-contained)

Your bound is `min_holes ≥ |X| + 3|U(X)| + 6` for every valid core pattern X, where U(X) is the union of the anchors of all active triples. With 50 active triples but only |U|=10 anchors, the triples **share anchors heavily**, and the term `3|U(X)|` claims that aggregating the per-grid forcings over these overlapping grids costs at least 3 holes per *distinct* anchor — no more double-counting collapse, and no interaction that lets some anchor's quota drop below 3.

Prove exactly this:

**(A) Aggregation lemma.** For every valid core pattern X and every valid full completion, the number of non-core holes is at least `3|U(X)| + 6`. The load-bearing sub-claim is: *every vertex v ∈ U(X) is forced, in every valid completion, to carry a hole into each of P_2, P_3, P_4 (so ≥ 3 anchor-empty holes per distinct anchor), these are pairwise distinct across anchors, and the +6 empty-empty holes are disjoint from all of them.* Make explicit **why overlap cannot reduce the count** — i.e., why a vertex shared by several active triples is still forced to its full 3-hole quota, and why no clever reuse of one anchor-empty hole across grids lets the total dip below 3|U(X)|. If any piece is finite, give the exact check (a blocking-number computation or a bounded case analysis), in the style of MATCH_BLOCK.

**(B) Tight witness (strongly preferred — this is cheaply machine-checkable).** Exhibit an EXPLICIT valid hole-assignment for star+K_{2,3} (P_0 = K_{1,4}, P_1 = K_{2,3}, P_2,P_3,P_4 empty) with **exactly 38 holes** — list the absent cross-pairs as vertex pairs. If min_holes = 38, this pins it exactly: lower bound from (A), upper bound from the witness, and we verify the witness in seconds directly against the full model (K_6-free + every 6-set spans ≥ 4 edges). If you cannot reach 38, give the smallest valid assignment you can and its exact hole count — that bounds how tight B is.

**(C) Honesty.** Same contract as before: every constant reduces to a finite check; mark any unproven sub-claim explicitly; never assert a proof you cannot verify. **If the aggregation is NOT valid in general, find the specific core pattern X or grid-overlap pattern where a vertex in U(X) is forced to fewer than 3 holes — that refutes B and tells us by how much, which is just as useful.**

The full decision model, for reference (you may assume a CP-SAT oracle is the final arbiter):
26 vertices, parts (6,5,5,5,5). One Boolean x_p per cross-pair (x_p=1 = hole). Constraints: (i) for every 6-set S, Σ_{p∈cross(S)} x_p ≤ |cross(S)| + |intEdges(S)| − 4; (ii) for every 6-set S whose within-part pairs are all internal edges, Σ_{p∈cross(S)} x_p ≥ 1. min_holes = min Σ x_p subject to (i),(ii).
