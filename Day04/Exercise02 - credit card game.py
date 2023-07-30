# Create a program that picks a name out of a list

# stg.split divides a string into a list with different items

# Don't change the below:

name_string = input("Give me everybody's names,separated by a comma")
names = name_string.split(", ")

print(names)
# write below:


length = len(names)

print(length)

import random

random_name = random.randint(0,length-1)

payer = (names[random_name])

print(payer)
