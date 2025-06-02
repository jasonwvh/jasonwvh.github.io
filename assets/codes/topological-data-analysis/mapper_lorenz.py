import kmapper as km
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from gtda.time_series import SingleTakensEmbedding, TakensEmbedding
from kmapper import Cover
from numpy.ma.core import equal
from scipy.integrate import solve_ivp
from scipy.stats import mode
from sklearn import ensemble, cluster
from sklearn.cluster import KMeans, DBSCAN
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
# Define the Lorenz system of differential equations
def lorenz(t, y, sigma, rho, beta):
    dydt = [sigma * (y[1] - y[0]),
            y[0] * (rho - y[2]) - y[1],
            y[0] * y[1] - beta * y[2]]
    return dydt

# Set the parameters
sigma = 10.0
rho = 28.0
beta = 8.0 / 3.0

# Set the initial conditions
initial_conditions = [1.0, 0.0, 20.0]

# Set the time span for integration
t_span = (0, 120)
t_eval = np.linspace(t_span[0], t_span[1], 12000)

# Solve the system of differential equations
time_series = solve_ivp(lorenz, t_span, initial_conditions, args=(sigma, rho, beta), t_eval=t_eval)

# Plot the Lorenz attractor
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot(time_series.y[0], time_series.y[1], time_series.y[2], lw=0.5)
# ax.set_xlabel('X-axis')
# ax.set_ylabel('Y-axis')
# ax.set_zlabel('Z-axis')
# ax.set_title('Lorenz Attractor')
# plt.savefig("Lorenz_attractor")
# plt.show()
#
# fig = plt.figure(figsize=(15, 4))  # Adjust the figsize as needed
# plt.plot(time_series.t, time_series.y[0], label='X-coordinate')
# plt.xlabel('Time')
# plt.ylabel('X-coordinate')
# plt.title('Lorenz Attractor: X-coordinate vs Time')
# plt.legend()
# plt.savefig("Lorenz_projection")
# plt.show()
#

te = TakensEmbedding()
sliced_time_series = time_series.y[:, :1000]
embedding = te.fit_transform(sliced_time_series)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(embedding[0], embedding[1], embedding[2], lw=1)
ax.set_title('3D Delay Embedding of Time Series')
ax.set_xlabel('x(t)')
ax.set_ylabel('x(t + τ)')
ax.set_zlabel('x(t + 2τ)')
plt.show()

embedding = embedding.reshape(-1, 3)

mapper = km.KeplerMapper(verbose=1)
lens1 = mapper.fit_transform(embedding)

projector = PCA(n_components=1)
lens2 = projector.fit_transform(embedding)

projector = ensemble.IsolationForest(random_state=42)
projector.fit(embedding)
lens3 = projector.decision_function(embedding)

lens = np.c_[lens1, lens3]

fig, axs = plt.subplots(1, 2, figsize=(9,4))
axs[0].scatter(lens1,lens2,alpha=0.3)
axs[0].set_xlabel('L^2-Norm')
axs[0].set_ylabel('PCA')
axs[1].scatter(lens1,lens3,alpha=0.3)
axs[1].set_xlabel('L^2-Norm')
axs[1].set_ylabel('IsolationForest')
plt.tight_layout()
plt.show()

nbrs = NearestNeighbors(n_neighbors=5).fit(embedding)
distances, _ = nbrs.kneighbors(embedding)
eps = np.mean(distances[:, 4])
print(f"Computed eps for DBSCAN: {eps}")

cover = km.Cover(n_cubes=15, perc_overlap=0.2)
clusterer = DBSCAN(eps=5, min_samples=3)

graph = mapper.map(
    lens,
    embedding,
    cover=cover,
    clusterer=clusterer
)

mapper.visualize(
    graph,
    path_html="mapper.html",
)

