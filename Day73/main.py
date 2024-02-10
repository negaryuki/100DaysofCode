# ------- Import Statements ---------
import pandas as pd
import matplotlib.pyplot as plt

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

# Challenge: Calculate the total number of post per language.
# Which Programming language has had the highest total number of posts of all time?

grouping_tags = df.groupby('TAG').count()
print(grouping_tags)

sum_tags = df.groupby('TAG').sum()
print(sum_tags)

print("------------------")

# Data cleaning

print(df['DATE'][1])

print(pd.to_datetime(df.DATE))
type(pd.to_datetime(df.DATE))

print("------------------")

# Cleaning Entire column

df.DATE = pd.to_datetime(df.DATE)
print(df.head())


print("------------------")
test_df = pd.DataFrame({'Age': ['Young', 'Young', 'Young', 'Young', 'Old', 'Old', 'Old', 'Old'],
                        'Actor': ['Jack', 'Arnold', 'Keanu', 'Sylvester', 'Jack', 'Arnold', 'Keanu', 'Sylvester'],
                        'Power': [100, 80, 25, 50, 99, 75, 5, 30]})
print(test_df)

print("------------------")

# The index is the category for the rows.
# The columns are the categories for the columns.
# The values are what you want in the new cells.

pivoted_df = test_df.pivot(index='Age', columns='Actor', values='Power')
print(pivoted_df)

print("------------------")

# Can you pivot the df DataFrame so that each row is a date and each column is a programming language?
# Store the result under a variable called reshaped_df.

reshaped_df = df.pivot(index="DATE", columns="TAG", values="POSTS")

print(reshaped_df)

print(reshaped_df.shape)
print(reshaped_df.columns)
print(reshaped_df.head())
print(reshaped_df.count())

print(reshaped_df.fillna(0, inplace=True))

print(reshaped_df.isna().values.any())

#-------Matplotlib----------

# .figure() - allows us to resize our chart
# .xticks() - configures our x-axis
# .yticks() - configures our y-axis
# .xlabel() - add text to the x-axis
# .ylabel() - add text to the y-axis
# .ylim() - allows us to set a lower and upper bound

roll_df = reshaped_df.rolling(window=6).mean()

roll_df = reshaped_df.rolling(window=6).mean()

plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)


for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column],
             linewidth=3, label=roll_df[column].name)

plt.legend(fontsize=16)

plt.show()
