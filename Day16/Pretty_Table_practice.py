from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name" , ["Pikachu" , "Squirtle" , "Charmander"])

table.add_column("Type" , ["Electric" , "Water" , "Fire"])


#Change object attribute:

table.align = "l"

print(table)


