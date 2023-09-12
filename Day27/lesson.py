# Tkinter Module: creating GUI !

import tkinter

window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

#---------------------------------------------------
# Creating a Label:
# step 1 - create Label
  
my_lable = tkingter.Lable(text="I Am a Label", font=("Arial", 24, "Bold"))  # this is not enough to display the lable

# step 2- Display Label:

my_lable.pack(expand=True)  #arguments: expand,before, anchor,side, ....
  
#---------------------------------------------------
# Unlilmited Positional Arguments:

def exmp(*args):  # This Function can accept any number of Arguments because of (*args)  
  print(args[2])
  for n in args:
    print(n)

# Example :

def add(*args):
  num_list =[number for number in args]
  total = sum(num_list)
  print(total)
    
add(2,5,4)

#---------------------------------------------------

window.mainloop() # acts like a while loop and keeps the window on the screen. this must always be at the end of the program
