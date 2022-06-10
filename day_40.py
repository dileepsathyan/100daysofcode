import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn import metrics
from sklearn.cluster import KMeans


# ONLINE RETAIL DATA CLUSTERING


# Import online retail dataset
df = pd.read_csv('/Users/dileepsathyan/Documents/GitHub/datasets/online_retail.csv', encoding= 'unicode_escape')



# Understand the datapoints and dataset.
print(df.head(10))
print(df.info())
print(df.describe())


#