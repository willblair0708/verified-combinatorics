# GPT Pro prompt — the concentrated triangle-free residue of Erdős #617 (m* ≥ 66)

> Paste everything below the line into GPT Pro. It is self-contained. The target
> is ONE residue family, embedded in a verification contract — not "solve #617."
> Whatever it returns must be machine-checked (general_rung.py / blocking.py /
> verify_packing.py) before any claim is trusted.

---

You are assisting a computer-assisted proof in extremal graph theory. Your job is
to propose a **machine-checkable integer combinatorial lemma**, not to "solve" a
problem in prose. Hard rules:

- Every claim you make must come with an **exact, finite verification procedure**
  (a small search, a blocking-number computation, a parity/counting check).
- If a step is unproven, **mark it explicitly** as a gap and say what is missing.
  Do **not** assert a proof you cannot verify. Partial lemmas are valuable; fake
  proofs are worse than nothing.
- If you can execute code, implement every numerical claim and run it. If you
  cannot, specify the exact code to run and the expected output.

## 1. The problem and the reduction

Erdős–Gyárfás (Combinatorica 1997) ask, for the first open case r = 5: in any
5-colouring of K_26, must some 6 vertices induce a K_6 missing a colour? Call a
colouring *balanced* if every 6 vertices see all 5 colours. Fix one colour class
G. Balanced ⟹ (A) α(G) ≤ 5 and (B) every 6-set spans ≤ 11 G-edges. Let m* = min
e(G) over such G on 26 vertices. Since 5·66 = 330 > 325 = e(K_26), **m* ≥ 66
settles the case**.

Pass to the complement H = G̅ on 26 vertices: H is **K_6-free** and **every 6-set
spans ≥ 4 edges**. As e(G)+e(H)=325, m* ≥ 66 ⟺ e(H) ≤ 259.

**Already proven (do not redo): m* ≥ 63** (i.e. e(H) ≤ 262), unconditionally, by
a Füredi-stability rung argument. What remains for m* ≥ 66 is to kill rungs
q = 8, 9, 10.

## 2. The rung accounting (exact)

By Füredi stability, e(H) = 270 − q forces a 5-partition of the 26 vertices, part
sizes (n_0,…,n_4), with internal (within-part) edge count I ≤ q. Define defect
d = Σ C(n_i,2) − 55. Then the number of **holes** (missing cross-part pairs)
satisfies the identity

    holes = I + q − d =: cap.

A configuration = (part sizes, the fixed internal graph). It is **INFEASIBLE**
(cannot occur, so contributes to closing the rung) **iff min_holes(config) >
cap**. Your goal is lower bounds `min_holes(config) ≥ B > cap`.

The dominant shape is (n_0,…,n_4) = (6,5,5,5,5), defect d = 0, so cap = I + q.
Parts: P_0 (size 6), P_1,…,P_4 (size 5 each).

## 3. The exact decision model (this is the ground truth verifier)

Vertices 0..25 partitioned into the parts. Internal edges E (within-part) are
fixed by the configuration. For each **cross-pair** p = {a,b} with a,b in
different parts, a Boolean variable x_p ∈ {0,1}: x_p = 1 means p is a *hole*
(absent in H). Constraints:

1. **Budget:** Σ_p x_p ≤ cap.
2. **Every-6-set-≥4-edges (Füredi):** for every 6-subset S, let c(S) = its
   cross-pairs and i(S) = its present internal edges. Then
   Σ_{p ∈ c(S)} x_p ≤ |c(S)| + |i(S)| − 4. (If the RHS < 0 for some S, the
   config is infeasible outright.)
3. **K_6-freeness:** for every 6-subset S all of whose within-part pairs are
   present internal edges, Σ_{p ∈ c(S)} x_p ≥ 1 (the would-be K_6 must carry a
   hole).

`min_holes` = the minimum of Σ_p x_p over all assignments satisfying (2),(3).
INFEASIBLE at rung q ⟺ min_holes > cap. This model is `general_rung.py`; you may
assume a working CP-SAT oracle exists and is the final arbiter.

## 4. What is ALREADY closed (do not re-derive)

- **Case A** (all internal edges inside P_0): holes ≥ 26 unconditionally
  (`Theorem A`), so dead at every q ≤ 12. Mechanism: pick a P_0 edge {u,v}; the
  sets U_i = P_i ∩ N(u) ∩ N(v) have |U_i| ≥ 3, and the K_6 {u,v}∪(transversal)
  forces blocking the U_1×U_2×U_3×U_4 grid; **BLOCK(3,3,3,3) = 18** (integer)
  plus 8 endpoint holes.
- **Clique cores** (`Lemma C`, integer blocking numbers, all exact): a triangle
  in a 5-part with ≥3 other empty 5-parts ⟹ holes ≥ 15; a K_4 (≥2 empty) ⟹ ≥ 9;
  a K_5 (≥1 empty) ⟹ ≥ 5.
- **Lemma D:** an internal edge + an empty 4-part + 3 empty 5-parts ⟹ K_6
  forced (infeasible at every cap).
- **Diffuse matchings** (explicit fractional packing, hand-auditable): internal
  edges forming a part-disjoint matching across ≥ 3 empty 5-parts close at q = 8
  (and the 4-part spread at q = 8,9,10).

## 5. YOUR TARGET — the concentrated triangle-free residue

The ONLY open family is: **a triangle-free graph concentrated in a single 5-part**
(plus a star K_{1,4} in P_0), shape (6,5,5,5,5). The internal graph on the one
loaded 5-part P_1 is one of: **K_{2,3}** (deg seq 3,3,2,2,2; 6 edges — the unique
triangle-free 6-edge graph on 5 vertices), **C_5**, **C_4**, or a **path P_4**.

Canonical hardest atom: **star(P_0) + K_{2,3}(P_1)**, I = 10, at q = 10, cap = 20.
The CP-SAT oracle proves it INFEASIBLE (min_holes ≥ 21 > 20; ~478 s). Your job: a
**clean integer lower bound min_holes ≥ B > cap** for this family, replacing the
per-config solver run with a lemma.

## 6. CRITICAL — what is PROVEN to NOT work (do not propose these)

This is the load-bearing constraint on your search. We *proved* (two independent
ways) that **fractional/LP packing and clique-core counting cannot reach the cap**
on this family — it is a theorem about the LP, not a lack of cleverness:

- The exact LP relaxation of the full model (covering + Füredi cuts) gives
  min_holes ≥ **13.75** for K_{2,3}, while the integer min is **≥ 21**. Gap ≈ 1.5.
- The Case-A bound rests on BLOCK(3,3,3,3) = **18** (integer); its LP relaxation
  is only **9** (put 1/4 on each grid hole — every transversal covered 1.5, every
  vertex load 0.75). A factor-2 gap baked into the geometry.
- **Mechanism:** a dense 5-part **absorbs its own Füredi constraints** — with
  e(P_1) = 6 the cut "{w}∪P_1 spans ≥ 4 edges" is vacuous, so a dense part offers
  a packing nothing, and the per-edge ("single-edge") charge collapses to ≈ 5.

**Therefore any lemma that works MUST be a genuinely integer argument** — a
blocking/parity/transversal count that exploits the integrality the LP cannot see
(in the spirit of BLOCK(3,3,3,3)=18, but for the triangle-free dense part where no
clique core exists). Fractional certificates, single-edge charging, and
clique-core demands are dead ends here; do not propose them.

## 7. Where the integer structure plausibly lives (a hint, not a constraint)

The K_6s that must be blocked split into two kinds: (i) **dense-part-anchored** —
two adjacent vertices of P_1 (an edge of K_{2,3}/C_5/C_4/path) plus a transversal
(w_0,w_2,w_3,w_4), one vertex from each of P_0,P_2,P_3,P_4; (ii)
**star-anchored** — a star edge {c,ℓ} in P_0 plus a transversal across
P_1,P_2,P_3,P_4. Each present internal edge generates a whole transversal grid of
forbidden K_6s; the holes blocking them are shared across many K_6s, but the
integer blocking minimum over the *union* of these grids exceeds what any single
grid's fractional relaxation sees. The open question is a clean integer count of
holes forced by simultaneously blocking the K_{2,3}-edge grids + the star grid,
with the foothold budget "each outside vertex has ≤ 1 hole into each empty 5-part"
(from {w}∪P_i, |P_i|=5, forcing deg ≥ 4).

## 8. Deliverable

For the family in §5 (start with the K_{2,3} atom at q = 10, cap = 20):

1. A precise lemma statement: `min_holes(star + K_{2,3} in one 5-part) ≥ B`,
   with B ≥ 21 (and ideally a B(config) covering C_5/C_4/path too).
2. A complete proof **or** an explicit list of the unproven sub-claims, each
   reduced to a finite check (a blocking number on ≤ ~15 vertices, a parity
   argument, a transversal count).
3. The exact verification: state the small finite computation that confirms each
   numerical constant, in the style of BLOCK(sizes) (min holes to block all
   transversals of a product of independent sets under the per-vertex ≤1 matching
   budget). If you can run code, compute it and report the number; compare to the
   CP-SAT min_holes ≥ 21.
4. If you cannot reach B > cap, report the **best B you can rigorously prove**,
   which rungs it closes (closes iff B > I + q − d), and precisely which sub-claim
   blocks you — that itself shrinks the machine residue and tells us where to aim.

Do not pad. Lead with the lemma and its verification; relegate exploration to the
end. Remember: a smaller honest B with an airtight finite check beats a larger B
you cannot certify.
