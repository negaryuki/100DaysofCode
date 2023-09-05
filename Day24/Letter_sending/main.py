with open("./Input/Names/invited_names.txt") as invited_names:
    names_list = (invited_names.readlines()). # readline turns all names into a list

with open("./Input/Letters/starting_letter.txt") as file:
    contents = file.read()

    for name in names_list:
        name = name.strip()
        new = contents.replace("[name]", name)
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt",
                  mode="w") as final_letter:
            final_letter.write(new)
