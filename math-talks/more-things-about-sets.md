---
layout: default
title: More Things About Sets
permalink: /math-talks/more-things-about-sets/
---

# More Things About Sets

## Sets

### Definition

A set is a **well-defined** collection of **distinct objects**, considered as an object in its own right.

**well-defined**: no ambiguity

**distinct**: no repetition

**objects**: often referred as element or members of a set

Q1: Is “the set of tall people" by definition a set?

### Common Notations

USE UPPERCASE LETTERS TO DENOTE A SET

use lowercase letters to denote an element

*$a\in A$, belongs to

$b\notin A$, doesn't belong to

$A\subseteq S$, $A$ is a subset of $S$

$S\supseteq A$, $S$ is a superset of $A$

$A\subset S$, $A$ is a proper subset of $S$

$S\supset A$, $S$ is a proper superset of $A$

$A\cup B$ is the **union** of sets $A$ and $B$

$A\cap B$ is the **intersection** of sets $A$ and $B$

*$\mid$ stands for "such that", e.g. $A=\lbrace x\mid x^2=2\rbrace=\lbrace - \sqrt 2,\ \sqrt2\rbrace$

## Ordered Sets

Sets + any **order** that you may define linked with <, satisfying:

1. if $x\in S, y\in S$ then only one of following holds:
   $x<y;\ x=y;\ x>y$

2. if $x,\ y,\ z\in S$, if $x<y$ and $y<z$, then $x<z$

Q2: is "the set of a random triangle, a rhombus, a random pentagon" an ordered set?

We will be mainly focusing on the set with numbers.    

### Order in $\mathbb{Q}$

The order is defined: for $x=\frac{a}{b},\ y=\frac{c}{d}$:

$x<y$ if $ad<bc$

or, the definition can be:

$x<y$ if $y-x$ is a positive rational number

## Supremum & Infimum

### Supremum

an **upper bound** $\alpha$ of an ordered set $S$ satisfies for any $\beta\in S$, we have $\alpha\ge\beta$

We say $\alpha$ is the **supremum** if:

1) $\alpha$ is an upper bound

2) if $\gamma<\alpha$, then $\gamma$ isn't an upper bound

The supremum of an ordered set $S$ is denoted as $\sup S$

### Infimum

a **lower bound** $\alpha$ of an ordered set $S$ satisfies for any $\beta\in S$, we have $\alpha\le\beta$

We say $\alpha$ is the **infimum** of $S$ if:

1. $\alpha$ is a lower bound

2. if $\gamma>\alpha$, then $\gamma$ isn't a lower bound

The infimum of an ordered set $S$ is denoted as $\inf S$

### Question

Q3: Are $\sup S$ and $\inf S$, if they exist, necessarily in $S$?

A3: No.

We shall show that $x=m$ is the supremum of the sets: $S=\lbrace x\mid x<m\rbrace$ and $T=\lbrace x\mid x\le m\rbrace$.

To show this, we use the definition, two things need to be satisfied:

Firstly, prove that $x=m$ is upper bound, simply by definition.

Secondly, prove for any number smaller than $x=m$, it's not an upper bound

Let's assume if there is such number $\gamma<m$ that is an upper bound of the sets. 

$\gamma+\gamma<\gamma+m<m+m$

$\gamma<\frac{\gamma+m}{2}<m$

Contradictory arise, so there does NOT exist any number under $m$ that is an upper  bound. Thus $x=m$ is the supremum.

## Archimedean property of $\mathbb{R}$

### Theorem

If $x\in \mathbb{R},\ y\in \mathbb{R}$ and $x>0$, then there is a positive integer $n$ such that:

$nx>y$

### Proof

Hint: let $A=\lbrace nx\mid n\in \mathbb{N}^+\rbrace$ and start by assuming that the theorem was false, thus $y$  would be an upper bound, and we put $\alpha=\sup\ A$, this will eventually lead to contradictory.

Since $x>0$, we have $\alpha-x<\alpha$. Since $\alpha$ is the supremum, $\alpha-x$ can't be an upper bound, thus $\alpha-x<mx$ for some positive integer $x$. However, this means $\alpha<(m+1)x$, and the right hand side is in set $A$, so $\alpha$ is not the supremum. Here's when contradiction arises.

## $\mathbb{Q}$ is dense in $\mathbb{R}$

### Theorem

If $x\in \mathbb{R}$, $y\in \mathbb{R}$, and $x<y$ then there exists a $p\in\mathbb{Q}$ such that $x<p<y$.

### Proof

Since $x<y$, $y-x>0$. Apply Archimedean property, we obtain $n(y-x)>1$, $1+nx<ny$.

There must exist a positive integer such that $m-1\le nx<m$, this formula here will break into two parts:

$m\le 1+nx$ and $nx<m$, combining the inequalities: $nx<m\le1+nx<ny$

Thus $x<\frac mn<y$, since $m$ and $n$ are all integers, $p=\frac mn\in \mathbb{Q}$.

### Corollary 1

There are infinite rational numbers in any interval in $\mathbb{R}$.

Hint: prove that the density theorem above can be applied multiple times.

### Corollary 2

$\mathbb{R}\backslash{\mathbb{Q}}$ is dense in $\mathbb{R}$.

Hint: prove that there is always a costructable irrational number $r$ that satisfies $x<r<y$ given $x,\ y\in \mathbb{R}$.

Hint: let $m$ be an irrational number, then $\frac mn$ with positive number $n$, is irrational. Then the inequality $x<p+\frac mn<y$ with $p$ being a rational number may become true under some specific conditions.

![](/easter-eggs/Jibba.png){: width="30%"}
