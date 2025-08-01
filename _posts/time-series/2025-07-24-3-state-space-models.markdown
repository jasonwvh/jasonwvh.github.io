---
layout: post
title: "Time Series 3: State-Space Models"
date: 2025-07-24
categories: time-series
---

In the [first part](/time-series/2025/07/24/1-arima.html) and [second part](/time-series/2025/07/24/2-spectral-analysis.html) of this series, we explored time series analysis from both the time-domain and frequency-domain perspectives. Now, we introduce a powerful and flexible framework that can unify and extend these models: the **state-space model**.

### Gaussian Linear State-Space Models

A common and important class of state-space models is the **Gaussian linear state-space model**. This model assumes that the relationships between variables are linear and that the noise components follow a Gaussian (normal) distribution.

The model is defined by two equations:

1.  **The State Equation:** Describes the evolution of the unobserved (latent) state over time.
    $$
    \mathbf{x}_t = \mathbf{\Phi} \mathbf{x}_{t-1} + \mathbf{w}_t, \quad \mathbf{w}_t \sim N(0, \mathbf{Q})
    $$
    Here, $$ \mathbf{x}_t $$ is the state vector, $$ \mathbf{\Phi} $$ is the state transition matrix, and $$ \mathbf{w}_t $$ is the process noise, which is assumed to be Gaussian with covariance $$ \mathbf{Q} $$.

2.  **The Observation Equation:** Describes how the observed data is generated from the latent state.
    $$
    \mathbf{y}_t = \mathbf{A}_t \mathbf{x}_t + \mathbf{v}_t, \quad \mathbf{v}_t \sim N(0, \mathbf{R})
    $$
    Here, $$ \mathbf{y}_t $$ is the observation vector, $$ \mathbf{A}_t $$ is the observation matrix, and $$ \mathbf{v}_t $$ is the measurement noise, also assumed to be Gaussian with covariance $$ \mathbf{R} $$.

This framework is highly versatile. For example, ARIMA models can be cast into this state-space form, allowing us to apply the powerful tools developed for state-space models to ARIMA analysis.

### The Kalman Filter: Inference in State-Space Models

The **Kalman filter** is a recursive algorithm that is central to working with Gaussian linear state-space models. It allows us to estimate the unobserved state of the system based on the noisy observations. The Kalman filter performs three main operations:

1.  **Prediction:** The filter predicts the state for the current time step before observing the data for that step. It also predicts the uncertainty of this state estimate.
    -   Predict state: $$ \hat{\mathbf{x}}_{t|t-1} = \mathbf{\Phi} \hat{\mathbf{x}}_{t-1|t-1} $$
    -   Predict uncertainty: $$ \mathbf{P}_{t|t-1} = \mathbf{\Phi} \mathbf{P}_{t-1|t-1} \mathbf{\Phi}^T + \mathbf{Q} $$

2.  **Update:** Once the observation for the current time step is available, the filter updates the state estimate by incorporating the new information. This update step corrects the initial prediction.
    -   The update is a weighted average of the predicted state and the new observation, where the weights are determined by the **Kalman gain**. The Kalman gain balances the uncertainty in the prediction and the uncertainty in the observation.

3.  **Smoothing:** While the Kalman filter provides an estimate of the state at time $$t$$ using data up to time $$t$$, **smoothing** algorithms (like the Rauch-Tung-Striebel smoother) use all the available data, up to the final time point $$T$$, to provide a more accurate estimate of the state at time $$t$$. This is particularly useful for historical analysis where the entire dataset is available.

By performing these steps, the Kalman filter provides a powerful and efficient way to track the latent state of a system, making it an essential tool in fields ranging from econometrics and finance to robotics and aerospace engineering.

### Hidden Markov Models (HMMs)

While Gaussian linear models assume a continuous latent state, another important type of state-space model is the **Hidden Markov Model (HMM)**, which deals with discrete latent states. In an HMM, the unobserved state variable $x_t$ can only take on one of $K$ discrete values, and the transitions between these states are governed by a transition probability matrix.

The core components of an HMM are:
-   **Hidden States ($S$):** A set of $K$ hidden states, $S = \{s_1, s_2, \dots, s_K\}$.
-   **Transition Probabilities ($A$):** An $K \times K$ matrix where $A_{ij} = P(x_t = s_j | x_{t-1} = s_i)$ is the probability of transitioning from state $s_i$ to state $s_j$.
-   **Emission Probabilities ($B$):** A set of probabilities describing the distribution of the observed variable $y_t$ for each hidden state. $B_i(y_t) = P(y_t | x_t = s_i)$.
-   **Initial State Probabilities ($\pi$):** A vector of probabilities for the state at $t=1$, where $\pi_i = P(x_1 = s_i)$.

HMMs are particularly well-suited for modeling systems that switch between different regimes or modes of behavior. For example, in finance, an HMM could be used to model a market that switches between "bull" and "bear" states. They are also famously used in bioinformatics for gene sequencing and in speech recognition to model phonemes.

While the Kalman filter is used for inference in linear Gaussian models, HMMs rely on different algorithms, such as the **Viterbi algorithm** to find the most likely sequence of hidden states, and the **Baum-Welch algorithm** for parameter estimation.

### Conclusion: A Unified View

State-space models, particularly when combined with the Kalman filter, offer a unified and powerful framework for time series analysis. They can model complex dynamic systems, handle missing data, and provide a principled way to estimate unobserved components, making them an indispensable tool for any data scientist's toolkit.