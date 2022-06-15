import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder
from kmodes.kmodes import KModes

# K-MODES CLUSTERING ON BANK CUSTOMER CATEGIRUCAL DATA.

# Import the dataset.
df = pd.read_csv('/Users/dileepsathyan/Documents/GitHub/datasets/bank_marketing.csv')
# print(df.head())


# Subset the dataframe only for categorical values.
df = df[['age', 'job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'day_of_week', 'poutcome']]
# print(df.head())


# Convert the age to a categorical variable by binning it into buckets.
df['age_bins'] = pd.cut(df['age'], 
                        [0, 20, 30, 40, 50, 60, 70, 80, 90, 100], 
                        labels=['0-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90', '90-100'])
# print(df.head())


# Drop the original age column.
df.drop(columns=['age'], axis=1, inplace=True)
# print(df.head())


# Find the stats of the resultant dataframe.
# print(df.describe())
# print(df.info())


# Prepare the data using Label Encoder.
encoder = LabelEncoder()
df_enc = df.apply(encoder.fit_transform)
print(df_enc.head())



# Build the model and fir it.
model = KModes(n_clusters=2, init='Cao', n_init=1, verbose=1)
cao_clusters = model.fit_predict(df_enc)
print(cao_clusters)

df_cluster_centroids = pd.DataFrame(model.cluster_centroids_)
df_cluster_centroids.columns = df_enc.columns
print(df_cluster_centroids)


# Update the clusters on the actual dataframe.
df_clusters = pd.DataFrame(cao_clusters)
df_clusters.columns = ['cluster_pred']
df = pd.concat([df, df_clusters], axis=1).reset_index()
print(df.head())


####################################################################################################################################

# Separate the clusters and to see the distribution in them.
df0 = df[df['cluster_pred'] == 0]
df1 = df[df['cluster_pred'] == 1]

print(df0.describe())
print(df1.describe())


# Plot the distribution of job.
plt.subplots(figsize=(15,5))
sns.countplot(df['job'], order=df['job'].value_counts().index, hue=df['cluster_pred'])
plt.show()


# Plot the distribution of marital status.
plt.subplots(figsize=(15,5))
sns.countplot(df['marital'], order=df['marital'].value_counts().index, hue=df['cluster_pred'])
plt.show()


# Plot the distribution of education.
plt.subplots(figsize=(15,5))
sns.countplot(df['education'], order=df['education'].value_counts().index, hue=df['cluster_pred'])
plt.show()


# Plot the similar distribution of fields: default, housing & loan.
fig, axs = plt.subplots(1, 3, figsize=(15,5))
sns.countplot(df['default'], order=df['default'].value_counts().index, hue=df['cluster_pred'], ax=axs[0])
sns.countplot(df['housing'], order=df['housing'].value_counts().index, hue=df['cluster_pred'], ax=axs[1])
sns.countplot(df['loan'], order=df['loan'].value_counts().index, hue=df['cluster_pred'], ax=axs[2])
plt.tight_layout()
plt.show()


# Plot the similar distribution of fields: month & day_of_week.
fig, axs = plt.subplots(1, 2, figsize=(12,5))
sns.countplot(df['month'], order=df['month'].value_counts().index, hue=df['cluster_pred'], ax=axs[0])
sns.countplot(df['day_of_week'], order=df['day_of_week'].value_counts().index, hue=df['cluster_pred'], ax=axs[1])
plt.tight_layout()
plt.show()


# Plot the similar distribution of fields: poutcome & age_bins.
fig, axs = plt.subplots(1, 2, figsize=(12,5))
sns.countplot(df['poutcome'], order=df['poutcome'].value_counts().index, hue=df['cluster_pred'], ax=axs[0])
sns.countplot(df['age_bins'], order=df['age_bins'].value_counts().index, hue=df['cluster_pred'], ax=axs[1])
plt.tight_layout()
plt.show()