import pandas as pd

# Import a csv file using Pandas
df1 = pd.read_csv('/Users/dileepsathyan/Documents/GitHub/datasets/Churn_Modelling.xls')
print(df1)


# Check the size of the DataFrame using 'shape' function
print(df1.shape)


# Check the general stats of the DataFrame using 'info' function
print(df1.info())


# Check the name of all columns in the DataFrame
print(df1.columns)


# View the first 5 rows of a DataFrame
print(df1.head())


# View the first 'n' number of rows
print(df1.head(9))


# View the last 5 rows of a DataFrame
print(df1.tail())


# View the last 'n' number of rows
print(df1.tail(9))


# Add a new column
df1.insert(7, 'BirthYear', 2022-df1['Age'])
print(df1[['CustomerId', 'Age', 'BirthYear']])


# Drop / Delete a column from the DataFrame
df1.drop(columns=['IsActiveMember'])
print(df1.columns)


# Find Unique Values in a column
print(df1['Geography'].unique())


# Count the unique values in a column
print(df1['Geography'].nunique())


# Select certain columns to read
print(df1[['CustomerId', 'Surname', 'Age']])


# Find the most common value in a column
print(df1['Geography'].value_counts())


# Find the SUM of values in a column
print(df1['HasCrCard'].sum())


# Find the Average of values in a column
print(df1['Age'].mean())


# Find the Median of values in a column
print(df1['Age'].median())


# Find the Average of values in a column
print(df1['Age'].mode())


# Find the overall statistics of the DataFrame
print(df1.describe())