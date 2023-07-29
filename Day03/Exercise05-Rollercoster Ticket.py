# write a program and tell the Guest how much they have to pay

height = int(input("What is your height in cm?"))
age = int(input("What is Your age?"))
want_photo = input("Do you want a Photo? Y or N?")

Bill = 0

if height >= 120:
    print("You can ride the roller coaster")
    if age <= 12:
        Bill=5
        print("Children tickets are 5$")
    elif age < 18:
        Bill =7
        print("Youth Tickets are 7$")
    elif age > 18 and 45 <= age <= 55:
        print("Congratulations! you have a free ticket")
        print(f'Your total Bill is {Bill}')
    else:
        print("Adult tickets are 12$")
        Bill = 12
        if want_photo == "Y":
            Bill += 3
        print(f'Your total Bill is {Bill}')

else:
    print("you can not ride the roller coaster")