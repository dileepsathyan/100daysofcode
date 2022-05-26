# LINEAR REGRESSION USING SCIKIT-LEARN IN PYTHON

import numpy as np
from sklearn.linear_model import LinearRegression


# Lets define the input x and response y.
# .reshape() makes the input variables 2-D (1 column vs many rows)

x = np.array([21, 24, 27, 30, 33, 36, 39]).reshape((-1, 1))
y = np.array([4, 7, 10, 8, 12, 11, 13])
# print(x)
# print(y)


# Create a linear regression model and fit it using the existing data.
model = LinearRegression()
model.fit(x, y)


# Once the model is fit, we can get the results such as R-Squared value, Intercept & Co-efficients

# Find the R-Squared value
r_sq = model.score(x, y)
print(f"R-Squared Value : {r_sq}")


# Find the Intercept
interc_val = model.intercept_
print(f"Intercept Value : {interc_val}")


# Find the Slope or Co-efficient value
slope = model.coef_
print(f"Slope or Co-eff Value : {slope}")


# Understanding the results:

# Intercept of -3.928 is the y value when the x is zero.
# Slope / co-eff value represents the y value increases by 0.44 units for 1 unit increase in x value.

