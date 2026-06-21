# 02 Classification — PYQ

Source: GATE DA Previous Year Questions

---

## Q5036

[MCQ]
[PYQ: GATE DA 2026]

Consider a linear regression model with L2 regularization (Ridge Regression). Which of the following statements is correct about the effect of the regularization parameter $\lambda$?
- **(A)** Increasing $\lambda$ decreases bias and increases variance
  
- **(B)** Increasing $\lambda$ decreases both bias and variance
  
- **(C)** Increasing $\lambda$ increases both bias and variance
  
- **(D)** Increasing $\lambda$ increases bias and decreases variance

**Answer:** D

---

## Q5037

[NAT]
[PYQ: GATE DA 2026]

Consider the model $\hat{y} = w_1 x_1 + w_2 x_2$ with weights $\mathbf{w} = (w_1, w_2) = (1, 2)$ and regularization parameter $\lambda = 0.5$. The training data and predictions are:

| $x_1$ | $x_2$ | $y$ | $\hat{y} = w_1 x_1 + w_2 x_2$ |
| --- | --- | --- | --- |
| 1 | 1 | 2 | 3 |
| 2 | 1 | 3 | 4 |
| 1 | 2 | 4 | 5 |

Compute the ridge loss $L = \sum_{i=1}^{n} |y_i - \hat{y}_i| + \lambda(w_1^2 + w_2^2)$ (rounded to 1 decimal place).

**Answer:** 5.5

---

## Q5038

[NAT]
[PYQ: GATE DA 2024]

Let $f: \mathbb{R} \to \mathbb{R}$ be the function $f(x) = \dfrac{1}{1 + e^{-x}}$.

The value of the derivative of $f$ at $x$ where $f(x) = 0.4$ is \_\_\_\_\_\_\_\_ (rounded off to two decimal places).

*Note:* $\mathbb{R}$ denotes the set of real numbers.

**Answer:** 0.24

---

## Q5039

[MCQ]
[PYQ: GATE DA 2024]

Match the items in Column 1 with the items in Column 2 in the following table:

| **Column 1** | **Column 2** |
| --- | --- |
| (p) Principal Component Analysis | (i) Discriminative Model |
| (q) Na\"ive Bayes Classification | (ii) Dimensionality Reduction |
| (r) Logistic Regression | (iii) Generative Model |

- **(A)** (p)--(iii), (q)--(i), (r)--(ii)
  
- **(B)** (p)--(ii), (q)--(i), (r)--(iii)
  
- **(C)** (p)--(ii), (q)--(iii), (r)--(i)
  
- **(D)** (p)--(iii), (q)--(ii), (r)--(i)

**Answer:** C

---

## Q5040

[MSQ]
[PYQ: GATE DA 2024]

<!-- FIGURE NEEDED: Original question references a figure from the GATE paper -->

Consider the following figures representing datasets consisting of two-dimensional features with two classes denoted by circles and squares.

Figures (i), (ii), (iii), (iv) show four different 2D datasets.

Which of the following is/are TRUE?

- **(A)** (i) is linearly separable.
  
- **(B)** (ii) is linearly separable.
  
- **(C)** (iii) is linearly separable.
  
- **(D)** (iv) is linearly separable.

**Answer:** A, D

---

## Q5041

[MSQ]
[PYQ: GATE DA 2025]

Consider a two-class problem in $\mathbb{R}^d$ with class labels red and green. Let $\boldsymbol{\mu}_{\text{red}}$ and $\boldsymbol{\mu}_{\text{green}}$ be the means of the two classes. Given test sample $\mathbf{x} \in \mathbb{R}^d$, a classifier calculates the squared Euclidean distance between $\mathbf{x}$ and the means of the two classes and assigns the class label that the sample $\mathbf{x}$ is closest to. That is, the classifier computes
$$
f(\mathbf{x}) = \norm{\boldsymbol{\mu}_{\text{red}} - \mathbf{x}}^2 - \norm{\boldsymbol{\mu}_{\text{green}} - \mathbf{x}}^2
$$
and assigns the label red to $\mathbf{x}$ if $f(\mathbf{x}) < 0$, and green otherwise. Which of the following statements is/are correct?

- **(A)** The sample $\mathbf{x} = \mathbf{0}$ is assigned the label green if $\norm{\boldsymbol{\mu}_{\text{red}}} < \norm{\boldsymbol{\mu}_{\text{green}}}$
  
- **(B)** $f$ is a linear function of $\mathbf{x}$
  
- **(C)** $f(\mathbf{x}) = \mathbf{w}^\top\mathbf{x} + b$, where $\mathbf{w}$ and $b$ are functions of $\boldsymbol{\mu}_{\text{red}}$ and $\boldsymbol{\mu}_{\text{green}}$
  
- **(D)** $f$ is a quadratic polynomial in $\mathbf{x}$

**Answer:** B, C

---
