# GPT Pro prompt #3 — generalize the cross-part-triangle lemma to the whole residue

> Paste below the line into the same GPT Pro chat. Your previous lemma was
> CERTIFIED (verified independently three ways, including a machine check against
> the full model). This asks you to push the same method across the rest of the
> q = 8,9,10 residue.

---

Your cross-part-triangle lemma is **certified**. We reproduced every finite check
independently and machine-confirmed the obstruction directly against the full model
(fixing the core to X\* and to the empty core both give UNSAT at cap 38). So
`min_holes(star + F in one 5-part) ≥ B(F)` holds for F ∈ {K\_{2,3}, C₅, C₄, P₄},
all above the cap. That family of the q=8,9,10 residue is closed by hand.

Now extend the **same machinery** to the rest of the residue. The setup is
unchanged (shape (6,5,5,5,5), parts P₀ size 6 and P₁..P₄ size 5, d=0, cap = I+q;
holes = absent cross-pairs; min_holes is the least holes making the complement
K₆-free with every 6-set spanning ≥ 4 edges; a config is closed at rung q iff
min_holes > cap). The general cross-part-triangle framework you should now use:

- an **internal edge** ab in any part (P₀ or some Pᵢ) plus any vertex w in a
  *different* part with wa, wb present is an active triangle {w,a,b};
- its K₆ completions run over the **empty** 5-parts, so (local matching budget:
  ≤ 1 hole per vertex per empty part; MATCH_BLOCK(3,2,2)=∞, MATCH_BLOCK(2,2,2)=6)
  each active triple forces 3 anchor-empty holes per anchor across the empty parts
  plus a 6-hole residual, exactly as in the certified lemma;
- aggregate: non-core holes ≥ 3·|U(X)| + 6 (or more, when ≥ 4 empty parts give
  larger MATCH_BLOCK residuals), where U(X) is the union of active-triple vertices.

## The residue still open (target these)

After the certified single-loaded-part star family, the q=8,9,10 residue is the
configs with **triangle-free, low-clique internal graphs** in these edge-profiles
(e₀,e₁,e₂,e₃,e₄ = internal edges per part, P₀ first), from the census in
`road66/handlemma/LEMMAS.md §8`:

1. **Edges spread across two 5-parts:** (4,1,1,0,0), (4,2,2,0,0) — a P₀ star plus
   triangle-free edges in *two* different 5-parts (so two loaded grids, not one).
   The fractional packing already closes the ≥3-part spreads; these 2-part spreads
   are the gap it left.
2. **Non-star P₀:** (5,1,0,0,0), (6,2,0,0,0), (7,1,0,0,0) — P₀ carries 5–7
   *triangle-free* edges (a non-star graph on 6 vertices: paths, C₄/C₅/C₆, K\_{2,3},
   K\_{2,4}, …) plus a lightly loaded 5-part. (If P₀ contains a triangle, the
   campaign's clique-core lemma already closes it, so assume P₀ triangle-free.)
3. **Mixed small:** (4,2,0,0,0), (4,4,0,0,0) and similar single-loaded profiles with
   F a *smaller* triangle-free graph — likely already inside your lemma's formula;
   confirm or extend.

## Deliverable

1. A **general aggregation bound** `min_holes(config) ≥ B(config)` for arbitrary
   triangle-free internal graphs distributed over the parts, proven by the same
   single-triple-forcing + no-overlap-collapse argument, with the empty-part count
   handled correctly (a config with k loaded parts has 4−k (or 5−k) empty parts;
   the MATCH_BLOCK residual and the per-anchor quota scale with that). State it so
   that `B(config) > cap = I + q` can be checked per profile.
2. A **core scan / finite verifier** (same shape as before: enumerate valid core
   patterns, compute |U|, report min B) for each target profile, and the resulting
   bound vs. cap at q = 8, 9, 10. Where equality could meet the cap, add the
   rainbow-style obstruction.
3. **A precise coverage statement:** which residue profiles your generalized lemma
   closes (B > cap) and which it does **not** — the genuine remainder that still
   needs the machine. A smaller honest covered-set with airtight finite checks beats
   an overclaim; if a profile resists, say which and why (where the anchor count or
   the empty-part budget falls short of the cap).
4. Same verification contract: every constant reduces to a finite check; mark any
   unproven sub-claim; never assert a proof you cannot verify; and for any bound you
   claim, give the exact `fix-core`-style assertion we can machine-check (pin the
   core, ask for a ≤ (cap)-hole completion, expect UNSAT).

If the generalized method closes the entire triangle-free residue, that plus the
clique-core lemmas and the fractional packing would close rungs 8,9,10 by hand and
give m\* ≥ 66 without the CP-SAT sweep. If it closes most but leaves a remainder,
tell us exactly what remains so we can sweep only that — minutes of compute instead
of the full residue.
