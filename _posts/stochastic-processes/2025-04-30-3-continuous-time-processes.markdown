---
layout: post
title:  "Stochastic Processes Part 3: Continuous-Time Processes"
date:   2025-04-30 14:19:38 +0800
categories: statistics
published: false
---

Welcome to Part 3 of our stochastic processes series! In Part 1, we explored random walks and Markov chains, modeling systems like network packet routing. Part 2 introduced Poisson and compound Poisson processes for events like traffic spikes. Now, we’re diving into continuous-time processes: the **Wiener process**, **Geometric Brownian Motion (GBM)**, and **Continuous-Time Markov Chains (CTMCs)**. These tools help model dynamic systems with randomness, like network latency or IoT sensor noise.
---

## Why Continuous-Time Processes?

Unlike discrete-time models (e.g., random walks in Part 1), continuous-time processes capture systems evolving smoothly or with frequent state changes. The Wiener process models random fluctuations, GBM handles multiplicative trends, and CTMCs track state transitions over time. They’re perfect for:

- **Networking:** Modeling latency jitter or traffic trends.
- **IoT:** Simulating sensor noise or device states.
- **System Monitoring:** Tracking dynamic metrics.

**Our series is building your toolkit:**

1. Part 1: Random walks, Markov chains (discrete-time).
2. Part 2: Poisson, compound Poisson (event-driven).
3. Part 3: Wiener process, GBM, CTMCs (continuous-time).
4. Part 4: Jump-diffusion, Monte Carlo (hybrid models).
5. Part 5: Anomaly detection case study.

---

## 1. Wiener Process: The Foundation of Continuous-Time

### What Is a Wiener Process?

A **Wiener process** (or Brownian motion) is a continuous-time stochastic process \( W_t \) with:

- **Starting point:** \( W_0 = 0 \)
- **Independent increments:** \( W_t - W_s \sim N(0, t-s) \) for \( s < t \)
- **Continuous paths:** \( W_t \) is continuous but nowhere differentiable
- **Zero mean, variance \( t \):** \( E[W_t] = 0 \), \( \text{Var}[W_t] = t \)

Think of it as a continuous version of a random walk (Part 1), modeling random fluctuations like network latency noise.

### Simulating a Wiener Process

Let’s simulate a Wiener process over 1 time unit (e.g., 1 hour):

```python
import numpy as np
import matplotlib.pyplot as plt

# Set random seed
np.random.seed(42)

# Parameters
T = 1.0  # Time horizon
N = 1000  # Steps
dt = T / N
t = np.linspace(0, T, N+1)

# Simulate Wiener process
dW = np.random.normal(0, np.sqrt(dt), N)
W = np.concatenate([[0], np.cumsum(dW)])

plt.figure(figsize=(10, 6))
plt.plot(t, W, label='Wiener Process')
plt.title('Wiener Process Simulation')
plt.xlabel('Time (hours)')
plt.ylabel('W(t)')
plt.grid(True)
plt.legend()
plt.savefig('wiener_process.png')
```

This plots a random, continuous path, showing the Wiener process’s erratic behavior.

---

## 2. Geometric Brownian Motion: Multiplicative Trends

### What Is GBM?

**Geometric Brownian Motion (GBM)** models systems with multiplicative random changes, defined by the stochastic differential equation (SDE):

\[
dX_t = \mu X_t dt + \sigma X_t dW_t
\]

where:

- \( X_t \): Process value (e.g., system load)
- \( \mu \): Drift (trend rate)
- \( \sigma \): Volatility (randomness scale)
- \( W_t \): Wiener process

GBM’s solution is:

\[
X_t = X_0 \exp\left( \left( \mu - \frac{\sigma^2}{2} \right)t + \sigma W_t \right)
\]

Unlike a Wiener process, GBM stays positive and grows exponentially, ideal for trending metrics.

### Simulating GBM

Let’s simulate GBM for network traffic over 1 hour:

```python
# Parameters
X0 = 100  # Initial value
mu = 0.1  # Drift
sigma = 0.2  # Volatility

# Simulate GBM
W = np.concatenate([[0], np.cumsum(np.random.normal(0, np.sqrt(dt), N))])
X = X0 * np.exp((mu - 0.5 * sigma**2) * t + sigma * W)

plt.figure(figsize=(10, 6))
plt.plot(t, X, label='Geometric Brownian Motion')
plt.title('GBM Simulation: Network Traffic')
plt.xlabel('Time (hours)')
plt.ylabel('Packets/Second')
plt.grid(True)
plt.legend()
plt.savefig('gbm_simulation.png')
```

This shows traffic growing with random multiplicative noise, unlike the Wiener process’s zero-mean drift.

---

## 3. Continuous-Time Markov Chains: State Transitions

### What Are CTMCs?

A **Continuous-Time Markov Chain (CTMC)** extends discrete-time Markov chains (Part 1) to continuous time. It models systems with states (e.g., “normal,” “congested”) and random transition times, governed by a rate matrix \( Q \), where \( q_{ij} \) is the transition rate from state \( i \) to \( j \), and diagonal \( q_{ii} = -\sum_{j \neq i} q_{ij} \).

The process:

- Stay in state \( i \) for an exponential time with rate \( -\sum_{j \neq i} q_{ij} \).
- Transition to state \( j \) with probability \( q_{ij} / (-\sum_{j \neq i} q_{ij}) \).

### Simulating a CTMC

Let’s simulate a network with three states: normal (0), congested (1), down (2):

```python
# Rate matrix Q
Q = np.array([
    [-0.5, 0.4, 0.1],  # Normal
    [0.3, -0.6, 0.3],  # Congested
    [0.2, 0.2, -0.4]   # Down
])

# Simulate CTMC
states = [0]  # Start normal
times = [0]
current_time = 0
current_state = 0
for _ in range(50):  # 50 transitions
    rate = -Q[current_state, current_state]
    sojourn = np.random.exponential(1 / rate)
    current_time += sojourn
    times.append(current_time)
    probs = Q[current_state] / rate
    probs[current_state] = 0
    next_state = np.random.choice([0, 1, 2], p=probs / probs.sum())
    states.append(next_state)
    current_state = next_state

# Plot
plt.figure(figsize=(10, 6))
plt.step(times, states, where='post', label='Network State')
plt.title('CTMC Simulation: Network States')
plt.xlabel('Time (hours)')
plt.ylabel('State (0=Normal, 1=Congested, 2=Down)')
plt.grid(True)
plt.legend()
plt.savefig('ctmc_simulation.png')
```

This plots state transitions, showing random switches driven by exponential times.