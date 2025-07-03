---
layout: post
title:  "Stochastic Processes Part 2: Discrete Stochastic Processes"
date:   2025-04-30 14:19:38 +0800
categories: statistics
published: true
---

### Markov Chains

A stochastic process is a lot to handle. The outcome at any given time could depend on the entire history of the process. Imagine trying to predict tomorrow's weather based on the weather of every day for the last fifty years!

Markov chains simplify this dramatically by introducing a "memoryless" rule called the **Markov Property**.

**The Markov Property**: The future state of the process depends *only* on the present state, not on the sequence of events that preceded it.

Think of a game of Snakes and Ladders. Your next position depends only on your current square and your dice roll—not on how you got to your current square. This assumption makes modeling complex systems surprisingly manageable.

A **Markov chain** is a stochastic process that follows the Markov property. To define one, we need two things: a set of possible states and a way to describe the movement between them.

### The Transition Matrix

Let's imagine a simple weather model where the weather can be in one of two states: **State 0 (Sunny)** or **State 1 (Rainy)**. We observe the weather each day.

The movement between these states is governed by probabilities. For instance:
* If it's sunny today, there's a 90% chance it will be sunny tomorrow and a 10% chance it will be rainy.
* If it's rainy today, there's a 50% chance it will be sunny tomorrow and a 50% chance it will be rainy.

We can capture this entire system in a neat package using linear algebra: the **transition matrix**, often denoted by $P$.

$$
P = \begin{pmatrix}
0.9 & 0.1 \\
0.5 & 0.5
\end{pmatrix}
$$

Here's how to read it: The element in row $i$ and column $j$, called $P_{ij}$, is the probability of moving from state $i$ to state $j$ in one step.
* $P_{01} = 0.1$ is the probability of moving from Sunny (State 0) to Rainy (State 1).
* $P_{11} = 0.5$ is the probability of moving from Rainy (State 1) to Rainy (State 1).

Notice that each row must sum to 1, because from any state, you *must* transition to one of the possible states.

### Matrix Multiplication

So, the matrix $P$ gives us one-step probabilities. But what's the probability that a sunny day is followed by another sunny day *two* days later?

This requires us to consider all possibilities for the intermediate day:
1.  Sunny → Sunny → Sunny
2.  Sunny → Rainy → Sunny

The probability is $(0.9 \times 0.9) + (0.1 \times 0.5) = 0.81 + 0.05 = 0.86$.

This calculation is tedious. This is where the elegance of linear algebra comes in. The probabilities for an n-step transition are given by the **n-step transition matrix**, $P^{(n)}$. And as the famous **Chapman-Kolmogorov equations** show, this is simply the initial matrix $P$ multiplied by itself $n$ times.

$$P^{(n)} = P^n$$

Let's find the 2-step transition matrix for our weather model by calculating $P^2$:

$$
P^2 = P \times P = \begin{pmatrix}
0.9 & 0.1 \\
0.5 & 0.5
\end{pmatrix}
\begin{pmatrix}
0.9 & 0.1 \\
0.5 & 0.5
\end{pmatrix}
= \begin{pmatrix}
(0.9)(0.9) + (0.1)(0.5) & (0.9)(0.1) + (0.1)(0.5) \\
(0.5)(0.9) + (0.5)(0.5) & (0.5)(0.1) + (0.5)(0.5)
\end{pmatrix}
$$

$$
P^2 = \begin{pmatrix}
0.86 & 0.14 \\
0.70 & 0.30
\end{pmatrix}
$$

The top-left entry, 0.86, is exactly what we calculated by hand! The matrix $P^2$ instantly gives us all the 2-day transition probabilities. Want to know the probabilities for 10 days from now? Just calculate $P^{10}$.

### State of the System

We can also represent the probability of being in any given state at a certain time $n$ with a **state probability vector**, $\pi_n$. For example, if we know today is sunny, our initial state vector is $\pi_0 = [1, 0]$ (100% chance of being in State 0, 0% in State 1).

To find the probability distribution for tomorrow, we simply multiply our initial state vector by the transition matrix:

$$\pi_1 = \pi_0 P = [1, 0] \begin{pmatrix} 0.9 & 0.1 \\ 0.5 & 0.5 \end{pmatrix} = [0.9, 0.1]$$

This tells us that tomorrow there's a 90% chance of sun and a 10% chance of rain, which matches our initial setup. To find the distribution for day $n$, the formula is beautifully simple:

$$\pi_n = \pi_0 P^n$$

### Stationary Distribution

So far, we've explored how to model transitions from one state to the next. But what happens in the long run?

Sometimes, no matter where we start, the probabilities of being in each state settle into a stable pattern. This is called the **stationary distribution**, denoted by \$\pi\$.

Mathematically, \$\pi\$ is a row vector satisfying:

$\pi P = \pi \quad \text{and} \quad \sum_i \pi_i = 1$

This means: if our system starts in the stationary distribution, it stays there forever.

#### When Does a Stationary Distribution Exist?

If the Markov chain is:

* **Irreducible**: Every state can be reached from every other state.
* **Aperiodic**: The chain doesn’t return to states in regular cycles.
* **Positive recurrent**: The expected return time to each state is finite.

then the chain has a **unique stationary distribution**, and:

$\pi_n \to \pi \quad \text{as} \quad n \to \infty$

In other words, after many steps, the state probabilities converge to \$\pi\$, no matter where you started.
