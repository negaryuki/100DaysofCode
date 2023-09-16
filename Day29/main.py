from tkinter import *


# ------------------- PASSWORD GENERATOR -------------------------
# ------------------- SAVE PASSWORD ------------------------------
# ------------------- UI SETUP -----------------------------------

window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

# ------------------- Canvas Widget ----------------------------

canvas = Canvas(width=200,height=200)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=pass_img)

canvas.grid(row=0,column=1)

# ------------------- Label ------------------------------------

website_label = Label(text="Website:")
website_label.grid(row=1,column=0)

mail_user_label = Label(text="Email/Username:")
mail_user_label.grid(row=2,column=0)

password_label = Label(text="Password:")
password_label.grid(row=3,column=0)


window.mainloop()