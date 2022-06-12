from lib2to3.pytree import HUGE
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


# IRIS DATA SET CLUSTERING USING KMEANS


# Import the dataset
df = pd.read_csv('/Users/dileepsathyan/Documents/GitHub/datasets/iris_dataset.csv')

# Analyse the dataset
print(df.head())
print(df.info())
print(df.describe())


# Process the valus in the dataset using StandardScaler
scaler = StandardScaler()
# scaled_data = scaler.fit_transform(df)
# df_scaled = pd.DataFrame(scaled_data, columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
# print(df_scaled.head())


# ELBOW Method: Find the optimal K value
# attempts = range(1,10)
# wss = []
# for k in attempts:
#     model_elbow = KMeans(n_clusters= k, init='k-means++')
#     model_elbow.fit(df_scaled)
#     wss_iter = model_elbow.inertia_
#     wss.append(wss_iter)

# df_wss = pd.DataFrame({'cluster': attempts, 'wss': wss})
# print(df_wss)


# sns.scatterplot(x=df_wss['cluster'], y=df_wss['wss'])
# plt.show()

# Looks like 3 clusters will be good for this dataset but we will reconfirm the same using Silhouette method.


# Build the final model with 3 clusters
model = KMeans(n_clusters=3, init='k-means++')
model.fit(df_scaled)
df['cluster'] = model.labels_

print(df.head())


# Plot the results to visulaize the clusters.
sns.pairplot(df, hue='cluster')
plt.show()