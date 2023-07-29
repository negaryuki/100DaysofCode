# Conditional Statements
# if CONDITION: DO THIS else: DO THIS

height = int(input("What is your height in cm?"))

if height == 120:
    print("You can ride the roller coaster")
else:
    print("You Can't ride the roller coaster")

# Modulo operator !! : 7 % 2 = 2 + 2 + 2 + (1) ==> 7 % 2 = 1

print(9 % 2)

# Nested if/else statement:

age = int(input("What is Your age?"))

if height >= 120:
    print("You can ride the roller coaster")
    if age <= 18:
        print("please pay 7$")
    else:
        print("please pay 12$")
else:
    print("You Can't ride the roller coaster")


# if/elif/ else

if height >= 120:
    print("You can ride the roller coaster")
    if age <= 12:
        print("Please pay 5$")
    elif 12 > age <= 18:
        print("Please Pay 7 $")
    else:
        print("please Pay 12$")
else:
    print("you can not ride the roller coaster")

# Multiple if

want_photo = input("Do you want a Photo? Y or N?")
Bill = 0

if height >= 120:
    print("You can ride the roller coaster")
    if age <= 12:
        Bill=5
        print("Children tickets are 5$")
    elif 12 > age <= 18:
        Bill =7
        print("Youth Tickets are 7$")
    else:
        print("Adult tickets are 12$")
        Bill = 12
        if want_photo == "Y":
            Bill += 3
        print(f'Your total Bill is {Bill}')

else:
    print("you can not ride the roller coaster")
