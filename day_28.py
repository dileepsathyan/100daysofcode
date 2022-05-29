import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression


# LOGISTIC REGRESSION

# Classification is an area of supervised machine learning that tries to predict which class or category some entity belongs to, based on its features

# The features or variables can take one of two forms:

# 1. Independent variables, also called inputs or predictors, don’t depend on other features of interest (or at least for the purpose of the analysis).
# 2. Dependent variables, also called outputs or responses, depend on the independent variables.


# Import the dataset which has flag for social_network_ads purchases across different users with their Gender, Age & Income distribution.
file = pd.read_csv("/Users/dileepsathyan/Documents/GitHub/datasets/logistic_regression_dataset.csv")
print(file.head(10))

