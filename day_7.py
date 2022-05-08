from operator import index
from statistics import median
import pandas as pd

df1 = pd.DataFrame(
                {
                'Science': [85, 65, 72, 47, 53],
                'Maths': [56, 73, 66, 92, 68],
                'English': [54, 88, 49, 82, 75]
                })
# print(df1)


df2 = pd.DataFrame(
                {
                'Science': [91, 48],
                'Maths': [75, 82],
                'English': [64, 95]
                })
# print(df2)


# Gather all columns into rows and rename the columns as appropriate
df3_melted = df1.melt().rename(columns={'variable': 'Subject', 'value': 'Marks'})
# print(df3_melted)


# Pivot the rows as columns
# print(df3_melted.pivot(columns='Subject', values='Marks'))


# Concatenate 2 dataframes on their columns (Append the rows of 2 dataframes)
print(pd.concat([df1, df2]))


df4 = pd.DataFrame(
                {
                'Hindi': [43, 32],
                'Biology': [67, 76],
                'Chemistry': [86, 76]
                })
print(df4)

# Concatenate 2 Dataframes horizontally (Append columns of 2 Dataframes)
print(pd.concat([df2, df4], axis=1))


# Sort the Dataframe based on the values in a column.
print(df3_melted.sort_values(by='Marks'))


# Sort values in descending order
print(df3_melted.sort_values(by='Marks', ascending=False))


# Find the MIN and MAX of a column
science_min = df1['Science'].min()
science_max = df1['Science'].max()
print(f'Science Min mark: {science_min} \nScience Max mark: {science_max}')


# Find the MEAN and MEDIAN of a column
science_mean = df1['Science'].mean()
science_median = df1['Science'].median()
print(f'Science Mean mark: {science_mean} \nScience Max mark: {science_median}')


# Merge 2 DataFrames
index_values1 = ['A', 'B', 'C', 'D', 'E']
index_values2 = ['A', 'B']

df1.insert(0, 'Names', index_values1)
df4.insert(0, 'Names', index_values2)

df1.set_index('Names', inplace=True)
df4.set_index('Names', inplace=True)
df5 = pd.merge(df1, df4, how='left', on='Names')
print(df1)
print(df4)
print(df5)