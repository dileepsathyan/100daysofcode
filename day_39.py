import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn import metrics
from sklearn.cluster import KMeans


# MALL CUSTOMER DATA CLUSTERING USING KMEANS ALGORITHM

df = pd.read_csv("/Users/dileepsathyan/Documents/GitHub/datasets/mall_customers.csv")

print(df.head())


# Create a pairplot using Seaborn to visualize the relationships among variables
sns.pairplot(df)
plt.show()


# From the pair plot, the below points are clearly visible
# 1. Age has a clear impact on the Spending Score. Age < 40 spend more than the elder.
# 2. Anmual income can be used to segment the customer data in clear 5 categories. However, we have to reconfirm the same using the ELBOW and SILHOUETTE methods before clustering.


