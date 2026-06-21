# 07 Clustering — PYQ

Source: GATE DA Previous Year Questions

---

## Q5057

[MCQ]
[PYQ: GATE DA 2024]

Euclidean distance based $k$-means clustering algorithm was run on a dataset of 100 points with $k = 3$.\ If the points $\begin{bmatrix} 1 \\ 1 \end{bmatrix}$ and $\begin{bmatrix} -1 \\ 1 \end{bmatrix}$ are both part of cluster 3, then which ONE of the following points is necessarily also part of cluster 3?
- **(A)** $\begin{bmatrix} 0 \\ 0 \end{bmatrix}$
  
- **(B)** $\begin{bmatrix} 0 \\ 2 \end{bmatrix}$
  
- **(C)** $\begin{bmatrix} 2 \\ 0 \end{bmatrix}$
  
- **(D)** $\begin{bmatrix} 0 \\ 1 \end{bmatrix}$

**Answer:** D

---

## Q5058

[MCQ]
[PYQ: GATE DA 2026]

In the following table, the Task column lists a few tasks related to machine learning.\ The Algorithm column lists a few algorithms.\ Each entry ``t'' from the Task column is to be matched with an appropriate entry ``a'' from the Algorithm column such that the task ``t'' can be solved using the algorithm ``a''.

| **Task** | **Algorithm** |
| --- | --- |
| T1 -- Clustering | A1 -- Markov Chain Monte Carlo |
| T2 -- Classification | A2 -- K-Medoid |
| T3 -- Sampling | A3 -- Linear Discriminant Analysis |
| T4 -- Feature Extraction | A4 -- Naive Bayes |

Which of the following options is/are the correct matching(s)?
- **(A)** T1:A4, T2:A3, T3:A1, T4:A2
  
- **(B)** T1:A2, T2:A4, T3:A1, T4:A3
  
- **(C)** T1:A3, T2:A4, T3:A1, T4:A2
  
- **(D)** T1:A2, T2:A3, T3:A4, T4:A1

**Answer:** B

---

## Q5059

[MCQ]
[PYQ: GATE DA 2024]

<!-- FIGURE NEEDED: Original question references a figure from the GATE paper -->

Consider the table below, where the $(i, j)$-th element of the table is the distance between points $x_i$ and $x_j$.\ Single linkage clustering is performed on data points $x_1, x_2, x_3, x_4, x_5$.

|  | $x_1$ | $x_2$ | $x_3$ | $x_4$ | $x_5$ |
| --- | --- | --- | --- | --- | --- |
| $x_1$ | 0 | 1 | 4 | 3 | 6 |
| $x_2$ | 1 | 0 | 3 | 5 | 3 |
| $x_3$ | 4 | 3 | 0 | 2 | 5 |
| $x_4$ | 3 | 5 | 2 | 0 | 1 |
| $x_5$ | 6 | 3 | 5 | 1 | 0 |

Which ONE of the following is the correct representation of the clusters produced?

(Options show different dendrogram structures --- see original paper for diagrams.)

**Answer:** A

---

## Q5060

[MCQ]
[PYQ: GATE DA 2025]

Let $C_1$ and $C_2$ be two sets of objects.\ Let $D(x, y)$ be a measure of dissimilarity between two objects $x$ and $y$.\ Consider the following definitions of dissimilarity between $C_1$ and $C_2$:
$$
\text{DIS-1}(C_1, C_2) = \max_{x \in C_1, y \in C_2} D(x, y)
$$
$$
\text{DIS-2}(C_1, C_2) = \min_{x \in C_1, y \in C_2} D(x, y)
$$
Which of the following statements is/are correct?
- **(A)** Single Linkage Clustering uses DIS-1
  
- **(B)** Single Linkage Clustering uses DIS-2
  
- **(C)** Complete Linkage Clustering uses DIS-2
  
- **(D)** Complete Linkage Clustering uses DIS-1

**Answer:** B, D

---

## Q5061

[MCQ]
[PYQ: GATE DA 2026]

Let four points in three-dimensional space be:
$$
P_1 = [2, 3, -1], \quad P_2 = [3, 1, 1], \quad P_3 = [5, -2, 3], \quad P_4 = [3, 3, 3].
$$
Hierarchical Agglomerative Clustering is used to cluster the above points.\ If Manhattan Distance is used as the distance metric during clustering, which of the following options indicates the two points that will be merged first?
- **(A)** $P_1, P_2$
  
- **(B)** $P_2, P_3$
  
- **(C)** $P_3, P_4$
  
- **(D)** $P_2, P_4$

**Answer:** D

---
