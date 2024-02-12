import pandas as pd

mark = '--------------------'

colors = pd.read_csv("data/colors.csv")
print(colors.head())
unique_colors = colors['name'].nunique()
print(unique_colors)

transparent_Colors = colors.is_trans.value_counts()

print(transparent_Colors)

print(mark)

sets = pd.read_csv("data/sets.csv")
print(sets.head())
print(sets.tail())

sorted_year = sets.sort_values('year')
print(sorted_year.head())

print(mark)

no_of_first_sets = sets[sets['year'] == 1949]
print(no_of_first_sets)

print(mark)

most_parts =sets.sort_values('num_parts', ascending=False).head()
print(most_parts)

mark = '--------------------'

theme_by_year = sets.groupby('year').agg({'theme_id': pd.Series.unique})
theme_by_year.rename(columns={'theme_id':'nr_themes'}, inplace = True)

print(theme_by_year.head())
print(theme_by_year.tail())

mark = '--------------------'

plt.plot(theme_by_year.index[:-2], theme_by_year.nr_themes[:-2])

