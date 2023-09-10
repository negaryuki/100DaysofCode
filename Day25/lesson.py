# without panda library :
#import csv

#with open("weather_data.csv") as data_file:
#  data = csv.reader(data_file)
#  tempretures = []
#  for row in data:
#    if row[1] != "temp":
#      tempretures.append(row[1])


# with Pandas: less codes, better outcome

import pandas

data = pandas.read_csv("weather_data.csv")
print(data) # is a "dataframe"

print(data["temp"]) # is a"series"

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)


average_temp = sum(temp_list) / len(temp_list)
print(average_temp)


# -------------------------------------------------------
# alternative way:
# In the Python pandas library, the .mean() function is used to calculate the mean (average) of numeric data in a DataFrame or Series.
# You can apply it to a pandas DataFrame or Series to get the average value of the data.   
   
average = data["temp"].mean()  

print(average)

# -------------------------------------------------------

max_value = data["temp"].max()

print(max_value)

# -------------------------------------------------------
