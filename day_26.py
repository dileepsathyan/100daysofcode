from pyexpat import model
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# MULTIPLE LINEAR REGRESSION

# In most of the cases, there are multiple variable responsible for a change, which can be tracked using Multiple Linear Regression.

# The process is similar to the Simple Linear Regression that we went through yesterday. The difference is only that the x variable will have more than 1 columns this time.


# Load the sample dataset
file = pd.read_csv("/Users/dileepsathyan/Documents/GitHub/datasets/Fish.csv")


# Prepare the dataset
file = file[file['Species']=='Bream']
print(file.head())


# Define the variables
x = file[['Length', 'Height', 'Width']]
y = file['Weight']


# Create a model and fit the model.
model1 = LinearRegression()
model1.fit(x, y)


# Get the results: Slope, Intercept & Co-eff values
r_sq1 = model1.score(x, y)
print(f'R-Squared value: {r_sq1}')
print(f'Slope or Co-eff value: {model1.coef_}')
print(f'Intercept value: {model1.intercept_}')


# Predict the y_values
predicted_y = model1.predict(x)
print(predicted_y)


# Verifying the intercepts & slopes from the model.
pred_y = model1.intercept_ + np.sum(model1.coef_ * x, axis=1)
print(f"Verifying the above reults here: {pred_y}")