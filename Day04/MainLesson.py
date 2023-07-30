# randomisation MODULE

import random
import MyModule

random_integer = random.randint(1, 25)
print(random_integer)

random_float = random.random()
print(random_float)

# a random decimal no. between 0 and 5
random_decimal = random.random() * 5
print(random_decimal)

# Python Lists: a data structure - a way of storing and organizing Data e.g. -> fruits = [item1, item 2]
# The order is important

fruits = ["Cherry", "Apple", "Banana"]

states_of_america = ["Delaware", "Pennsylvania", "Texas"]

print(fruits[2])
print(states_of_america[0])

# changing an item in a list
fruits[1] = "Pears"

print(fruits)

# adding data to lists:

fruits.append("Kiwi")
print(fruits)

# in order to add more items to the list

fruits.extend(["melon","watermelon"])

print(fruits)
