stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']



import random


# VARIABLE DEFINITIONS:

word_list = ["Advocate", "baboom", "camel"]
chosen_word = random.choice(word_list)
print(f'Psst the chosen word is: {chosen_word}')
word_len = len(chosen_word)
num_life = len(stages) -1

# Hangman game structure:

display = []

for i in chosen_word:
    display += "_"

print(display)

# Right Character path:

game_finished = False

while not game_finished:
    guess = (input("Guess a letter")).lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            print(display)

# Wrong character Path:
    if guess not in chosen_word:
        num_life -= - 1
        if num_life == 0:
            game_finished = True
            print("You loose")

        if "_" not in display:
            game_finished = True
            print("Game over")



