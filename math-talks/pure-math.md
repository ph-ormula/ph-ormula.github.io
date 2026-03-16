---
layout: default
title: "Pure Math (Sequel)"
permalink: /math-talks/pure-math/
toc: true
---

# Pure Math (Sequel)

## Euclidean Space

**Definition:**

$\mathbb{R}^n=\{(x_1, x_2,...,x_n)\mid x_i\in\mathbb{R}\text{ for }i=1,2,...,n\}$

Basically a set of all n-tuples of real numbers, or set of points

**Point:**

A point $x$ in $\mathbb{R}^n$ can be denoted as $x=(x_1,x_2,...,x_n)$

$∥x∥$ is the distance from this point to the origin

**Examples:**

In $\mathbb{R}$: $x=5$

In $\mathbb{R}^2$: $x=(2,3)$

In $\mathbb{R}^3$: $x=(3,4,-2)$

$∥(3,4)∥=5$

## Metric

**Definition:**

A metric $d:X\times X→\mathbb{R}$ satisfies:

1. $d(x,y)≥0$

2. $d(x,y)=0⟺x=y$

3. $d(x,y)=d(y,x)$

4. $d(x,z)≤d(x,y)+d(y,z)$

**Notations:**

$d$ is the letter generally used to represent metric

$X$ is a set

$X\times X$ is the Cartesian product of $X$ and itself, defined as

$A\times B=\{(a,b)\mid a\in A\text{ and }b\in B\}$

$\to$ means mapping

$\mathbb{R}$ is the set of real numbers

The metric function $d$ takes two point in the same set $X$ and returns a real number.

**Example:**

Metric in $$\mathbb{R}^2$$

: $$d(x,y)=\sqrt{(x_1-x_2)^2+(y_1-y_2)^2}$$

## Sequence

**Definition:**

A sequence in $\mathbb{R}^n$ is a function $x:\mathbb{N}\to\mathbb{R}^n$, written as $(x_k​)_{k≥1}​$.

Basically an ordered list of points that goes on forever.

**Examples:**

In $\mathbb{R}$: $x_k=k^2=1，4，9，16...$

In $\mathbb{R}^2$: $x_k=(\frac k2,k-1)=(0.5,0),(1,1),(1.5,2)...$

## Convergence

**Definition:**

A sequence $(x_k​)$ converges to $x∈\mathbb{R}^n$ if:

$\forall\varepsilon>0,\exists N\in\mathbb{N}\text{ s.t. }k>N⟹d(x_k​,x)<\varepsilon$

A sequence converges if its points eventually get and stay very close to a fixed point, no matter how small a distance you pick.

**Examples:**

$x_k​=\frac1k\to0$

$x_k=k^2$ does not converge

## Bounded

**Definition:**

A sequence $(x_k​)$ is bounded if $\exists M>0$ such that $∥x_k​∥\le M$ for all $k$

A sequence is bounded if all its points stay inside some “big enough ball”

**Example:**

$x_k={(-1)}^k$ is bounded because $∥x_k​∥\le1$ for all $k$

## Cauchy

**Definition:**

A sequence $(x_k​)$ is Cauchy if:

$\forall\varepsilon>0,\exists N\in N\text{ s.t. }k,m>N⟹d(x_k​,x_m​)<\varepsilon$

A sequence is Cauchy if the points get arbitrarily close to each other as the sequence progresses, even if we don’t know the limit yet.

**Example:**

$x_k=\frac1k$ is Cauchy because for large enough $k,m$, $\vert\frac1k−\frac1m\vert$ can be made as small as desired.

## Complete

**Definition:**

A metric space $(\mathbb{R}^n,d)$ is complete if all Cauchy sequence converges to a point in $\mathbb{R}^n$.

**Examples:**

$\mathbb{R}^n$ (see proof below)

$\mathbb{H}^n$ (hyperbolic space)

$\mathbb{H}^2$:

Poincaré disk ($\mathbb{D}=\{(x,y)\in\mathbb{R}^2:x^2+y^2<1\}$, $ds^2=\frac{4(dx^2+dy^2)}{(1-x^2-y^2)^2}$) Upper half-plane model ($\mathbb{H}=\{z=x+iy\in C:y>0\}$), $ds^2=\frac{dx^2+dy^2}{y^2}$） Hyperboloid ($\mathbb{H}^2=\{(X,Y,T)\in\mathbb{R}^{2,1}:-T^2+X^2+Y^2=-1,T>0\}$)

$\mathbb{R}^{n,1}$ (Minkowski space: geodesically complete, metric is non-Riemann)

$L^p(\Omega),1\le p\le \infty$ (Lebesgue)

$\mathcal{H}$ (Hilbert space)    

$B$ (Banach space)

$W^{k,p}(\Omega)$ (Sobolev space)

$F$ (Fréchet space)

$\mathcal{F}$ (Fock space)

$Gr(k,n)$ (Grassmannian)

$\mathcal{T}_g$ (Teichmüller space)

**Counterexamples:**

$\mathbb{Q}$ (missing irrational numbers)

open subset $U\subseteq\mathbb{R}^n$ (missing limit points)

$\mathcal{M}_g$ (Moduli space)

## Proving Completeness of $\mathbb{R}^n$

**Note:**

This proof is based on the fact that $\mathbb{R}$ is complete, this property is innate due to the way $\mathbb{R}$ is constructed from $\mathbb{Q}$, the set of rational numbers.

The construction is centered around two methods: Dedekind Cut and Cauchy sequence.

The idea of Dedekind cut is to cut $\mathbb{Q}$ at an irrational point so that the supremum of one set is the irration number.

The idea of Cauchy sequence is to approach the irrational number by an endless sequence.

Both of these guarantee that $\mathbb{R}$ is complete.

**Proof:**

Let $(x_k​)$ be a Cauchy sequence in $\mathbb{R}^n$.

Write $x_k​=(x_k^1​,x_k^2​,…,x_k^n​)$, where $x_k^i$​ is the $i$-th coordinate of the $k$-th point.

$\forall\varepsilon>0,\exists N\in N\text{ s.t. }k,m>N⟹d(x_k​,x_m​)<\varepsilon$

$d(x_k,x_m)=∥x_k-x_m∥=\sqrt{\sum_{i=1}^n{(x_k^i-x_m^i)}^2}<\varepsilon$

Thus, each coordinate sequence $(x_k^i​)$ is a Cauchy sequence in $\mathbb{R}$.

By completeness of $\mathbb{R}$, the sequence of coordinates converges:

$x_k^i\to x^i\text{ for each }i=1,2,...,n$

Thus, $\forall\varepsilon>0$, $\exists N_i \text{ s.t. } \forall k>N_i:\ \vert x_k^i-x^i\vert<\frac{\varepsilon}{\sqrt{n}}$

Let $N=\max(N_1,N_2,...,N_n)$

Define: $x=(x^1,x^2,...,x^n)\in\mathbb{R}^n$

$\forall k>N$:

$∥x_k-x∥=\sqrt{\sum_{i=1}^n{(x_k^i-x^i)}^2}\le\sqrt{\sum_{i=1}^n{(\frac{\varepsilon}{\sqrt{n}})}^2}=\sqrt{n\cdot\frac{\varepsilon^2}n}=\varepsilon$

This shows $∥x_k-x∥<\varepsilon$ for all large $k$. Hence $x_k\to x$, and we can find a limit for all the Cauchy sequences in $\mathbb{R}^n$.
