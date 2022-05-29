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

# The nature of the dependent variables differentiates regression and classification problems. Regression problems have continuous and usually unbounded outputs. An example is when you’re estimating the salary as a function of experience and education level. On the other hand, classification problems have discrete and finite outputs called classes or categories. For example, predicting if an employee is going to be promoted or not (true or false) is a classification problem.

# There are two main types of classification problems:

# 1. Binary or Binomial classification: exactly two classes to choose between (usually 0 and 1, true and false, or positive and negative)
# 2. Multiclass or multinomial classification: three or more classes of the outputs to choose from.

# Binary classification has four possible types of results:

# True negatives: correctly predicted negatives (zeros)
# True positives: correctly predicted positives (ones)
# False negatives: incorrectly predicted negatives (zeros)
# False positives: incorrectly predicted positives (ones)


# Classification Accuracy: 
# The most straightforward indicator of classification accuracy is the ratio of the number of correct predictions to the total number of predictions (or observations). Other indicators of binary classifiers include the following:

# The 'positive predictive value' is the ratio of the number of true positives to the sum of the numbers of true and false positives.
# The 'negative predictive value' is the ratio of the number of true negatives to the sum of the numbers of true and false negatives.
# The 'sensitivity' (aka recall or true positive rate) is the ratio of the number of true positives to the number of actual positives
# The 'specificity' (or true negative rate) is the ratio of the number of true negatives to the number of actual negatives.
