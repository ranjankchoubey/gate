# Linear Regression — Simple and Multiple

Source: GATE-DA Syllabus — Machine Learning

---

## Q901

[MCQ]

Given a dataset with $n = 5$ points, the total sum of squares is $\text{SST} = 200$ and the residual sum of squares is $\text{SSR} = 50$. What is the value of $R^2$?

- **(A)** 0.25
- **(B)** 0.50
- **(C)** 0.75
- **(D)** 0.80

**Answer:** C

---

## Q902

[NAT]

A simple linear regression model $\hat{y} = \beta_0 + \beta_1 x$ is fitted to the following data:

| $x$ | 1 | 2 | 3 | 4 | 5 |
|-----|---|---|---|---|---|
| $y$ | 2 | 4 | 5 | 4 | 5 |

The OLS estimate $\hat{\beta}_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2}$. Compute $\hat{\beta}_1$ (rounded to 2 decimal places).

**Answer:** 0.60

---

## Q903

[MSQ]

Which of the following are properties of the Ordinary Least Squares (OLS) estimator under the Gauss-Markov assumptions? (Select all that apply)

- **(A)** It is unbiased: $E[\hat{\beta}] = \beta$
- **(B)** It minimises the sum of squared residuals
- **(C)** It has the highest variance among all linear unbiased estimators
- **(D)** It is the Best Linear Unbiased Estimator (BLUE)

**Answer:** A, B, D

---

## Q904

[MCQ]

For a multiple linear regression model with $p = 3$ predictors and $n = 20$ observations, $R^2 = 0.80$. What is the adjusted $R^2$?

$$\bar{R}^2 = 1 - (1 - R^2)\frac{n-1}{n-p-1}$$

- **(A)** 0.7625
- **(B)** 0.762
- **(C)** 0.800
- **(D)** 0.784

**Answer:** A

---

## Q905

[NAT]

In a simple linear regression, $\bar{x} = 3$, $\bar{y} = 4$, $\hat{\beta}_1 = 0.60$. Compute $\hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x}$.

**Answer:** 2.20

---

## Q906

[MCQ]

The design matrix for simple linear regression on $n$ points is $X \in \mathbb{R}^{n \times 2}$ (first column all ones). The OLS solution is $\hat{\beta} = (X^\top X)^{-1} X^\top y$. Which condition makes $(X^\top X)$ non-invertible?

- **(A)** The response variable $y$ has zero mean
- **(B)** Two predictor columns are perfectly linearly dependent (multicollinearity)
- **(C)** The number of observations $n$ is large
- **(D)** The residuals are non-normally distributed

**Answer:** B

---

## Q907

[MCQ]

In gradient descent for linear regression with learning rate $\alpha = 0.01$ and cost function $J(\theta) = \frac{1}{2n}\sum_{i=1}^n (h_\theta(x^{(i)}) - y^{(i)})^2$, if $\alpha$ is increased to 10, what is the most likely outcome?

- **(A)** Faster convergence to the global minimum
- **(B)** Slower convergence to the global minimum
- **(C)** Divergence — the cost increases rather than decreasing
- **(D)** Convergence to a local minimum

**Answer:** C

---

## Q908

[NAT]

A linear regression model predicts $\hat{y} = [2, 4, 3, 5]$ while the true values are $y = [3, 4, 2, 6]$. Compute the Mean Squared Error (MSE) $= \frac{1}{n}\sum_{i=1}^n (y_i - \hat{y}_i)^2$.

**Answer:** 0.75

---

## Q909

[MCQ]

Which of the following correctly describes the effect of feature scaling (standardisation) on gradient descent for linear regression?

- **(A)** It changes the optimal parameter values $\hat{\beta}$
- **(B)** It speeds up convergence by making the cost function contours more circular
- **(C)** It is mandatory for OLS to produce a valid solution
- **(D)** It increases the MSE of the fitted model

**Answer:** B

---

## Q910

[MSQ]

Which of the following statements about $R^2$ in linear regression are correct? (Select all that apply)

- **(A)** $R^2$ always lies in $[0, 1]$ for OLS with an intercept term
- **(B)** Adding a predictor to a multiple regression model can never decrease $R^2$
- **(C)** $R^2 = 1$ implies perfect prediction with zero residuals
- **(D)** A high $R^2$ guarantees that the model will generalise well to new data

**Answer:** A, B, C

---
