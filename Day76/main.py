import pandas as pd

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