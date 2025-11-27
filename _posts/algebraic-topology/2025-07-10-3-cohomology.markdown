---
layout: post
title: "Algebraic Topology 3: Cohomology"
date: 2025-07-10 09:02:00 -0000
categories: algebraic-topology
---

We've seen how homology detects holes by finding cycles that are not boundaries. **Cohomology** is the powerful dual to homology. Instead of building objects (chains), it analyzes functions *on* those objects (cochains). This shift in perspective unlocks a much richer algebraic structure.

An intuition: Imagine a vector field on a surface. Homology might find a loop where the field flows consistently around a hole. Cohomology asks a different question: is this vector field the gradient of some scalar potential function? If a field is "locally" a gradient (its curl is zero everywhere), but it's not "globally" a gradient, it must be because it wraps around a hole.

### The Machinery of Cohomology: Duality

The setup for cohomology is a direct dualization of homology. We take the entire chain complex construction and apply the $$\text{Hom}(–, G)$$ functor, which essentially means we replace vector spaces with their duals and linear maps with their transposes.

1.  **Cochain Groups ($$C^k$$):** A k-cochain is a linear function $$f: C_k \to G$$ that assigns a value from a coefficient group $$G$$ (e.g., $$\mathbb{R}$$ or $$\mathbb{Z}$$) to each k-simplex. The space of all such functions is the dual space $$C^k = \text{Hom}(C_k, G)$$.

2.  **Coboundary Operator ($$\delta^k$$):** The coboundary operator $$\delta^k: C^k \to C^{k+1}$$ is the dual map (transpose) of the boundary operator $$\partial_{k+1}$$. It's defined by the relation: $$(\delta f)(\sigma) = f(\partial\sigma)$$ for a k-cochain $$f$$ and a (k+1)-simplex $$\sigma$$. This is a discrete version of Stokes' Theorem.

Since $$\partial \circ \partial = 0$$, it follows that **$$\delta \circ \delta = 0$$**.

3.  **Cocycles ($$Z^k = \ker \delta^k$$):** The k-cocycles are k-cochains $$f$$ whose coboundary is zero. A 1-cocycle, for instance, is a function on edges that sums to zero around any filled triangle (i.e., it's locally consistent).

4.  **Coboundaries ($$B^k = \text{im } \delta^{k-1}$$):** The k-coboundaries are k-cochains that are the coboundary of a (k-1)-cochain. A 1-coboundary, for example, is a function on edges whose values are simply the differences in the values of a 0-cochain (a function on vertices). It's a "global gradient."

### A Concrete Example: De Rham Cohomology

For those familiar with calculus on manifolds, there is a beautiful, parallel theory.
- **The space:** A smooth (differentiable) manifold $$M$$.
- **The "cochains":** Instead of functions on simplices, we use smooth **differential k-forms**, $$\Omega^k(M)$$. A 0-form is a smooth function, a 1-form is like a vector field, etc.
- **The "coboundary operator":** The **exterior derivative** $$d: \Omega^k(M) \to \Omega^{k+1}(M)$$. This operator generalizes grad, curl, and div.
- **The crucial property:** A fundamental fact from calculus is that $$d(d\omega) = 0$$ for any k-form $$\omega$$. That is, **$$d^2 = 0$$**.

This gives us a new chain complex, the de Rham complex. We define:
- **Closed k-forms:** Forms $$\omega$$ such that $$d\omega = 0$$. These are the "cocycles."
- **Exact k-forms:** Forms $$\omega$$ such that $$\omega = d\eta$$ for some (k-1)-form $$\eta$$. These are the "coboundaries."

The **k-th de Rham cohomology group** is then:
$$ H^k_{dR}(M) = (\text{Closed k-forms}) / (\text{Exact k-forms}) $$

**De Rham's Theorem** states that for a smooth manifold M, the de Rham cohomology is isomorphic to the singular (or simplicial) cohomology with real coefficients: $$H^k_{dR}(M) \cong H^k(M; \mathbb{R})$$. This is a profound result: it shows that a purely analytic construction (derivatives of forms) computes a purely topological invariant (the number of holes).

### Cohomology Groups and the Cup Product

The k-th **cohomology group ($$H^k$$)** is the quotient group:

$$ H^k(X; G) = Z^k / B^k = (\text{Cocycles}) / (\text{Coboundaries}) $$

For many "nice" spaces, the cohomology groups are isomorphic to the homology groups. The Universal Coefficient Theorem gives the precise relationship. So why the extra machinery?

The power of cohomology lies in its extra structure. The direct sum of cohomology groups forms a **graded ring**. We can define a product, the **cup product**, which maps $$\cup: H^p \times H^q \to H^{p+q}$$.

Given a p-cocycle $$\phi$$ and a q-cocycle $$\psi$$, their cup product $$(\phi \cup \psi)$$ is a (p+q)-cocycle defined on a (p+q)-simplex $$\sigma = [v_0, \dots, v_{p+q}]$$ by:
$$ (\phi \cup \psi)(\sigma) = \phi([v_0, \dots, v_p]) \cdot \psi([v_p, \dots, v_{p+q}]) $$
This product is associative and graded-commutative. It gives the **cohomology ring**, a powerful invariant that homology lacks. In de Rham theory, the cup product corresponds to the wedge product $$\wedge$$ of differential forms.

### Example: Torus vs. Wedge of Spheres

Let's see the cup product in action. Consider two spaces:
1.  The torus $$T^2 = S^1 \times S^1$$.
2.  The wedge $$X = S^1 \vee S^2$$ (a sphere attached to a circle at a single point).

Both spaces have the same homology groups: $$H_0=\mathbb{Z}, H_1=\mathbb{Z}, H_2=\mathbb{Z}$$. They are indistinguishable from the perspective of Betti numbers.

Now let's look at their cohomology rings.
- **For the torus $$T^2$$:** Let $$\alpha \in H^1$$ be the cocycle corresponding to the loop around the short way, and $$\beta \in H^1$$ be the cocycle for the long way. Their cup product $$\alpha \cup \beta$$ is a non-zero element in $$H^2(T^2)$$. It represents the fundamental 2-cell of the torus. The ring structure is that of an exterior algebra on two generators.
- **For the wedge $$X = S^1 \vee S^2$$:** Let $$\gamma \in H^1$$ be the generator from the circle part. Any cup product of positive-degree elements is zero. In particular, $$\gamma \cup \gamma = 0$$. There is no way to combine 1D classes to get a 2D class because the 1D and 2D parts of the space only touch at a single point.

The non-trivial cup product on the torus tells us its 1D holes are intertwined in a way that "creates" a 2D hole. The trivial cup product on the wedge tells us its 1D and 2D holes are separate. Cohomology doesn't just count holes; it reveals their multiplicative relationships. In our next post, we'll shift gears to an entirely different approach: **homotopy**.
