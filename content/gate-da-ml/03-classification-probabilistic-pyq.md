# 03 Classification Probabilistic — PYQ

Source: GATE DA Previous Year Questions

---

## Q5042

[MCQ]
[PYQ: GATE DA 2024]

Given a dataset with $K$ binary-valued attributes (where $K > 2$) for a two-class classification task, the number of parameters to be estimated for learning a na\"ive Bayes classifier is

- **(A)** $2K + 1$
  
- **(B)** $2K + 1$
  
- **(C)** $2^{K+1} + 1$
  
- **(D)** $K^2 + 1$

**Answer:** B

---

## Q5043

[NAT]
[PYQ: GATE DA 2025]

The naive Bayes classifier is used to solve a two-class classification problem with class labels $y_1, y_2$. Suppose the prior probabilities are $P(y_1) = \frac{1}{3}$ and $P(y_2) = \frac{2}{3}$. Assuming a discrete feature space with
$$
P(\mathbf{x} \mid y_1) = \frac{3}{4} \quad \text{and} \quad P(\mathbf{x} \mid y_2) = \frac{1}{4}
$$
for a specific feature vector $\mathbf{x}$. The probability of misclassifying $\mathbf{x}$ is \_\_\_\_\_\_\_\_ (rounded off to two decimal places).

**Answer:** 0.40

---

## Q5044

[NAT]
[PYQ: GATE DA 2026]

A clinic specializes in testing for a disease $D$. The result of the test can be either positive or negative.

A study revealed that if a person suffers from the disease $D$, the test result in that clinic comes out positive 80\

If a person tests positive for $D$ in that clinic, the probability that he/she actually suffers from the disease $D$ is \_\_\_\_\_\_\_\_ (rounded off to two decimal places).

**Answer:** 0.77

---

## Q5045

[NAT]
[PYQ: GATE DA 2024]

<!-- FIGURE NEEDED: Original question references a figure from the GATE paper -->

Given the two-dimensional dataset consisting of 5 data points from two classes (circles and squares) and assume that the Euclidean distance is used to measure the distance between two points. The minimum odd value of $k$ in $k$-nearest neighbor algorithm for which the diamond ($\diamond$) shaped data point is assigned the label square is \_\_\_\_\_\_\_\_.

*Note:* The figure shows 5 labeled points (3 circles, 2 squares) and a query point $\diamond$ in 2D space.

**Answer:** 5

---

## Q5046

[MCQ]
[PYQ: GATE DA 2024]

For any binary classification dataset, let $S_B \in \mathbb{R}^{d \times d}$ and $S_W \in \mathbb{R}^{d \times d}$ be the between-class and within-class scatter (covariance) matrices, respectively. The Fisher linear discriminant is defined by $u^* \in \mathbb{R}^d$, that maximizes
$$
J(u) = \frac{u^\top S_B u}{u^\top S_W u}
$$

If $\lambda = J(u^*)$, $S_W$ is non-singular and $S_B \neq 0$, then $(u^*, \lambda)$ must satisfy which ONE of the following equations?

Note: $\mathbb{R}$ denotes the set of real numbers.
- **(A)** $S_W\inv S_B u^* = \lambda u^*$
  
- **(B)** $S_W u^* = \lambda S_B u^*$
  
- **(C)** $S_B S_W u^* = \lambda u^*$
  
- **(D)** $u^{*\top} u^* = \lambda^2$

**Answer:** A

---
