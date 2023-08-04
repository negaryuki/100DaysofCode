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

for position in range(word_length):
    letter = chosen_word[position]

    if letter == guess:
        display[position] = letter


print(display)
