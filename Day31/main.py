from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC5"

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dic(orient="records")



#-------------- NEXT CARD COMMAND ---------------

def next_card()
  current_card =random.choice(to_learn)
  canvas.itemconfig(card_title,text="French")  canvas.itemconfig(card_word, current_card["French"])


#-------------- Setup window ---------------
window= Tk()
window.title("Flash Cards")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)

#-------------- Canvas----------------------
  
canvas = Canvas(width=800,height=526)
card_front_img = PhotoImage(file="images/card_front.png")

canvas.create_image(400, 263,image=card_front_img)
card_title= canvas.create_text(400,150, text="Title", font=("Ariel", 40, "italic"))
card_word= canvas.create_text(400,263, text="word",font=("Ariel",60,"bold)")

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0,column=0)


#-------------- Button----------------------

cross_img = PhotoImage(images/wrong.png)
unknown_button= Button(image=cross_img, highlightthickness=0, c)
unknown_button.grid(row=1,column=0, columnspan=1)

check_img = PhotoImage(images/right.png)
known_button= Button(image=check_img, highlightthickness=0)
known_button.grid(row=1,column=1)

next_card()

window.mainloop()
