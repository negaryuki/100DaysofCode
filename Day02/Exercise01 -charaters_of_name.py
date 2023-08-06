#write a program that asks your name and tells you how many characters that name has

num_char = len(input("what is your name?\n"))

print(type(num_char))

new_num_char = str(num_char)

print(type(new_num_char))

print("your name has " + new_num_char + " characters")
