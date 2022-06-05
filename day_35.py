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
# plt.figure(figsize=(18,5))

# plt.subplot(1, 3, 1)
# sns.countplot(df.sex)
# plt.title('Gender Distribution')

# plt.subplot(1, 3, 3)
# sns.countplot(df.smoker)
# plt.title('Smoker / Non Smoker Distribution')
# plt.show()



# Age distribution
# plt.figure(figsize=(15,5))
# sns.countplot(df.age)
# plt.title('Age Distribution')
# plt.show()



# Check the age & price distribution.
# plt.figure(figsize=(15,5))
# sns.boxplot(df.age, df.charges)
# plt.show()


# Calculate the mean price for each age.
mean_charge_for_age = pd.DataFrame(df.groupby(['age'])['charges'].mean().reset_index())
# print(mean_charge_for_age.head())


# Plot the mean price per age
# plt.figure(figsize=(10,5))
# sns.lineplot(x = mean_charge_for_age.age, y=mean_charge_for_age.charges, color='r')
# plt.show()


# Plot BMI distribution
sns.distplot(df.bmi)
plt.title('BMI Distribution')
plt.show()