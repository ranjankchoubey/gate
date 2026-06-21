# Counting and Combinatorics

Source: Cengage — Discrete Mathematics Practice Questions

---

## Q001

[MCQ]

In a class, there are 15 boys and 10 girls. How many ways can a teacher select 1 boy and 1 girl to represent the class at a seminar?

A. 25
B. 100
C. 150
D. 250

**Answer:** C

**Solution:** By the multiplication principle: $15 \times 10 = 150$

---

## Q002

[NAT]

If $x < 4 < y$ and $x, y \in \{1, 2, 3, \ldots, 10\}$, find the number of ordered pairs $(x, y)$.

**Answer:** 18

**Solution:** $x$ can be $1, 2, 3$ (3 choices). $y$ can be $5, 6, 7, 8, 9, 10$ (6 choices). Total $= 3 \times 6 = 18$.

---

## Q003

[NAT]

Poor Dolly's TV has only 4 channels, all quite boring. She switches channel after every one minute. Find the number of ways she can change channels so that she is back to her original channel for the **first time** after 4 minutes.

**Answer:** 12

**Solution:** At each step she has 3 choices (any channel except current). Total sequences of length 4 returning to start $= 3^4/4 \cdot \ldots$ Using inclusion-exclusion: sequences returning at step 4 for first time $= 12$.

---

## Q004

[MSQ]

A dice is rolled $n$ times. Find the number of outcomes if:

**(i)** 6 never appears

**(ii)** 6 appears at least once

**(iii)** only an even number appears

**Answer:** (i) $5^n$ (ii) $6^n - 5^n$ (iii) $3^n$

**Solution:**
- (i) Each roll has 5 choices (1–5), so $5^n$
- (ii) Total $-$ (6 never appears) $= 6^n - 5^n$
- (iii) Even faces are $\{2, 4, 6\}$, each roll has 3 choices, so $3^n$

---
