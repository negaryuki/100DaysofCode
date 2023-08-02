# step 2


import random

word_list = ["Advocate", "baboom", "camel"]

chosen_word = random.choice(word_list)
print(f'Psst the chosen word is: {chosen_word}')


guess = (input("Guess a letter")).lower()

word_len = len(chosen_word)
display =[]

for i in chosen_word:
    display += "_"


print(display)


for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter


print(display)