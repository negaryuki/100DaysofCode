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


# ------------The Highest Mid-Career Salary---------------

print("What college major has the highest mid-career salary? How much do graduates with this major earn?")
print(f"Highest Mid-career salary:{clean_df['Mid-Career Median Salary'].max()}")
print(f"Index for the max mid career salary: {clean_df['Mid-Career Median Salary'].idxmax()}")
print(f"college major with highest mid-career salary: {clean_df['Undergraduate Major'][8]}")