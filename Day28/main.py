from tkinter import *

#------------------- CONSTANTS --------------------------
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
#------------------- TIMER RESET ------------------------

#------------------- TIMER MECHANISM ---------------------

#------------------ COUNTDOWN MECHANISM ------------------

#------------------- UI SETUP ----------------------------

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas Widget 

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)   # highlightthickness removes the gap between the canvas and window
tomato_img = PhotoImage(file="tomato.png")  # calls the image
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(column=1, row=1)

# Label

timer_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)   # fg = foreground which defines the color of the text 

timer_label.grid(column=0, row=1)   # Place the label on grid

checkmark_label = Label(text="✔", font=(FONT_NAME, 22, "bold"), fg=GREEN, bg=YELLOW)

checkmark_label.grid(column=1, row=3)   # Place the label on grid

# Buttons

start_button = Button(text="Start", highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(column=2, row=2)

window.mainloop()
