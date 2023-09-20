# Tkinter Module: creating GUI !

import tkinter

window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

# ---------------------------------------------------
# Creating a Label:
# step 1 - create Label

my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "Bold"))  # this is not enough to display the lable

# step 2- Display Label:

my_label.pack(expand=True)  # arguments: expand,before, anchor,side, ....


# ---------------------------------------------------
# Unlilmited Positional Arguments:

def exmp(*args):  # This Function can accept any number of Arguments because of (*args)  
    print(args[2])
    for n in args:
        print(n)


# Example :

def add(*args):
    num_list = [number for number in args]
    total = sum(num_list)
    print(total)


add(2, 5, 4)


# ---------------------------------------------------
# Keyword Arguments:

def example(**kwargs):  # This Function can accept unlimited keyword arguments)
    print(kwargs)
    # for key, value in kwargs.item()
    #  print(key)
    #  print(value)


example(add=3, multiply=5)


# Example:

def calculator(input_number, **kwargs):
    input_number += kwargs["add"]
    input_number *= kwargs["multiply"]
    print(input_number)


calculator(2, add=3, multiply=4)


# Example2:

class Car:

    def __init__(self, **kw):
        self.make = kw.get(
            "make")  # instead of writing kw["make"] we can use the get function. the difference is that if
        # we don't input a value for either key it will return "none" instead of giving an error
        self.model = kw.model("model")


my_car = Car(make="Nissan")
# ---------------------------------------------------
# configure and change properties of a created component:

my_label["text"] = "new text"  # as if it was a dictionary

# or 

my_label.config(text="Another new text")


# ---------------------------------------------------
# Buttons and actions:

# step 1 - create Function as a "command" for the Button

def button_click():
    print("you clicked the Button")
    my_label.config(text="Button got clicked")


# step 2 - create button -> type (not call) the command kw

button = tkinter.Button(text="click here", command=button_click())

# step 3- Display button:

button.pack()

# ---------------------------------------------------
# Entry component(Input):

input = tkinter.Entry(width=10)
input.pack()
input.get()  # returns the input as a string    

# ---------------------------------------------------

window.mainloop()  # acts like a while loop and keeps the window on the screen. this must always be at the end of the
# program
