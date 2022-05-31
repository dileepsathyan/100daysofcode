# Pandas is a python library that provides high-performance, easy-to-use data structures such as 
# a series, Data Frame, and Panel for data analysis tools for Python programming language. 
# Moreover, Pandas Data Frame consists of main components, the data, rows, and columns.


import pandas as pd

# Creating a DataFrame (Data Frame is a 2-D data structure, data is stored in rows and columns)

# The Pandas data frame can be created by loading the data from the external, existing storage like 
# a database, SQL, or CSV files. But the Pandas Data Frame can also be created from the lists, dictionary, etc

dict1 = {
        'name': ['Dileep', 'Trinay', 'Sachu', 'Sathyan', 'Latha'],
        'age': [34,3,31,60,55],
        'relationship': ['self', 'son', 'spouse', 'father', 'mother']
        }
df1 = pd.DataFrame(dict1)
#print(df1)


# Importing a csv file as DataFrame.
df2 = pd.read_csv('/Users/dileepsathyan/Downloads/Sample_File.csv')
print(df2)


# Selecting a column in a DataFrame
# In order to select a particular column from a DataFrame, specify the name of the clolumn as below.
print(df1['name'])


# Selecting multiple columns from a DataFrame
print(df1[['name', 'relationship']])


# Selecting a particular row in a DataFrame, using the index_name of the row.
df1_renamed = pd.DataFrame({
                            'name': ['Dileep', 'Trinay', 'Sachu', 'Sathyan', 'Latha'],
                            'age': [34,3,31,60,55],
                            'relationship': ['self', 'son', 'spouse', 'father', 'mother']},
                            index=['a', 'b', 'c', 'd', 'e'])
print(df1_renamed.loc[['a', 'c']])


# Selecting a particular row in a DataFrame, using the index of the row.
print(df1.iloc[[0, 2]])


# Renaming a column in a DataFrame
df1_renamed = df1.rename(columns= {'name': 'NAME',
                                    'age': 'AGE',
                                    'relationship': 'RELATIONSHIP'
                                    })
print(df1_renamed)


# 'Insert' function is an effective way of adding a new column to a DataFrame at the desired location.
df1.insert(2, 'age_doubled', df1['age']*2)
#print(df1)
