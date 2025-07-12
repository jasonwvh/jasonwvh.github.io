---
layout: post
title: "Algebraic Topology 3: Cohomology"
date: 2025-07-10 09:02:00 -0000
categories: algebraic-topology
---

We've seen how homology detects holes by finding cycles that are not boundaries. **Cohomology** is the powerful dual to homology. Instead of building objects (chains), it analyzes functions *on* those objects (cochains). This shift in perspective unlocks a much richer algebraic structure.

An intuition: Imagine a vector field on a surface. Homology might find a loop where the field flows consistently around a hole. Cohomology asks a different question: is this vector field the gradient of some scalar potential function? If a field is "locally" a gradient (its curl is zero everywhere), but it's not "globally" a gradient, it must be because it wraps around a hole.

### The Machinery of Cohomology: Duality

The setup for cohomology is a direct dualization of homology. We take the entire chain complex construction and apply the `Hom(–, G)` functor, which essentially means we replace vector spaces with their duals and linear maps with their transposes.

1.  **Cochain Groups (C^k):** A k-cochain is a linear function `f: C_k -> G` that assigns a value from a coefficient group `G` (e.g., ℝ or ℤ) to each k-simplex. The space of all such functions is the dual space `C^k = Hom(C_k, G)`.

2.  **Coboundary Operator (δ^k):** The coboundary operator `δ^k: C^k -> C^{k+1}` is the dual map (transpose) of the boundary operator `∂_{k+1}`. It's defined by the relation: `(δf)(σ) = f(∂σ)` for a k-cochain `f` and a (k+1)-simplex `σ`. This is a discrete version of Stokes' Theorem.

Since `∂ ∘ ∂ = 0`, it follows that **`δ ∘ δ = 0`**.

3.  **Cocycles (Z^k = ker δ^k):** The k-cocycles are k-cochains `f` whose coboundary is zero. A 1-cocycle, for instance, is a function on edges that sums to zero around any filled triangle (i.e., it's locally consistent).

4.  **Coboundaries (B^k = im δ^{k-1}):** The k-coboundaries are k-cochains that are the coboundary of a (k-1)-cochain. A 1-coboundary, for example, is a function on edges whose values are simply the differences in the values of a 0-cochain (a function on vertices). It's a "global gradient."

### A Concrete Example: De Rham Cohomology

For those familiar with calculus on manifolds, there is a beautiful, parallel theory.
- **The space:** A smooth (differentiable) manifold `M`.
- **The "cochains":** Instead of functions on simplices, we use smooth **differential k-forms**, `Ω^k(M)`. A 0-form is a smooth function, a 1-form is like a vector field, etc.
- **The "coboundary operator":** The **exterior derivative** `d: Ω^k(M) -> Ω^{k+1}(M)`. This operator generalizes grad, curl, and div.
- **The crucial property:** A fundamental fact from calculus is that `d(dω) = 0` for any k-form `ω`. That is, **`d² = 0`**.

This gives us a new chain complex, the de Rham complex. We define:
- **Closed k-forms:** Forms `ω` such that `dω = 0`. These are the "cocycles."
- **Exact k-forms:** Forms `ω` such that `ω = dη` for some (k-1)-form `η`. These are the "coboundaries."

The **k-th de Rham cohomology group** is then:
**H^k_{dR}(M) = (Closed k-forms) / (Exact k-forms)**

**De Rham's Theorem** states that for a smooth manifold M, the de Rham cohomology is isomorphic to the singular (or simplicial) cohomology with real coefficients: `H^k_{dR}(M) ≅ H^k(M; ℝ)`. This is a profound result: it shows that a purely analytic construction (derivatives of forms) computes a purely topological invariant (the number of holes).

### Cohomology Groups and the Cup Product

The k-th **cohomology group (H^k)** is the quotient group:

**H^k(X; G) = Z^k / B^k = (Cocycles) / (Coboundaries)**

For many "nice" spaces, the cohomology groups are isomorphic to the homology groups. The Universal Coefficient Theorem gives the precise relationship. So why the extra machinery?

The power of cohomology lies in its extra structure. The direct sum of cohomology groups forms a **graded ring**. We can define a product, the **cup product**, which maps `∪: H^p × H^q -> H^{p+q}`.

Given a p-cocycle `φ` and a q-cocycle `ψ`, their cup product `(φ ∪ ψ)` is a (p+q)-cocycle defined on a (p+q)-simplex `σ = [v₀, ..., v_{p+q}]` by:
`(φ ∪ ψ)(σ) = φ([v₀, ..., v_p]) ⋅ ψ([v_p, ..., v_{p+q}])`
This product is associative and graded-commutative. It gives the **cohomology ring**, a powerful invariant that homology lacks. In de Rham theory, the cup product corresponds to the wedge product `∧` of differential forms.

### Example: Torus vs. Wedge of Spheres

Let's see the cup product in action. Consider two spaces:
1.  The torus `T² = S¹ × S¹`.
2.  The wedge `X = S¹ ∨ S²` (a sphere attached to a circle at a single point).

Both spaces have the same homology groups: H₀=ℤ, H₁=ℤ, H₂=ℤ. They are indistinguishable from the perspective of Betti numbers.

Now let's look at their cohomology rings.
- **For the torus `T²`:** Let `α ∈ H¹` be the cocycle corresponding to the loop around the short way, and `β ∈ H¹` be the cocycle for the long way. Their cup product `α ∪ β` is a non-zero element in `H²(T²)`. It represents the fundamental 2-cell of the torus. The ring structure is that of an exterior algebra on two generators.
- **For the wedge `X = S¹ ∨ S²`:** Let `γ ∈ H¹` be the generator from the circle part. Any cup product of positive-degree elements is zero. In particular, `γ ∪ γ = 0`. There is no way to combine 1D classes to get a 2D class because the 1D and 2D parts of the space only touch at a single point.

The non-trivial cup product on the torus tells us its 1D holes are intertwined in a way that "creates" a 2D hole. The trivial cup product on the wedge tells us its 1D and 2D holes are separate. Cohomology doesn't just count holes; it reveals their multiplicative relationships. In our next post, we'll shift gears to an entirely different approach: **homotopy**.
