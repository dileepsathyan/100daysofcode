from typing import Any
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from datetime import datetime as dt
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


# ONLINE RETAIL DATA CLUSTERING


# Import online retail dataset
df = pd.read_csv('/Users/dileepsathyan/Documents/GitHub/datasets/online_retail.csv', encoding= 'unicode_escape')


# Understand the datapoints and dataset.
# print(df.head(10))
# print(df.describe())
# print(df.info())


# Drop the NULL values from the dataset.
df = df.dropna()
# print(df.info())


# Convert the InvoiceDate column to the right datatype.
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], format='%d-%m-%Y %H:%M')


# Add new column as Amount of purchase
df['Amount'] = df['UnitPrice'] * df['Quantity']
# print(df.head(10))


# Check the loyalty of the Customers.
df1 = df.groupby(['CustomerID'])['InvoiceNo'].count().reset_index()
df1.rename({'InvoiceNo':'Frequency'}, axis=1, inplace=True)
# print(df1.head())


# Merge the 2 dataframes
df = df.merge(df1, on='CustomerID', how='left')
# print(df.head())


# Calculate the recency of each Customer.
# Find the latest invoice date in the dataframe.
max_date = max(df['InvoiceDate'])


# Create a new fiels with the difference between the first InvoiceDate for each user and the latest date in the dataframe.
df['Recency'] = (max_date - df['InvoiceDate']).dt.days


# Group the Customers to find the first InvoiceDate for each ID.
df2 = df.groupby(['CustomerID'])['Recency'].min().reset_index()
df2.rename({'Recency':'RecencyDays'}, axis=1, inplace=True)
# print(df2.head())


# Merge the dataframes on CustomerID to get the Recency field onto the original df.
df = df.merge(df2, on='CustomerID', how='left')
df.drop(columns=['Recency'], axis=1, inplace=True)
df.rename({'RecencyDays':'Recency'}, axis=1, inplace=True)
# print(df.head(10))

############################################################################################################################


# Subset the dataframe for clustering.
df_final = df[['Amount', 'Frequency', 'Recency']]

scaler = StandardScaler()
df_final_scaled = scaler.fit_transform(df_final)
# print(df_final_scaled.shape)

df_final_scaled = pd.DataFrame(df_final_scaled, columns=['Amount', 'Frequency', 'Recency'])
print(df_final_scaled.head())





# Find the optimal number of clusters

# ELBOW Method: using Within-Cluster-Sum-Of-Squares Scores
# attempts = range(1, 10)
# wss = []
# for k in attempts:
#     model_elbow = KMeans(n_clusters=k, init='k-means++')
#     model_elbow.fit(df_final)
#     wss_iter = model_elbow.inertia_
#     wss.append(wss_iter)


# df_wss = pd.DataFrame({'clusters': attempts, 'wss': wss})
# print(df_wss)

# Plot the wss scores to find the optimal k value.
# sns.scatterplot(df_wss.clusters, df_wss.wss)
# plt.show()

# From the plot, we are not able to decide between 6 or 7 number of clusters. So we will clarify it with Silhouette method.


# SILHOUETTE Method: 
# for k in range(3, 10):
#     model_silh = KMeans(n_clusters=k, init='k-means++', random_state=200)
#     model_silh.fit(df_final)
#     labels = model_silh.labels_
#     silh_score = metrics.silhouette_score(df_final, labels, metric='euclidean', sample_size=200, random_state=200)
#     print('Silhouette score for '+ str(k) + ' clusters = ' + str(silh_score))

# Its clear from the Silhouette score that, 6 clusters will be ideal for this dataset.


# Build the final model with 6 clusters.
# model_final = KMeans(n_clusters= 6, init='k-means++')
# model_final.fit(df_final)
# df_final['clusters'] = model_final.labels_
# print(df_final.tail(25))


# Group the dataframes to have the cluster numbers for each CustomerID
# print(df.shape)
# df = df.merge(df_final, on=['Amount', 'Frequency', 'Recency'], how='left')
# # print(df.head(20))
# print(df.shape)
