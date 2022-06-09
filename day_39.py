from curses import def_shell_mode
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
# sns.pairplot(df)
# plt.show()


# From the pair plot, the below points are clearly visible
# 1. Age has a clear impact on the Spending Score. Age < 40 spend more than the elder.
# 2. Anmual income can be used to segment the customer data in clear 5 categories. However, we have to reconfirm the same using the ELBOW and SILHOUETTE methods before clustering.

df_cluster = df[['CustomerID', 'Age', 'Annual Income (k$)', 'Spending Score (1-100)']]
# print(df_cluster.head())


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

# From the scatterplot, it might be good to consider 4 or 5 clusters, which we will figure out using Silhouette method
