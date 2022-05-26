# LINEAR REGRESSION USING SCIKIT-LEARN IN PYTHON

import numpy as np
from sklearn.linear_model import LinearRegression


# Lets define the input x and response y.
# .reshape() makes the input variables 2-D (1 column vs many rows)

x = np.array([21, 24, 27, 30, 33, 36, 39]).reshape((-1, 1))
y = np.array([4, 7, 10, 8, 12, 11, 13])
print(x)
print(y)


# Create a linear regression model and fit it using the existing data.
model1 = LinearRegression()
model1.fit(x, y)


# Once the model is fit, we can get the results such as R-Squared value, Intercept & Co-efficients

# Find the R-Squared value
r_sq1 = model1.score(x, y)
print(f"R-Squared Value : {r_sq1}")


# Find the Intercept
interc_val = model1.intercept_
print(f"Intercept Value : {interc_val}")


# Find the Slope or Co-efficient value
slope = model1.coef_
print(f"Slope or Co-eff Value : {slope}")


print('###################')

# Understanding the results:

# Intercept of -3.928 is the y value when the x is zero.
# Slope / co-eff value represents the y value increases by 0.44 units for 1 unit increase in x value.

# Since the response variable y is 1-D in the above example, the intercept is a scalar value & the slope is an array with just 1 variable.

# In case the response variable is 2-D, we will get the Intercept also as an array. Lets verify that in the below example by making both input and response as 2-D.
p = np.array([21, 24, 27, 30, 33, 36, 39]).reshape((-1, 1))
q = np.array([4, 7, 10, 8, 12, 11, 13]).reshape((-1, 1))
print(p)
print(q)

model2 = LinearRegression()
model2.fit(p, q)

r_sq2 = model2.score(p, q)
print(f"R-Squared Value : {r_sq2}")
print(f"Intercept Value : {model2.intercept_}")
print(f"Slope or Co-eff Value : {model2.coef_}")

# In both cases, we got the similar values as result but this time we notice the Intercept also as an array..



# Predicting the response.

# Once we have a satisfactory model, we can use it for predicting the response for a new set of regressors using .predict() method.

