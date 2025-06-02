---
layout: post
title:  "Time Series Part 1: Foundations"
date:   2025-05-15 14:19:38 +0800
categories: time-series
published: false
---

# Time Series Analysis Part 1: Introduction to Time Series and Stationarity

Welcome to the first part of our series on time series analysis! Time series analysis helps us understand patterns, forecast future values, and detect anomalies in dynamic systems.

In this post, we’ll cover the basics: what time series data is, key concepts like trends and seasonality, and why stationarity matters. We’ll use Python to explore a simple dataset and set the stage for modeling in later parts.

---

## What Is Time Series Data?

A **time series** is a sequence of data points collected at regular intervals over time. Think of it as a snapshot of a system’s behavior, like hourly network packet counts or daily server CPU usage. Unlike regular datasets, time series data is ordered, and its patterns (e.g., trends, cycles) are tied to time.

---

## Key Concepts in Time Series

Time series data typically has three components:

- **Trend:** A long-term increase or decrease (e.g., growing network traffic over months).
- **Seasonality:** Repeating patterns at fixed intervals (e.g., daily spikes in server load).
- **Noise:** Random fluctuations that don’t follow a pattern (e.g., unpredictable packet delays).

Understanding these helps us model and forecast data. Let’s visualize them with a synthetic time series.

```python
import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic time series (100 hours)
t = np.arange(100)
trend = 0.5 * t  # Linear trend
seasonality = 10 * np.sin(2 * np.pi * t / 24)  # Daily cycle
noise = np.random.normal(0, 2, 100)  # Random noise
series = trend + seasonality + noise

# Plot
plt.figure(figsize=(10, 6))
plt.plot(t, series, label='Time Series')
plt.title('Synthetic Time Series: Trend, Seasonality, Noise')
plt.xlabel('Time (hours)')
plt.ylabel('Value (e.g., Packets/Second)')
plt.grid(True)
plt.legend()
plt.savefig('time_series.png')
```

This code creates a time series with a rising trend, daily seasonality, and noise, mimicking network traffic. The plot shows a clear upward slope with periodic waves and random wiggles.

---

## Stationarity: Why It Matters

Many time series models (like ARIMA, coming in Post 2) assume **stationarity**, meaning the data’s statistical properties (mean, variance, autocorrelation) don’t change over time. Non-stationary data, with trends or varying seasonality, can mislead models.

For example, our synthetic series above is non-stationary due to its trend. To check stationarity, we use statistical tests:

- **Augmented Dickey-Fuller (ADF) Test:** Tests for a unit root (non-stationarity). Null hypothesis: non-stationary.
- **KPSS Test:** Tests for stationarity around a mean or trend. Null hypothesis: stationary.

Let’s test our series with the ADF test.

```python
from statsmodels.tsa.stattools import adfuller

# ADF test
result = adfuller(series)
print(f'ADF Statistic: {result[0]:.3f}')
print(f'p-value: {result[1]:.3f}')
print('Stationary' if result[1] < 0.05 else 'Non-Stationary')
```

Running this likely shows a high p-value (>0.05), indicating non-stationarity due to the trend. We’ll address this with differencing later.

---

## Decomposition: Breaking Down the Components

Decomposition splits a time series into trend, seasonality, and residuals (noise). There are two types:

- **Additive:** Series = Trend + Seasonality + Residuals.
- **Multiplicative:** Series = Trend × Seasonality × Residuals.

Our synthetic series is additive (trend + seasonality + noise). Let’s decompose it.

```python
from statsmodels.tsa.seasonal import seasonal_decompose

# Decompose (assume 24-hour periodicity)
decomp = seasonal_decompose(series, model='additive', period=24)
plt.figure(figsize=(10, 8))
decomp.plot()
plt.savefig('decomposition.png')
```

This plots the series, trend, seasonality, and residuals, helping us see each component clearly. Try a multiplicative model if the series has growing seasonal swings!

---

## Differencing: A Tool for Stationarity

To make a non-stationary series stationary, we can use **differencing**: subtract each value from the previous one to remove trends. For a series \( y_t \):

\[
y'_t = y_t - y_{t-1}
\]

Let’s difference our series and retest stationarity.

```python
# Difference the series
diff_series = np.diff(series)
result_diff = adfuller(diff_series)
print(f'ADF Statistic (Differenced): {result_diff[0]:.3f}')
print(f'p-value (Differenced): {result_diff[1]:.3f}')
print('Stationary' if result_diff[1] < 0.05 else 'Non-Stationary')
```

Differencing often lowers the p-value, indicating stationarity. This is key for models like ARIMA (Post 2).