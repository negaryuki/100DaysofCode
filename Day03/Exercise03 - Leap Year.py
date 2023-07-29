# write a program that works out whether if a given year is a leap year.
# a normal year consists of 365 days.
# Leap years have 366 days

# on every year that us evenly divisible by 4
# except every year that is evenly divisible by 100
# unless the year is also evenly divisible by 400

# Don't change the below code:

year = int(input("Which year would you like to check?"))

# write your code below:

if year % 4 == 0:
    if year % 100 ==0:
        if year % 400 ==0:
            print("It's a LEAP YEAR")
        else:
            print("It's a LEAP YEAR")
    else:
        print("It's a LEAP YEAR")
else:
    print("It's a Normal year")
