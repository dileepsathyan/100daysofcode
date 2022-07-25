from operator import index
import pandas as pd


df1 = pd.read_csv('/Users/dileepsathyan/Documents/GitHub/datasets/Churn_Modelling.xls')
print(df1.head())


print(df1.info())


# 'Group By' and aggregate values
df2 = df1[['Geography', 'Gender', 'Balance']].groupby(['Geography', 'Gender']).mean()
print(df2)


# 'Group By' and apply multiple aggregate functions
print(df1[['Geography', 'Gender', 'Balance']].groupby(['Geography', 'Gender']).agg(['mean', 'count', 'sum']))


# Creating a subset of the Dataframe based on a condition on a column
print(df1[df1['Geography']=='France'].head())


# Creating a subset using 'isin()' on a column
print(df1[df1['Tenure'].isin([1,2,3])].head(3))


# Reset the index values of a Dataframe
print(df2.reset_index())


# Create a subset of a DataFrame specifying the number of rows using 'sample' function
print(df1[['Geography', 'Gender', 'Balance']].sample(n=6))

# The above method returns new DataFrame with the original index.
# If we have to keep the original indexes and add a new index to it, use below method
print(df1[['Geography', 'Gender', 'Balance']].sample(n=6).reset_index())


# In the above method, if we dont prefer to keep the original indexes,
# we can explicitly mention the same in the function.
print(df1[['Geography', 'Gender', 'Balance']].sample(n=6).reset_index(drop=True))
