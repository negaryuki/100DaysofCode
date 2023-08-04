# step 3


import random

word_list = ["Advocate", "baboom", "camel"]

chosen_word = random.choice(word_list)
print(f'Psst the chosen word is: {chosen_word}')

word_len = len(chosen_word) -1
num_life = 6

display = []

for i in chosen_word:
    display += "_"

print(display)


game_finished = False

while not game_finished:
    guess = (input("Guess a letter")).lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

    if guess not in chosen_word:
        num_life -= - 1
        if num_life == 0:
            game_finished = True
            print("You loose")


    if "_" not in display:
        game_finished = True
        print("Game over")