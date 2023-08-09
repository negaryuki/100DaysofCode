# Function with Outputs

def format_name (name,lastname):
    if name == "" or lastname == "":
        return "You did not provide valid inputs"
    
    formated_name = name.title()
    formated_lastname = lastname.title()
    
    return f'Result is : {formated_name} {formated_lastname}'
    

print(format_name (input("what is your name"), input("what is your last name")))