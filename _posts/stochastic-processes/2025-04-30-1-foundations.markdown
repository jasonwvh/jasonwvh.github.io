---
layout: post
title:  "Stochastic Processes Part 1: Foundations"
date:   2025-04-30 14:19:38 +0800
categories: statistics
published: false
---

Welcome to the first part of our series on **stochastic processes**! Stochastic processes are mathematical tools to describe systems that evolve unpredictably over time, and they’re a gateway to exciting applications in data science, networking, and beyond. In this post, we’ll kick things off with two foundational concepts: **random walks** and **Markov chains**. These discrete-time processes are intuitive, code-friendly, and set the stage for everything from event modeling to anomaly detection.

---

## What Are Stochastic Processes?

A **stochastic process** is a sequence of random variables indexed by time, representing a system’s evolution. Think of it as a model for things like a server’s load fluctuating or a user clicking through a website. Unlike deterministic systems (e.g., \( y = 2x \)), stochastic processes embrace uncertainty, making them perfect for real-world problems where randomness rules.

---

## 1. Random Walks: A Simple Stroll Through Randomness

### What Is a Random Walk?

A **random walk** is one of the simplest stochastic processes. Imagine a person standing at position 0 on a number line, flipping a coin every second. Heads, they step right (+1); tails, they step left (-1). Their position over time is a random walk—a sequence of steps driven by chance.

Mathematically, for a simple symmetric random walk:

- Start at \( S_0 = 0 \).
- At time \( t \), take a step \( X_t = +1 \) or \( -1 \) with equal probability (0.5).
- Position at time \( t \): \( S_t = S_{t-1} + X_t \), or \( S_t = \sum_{i=1}^t X_i \).

Random walks model systems where small, random changes accumulate, like a network packet’s jitter or a sensor’s noisy readings.

### Simulating a Random Walk

Let’s simulate a 1000-step random walk in Python, starting at 0, with +1 or -1 steps.

```python
import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Parameters
n_steps = 1000
steps = np.random.choice([1, -1], size=n_steps)  # +1 or -1
position = np.cumsum(steps)  # Cumulative sum
time = np.arange(n_steps)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(time, position, label='Random Walk')
plt.title('Simple Random Walk')
plt.xlabel('Step')
plt.ylabel('Position')
plt.grid(True)
plt.legend()
plt.savefig('random_walk.png')
```

This code generates a jagged path, showing the position wandering randomly. Run it a few times—each path is unique! Try tweaking the step probabilities (e.g., 60% for +1) to model biased systems.

### Key Properties

- **Expected Value:** \( E[S_t] = 0 \) for a symmetric walk (equal chance of +1/-1).
- **Variance:** \( \text{Var}(S_t) = t \), so the walk spreads out over time.
- **Recurrence:** In 1D, the walk returns to 0 infinitely often (with probability 1).

---

## 2. Markov Chains: Memoryless State Transitions

### What Is a Markov Chain?

A **Markov chain** extends the idea of random walks to systems with multiple states. Imagine a server switching between states like “Idle,” “Busy,” or “Down.” The next state depends only on the current state, not the past—a property called **memorylessness**.

Formally, a discrete-time Markov chain is defined by:

- **States:** A set of possible states (e.g., {Idle, Busy, Down}).
- **Transition Matrix:** A matrix \( P \) where \( P_{ij} \) is the probability of moving from state \( i \) to state \( j \). Each row sums to 1.
- **Markov Property:** \( P(X_{t+1} = j \mid X_t = i, X_{t-1}, \dots) = P(X_{t+1} = j \mid X_t = i) \).

For example, a server’s transition matrix might be:

\[
P = \begin{bmatrix}
0.8 & 0.15 & 0.05 \\
0.2 & 0.7 & 0.1 \\
0.1 & 0.3 & 0.6
\end{bmatrix}
\]

If the server is Idle, there’s an 80% chance it stays Idle, 15% it becomes Busy, and 5% it goes Down.

### Simulating a Markov Chain

Let’s simulate a Markov chain for a server’s state over 100 steps, starting as Idle, using the transition matrix above.

```python
import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Transition matrix
P = np.array([
    [0.8, 0.15, 0.05],  # Idle -> Idle, Busy, Down
    [0.2, 0.7, 0.1],    # Busy -> Idle, Busy, Down
    [0.1, 0.3, 0.6]     # Down -> Idle, Busy, Down
])

# Simulate Markov chain
states = [0]  # Start at Idle (state 0)
n_steps = 100
for _ in range(n_steps - 1):
    current_state = states[-1]
    next_state = np.random.choice([0, 1, 2], p=P[current_state])
    states.append(next_state)

# Convert states to labels
state_labels = {0: 'Idle', 1: 'Busy', 2: 'Down'}
state_sequence = [state_labels[s] for s in states]

# Plot
plt.figure(figsize=(10, 4))
plt.plot(range(n_steps), states, 'o-', label='Server State')
plt.yticks([0, 1, 2], ['Idle', 'Busy', 'Down'])
plt.title('Markov Chain: Server State Simulation')
plt.xlabel('Step')
plt.ylabel('State')
plt.grid(True)
plt.legend()
plt.savefig('markov_chain.png')
```

This code generates a sequence of server states, jumping between Idle, Busy, and Down. The plot shows the state transitions over time. Try changing the transition matrix to model a less reliable server!

### Key Properties

- **Stationary Distribution:** Over time, the chain may settle into a stable probability distribution (e.g., 60% Idle, 30% Busy, 10% Down).
- **Irreducibility:** If every state can reach every other state, the chain is irreducible.
- **Link to Random Walks:** A random walk is a Markov chain where states are positions and transitions are +1/-1 steps.

---
