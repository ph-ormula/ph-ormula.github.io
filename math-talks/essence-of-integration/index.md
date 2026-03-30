---
layout: default
title: The Essence of Integration
permalink: /math-talks/essence-of-integration/
toc: true
---

# The Essence of Integration

## Geometric Essence of Integration

- **Core Goal:** Finding the area under a function curve.
- For a continuous function $y=f(x)$ on $[a, b]$, the integral represents the area of the **curvilinear trapezoid** enclosed by the curve, the x-axis, and the lines $x=a$ and $x=b$.
- **Approximation:** Irregular shapes are approximated by simple regular shapes (rectangles).
- **Infinite Subdivision:** Error is eliminated by breaking the area into an infinite number of infinitely small narrow rectangles.
	- Width $\Delta x$ approaches $dx$ as $n \to \infty$.
	- Height is taken as $f(x)$ at any point in the interval.
	- Area of a single block: $dS = f(x) \cdot dx$.

## Origin of the Integral Symbol

- **Sigma ($\sum$):** Used for finite, discrete summation.
- **Integral ($\int$):** A "stretched sigma" used for infinite summation of continuous quantities.
- **Notation:** $S = \int_a^b f(x) dx$
	- $\int$: Integral symbol (infinite summation).
	- $a, b$: Limits of integration (range of summation).
	- $f(x)$: Integrand (height of rectangles).
	- $dx$: Integration variable (infinitesimal base).

## Integrals vs. Geometric Areas

- **Integrals $\neq$ Geometric Area.**
- Integrals are **signed cumulative sums**.
- Function values below the x-axis ($f(x) < 0$) result in negative area elements, which can "cancel out" positive values.
- **Physical Example: $v-t$ (Velocity-Time) Graph**
	- **Displacement:** The integral $\int_{t_1}^{t_2} v(t) dt$. Reflects the net change in position (can be zero).
	- **Distance:** The total geometric area (sum of absolute values). Reflects the actual path length.

## Underlying Essence of Derivatives

- **Origin of $dy/dx$:** The limit of the incremental ratio $\frac{\Delta y}{\Delta x}$ as $\Delta x \to 0$.
- **Geometric Meaning:** The slope of the tangent line.
- **Independence of Differentials:** $dy$ and $dx$ are independent infinitesimals.
	- They can be separated and treated like numbers: $dy = f'(x) dx$.
	- **Inversion:** $dx/dy$ represents the slope of the **normal** to the curve.
	- Reciprocal relationship: $k_{tangent} \cdot k_{normal} = \frac{dy}{dx} \cdot \frac{dx}{dy} = 1$.

## Second Derivative and Concavity

- **Definition:** The rate of change of the derivative (slope).
- **Geometric Interpretation:**
	- $f''(x) > 0$: Slope is increasing $\implies$ Curve is **concave upward**.
	- $f''(x) < 0$: Slope is decreasing $\implies$ Curve is **concave downward**.
- **Notation:** $\frac{d^2y}{dx^2}$ indicates $y$ is differentiated twice, with $dx$ acting as an independent infinitesimal base.

## Taylor Expansion and Integration Methods

- **Taylor's Significance:** Breaking down complex functions into polynomials to use familiar tools.
- **Maclaurin Series:** Taylor expansion centered at $a=0$.
- **Integrating Differentials:** "Hiding" functions after the differential $d$ (substitution).
	- Example: $\int \sin^3 x \cdot \cos x dx = \int \sin^3 x d(\sin x)$.
	- Substituting $\Delta = \sin x$: $\int \Delta^3 d\Delta = \frac{1}{4}\Delta^4 + C = \frac{1}{4}\sin^4 x + C$.

## Verification of L'Hôpital's Rule

- L'Hôpital's rule for $0/0$ forms can be verified using Maclaurin expansions.
- Example: $\lim_{x \to 0} \frac{\sin x}{x}$
	- $\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \dots$
	- $\frac{\sin x}{x} = 1 - \frac{x^2}{3!} + \frac{x^4}{5!} - \dots$
	- As $x \to 0$, the higher-order terms vanish, leaving the limit as $1$.
