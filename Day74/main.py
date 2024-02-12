..import pandas as pd

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

print(mark)

parts_per_set = sets.groupby('year').agg({'num_parts': pd.Series.mean})

plt.scatter(parts_per_set.index[:-2], parts_per_set.num_parts[:-2])
   
print(mark)
  
set_theme_count = sets["theme_id"].value_counts()
print(set_theme_count[:5]


print(mark)

themes = pd.read('data/themes.csv')
print(themes.head())


star_wars_themes = themes[themes.name == 'Star Wars']

star_wars_sets = sets[sets.theme_id ==18]
star_wars_sets = sets[sets.theme_id ==209]


set_theme_count = pd.DataFrame({'id': set_theme_count.index,
                                'set_count': set_theme_count.values})
                                
merged_df = pd.merge(set_theme_count,themes, on= 'id')
merged_df[:3]

print(mark)

plt.figure(figsize=(14,8))
plt.xticks(fontsize=14,rotation=45)
plt.yticks(fontsize=14)
plt.ylabel('Nr. of Sets', fontsize=14)
plt.xlabel('Theme name', fontsize=14)
plt.bar(merged_df.name[:10], merged_df.set_count


             
  