---
layout: default
title: Trigonometry and Geometry Through 2-Dimensional Vectors
permalink: /math-talks/2d-vectors-and-geometry/
---

# Introduction to 2-Dimensional Vectors and Matrices and Results in Geometry and Trigonometry

## Putting 2-Dimensional Vectors in the Coordinate Plane

### Review of vectors

- Addition:
	- Associative: $(\vec a+\vec b)+\vec c=\vec a+(\vec b+\vec c)$
	- Commutative: $\vec a+\vec b=\vec b+\vec a$


- Multiplication by scalars:
	- Distributive: $c(\vec a+\vec b)=c\vec a+c\vec b$

![](https://www.albert.io/blog/wp-content/uploads/2025/03/Vector_addition_commutativity.svg){: width="30%"}
![](https://upload.wikimedia.org/wikipedia/commons/f/fa/Scalar_multiplication_by_r%3D3.svg){: width="30%"}

- Can vectors be multiplied by vectors?
- How to find a vector rotated/flipped/sheered/etc.?
- To answer these, we need a way to describe vectors using numbers

### How to describe vectors in the coordinate plane?

- Vector starting on origin $(0, 0)$ and ending on $(a,b)$: denote as vector $$\begin{pmatrix}a\\b\end{pmatrix}$$
- Represents $a$ unit to the right and $b$ unit upwards

![](https://wumbo.net/glossary/vector/figures/VectorExample-480-270.dark.svg){: width="60%"}

- $$\begin{pmatrix}a\\b\end{pmatrix}+\begin{pmatrix}c\\d\end{pmatrix}=\begin{pmatrix}a+c\\b+d\end{pmatrix}$$, $$n\begin{pmatrix}a\\b\end{pmatrix}=\begin{pmatrix}na\\nb\end{pmatrix}$$ (obvious and intuitive)

## Transforming Vectors: Matrices

Consider this problem:

> On the 2D coordinate system with origin $O$, point $A$ lies on $(3, 4)$. The entire coordinate system gets "sheered" horizontally so that point $(0, 1)$ goes to $(1, 1)$. Find where point $A$ ends up.

<video width="100%" height=auto controls>
	<source src="/images/math-talk/linalg-geometry/sheer.mp4" type="video/mp4">
</video>

- Notice that vector $$\begin{pmatrix}3\\4\end{pmatrix}$$ represents $$3\begin{pmatrix}1\\0\end{pmatrix}+4\begin{pmatrix}0\\1\end{pmatrix}$$
- When transformed, $$\begin{pmatrix}3\\4\end{pmatrix}$$ should still be equivalent to 3 times the transformed $$\begin{pmatrix}1\\0\end{pmatrix}$$ plus 4 times the transformed $$\begin{pmatrix}0\\1\end{pmatrix}$$
- After rotating, $$\begin{pmatrix}1\\0\end{pmatrix}$$ stays the same, and $$\begin{pmatrix}0\\1\end{pmatrix}$$ becomes $$\begin{pmatrix}1\\1\end{pmatrix}$$
- Thus $$\begin{pmatrix}3\\4\end{pmatrix}$$ transformed is $$3\begin{pmatrix}1\\0\end{pmatrix}+4\begin{pmatrix}1\\1\end{pmatrix}=\begin{pmatrix}7\\4\end{pmatrix}$$

### What about when vector $$\begin{pmatrix}x\\y\end{pmatrix}$$ is transformed the same way?

- Vector $$\begin{pmatrix}x\\y\end{pmatrix}=x\begin{pmatrix}1\\0\end{pmatrix}+y\begin{pmatrix}0\\1\end{pmatrix}$$
- After rotating: $$x\begin{pmatrix}1\\0\end{pmatrix}+y\begin{pmatrix}1\\1\end{pmatrix}=\begin{pmatrix}x\cdot1+y\cdot1\\x\cdot0+y\cdot1\end{pmatrix}$$

### Does this apply to more complex transformations?

- Coordinate system is being transformed so that $$\begin{pmatrix}1\\0\end{pmatrix}$$ goes to $$\begin{pmatrix}a\\b\end{pmatrix}$$ and $$\begin{pmatrix}0\\1\end{pmatrix}$$ goes to $$\begin{pmatrix}c\\d\end{pmatrix}$$
- Vector $$\begin{pmatrix}x\\y\end{pmatrix}=x\begin{pmatrix}1\\0\end{pmatrix}+y\begin{pmatrix}0\\1\end{pmatrix}$$ goes to $$x\begin{pmatrix}a\\b\end{pmatrix}+y\begin{pmatrix}c\\d\end{pmatrix}=\begin{pmatrix}ax+cy\\bx+dy\end{pmatrix}$$
- We describe such a transformation of the coordinate plane by the **matrix** $$\begin{pmatrix}a & c\\b & d\end{pmatrix}$$
- Vector $$\begin{pmatrix}x\\y\end{pmatrix}$$ transformed by the matrix above is denoted as the **matrix-vector multiplication** $$\begin{pmatrix}a & c\\b & d\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix}=\begin{pmatrix}ax+cy\\bx+dy\end{pmatrix}$$
	- \*2D rotation matrix: $$\begin{pmatrix}\cos\theta & \sin\theta\\-\sin\theta & \cos\theta\end{pmatrix}$$

## Can You Multiply a Vector by a Vector?

- A number can be thought of as a 1-dimensional vector
- Length is absolute value, direction can only be right or left
- When you multiply a 1D vector by itself, you get its length squared
- Should multiplying a 2D vector by itself also get its length squared?
- Then $$\begin{pmatrix}a\\b\end{pmatrix}\cdot\begin{pmatrix}a\\b\end{pmatrix}=a^2+b^2$$ (Pythagorean theorem)
- Intuitively, how about defining $$\begin{pmatrix}a\\b\end{pmatrix}\cdot\begin{pmatrix}c\\d\end{pmatrix}=ac+bd$$?

### Geometric meaning of this product

Consider this problem:

> Points $A$ and $B$ are on the first quadrant of the coordinate plane, both with distance 1 to the origin. Point $C$ is at $(1,0)$. $\angle AOC=30^\circ$ and $\angle BOC=45^\circ$. Find $\cos\angle AOB$.

![](/images/math-talk/linalg-geometry/difference-angle.svg){: width="100%"}

- Shift the coordinate plane so that every point gets projected perpendicularly to the line $AO$ and becomes a 1D vector

<video width="100%" height=auto controls>
	<source src="/images/math-talk/linalg-geometry/2d-coords-project-to-1d.mp4" type="video/mp4">
</video>

- Coordinate "grid" structure still preserved after transforming the 2D space to a 1D one, so $$\vec{OB}=\begin{pmatrix}\cos45^\circ\\\sin45^\circ\end{pmatrix}=\begin{pmatrix}\frac{\sqrt2}{2}\\\frac{\sqrt2}{2}\end{pmatrix}$$ transformed is still equal to $$\frac{\sqrt2}{2}\cdot\text{transformed }\begin{pmatrix}1\\0\end{pmatrix}+\frac{\sqrt2}{2}\cdot\text{transformed }\begin{pmatrix}0\\1\end{pmatrix}$$
- During the "squish" transformation, $$\begin{pmatrix}1\\0\end{pmatrix}$$ moves to $\cos30^\circ=\frac{\sqrt3}{2}$ on the line, and $$\begin{pmatrix}0\\1\end{pmatrix}$$ moves to $\sin30^\circ=\frac{1}{2}$
- Where $\vec{OB}$ ends up is $\cos\angle AOB$
- Thus $$\cos\angle AOB=\begin{pmatrix}\cos30^\circ & \sin30^\circ\end{pmatrix}\begin{pmatrix}\cos45^\circ\\\sin45^\circ\end{pmatrix}=\cos30^\circ\cdot\cos45^\circ+\sin30^\circ\cdot\sin45^\circ=\frac{\sqrt2+\sqrt6}{4}$$
- Notice that this multiplication of a 2D vector by a 2x1 matrix is also how we defined $$\vec{OA}\cdot\vec{OB}=\begin{pmatrix}\cos30^\circ\\\sin30^\circ\end{pmatrix}\cdot\begin{pmatrix}\cos45^\circ\\\sin45^\circ\end{pmatrix}$$
- Thus, when $\vert\vec{a}\vert=\vert\vec{b}\vert=1$, $\vec{a}\cdot\vec{b}=\vert\vec{a}\vert\vert\vec{b}\vert\cos\theta$, where $\theta$ is the angle between $\vec{a}$ and $\vec{b}$
- Also notice that $(k\vec{a})\cdot\vec{b}=k(\vec{a}\cdot\vec{b})$, so $\vec{a}\cdot\vec{b}=\vert\vec{a}\vert\vert\vec{b}\vert\cos\theta$ applies to all vectors, not just those of length 1

### Difference-angle and sum-angle formula of cosine

- Let $$\vec{a}=\begin{pmatrix}\cos\alpha\\\sin\alpha\end{pmatrix}$$, $$\vec{b}=\begin{pmatrix}\cos\beta\\\sin\beta\end{pmatrix}$$
- Since $\vec{a}$ and $\vec{b}$ both have length 1, geometrically, $\vec{a}\cdot\vec{b}=\cos(\alpha-\beta)$ (doesn't matter whether $\alpha$ or $\beta$ is larger since $\cos\theta=\cos(-\theta)$)
- Algebraically, the same expression equals $\cos\alpha\cos\beta+\sin\alpha\sin\beta$
- For the sum-angle formula, substitute $\beta$ for $-\gamma$, then $$\vec{b}=\begin{pmatrix}\cos\gamma\\-\sin\gamma\end{pmatrix}$$, and $\cos(\alpha-\gamma)=\vec{a}\cdot\vec{b}=\cos\alpha\cos\gamma-\sin\alpha\sin\gamma$

### Properties of vector dot product

- Commutative: $\vec{a}\cdot\vec{b}=\vec{b}\cdot\vec{a}$
- Distributive: $$\begin{pmatrix}x\\y\end{pmatrix}\cdot(\begin{pmatrix}a\\b\end{pmatrix}+\begin{pmatrix}c\\d\end{pmatrix})=x(a+c)+y(b+d)=(xa+yb)+(xc+yd)=\begin{pmatrix}x\\y\end{pmatrix}\cdot\begin{pmatrix}a\\b\end{pmatrix}+\begin{pmatrix}x\\y\end{pmatrix}\cdot\begin{pmatrix}c\\d\end{pmatrix}$$

### Law of cosine using vectors

- In triangle $ABC$, $\vec{BC}=\vec{AC}-\vec{AB}$
- $BC^2=\vec{BC}\cdot\vec{BC}=(\vec{AC}-\vec{AB})\cdot(\vec{AC}-\vec{AB})=\vec{AC}\cdot\vec{AC}+\vec{AB}\cdot\vec{AB}-2\cdot\vec{AC}\cdot\vec{AB}=AC^2+AB^2-2\cdot AC\cdot AB\cdot\cos\angle A$

## Vectors Are More Useful Than You Think: A Purely Algebraic Proof of Ptolemy's Theorem

![](https://mathworld.wolfram.com/images/eps-svg/PtolemysTheorem_1000.svg){: width="60%"}

- $AB\cdot CD+AD\cdot BC=AC\cdot BD$. Can you prove this using vectors?
- The 2 opposite angles of a cyclic quadrilateral adds up to $180^\circ$, can you describe that using vector dot product?
- $$\frac{\vec{AB}\cdot\vec{BC}}{AB\cdot BC}+\frac{\vec{CD}\cdot\vec{DA}}{CD\cdot DA}=0$$

[Manim source](/math-talks/vectors-manim-source)
