# Function with Outputs


# This function returns an early output by using "return"

def format_name (name,lastname):
    """ takes a name and a last name and changes it to title mode"""

    if name == "" or lastname == "":
        return "You did not provide valid inputs"
    
    formated_name = name.title()
    formated_lastname = lastname.title()
    
    return f'Result is : {formated_name} {formated_lastname}'
    

print(format_name (input("what is your name"), input("what is your last name")))

"""
Docstrings: are strings that explain more about the fuction we wrote  ---> """ The text is written here"""
Using docstrings allows us to write as many lines as we want
Docstrings can also be used as multiline comments
Python suggests not using this for commenting.
"""
