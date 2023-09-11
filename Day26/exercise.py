# EXERCISE 01 - write a list comprehension that creates a new list called squared_numbers which contains every number in the "number" list but it should be squared.

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [n**2 for n in numbers]

print(squared_numbers)
