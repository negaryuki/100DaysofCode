import random

from Hangman_words import word_list
from Hangman_art import stages, logo

print(logo)

chosen_word = random.choice(word_list)

word_length = len(chosen_word)
lives = len(stages)-1

#print(f'The Original word is {chosen_word}')

display = []

end_of_game = False

for letter in range(word_length):
    display += "_"

print(display)

while not end_of_game:
    guess = input("Guess a letter\n").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        lives -= 1
        print(f'You have guessed {guess}, You lost a life')
        if lives == 0:
            end_of_game = True
            print(f'You Lose')

    if "_" not in display:
        end_of_game = True

    print(stages[lives])