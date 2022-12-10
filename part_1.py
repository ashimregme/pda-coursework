from __future__ import division
import pandas as pd
import random as rand
import matplotlib.pyplot as plt
import seaborn as sns

# 2. Data Transformation and evaluation
# --------------------------------------------------------------------------------------


def yes_no_to_1_0(val):
    """
This function takes one argument, 'val' and transforms it to 1 or 0.
    """
    if val == 'yes':
        return 1
    elif val == 'no':
        return 0
    else:
        return val


def to_ordinal(dataframe, *column_names):
    """
This function takes two arguments (dataframe & column_name) and
creates a new column by assigning ordinal number based on
cases in the dataset.
    """
    for column_name in column_names:
        dataframe[column_name +
                  '_ordinal'], _ = dataframe[column_name].factorize()


# 2. a)
# read data from bank.csv file and convert 'housing',
# 'default', 'loan' and 'y' columns from yes/no to 1/0.
df = pd.read_csv('bank.csv', converters={
    'housing': yes_no_to_1_0,
    'default': yes_no_to_1_0,
    'loan': yes_no_to_1_0,
    'y': yes_no_to_1_0
})

# 2. b)
# create new ordinal columns
to_ordinal(df, 'job', 'education', 'marital', 'contact', 'month', 'poutcome')

# 2. c)
# create new 'age_category' column to categorize age of the clients
df['age_category'] = pd.cut(df['age'], [18, 19, 25, 30, 35, 40, 49, 59, 69, 79, float(
    "inf")], labels=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# 2. d)
print('The median age of the clients is: ', df['age'].median())

# 2. e)
print('The total number of clients whose job title is "housemaid" is: ',
      df['job'].eq('housemaid').sum())

# 2. f)
print("The success rate of the previous marketing campaign is: ",
      df['poutcome'].eq('success').sum() / df['poutcome'].count() * 100, "%")

# 2. g)
print("The average age of clients who are entrepreneurs is: ",
      df[df['job'] == 'entrepreneur']['age'].mean())

# 2. h)
df['contact'] = df['contact'].apply(lambda row: rand.choice(
    ['cellular_unknown', 'telephone_unknown']) if row == 'unknown' else row)

# 2. i)
df['duration_minutes'] = df['duration'] / 60

print(df)

# 3) Initial Data Analysis
# --------------------------------------------------------------------------------------


def display_summary_stats(dataframe, *column_names):
    """
This function take two arguments and display summary statistics
like sum, mean, median, standard deviation, maximum and minimum
of multiple columns.
    """
    for column_name in column_names:
        print('The sum of ', column_name, ' is ', dataframe[column_name].sum())
        print('The mean of ', column_name, ' is ',
              dataframe[column_name].mean())
        print('The median of ', column_name, ' is ',
              dataframe[column_name].median())
        print('The std of ', column_name, ' is ', dataframe[column_name].std())
        print('The max of ', column_name, ' is ', dataframe[column_name].max())
        print('The min of ', column_name, ' is ',
              dataframe[column_name].min(), end='\n\n')


# 3) a)
display_summary_stats(df, 'age', 'balance', 'duration',
                      'campaign', 'duration_minutes')

# Calculate the correlations between the "age", "balance", "duration", "campaign" and "duration_minutes" columns
print(df[['age', 'balance', 'duration',
          'campaign', 'duration_minutes']])
corr = df[['age', 'balance', 'duration',
           'campaign', 'duration_minutes']].corr()

# Create a heatmap visualization of the correlation values
sns.heatmap(corr, annot=True)

# 4. Data Exploration and Visualization
# --------------------------------------------------------------------------------------

# 4. a)
corr = df.corr(numeric_only=True).loc[['y'], :].drop('y', axis=1)
sns.heatmap(corr, annot=True)

# 4. b)
df[['age', 'balance', 'duration']].hist()
df[['age', 'balance', 'duration']].plot.box()

# 4. c)
subscription_bar = df[['y', 'job']].loc[df['y'] == 1].groupby('job').count().plot.bar(
    title='Number of clients grouped by the type of job who subscribed a term deposit'
)
subscription_bar.set_xlabel('Type of Job')
subscription_bar.set_ylabel('Number of clients')

# 4. d)
balance_bar = df[['age_category', 'balance']].groupby('age_category').mean().plot.bar(
    title='Balance by age category'
)
balance_bar.set_xlabel('Age category')
balance_bar.set_ylabel('Balance')

plt.show()
