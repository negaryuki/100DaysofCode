import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv('cost_revenue_dirty.csv')
shapes = data.shape
print(shapes)

print(data.head())
print(data.tail())

# check for NaN values:
print(data.isna().values.any())

# check for duplicates

print(data.duplicated().values.any())
duplicated_rows = data[data.duplicated()]
print(len(duplicated_rows))

print(f'Any NaN values among the data? {data.isna().values.any()}')

print(f' Number of duplicates: {len(duplicated_rows)}')


# convert data

chars_to_remove = [',', '$']
columns_to_clean = ['USD_Production_Budget', 
                    'USD_Worldwide_Gross',
                    'USD_Domestic_Gross']

for col in columns_to_clean:
    for char in chars_to_remove:
        # Replace each character with an empty string
        data[col] = data[col].astype(str).str.replace(char, "")
    # Convert column to a numeric data type
    data[col] = pd.to_numeric(data[col])
    
    
data.Release_Date = pd.to_datetime(data.Release_Date)

data.describe()

print(f'the lowest budget film was {data[data.USD_Production_Budget == 1100.00]}')

print(f'the highest budget film was {data[data.USD_Production_Budget == 425000000.00]}')

zero_domestic = data[data.USD_Domestic_Gross == 0]
print(f'Number of films that grossed $0 domestically {len(zero_domestic)}')
zero_domestic.sort_values('USD_Production_Budget', ascending=False)

international_releases = data.loc[(data.USD_Domestic_Gross == 0) & 
                              (data.USD_Worldwide_Gross != 0)]
                              
#or using .query() method

international_releases = data.query('USD_Domestic_Gross == 0 and USD_Worldwide_Gross != 0')
print(f'Number of international releases: {len(international_releases)}')
international_releases

scrape_date = pd.Timestamp('2018-5-1')

future_releases = data [data.Release_Date >= scrape_date]
print (f'Number of unreleased movies: {len (future_releases) }')


data_clean = data.drop(future_releases.index)

money_losing = data_clean.query('USD_Production_Budget > USD_Worldwide_Gross')
money_losing.shape[0]/data_clean.shape[0]

sns.scatterplot(data=data_clean,
                x='USD_Production_Budget',
                y='USD_Worldwide_Gross')

plt.figure(figsize=(8,4), dpi=200)
sns.scatterplot (data=data_clean,
x='USD_Production_Budget',
y='USD Worldwide Gross')

plt.show()

plt.figure(figsize=(8,4), dpi=200)

with sns.axes_style("darkgrid"):
    ax = sns.scatterplot(data=data_clean,
                    x='Release_Date',
                    y='USD_Production_Budget',
                    hue='USD_Worldwide_Gross',
                    size='USD_Worldwide_Gross',)

    ax.set(ylim=(0, 450000000),
           xlim=(data_clean.Release_Date.min(), data_clean.Release_Date.max()),
           xlabel='Year',
           ylabel='Budget in $100 millions')

dt_index = pd.DatetimeIndex(data_clean.Release_Date)
years = dt_index.year

decades = years//10*10
data_clean['Decade'] = decades

old_films = data_clean[data_clean.Decade <= 1960]
new_films = data_clean[data_clean.Decade > 1960]

old_films.describe()

old_films.sort_values('USD Production Budget', ascending=False).head()

sns.regplot(data=old_films,
            x='USD_Production_Budget',
            y='USD_Worldwide_Gross')

plt.figure(figsize=(8,4), dpi=200)
with sns.axes_style("whitegrid"):
  sns.regplot(data=old_films,
            x='USD_Production_Budget',
            y='USD_Worldwide_Gross',
            scatter_kws = {'alpha': 0.4},
            line_kws = {'color': 'black'})

plt.figure(figsize=(8, 4), dpi=200)
with sns.axes_style('darkgrid'):
    ax = sns.regplot(data=new_films,
                     x='USD_Production_Budget',
                     y='USD_Worldwide_Gross',
                     color='#2f4b7c',
                     scatter_kws={'alpha': 0.3},
                     line_kws={'color': '#ff7c43'})

    ax.set(ylim=(0, 3000000000),
           xlim=(0, 450000000),
           ylabel='Revenue in $ billions',
           xlabel='Budget in $100 millions')

regression = LinearRegression()

# Explanatory Variable(s) or Feature(s)
X = pd.DataFrame(new_films, columns=['USD_Production_Budget'])

# Response Variable or Target
y = pd.DataFrame(new_films,columns=['USD_Worldwide_Gross'])

# Find the best-fit line
regression.fit(X, y)