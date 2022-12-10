from __future__ import division
import pandas as pd
import random as rand
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option("display.max_rows", 1000)

# 2. a)
# -----------------------------------------------------------------------------

horseasses_pop_df = pd.read_csv(
    'horseasses-population-in-nepal-by-district.csv')
rabbit_pop_df = pd.read_csv('rabbit-population-in-nepal-by-district.csv')
yak_pop_df = pd.read_csv('yak-nak-chauri-population-in-nepal-by-district.csv')
milk_prod_df = pd.read_csv(
    'milk-animals-and-milk-production-in-nepal-by-district.csv')
meat_prod_df = pd.read_csv('net-meat-production-in-nepal-by-district.csv')
cotton_prod_df = pd.read_csv('production-of-cotton-in-nepal-by-district.csv')
egg_prod_df = pd.read_csv('production-of-egg-in-nepal-by-district.csv')
wool_prod_df = pd.read_csv('wool-production-in-nepal-by-district.csv')


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
    horseasses_pop_df, rabbit_pop_df, yak_pop_df, milk_prod_df, meat_prod_df, cotton_prod_df, egg_prod_df, wool_prod_df
)

replace_value({
    'DISTRICT': {
        'Total': 'NEPAL'
    }},
    True,
    horseasses_pop_df, rabbit_pop_df, yak_pop_df
)

df = pd.merge(horseasses_pop_df, rabbit_pop_df, on='DISTRICT', how='left')
df = pd.merge(df, yak_pop_df, on='DISTRICT', how='left')
df = pd.merge(df, milk_prod_df, on='DISTRICT', how='left')
df = pd.merge(df, meat_prod_df, on='DISTRICT', how='left')
df = pd.merge(df, cotton_prod_df, on='DISTRICT', how='left')
df = pd.merge(df, egg_prod_df, on='DISTRICT', how='left')
df = pd.merge(df, wool_prod_df, on='DISTRICT', how='left')

print(df.sort_values(by='DISTRICT'))

# df.plot.bar(title='Overall')
# plt.show()
