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
# print(df.head())
# print(df.info())
# print(df.describe())

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

print(df.columns)

# Data Preprocessing using StandardScaler.

scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)
df_scaled = pd.DataFrame(scaled_data, columns=['Alcohol', 'Malic_Acid', 'Ash', 'Ash_Alcanity', 'Magnesium',
                                                'Total_Phenols', 'Flavanoids', 'Nonflavanoid_Phenols',
                                                'Proanthocyanins', 'Color_Intensity', 'Hue', 'OD280', 'Proline'])
# print(df_scaled.head())


# ELBOW Method: identify optimal number of clusters.
