import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression


# LOGISTIC REGRESSION

# Classification is an area of supervised machine learning that tries to predict which class or category some entity belongs to, based on its features

# The features or variables can take one of two forms:

# 1. Independent variables, also called inputs or predictors, don’t depend on other features of interest (or at least for the purpose of the analysis).
# 2. Dependent variables, also called outputs or responses, depend on the independent variables.


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


# Single-variate logistic regression is the most straightforward case of logistic regression with only one independent variable (or feature).
# Multi-variate logistic regression has more than one input variable.


# Import the dataset which has flag for social_network_ads purchases across different users with their Gender, Age & Income distribution.
file = pd.read_csv("/Users/dileepsathyan/Documents/GitHub/datasets/logistic_regression_dataset.csv")
print(file.head(10))


x = file[['Age']]
y = file['Purchased']


# Create a model and fit it.
model1 = LogisticRegression(solver='liblinear', random_state=0)
model1.fit(x, y)

# random_state is an integer, an instance of numpy.RandomState, or None (default) that defines what pseudo-random number generator to use.
# solver is a string ('liblinear' by default) that decides what solver to use for fitting the model. Other options are 'newton-cg', 'lbfgs', 'sag', and 'saga'.
    # 'liblinear' solver doesn’t work without regularization.
    # 'newton-cg', 'sag', 'saga', and 'lbfgs' don’t support L1 regularization.
    # 'saga' is the only solver that supports elastic-net regularization.

# Get the attributes of the model

# The attribute .classes_ represents the array of distinct values that y takes:
print(model1.classes_)

# Print the intercept and slope
print(f'Intercept: {model1.intercept_}')
print(f'Slope: {model1.coef_}')


# Predicting the reponses.
# Once a model is defined, .predict_proba(), returns the matrix of probabilities that shows the predicted output is equal to zero or one:
result1 = model1.predict_proba(x)
print(result1)

# Interpreting the predicted values.
# each row in the predicted matrix, corresponds to a single observation. The first column is the probability of the predicted output being zero, that is 1 - 𝑝(𝑥). The second column is the probability that the output is one, or 𝑝(𝑥).

# We can get the actual predictions, based on the probability matrix and the values of 𝑝(𝑥), with .predict():
# pred1 = model1.predict(x)
# print(pred1)


# Print the accuracy of the model using .score()
# print(model1.score(x, y))


# Confusion matrix is usually better in comparing the results of the model.
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix


# cm = confusion_matrix(y, model1.predict(x))

# fig, ax = plt.subplots(figsize=(5, 5))
# ax.imshow(cm)
# ax.grid(False)
# ax.xaxis.set(ticks=(0, 1), ticklabels=('Predicted 0s', 'Predicted 1s'))
# ax.yaxis.set(ticks=(0, 1), ticklabels=('Actual 0s', 'Actual 1s'))
# ax.set_ylim(1.5, -0.5)
# for i in range(2):
#     for j in range(2):
#         ax.text(j, i, cm[i, j], ha='center', va='center', color='red')
# plt.show()