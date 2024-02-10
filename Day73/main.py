# ------- Import Statements ---------
import pandas as pd

# Setting the header row to 0 allows us to substitute our own column names.
df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)

# Challenge: Examine the first 5 rows and the last 5 rows of the of the dataframe

print(df.head())
print(df.tail())

print("------------------")
# Challenge:Check how many rows and how many columns there are.
# What are the dimensions of the dataframe?

print(df.shape)
print(df.count())

print("------------------")

# Challenge**: Calculate the total number of post per language.
# Which Programming language has had the highest total number of posts of all time?

grouping_tags = df.groupby('TAG').count()
print(grouping_tags)

sum_tags = df.groupby('TAG').sum()
print(sum_tags)