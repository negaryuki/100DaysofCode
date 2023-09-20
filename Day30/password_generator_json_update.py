from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ------------------- PASSWORD GENERATOR -------------------------
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Clear the password_entry widget
    password_entry.delete(0, END)

    password_list = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_list += [random.choice(numbers) for char in range(random.randint(2, 4))]
    password_list += [random.choice(symbols) for char in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, f"{password}")
    pyperclip.copy(password)


# ------------------- SAVE PASSWORD ------------------------------
def save():
    website = website_entry.get()
    email = mail_user_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ------------------- FIND PASSWORD ------------------------------

def find_password():
    website = website_entry.get()

    try:

        with open("data.json") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data fie found")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f' Email: {email}\nPassword:{password}')

        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists")

        # ------------------- UI SETUP -----------------------------------


window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

# ------------------- Canvas Widget ----------------------------

canvas = Canvas(width=200, height=200)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_img)
canvas.grid(row=0, column=1,columnspan =2)

# ------------------- Label ------------------------------------

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

mail_user_label = Label(text="Email/Username:")
mail_user_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# ------------------- ENTRY ------------------------------------

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()  # When a widget has the focus, it means that it is ready to accept user input

mail_user_entry = Entry(width=40)
mail_user_entry.grid(row=2, column=1, columnspan=2)
mail_user_entry.insert(0, "python@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# ------------------- BUTTON ------------------------------------

gen_pass_button = Button(text="Generate Password", width=15, command=generate_password)
gen_pass_button.grid(row=3, column=2, columnspan=2)

add_button = Button(text="Add", width=38, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="search", width=13, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()
