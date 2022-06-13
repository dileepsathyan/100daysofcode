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


