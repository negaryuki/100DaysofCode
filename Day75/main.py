import pandas as pd
import maatplotlib.pyplot as plt
import matplotlib.dates as mdates
from pandas.plotting import register_matplotlibconverters
register_matplotlib_converters( )

df_tesla = pd.read_csv('tesla.csv')
df_unemployment = pd.read_csv('unemployment.csv')
df_btc_price = pd.read_csv('###')
df_btc_search = pd.read_csv('###')

# -------------------TESlA------------------------

print(df_tesla.shape)
print(df_tesla.head())


print (f'Largest value for Tesla in Web Search: {df tesla.TSLA WEB SEARCH.max ( )}')
print (f'Smallest value for Tesla in Web Search: {df tesla.TSLA WEB SEARCH.min() }')

df_tesla.describe()

# -------------------Unemployment-------------------
  
print(df_unemployment.shape)
print(df_unemployment.head())

print (f'Largest value for "Unemployemnt Benefits" in Web Search: {df unemployment.UE_BENEFITS_WEB-SEARCH.max( )}')

# -------------------Bitcoin-------------------

print(df_btc_price.shape)
print(df_btc_price.head())


print(df_btc_search.shape)
print(df_btc_search.head())


print (f'largest BIC News Search (df _bto_search. BIC NEWS_SEARCH.max ())')


# -------------------Cleaning Data-------------------

print(f'Missing values for Tesla? {df_teslaisna().values().any()}')
print(f'Missing values for Unemployment? {df_unemployment.isna().values().any()}')
print(f'Missing values for Tesla? {df_btc_search.isna().values().any()}')

print(f'Missing values for Tesla? {df_btc_search.isna().values().sum()}')
df_btc_price[df_btc_price.ClOSE.isna()]

df_btc_price = df_btc_price.dropna()

# Remove any Missing values:
  
df_btc_price = df_btc_price.dropna(inplace=True)

# Change Datetime type:
  
type(df_tesla.MONTH[0])

df_tesla.MONTH = pd.to_datetime(df_tesla.MONTH)
df_btc_search.MONTH = pd.to_datetime(df_btc_search.MONTH)
df_unemployment.MONTH = pd.to_datetime(df_unemployment.MONTH)
df_btc_price.DATE = pd.to_datetime(df_btc_price.DATE)

# Converting Data:
  
df_btc_monthly = df_btc_price.resample('M',on='DATE').last()

print(df_btc_monthly.shape)
df_btc_monthly.head( )

#----------------Visualization--------------------

# size and resolution
plt.figure(figsize=(14,8), dpi=120) 
plt.title('Tesla Web Search vs Price', fontsize=18)

ax1 = plt.gca()
ax2 = ax1.twinx()

# fontsize and linewidth for larger charts
ax1.set_ylabel('TSLA Stock Price', color='#E6232E', fontsize=14)
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)

ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color='#E6232E', linewidth=3)
ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, color='skyblue', linewidth=3)

# Displays chart
plt.show()

