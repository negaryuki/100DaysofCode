import pandas as pd

df = pd.read_csv('salaries-by-college-major.csv')

# print(df.head())
# print(df.shape)
# print(df.columns)

# print(df.isna())
# print(df.tail())

clean_df = df.dropna()
# print(clean_df.tail())

print(clean_df['Starting Median Salary'].max())
print(clean_df['Starting Median Salary'].idxmax())
print(clean_df['Undergraduate Major'].loc[43])
print(clean_df.loc[43])

# ------------The Highest Mid-Career Salary---------------

print("What college major has the highest mid-career salary? How much do graduates with this major earn?")
print(f"Highest Mid-career salary:{clean_df['Mid-Career Median Salary'].max()}")
print(f"Index for the max mid career salary: {clean_df['Mid-Career Median Salary'].idxmax()}")
print(f"college major with highest mid-career salary: {clean_df['Undergraduate Major'][8]}")

# ---------The Lowest Starting and Mid-Career Salary---------------

print("Which college major has the lowest starting salary and how much do graduates earn after university?")

print(f"Lowest starting salary:{clean_df['Starting Median Salary'].min()}")
print(f"college major with lowest mid-career salary: {clean_df.loc[clean_df['Mid-Career Median Salary'].idxmin()]}")
print(clean_df.loc[clean_df['Mid-Career Median Salary'].idxmin()])

# ----------------------------------------------------------
spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(1, 'Spread', spread_col)
clean_df.head()

# ------------------Sorting by the Lowest Spread-----------------------

low_risk = clean_df.sort_values('Spread')
low_risk[['Undergraduate Major', 'Spread']].head()

# ---------------Majors with the Highest Potential----------------------

highest_potential = clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
highest_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head()

# ------------Majors with the Greatest Spread in Salaries-----------------

highest_spread = clean_df.sort_values('Spread', ascending=False)
highest_spread[['Undergraduate Major', 'Spread']].head()

print("------------------------")

# ------------------------Group By------------------------------------

print(clean_df.groupby('Group').count())
pd.options.display.float_format = '{:,.2f}'.format
average = clean_df.groupby('Group')["Mid-Career Median Salary"].mean()
print(average)
