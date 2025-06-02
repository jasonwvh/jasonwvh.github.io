---
layout: post
title:  "Stochastic Processes Part 4: Monte Carlo Processes"
date:   2025-04-30 14:19:38 +0800
categories: statistics
published: false
---

Welcome to Part 4 of our stochastic processes series! We’ve laid a solid foundation:  
- **Part 1:** Random walks and Markov chains  
- **Part 2:** Poisson and compound Poisson processes  
- **Part 3:** Wiener process, Geometric Brownian Motion (GBM), and Continuous-Time Markov Chains (CTMCs)  

Now, we’re diving into **jump-diffusion processes** to model sudden changes and **Monte Carlo methods** to estimate probabilities—ideal for systems with abrupt shifts like network traffic or IoT sensor readings. 

---

## Why Jump-Diffusion and Monte Carlo?

Many systems experience smooth trends punctuated by sudden jumps (e.g., traffic spikes from user surges). Jump-diffusion processes blend continuous diffusion (like GBM) with random jumps (like Poisson processes), capturing both dynamics. Monte Carlo methods use simulations to estimate probabilities in complex systems, perfect when analytical solutions are tricky.

**These tools shine in:**
- **Networking:** Modeling traffic surges.
- **IoT:** Simulating sensor spikes.
- **System Monitoring:** Assessing overload risks.

**Our series is:**
1. Random walks, Markov chains (discrete-time)
2. Poisson, compound Poisson (event-driven)
3. Wiener process, GBM, CTMCs (continuous-time)
4. Jump-diffusion, Monte Carlo (hybrid models)
5. Anomaly detection case study

---

## 1. Jump-Diffusion Processes: Trends with Sudden Shifts

### What Is a Jump-Diffusion Process?

A jump-diffusion process models systems with continuous trends and random jumps, defined by the stochastic differential equation (SDE):

\[
dX_t = \mu X_t dt + \sigma X_t dW_t + J_t dN_t
\]

where:
- \( X_t \): Process value (e.g., network traffic)
- \( \mu \): Drift rate (trend)
- \( \sigma \): Volatility (randomness scale)
- \( W_t \): Wiener process (Part 3)
- \( N_t \): Poisson process with rate \( \lambda \) (Part 2)
- \( J_t \): Random jump size (e.g., normal distribution)

It extends GBM (Part 3) with Poisson-driven jumps, ideal for sudden changes.

---

### Simulating a Jump-Diffusion Process

Let’s simulate network traffic over 1 hour with jump-diffusion.

```python
import numpy as np
import matplotlib.pyplot as plt

# Set random seed
np.random.seed(42)

# Parameters
T = 1.0  # Time horizon
N = 1000  # Steps
dt = T / N
X0 = 100  # Initial traffic
mu = 0.1  # Drift
sigma = 0.2  # Volatility
lam = 5  # Jump rate
jump_mean, jump_std = 20, 5  # Jump size

# Simulate
t = np.linspace(0, T, N+1)
X = np.zeros(N+1)
X[0] = X0
dW = np.random.normal(0, np.sqrt(dt), N)
jumps = np.random.poisson(lam * dt, N)
jump_sizes = np.random.normal(jump_mean, jump_std, N) * jumps
for i in range(N):
    X[i+1] = X[i] + mu * X[i] * dt + sigma * X[i] * dW[i] + jump_sizes[i]
plt.figure(figsize=(10, 6))
plt.plot(t, X, label='Jump-Diffusion Process')
plt.title('Jump-Diffusion: Network Traffic with Spikes')
plt.xlabel('Time (hours)')
plt.ylabel('Packets/Second')
plt.grid(True)
plt.legend()
plt.savefig('jump_diffusion.png')
```

This shows a trending path with random spikes, like traffic during peak usage.

---

## 2. Monte Carlo Methods: Estimating Probabilities

### What Are Monte Carlo Methods?

Monte Carlo methods estimate probabilities by running many simulations. For jump-diffusion, we can estimate the chance of traffic exceeding a threshold (e.g., indicating congestion).

**Steps:**
1. Simulate multiple process paths.
2. Compute the metric (e.g., threshold exceedance).
3. Average results for probability.

---

### Monte Carlo for Jump-Diffusion

Let’s estimate the probability that traffic exceeds 150 packets/second.

```python
# Monte Carlo parameters
n_sim = 1000  # Simulations
threshold = 150  # Threshold
exceed = np.zeros(n_sim)

# Simulate paths
for j in range(n_sim):
    X = np.zeros(N+1)
    X[0] = X0
    dW = np.random.normal(0, np.sqrt(dt), N)
    jumps = np.random.poisson(lam * dt, N)
    jump_sizes = np.random.normal(jump_mean, jump_std, N) * jumps
    for i in range(N):
        X[i+1] = X[i] + mu * X[i] * dt + sigma * X[i] * dW[i] + jump_sizes[i]
    exceed[j] = np.any(X > threshold)
prob = np.mean(exceed)
print(f'Probability of Traffic > {threshold}: {prob:.3f}')

# Plot sample paths
plt.figure(figsize=(10, 6))
for j in range(5):  # 5 paths
    X = np.zeros(N+1)
    X[0] = X0
    dW = np.random.normal(0, np.sqrt(dt), N)
    jumps = np.random.poisson(lam * dt, N)
    jump_sizes = np.random.normal(jump_mean, jump_std, N) * jumps
    for i in range(N):
        X[i+1] = X[i] + mu * X[i] * dt + sigma * X[i] * dW[i] + jump_sizes[i]
    plt.plot(t, X, alpha=0.5)
plt.axhline(threshold, color='red', linestyle='--', label='Threshold')
plt.title('Monte Carlo: Jump-Diffusion Paths')
plt.xlabel('Time (hours)')
plt.ylabel('Packets/Second')
plt.grid(True)
plt.legend()
plt.savefig('monte_carlo_paths.png')
```

This estimates the exceedance probability and visualizes path variability.