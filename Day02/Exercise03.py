#Body Mass index (BMI) Calculator

# Don't change the below code:

height = input("enter your height in m:\n")
weight = input("enter your weight in Kg:\n")

#write here:

#BMI = weight (kg) / height (m**2)

new_height = float(height)
new_weight = float(weight)

bmi = int(new_weight / new_height ** 2)

#for short  -->  bmi = float(weight) / float(height) **2

new_bmi = str(bmi)
print("Your BMI is " + new_bmi)
