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
  - _Example:_ A soccer ball kicked vertically first rises ($v > 0$) then falls ($v < 0$). The integral over the whole trip is 0 (net displacement), while the total area is the actual path length (total distance).

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
  - $f^{\prime\prime}(x) > 0$: Slope is increasing $\implies$ Curve is **concave upward**.
  - $f^{\prime\prime}(x) < 0$: Slope is decreasing $\implies$ Curve is **concave downward**.
- **Notation Breakdown:** In the official notation $\frac{d^2y}{dx^2}$:
  - **Molecule ($d^2y$):** Indicates $y$ is differentiated twice. The first $d$ is the derivative sign, and the second corresponds to the differential $dy$.
  - **Denominator ($dx^2$):** Represents $(dx)^2$, meaning $x$ is differentiated twice with respect to the infinitesimal $dx$. It is NOT a squaring operation of $x$.

## Application: Badminton Shuttlecock Trajectory

- **Problem:** A shuttlecock is thrown at an angle of $60^\circ$ with initial velocity $u$. If the tangents to the trajectory at $t=5$ and $t=15$ are perpendicular, find $u$.
- **Decomposition:**
  - $x(t) = \frac{1}{2}ut$ (Horizontal, uniform velocity).
  - $y(t) = \frac{\sqrt{3}}{2}ut - 5t^2$ (Vertical, uniform acceleration with $g=10$).
- **Parametric Differentiation:**
  - $dx/dt = \frac{1}{2}u$
  - $dy/dt = \frac{\sqrt{3}}{2}u - 10t$
  - $\frac{dy}{dx} = \frac{dy/dt}{dx/dt} = \frac{\frac{\sqrt{3}}{2}u - 10t}{\frac{1}{2}u}$
- **Perpendicularity Condition:** The product of slopes at $t=5$ and $t=15$ is $-1$.
  - $k_5 = \frac{\frac{\sqrt{3}}{2}u - 50}{\frac{1}{2}u}$
  - $k_{15} = \frac{\frac{\sqrt{3}}{2}u - 150}{\frac{1}{2}u}$
  - $(\frac{\sqrt{3}}{2}u - 50) \cdot (\frac{\sqrt{3}}{2}u - 150) = -(\frac{1}{2}u)^2$
- Solving this equation allows finding the initial velocity $u$.

## Taylor Expansion and Integration Methods

- **Taylor's Significance:** Breaking down complex functions into polynomials to use familiar tools.
- **Maclaurin Series:** Taylor expansion centered at $a=0$.
- **"Guessing" $\ln(1-x)$ via Integration:**
  - We know the geometric series: $1 + x + x^2 + x^3 + \dots = \frac{1}{1-x}$.
  - Since the derivative of $\ln(x)$ is $1/x$, the integral of $1/(1-x)$ should be related to $\ln(1-x)$.
  - **Chain Rule Correction:** Integrating term-by-term on the left and using the chain rule on the right, we find $\int \frac{1}{1-x} dx = -\ln(1-x)$.
  - Thus, $-\ln(1-x) = x + \frac{x^2}{2} + \frac{x^3}{3} + \dots$
- **Integrating Differentials:** "Hiding" functions after the differential $d$ (substitution).
  - Example: $\int \sin^3 x \cdot \cos x dx = \int \sin^3 x d(\sin x)$.
  - Substituting $\Delta = \sin x$: $\int \Delta^3 d\Delta = \frac{1}{4}\Delta^4 + C = \frac{1}{4}\sin^4 x + C$.

## Verification of L'Hôpital's Rule

- L'Hôpital's rule for $0/0$ forms can be verified using Maclaurin expansions.
- **Example:** $\lim_{x \to 0} \frac{\sin x}{x}$
  - Periodicity of derivatives for $\sin x$: $1, 0, -1, 0, \dots$ at $x=0$.
  - $\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \dots$
  - Substituting into the limit: $\frac{x - \frac{x^3}{3!} + \dots}{x} = 1 - \frac{x^2}{3!} + \dots$
  - As $x \to 0$, the higher-order infinitesimal terms approach 0, confirming the limit is $1$.
