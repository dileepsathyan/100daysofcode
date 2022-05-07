

from cmath import nan
from traceback import print_tb
import numpy as np
import pandas as pd


dict = {
        'Gender': ['Male', nan, 'Female', nan, 'Female'],
        'Science': [85, nan, 72, 47, 53],
        'Maths': [56, nan, nan, 92, 68],
        'English': [nan, nan, 49, 82, 75]
        }

df1 = pd.DataFrame(dict)
# print(df1)


# Missing Values and handling of missing values


# Check is a NULL value exists or not.
# print(df1.isnull())


# Check the opposite of the above query (find all the non_NULL values)
# print(df1.notnull())


# Fill the null values with a explicit value
# print(df1.fillna('1'))


# Fill the null values with the previous values in the column
# print(df1.fillna(method='ffill'))


# Fill the null values with the next values in the column
# print(df1.fillna(method='bfill'))


# Fill a particular column with an explicit value for the NULL
# df1['Gender'].fillna('Not Specified', inplace=True)
# print(df1)


# Replace the nan values with an explicit number
# df1['Science'].replace(to_replace= np.nan, value= 1)
# print(df1)


# Interpolate missing values using Linear method. 
# Linear method ignore the index and treats the values as equally spaced.
# print(df1.interpolate(method='linear', limit_direction='forward'))


# Drop the rows with at least 1 NULL value
# print(df1.dropna())


# Drop the rows with all NULL values
# print(df1.dropna(how='all'))


# Drop the columns with at least 1 NULL value
dict2 = {
        'Gender': ['Male', nan, 'Female', nan, 'Female'],
        'Science': [85, 86, 72, 47, 53],
        'Maths': [56, nan, nan, 92, 68],
        'English': [nan, nan, 49, 82, 75]
        }
df2 = pd.DataFrame(dict2)
# print(df2)
# print(df2.dropna(axis =1))


























# Concatenating, Merging, and Joining in a data frame
# Summary Analysis, Cross Tabulation, and Pivot