---
layout: post
title:  "Stochastic Processes Part 3: Continuous Stochastic Processes"
date:   2025-04-30 14:19:38 +0800
categories: statistics
published: false
---

### Poisson Process

The most fundamental continuous process is the **Poisson Process**. It is the direct analogue of the Binomial process for continuous intervals. It describes the number of events that have occurred up to a certain time, $t$.

Let $N(t)$ be the number of events by time $t$. A Poisson Process with rate $\lambda > 0$ has two defining properties:
1.  **Stationary Increments**: The number of events in any interval of length $s$ has the same distribution, regardless of where the interval is on the timeline.
2.  **Independent Increments**: The number of events in disjoint time intervals are independent of each other.

For any time $t$, the number of events $N(t)$ follows a Poisson distribution with mean $\lambda t$.

$$P\{N(t) = n\} = \frac{e^{-\lambda t}(\lambda t)^n}{n!}$$

A beautiful and crucial property of the Poisson process is that the **waiting time** between consecutive events follows an **Exponential distribution** with rate $\lambda$. This directly connects our study of continuous random variables from the first post to the dynamic processes we see now.

### Continuous-Time Markov Chains

Just as we did in the discrete case, we can generalize beyond a simple counting process using the **Markov Property**: the future depends only on the present. This gives us the **continuous-time Markov chain**.

However, our old tool—the transition probability matrix $P$—no longer works. The probability of a transition happening in an infinitesimally small sliver of time, $dt$, is essentially zero. The question changes from "What is the *probability* of moving to state $j$?" to "What is the *rate* at which we move to state $j$?"

This shift in thinking is the key to the entire topic.

We replace the one-step probability matrix $P$ with a new engine: the **infinitesimal generator matrix**, also known as the **rate matrix**, $Q$.

For a system with states ${0, 1, 2, ...}$, the elements of $Q$ are:
* $q_{ij}$ (for $i \neq j$): The instantaneous **rate** of transition from state $i$ to state $j$.
* $q_{ii}$: The rate of **leaving** state $i$.

To ensure the logic holds, the rate of leaving a state must be the sum of the rates of going to all other states. Therefore, the diagonal elements are defined as:

$$q_{ii} = -\sum_{j \neq i} q_{ij}$$

This has a critical consequence: **the rows of a rate matrix $Q$ always sum to zero.**

#### Example: A Simple Machine

Consider a machine that can be in one of two states: **State 0 (Working)** or **State 1 (Broken)**.
* When it's working, it fails at a rate of $\lambda$.
* When it's broken, it is repaired at a rate of $\mu$.

The generator matrix $Q$ for this system is:
$$
Q = \begin{pmatrix}
-\lambda & \lambda \\
\mu & -\mu
\end{pmatrix}
$$
* $q_{01} = \lambda$ is the rate of moving from Working to Broken.
* $q_{10} = \mu$ is the rate of moving from Broken to Working.
* $q_{00} = -\lambda$ and $q_{11} = -\mu$ ensure the rows sum to 0.


#### The Kolmogorov Equations

So we have rates, but we still want probabilities. How can we find the probability of being in state $j$ at time $t$ if we started in state $i$? Let's call this $P_{ij}(t)$.

In the discrete world, we found this by taking powers of the matrix $P$. In the continuous world, the relationship between the rate matrix $Q$ and the probability matrix $P(t)$ is described by a system of **differential equations**.

These are the famous **Kolmogorov's Equations**. In matrix form, they are surprisingly elegant:

* **Forward Equation**: $P'(t) = P(t) Q$
* **Backward Equation**: $P'(t) = Q P(t)$

Here, $P'(t)$ is the matrix of the derivatives of the probability functions $P_{ij}(t)$. These equations state that the rate of change in transition probabilities is governed by the generator matrix $Q$. While solving these systems is a topic for a deeper dive, their existence provides the mathematical machinery to turn instantaneous rates into long-term probabilities.

### Brownian Motion

While continuous-time Markov chains model systems that *jump* between discrete states, another, equally important process describes movement that is completely erratic and continuous. This is **Brownian motion**, the mathematical model for phenomena like the random jiggling of a pollen grain in water or the fluctuations of a stock price.

Named after botanist Robert Brown and put on a rigorous mathematical footing by Albert Einstein and Norbert Wiener, it is one of the most studied stochastic processes. It is often called a **Wiener process**.

#### What Defines Brownian Motion?

A standard Brownian motion, denoted by $\{B(t), t \ge 0\}$, is a process defined by a few key properties:

1.  **Starts at Zero**: $B(0) = 0$. The process begins at the origin.
2.  **Independent Increments**: Just like the Poisson process, the movement during any time interval is independent of the movement in any other non-overlapping interval.
3.  **Normal Increments**: This is the crucial property. The change in the process over an interval of length $t$, which is $B(t+s) - B(s)$, follows a **Normal distribution** with a mean of 0 and a variance of $t$.
    $$B(t+s) - B(s) \sim \mathcal{N}(0, t)$$
4.  **Continuous Paths**: The function $B(t)$ is continuous in $t$. This means there are no jumps—the path is connected, however jagged it may be.

The "Normal increments" property is what sets it apart. While a Poisson process *counts* events over time, a Brownian motion path accumulates an infinite number of infinitesimally small, normally distributed "nudges."

#### The "Beautifully Strange" Nature of the Path

The consequences of these properties are fascinating and non-intuitive:

* **Nowhere Differentiable**: A Brownian motion path is continuous everywhere but differentiable *nowhere*. Its path is so jagged and irregular on every scale that you can never define a tangent line.
* **Infinite Variation**: The path zig-zags so much that its total length over any finite time interval is infinite.

#### Why Brownian Motion is Essential

Brownian motion is a cornerstone of modern science and finance for two main reasons:

1.  **It is the limit of random walks**: Just as the Normal distribution is the limit of the Binomial distribution (the Central Limit Theorem), Brownian motion is the continuous-time limit of a simple random walk.
2.  **Applications are everywhere**:
    * **Physics**: It's the standard model for diffusion and other random transport phenomena.
    * **Finance**: A variation called **Geometric Brownian Motion** is the foundation of the Nobel Prize-winning **Black-Scholes model** for pricing financial options. It's used to model stock prices under the assumption that their percentage returns (not absolute returns) are random.

In summary, if a Poisson process is about *when* jumps occur, Brownian motion is about continuous, erratic wandering. It represents a different, but equally fundamental, pillar in the study of continuous stochastic processes.
