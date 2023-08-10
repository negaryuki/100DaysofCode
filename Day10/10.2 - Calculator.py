# Calculator Project


from art import logo

# Add:

def add (n1 , n2):
  return n1 + n2

# Subtract:

def subtract (n1 , n2):
  return n1 - n2

# Multiply;

def multiply (n1 , n2):
  return n1 * n2

#Divide:

def divide (n1 , n2):
  return n1 / n2


operations = { 
"+" : add,
"-" : subtract,
"*" : multiply,
"/" : divide
            }

def calculator():
    num1 = float(input("what's the first number"))

    for symbol in operations:
        print(symbol)

    continue_cal = True

    while continue_cal:

        operation_symbol = input(" Pick an Operation symbol from the line above")    
        num2 = float(input("what is the next number?"))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")


        question = input("Do you want to continue? 'Yes' or 'No'").lower()

        if question == "yes":
            num1 = answer 

        else:
            continue_cal = False
            print("The program has finished")
            calculator()
            
calculator()
  
# we could have also written it like this:
 
#         if operation_symbol == "+":
#         answer = add(num1,num2)
    
#     elif operation_symbol == "-":
#         answer = subtract(num1,num2)
    
#     elif operation_symbol == "*":
#         answer = multiply(num1,num2)
        
#     elif operation_symbol == "/":
#         answer = divide(num1,num2)
