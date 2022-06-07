import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans


# Create a dataset using make_blobs()

data_points = make_blobs(100, n_features=2, centers=3)

df = pd.DataFrame(data_points[0], columns=['feat_1', 'feat_2'])
# print(df.head())


# Create a model and fit it
kmeans = KMeans(n_clusters=3)
kmeans.fit(df)

print(kmeans.cluster_centers_)

df['clusters'] = kmeans.labels_

print(df.head(10))

print(df.clusters.value_counts())


# sns.scatterplot(df.feat_1, df.feat_2, hue=df.clusters)
# plt.show()


# Optimising the k-value (number of clusters for a dataset)

# There are 2 methods used to optimise the number of clusters for a dataset, which are,

# ---- 1. ELBOW method (using WSS SCORE: Within-Cluster-Sum-of-Squares). By checking the compactness within a cluster.






# ---- 1. SILHOUETTE method

