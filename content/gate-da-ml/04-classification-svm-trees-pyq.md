# 04 Classification Svm Trees — PYQ

Source: GATE DA Previous Year Questions

---

## Q5047

[MCQ]
[PYQ: GATE DA 2024]

Consider the dataset with six datapoints: $\{(\mathbf{x}_1, y_1), (\mathbf{x}_2, y_2), \ldots, (\mathbf{x}_6, y_6)\}$, where
$\mathbf{x}_1 = \begin{bmatrix}1\\0\end{bmatrix}$, $\mathbf{x}_2 = \begin{bmatrix}0\\1\end{bmatrix}$, $\mathbf{x}_3 = \begin{bmatrix}0\\-1\end{bmatrix}$, $\mathbf{x}_4 = \begin{bmatrix}-1\\0\end{bmatrix}$, $\mathbf{x}_5 = \begin{bmatrix}2\\2\end{bmatrix}$, $\mathbf{x}_6 = \begin{bmatrix}-2\\-2\end{bmatrix}$

and the labels are given by $y_1 = y_2 = y_5 = 1$ and $y_3 = y_4 = y_6 = -1$. A hard margin linear support vector machine is trained on the above dataset.

Which ONE of the following sets is a possible set of support vectors?
- **(A)** $\{\mathbf{x}_1, \mathbf{x}_2, \mathbf{x}_5\}$
  
- **(B)** $\{\mathbf{x}_3, \mathbf{x}_4, \mathbf{x}_5\}$
  
- **(C)** $\{\mathbf{x}_4, \mathbf{x}_5\}$
  
- **(D)** $\{\mathbf{x}_1, \mathbf{x}_2, \mathbf{x}_3, \mathbf{x}_4\}$

**Answer:** D

---

## Q5048

[MCQ]
[PYQ: GATE DA 2025]

Consider designing a linear binary classifier $f(\mathbf{x}) = \text{sign}(\mathbf{w}^\top\mathbf{x} + b)$, $\mathbf{x} \in \mathbb{R}^2$ on the following training data:

Class-1: $\begin{bmatrix}2\\0\end{bmatrix}$, $\begin{bmatrix}0\\2\end{bmatrix}$, $\begin{bmatrix}2\\2\end{bmatrix}$ \qquad Class-2: $\begin{bmatrix}0\\0\end{bmatrix}$

Hard-margin support vector machine (SVM) formulation is solved to obtain $\mathbf{w}$ and $b$. Which of the following options is/are correct?
- **(A)** $\mathbf{w} = \begin{bmatrix}4\\4\end{bmatrix}$ and $b = 1$
  
- **(B)** The number of support vectors is 3
  
- **(C)** The margin is $\sqrt{2}$
  
- **(D)** Training accuracy is 98\

**Answer:** B, C

---

## Q5049

[NAT]
[PYQ: GATE DA 2024]

Details of ten international cricket games between two teams ``Green'' and ``Blue'' are given in Table~C. This table consists of matches played on different pitches, across formats along with their winners. The attribute Pitch can take one of two values: spin-friendly (represented as $S$) or pace-friendly (represented as $F$). The attribute Format can take one of two values: one-day match (represented as $O$) or test match (represented as $T$).

| **Match Number** | **Pitch** | **Format** | **Winner (Target)** |
| --- | --- | --- | --- |
| 1 | $S$ | $T$ | Green |
| 2 | $S$ | $T$ | Blue |
| 3 | $F$ | $O$ | Blue |
| 4 | $S$ | $O$ | Blue |
| 5 | $F$ | $T$ | Green |
| 6 | $F$ | $O$ | Blue |
| 7 | $S$ | $O$ | Green |
| 8 | $F$ | $T$ | Blue |
| 9 | $F$ | $O$ | Blue |
| 10 | $S$ | $O$ | Green |

A cricket organization would like to use the information given in Table~C to develop a decision-tree model to predict outcomes of future games between these two teams.

To develop such a model, the computed $\text{InformationGain}(\text{C, Pitch})$ with respect to the Target is \_\_\_\_\_\_\_\_ (rounded off to two decimal places).

**Answer:** 0.12 to 0.13

---
