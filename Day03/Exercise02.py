#BMI calculator 2.0 - Upgrated version

#Don't change the below:

height = float(input("Please enter your height in m"))
weight = float(input("Please enter your weight in Kg"))

#write code below:

BMI = round(weight / height ** 2,2)

print(f'Your BMI is {BMI}')

if BMI <= 18.5:
    print("You are underweight")
elif 18.5 < BMI <= 25:
    print("You are Normal")
elif 25 < BMI <= 30:
    print("You are overweight")
elif 30 < BMI <=35:
    print("you are obese")
else:
    print(" you are clinically obese")

