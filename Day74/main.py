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


themes_by_year = sets.groupby('year').agg({'theme_id': pd.Series.unique})
themes_by_year.rename(columns={'theme_id':'nr_themes'}, inplace = True)

print(themes_by_year.head())
print(themes_by_year.tail())

print(mark)

plt.plot(themes_by_years.index[:-2], themes_by_year.nr_themes[:-2])

ax1 = plt.gca() # getting the axis 
ax2 = ax1.twinx()  #create another axis that shares the same x-axis


ax1.plot(sets_by_year.index[:-2], sets_by_year.nr_themes[:-2], color='g')
ax2.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2], color='b')


ax1.set_xlabel('Year')
ax1.set_ylabel('Number of Sets', color='green')
ax2.set_ylabel('Number of Themes', color = 'blue')



             
  