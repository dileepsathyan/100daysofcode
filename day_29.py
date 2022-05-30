import numpy as np
import pandas as pd


# HOUSE PRICE PREDICTION.

# Dataset source: https://www.kaggle.com/code/divan0/multiple-linear-regression/data

# Import the King County House Price Dataset (downloaded from Kaggle).
df = pd.read_csv("/Users/dileepsathyan/Documents/GitHub/datasets/kc_house_data.csv")
# print(df.info())


# Have a look at the columns in the dataset.
# print(df.columns)


# Make sure there are no NULL values.
print(df.isnull)