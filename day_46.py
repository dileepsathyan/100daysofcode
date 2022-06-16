import matplotlib
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set()


# CREDIT CARD FRAUD DETECTION


# Import the dataset.
df = pd.read_csv('/Users/dileepsathyan/Documents/GitHub/datasets/credit_card.csv')
print(df.head())
print(df.info())
print(df.describe())

cols = df.columns.to_list()
cols = cols[1:-1]
print(cols)

fig = plt.figure(figsize = (14, 9))
# i = 1
# for col in cols:
#     plt.subplot(5, 6, i)
#     plt.plot(df[col])
#     while i == 29:
#         break
#     else:
#         i += 1
# plt.tight_layout()
# plt.show()