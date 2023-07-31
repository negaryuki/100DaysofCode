# Create a game of FizzBuzz , divisible by 3 = Fizz , divisible by 5 = Buzz , divisible by 3 and 5 =FizzBuzz

for number in range(1,101):
    if number % 3 == 0 and number % 5 > 0:
        print("Fizz")
    elif number % 5 ==0 and number % 3 != 0:
        print("Buzz")
    elif number % 5 == 0 and number % 3 == 0:
        print("FizzBuzz")
    else:
        print(number)

# or like this:

for game in range(1,101):
    if number % 5 == 0 and number % 3 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 ==0:
        print("Buzz")
    else:
        print(game)
