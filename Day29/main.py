from tkinter import *


# ------------------- PASSWORD GENERATOR -------------------------
# ------------------- SAVE PASSWORD ------------------------------
# ------------------- UI SETUP -----------------------------------

window = Tk()
window.title("Password Generator")
window.config()

window = Tk()
window.title("Pomodoro")
window.config(padx=20, pady=20)

# ------------------- Canvas Widget ----------------------------

canvas = Canvas(width=200,height=200)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=pass_img)

canvas.pack()
#anvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)


window.mainloop()