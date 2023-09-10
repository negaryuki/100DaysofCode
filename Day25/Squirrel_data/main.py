import pandas

# extract data from csv file:
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")


# exrtact count of various colors of Squirrels

gray = data["Primary Fur Color"] == "Gray"
gray_count = len(gray)  # because gray counts as some kind of list

red_count = len(data["Primary Fur Color"] == "Cinnamon")
black_count = len(data["Primary Fur Color"] == "Black")

# Construct Dataframe:

# step 1- Create Dictionary
data_dict = {
   "Fur color" : ["Gray","Cinnamon", "Black"],
   "Count" :[gray_count, red_count, black_count]
 } 
 
 #Step 2- get hold of DataFrame

df =pandas.DataFrame(data_dict)

df.to_csv("squirrel_count.csv")
