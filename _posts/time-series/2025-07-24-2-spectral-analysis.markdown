---
layout: post
title: "Time Series 2: Spectral Analysis"
date: 2025-07-24
categories: time-series
---

In the [first part of this series](/time-series/2025/07/24/1-arima.html), we explored ARIMA models, which operate in the time domain. Now, we'll shift our perspective to the frequency domain and explore spectral analysis. This powerful technique allows us to identify hidden periodicities and cyclical patterns in time series data that are often difficult to detect by simply looking at the data over time.

### Decomposing Signals into Frequencies

The core idea of spectral analysis is that any time series can be represented as a combination of sine and cosine waves of different frequencies. By breaking down a time series into its constituent frequencies, we can identify the dominant cycles in the data.

The primary tool for this decomposition is the **Discrete Fourier Transform (DFT)**. The DFT takes a time series and transforms it from the time domain to the frequency domain. For a time series $$x_t$$ of length $$n$$, the DFT is given by:

$$ d(\omega_j) = \frac{1}{\sqrt{n}} \sum_{t=1}^{n} x_t e^{-2\pi i \omega_j t} $$

where $$\omega_j = j/n$$ are the Fourier frequencies. The DFT produces a set of complex numbers that represent the amplitude and phase of each frequency component.

While the DFT is foundational, in practice, we often use the **Fast Fourier Transform (FFT)**, which is a highly efficient algorithm for computing the DFT. The FFT makes spectral analysis computationally feasible for large datasets.

### The Periodogram: Visualizing Frequency Content

Once we have transformed our data to the frequency domain using the FFT, we need a way to visualize the strength of each frequency. This is where the **periodogram** comes in. The periodogram is a plot that shows the power (or variance) of the time series at different frequencies.

The periodogram is calculated as the squared magnitude of the DFT coefficients:

$$ I(\omega_j) = |d(\omega_j)|^2 $$

A peak in the periodogram at a specific frequency indicates that a significant portion of the time series' variance is concentrated at that frequency, which in turn suggests the presence of a cycle.

For example, if we analyze a time series of daily temperature data, we would expect to see a strong peak in the periodogram at a frequency corresponding to a 365-day cycle, as well as a smaller peak for the 24-hour cycle. Similarly, for economic data, we might find cycles related to business quarters or fiscal years.

By examining the periodogram, we can uncover these hidden rhythms in our data, providing valuable insights that might be missed by time-domain analysis alone.

In the next and final part of this series, we will explore state-space models, a flexible framework that can encompass ARIMA models and more.