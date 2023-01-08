from __future__ import division
import pandas as pd
import numpy as np
import random as rand
import matplotlib.pyplot as plt
import seaborn as sns


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
print(horseasses_pop_df)

# horseasses_region_df_index = horseasses_pop_df[(
#     horseasses_pop_df['DISTRICT'].str.contains('REGION') == True)].index
# horseasses_total_df_index = horseasses_pop_df[horseasses_pop_df['DISTRICT'] == 'Total'].index
# horseasses_pop_df[['DISTRICT', 'Horses/Asses']
#                   ].drop(horseasses_region_df_index).drop(horseasses_total_df_index).sort_values('Horses/Asses', ascending=False).head(10).plot.bar(
#     x='DISTRICT',
#     legend=False
# )

# horseasses_region_df_index = horseasses_pop_df[(
#     horseasses_pop_df['DISTRICT'].str.contains('REGION') == True)].index
# horseasses_total_df_index = horseasses_pop_df[horseasses_pop_df['DISTRICT'] == 'NEPAL'].index
# milk_prod_df[['DISTRICT', 'TOTAL MILK PRODUCED']
#              ].drop(horseasses_region_df_index).drop(horseasses_total_df_index).sort_values('TOTAL MILK PRODUCED', ascending=False).head(10).plot.bar(
#     x='DISTRICT',
#     legend=False
# )

# Show the plot
plt.show()
