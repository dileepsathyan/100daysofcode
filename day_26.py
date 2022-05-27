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



# POLYNOMIAL REGRESSION

# Polynomial regression is very similar to Linear Regression above except the preprocessing required on for the explanatory variable. 
# In this case, we need to convert the x variable to a higher degree polynomial before fitting to a model. Scikit Learn library has the inbuilt feature to do this conversion.

from sklearn.preprocessing import PolynomialFeatures


# Create a transformer to convert the x vars to a 2nd degree polynomial
transformer  = PolynomialFeatures(degree=2, include_bias=False)


# Use the transformer and process the explanatory variables.
# This method also takes the input array and effectively does the same thing as .fit() and .transform() called in that order. It also returns the modified array with the actual values and their squared values.

poly_x = transformer.fit_transform(x)

print(poly_x)


# Now, create a model and fit the values
model2 = LinearRegression.fit(poly_x, y)

