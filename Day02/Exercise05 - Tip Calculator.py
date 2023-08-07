#create a tip calculator project

print("welcome to the tip Calculator:")
total_bill = input("What was the total Bill?")
percentage = input("what percentage tip would you like to give? 10 , 12 or 15?")
people = input("How many people to split the bill?")

total_bill_float = float(total_bill)
percentage_float = float(percentage)
people_int = int(people)

share_without_tip = total_bill_float / people_int
tip = total_bill_float * percentage_float / 100
each_tip = tip/people_int
each_share = round(share_without_tip + each_tip, 2)

# in order to force the program to write the second decimal, although it's a 0
each_share = "{:.2f}".format(each_share)

print(f'Each person should pay {each_share}')
