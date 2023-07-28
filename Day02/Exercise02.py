#write a program that adds the digits in a 2 digit number
# e.g. if the input was 35, then the inputs e.g. should be 3 + 5 = 8.

entered_number = input("write a 2 digit Number\n")

print(type(entered_number))

first_digit = int(entered_number[0])
second_digit = int(entered_number[1])

result = str(first_digit + second_digit)

output = print(" The result is: " + result)