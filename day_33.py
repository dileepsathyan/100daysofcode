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

print(df.columns)


# Add a new calculated column: 'age' of the house.
df.insert(5, 'age', (df.year - df.yr_built))

print(df[['year', 'yr_built', 'age']])


# Check whether the house has been renovated or not.
print(df.yr_renovated.head(10))
