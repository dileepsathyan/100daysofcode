# LINEAR REGRESSION USING SCIKIT-LEARN IN PYTHON

import numpy as np
from sklearn.linear_model import LinearRegression


# Lets define the input x and response y.
# .reshape() makes the input variables 2-D (1 column vs many rows)

x = np.array([21, 24, 27, 30, 33, 36, 39]).reshape((-1, 1))
y = np.array([4, 6, 8, 10, 12, 14, 16])

# print(x)
# print(y)