import pandas as pd


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
