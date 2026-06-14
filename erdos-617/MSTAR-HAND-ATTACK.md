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

Status: footholds proven (elementary); **Milestone 1 PROVED (see below)**;
the q ≤ 10 cascade toward 66 is the active front.

---

## MILESTONE 1 (2026-06-12): m\* ≥ 60, by hand

**Theorem.** Every graph G on 26 vertices with α(G) ≤ 5 and every 6-set
spanning ≤ 11 edges has e(G) ≥ 60.

*Proof.*  Pass to the complement H: K₆-free, every 6-set spans ≥ 4 edges;
suppose for contradiction e(H) ≥ 266 = e(T₂₆,₅) − 4.

**(1) Stability.**  By Füredi's Theorem 1 (arXiv:1501.03129, verbatim: "If
K_{p+1} ⊄ G, |V(G)| = n, t ≥ 0, and e(G) = e(T_{n,p}) − t, then there
exists an (at most) p-chromatic subgraph H₀ ⊆ G with e(H₀) ≥ e(G) − t" —
no conditions on n or t), applied with p = 5, t = 270 − e(H) ≤ 4: the
5-colour classes of H₀ give a 5-partition of V with **I ≤ 4 internal
H-edges**.

**(2) The partition is forced to be (6,5,5,5,5).**  Five parts of size ≤ 5
cover only 25 < 26 vertices, so some part has ≥ 6.  A part of size 7 needs
≥ 6 internal edges (every 6-subset spans ≥ 4: summing m − deg(x) ≥ 4 over
its 7 vertices gives 5m ≥ 28), and sizes ≥ 8 need ≥ 8 — both exceed I ≤ 4.
Two parts of size 6 need 4 + 4 = 8 > 4.  Hence exactly one 6-part P₀ and
four 5-parts; the 6-set P₀ forces e(P₀) ≥ 4, so **I = 4, e(P₀) = 4, and
every 5-part is internally empty**.

**(3) Hole budgets.**  Write "holes" for missing cross-pairs of the
partition; counting e(H) = (270 − holes) + I ≥ 266 gives **holes ≤ 8**.
Foothold 1 with empty 5-parts: every vertex has ≤ 1 hole into each 5-part.

**(4) Blocking.**  Pick any internal edge uv ⊆ P₀.  For i = 1..4 let
Uᵢ ⊆ Pᵢ be the common H-neighbours of u and v in Pᵢ; by (3),
|Uᵢ| ≥ 5 − 1 − 1 = 3.  If some transversal (w₁,…,w₄) ∈ U₁×…×U₄ had all six
wᵢwⱼ pairs present, {u,v,w₁..w₄} would be a K₆.  So the cross-holes
between 5-parts must meet every transversal of U₁×…×U₄.  A hole between
parts i and j kills exactly ∏_{m∉{i,j}}|U_m| of the ∏|U_m| transversals,
so the number of such holes is at least min_{i<j}|Uᵢ||Uⱼ| ≥ 3·3 = **9**.

But (3) caps ALL holes at 8 < 9.  Contradiction. ∎

Notes: the proof needs only ONE internal edge in P₀, and the bound 9 > 8
has slack against u, v spending A-holes (each A-hole spent shrinks the
budget 8 further while |Uᵢ| ≥ 3 regardless).  Independent consistency:
CP-SAT minimise has m\* ≤ 90 (verified witness), and the certified ladder
(T58/T60) cross-checks by machine.  Trust base: Füredi 2015 Theorem 1
(published; statement verified verbatim against ar5iv 2026-06-12; we do
NOT need the weaker 3t edit-distance corollary).

## Rung q = 5 (m\* ≥ 61) — Case A closed, Case B open

Setup: e(H) ≥ 265 ⟹ Füredi I ≤ 5; 7-parts need ≥ 6 > 5 internal and two
6-parts need 8 > 5, so the partition is again (6,5,5,5,5) with
e(P₀) = 4, I₅ := I − 4 ≤ 1, and holes ≤ 270 + I − e(H) ≤ 10.

**Case A (I₅ = 0): CLOSED.**  All 5-parts empty, so u, v spend
sᵢ ∈ {0,1,2} holes into Pᵢ and |Uᵢ| = 5 − sᵢ.  Total holes ≥
Σsᵢ + min_{i<j}(5−sᵢ)(5−sⱼ); minimising over all (sᵢ) ∈ {0,1,2}⁴ gives
**13**, attained at (2,2,0,0) → 4 + 3·3.  13 > 10. ∎
(The same table gives 13 > 12 = the q = 6 budget, so Case A is closed
through q = 6 as well; it fails first at q = 7 where holes ≤ 14.)

**Case B (I₅ = 1, edge xy in a 5-part P₁): CLOSED — see the next
section.**  The covering bound (≥ min|Uᵢ||Uⱼ|) was the wrong tool (it
bottoms out at 9 ≤ 10); the closure came from a *feasibility* analysis:
blocking a (≥3)×(≥2)×(≥2) grid between empty parts is impossible, not
merely expensive.

### Rung q = 5, Case B: CLOSED (2026-06-12, agent-derived, twice machine-checked) — m\* ≥ 61

**Lemma G (grid).**  Let A, B, C be subsets of three distinct internally
empty 5-parts with |A| ≥ 3, |B|, |C| ≥ 2.  Then some transversal
(a, b, c) ∈ A × B × C has all three pairs present in H.
*Proof.*  Shrink to |A| = 3, |B| = |C| = 2; suppose all transversals
blocked.  Fix a ∈ A.  If a has no hole into B: pick c ∈ C with ac
present (a has ≤ 1 hole into C's part); then (a, b₁, c), (a, b₂, c)
force b₁c, b₂c both holes — two holes at c into one part, violating c's
budget.  So each of the three a ∈ A has a hole into {b₁, b₂}; some bᵢ
absorbs two from distinct vertices of A's part — violating bᵢ's budget. ∎

**Lemma E (exact pinning).**  For every internal edge uv ⊆ P₀ and every
internally empty 5-part Pᵢ (i ≥ 2): |Uᵢ| = 3 exactly, so u and v each
have exactly one hole into Pᵢ at distinct vertices; and every pivot
w₁ ∈ U₁ has exactly one hole into each Uᵢ, landing inside Uᵢ.
*Proof.*  |Uᵢ| ≥ 3, |U₁| ≥ 1 by budgets.  If |Uᵢ| ≥ 4: take w₁ ∈ U₁,
Uⱼ′ = Uⱼ ∩ N(w₁) (sizes ≥ |Uⱼ| − 1); Lemma G on (Uᵢ′; Uⱼ′, Uₖ′) yields a
present transversal, and {u, v, w₁, w₂, w₃, w₄} spans all 15 pairs — K₆.
Same argument forces |Uᵢ′| = 2. ∎

**Theorem (Case B).**  The four P₀-edges span ≥ 4 vertices of P₀; by
Lemma E each spanned vertex carries exactly one hole into each of
P₂, P₃, P₄ — all distinct pairs.  Total ≥ 3·4 = 12 > 10.  ∎  Combined
with Case A: **e(H) ≤ 264, i.e. m\* ≥ 61**, trust base Füredi 2015
Thm 1 + elementary counting.

Remarks.  (1) Retrofit: the same lemmas re-close Case A at ≥ 16 > 10 and
Milestone 1 at ≥ 12 > 8, with slack.  (2) Machine cross-checks (OR-Tools
CP-SAT, artifacts/caseB/): full Case-B spec INFEASIBLE at ≤ 10 holes for
all nine non-isomorphic 4-edge P₀-configurations; the premise-exact
relaxation (exactly the proof's hypotheses) INFEASIBLE at ≤ 11 and ≤ 14,
matching the hand bounds 12 and 15; encoding validated by verified SAT
witnesses at higher hole counts and by rejection of two near-miss hand
allocations exactly where Lemma G predicts.  Lemma G itself brute-forced:
(3,2,2) unblockable, (2,2,2) blockable with minimum 6.

### Rung q = 6 (m\* ≥ 62) status

Machine ground truth: all 27 cases (nine P₀-configs × {matching in P₁,
path in P₁, edges in P₁ and P₂}) INFEASIBLE at ≤ 12 under the full
spec — every (6,5,5,5,5) sub-case of q = 6 is TRUE and awaits hand
polish.  By hand: both-edges-in-P₁ closes via Lemmas G/E + endpoint
accounting (~2 pages, checked branch-by-branch); e(P₀) = 5 and 6 splits
close free (≥ 15 > 12 with the pivot bonus; Case A's 13/16 > 12).  The
one real hand-gap in (6,5,5,5,5): the edges-in-two-parts variant's
three-system dichotomy.  Genuinely open at q = 6: the **(7,5,5,5,4)
size vector** — the 4-part admits no single-vertex budget, so the grid
machinery needs a new foothold there.

## Rungs q = 6..10 (toward 66 = the r=5 proof)

q = 6 adds the size vector (7,5,5,5,4) (7-part carrying all I = 6, every
6-subset of it spanning ≥ 4); q ≥ 8 adds two-6-part vectors.  The
skeleton (stability → forced shapes → budgets → covering) applies
throughout; the open question is whether the slack survives the loosened
budgets.  q = 6 re-derives the imported pass-ladder 62 *unconditionally*.

**Foothold notes for (7,5,5,5,4)** (2026-06-12, groundwork): write Q for
the 4-part, P₇ for the 7-part (e(P₇) ≥ 6 forced).
(a) *Q has PAIR-budgets*: for outside vertices w, w′ the 6-set
{w, w′} ∪ Q gives e(Q) + deg_Q(w) + deg_Q(w′) + [ww′ ∈ H] ≥ 4; with
e(Q) = 0, joint holes into Q are ≤ 4 + [ww′].  So at most one vertex in
the graph has ≥ 3 Q-holes, and any two with 2 each must be H-adjacent.
(b) *The adversary's refuge is Q-side blocking*: for uv ⊆ P₇, Lemma G
still forces present triangles across the three empty 5-parts, but the
K₆ needs a fourth vertex in U_Q adjacent to the triangle — each q ∈ U_Q
dodges a given triangle with one budget-1 hole into a 5-part, shrinking
the grid to (2,2,2), which IS blockable (min 6).  Lemma E does not
transfer; the demand must charge (i) q-side dodging holes, (ii) residual
(2,2,2)-grid blocking at ~6 β-holes, (iii) P₇-internal spread (6 edges
on 7 vertices with every 6-subset ≥ 4 ⟹ ≥ 5 vertices spanned).
(c) *Target*: at q = 6 this vector has cross-pairs 268 and e(H) = 264,
so holes = 268 + 6 − 264 = **10**; the (i)+(ii)+(iii) accounting must
beat 10, with the pair-budget lattice (a) making Q-spends expensive at
scale.

**Partial hand progress (2026-06-13), the C₆ sub-case — clean knockout.**
P₇ has 6 edges, max-degree ≤ 2 (every 6-subset ≥ 4 ⟹ deg ≤ 2), so it is
a union of paths/cycles.  Take the sub-case P₇ = C₆ ⊔ K₁.  For an internal
edge uv, U_Q := Q ∩ N(u) ∩ N(v).
- If **U_Q = ∅** (u,v jointly miss all 4 of Q), then h_Q(u) + h_Q(v) ≥ 4
  (each Q-vertex missed by u or v).  Suppose this holds for *every* C₆
  edge.  Sum over the 6 edges: Σ_{uv∈C₆}[h_Q(u)+h_Q(v)] =
  Σ_{x∈C₆} deg_{C₆}(x)·h_Q(x) = 2 Σ_x h_Q(x) ≥ 24, so the Q-holes
  incident to C₆ number ≥ 12 > 10 = budget.  **Contradiction.**  Hence at
  least one C₆ edge has U_Q ≠ ∅.
- If **U_Q ≠ ∅**, pick w_Q ∈ U_Q.  Its single-vertex budget into each
  empty 5-part holds (6-set {w_Q}∪P_i, P_i empty ⟹ ≤1 hole), so
  |N(w_Q)∩U_i| ≥ |U_i|−1 ≥ 2.  To avoid a K₆ {u,v,w_Q,·,·,·}, Lemma G
  must fail on (N(w_Q)∩U_a, N(w_Q)∩U_b, N(w_Q)∩U_c): no coordinate ≥ 3,
  forcing all three = 2 (w_Q spends 3 holes, one per empty part) AND the
  residual 2×2×2 grid carries no present triangle (≥ 6 holes among the
  empty parts, per the caseB exhaustion).  So this edge alone charges
  ≥ 3 + 6 = 9.

STATUS: the C₆ sub-case is one combine-step from closed (9 from the
U_Q≠∅ edge + the residual Q-holes from the other five edges must exceed
10 — needs the per-structure bookkeeping finished).  The other P₇
structures (C₅⊔P₂, C₃⊔P₄, P₇, C₄⊔P₃, C₃⊔C₃⊔K₁) need the same treatment.
NOT a complete proof yet — recorded so it is not lost; the cloud decision
ladder (dec61) settles m* ≥ 62 by machine in parallel as the reliable
route.

## Multiedge agent integration (2026-06-13) — what is verified vs claimed

A second agent attacked the joint multi-edge accounting.  Its artifacts
were lost (ephemeral /tmp cleaned on completion), so its claims are
triaged here by what survives independent recheck.

**INDEPENDENTLY CONFIRMED (re-reproduced here, `verify_18lemma.py`):**
the "18-lemma".  A single internal edge uv ⊆ P₀ with all four 5-parts
empty forces its U-grid (3×3×3×3) to be blocked by between-part holes,
and under the Foothold-1 *matching* constraint (each vertex ≤ 1 hole per
part) the exact minimum is **18** — not the naive covering bound 9
(which ignores the matching constraint; the constraint is the whole
crux).  So the single-edge Case-A demand is 8 (endpoints) + 18 = **26**,
and since 26 > 2q for all q ≤ 12, **Case A (all 5-parts internally
empty) dies at every rung through q = 12**.  Consequence (the agent's
L4): at every rung q ≤ 10 some 5-part must carry an internal edge — the
fight is always in the "Case B and beyond" regime.

**SOUND, elementary, spot-checked — the shape census** (min internal
edges f(m) of an m-part with every 6-subset ≥ 4 edges): f(≤5) = 0,
f(6) = 4, **f(7) = 6** (hand-verified: 5·e(P₇) ≥ 7·4 ⟹ e ≥ 6; P₇
achieves, every 6-subset of a path spans ≥ 4), f(8) = 8 (2-regular
forced), f(9) = 11 (excludes all 9-parts through q = 10), 4-parts need
Σf ≥ 15.  This pins the partition shapes per rung:
q ≤ 5 → only (6,5,5,5,5); q = 6 → adds (7,5,5,5,4); q = 8 → adds
(6,6,5,5,4),(8,5,5,4,4),(8,5,5,5,3); q = 10 → adds (7,6,5,4,4),(7,6,5,5,3).

**CLAIMED, artifacts lost — NOT banked, needs re-computation:**
- m\* ≥ 62 via (7,5,5,5,4): claimed closed by hand ("Σ ≥ 12 > budget").
  Status: the *other* shape at q=6, (6,5,5,5,5), is machine-verified
  27/27 (artifacts/caseB, two agents).  (7,5,5,5,4) is the sole
  remaining shape and is being settled cleanly by the direct probe at
  target 61 (`probe_mstar.py … 61`; INFEASIBLE ⟹ m\* ≥ 62 outright, no
  partition dependence) — running.
- Rungs q = 7..10 (m\* ≥ 63..66): the agent reported a 154-vector grid
  with per-vector CP-SAT minima, claiming q=7 "four exact solves away"
  and q ≤ 10 reducing to finishing the grid.  The agent itself did NOT
  claim 66 closed, and flagged q = 7 hand-ledgers landing *at* budget
  (14 vs 14) for cap-3/4 kill-vectors.  All artifacts lost.  This whole
  tower must be re-run before any m\* ≥ 63 claim — it is a roadmap, not
  a result.

**Honest ladder state: 61 PROVEN (hand, twice-checked); 62 machine-pending
(one shape left, direct probe running); 63–66 a documented roadmap whose
load-bearing lemma (18) now checks out but whose per-vector closures need
reconstruction.**
