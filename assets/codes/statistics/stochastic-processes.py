import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)  # For reproducibility
T = 1.0  # Total time
N = 1000  # Number of steps
dt = T / N
t = np.linspace(0, T, N)

# 2. Random Walk (symmetric)
random_steps = np.random.choice([-1, 1], size=N)
random_walk = np.cumsum(random_steps)

# 3. Wiener Process (Brownian Motion)
dW = np.random.normal(0, np.sqrt(dt), size=N)
W = np.cumsum(dW)  # Cumulative sum of normal increments

# 4. Poisson Process
lambda_rate = 10  # Rate λ
poisson_times = np.cumsum(np.random.exponential(1 / lambda_rate, int(1.5 * lambda_rate * T)))
poisson_times = poisson_times[poisson_times <= T]
poisson_process = np.arange(1, len(poisson_times) + 1)

# Plot all processes
fig, axs = plt.subplots(3, 1, figsize=(10, 12))

axs[0].plot(t, random_walk)
axs[0].set_title("Symmetric Random Walk")

axs[1].plot(t, W)
axs[1].set_title("Wiener Process (Brownian Motion)")

axs[2].step(poisson_times, poisson_process, where='post')
axs[2].set_title("Poisson Process (λ = 10)")
axs[2].set_xlim([0, T])

plt.tight_layout()
plt.show()

