import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from datetime import datetime as dt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import explained_variance_score, mean_squared_error, mean_absolute_error, r2_score


# KING COUNTY HOUSE PRICE PREDICTION

df = pd.read_csv("/Users/dileepsathyan/Documents/GitHub/datasets/kc_house_data.csv")
# print(df.head())
# print(df.describe())
# print(df.info())


# Fix the date column to right format.
df.date = pd.to_datetime(df.date)
df.insert(2, 'year', df.date.dt.year)
df.insert(3, 'month', df.date.dt.month)
df.insert(4, 'day', df.date.dt.day)
# print(df[['date', 'year', 'month', 'day']].head())

# print(df.columns)


# Add a new calculated column: 'age' of the house.
df.insert(5, 'age', (df.year - df.yr_built))

# print(df[['year', 'yr_built', 'age']])


# Check whether the house has been renovated or not.
# print(df.yr_renovated.head(10))


# Since the above field is filled with 0 for those houses which were NOT renovated, lets create a new flag column for renovation.
df['renovated_flag'] = np.where(df.yr_renovated ==0, 0, 1)
# print(df.renovated_flag.head(10))


# Check the correlation among the variables.
corr_fields = ['price', 'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'waterfront', 'view', 
            'condition', 'grade', 'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated', 'zipcode', 
            'lat', 'long', 'sqft_living15', 'sqft_lot15']
# print(df[corr_fields].corr())


# Visualize the correlation values using seaborn
# plt.figure(figsize=(15,8))
# sns.heatmap(df[corr_fields].corr(), vmin=-1, vmax=1, annot=True,cmap='BrBG', fmt=".1g")
# print(plt.show())


# Find the outliers in the fields.

def create_boxplot(dfx, col):
    plt.figure(figsize=(12,5))
    sns.boxplot(dfx[col], dfx['price'])
    plt.title(col)
    plt.show()

# cols = ['bedrooms','bathrooms','floors','waterfront','view','condition','grade']
cols = ['bedrooms']


for col in cols:
    create_boxplot(df, col)



# Remove the outliers.

def remove_outliers_iqr(dfx,col):
    iqr = df[col].quantile(0.75) - df[col].quantile(0.25)
    min_limit = df[col].quantile(0.25)-(1.5*iqr)
    max_limit = df[col].quantile(0.75)+(1.5*iqr)
    outliers = []
    for i in df[col]:
        if i > max_limit or i < min_limit:
            outliers.append(i)
        else:
            pass
    outliers = pd.Series(outliers)
    filtered_df = df[~df[col].isin(outliers)]
    return filtered_df
    

def remove_outliers(dfx, col):
    q1 = dfx[col].quantile(0.25)
    q3 = dfx[col].quantile(0.75)
    iqr = q3 - q1
    min_limit = q1 - iqr
    max_limit = q3 + iqr

    outliers_list = []
    for i in dfx[col]:
        if i < min_limit or i > max_limit:
            outliers_list.append(i)
        else:
            pass
    outliers = pd.Series(outliers_list)
    df_cleaned = dfx[~dfx[col].isin(outliers)]
    return df_cleaned


for col in cols:
    remove_outliers(df, col)


for col in cols:
    create_boxplot(df, col)