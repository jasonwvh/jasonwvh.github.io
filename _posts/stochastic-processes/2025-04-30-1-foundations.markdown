---
layout: post
title:  "Probability 1: Foundations"
date:   2025-04-30 14:19:38 +0800
categories: statistics
published: true
---

## Probability 1: Foundations

The world is full of randomness, from the fluctuating price of a stock to the unpredictable movement of particles in the air. Stochastic processes provide a mathematical framework for describing and analyzing these dynamic, uncertain systems. This introductory post lays the essential groundwork, defining what a stochastic process is and introducing the key concepts of sample space, sample functions, and the probabilistic laws that govern them. We'll explore how to classify these processes and delve into the fundamental ideas of stationarity and ergodicity, which are crucial for making sense of random data over time.

### Random Variables

At its core, a random variable is a way of assigning a numerical value to the outcome of a random experiment. Imagine flipping a coin, the outcome could be "heads" or "tails." A random variable, let's call it $X$, could assign $1$ to "heads" and $0$ to "tails."

There are two types of random variable: **discrete** and **continuous**.

### Discrete Random Variables

A random variable is **discrete** if it can take on a finite or countably infinite number of values. Think of things you can count, even if the count could theoretically go on forever.

* The number of heads in three coin flips (0, 1, 2, or 3).
* The number of emails you receive in an hour (0, 1, 2, 3, ...).
* The number of times you roll a die until you get a six (1, 2, 3, 4, ...).

The behavior of a discrete random variable is described by its **Probability Mass Function (PMF)**. The PMF, denoted as $p(a)$, gives us the probability that the random variable $X$ is exactly equal to some value $a$.

$$P(X = a) = p(a)$$

A key rule for any PMF is that the sum of the probabilities for all possible values must equal 1.

#### Expectation

A crucial concept for any random variable is its **expected value**. For a discrete random variable $X$, the expected value, denoted $E[X]$, is the weighted average of its possible values, where the weights are the probabilities from the PMF.

$$E[X] = \sum_{x} x \cdot P(X=x)$$

But not all outcomes are equally close to this mean. The **variance** measures how spread out the values are around the expected value:

$\text{Var}(X) = E[(X - E[X])^2] = \sum_x (x - E[X])^2 \cdot P(X=x)$

It tells us about the unpredictability of \$X\$. A coin flip (low variance) is more predictable than roulette (high variance).

#### Common Discrete Random Variables

* **Bernoulli**: The simplest of all. It represents a single trial with two outcomes (success/failure), like a single coin flip. $X=1$ for success (with probability $p$) and $X=0$ for failure (with probability $1-p$).
* **Binomial**: This is just a sequence of independent Bernoulli trials. It answers the question: "If I flip a coin $n$ times, what's the probability of getting exactly $k$ heads?"
* **Poisson**: This variable is a workhorse for modeling the number of events occurring in a fixed interval of time or space. For example, the number of customers arriving at a store in an hour or the number of typos on a page.

### Continuous Random Variables

A random variable is **continuous** if it can take any value within a given range. Think of things you measure, not count.

* The height of a person.
* The exact temperature of a room.
* The time it takes for a web page to load.

For a continuous variable, the probability of it being *exactly* a specific value is zero. Why? Because there are infinitely many possible values. We can't assign a non-zero probability to each one without breaking the "sum must be 1" rule.

Instead, we use a **Probability Density Function (PDF)**, denoted as $f(x)$. The PDF doesn't give us direct probabilities. Instead, the probability that a random variable $X$ falls within a certain range is the **area under the curve** of the PDF in that range.

$$P(a \le X \le b) = \int_{a}^{b} f(x) \,dx$$

Like the PMF, the total area under the PDF curve across all possible values must be 1.

#### Expectation

The concept of expected value is the same, but instead of summing, we integrate over the PDF.

$$E[X] = \int_{-\infty}^{\infty} x \cdot f(x) \,dx$$

Again, this represents the long-run average value of the random variable.

Fun fact: the expected value at any particular time is 0, because the integral at any particular time is also 0.

#### Common Continuous Random Variables

* **Uniform**: This describes a variable where all outcomes in a range are equally likely. Think of a perfect random number generator that produces a value between 0 and 1.
* **Exponential**: Often used to model the time until an event occurs, like the lifespan of a lightbulb or the time between customer arrivals. It's closely related to the Poisson distribution.
* **Normal (or Gaussian)**: The famous "bell curve." It appears everywhere, from statistical measurements and financial modeling to the distribution of heights and test scores, thanks to the Central Limit Theorem.

### Joint Distributions

Sometimes we deal with more than one random variable—say, \$X\$ and \$Y\$. Their behavior together is described by a **joint distribution**.

* For discrete variables:
  $P(X = x, Y = y)$ is the **joint PMF**.

* For continuous variables:
  $f(x, y)$ is the **joint PDF**, and:
  $P((X, Y) \in A) = \iint_A f(x, y) \,dx\,dy$

From the joint distribution, we can extract:

* **Marginal distribution** of \$X\$:
  $P(X = x) = \sum_y P(X = x, Y = y)$
* **Conditional distribution**:
  $P(Y = y \mid X = x) = \frac{P(X = x, Y = y)}{P(X = x)}$

Two variables \$X\$ and \$Y\$ are **independent** if and only if:
$P(X = x, Y = y) = P(X = x)P(Y = y)$

Joint distributions are essential for modeling everything from correlations in asset returns to dependencies in queuing systems.