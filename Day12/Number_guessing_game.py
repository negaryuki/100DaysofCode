# creating. number guessing game

import random

from art import logo




def randomize_number():
    number = random.randint(1, 100)
    return number


hard_attempt = 5
easy_attempt = 10


def set_difficulty():
    game_continue = True
    level = input(
        'Welcome to the number guessing game ^o^/ ! your goal is to guess what random number the computer chose '
        'between 1 and 100.\n first choose your level. \'hard\' or \'easy\'?').lower()

    while game_continue:

        if level == "hard":
            return hard_attempt

        elif level == "easy":
            return easy_attempt

        else:
            print("you entered an invalid input. the game will now restart")
            game_continue = False
            set_difficulty()


def game_fundamental():
    number = randomize_number()
    continue_guess = True
    attempt = set_difficulty()

    while continue_guess:
        guess = int(input("Enter a number\n"))

        if guess > number:
            attempt -= 1
            print(f'too high you have {attempt} attempts left')

        if guess < number:
            attempt -= 1
            print(f'too low you have {attempt} attempts left')

        if guess == number:
            print("You guessed right! You win!")

        if attempt == 0:
            continue_guess = False
            print(f"you are out of tries. the asnwer was {number} Game over")


if input("Do you wanna guess the randomized number? 'y' or 'n'").lower() =='y':
    print(logo)
    game_fundamental()
else:
    print("ByeBye See you next time! ")

