# Conditional Probability, Bayes' Theorem and Independence

Source: GATE-DA Syllabus — Probability and Statistics

---

## Q201

[MCQ]

For two events $A$ and $B$ with $P(B) > 0$, the conditional probability $P(A|B)$ is defined as:

- **(A)** $P(A) \cdot P(B)$
- **(B)** $\dfrac{P(A \cap B)}{P(A)}$
- **(C)** $\dfrac{P(A \cap B)}{P(B)}$
- **(D)** $P(A) + P(B)$

**Answer:** C

---

## Q202

[NAT]

$P(A) = 0.6$, $P(B) = 0.5$, and $P(A \cap B) = 0.3$. What is $P(A|B)$?

**Answer:** 0.6

---

## Q203

[MCQ]

A box contains 6 red and 4 blue balls. Two balls are drawn without replacement. Given that the first ball drawn is red, what is the probability that the second ball is also red?

- **(A)** $\dfrac{6}{10}$
- **(B)** $\dfrac{5}{9}$
- **(C)** $\dfrac{5}{10}$
- **(D)** $\dfrac{6}{9}$

**Answer:** B

---

## Q204

[MCQ]

Two events $A$ and $B$ are independent if and only if:

- **(A)** $P(A \cap B) = 0$
- **(B)** $P(A \cup B) = 1$
- **(C)** $P(A \cap B) = P(A) \cdot P(B)$
- **(D)** $P(A|B) = P(B)$

**Answer:** C

---

## Q205

[NAT]

$P(A) = 0.4$ and $P(B) = 0.3$. If $A$ and $B$ are independent, what is $P(A \cap B)$?

**Answer:** 0.12

---

## Q206

[MSQ]

Which of the following are true if $A$ and $B$ are independent events? (Select all that apply)

- **(A)** $P(A|B) = P(A)$
- **(B)** $P(B|A) = P(B)$
- **(C)** $P(A \cap B) = 0$
- **(D)** $A^c$ and $B^c$ are also independent

**Answer:** A, B, D

---

## Q207

[MCQ]

Bayes' theorem states that $P(H|E)$ equals:

- **(A)** $\dfrac{P(E) \cdot P(H)}{P(E|H)}$
- **(B)** $\dfrac{P(E|H) \cdot P(H)}{P(E)}$
- **(C)** $P(E|H) + P(H)$
- **(D)** $\dfrac{P(H)}{P(E|H)}$

**Answer:** B

---

## Q208

[NAT]

A disease affects 1% of a population. A diagnostic test has sensitivity 0.99 (true positive rate) and specificity 0.95 (true negative rate). A randomly chosen person tests positive. Using Bayes' theorem, what is the posterior probability (to 2 decimal places) that the person actually has the disease?

$$P(\text{Disease}|\text{Pos}) = \frac{0.99 \times 0.01}{0.99 \times 0.01 + 0.05 \times 0.99} = \frac{0.0099}{0.0594} \approx 0.17$$

**Answer:** 0.17

---

## Q209

[MCQ]

A factory has two machines: $M_1$ produces 60% of items (3% defective) and $M_2$ produces 40% (5% defective). An item chosen at random is defective. What is the probability it came from $M_1$?

- **(A)** $\dfrac{9}{19}$
- **(B)** $\dfrac{10}{19}$
- **(C)** $\dfrac{3}{8}$
- **(D)** $\dfrac{18}{38}$

**Answer:** A

---

## Q210

[NAT]

Three bags each contain balls: $B_1$ has 2 white and 3 black, $B_2$ has 3 white and 2 black, $B_3$ has 4 white and 1 black. One bag is selected with equal probability and one ball is drawn. Given the ball is white, what is $P(B_3 | \text{white})$? Express your answer as a decimal rounded to 2 decimal places.

$$P(W) = \frac{1}{3}\!\left(\frac{2}{5}+\frac{3}{5}+\frac{4}{5}\right) = \frac{1}{3}\cdot\frac{9}{5} = \frac{3}{5}$$
$$P(B_3|W) = \frac{\frac{1}{3}\cdot\frac{4}{5}}{\frac{3}{5}} = \frac{4}{9} \approx 0.44$$

**Answer:** 0.44

---
