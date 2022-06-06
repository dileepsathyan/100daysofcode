from cgitb import reset
from pyexpat import model
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


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
# sns.distplot(df.bmi)
# plt.title('BMI Distribution')
# plt.show()


################################################

# Region Distribution

# plt.figure(figsize=(6,5))
# sns.countplot(df.region)
# plt.title('Region Distribution')
# plt.show()


region_and_charges = pd.DataFrame(df.groupby(['sex', 'region'])['charges'].agg([np.mean, np.std])).reset_index()
# print(region_and_charges)



# Client distribution on number of children.
# plt.figure(figsize=(6,5))
# sns.countplot(df.children)
# plt.title('Children Distribution')
# plt.show()

children_and_charges = pd.DataFrame(df.groupby(['sex', 'children'])['charges'].agg([np.mean, np.std])).reset_index()
# print(children_and_charges)



# Find correlation for price among variables.
# sns.heatmap(df.corr(), annot=True, cmap='BrBG', cbar=True)
# plt.show()



# Prepare the dataset for the categorical values.
# print(df.head())


df.replace({'sex': {'female': 0, 'male': 1}}, inplace=True)
df.replace({'smoker': {'no': 0, 'yes': 1}}, inplace=True)
df.replace({'region': {'southeast': 0, 'southwest': 1,
                        'northeast': 2, 'northwest': 3}}, inplace=True)
# print(df.head())

y = df['charges']
X = df.drop(columns='charges', axis=1)

print(y.head())
print(X.head())


# Separate the train and test datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state=1)


# Create a model and fit it

model = LinearRegression()
model.fit(X_train, y_train)


# Predict the results using the model
y_pred = model.predict(X_test)


# Find the MSE and r2 value
mse = mean_squared_error(y_test, y_pred)
r2_train = r2_score(y_train, model.predict(X_train))
r2_test = r2_score(y_test, y_pred)

print(f'Coefficient Values or Slope : {model.coef_}')
print(f'Intercept Value: {model.intercept_}')
print(f'Mean Squared Error: {mse}')

print(f'R Squared Value within train data: {r2_train}')
print(f'R Squared Value on test data: {r2_test}')