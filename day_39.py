import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn import metrics
from sklearn.cluster import KMeans


# MALL CUSTOMER DATA CLUSTERING USING KMEANS ALGORITHM

df = pd.read_csv("/Users/dileepsathyan/Documents/GitHub/datasets/mall_customers.csv")
print(df.head())


# Create a pairplot using Seaborn to visualize the relationships among variables
sns.pairplot(df)
plt.show()


# From the pair plot, the below points are clearly visible
# 1. Age has a clear impact on the Spending Score. Age < 40 spend more than the elder.
# 2. Anmual income can be used to segment the customer data in clear 5 categories. However, we have to reconfirm the same using the ELBOW and SILHOUETTE methods before clustering.


# Prepare the dataset for clustering.
df_cluster = df.replace({'Gender': {'Male': 1, 'Female': 0}})
print(df_cluster.head())


# Check the optimal number of clusters using ELBOW method.

attempts = range(1, 9)
wss = []
for k in attempts:
    model1 = KMeans(n_clusters= k, init='k-means++')
    model1.fit(df_cluster)
    wss_iter = model1.inertia_
    wss.append(wss_iter)


df_elbow_scores = pd.DataFrame({'clusters': attempts, 'wss': wss})
print(df_elbow_scores)


# Plot the wss scores of each k value to see the optimal number of clusters.
sns.scatterplot(df_elbow_scores.clusters, df_elbow_scores.wss)
plt.show()



# From the scatterplot, it might be good to consider 4 or 5 clusters, which we will figure out using Silhouette method below.

for k in range(3,9):
    kmeans_silh = KMeans(n_clusters= k, init='k-means++', random_state=200)
    kmeans_silh.fit(df_cluster)
    labels = kmeans_silh.labels_
    silh_score = metrics.silhouette_score(df_cluster, labels, metric='euclidean', 
                                        sample_size=200, random_state=200)
    print('Silhouette score for '+ str(k) + ' clusters: '+ str(silh_score))


# 5 clusters has a slightly higher Silhouette score than 4 clusters. So we will use the same in the final model and use it for prediction.


# Create the final model with 5 clusters.

kmeans_final = KMeans(n_clusters= 5, init='k-means++')
kmeans_final.fit(df_cluster)

print(kmeans_final.cluster_centers_)


df_cluster['clusters'] = kmeans_final.labels_

print(df_cluster.head(10))