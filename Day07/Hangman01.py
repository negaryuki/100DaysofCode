# step 1
import random

word_list = ["Advocate", "baboom", "camel"]

chosen_word = random.choice(word_list)

print(chosen_word)

guess = (input("Guess a letter")).lower()


for letter in chosen_word:
    if letter == guess:
        print(guess)
    else:
        print("wrong")
