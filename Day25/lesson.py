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
        # = data.temp.max()
print(max_value)

# -------------------------------------------------------
# Get Data in columns:

condition1 = data["condition"]

print(condition1)

#alternative way, but be careful, the spelling must be exact

condition2 = data.condition

# -------------------------------------------------------
# Get data in Row:
  
required_row = data[data.day == "Monday"]
print(required_row)

row_max_temp = data[data.temp == max_value]

monday = data[data.day == "Monday"]
print(monday.condition)

# converting celcius to farenheit --> C x (9/5) +32

mon_celcius = int(monday.temp)
mon_farenheit = mon_celcius * (9/5) + 32

# -------------------------------------------------------
# Create dataframe from scratch:
  
data_dict = {
  "students":["Amy", "James", "Angela"] , 
  "scores" : [76, 56, 65]
}

data2 = pandas.DataFrame(data_dict)
print(data2)

data.to_csv('new_data.csv')  # creates a new csv data in the same path
  
