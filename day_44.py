import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder
from kmodes.kmodes import KModes

# K-MODES CLUSTERING ON BANK CUSTOMER CATEGIRUCAL DATA.

# Import the dataset.
df = pd.read_csv('/Users/dileepsathyan/Documents/GitHub/datasets/bank_marketing.csv')

# Analyse the dataset
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
print(df.info())

