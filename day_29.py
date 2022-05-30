import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# CAR PRICE PREDICTION USING LINEAR REGRESSION MODELS.


# Import the dataset.
df = pd.read_csv("/Users/dileepsathyan/Documents/GitHub/datasets/car_price_prediction.csv")
# print(df.head())



# Do some EDA on the dataset before working on the models.
# First, get the gist of the dataset
# print(df.info())


# View all the columns in the dataset
# print(df.columns)


# View the size of the dataset
# print(df.shape)


# Get the complete stats of the dataset using .describe() method.
# print(df.describe())



# DATA CLEANING
# CarName field in the dataset contains both the Company Name followed by the model name. Lets split them into 2 columns.
# print(df['CarName'].unique())


# CompanyName = df['CarName'].apply(lambda x: x.split(' ')[0])
# df.insert(3, 'CompanyName', CompanyName)
# df['CarName'] = df['CarName'].apply(lambda x: x.split(' ', maxsplit=1)[1:])
# df['CompanyName'] = df['CompanyName'].str.lower()

# print(df['CompanyName'].unique())


# The company names need some spelling corrections.
# Define a function that replaces the names with correct spelling.

# def correct_names(wrong_name, correct_name):
#     df['CompanyName'].replace(wrong_name, 
#                               correct_name, 
#                               inplace=True)



# Call the function to replace with the correct names.
# correct_names('maxda', 'mazda')
# correct_names('porcshce', 'porsche')
# correct_names('toyouta', 'toyota')
# correct_names('vokswagen', 'volkswagen')
# correct_names('vw', 'volkswagen')

# print(df['CompanyName'].unique())