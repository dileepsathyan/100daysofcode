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

# # From the plot, its clear that most of the car prices are below 15,000 and the plot itself is right skewed.


# # Check the values of car prices by percentiles
# # print(df['price'].describe(percentiles= [0.25, 0.5, 0.75, 0.9, 1]))

# # There is huge difference between the mean and median of the distribution.
# # 90% of the values are below 22563 which shows high variance in the car prices when compared to the max price of 45400.


# # Visualizing the categorical values in the dataframe

# # CompanyName
# df['CompanyName'].value_counts().plot(kind='barh')
# plt.title('Company Names')
# plt.show()

# # Toyota seems to be the favorite car for the customer base.

# # Fuel Types
# df['fueltype'].value_counts().plot(kind='barh')
# plt.title('Fuel Types')
# plt.show()

# # Gas fuelled cars are considerably higher in number than that of Diesel fuelled cars.

# # Car Types
# df['carbody'].value_counts().plot(kind='barh')
# plt.title('Car Types')
# plt.show()

# # Sedan, followed by hatchback, seems to lead the among all the car types.


import seaborn as sns


# # Engine Type
# plt.figure(figsize=(12,6))

# plt.subplot(1,2,1)
# plt.title('Engine Type')
# sns.countplot(df['enginetype'], palette=("Blues_d"))

# plt.subplot(1,2,2)
# plt.title('Engine Type vs Price')
# sns.boxplot(x=df['enginetype'], y=df['price'], palette=("PuBuGn"))

# plt.show()

# # ohc engine type is the most liked type.
# # ohc and ohcf have the lowest price range.


# # Check the average car price among all brands.

# brand_price = df.groupby(['CompanyName'])['price'].mean().sort_values(ascending=False)
# brand_price.plot(kind='barh')
# plt.show()

# # Jaguar has the highest average price while the chevrolet is the cheapest among all car brands.


# # Check the average car price among fuel types.

# fueltype_price = df.groupby(['fueltype'])['price'].mean().sort_values(ascending=False)
# fueltype_price.plot(kind='barh')
# plt.show()

# # Diesel fuelled cars are expensive than Gas fuelled cars, which resonates with the higher sales of Gas fuelled cars.


# # Check the average car price among car types.

# carbody_price = df.groupby(['carbody'])['price'].mean().sort_values(ascending=False)
# carbody_price.plot(kind='barh')
# plt.show()

# # hatchback and wagon type cars are cheaper in price than that of hardtop and convetible cars.


# # Check the number of doors and the price distribution.

# plt.figure(figsize=(12,6))

# plt.subplot(1,2,1)
# plt.title('Door Number')
# sns.countplot(df['doornumber'], palette=("plasma"))

# plt.subplot(1,2,2)
# plt.title('Door Number vs Price')
# sns.boxplot(x=df['doornumber'], y=df['price'], palette=("plasma"))

# plt.show()

# # Number of doors dont seem to have much impact on the price.




# # Check the aspiration and the price distribution.

# plt.figure(figsize=(12,6))

# plt.subplot(1,2,1)
# plt.title('Aspiration')
# sns.countplot(df['aspiration'], palette=("plasma"))

# plt.subplot(1,2,2)
# plt.title('Aspiration vs Price')
# sns.boxplot(x=df['aspiration'], y=df['price'], palette=("plasma"))

# plt.show()

# Looks like aspiration with turbo has higher price range than std.

######################################################################################################

# Visualising the numerical variables.


# plt.figure(figsize=(12,10))

# plt.subplot(2,2,1)
# plt.scatter(df['carlength'], df['price'])
# plt.title('Car Length vs Price')
# plt.ylabel('Price')
# plt.xlabel('Car Length')

# plt.subplot(2,2,2)
# plt.scatter(df['carwidth'], df['price'])
# plt.title('Car Width vs Price')
# plt.ylabel('Price')
# plt.xlabel('Car Width')

# plt.subplot(2,2,3)
# plt.scatter(df['carheight'], df['price'])
# plt.title('Car Height vs Price')
# plt.ylabel('Price')
# plt.xlabel('Car Height')

# plt.subplot(2,2,4)
# plt.scatter(df['curbweight'], df['price'])
# plt.title('Curb Weight vs Price')
# plt.ylabel('Price')
# plt.xlabel('Curb Weight')

# plt.show()

# carlength, carwidth & curbweight are positively correlated to the price
# However, carheight doesnt have any relation to its price.


# Feature Engineering.
# Create a new feature called fueleconomy by calcualting 55% of the city mileage and 45% of highway mileage

df['fueleconomy'] = (df['citympg'] * 0.55) + (df['highwaympg'] * 0.45)
# print(df[['CompanyName', 'fueleconomy']])

# Plot the new feature

# plt.figure(figsize=(6,5))

# plt.title('Fuel economy vs Price')
# sns.scatterplot(x=df['fueleconomy'], y=df['price'], hue=df['drivewheel'])
# plt.xlabel('Fuel Efficiency')
# plt.ylabel('Price')

# plt.show()
# plt.tight_layout()

# As suspected, fuel efficiency has a clear negative correlation with the price.


df_final = df[['price', 'fueltype', 'aspiration','carbody', 'drivewheel','wheelbase',
        'curbweight', 'enginetype', 'cylindernumber', 'enginesize', 'boreratio','horsepower', 
        'fueleconomy', 'carlength','carwidth']]

# Convert the categorical variables into dummies before passing on to model.
def dummies(x, dfx):
    temp = pd.get_dummies(dfx[x], drop_first = True)
    dfx = pd.concat([dfx, temp], axis = 1)
    dfx.drop([x], axis = 1, inplace = True)
    return dfx

# Applying the function to the cars_lr

df_final = dummies('fueltype',df_final)
df_final = dummies('aspiration',df_final)
df_final = dummies('carbody',df_final)
df_final = dummies('drivewheel',df_final)
df_final = dummies('enginetype',df_final)
df_final = dummies('cylindernumber',df_final)

# print(df.head())



from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler


# Split the dataframe as 70% for training and 30% for testing.

np.random.seed(0)
df_train, df_test = train_test_split(df_final, train_size = 0.7, test_size = 0.3, random_state = 100)


scaler = MinMaxScaler()
num_vars = ['wheelbase', 'curbweight', 'enginesize', 'boreratio', 
            'horsepower', 'fueleconomy','carlength','carwidth','price']

df_train[num_vars] = scaler.fit_transform(df_train[num_vars])


# Convert the train dataframe into X and Y variables.

X_train = df_train.pop('price')
y_train = df_train

print(f'Train dataframe size: {df_train.shape}')
print(f'Test dataframe size: {df_test.shape}')

# print(X_train)

# Build the model and fit it

# from sklearn.feature_selection import RFE
# from sklearn.linear_model import LinearRegression
# import statsmodels.api as sm 
# from statsmodels.stats.outliers_influence import variance_inflation_factor


# lm = LinearRegression()
# lm.fit(X_train, y_train)
# rfe = RFE(lm, 10)
# rfe = rfe.fit(X_train, y_train)

# x_train_rfe = X_train[X_train.columns[rfe.support_]]
# x_train_rfe.head()


# def build_model(X,y):
#     X = sm.add_constant(X) #Adding the constant
#     lm = sm.OLS(y,X).fit() # fitting the model
#     print(lm.summary()) # model summary
#     return X
    
# def checkVIF(X):
#     vif = pd.DataFrame()
#     vif['Features'] = X.columns
#     vif['VIF'] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
#     vif['VIF'] = round(vif['VIF'], 2)
#     vif = vif.sort_values(by = "VIF", ascending = False)
#     return(vif)


# x_train_new = build_model(x_train_rfe, y_train)