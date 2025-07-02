---
layout: post
title:  "Stochastic Processes Part 5: Simulation"
date:   2025-04-30 14:19:38 +0800
categories: statistics
published: false
---

### Why Simulate?

Many real-world systems, from a city's traffic flow to the risk profile of a financial portfolio, are too complex for direct mathematical analysis. The equations might exist, but they are often intractable.

**Simulation** offers a powerful alternative. By using a computer to generate artificial data that mimics a real-world process, we can estimate probabilities, calculate expected values, and understand the behavior of a system without needing a closed-form solution. The core idea, often called the **Monte Carlo method**, is to use randomness to solve problems that may appear deterministic.

At the heart of every simulation is the ability to generate numbers that "look" random and, more importantly, to transform those numbers into the specific random variables that drive our model.

---

### Generating Random Variables

Computers are deterministic machines, so they can't produce truly random numbers. Instead, they generate **pseudo-random numbers**, typically starting with a "seed" value and using an algorithm to produce a sequence of numbers that appears random and passes statistical tests for randomness.

Most programming languages provide a function—often `rand()` or similar—that generates a random number uniformly distributed between 0 and 1. This uniform distribution is the fundamental building block from which we can create any other distribution we need.

#### The Inverse Transform Method

The most intuitive and fundamental technique for generating a random variable with a specific distribution is the **inverse transform method**. It works for any distribution whose cumulative distribution function (CDF), $F(x)$, can be inverted.

The process is simple:
1.  Generate a random number $U$ from a Uniform(0, 1) distribution.
2.  Set $U = F(X)$, where $F(X) = P(X \le x)$ is the desired CDF.
3.  Solve for $X$ by inverting the function: $X = F^{-1}(U)$.

The resulting value $X$ will have the desired distribution.

**Example: Simulating an Exponential Variable**
An exponential random variable has the CDF $F(x) = 1 - e^{-\lambda x}$.
1.  Generate $U \sim \text{Uniform}(0, 1)$.
2.  Set $U = 1 - e^{-\lambda X}$.
3.  Solving for $X$ gives $1 - U = e^{-\lambda X}$, which leads to $X = -\frac{1}{\lambda} \ln(1 - U)$.
Since $1-U$ is also uniformly distributed on (0, 1), we can use the simpler formula $X = -\frac{1}{\lambda} \ln(U)$. By plugging numbers from our `rand()` function into this formula, we can generate as many exponentially distributed outcomes as we need!

#### The Acceptance-Rejection Method

What if the CDF is difficult or impossible to invert? The **acceptance-rejection method** is a clever technique for such cases.

Imagine you want to generate a random variable from a target density function $f(x)$, but it's too complex. However, you know a simpler density function $g(x)$ that you *can* easily simulate from, and which "covers" $f(x)$ when scaled by a constant $c$ (i.e., $f(x) \le c \cdot g(x)$ for all $x$).

The algorithm is as follows:
1.  Generate a random value $Y$ from the simpler distribution $g$.
2.  Generate a random number $U$ from a Uniform(0, 1) distribution.
3.  **Accept** $Y$ as your sample if $U \le \frac{f(Y)}{c \cdot g(Y)}$. Otherwise, **reject** it and return to step 1.

Essentially, we use the simpler distribution to propose candidates and then accept them with a certain probability that ensures the final accepted values conform to the target distribution $f(x)$.

---

### Simulating a System

With these tools, we can simulate complex processes. To estimate a quantity of interest (like the average waiting time in a queue):
1.  **Model the System**: Define the components using random variables (e.g., Poisson arrivals, general service times).
2.  **Generate Paths**: Simulate one full "run" of the system (e.g., one customer's journey through the queue) by generating the necessary random variables using methods like inverse transform.
3.  **Record Data**: Collect the metric of interest from that run (e.g., the customer's waiting time).
4.  **Repeat**: Perform many independent runs (thousands or millions of times).
5.  **Analyze**: Average the results from all runs. By the Law of Large Numbers, this average will converge to the true expected value you're trying to find.