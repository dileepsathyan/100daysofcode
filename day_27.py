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



