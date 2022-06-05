import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# MEDICAL INSURANCE PRICE PREDICTION


# Import the dataset
df = pd.read_csv("/Users/dileepsathyan/Documents/GitHub/datasets/medical_insurance.csv")
# print(df.head())


