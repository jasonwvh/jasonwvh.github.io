import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_circles
from ripser import ripser
from persim import plot_diagrams

# Generate the circle dataset
points, labels = make_circles(n_samples=2000, noise=0.1, factor=0.3, random_state=42)

# Compute persistent homology
diagrams = ripser(points)['dgms']

# Plot the point cloud
plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.scatter(points[:, 0], points[:, 1], c=labels, s=5, alpha=0.5)
plt.title("Point Cloud (Circle)")
plt.xlabel("x")
plt.ylabel("y")
plt.axis('equal')

# Plot the persistence diagram
plt.subplot(1, 2, 2)
plot_diagrams(diagrams, show=True)
plt.title("Persistence Diagram")
plt.tight_layout()
plt.show()