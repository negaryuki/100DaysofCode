#create a program using mths and f-string that telll us how many days, weeks,months
#we have left to live until 90 years old

#Don't change the below

age = input("What is your current age?\n")

#write your code below

years = 90 - int(age)
months = years * 12
weeks = years * 52
days = years * 365

print(f" You have {days}, {weeks}, and {months} left.")
print(f" As a Bonus,\n You have {years} years left until you are 90")