import numpy as np
import pandas as pd
import statsmodels.api as sm


# LINEAR REGRESSION USING STATSMODELS.

# Statsmodel is preferred to analyse Linear Regression when more detailed results are required. The process is similar to that of SKLEARN.

# First import the datasets & define the variables.
file = pd.read_csv("/Users/dileepsathyan/Documents/GitHub/datasets/Fish.csv")
file = file[file['Species']=='Bream']

x = file[['Length', 'Height', 'Width']]
y = file['Weight']


# Now create a model and fit it to get the results
model1 = sm.OLS(y, x)
results1 = model1.fit()


# Print the results
# print(results1.summary())


# print(f'R-squared value :{results1.rsquared}')
print(f'Adjusted R-squared value :{results1.rsquared_adj}')
print(f'Coefficients :{results1.params}')


# Predict the results: Method1: .fittedvalues
print(results1.fittedvalues)


# Predict the results: Method2: .predict()
print(results1.predict(x))