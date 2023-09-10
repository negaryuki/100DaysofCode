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
print(data)

print(data["temp"])
