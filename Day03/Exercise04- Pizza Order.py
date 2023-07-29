# Build an automotive Pizza order program
# Based on the user's order, work out their final bill

# Small Pizza : $15
# Medium Pizza : $20
# Large Pizza: $ 25

# Extra pepperoni Small: $2
# Extra pepperoni Medium and Large: $3
# Extra Cheese: $1

# Don't change the below:

print("Welcome to Python Pizza Deliveries!")
size = input("What size do you want? S, M, L \n")
add_pepperoni = input(" Do you want to add pepperoni? Y , N\n")
extra_cheese = input("Do you want to add cheese? Y , N \n")

# write below:

Bill = 0

if size == "S":
    Bill = 15
    if add_pepperoni == "Y":
        Bill += 2
    if extra_cheese == "Y":
        Bill += 1
elif size == "M":
    Bill = 20
    if add_pepperoni == "Y":
        Bill += 3
    if extra_cheese == "Y":
        Bill += 1
elif size == "L":
    Bill = 25
    if add_pepperoni == "Y":
        Bill += 3
    if extra_cheese == "Y":
        Bill += 1

print(f'Your total Bill is ${Bill}')
