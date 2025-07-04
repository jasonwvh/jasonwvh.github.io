---
layout: post
title:  "Deep Learning Simplified"
date:   2025-07-01 14:19:38 +0800
categories: machine-learning
published: true
---

### Linear Regression

We begin with one of the most fundamental concepts in machine learning: **linear regression**. Its purpose is simple: to model a linear relationship between a dependent variable and one or more independent variables. Imagine plotting data points on a graph; linear regression attempts to find the straight line that best fits these points.

**The Mathematics:**

The hypothesis function, or the model, for simple linear regression is represented as:

$$h_\theta(x) = \theta_0 + \theta_1x$$

Here, $h_\theta(x)$ is the predicted output, $x$ is the input feature, and $\theta_0$ and $\theta_1$ are the parameters (weights) of the model that we need to learn. $\theta_1$ represents the slope of the line, and $\theta_0$ is the y-intercept.

To determine how well our line fits the data, we use a **cost function**. The most common one for linear regression is the **Mean Squared Error (MSE)**:

$$J(\theta_0, \theta_1) = \frac{1}{2m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)})^2$$

where $m$ is the number of training examples, $x^{(i)}$ is the input for the $i$-th example, and $y^{(i)}$ is its actual output. Our goal is to find the values of $\theta_0$ and $\theta_1$ that minimize this cost function.

### Logistic Regression

While linear regression is excellent for predicting continuous values, what if we want to classify data into discrete categories (e.g., spam or not spam)? This is where **logistic regression** comes in. Despite its name, it's a classification algorithm.

The key difference lies in the hypothesis function. Instead of a straight line, logistic regression uses the **sigmoid function** (also known as the logistic function) to constrain the output between 0 and 1.

**The Mathematics:**

The sigmoid function is defined as:

$$g(z) = \frac{1}{1 + e^{-z}}$$

Our hypothesis function then becomes:

$$h_\theta(x) = g(\theta^T x) = \frac{1}{1 + e^{-\theta^T x}}$$

The output $h_\theta(x)$ can be interpreted as the probability that the output is 1. For example, if $h_\theta(x) = 0.7$, it means there's a 70% chance that the output is 1.

The cost function for logistic regression is also different, designed to handle the probabilistic nature of the output. It's the **Log Loss** or **Binary Cross-Entropy** cost function:

$$J(\theta) = -\frac{1}{m} \sum_{i=1}^{m} [y^{(i)} \log(h_\theta(x^{(i)})) + (1 - y^{(i)}) \log(1 - h_\theta(x^{(i)}))]$$

This cost function penalizes the model more heavily when it's confident about a wrong prediction.

### Gradient Descent

Now that we have our cost functions, how do we find the optimal parameters ($\theta$) that minimize them? The answer is an iterative optimization algorithm called **gradient descent**.

Imagine you're standing on a mountain and want to get to the lowest point. You'd look around and take a step in the steepest downward direction. Gradient descent does precisely this. It calculates the gradient (the direction of steepest ascent) of the cost function and takes a small step in the opposite direction to find what's called the **minima**.

**The Mathematics:**

The update rule for gradient descent is:

$$\theta_j := \theta_j - \alpha \frac{\partial}{\partial \theta_j} J(\theta)$$

Here, $\alpha$ is the **learning rate**, a hyperparameter that controls the size of the steps we take. The term $\frac{\partial}{\partial \theta_j} J(\theta)$ is the partial derivative of the cost function with respect to the parameter $\theta_j$, which gives us the direction of the gradient. We repeat this update for all parameters until the cost function converges to a minimum. We will find the minimum when the **gradient is zero**

There are three main types of gradient descent:
* **Batch Gradient Descent:** Calculates the gradient using the entire training dataset in each update. It's computationally expensive but guarantees convergence to the global minimum for convex cost functions.
* **Stochastic Gradient Descent (SGD):** Updates the parameters for each training example. It's much faster but the path to the minimum can be noisy.
* **Mini-batch Gradient Descent:** A compromise between the two, it updates the parameters using a small batch of training examples. This is the most common type used in deep learning.

### Forward and Backward Propagation

Now, let's assemble these building blocks into a simple **neural network**. A neural network consists of interconnected layers of "neurons." Each neuron is essentially a logistic regression unit.

The process of training a neural network involves two key phases: **forward propagation** and **backward propagation**.

**Forward Propagation:**

This is the process of making a prediction. Input data is fed into the first layer of the network. Each neuron in this layer performs a weighted sum of its inputs, adds a bias term, and then applies an **activation function** (like the sigmoid function) to its output. This output is then passed as input to the neurons in the next layer, and this process continues until the final output layer is reached, which gives us our prediction.

**The Mathematics (for a single neuron):**

$$z = w^T x + b$$
$$a = g(z)$$

Here, $w$ is the vector of weights, $x$ is the input vector, $b$ is the bias, $g$ is the activation function, and $a$ is the output of the neuron.

**Backward Propagation:**

Once we have our prediction, we compare it to the actual target value to calculate the error. **Backward propagation** (or backprop) is the algorithm used to propagate this error backward through the network. It calculates the gradient of the cost function with respect to each weight and bias in the network. This is done using the **chain rule** from calculus, which allows us to efficiently compute how much each parameter contributed to the overall error.

**The Mathematics:**

The core of backpropagation is to compute the partial derivatives of the cost function with respect to the weights ($w$) and biases ($b$) in each layer. For the output layer, this is relatively straightforward. For the hidden layers, the chain rule is used to propagate the error gradient backward. For a weight $w_{jk}^l$ connecting the $k$-th neuron in layer $l-1$ to the $j$-th neuron in layer $l$, the update rule involves:

$$\frac{\partial J}{\partial w_{jk}^l} = a_k^{l-1} \delta_j^l$$
$$\frac{\partial J}{\partial b_j^l} = \delta_j^l$$

where $\delta_j^l$ is the error term for the $j$-th neuron in layer $l$, and $a_k^{l-1}$ is the activation of the $k$-th neuron in the previous layer. These gradients are then used in the gradient descent update rule to adjust the weights and biases.

### Activation Functions

We've mentioned activation functions, but their role is crucial. If we only used linear operations, our neural network, no matter how many layers it has, would still be a linear model. **Activation functions** introduce non-linearity into the network, allowing it to learn much more complex patterns in the data.

Besides the sigmoid function, other popular activation functions include:

* **Hyperbolic Tangent (tanh):** Similar to the sigmoid but outputs values between -1 and 1, which can help in centering the data.
    $$
    \tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}
    $$
* **Rectified Linear Unit (ReLU):** This is the most widely used activation function in modern deep learning. It's computationally efficient and helps mitigate the "vanishing gradient" problem (where gradients become very small during backpropagation, slowing down learning).
    $$
    \text{ReLU}(z) = \max(0, z)
    $$
* **Softmax:** Used in the output layer for multi-class classification problems. It converts the raw outputs of the network into a probability distribution over the classes.
    $$
    \text{softmax}(z)_i = \frac{e^{z_i}}{\sum_{j} e^{z_j}}
    $$

### The Neural Network

Finally, we can put all the pieces together to form a neural network. It's a collection of layers, each containing neurons. The first layer is the **input layer**, the last is the **output layer**, and the layers in between are the **hidden layers**. The "deep" in deep learning refers to networks with many hidden layers.

The training process is an iterative loop:
1.  **Forward Propagation:** Feed a batch of training data through the network to get predictions.
2.  **Cost Calculation:** Compare the predictions with the actual labels using a cost function.
3.  **Backward Propagation:** Calculate the gradients of the cost function with respect to all the weights and biases.
4.  **Parameter Update:** Update the weights and biases using an optimization algorithm like gradient descent.

This process is repeated for many epochs (passes through the entire training dataset) until the model's performance on a validation set stops improving.

### Putting It Together

Let's walk through a single iteration with a very simple network to see the numbers in action.

**1. The Setup**

* **Network:** 2 input neurons, one hidden layer with 2 neurons, and 1 output neuron.
* **Inputs (x):** $[0.1, 0.5]$
* **Target (y):** $1$
* **Hidden Layer (Layer 1):**
    * Weights: $W_1 = \begin{bmatrix} 0.2 & 0.4 \\ -0.5 & 0.6 \end{bmatrix}$
    * Biases: $b_1 = [0.1, -0.2]$
    * Activation Function: ReLU
* **Output Layer (Layer 2):**
    * Weights: $W_2 = [0.7, -0.3]$
    * Bias: $b_2 = [0.3]$
    * Activation Function: Sigmoid
* **Cost Function:** Mean Squared Error (MSE), $J = \frac{1}{2}(y_{pred} - y)^2$
* **Learning Rate ($\alpha$):** $0.05$

**2. Forward Propagation**

First, we calculate the output of the hidden layer.

* **Weighted Sum (z1):**
    $$z_1 = W_1 \cdot x + b_1$$
    $$z_1 = \begin{bmatrix} 0.2 & 0.4 \\ -0.5 & 0.6 \end{bmatrix} \begin{bmatrix} 0.1 \\ 0.5 \end{bmatrix} + \begin{bmatrix} 0.1 \\ -0.2 \end{bmatrix} = \begin{bmatrix} (0.2 \cdot 0.1) + (0.4 \cdot 0.5) \\ (-0.5 \cdot 0.1) + (0.6 \cdot 0.5) \end{bmatrix} + \begin{bmatrix} 0.1 \\ -0.2 \end{bmatrix} = \begin{bmatrix} 0.22 \\ 0.25 \end{bmatrix} + \begin{bmatrix} 0.1 \\ -0.2 \end{bmatrix} = \begin{bmatrix} 0.32 \\ 0.05 \end{bmatrix}$$
* **Activation (a1):** Apply ReLU, $a_1 = \text{ReLU}(z_1)$.
    $$a_1 = [\max(0, 0.32), \max(0, 0.05)] = [0.32, 0.05]$$

Now, we feed these activations into the output layer.

* **Weighted Sum (z2):**
    $$z_2 = W_2 \cdot a_1 + b_2$$   
    $$z_2 = [0.7, -0.3] \begin{bmatrix} 0.32 \\ 0.05 \end{bmatrix} + 0.3 = (0.7 \cdot 0.32) + (-0.3 \cdot 0.05) + 0.3 = 0.224 - 0.015 + 0.3 = 0.509$$
* **Activation (a2 - Our Prediction):** Apply Sigmoid, $y_{pred} = g(z_2)$.
    $$y_{pred} = \frac{1}{1 + e^{-0.509}} \approx 0.6246$$

**3. Cost Calculation**

We compare our prediction ($y_{pred}$) with the actual target ($y$).

$$J = \frac{1}{2}(0.6246 - 1)^2 = \frac{1}{2}(-0.3754)^2 \approx 0.0705$$
Our initial error is $0.0705$. Now we need to figure out how to adjust our weights to reduce this error.

**4. Backward Propagation (A Glimpse)**

Here, we calculate the gradients for the output layer's weights ($W_2$) and bias ($b_2$) using the chain rule.

* **Gradient of Cost w.r.t. Prediction ($\frac{\partial J}{\partial y_{pred}}$):**
    $$\frac{\partial J}{\partial y_{pred}} = (y_{pred} - y) = 0.6246 - 1 = -0.3754$$
* **Gradient of Prediction w.r.t. Output Sum ($\frac{\partial y_{pred}}{\partial z_2}$):** This is the derivative of the sigmoid function, which is $g(z)(1-g(z))$.
    $$\frac{\partial y_{pred}}{\partial z_2} = y_{pred}(1 - y_{pred}) = 0.6246(1 - 0.6246) \approx 0.2344$$
* **Gradient of Cost w.r.t. Output Weights ($\frac{\partial J}{\partial W_2}$):**
    $$\frac{\partial J}{\partial W_2} = \frac{\partial J}{\partial y_{pred}} \cdot \frac{\partial y_{pred}}{\partial z_2} \cdot \frac{\partial z_2}{\partial W_2}$$
    The term $\frac{\partial z_2}{\partial W_2}$ is simply the activation from the previous layer, $a_1$.
    $$\delta_2 = \frac{\partial J}{\partial y_{pred}} \cdot \frac{\partial y_{pred}}{\partial z_2} = -0.3754 \cdot 0.2344 \approx -0.0880$$   
    $$\frac{\partial J}{\partial W_2} = \delta_2 \cdot a_1^T = -0.0880 \cdot [0.32, 0.05] = [-0.02816, -0.0044]$$

**5. Parameter Update**

Finally, we update the weights of the output layer.

$$W_2 := W_2 - \alpha \frac{\partial J}{\partial W_2}$$
$$W_2 := [0.7, -0.3] - 0.05 \cdot [-0.02816, -0.0044]$$
$$W_2 := [0.7, -0.3] - [-0.001408, -0.00022]$$
$$W_2^{new} = [0.701408, -0.29978]$$

The same process would be performed for the output bias $b_2$, and then this error ($\delta_2$) would be propagated further back to calculate the gradients for $W_1$ and $b_1$. After one full iteration, the weights have been slightly adjusted to produce a better prediction on the next pass. Repeating this process millions of times is what constitutes "training" a neural network.

