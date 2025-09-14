---
layout: default
title: Trigonometry and Geometry Through 2-Dimensional Vectors
permalink: /math-talks/2d-vectors-and-geometry/
---

# Introduction to 2-Dimensional Vectors and Matrices and Results in Geometry and Trigonometry

## Putting 2-Dimensional Vectors in the Coordinate Plane

### Review of Vectors

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

### How to Describe Vectors in the Coordinate Plane?

- Vector starting on origin $(0, 0)$ and ending on $(a,b)$: denote as vector $$\begin{pmatrix}a\\b\end{pmatrix}$$
- Represents $a$ unit to the right and $b$ unit upwards

![](https://wumbo.net/glossary/vector/figures/VectorExample-480-270.dark.svg){: width="60%"}

- $$\begin{pmatrix}a\\b\end{pmatrix}+\begin{pmatrix}c\\d\end{pmatrix}=\begin{pmatrix}a+c\\b+d\end{pmatrix}$$, $$n\begin{pmatrix}a\\b\end{pmatrix}=\begin{pmatrix}na\\nb\end{pmatrix}$$ (obvious and intuitive)

## Transforming Vectors: Matrices

Consider this problem:

> On the 2D coordinate system with origin $O$, point $A$ lies on $(3, 4)$. Segment $AO$ is rotated counterclockwise around $O$ by $45^\circ$, and point $A$ ends up at point $B$. Find the coordinates of point $B$.

Problem restated as vectors: **what vector does $$\begin{pmatrix}3\\4\end{pmatrix}$$ become when rotated by $45^\circ$ counterclockwise?**

- Instead of rotating the vectors, **rotate the entire coordinate system**
- Notice that vector $$\begin{pmatrix}3\\4\end{pmatrix}$$ represents $$3\begin{pmatrix}1\\0\end{pmatrix}+4\begin{pmatrix}0\\1\end{pmatrix}$$
- When transformed, $$\begin{pmatrix}3\\4\end{pmatrix}$$ should still be equivalent to 3 times the transformed $$\begin{pmatrix}1\\0\end{pmatrix}$$ plus 4 times the transformed $$\begin{pmatrix}0\\1\end{pmatrix}$$
- After rotating, $$\begin{pmatrix}1\\0\end{pmatrix}$$ becomes $$\begin{pmatrix}\frac{\sqrt2}{2}\\\frac{\sqrt2}{2}\end{pmatrix}$$ and $$\begin{pmatrix}0\\1\end{pmatrix}$$ becomes $$\begin{pmatrix}-\frac{\sqrt2}{2}\\\frac{\sqrt2}{2}\end{pmatrix}$$
- Thus $$\begin{pmatrix}3\\4\end{pmatrix}$$ transformed is $$3\begin{pmatrix}\frac{\sqrt2}{2}\\\frac{\sqrt{2}}{2}\end{pmatrix}+4\begin{pmatrix}-\frac{\sqrt2}{2}\\\frac{\sqrt2}{2}\end{pmatrix}=\begin{pmatrix}-\frac{\sqrt2}{2}\\\frac{7\sqrt2}{2}\end{pmatrix}$$

### What about when vector $$\begin{pmatrix}x\\y\end{pmatrix}$$ is rotated the same way?

- Vector $$\begin{pmatrix}x\\y\end{pmatrix}=x\begin{pmatrix}1\\0\end{pmatrix}+y\begin{pmatrix}0\\1\end{pmatrix}$$
- After rotating: $$x\begin{pmatrix}\frac{\sqrt2}{2}\\\frac{\sqrt{2}}{2}\end{pmatrix}+y\begin{pmatrix}-\frac{\sqrt2}{2}\\\frac{\sqrt2}{2}\end{pmatrix}=\begin{pmatrix}x\cdot \frac{\sqrt2}{2}+y\cdot-\frac{\sqrt2}{2}\\x\cdot\frac{\sqrt2}{2}+y\cdot\frac{\sqrt2}{2}\end{pmatrix}$$

### Does this apply outside of rotations?

- Coordinate system is being transformed so that $$\begin{pmatrix}1\\0\end{pmatrix}$$ goes to $$\begin{pmatrix}a\\b\end{pmatrix}$$ and $$\begin{pmatrix}0\\1\end{pmatrix}$$ goes to $$\begin{pmatrix}c\\d\end{pmatrix}$$
- Vector $$\begin{pmatrix}x\\y\end{pmatrix}=x\begin{pmatrix}1\\0\end{pmatrix}+y\begin{pmatrix}0\\1\end{pmatrix}$$ goes to $$x\begin{pmatrix}a\\b\end{pmatrix}+y\begin{pmatrix}c\\d\end{pmatrix}=\begin{pmatrix}ax+cy\\bx+dy\end{pmatrix}$$
- We describe such a transformation of the coordinate plane by the **matrix** $$\begin{pmatrix}a & c\\b & d\end{pmatrix}$$
- Vector $$\begin{pmatrix}x\\y\end{pmatrix}$$ transformed by the matrix above is denoted as the **matrix-vector multiplication** $$\begin{pmatrix}a & c\\b & d\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix}=\begin{pmatrix}ax+cy\\bx+dy\end{pmatrix}$$
	- \*2D rotation matrix: $$\begin{pmatrix}\cos\theta & \sin\theta\\-\sin\theta & \cos\theta\end{pmatrix}$$

## Can you multiply a vector by a vector?

- A number can be thought of as a 1-dimensional vector
- Length is absolute value, direction can only be right or left
- When you multiply a 1D vector by itself, you get its length

## Basic Trigonometry: Overview

- Unit circle
- Radian
- Angle between $0$ and $2\pi$ corresponds to a point on unit circle
- Sine: signed height of the point
- Cosine: signed position of "shadow" of the point

## 2-Dimensional Matrices: Brief Overview

## Dot Product

### Connection to matrix multiplication

### Distributive law

## Applications

### Law of cosine

### Sum/difference angle formulas for cosine

### Ptolemy's theorem
