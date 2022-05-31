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


CompanyName = df['CarName'].apply(lambda x: x.split(' ')[0])
df.insert(3, 'CompanyName', CompanyName)
df['CarName'] = df['CarName'].apply(lambda x: x.split(' ', maxsplit=1)[1:])
df['CompanyName'] = df['CompanyName'].str.lower()

# print(df['CompanyName'].unique())


# The company names need some spelling corrections.
# Define a function that replaces the names with correct spelling.

def correct_names(wrong_name, correct_name):
    df['CompanyName'].replace(wrong_name, 
                              correct_name, 
                              inplace=True)



# Call the function to replace with the correct names.
correct_names('maxda', 'mazda')
correct_names('porcshce', 'porsche')
correct_names('toyouta', 'toyota')
correct_names('vokswagen', 'volkswagen')
correct_names('vw', 'volkswagen')

# print(df['CompanyName'].unique())

######################################################################################################

# Data Visualisation using matplotlib library

# plt.figure(figsize=(8,4))

# plt.subplot(1, 2, 1)
# plt.hist(df['price'], 10)
# plt.title('Car Price Distribution')

# plt.subplot(1, 2, 2)
# plt.boxplot(df['price'])
# plt.title('Car Price Spread')
# plt.show()

# From the plot, its clear that most of the car prices are below 15,000 and the plot itself is right skewed.


# Check the values of car prices by percentiles
# print(df['price'].describe(percentiles= [0.25, 0.5, 0.75, 0.9, 1]))

# There is huge difference between the mean and median of the distribution.
# 90% of the values are below 22563 which shows high variance in the car prices when compared to the max price of 45400.


# Visualizing the categorical values in the dataframe

# CompanyName
# df['CompanyName'].value_counts().plot(kind='barh')
# plt.title('Company Names')
# plt.show()

# Toyota seems to be the favorite car for the customer base.

# Fuel Types
# df['fueltype'].value_counts().plot(kind='barh')
# plt.title('Fuel Types')
# plt.show()

# Gas fuelled cars are considerably higher than that of Diesel fuelled cars.

# Car Types
df['carbody'].value_counts().plot(kind='barh')
plt.title('Car Types')
plt.show()

# Sedan, followed by hatchback, seems to lead the among all the car types.


