from typing import Any
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from datetime import datetime as dt
from sklearn import metrics
from sklearn.cluster import KMeans


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


df3 = pd.DataFrame(df.groupby(['Description'])['Quantity'].sum()).reset_index()
print(df3.head())


sns.barplot(x = 'Description', y = 'Quantity', data=df3)
plt.show()