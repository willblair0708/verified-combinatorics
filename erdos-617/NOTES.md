# Provenance, imported claims, and verification notes

## 1. Unconditional elementary facts (verified here, trivial)

For a 5-colouring of K_26, *balanced* means every 6-set sees all 5 colours.
Writing G_c for the colour-c graph:

* balanced ⟺ α(G_c) ≤ 5 for every colour c (every 6-set has a c-edge);
* hence every 6-set S has e_c(S) ≤ 15 − 4 = 11 for every c;
* hence (complement of G_c is K₆-free, Turán) |G_c| ≥ 325 − T(26,5)
  = 325 − 270 = **55**, unconditionally, for every colour.

## 2. Imported claims (NOT verified in this repository)

The following are quoted from ~20 earlier working passes whose artifacts
were never committed anywhere; they could not be re-verified here and every
"conditional" statement below depends on them:

* (P1) |G_c| ≥ 61 for every colour, and |G_c − v| ≥ 55 for every vertex.
* (P2) if |G_c| = 61 then G_c has a vertex v of degree 6; with A = N(v)
  (|A|=6), B = rest (|B|=19): e(G_c[B]) = 40 is forced.
* (P3) G[A] ≅ K₄⊔2K₁ (Case I) or K₄⊔K₂ (Case II); the A→B edges split as
  |N_B(p)|=4, |N_B(q)|=5 (Case I) resp. 4,4 (Case II) over the two
  non-K₄ vertices p,q, and the four K₄-vertices of A have **no**
  B-neighbours.
* (P4) Δ(B) ≤ 6, τ₃(B) ≥ 9.
* (P5) complement(B) is K₅-saturated and not 4-partite; τ₄(B) = 4.

Internal consistency checks that pass: e(A)+e(A,B)+e(B) = 6+9+40 = 55
(Case I) and 7+8+40 = 55 (Case II). ✓

## 3. The §3 hitset-pair derivations (re-derived independently — correct
**given** P2–P4)

All six-sets below must carry a colour-c edge (balancedness); u denotes any
K₄-vertex of A, which by (P3) has no B-neighbour and is non-adjacent to p
and q in G_c.

* **α(B) ≤ 4**: for a 5-set I ⊆ B, the 6-set {v}∪I has no c-edge at v
  (B = non-neighbours of v), so I contains an edge.
* **P hits every independent 4-set F of B** (both cases): the 6-set
  {p,u}∪F has c-edges only inside p→F = p→(F∩P); so F∩P ≠ ∅.  Symmetric
  for Q.
* **Case I, P∪Q hits every independent 3-set T of B**: the 6-set
  {p,q,u}∪T has c-edges only in p→(T∩P) ∪ q→(T∩Q) (p,q non-adjacent in
  Case I), so T∩(P∪Q) ≠ ∅.
* **Case I, P∩Q = ∅**: P∪Q is a τ₃-hitting set, |P∪Q| ≥ τ₃(B) ≥ 9 = |P|+|Q|.
  (Uses imported τ₃ bound (P4).)
* **Case I, e_B(Q) ≤ 6**: 6-set {q}∪Q carries 5 + e_B(Q) ≤ 11 c-edges.
* **Case II, e_B(P) + |P∩Q| ≤ 6**: 6-set {p,q}∪P carries
  1 (pq) + 4 (p→P) + |P∩Q| (q→P) + e_B(P) ≤ 11.  Symmetric for Q.
* τ₄(B) ≤ 4 is implied by P being a hitting 4-set, so (P5)'s τ₄(B)=4
  reduces to τ₄(B) ≥ 4.

WLOG canonical placement of (P,Q) used by the solver is sound: every
constraint of the spec is invariant under relabelling vertices of B, and in
Case II the sub-cases k = |P∩Q| = 0..4 are exhaustive.

## 4. Encoding soundness notes (solve_hitset_pair.py)

* Eagerly encoded: e(B)=40 (totalizer), Δ≤6 (seq. counters), α≤4
  (one clause per 5-set), hitting conditions (one clause per relevant
  4-/3-set), e_B(P)/e_B(Q) caps, K₅-saturation of the complement
  (per-pair existential gadgets, implication only in the sound direction),
  τ₄ ≥ 4 (per-3-set existential gadgets, sound direction).
* Lazily encoded (CEGAR, each added constraint individually implied by the
  spec): e_B(S) ≤ 11 per violated 6-set; "this particular partition of V
  into 4 parts is not a B-clique cover" per discovered cover.
* Termination: UNSAT, or a witness with no violated lazy condition; every
  SAT witness is re-verified by `check_witness.py` against the *entire*
  spec from scratch.

## 4b. Structural lemmas proved here (unconditional consequences of the spec)

* **Lemma 1** (Case I): e(B−P) ≥ 31 — `case1_structure.md`.
* **Lemma 2** (Case I): e(B−Q) ≥ 27 — `case1_structure.md`.
* **Lemma 3** (Case II): e(B−P) ≥ 31 and e(B−Q) ≥ 31 — `case2_structure.md`.
* **Restricted-T saturation**: every saturation witness T for a B-edge uv
  satisfies T∩P ≠ ∅ (unless u,v ∈ P) and T∩Q ≠ ∅ (unless u,v ∈ Q), because
  T∪{u}, T∪{v} are independent 4-sets which P,Q must hit.  Used to shrink
  the saturation gadgets ~3x in both solvers, soundly.

## 5. Results and run status

Diagnostics established by quick solver probes (artifacts/solve_log*.txt):

* The **encoder is sound and not vacuous**: with the single cap e_B(Q) ≤ 6
  removed, Case I (including e(B)=40, both hitting conditions, hit3,
  K₅-saturation, τ₄ ≥ 4, Δ ≤ 6, α ≤ 4) is SAT in < 0.1 s, and the model
  found is exactly the pass-20 "near-miss" family: P = K₄, Q = K₅,
  e(R) = 24 with α(R) ≤ 2, and **zero** P–Q, P–R, Q–R edges.
* The 4-clique control graph K₄⊔3K₅ is correctly rejected (e=36 ≠ 40) and
  `check_witness.py` reports exactly the expected pass/fail pattern on it.
* In Case II.k0 the caps e_B(P), e_B(Q) ≤ 6 are vacuous (max is C(4,2)=6),
  so that case is purely: two disjoint 4-sets each hitting every
  independent 4-set, under L1–L7.  Lemma 3 kills the natural 3K₅
  constructions for it.
* v1 CEGAR runs (lazy saturation) found relaxation models freely with the
  cap in place — so {core + cap} is SAT and **K₅-saturation is the
  binding constraint** in Case I; the hard search is the interaction
  "Q sparse" × "Q hits all independent 4-sets" × "complement saturated".

Verdict status at the time of this commit: Case I and Case II.k0 running
on two independent engines (CaDiCaL 1.9.5 incremental CEGAR; CP-SAT with
eager L4 + degree-sorted symmetry breaking); Case II.k1–k4 queued.
No case has yet returned UNSAT or a witness.  Any UNSAT verdict will be
re-certified from the dumped CNF via Glucose 4.2 DRAT + drat-trim
(`certify_unsat.py`, pipeline validated on PHP(4,3)); any witness will be
re-verified by `check_witness.py`.
