import pandas

# TODO 1: create a dictionary in this format:
# {"A": "Alfa" , "B: "Bravo"}

# TODO 2: Create a list of phonetic code words from a word that the user inputs

# ----------------------------------------------------

# extract data from csv file:
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create a new dictionary from the DataFrame using comprehensive dict:
# {new_key:new_value for (index,row) in df.iterrows()}

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("enter a word:\n").upper()

output_list = [phonetic_dict[letter] for letter in word]

print(output_list)

# ----------------------------------------------------
