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