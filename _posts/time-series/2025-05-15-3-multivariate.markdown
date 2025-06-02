---
layout: post
title:  "Time Series Part 3: Multivariate Time Series"
date:   2025-05-15 14:19:38 +0800
categories: time-series
published: false
---

# Time Series Analysis Part 3: Seasonal and Multivariate Models

Welcome to Part 3 of our time series analysis series! In Part 1, we covered time series basics like trends, seasonality, and stationarity, and in Part 2, we explored classical univariate models (AR, MA, ARMA, ARIMA) for forecasting single series. Now, we’re stepping up to seasonal and multivariate models to handle periodic patterns and correlated data.
---

## Why Seasonal and Multivariate Models?

Time series often exhibit repeating patterns (e.g., daily traffic peaks) or involve multiple related variables (e.g., traffic and latency). Seasonal models like SARIMA capture periodic behavior, while multivariate models like VAR handle correlations between series. These are key for complex systems like IoT or network monitoring. In this post, we’ll:

- Model seasonal patterns with SARIMA, Holt-Winters, and ETS.
- Forecast correlated series with VAR.
- Use Python to fit models to synthetic data.

---

## 1. SARIMA: Seasonal ARIMA for Periodic Patterns

### What Is SARIMA?

SARIMA (Seasonal ARIMA) extends ARIMA (Part 2) to handle seasonality, like daily or weekly cycles in network traffic. It combines:

- **ARIMA(p,d,q):** Non-seasonal components (autoregression, differencing, moving average).
- **Seasonal (P,D,Q)m:** Seasonal components with period \( m \) (e.g., \( m=24 \) for hourly data with daily cycles).

Denoted SARIMA(p,d,q)(P,D,Q)m, it models trends, noise, and seasonal patterns. For example, SARIMA(1,1,0)(1,1,0)\(_{24}\) captures a trend (d=1), autoregression (p=1), and daily seasonality (D=1, P=1, m=24).

### Fitting a SARIMA Model

Let’s simulate hourly network traffic (100 hours) with a trend and daily seasonality, then fit a SARIMA model.

```python
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX

# Set random seed
np.random.seed(42)

# Generate synthetic time series
t = np.arange(100)
trend = 0.5 * t
seasonality = 10 * np.sin(2 * np.pi * t / 24)
noise = np.random.normal(0, 2, 100)
series = trend + seasonality + noise

# Fit SARIMA(1,1,0)(1,1,0)24
model = SARIMAX(series, order=(1, 1, 0), seasonal_order=(1, 1, 0, 24))
fit = model.fit(disp=False)
forecast = fit.forecast(steps=24)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(t, series, label='Time Series')
plt.plot(np.arange(100, 124), forecast, label='Forecast', linestyle='--')
plt.title('SARIMA(1,1,0)(1,1,0)24: Traffic Forecast')
plt.xlabel('Time (hours)')
plt.ylabel('Packets/Second')
plt.grid(True)
plt.legend()
plt.savefig('sarima_forecast.png')
```

This code fits a SARIMA model, capturing the trend and daily cycles, and forecasts 24 hours. The plot shows the series and forecast continuing the pattern.

---

## 2. Holt-Winters: Exponential Smoothing for Seasonality

### What Is Holt-Winters?

Holt-Winters (triple exponential smoothing) models level, trend, and seasonality using weighted averages, smoothing data over time. It’s simpler than SARIMA and great for quick forecasts. There are additive and multiplicative versions:

- **Additive:** Level + Trend + Seasonality.
- **Multiplicative:** Level × Trend × Seasonality.

### Fitting Holt-Winters

Let’s apply additive Holt-Winters to our series.

```python
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Fit Holt-Winters (additive, 24-hour period)
model_hw = ExponentialSmoothing(series, trend='add', seasonal='add', seasonal_periods=24)
fit_hw = model_hw.fit()
forecast_hw = fit_hw.forecast(steps=24)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(t, series, label='Time Series')
plt.plot(np.arange(100, 124), forecast_hw, label='Holt-Winters Forecast', linestyle='--')
plt.title('Holt-Winters: Traffic Forecast')
plt.xlabel('Time (hours)')
plt.ylabel('Packets/Second')
plt.grid(True)
plt.legend()
plt.savefig('holt_winters_forecast.png')
```

This forecasts 24 hours, capturing seasonality and trend with smooth predictions.

---

## 3. ETS Models: Error, Trend, Seasonality

### What Is ETS?

ETS (Error, Trend, Seasonality) models generalize exponential smoothing, allowing combinations of:

- **Error:** Additive or multiplicative.
- **Trend:** None, additive, multiplicative, damped.
- **Seasonality:** None, additive, multiplicative.

ETS is flexible, fitting data via maximum likelihood, similar to SARIMA but simpler to tune.

### Fitting an ETS Model

Let’s fit an ETS model (additive error, trend, seasonality).

```python
from statsmodels.tsa.exponential_smoothing.ets import ETSModel

# Fit ETS (additive)
model_ets = ETSModel(series, error='add', trend='add', seasonal='add', seasonal_periods=24)
fit_ets = model_ets.fit()
forecast_ets = fit_ets.forecast(steps=24)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(t, series, label='Time Series')
plt.plot(np.arange(100, 124), forecast_ets, label='ETS Forecast', linestyle='--')
plt.title('ETS: Traffic Forecast')
plt.xlabel('Time (hours)')
plt.ylabel('Packets/Second')
plt.grid(True)
plt.legend()
plt.savefig('ets_forecast.png')
```

This produces a forecast similar to Holt-Winters but optimized via likelihood.

---

## 4. Vector Autoregression (VAR): Modeling Correlated Series

### What Is VAR?

Vector Autoregression (VAR) models multiple time series together, capturing their correlations. For two series (e.g., traffic and latency), VAR(p) predicts each series using past values of both:

\[
\begin{align*}
y_{1,t} &= c_1 + \phi_{11,1} y_{1,t-1} + \phi_{12,1} y_{2,t-1} + \dots + \epsilon_{1,t} \\
y_{2,t} &= c_2 + \phi_{21,1} y_{1,t-1} + \phi_{22,1} y_{2,t-1} + \dots + \epsilon_{2,t}
\end{align*}
\]

VAR assumes stationarity (Part 1), often requiring differencing.

### Fitting a VAR Model

Let’s simulate correlated traffic and latency, then fit a VAR model.

```python
import pandas as pd
from statsmodels.tsa.vector_ar.var_model import VAR

# Generate correlated series
np.random.seed(42)
traffic = series  # From SARIMA example
latency = 0.5 * traffic + np.random.normal(0, 1, 100)  # Correlated with noise
data = pd.DataFrame({'Traffic': traffic, 'Latency': latency})

# Fit VAR(1)
model_var = VAR(data.diff().dropna())  # Difference for stationarity
fit_var = model_var.fit(maxlags=1)
forecast_var = fit_var.forecast(data.diff().dropna().values[-1:], steps=10)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(data.index[-20:], data['Traffic'][-20:], label='Traffic')
plt.plot(np.arange(100, 110), forecast_var[:, 0], label='Traffic Forecast', linestyle='--')
plt.plot(data.index[-20:], data['Latency'][-20:], label='Latency')
plt.plot(np.arange(100, 110), forecast_var[:, 1], label='Latency Forecast', linestyle='--')
plt.title('VAR: Traffic and Latency Forecast')
plt.xlabel('Time (hours)')
plt.ylabel('Value')
plt.grid(True)
plt.legend()
plt.savefig('var_forecast.png')
```

This models traffic and latency, forecasting both with their correlation.