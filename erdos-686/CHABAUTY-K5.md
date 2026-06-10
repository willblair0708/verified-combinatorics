# k = 5, N = 4 reduces to one genus-2 curve

Date: 2026-06-09. Status: reduction proven (symbolically verified,
`verify_chabauty_reduction.py`); rank computation scoped; this is the
concrete path to closing the most valuable open cell of Erdős #686.

## The reduction

The equation `P₅(m) = 4·P₅(n)`, `P₅(y) = (y+1)⋯(y+5)`, centered at
`u = m+3, v = n+3`, becomes `g(u) = 4·g(v)` with the **odd** quintic
`g(u) = u⁵ − 5u³ + 4u = u(u²−1)(u²−4)`.

The plane curve `C : g(u) = 4g(v)` is a smooth quintic (verified: no shared
critical values, 5 distinct points at infinity), genus 6 — hopeless
directly. But oddness gives the involution `σ(u,v) = (−u,−v)`, with 6 fixed
points ((0,0) and the 5 points at infinity); Riemann–Hurwitz:
`10 = 2(2g′−2) + 6`, so the quotient `C/σ` has **genus 2**.

Explicitly, with `p = u²`, `q = v²`, `h(s) = (s−1)(s−4)`:

- `t := 4h(q)/h(p)` satisfies `p = q·t²`, and
- `q²(t⁵−4) − 5q(t³−4) + 4(t−4) = 0` — *quadratic in q*, so
- `w := 2q(t⁵−4) − 5(t³−4)` gives the hyperelliptic model

```
C₂ :  w² = D(t) = 9t⁶ + 64t⁵ − 200t³ + 64t + 144        (genus 2)
```

(`D` squarefree; leading coefficient `9 = 3²` ⇒ two rational points at
infinity.) All identities verified symbolically modulo the curve ideal.

**Lifting.** A point `(t,w) ∈ C₂(ℚ)` with `t⁵ ≠ 4` lifts to a point of
`C(ℚ)` iff `q = (w + 5(t³−4)) / (2(t⁵−4))` is a rational square (then
`p = qt²` is automatically one). Every integer solution of the original
equation with `u ∉ {0,±1,±2}` maps to such a point. Hence:

> **`C₂(ℚ)` finite and known ⇒ the cell (k=5, N=4) of #686 is closed.**

## Data

- Conductor (PARI `genus2red`): `1 364 371 875 = 3²·5⁵·139·349`.
  (Above the LMFDB genus-2 range, so the curve is not in LMFDB.)
- Point search to height 10⁶ (PARI `hyperellratpoints`): 34 affine points,
  x-coordinates `t ∈ {0, ±1, ±2, 4, −20, ±1/2, −38/5, −34/5, 2/7, −19/9,
  14/11, −20/17, −34/43, −53/55}` (each with ±w), plus `∞±`.
- Pullback analysis (all 34 checked): the lifting condition `q = □` holds
  only for the degenerate points (they map to `u², v² ∈ {0,1,4}`, i.e.
  product = 0) **and one nontrivial orbit**: `t = 14/11` lifts to
  `(u,v) = (±14/3, ±11/3)`, i.e. the rational identity
  `P₅(5/3) = 4·P₅(2/3)` — a non-integral rational point. No integral
  solutions appear, consistent with #686.
- The abundance of non-lifting rational points suggests
  `rank J(ℚ) ≥ 2`; analytic rank computation via PARI `lfungenus2` was
  started (slow at conductor ~1.4·10⁹; see logs).

## What a specialist (or a Magma session) should run

```magma
P<x> := PolynomialRing(Rationals());
C := HyperellipticCurve(9*x^6 + 64*x^5 - 200*x^3 + 64*x + 144);
J := Jacobian(C);
RankBounds(J);                      // expect 2 (maybe 3)
// if rank <= 1: Chabauty(J ! [pt - infty]) finishes immediately.
// if rank = 2:  quadratic Chabauty (Balakrishnan–Dogra–Müller toolkit),
//               or Two-cover descent + Mordell–Weil sieve:
TwoCoverDescent(C);
```

The Mordell–Weil sieve is particularly promising here because we do not
need all of `C₂(ℚ)`: we only need the points where `q` is a square, i.e.
rational points on the *double cover* `z² = q(t,w)`, which is a curve of
higher genus — an Elliptic-Chabauty-style finish over `ℚ` may apply to it
directly.

## Literature check (done 2026-06-09)

Web search found no prior treatment of the specific equation
`P₅(m) = 4·P₅(n)`: the classical results (Erdős–Selfridge;
Bennett–Bruin–Győry–Hajdu and successors) concern *perfect powers* of
products of consecutive terms, not fixed rational ratios between two
shifted blocks. The #686 forum thread is at
erdosproblems.com/forum/thread/686. A deeper check against the
`f(x) = c·f(y)` literature (Beukers-style, Hajdu–Pintér) is still advised
before publication.

## Caveats / further checks before claiming novelty

Equations `f(x) = c·f(y)` for products of consecutive integers have a
literature (Bennett–Bruin–Győry–Hajdu and successors on
`x(x+1)⋯(x+k−1) = c·y(y+1)⋯(y+k−1)`); the case `c = 4, k = 5` may already
be resolved or resolvable by their methods. Check before publishing:
- Bennett–Bruin–Győry–Hajdu, *Powers from products of consecutive terms in
  arithmetic progression* and related;
- Hajdu–Pintér and Beukers-style results on `f(x) = cf(y)`;
- Stoll's work on `y(y+1)⋯(y+k−1) = x(x+1)⋯(x+k−1)·c`.

## Outlook for other cells

The same oddness trick works for every odd `k` (P_k is odd around its
center) and every `N`: `g_k(u) = N·g_k(v)` has the `(−u,−v)` involution and
the quotient has genus `(k−1)/2 − 1 + (k − #{...})`-type drop; for `k = 5`
genus 6 → 2. For `k = 7`: genus 15 → quotient genus 6 (still hard). So
`k = 5` is the unique cell where this collapse lands in Chabauty range —
exactly the cell the pass-6 report identified as the most valuable target.
