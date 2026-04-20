---
layout: default
title: "Determinants of Matrices: Continuous and Discrete Interpretations"
permalink: /math-talks/duality-determinants/
toc: true
---

# Determinants of Matrices: Continuous and Discrete Interpretations

## Definitions

### Matrix

- Matrix: rectangular array of numbers $a_{ij}$
  - Matrix usually written as capital ($A$), its elements as lowercase with subscripts ($a_{ij}$)
- Multiple use cases: [linear transformations](/math-talks/2d-vectors-and-geometry/), [evaluating choices](/math-talks/himcm-scoring-models/), [describing a graph](/math-talks/duality-determinants/), etc.

### Permutation

- A permutation $\tau$ of $n$ elements is a function that maps values from $\\\{1\leq x \leq n \mid x\in\mathbb{Z}\\\}$ to the same set
- Mappings of a permutation is bijective (one-to-one), or each integer between $1$ and $n$ is mapped to a distinct integer between $1$ and $n$ by $\tau$
- The set of all permutations of $n$ elements is the symmetric group $S_n$, which has $n!$ elements

#### Cycle notation

- Permutations can be described by how they "cycle" elements
- E.g. define permutation $\tau\in S_5$ as $\tau=(123)(45)$:
  - The first "cycle" says that $\tau(1)=2$, $\tau(2)=3$, $\tau(3)=1$
  - The second "cycle" says that $\tau(4)=5$, $\tau(5)=4$

#### Sign of a permutation

- $\mathrm{sgn}(\tau)$ is $+1$ if it contains a single cycle of odd length, and $-1$ if it contains a single cycle of even length
- If $\tau$ contains multiple cycles, then $\mathrm{sgn}(\tau)$ is the product of the sign of all its cycles
- \*A property of $\mathrm{sgn}$ is that swapping any 2 elements of $\tau$ multiplies its sign by $-1$
- Similar to "parity" (e.g. in Rubik's cube and other puzzle games)

### Determinant (行列式)

$$\det(A) = \sum_{\tau\in S_n}\mathrm{sgn}(\tau)\cdot\prod_{i=1}^na_{i\tau(i)}$$

#### Equivalent formulas

- For a 2D matrix: $$\begin{vmatrix}a & b \\ c & d\end{vmatrix} = ad - bc$$
- For 3D matrix: Add all `\` diagonal products, subtract all `/` diagonal products (diagonals warp)
  - For $$\begin{pmatrix}a & b & c \\ d & e & f \\ g & h & i\end{pmatrix}$$
    , `\` diagonals are $aei$, $cdh$, and $bfg$, `/` diagonals are $ceg$, $bdi$, and $afh$
- Higher dimensional matrices: calculate recursively
  - $$
        \begin{vmatrix}
            a & b & c & d\\
            e & f & g & h\\
            i & j & k & l\\
            m & n & o & p
        \end{vmatrix}=a\cdot\begin{vmatrix}
            f & g & h\\
            j & k & l\\
            n & o & p
        \end{vmatrix}-b\cdot\begin{vmatrix}
            e & g & h\\
            i & k & l\\
            m & o & p
        \end{vmatrix}+c\cdot\begin{vmatrix}
            e & f & h\\
            i & j & l\\
            m & n & p
        \end{vmatrix}-d\cdot\begin{vmatrix}
            e & f & g\\
            i & j & k\\
            m & n & o
        \end{vmatrix}
    $$

## The geometric view: area/volume/mass

- ![](./images/determinant-and-area.png)

## The discrete view: counting spanning trees of a graph (Kirchhoff's theorem)

- Definition of tree:
  - Connected: path between every pair of vertices in the graph
  - Acyclic: contains no cycles (no paths start and end at the same vertex without backtracking)
  - Equivalent definition: exactly 1 simple (non-backtracking) path exists between any 2 vertices

#### Euler's formula

- $V - E + F = 2$ for planar graphs (the "outside" face counts as one face)
- For trees: $F = 1$, so $V = E + 1$
- $V$ vertices, $V - 1$ arrows

- Intuitive plan: list all subgraphs with the correct number of edges, delete those with cycles

### Counting directed graphs (digraphs)

#### Avoiding undirected cycles

- Undirected cycles: $A \to B \to C$, $A \to D \to C$
- All undirected cycles have a vertex with $2$ arrows pointing at it
- Can counting these cycles be avoided by only counting cycles where all vertices have $0$ or $1$ arrows to it?

- \*_Given a tree and a root vertex, there exists exactly one directed tree, where there is exactly one directed path from the root vertex to any vertex_
  - Hint: vertices with smaller "distance" to the root should point toward vertices with larger "distance" to the root
- In a directed tree, the root has $0$ arrows to it, and all other vertices have $1$ arrow to it
  - Proof by contradiction: a vertex with $2$ arrows $\Rightarrow$ $2$ distinct paths from root to that vertex
- Choose any vertex on the graph, each spanning tree corresponds to exactly one digraph satisfying:
  1. One of the vertices have $0$ arrows pointing at it
  2. All other vertices have exactly $1$ arrow pointing at it
  3. No directed cycles

### Inclusion-exclusion principle

- Count all digraphs with one vertex with $0$ arrows and all other vertices with $1$ arrow
  - Pick $n-1$ of $n$ vertices, multiply their degrees
- For each directed cycle, subtract the number of such digraphs with that cycle
- For each pair of $2$ directed cycles, add back the number of such digraphs with these $2$ cycles
- For each pair of $3$ directed cycles, subtract the number of such digraphs with these $3$ cycles
- ...
- General form: odd number of cycles are subtracted, even number of cycles are added
- E.g. to count all graphs satisfying 1 and 2 and containing the cycle $(1\ 3)$ in a $5$-vertex graph, calculate $\deg(v_2)\cdot\deg(v_4)\cdot\deg(v_5)\cdot\mathrm{adj}(v_1,v_3)\cdot\mathrm{adj}(v_3,v_1)$
  - $\deg$ is degree of vertex, $\mathrm{adj}(x,y)$ is whether there is a (directed) arrow connecting from vertex $x$ to $y$
- How can we ensure that each count is added or subtracted correctly?

### Laplacian matrix

- $a_{xx}$: how many edges are connected to vertex $x$ (or $\deg(v_x)$)
- $a_{xy}\ (x\neq y)$: whether vertex $x$ is directly connected to vertex $y$. $-1$ if true, $0$ if false (or $-\mathrm{adj}(v_x,v_y)$)

## Summary: what is the determinant

- A function that maps a matrix to a single number that "captures" all its intrinsic properties
- The properties of a matrix doesn't change from permuting rows and columns by the same way, so the function's result shouldn't change either
  - Probably something that sums over permutations
- It's intuitive for an $n\times n$ matrix's determinant to be of degree $n$
  - $\sum_{\tau\in S_n}\prod a_{i\tau(i)}$ (permanent (积和式) of matrix)
- Swapping 2 rows or 2 columns (not both) of the matrix "multiplies the matrix by $-1$"
  - Use the sign/parity of permutations as weight of each term in the sum
  - Try $\det(A) = \sum_{\tau\in S_n}\mathrm{sgn}(\tau)\cdot\prod_{i=1}^na_{i\tau(i)}$ which is the determinant

### Exercise: use the "meta" properties of the determinant to prove that it calculates the volume of higher-dimensional parallelepipeds

- Hint: use the identity matrix as the base case (its determinant is $1$), then show that:
  - Scaling one of the columns scales the determinant by the same factor
  - Sheering (adding a multiple of one column to another column) preserves determinant (and also area)
    - Further hint: show that $\det(\dots,u+v,\dots)=\det(\dots,u,\dots)+\det(\dots,v,\dots)$ and $\det(\dots,v,\dots,v,\dots)=0$
  - Swapping 2 columns multiplies the determinant by $-1$
