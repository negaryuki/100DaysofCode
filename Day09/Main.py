# Dictionary and nesting

# Creating a Dictionary {key: value}
programming_dictionary = {"Bug": " an error in a program that ....",
                          "Function": "is ..."}

# retrieve an item from dictionary :
# in lists we would use index [0]

print(programming_dictionary["Bug"])

# add new entry to dictionary: Dictionary["key"] = value

programming_dictionary["Loop"] = " a piece of code that ..."
print(programming_dictionary)

# Creating an empty Dictionary:

empty_dictionary = {}
print(empty_dictionary)

# wiping a dictionary:

# programming_dictionary={}
# print(programming_dictionary)

# edit an item in a dictionary:

programming_dictionary["Bug"] = " this text was replaced"

print(programming_dictionary)

# Loop through a dictionary:

for thing in programming_dictionary:
    print(thing)
    print(programming_dictionary[thing])


# Nesting lists in Dictionaries:
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}
travel_log = {
    "France": ["Paris","lille","Dijon"],
    "Germany": "Berlin"
}

# Nesting Dictionary in Dictionary

traveling = {
    "France": {"cities": "Paris" , "times": 3},
    "Germany": {"cities": "Berlin" , "times": 3},

}

# Nesting Dictionary in lists

traveling_log = [
    {"Country": "France",
     "cities": ["Paris" , "Dijon"],
     "times": 3},
    {"Country": "Germany",
     "cities": ['Berlin'],
    "times": 3}
]
