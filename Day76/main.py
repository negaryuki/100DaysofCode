import pandas as pd
import plotly.express as px

df_apps = pd.read_csv('apps.csv')
shapes = df_apps.shape

print(shapes)

head_rows = df_apps.head()
print(head_rows)

# returns random samples:
print(df_apps.sample(5))

#remove columns:
df_apps.drop(['Last_Updated', 'Android_Ver'], axis=1,inplace=True)
print(head_rows)

#find NaN values in "Rating" and remove them:

nan_rows = df_apps[df_apps.Rating.isna()]
print(nan_rows.shape)
print(nan_rows.head( ))

df_apps_clean = df_apps.dropna()
print(df_apps_clean.shape)

# Find Duplicates and remove them:

duplicated_rows = df_apps_clean[df_apps_clean.duplicated()]
print(duplicated_rows.shape)
print(duplicated_rows.head())

df_apps_clean = df_apps_clean.drop_duplicates(subset= ['App', 'Type', 'Price'])
df_apps_clean[df apps_clean.App =='Instagram'] 

df_apps_clean.shape

  
# Data exploration

df_apps_clean.sort_values('Rating', ascending=False).head()
df_apps_clean.sort_values('Size_MBs', ascending=False).head()
df_apps_clean.sort_values('Reviews', ascending=False).head(50) 


ratings = df_apps_clean.Content_Rating.value_counts()

fig = px.pie(labels=ratings.index,
values=ratings.values,
title="Content Rating",
names=ratings.index,
)
fig.update_traces(textposition='outside', textinfo='percent+label')

fig.show()

# Donut chart 

fig = px.pie(labels=ratings.index,
values=ratings.values,
title="Content Rating",
names=ratings.index,
hole=0.6,
)
fig.update_traces(textposition='inside', textfont_size=15, textinfo='percent')

fig.show()


# checking Data types:
  
df_apps_clean.info()
df_apps_clean.installs.describe()

df_apps_clean.Installs = df_apps_clean.Installs.astype(str).str.replace(',',"")
df_apps_clean.Installs = pd.to_numeric(df_apps_clean.Installs)
df_apps_clean[['App', 'Installs']].groupby('Installs').count()
  
