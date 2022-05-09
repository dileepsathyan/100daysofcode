from turtle import title
import pandas as pd
import matplotlib.pyplot as plt

filepath = '/Users/dileepsathyan/Downloads/Personal Stuff/100daysofcode/Churn_Modelling.xls'
df1 = pd.read_csv(filepath)
# print(df1.head())


fig1 = df1['Balance'].plot(kind='hist', figsize=(5,3), title='Balance Summary')
# print(plt.show())

fig2 = plt.barh(df1['EstimatedSalary'], df1['Geography'])
plt.xlim(0,10000)
print(plt.show())
