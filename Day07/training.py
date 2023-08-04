import random

word_list = ["ardvark", "baboom", "camel"]

chosen_word = random.choice(word_list)

word_length = len(chosen_word)

print(f'The Original word is {chosen_word}')

display = []

end_of_game = False

for letter in range(word_length):
    display += "_"

print(display)

while not end_of_game:
    guess = input("Guess a letter").lower()

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

        if not guess in chosen_word:
            end_of_game = True

        if not "_" in display:
            end_of_game = True
print(display)
