---
layout: default
title: Introduction to Group Theory and Important Theorems
permalink: /math-talks/intro-to-group-theory/
toc: true
---

# Introduction to Group Theory and Important Theorems

## Introductory Problem

1. If today is Sunday, what day of the week will it be in $2^{100}$ days?
2. How many rotationally distinct subsets of the "frame" of the regular octagon are there?

## Definition of Group

- A group is defined by a set $S$, operation $\cdot$, and identity $e\in G$ (optional)
- Closure: $x\cdot y\in G\ \forall x,y\in G$
- Associativity: $x\cdot (y\cdot z)=(x\cdot y)\cdot z\ \forall x,y,z\in G$
	- Conventionally $x\cdot y$ is "$x$ then $y$", so $x\cdot y\cdot z$ means $x\cdot(y\cdot z)$
- Identity: $x\cdot e=e\cdot x\ \forall x\in G$
- Inverse: $\forall x\in G\ \exists x^{-1}\in G\ x\cdot x^{-1}=x^{-1}\cdot x=e$

## Intuitive Understanding and Examples

- Symmetries of object
- Polygons without flipping is equivalent to modular arithmetic
- Dihedral groups: symmetries of polygons including flipping
	- Notice the $\cdot$ operation in group doesn't need to be commutative ($x\cdot y\neq y\cdot x$)
- Symmetries of polyhedrons
- $\mathbb{Z}$, $\mathbb{R}$, $\mathbb{C}$: translational symmetry

## Visualization: cayley diagrams

- ![](https://www.log24.com/log/pix10/100301-Cayley.jpg){: width="60%"}

## Subgroups

- Subset that's also a group
- Notation: subgroup $H\subset G$
- Example: $D_3$ group

### Cosets (陪集)

- Define left coset $gH=\{gh:h\in H\}$ $\forall g\in G$
	- Right cosets: $Hg=\{hg:h\in H\}$
- Size of cosets are equal to $|H|$
	- $gh=gh' \iff h = h'$, proven before

#### Lemma: cosets partition group into equal-sized pieces

- What algebraic manipulations can be done in group theory proofs?
	- "Multiply" the same terms on both sides of the equation
		- Need to multiply both on left or both on right
	- Can't divide by terms, but can "multiply" by inverse (if the element being taken inverse is in a group)
		- E.g. $g_1g_3=g_2g_3\iff g_1g_3g_3^{-1}=g_2g_3g_3^{-1}\iff g_1e=g_2e\iff g_1=g_2$
	- Can't swap terms, but can start evaluating results from anywhere in a large "product"
		- E.g. $g_1(g_2(g_2^{-1}g_3))=g_1((g_2g_2^{-1})g_3)=g_1(eg_3)=g_1g_3$
- $\forall g_1,g_2\in G$, either $g_1H=g_2H$ or $g_1H\cap g_2H=\varnothing$
	- If $g_1H\cap g_2H\neq\varnothing$, then there exists $h_1$, $h_2$ so that $g_1h_1=g_2h_2$. Need to prove that for all $h\in H$ there exists $h'\in H$ so that $g_1h=g_2h'$
	- $g_1h_1 = g_2h_2 \Rightarrow g_1h_1h_1^{-1}h = g_2h_2h_1^{-1}h \Rightarrow g_1h=g_2h_2h_1^{-1}h \Rightarrow$ the $h'$ we need to find is $h_2h_1^{-1}h$ which is in $H$ by closure and inverse properties
- $\forall g\in G\ \exists g'\ g\in g'H$: obvious, let $g'=g$

### Lagrange's Theorem: Order of Subgroup Divides Order of Group

- All possible distinct $gH$ of size $|H|$ "tiles" $G$
- $|H|$ divides $|G|$

### Fermat's Little Theorem and Euler's Totient Theorem

- If a group has a prime number order $p$, then it has no subgroups and can only be group $C_p$
- Define group $(\mathbb{Z}/p\mathbb{Z})^\times=\{n\mid 1\leq n\leq p-1\}$
	- Operation is multiplication modulo $p$
	- Identity is 1
	- Closure is obvious
	- Inverses exist because of Bézout's theorem (inverse Euclid's algorithm)
- Fermat's Little Theorem: $a^p\equiv a\pmod p$ if $p$ is prime

#### Solving problem 1

## Group Actions

### Orbits

### Burnside's Lemma

- Important proof technique (in and outside group theory): double counting
- Given pairs $(g\in G, s\in S)$, how can the size of $S$ be expressed?
- $\sum_{g\in G}|\{s\in S\mid gs=s\}| = \sum_{s\in S}|\{g\in G\mid gs=s\}|$
- $G_s=\frac{G}{|\mathrm{orb}(s)|}$

#### Solving problem 2

- Identity: 1 element
	- All subsets of edges are fixed points of this element, giving a total of $2^{12} = 4096$ fixed points
- Rotation along the center of a face: 4 axes ($\frac{8\text{ faces}}{2}$), 2 rotations for each axis, 8 elements
	- 4 sets of edges, 3 each, must be either all chosen or all not chosen, a total of $2^{4} = 16$ fixed points
- Rotation along the midpoint of an edge: 6 axes, 1 rotation for each axis, 6 elements
	- The 2 edges on the axis of rotation can be chosen or not chosen independently, the other 10 edges are in 5 pairs, each pair must be chosen or not chosen together, giving a total of $2^{7} = 128$ fixed points
- Rotation along a vertex: 3 axes, 3 rotations for each axis, 9 elements
	- 3 sets of edges, 4 each, must be all chosen or all not chosen, giving a total of $2^{3} = 8$ fixed points
- And by Burnside's lemma, the total number of orbits is
$$|\text{orb}_{G}| = \frac{1}{|G|} \cdot \sum_{g \in G}|\text{fix}(g)| = \frac{1}{24} \cdot (4096 + 8 \cdot 16 + 6 \cdot 128 + 9 \cdot 8) = (211)$$
