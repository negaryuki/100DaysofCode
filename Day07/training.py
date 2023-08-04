import random

word_list = ["ardvark", "baboom", "camel"]

chosen_word = random.choice(word_list)

guess = input("Guess a letter").lower()

for letter in chosen_word:
    if guess == letter:
        print("right")
    else:
        print("wrong")