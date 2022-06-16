import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import sklearn


# CREADIT CARD FRAUD DETECTION


# Import the dataset.
df = pd.read_csv('/Users/dileepsathyan/Documents/GitHub/datasets/credit_card.csv')
print(df.head())
print(df.info())
print(df.describe())

