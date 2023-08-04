# Symple Function

def greet():
    print("Hi")
    print("How do you do?")
    print("Isn't the Weather lovely today?")

greet()

# Function that allows for input (Parameter / Argument)  (Parameter) name = (Argument) Emilia

def greet_with_name(name):
    print(f'Hi {name}')
    print(f"How do you do {name}?")
    print(f"Isn't the Weather lovely today {name}?")

greet_with_name("Emilia")

greet_with_name("Goerge")

# Functions with more than one input:

def greet_with (name, location):
    print(f'Hello, My name is {name} and I am from {location}')


greet_with("Angel" , "Las vegas")