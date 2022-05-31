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

# Gas fuelled cars are considerably higher in number than that of Diesel fuelled cars.

# Car Types
# df['carbody'].value_counts().plot(kind='barh')
# plt.title('Car Types')
# plt.show()

# Sedan, followed by hatchback, seems to lead the among all the car types.


import seaborn as sns


# Engine Type
# plt.figure(figsize=(12,6))

# plt.subplot(1,2,1)
# plt.title('Engine Type')
# sns.countplot(df['enginetype'], palette=("Blues_d"))

# plt.subplot(1,2,2)
# plt.title('Engine Type vs Price')
# sns.boxplot(x=df['enginetype'], y=df['price'], palette=("PuBuGn"))

# plt.show()

# ohc engine type is the most liked type.
# ohc and ohcf have the lowest price range.


# Check the average car price among all brands.

# brand_price = df.groupby(['CompanyName'])['price'].mean().sort_values(ascending=False)
# brand_price.plot(kind='barh')
# plt.show()

# Jaguar has the highest average price while the chevrolet is the cheapest among all car brands.


# Check the average car price among fuel types.

# fueltype_price = df.groupby(['fueltype'])['price'].mean().sort_values(ascending=False)
# fueltype_price.plot(kind='barh')
# plt.show()

# Diesel fuelled cars are expensive than Gas fuelled cars, which resonates with the higher sales of Gas fuelled cars.


# Check the average car price among car types.

# carbody_price = df.groupby(['carbody'])['price'].mean().sort_values(ascending=False)
# carbody_price.plot(kind='barh')
# plt.show()

# hatchback and wagon type cars are cheaper in price than that of hardtop and convetible cars.


# Check the number of doors and the price distribution.

plt.figure(figsize=(12,6))

plt.subplot(1,2,1)
plt.title('Door Number')
sns.countplot(df['doornumber'], palette=("plasma"))

plt.subplot(1,2,2)
plt.title('Door Number vs Price')
sns.boxplot(x=df['doornumber'], y=df['price'], palette=("plasma"))

plt.show()

# Number of doors dont seem to have much impact on the price.




# Check the aspiration and the price distribution.

plt.figure(figsize=(12,6))

plt.subplot(1,2,1)
plt.title('Aspiration')
sns.countplot(df['aspiration'], palette=("plasma"))

plt.subplot(1,2,2)
plt.title('Aspiration vs Price')
sns.boxplot(x=df['aspiration'], y=df['price'], palette=("plasma"))

plt.show()

# Looks like aspiration with turbo has higher price range than std.