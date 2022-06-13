from random import random
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


# WINE DATA CLUSTERING

# Import the dataset.
df = pd.read_csv('/Users/dileepsathyan/Documents/GitHub/datasets/wine_clustering.csv')

# Analyse the dataset
print(df.head())
print(df.info())
print(df.describe())

# Check the histogram of the dataframe fields.
# df.hist(figsize=(10,10))
# plt.show()


# Find the correlation among the fields.
# plt.figure(figsize=(10,8))
# sns.heatmap(df.corr(), annot=True, cmap='BrBG', cbar=True)
# plt.show()



# Find the relationship using pairplot.
# sns.pairplot(df)
# plt.show()



# Data Preprocessing using StandardScaler.
# scaler = StandardScaler()
# scaled_data = scaler.fit_transform(df)
# df_scaled = pd.DataFrame(scaled_data, columns=['Alcohol', 'Malic_Acid', 'Ash', 'Ash_Alcanity', 'Magnesium',
#                                                 'Total_Phenols', 'Flavanoids', 'Nonflavanoid_Phenols',
#                                                 'Proanthocyanins', 'Color_Intensity', 'Hue', 'OD280', 'Proline'])
# # print(df_scaled.head())


# ELBOW Method: identify optimal number of clusters.
# attempts = range(1, 9)
# wss = []
# for k in attempts:
#     model_elbow = KMeans(n_clusters= k, init='k-means++')
#     model_elbow.fit(df_scaled)
#     wss_iter = model_elbow.inertia_
#     wss.append(wss_iter)

# df_wss = pd.DataFrame({'clusters': attempts, 'wss': wss})
# print(df_wss)


# Plot the Within Cluster Sum of Square values to find the optimal K value.
# sns.scatterplot(df_wss.clusters, df_wss.wss)
# plt.show()



# SILHOUETTE Method: Optimal K value.
# for k in range(2, 9):
#     model_sil = KMeans(n_clusters= k, init='k-means++')
#     model_sil.fit(df_scaled)
#     label = model_sil.labels_
#     sil_score = metrics.silhouette_score(df_scaled, label, metric='euclidean', random_state=50)
#     print('Silhouette Score for '+ str(k) + ' clusters = ' + str(sil_score))

# Both ELBOW & SILHOUETTE Methods confirm the optimal K value as 3 clusters.



# Build the final model with 3 clusters.
# model = KMeans(n_clusters= 3, init='k-means++')
# model.fit(df_scaled)
# df['cluster'] = model.labels_
# print(df.head())



# sns.set(rc={'figure.figsize':(6,6)})
# sns.pairplot(df, hue='cluster')
# plt.show()
