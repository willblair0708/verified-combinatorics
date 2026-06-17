# Candidate OEIS extensions from the Vela discovery engine

The `vela campaign` discovery engine (deterministic seeded search +
frozen-verify) produced verified lower bounds that extend three OEIS sequences
past their last listed term (data field AND b-file checked 2026-06-16). All
witnesses re-verify from scratch with `vela reproduce`. **These are lower
bounds, not proven maxima; submitting is the account holder's call.**

Ranked by how much we should trust the extension — measured by whether the
engine reproduces the sequence's *already-proven* terms:

## 1. A321531 — rook directions  (strongest; submission drafted)

Reproduces **every** listed term exactly: a(4..10) = 4,6,8,11,14,18,23. Then:
a(11..20) ≥ 28,33,38,43,49,56,62,70,77,86. Because it hits every proven
maximum it can be checked against, the extension is credible. See
`rook-directions-A321531/SUBMISSION_DRAFT.md`.

## 2. A394031 — Sidon sets in GF(2)^n  (moderate)

Matches a(2..9) exactly, but tops out at 32 vs the known a(10)=34 — so the
greedy is not reliably optimal here. Extensions are looser lower bounds:
a(11) ≥ 48, a(12) ≥ 52, a(13) ≥ 68, a(14) ≥ 88. Worth a stronger search
(SA / algebraic seeds) before submitting; a better construction likely beats
these.

## 3. A347025 — union-free families  (weakest)

Misses a(6) by one (23 vs the known 24), so the local search is clearly not
optimal for this sequence. Extensions are loose lower bounds: a(8) ≥ 60,
a(9) ≥ 107, a(10) ≥ 175. Treat as a floor, not a record.

---

**Method note.** "Reproduces the proven terms" is the credibility test. Rook
passes it cleanly; the other two miss one proven term each, which is exactly
why their extensions carry less weight. A stronger search that closes the
a(6)=24 and a(10)=34 gaps would also raise confidence in the n beyond.
