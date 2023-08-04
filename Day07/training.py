import random

word_list = ["ardvark", "baboom", "camel"]

chosen_word = random.choice(word_list)

word_length = len(chosen_word)

print(f'The Original word is {chosen_word}')

display = []

for letter in range(word_length):
    display += "_"

print(display)

guess = input("Guess a letter").lower()

for letter in chosen_word:
    if guess == letter:
        print("right")
    else:
        print("wrong")
