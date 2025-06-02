import kmapper as km
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from gtda.time_series import SingleTakensEmbedding
from kmapper import Cover
from numpy.ma.core import equal
from scipy.stats import mode
from sklearn import ensemble, cluster
from sklearn.cluster import KMeans, DBSCAN
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler, RobustScaler
from sklearn.neighbors import NearestNeighbors

np.random.seed(42)

n_points = 5000  # Number of time points
t = np.linspace(0, 10 * np.pi, n_points)  # Time vector
freq1, freq2 = 1.0, 0.5  # Frequencies of two sinusoidal components
amp1, amp2 = 10, 8  # Amplitudes of sinusoids
noise_amplitude = 0.2  # Amplitude of noise

# Generate cyclic time series (superposition of two sines)
signal = amp1 * np.sin(freq1 * t) + amp2 * np.sin(freq2 * t)

noise = noise_amplitude * np.random.normal(0, 1, n_points)
time_series = signal + noise

plt.figure(figsize=(12, 4))
plt.plot(t, time_series, label='Cyclic Time Series')
plt.title('Synthetic Time Series with Cycles')
plt.xlabel('Time')
plt.ylabel('Value')
plt.grid(True)
plt.legend()
plt.show()

df = pd.DataFrame(time_series, columns=['Value'], index=t)
mapper = km.KeplerMapper(verbose=1)
lens1 = mapper.fit_transform(df, projection="l2norm")
projector = ensemble.IsolationForest(random_state=42)
projector.fit(df)
lens2 = projector.decision_function(df)
lens = np.c_[lens1, lens2]
cover = km.Cover(n_cubes=15, perc_overlap=0.2)
clusterer = DBSCAN(eps=1, min_samples=3)
graph = mapper.map(
    lens,
    df,
    cover=cover,
    clusterer=clusterer
)
mapper.visualize(
    graph,
    custom_tooltips=df['Value'].values,
    color_values=df['Value'].values,
    color_function_name="Value",
    path_html="mapper_time_series_raw.html",
)

te = SingleTakensEmbedding(time_delay=60, dimension=3)
embedding = te.fit_transform(time_series)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(embedding[:, 0], embedding[:, 1], embedding[:, 2], lw=1)
ax.set_title('3D Delay Embedding of Time Series')
ax.set_xlabel('x(t)')
ax.set_ylabel('x(t + τ)')
ax.set_zlabel('x(t + 2τ)')
plt.show()

sliced_time_series = time_series[:2000]
sliced_t = t[:2000]

plt.figure(figsize=(8, 6))
plt.plot(sliced_t, sliced_time_series, c='red', lw=5, label='Sliced Time Series')
plt.plot(t, time_series, c='blue', lw=2, label='Original Time Series')
plt.title('Sliced Time Series with Cycles')
plt.xlabel('Time')
plt.ylabel('Value')
plt.grid(True)
plt.legend()
plt.show()

embedding = te.fit_transform(sliced_time_series)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(embedding[:, 0], embedding[:, 1], embedding[:, 2], lw=1)
ax.set_title('3D Delay Embedding of Time Series')
ax.set_xlabel('x(t)')
ax.set_ylabel('x(t + τ)')
ax.set_zlabel('x(t + 2τ)')
plt.show()

mapper = km.KeplerMapper(verbose=1)
lens1 = mapper.fit_transform(embedding)

projector = PCA(n_components=1)
lens2 = projector.fit_transform(embedding)

projector = ensemble.IsolationForest(random_state=42)
projector.fit(embedding)
lens3 = projector.decision_function(embedding)

lens = np.c_[lens1, lens2]

# fig, axs = plt.subplots(1, 2, figsize=(9,4))
# axs[0].scatter(lens1,lens2,alpha=0.3)
# axs[0].set_xlabel('L^2-Norm')
# axs[0].set_ylabel('PCA')
# axs[1].scatter(lens1,lens3,alpha=0.3)
# axs[1].set_xlabel('L^2-Norm')
# axs[1].set_ylabel('IsolationForest')
# plt.tight_layout()
# plt.show()

cover = km.Cover(n_cubes=15, perc_overlap=0.2)
clusterer = DBSCAN(eps=2, min_samples=3)

graph = mapper.map(
    lens,
    embedding,
    cover=cover,
    clusterer=clusterer
)

mapper.visualize(
    graph,
    path_html="mapper_time_series_takens.html",
)

