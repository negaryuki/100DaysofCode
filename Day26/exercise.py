# EXERCISE 01 - write a list comprehension that creates a new list called squared_numbers which contains every number in the "number" list but it should be squared.

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [n**2 for n in numbers]

print(squared_numbers)

#--------------------------------------------------

# EXERCISE 02 - write a list comprehension to vreate a new list called results. This new list should only contain the even numbers from the list numbers.

results = [n for n in numbers if n % 2 == 0]

print(results)

#--------------------------------------------------

# EXERCISE 03 - Take a look inside file1.txt and file2.txt They each contain a bunch of numbers, each number on a new line.  Create a list called "results2" which contains the numbers that are common in both files.

with open("file1.txt") as file1:
    file1_data = file1.readlines()

with open("file2.txt") as file2:
    file2_data = file2.readlines()

results2 = [int(n.strip()) for n in file1_data if n in file2_data]

print(results2)

#--------------------------------------------------

# EXERCISE 04 - Use dictionary Comprehension to create a dictionary called result3 that takes each word in the given sentence and calculates the number of letters in each word.

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

split_sentence = sentence.split()
result3 ={word:len(word) for word in split_sentence}

print(result3) 


