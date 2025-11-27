---
layout: post
title:  "Topological Data Analysis 1: Understanding Persistent Homology"
date:   2025-04-15 14:19:38 +0800
categories: topological-data-analysis
published: true
---

## Understanding Persistent Homology
Persistent homology tracks topological features (connected components, loops, voids) across multiple scales to help us understand intrinsic patterns and behaviors hidden in high-dimensional data.

- Build a family of simplicial complexes (graphs, triangles, tetrahedra, etc.) from data points by connecting points within a growing radius $$\epsilon$$.  
- Track when features **appear** (birth) and **disappear** (death) as $$\epsilon$$ changes.  
- Features that persist across a wide range of scales are considered meaningful; short-lived features are often noise.

### Applying Persistent Homology 

Assuming we have a point cloud $$\mathbf{X}$$:

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_circles
from ripser import ripser
from persim import plot_diagrams

point_cld, labels = make_circles(n_samples=2000, noise=0.05, factor=0.3, random_state=42)

diagrams = ripser(point_cld)['dgms']
plot_diagrams(diagrams, show=True)
```

![](/assets/images/understanding-ph/ph_005.png)
![](/assets/images/understanding-ph/ph_01.png)
![](/assets/images/understanding-ph/ph_05.png)

### Interpreting the Persistence Diagrams
H0 diagram: Points far from the diagonal correspond to long-lasting connected components (clusters).

H1 diagram: Points far from the diagonal correspond to persistent loops, which may represent cycles or periodic behavior in the traffic dynamics.

### Summary
TDA provides a novel, geometry-driven perspective to analyze data.

Persistent homology reveals multi-scale topological features robust to noise.