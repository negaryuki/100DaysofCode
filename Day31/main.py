from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC5"
current_card = {}
to_learn = {}

# -------------- READ PANDA CSV ---------------

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# -------------- NEXT CARD FUNCTION ---------------

def next_card():
    global current_card, flip_timer

    window.after_cancel(flip_timer)  # invalidate timer
    current_card = random.choice(to_learn)
    to_learn_french = current_card["French"]

    canvas.itemconfig(canvas_title, text="French", fill="black")
    canvas.itemconfig(canvas_word, text=to_learn_french, fill="black")
    canvas.itemconfig(canvas_background, image=card_front_img)

    flip_timer = window.after(3000, func=flip_card)


# -------------- FLIP CARD FUNCTION ---------------

def flip_card():
    to_learn_english = current_card["English"]

    canvas.itemconfig(canvas_title, text="English", fill="white")
    canvas.itemconfig(canvas_word, text=to_learn_english, fill="white")

    canvas.itemconfig(canvas_background, image=card_back_img)


# -------------- IS_KNOWN FUNCTION ---------------

def is_known():
    to_learn.remove(current_card)
    next_card()

    # in order to keep hold of the words we have to learn, we have to save it to a list:

    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv")


# -------------- SETUP WINDOW ---------------

window = Tk()
window.title('Flash Card Learner')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# ------------------- CANVAS ---------------

canvas = Canvas(width=800, height=526)

# import pictures:
card_front_img = PhotoImage(file="Images/card_front.png")
card_back_img = PhotoImage(file="Images/card_back.png")

canvas_background = canvas.create_image(400, 263, image=card_front_img)

# ------------------- Canvas text ---------------

canvas_title = canvas.create_text(400, 150, text="English/French", font=("Arial", 40, "italic"))

canvas_word = canvas.create_text(400, 263, text="WORD", font=("Arial", 60, "bold"))

canvas.config(bg= BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# ------------------- BUTTONS ---------------

# import pictures:

cross_img = PhotoImage(file="Images/wrong.png")
check_img = PhotoImage(file="Images/right.png")

# creating buttons:

unknown_button = Button(image=cross_img, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

known_button = Button(image=check_img, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
