from tkinter import *
from tkinter import messagebox


# ------------------- PASSWORD GENERATOR -------------------------
# ------------------- SAVE PASSWORD ------------------------------
def save():
    global is_ok
    website = website_entry.get()  # get() method is used to retrieve the current value of an Entry widget
    email = mail_user_entry.get()
    password = password_entry.get()

    is_ok = messagebox.askokcancel(title=website,
                                   message=f'These are the details entered:\n Website: {website}\n Email: {email}\n '
                                           f'Password: {password}\n Is it Ok to Save?')
    if is_ok:
        with open("data.text", mode='a') as data:
            data.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)  # delete() removes the characters we entered after triggering the button
            password_entry.delete(0, END)


# ------------------- UI SETUP -----------------------------------

window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

# ------------------- Canvas Widget ----------------------------

canvas = Canvas(width=200, height=200)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_img)
canvas.grid(row=0, column=1)

# ------------------- Label ------------------------------------

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

mail_user_label = Label(text="Email/Username:")
mail_user_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# ------------------- ENTRY ------------------------------------

website_entry = Entry(width=40)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()  # When a widget has the focus, it means that it is ready to accept user input

mail_user_entry = Entry(width=40)
mail_user_entry.grid(row=2, column=1, columnspan=2)
mail_user_entry.insert(0, "python@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# ------------------- BUTTON ------------------------------------

gen_pass_button = Button(text="Generate Password", width=15)
gen_pass_button.grid(row=3, column=2, columnspan=2)

add_button = Button(text="Add", width=38, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
