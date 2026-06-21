# 06 Neural Networks — PYQ

Source: GATE DA Previous Year Questions

---

## Q5052

[MCQ]
[PYQ: GATE DA 2025]

Consider the standard perceptron learning algorithm with learning rate $\eta > 0$. A training point $(\mathbf{x}_n, y_n)$ is misclassified by the current weight vector $\mathbf{w}_{\text{old}}$, so the weight vector is updated to $\mathbf{w}_{\text{new}} = \mathbf{w}_{\text{old}} + \eta \, y_n \, \mathbf{x}_n$.

Let $f(\mathbf{x}_n; \mathbf{w}) = \mathbf{w}^\top \mathbf{x}_n$.

Which of the following statements is TRUE?
- **(A)** $\abs{f(\mathbf{x}_n; \mathbf{w}_{\text{new}})} \geq \abs{f(\mathbf{x}_n; \mathbf{w}_{\text{old}})}$
  
- **(B)** $\abs{f(\mathbf{x}_n; \mathbf{w}_{\text{new}})} \leq \abs{f(\mathbf{x}_n; \mathbf{w}_{\text{old}})}$
  
- **(C)** $y_n \cdot f(\mathbf{x}_n; \mathbf{w}_{\text{new}}) > y_n \cdot f(\mathbf{x}_n; \mathbf{w}_{\text{old}})$
  
- **(D)** $y_n \cdot f(\mathbf{x}_n; \mathbf{w}_{\text{new}}) < y_n \cdot f(\mathbf{x}_n; \mathbf{w}_{\text{old}})$

**Answer:** C

---

## Q5053

[MCQ]
[PYQ: GATE DA 2024]

Consider two feed-forward neural networks $N_1$ and $N_2$, each with one hidden layer and ReLU activation. Both networks have architecture $1 \to 2 \to 1$ (1 input, 2 hidden units, 1 output) with no bias.

Network $N_1$ has weights: input$\to$hidden $= (2, -1)$, hidden$\to$output $= (3, 4)$.

Network $N_2$ has weights: input$\to$hidden $= (p, q)$, hidden$\to$output $= (r, 4)$.

If $N_1$ and $N_2$ compute the same function for all inputs $x \in \mathbb{R}$, which of the following is a valid $(p, q, r)$?
- **(A)** $(4, -1, 1.5)$
  
- **(B)** $(2, -2, 3)$
  
- **(C)** $(1, -1, 6)$
  
- **(D)** $(2, -1, 4)$

**Answer:** A

---

## Q5054

[MCQ]
[PYQ: GATE DA 2025]

Consider a feed-forward neural network with one hidden unit. The computation is:
$$
a = w_1 x_1 + w_2 x_2, \quad f = \text{ReLU}(a), \quad y = v \cdot f
$$
where $w_1 = 1$, $w_2 = -1$, $v = 2$, and input $(x_1, x_2) = (3, 1)$.

Which of the following is/are correct?
- **(A)** $\pd{y}{a} = 2$
  
- **(B)** $\pd{y}{a} = 0$
  
- **(C)** $\pd{y}{f} = 2$
  
- **(D)** $\pd{y}{f} = 0$

**Answer:** A

---

## Q5055

[MCQ]
[PYQ: GATE DA 2025]

The ReLU (Rectified Linear Unit) activation function is defined as $f(x) = \max(0, x)$.

Which of the following statements is/are TRUE?
- **(A)** $f(x)$ is continuous everywhere
  
- **(B)** $f(x)$ is differentiable everywhere
  
- **(C)** $f(x)$ is not differentiable at $x = 0$
  
- **(D)** $f(x)$ is not continuous at $x = 0$

**Answer:** A, C

---

## Q5056

[NAT]
[PYQ: GATE DA 2026]

A feed-forward neural network has the following architecture: 30 input neurons, followed by hidden layers of size 4 and 3, and an output layer of 1 neuron. The network has no bias parameters. What is the total number of learnable parameters (weights) in this network? ______

**Answer:** 135

---
