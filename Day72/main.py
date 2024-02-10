import pandas as pd
df = pd.read_csv('salaries-by-college-major.csv')


#print(df.head())
#print(df.shape)
#print(df.columns)

#print(df.isna())
#print(df.tail())

clean_df = df.dropna()
#print(clean_df.tail())

print(clean_df['Starting Median Salary'].max())
print(clean_df['Starting Median Salary'].idxmax())
print(clean_df['Undergraduate Major'].loc[43])
print(clean_df.loc[43])