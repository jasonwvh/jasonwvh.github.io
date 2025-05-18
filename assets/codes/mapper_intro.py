import kmapper as km
import matplotlib.pyplot as plt
import numpy as np
import sklearn
from kmapper import Cover
from sklearn import ensemble, cluster, datasets
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

points, labels = datasets.make_circles(n_samples=2000, noise=0.1, factor=0.3, random_state=42)
fig = plt.figure(figsize=(5, 4))
ax = fig.add_subplot(111)
ax.scatter(points[labels == 0, 0], points[labels == 0, 1], c='blue', s=10, alpha=0.5, label='Label 0')
ax.scatter(points[labels == 1, 0], points[labels == 1, 1], c='green', s=10, alpha=0.5, label='Label 1')
plt.title("2D Circles")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

projector = ensemble.IsolationForest(random_state=42)
projector.fit(points)
lens1 = projector.decision_function(points)

mapper = km.KeplerMapper(verbose=1)
lens2 = mapper.fit_transform(points, projection="l2norm")

projector = PCA(n_components=1)
lens3 = projector.fit_transform(points)

fig, axs = plt.subplots(1, 2, figsize=(9,4))
axs[0].scatter(lens1,lens2,c=labels.reshape(-1,1),alpha=0.3)
axs[0].set_xlabel('IsolationForest')
axs[0].set_ylabel('L^2-Norm lens')
axs[1].scatter(lens1,lens3,c=labels.reshape(-1,1),alpha=0.3)
axs[1].set_xlabel('IsolationForest')
axs[1].set_ylabel('PCA')
plt.tight_layout()
plt.show()

lens = np.c_[lens1, lens2]
G = mapper.map(
    lens,
    points,
    cover=Cover(n_cubes=15, perc_overlap=0.15),
    clusterer=KMeans(n_clusters=2, random_state=42)
)

_ = mapper.visualize(
    G,
    custom_tooltips=labels,
    color_values=labels,
    color_function_name="target",
    path_html="mapper.html",
    X=points,
    lens=lens,
)