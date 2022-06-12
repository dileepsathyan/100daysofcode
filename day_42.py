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
# print(df.head())
# print(df.info())
# print(df.describe())


# Process the valus in the dataset using StandardScaler
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)
df_scaled = pd.DataFrame(scaled_data, columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
# print(df_scaled.head())


# ELBOW Method: Find the optimal K value
attempts = range(1,10)
wss = []
for k in attempts:
    model_elbow = KMeans(n_clusters= k, init='k-means++')
    model_elbow.fit(df_scaled)
    wss_iter = model_elbow.inertia_
    wss.append(wss_iter)

df_wss = pd.DataFrame({'cluster': attempts, 'wss': wss})
# print(df_wss)


sns.scatterplot(x=df_wss['cluster'], y=df_wss['wss'])
plt.show()

# Looks like 5 clusters will be good for this dataset but we will reconfirm the same using Silhouette method.


# SILHOUETTE Method: Find the optimal KK value
for k in range(2, 7):
    model_sil = KMeans(n_clusters= k, init='k-means++')
    model_sil.fit(df_scaled)
    label = model_sil.labels_
    sil_score = metrics.silhouette_score(df_scaled, label, metric='euclidean', sample_size=100)
    print('Silhouette Score for '+ str(k) + ' clusters = ' + str(sil_score))

