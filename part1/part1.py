from __future__ import division
import numpy as np
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
df = pd.read_csv('part1/bank.csv', converters={
    'housing': yes_no_to_1_0,
    'default': yes_no_to_1_0,
    'loan': yes_no_to_1_0,
    'y': yes_no_to_1_0
})

print(df[['housing', 'default', 'loan', 'y']])

# 2. b)
# create new ordinal columns
to_ordinal(df, 'job', 'education', 'marital', 'contact', 'month', 'poutcome')

print(df[['job', 'job_ordinal']])
print(df[['education', 'education_ordinal']])
print(df[['marital', 'marital_ordinal']])
print(df[['contact', 'contact_ordinal']])
print(df[['month', 'month_ordinal']])
print(df[['poutcome', 'poutcome_ordinal']])

# 2. c)
# create new 'age_category' column to categorize age of the clients
df['age_category'] = pd.cut(
    df['age'],
    [18, 19, 25, 30, 35, 40, 49, 59, 69, 79, float("inf")],
    labels=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
)

print(df[['age', 'age_category']])

# 2. d)
print('The median age of the clients is: ', df['age'].median())

# 2. e)
print('The total number of clients whose job title is "housemaid" is: ',
      df['job'].eq('housemaid').sum())

# 2. f)
print(
    "The success rate of the previous marketing campaign is: ",
    round(df['poutcome'].eq('success').sum() /
          df['poutcome'].count() * 100, 2),
    "%"
)

# 2. g)
print("The average age of clients who are entrepreneurs is: ",
      round(df[df['job'] == 'entrepreneur']['age'].mean(), 2))

# 2. h)
df['contact'] = df['contact'].apply(
    lambda row: rand.choice(
        ['cellular_unknown', 'telephone_unknown']
    ) if row == 'unknown' else row
)
print(df['contact'])

# 2. i)
df['duration_minutes'] = round(df['duration'] / 60, 2)

print(df[['duration', 'duration_minutes']])

# 3) Initial Data Analysis
# --------------------------------------------------------------------------------------


def display_summary_stats(dataframe, *column_names):
    """
This function take two arguments and display summary statistics
like sum, mean, median, standard deviation, maximum and minimum
of multiple columns.
    """
    for column_name in column_names:
        print('The sum of ', column_name, ' is ',
              round(dataframe[column_name].sum(), 2))
        print('The mean of ', column_name, ' is ',
              round(dataframe[column_name].mean(), 2))
        print('The median of ', column_name, ' is ',
              round(dataframe[column_name].median(), 2))
        print('The std of ', column_name, ' is ',
              round(dataframe[column_name].std(), 2))
        print('The max of ', column_name, ' is ', dataframe[column_name].max())
        print('The min of ', column_name, ' is ',
              round(dataframe[column_name].min(), 2), end='\n\n')


# 3) a)
display_summary_stats(
    df,
    'age',
    'balance',
    'duration',
    'campaign',
    'duration_minutes'
)

# Calculate the correlations between the "age", "balance", "duration", "campaign" and "duration_minutes" columns
print(df[['age', 'balance', 'duration',
          'campaign', 'duration_minutes']])
corr = df[[
    'age', 'balance', 'duration', 'campaign', 'duration_minutes'
]].corr()

# Create a heatmap visualization of the correlation values
sns.heatmap(corr, annot=True)

# 4. Data Exploration and Visualization
# --------------------------------------------------------------------------------------
# 4. a)

# Calculate the correlation between column 'y' and all other columns
print(df.drop(columns=['job', 'marital',
                       'education', 'contact', 'month']).columns)
corr = df.drop(columns=[
    'job',
    'marital',
    'education',
    'contact',
    'month',
    'poutcome',
    'duration_minutes',
    'age_category'
]).corr(numeric_only=False)

print(corr['y'])
corr['y'].drop('y').plot.bar(
    title='Correlation with target variable',
    xlabel='Other variables',
    ylabel='y',
    legend=False
)
# 4. b)
hist = df['age'].plot.hist(bins=50)
hist.set_xlabel(xlabel='Age')

df.boxplot(column='duration')

hist = df['balance'].plot.hist(bins=50)
plt.gca().set_xlim(left=df['balance'].min(), right=df['balance'].max())
hist.set_xlabel(xlabel='Balance')

# 4. c)
df_y_1_job = df[['y', 'job']].loc[df['y'] == 1]
subscription_bar = df_y_1_job.groupby('job').count().plot.bar(
    title='Number of clients grouped by the type of job who subscribed a term deposit',
    legend=False
)
subscription_bar.set_xlabel('Type of Job')
subscription_bar.set_ylabel('Number of clients')

# 4. d)
df_balance_age = df[['age_category', 'balance']].groupby('age_category')
balance_bar = df_balance_age.mean().plot.bar(
    title='Average balance by age category',
    legend=False
)
balance_bar.set_xlabel('Age category')
balance_bar.set_ylabel('Average Balance')

pd.set_option("display.max_rows", 1000)

# 2. a)
# -----------------------------------------------------------------------------

horseasses_pop_df = pd.read_csv(
    'part2/horseasses-population-in-nepal-by-district.csv')
rabbit_pop_df = pd.read_csv('part2/rabbit-population-in-nepal-by-district.csv')
yak_pop_df = pd.read_csv(
    'part2/yak-nak-chauri-population-in-nepal-by-district.csv')
milk_prod_df = pd.read_csv(
    'part2/milk-animals-and-milk-production-in-nepal-by-district.csv')
meat_prod_df = pd.read_csv(
    'part2/net-meat-production-in-nepal-by-district.csv')
cotton_prod_df = pd.read_csv(
    'part2/production-of-cotton-in-nepal-by-district.csv')
egg_prod_df = pd.read_csv('part2/production-of-egg-in-nepal-by-district.csv')
wool_prod_df = pd.read_csv('part2/wool-production-in-nepal-by-district.csv')


# Clean the dataframes
def replace_value(dict, inplace, *df_array):
    for df in df_array:
        df.replace(dict, inplace=inplace)


replace_value({
    'DISTRICT': {
        'FW. REGION': 'FW.REGION',
        'W. REGION': 'W.REGION',
        'MW. REGION': 'MW.REGION',
        'C. REGION': 'C.REGION',
        'E. REGION': 'E.REGION',
    }},
    True,
    horseasses_pop_df,
    rabbit_pop_df,
    yak_pop_df,
    milk_prod_df,
    meat_prod_df,
    cotton_prod_df,
    egg_prod_df,
    wool_prod_df
)

replace_value({
    'DISTRICT': {
        'Total': 'NEPAL'
    }},
    True,
    horseasses_pop_df, rabbit_pop_df, yak_pop_df
)
milk_prod_nepal_df = milk_prod_df[milk_prod_df['DISTRICT'] == 'NEPAL']
# print(milk_prod_nepal_df)
milk_prod_nepal_df["TOTAL MILK PRODUCED"] = milk_prod_nepal_df["COW MILK"] + \
    milk_prod_nepal_df["BUFF MILK"]
# print(
# milk_prod_nepal_df
# )
df = pd.merge(horseasses_pop_df, rabbit_pop_df, on='DISTRICT', how='left')
df = pd.merge(df, yak_pop_df, on='DISTRICT', how='left')
df = pd.merge(df, milk_prod_df, on='DISTRICT', how='left')
df = pd.merge(df, meat_prod_df, on='DISTRICT', how='left')
df = pd.merge(df, cotton_prod_df, on='DISTRICT', how='left')
df = pd.merge(df, egg_prod_df, on='DISTRICT', how='left')
df = pd.merge(df, wool_prod_df, on='DISTRICT', how='left')
# print(df.columns)

# print(df.sort_values(by='DISTRICT'))

# Replace NaN values by 0 using inplace method
df.fillna(0, inplace=True)

# Convert all numerical values to int
df = df.astype({col: int for col in df.columns[1:]})

print(df.sort_values(by='DISTRICT'))

df_regions = df[df['DISTRICT'].str.contains('REGION') == True]

# Horses/Asses Population by Region
df_regions[['DISTRICT', 'Horses/Asses']].plot(
    kind='pie',
    title='Horses/Asses Population by Region',
    autopct='%1.0f%%',
    y='Horses/Asses',
    labels=df_regions['DISTRICT']
)


# Total Egg Production by Region
df_regions[['DISTRICT', 'TOTAL EGG']].plot(
    kind='pie',
    title='Total Egg produced by Region',
    autopct='%1.0f%%',
    y='TOTAL EGG',
    labels=df_regions['DISTRICT']
)

# Show all the plots
plt.show()
