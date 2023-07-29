#Don't change the below:
print("Welcome to the love calculator!")
name1 = input("What is your name?")
name2 = input("What is their name?")

# write your code below:

name1_lower = name1.lower()
name2_lower = name2.lower()

both_names = (name1_lower + name2_lower)

# "True" count:
t = both_names.count("t")
r = both_names.count("r")
u = both_names.count("u")
e = both_names.count("e")

# "Love" count:
l = both_names.count("l")
o = both_names.count("o")
v = both_names.count("v")

word_true = str(t + r + u + e)
word_love = str(l + o + v + e)

percent_str = (word_true) + (word_love)
percent_int = int(percent_str)

if 10 > percent_int or percent_int > 90:
    print(f' Your Result is {percent_str}%, You go together like coke and mentos')
elif 40 < percent_int < 50:
    print(f' Your Result is {percent_str}%, You are alright together')
else:
    print(f' Your Result is {percent_str}%')
