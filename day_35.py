import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# MEDICAL INSURANCE PRICE PREDICTION


# Import the dataset
df = pd.read_csv("/Users/dileepsathyan/Documents/GitHub/datasets/medical_insurance.csv")

# print(df.head())
# print(df.shape)
# print(df.info())
# print(df.describe())



# Plot the Gender and Smoker distribution among the dataset.
# plt.figure(figsize=(10,5))

# plt.subplot(1, 2, 1)
# sns.countplot(df.sex)
# plt.title('Gender Distribution')

# plt.subplot(1, 2, 2)
# sns.countplot(df.smoker)
# plt.title('Smoker / Non Smoker Distribution')
# plt.show()


