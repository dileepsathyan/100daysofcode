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

