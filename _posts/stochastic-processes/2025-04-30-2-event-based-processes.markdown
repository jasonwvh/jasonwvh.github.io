---
layout: post
title:  "Stochastic Processes Part 2: Event-Based Processes"
date:   2025-04-30 14:19:38 +0800
categories: statistics
published: false
---

Welcome to Part 2 of our series on stochastic processes! In Part 1, we explored random walks and Markov chains, laying the groundwork for modeling systems with discrete steps and state transitions. Now, we’re diving into event-based processes: **Poisson processes** and **compound Poisson processes**. These tools are perfect for modeling random events—like network packet arrivals or system alerts—where timing and impact matter.

---

## Why Event-Based Processes?

Stochastic processes model systems evolving with randomness, from user clicks to server loads. While random walks (Part 1) track cumulative steps and Markov chains handle state switches, **Poisson processes focus on when events occur**, and **compound Poisson processes add how big those events are**. These are key for systems where events happen sporadically, like monitoring network traffic or logging errors.

**In this post, we’ll:**

- Simulate a Poisson process to count events over time.
- Extend it to a compound Poisson process to model events with random magnitudes.
- Apply these to problems like network monitoring or system event analysis.

**This series is building your toolkit:**

1. Part 1: Random walks and Markov chains (discrete foundations).
2. Part 2: Poisson and compound Poisson processes (event-driven models).
3. Part 3: Wiener process, geometric Brownian motion, and continuous-time Markov chains (continuous-time dynamics).
4. Part 4: Jump-diffusion processes and Monte Carlo methods (advanced models and simulation).
5. Part 5: Case study on anomaly detection in time-series data.

---

## 1. Poisson Process: Counting Random Events

### What Is a Poisson Process?

A **Poisson process** models events that occur randomly over time at a constant average rate. Imagine packets arriving at a network router: they don’t follow a schedule, but you expect about 10 per second on average. The Poisson process counts these arrivals, assuming events are independent and don’t “clump” unnaturally.

Formally, a Poisson process \( N(t) \) with rate \( \lambda \) (events per unit time) has:

- **Number of Events:** \( N(t) \), the count of events by time \( t \), follows a Poisson distribution:  
  \( P(N(t) = k) = \frac{(\lambda t)^k e^{-\lambda t}}{k!} \)
- **Interarrival Times:** Times between events are exponential with mean \( \frac{1}{\lambda} \).
- **Independent Increments:** Events in non-overlapping intervals are independent.

For example, if \( \lambda = 10 \) packets/second, the number of packets in 2 seconds follows a Poisson distribution with mean \( \lambda t = 20 \).

### Simulating a Poisson Process

Let’s simulate a Poisson process for network packet arrivals over 10 seconds with rate \( \lambda = 5 \) packets/second.

```python
import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Parameters
lambda_rate = 5  # Events per second
T = 10  # Total time (seconds)

# Simulate interarrival times (exponential)
interarrivals = np.random.exponential(1/lambda_rate, size=100)  # More than needed
arrival_times = np.cumsum(interarrivals)
arrival_times = arrival_times[arrival_times <= T]  # Keep within [0, T]

# Compute event counts
event_counts = np.arange(len(arrival_times))
time_points = np.concatenate(([0], arrival_times))  # Include t=0
counts = np.concatenate(([0], event_counts))  # Include N(0)=0

# Plot
plt.figure(figsize=(10, 6))
plt.step(time_points, counts, where='post', label='Poisson Process')
plt.title(f'Poisson Process (λ={lambda_rate} packets/second)')
plt.xlabel('Time (seconds)')
plt.ylabel('Number of Packets')
plt.grid(True)
plt.legend()
plt.savefig('poisson_process.png')
```

This code generates random interarrival times (exponential distribution), computes cumulative arrival times, and plots a step function counting packets. Each step is an event, and the jumps occur at random times. Try changing \( \lambda \) to simulate busier or quieter traffic!

### Key Properties

- **Expected Value:** \( E[N(t)] = \lambda t \) (e.g., 50 packets in 10 seconds for \( \lambda = 5 \)).
- **Variance:** \( \text{Var}(N(t)) = \lambda t \), so counts become more variable over time.
- **Memorylessness:** The exponential interarrivals mean past events don’t affect future ones, like Markov chains (Part 1).

---

## 2. Compound Poisson Process: Events with Random Magnitudes

### What Is a Compound Poisson Process?

A **compound Poisson process (CPP)** builds on the Poisson process by assigning a random magnitude to each event. Instead of just counting packets, a CPP tracks the total data size of packets, where each packet has a random size (e.g., bytes). This makes it ideal for systems where events have varying impacts.

Mathematically, a CPP \( Y(t) \) is:
\[
Y(t) = \sum_{i=1}^{N(t)} X_i
\]
where:

- \( N(t) \): Poisson process with rate \( \lambda \) (number of events by time \( t \)).
- \( X_i \): Independent, identically distributed random magnitudes (e.g., packet sizes).

For example, if packets arrive at \( \lambda = 5 \)/second and each has a size drawn from a normal distribution (\( \mu = 1000 \) bytes, \( \sigma = 200 \)), \( Y(t) \) is the total bytes received by time \( t \).

### Simulating a Compound Poisson Process

Let’s simulate a CPP for network traffic over 10 seconds with \( \lambda = 5 \), where each packet’s size is normally distributed (\( \mu = 1000 \) bytes, \( \sigma = 200 \)).

```python
import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Parameters
lambda_rate = 5  # Events per second
T = 10  # Total time (seconds)
mu_size = 1000  # Mean packet size (bytes)
sigma_size = 200  # Std dev of packet size

# Simulate Poisson process (event times)
interarrivals = np.random.exponential(1/lambda_rate, size=100)
arrival_times = np.cumsum(interarrivals)
arrival_times = arrival_times[arrival_times <= T]

# Simulate packet sizes
sizes = np.random.normal(mu_size, sigma_size, len(arrival_times))

# Compute compound Poisson process
Y = np.cumsum(sizes)  # Cumulative sum of sizes
time_points = np.concatenate(([0], arrival_times))  # Include t=0
values = np.concatenate(([0], Y))  # Include Y(0)=0

# Plot
plt.figure(figsize=(10, 6))
plt.step(time_points, values, where='post', label='Compound Poisson Process')
plt.title(f'Compound Poisson Process (λ={lambda_rate}, Size ~ N({mu_size}, {sigma_size}))')
plt.xlabel('Time (seconds)')
plt.ylabel('Total Bytes')
plt.grid(True)
plt.legend()
plt.savefig('compound_poisson.png')
```

This code extends the Poisson process by adding random packet sizes, plotting the cumulative data volume. The step function jumps at event times, with jump sizes varying. Try using an exponential distribution for sizes to model more skewed data!

### Key Properties

- **Expected Value:** \( E[Y(t)] = \lambda t E[X_i] \), where \( E[X_i] \) is the expected magnitude (e.g., 1000 bytes).
- **Variance:** \( \text{Var}(Y(t)) = \lambda t E[X_i^2] \), accounting for variability in sizes.
- **Connection to Poisson:** If \( X_i = 1 \), the CPP reduces to a Poisson process.
