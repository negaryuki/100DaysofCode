# Miles to Km converter 

from tkinter import *


def converter():
  miles = float(miles_input.get())
  km = miles * 1.609
  kilometer_result_lable.config(text=f"({km}")

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20 )

#widgets

miles_input = Entry(width=7)
miles_input.grid(column=1,row=0)

miles_lable =Lable(text= "Miles").grid(column=2,row=0)
miles_lable =Lable.grid(column=2,row=0)

is_equal_lable= Lable(text="Is Equal to")
is_equal_lable.grid(column=0,row=1)

kilometer_result_lable = Lable(text="0")
kilometer_result_lable.grid(column=1,row=1)

kilometer_lable = Lable(text="Km")
kilometer_lable = Lable(text="Km").grid(column=2,row=1)

Calculate_buttom= Buttom(text= "Calculate", command=converter)
Calculate_buttom= Buttom(text= "Calculate").grid(column=1,row=2)

window.mainloop()
