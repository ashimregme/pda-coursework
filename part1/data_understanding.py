from __future__ import division
import pandas as pd
import numpy as np
import random as rand
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('part1/bank.csv')
df[''] = np.arange(1, len(df) + 1)
print(df)

print(df['age'].sort_values())

df['age_category'] = pd.cut(df['age'], [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, float(
    "inf")], labels=['20-25', '25-30', '30-35', '35-40', '40-45', '45-50', '50-55', '55-60', '60-65', '65-70', '70-75', '75-80', 'Above 80'])

print(df[['id', 'poutcome']])
bar = df[['id', 'poutcome']].groupby('poutcome').count().plot.bar(
    title='Age distribution of clients',
)
bar.set_xlabel('Age Category')
bar.set_ylabel('Number of clients')

print(df.groupby(['poutcome'])[''].count().plot(
    kind='pie', title='Summary of outcome', autopct='%1.0f%%'
))

line = df[['', 'duration']].plot.scatter(
    x='duration',
    y='',
    s=1
)
line.set_xticks(range(0, 5400, 300))
plt.show()


# Create a sample dataframe
df = pd.DataFrame({'a': [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6],
                   'b': [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86],
                   'c': [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6],
                   'd': [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]})

# Calculate the correlation between column 'a' and all other columns
corr = df.corr()['a'].drop('a')

# Plot the correlation as a bar plot
corr.plot.bar(title='Correlation between column "a" and other columns',
              xlabel='Columns', ylabel='Correlation coefficient',
              legend=True)

# Show the plot
plt.show()
