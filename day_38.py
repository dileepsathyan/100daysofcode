import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn import metrics
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

#### Run the cluster analysis for 5 times (just for this case) to get the WSS scores and plot them to find the ELBOW point.

attempts = range(1, 6)
# wss = []
# for k in attempts:
#     kmeans_elbow = KMeans(n_clusters= k, init='k-means++')
#     kmeans_elbow.fit(df)
#     wss_iter = kmeans_elbow.inertia_
#     wss.append(wss_iter)

# temp_df = pd.DataFrame({'clusters': attempts, 'wss': wss})
# print(temp_df)


# sns.scatterplot(y=temp_df.wss, x=temp_df.clusters)
# plt.show()



# ---- 1. SILHOUETTE method

#### The Silhouette Coefficient is calculated using the mean intra-cluster distance (a) and the mean nearest-cluster distance (b) for each sample. The Silhouette Coefficient for a sample is (b - a) / max(a, b). To clarify, b is the distance between a sample and the nearest cluster that the sample is not a part of. Note that Silhouette Coefficient is only defined if number of labels is 2 <= n_labels <= n_samples - 1.


# for k in range(2,8):
#     kmeans_silh = KMeans(n_clusters= k, init='k-means++', random_state=200)
#     kmeans_silh.fit(df)
#     labels = kmeans_silh.labels_
#     silh_score = metrics.silhouette_score(df, labels, metric='euclidean', 
#                                         sample_size=200, random_state=200)
#     print('Silhouette score for '+ str(k) + ' clusters: '+ str(silh_score))

