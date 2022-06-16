import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import sklearn


# CREADIT CARD FRAUD DETECTION


# Import the dataset.
df = pd.read_csv('/Users/dileepsathyan/Documents/GitHub/datasets/credit_card.csv')
# print(df.head())
# print(df.info())
# print(df.describe())

cols = df.columns.to_list()

fig = plt.figure(figsize = (12, 10))
for col in cols:
    i = 0
    plt.subplot(5, 6, i+1)
    plt.plot(df[col])
    while i == 29:
        break
    else:
        i += 1
plt.show()