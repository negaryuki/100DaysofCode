from tkinter import *


# ------------------- PASSWORD GENERATOR -------------------------
# ------------------- SAVE PASSWORD ------------------------------
# ------------------- UI SETUP -----------------------------------

window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

# ------------------- Canvas Widget ----------------------------

canvas = Canvas(width=200,height=200)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=pass_img)
canvas.grid(row=0, column=1)

# ------------------- Label ------------------------------------

website_label = Label(text="Website:")
website_label.grid(row=1,column=0)

mail_user_label = Label(text="Email/Username:")
mail_user_label.grid(row=2,column=0)

password_label = Label(text="Password:")
password_label.grid(row=3,column=0)

# ------------------- ENTRY ------------------------------------

website_entry = Entry(width=40)
website_entry.grid(row=1, column=1, columnspan=2)

mail_user_entry = Entry(width=40)
mail_user_entry.grid(row=2,column=1,columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)

# ------------------- BUTTON ------------------------------------

gen_pass_button = Button(text="Generate Password",width=15)
gen_pass_button.grid(row=3,column=2, columnspan=2)

add_button = Button(text="Add",width=38)
add_button.grid(row=4,column=1, columnspan=2)


window.mainloop()