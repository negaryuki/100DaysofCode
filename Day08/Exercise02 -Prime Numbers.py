# Write your code below this line 👇

def prime_checker(number):
    is_prime = True

    for divisor in range(2,number):
        if number % divisor == 0:
            is_prime = False

    if number == 1:
            is_prime = True
    if is_prime:
        print("The number entered is a prime number")
    else:
        is_prime = False
        print("The number entered is NOT a prime number")



# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)