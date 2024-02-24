import pandas as pd
import matplotlib.pyplot as plt
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

