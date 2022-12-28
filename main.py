from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_textfield.delete(0, END)  # Everytime the button is clicked, it gets cleared for UX

    # Password Generator Project

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))

    password_list += [random.choice(letters) for index in range(nr_letters)]

    password_list += [random.choice(symbols) for index in range(nr_symbols)]

    password_list += [random.choice(numbers) for index in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)  # Makes a list into a string

    password_textfield.insert(index=0, string=password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_info():
    website = website_textfield.get()
    username = username_textfield.get()
    password = password_textfield.get()
    password_length = len(password.strip(" "))  # Stripping spaces because user may spam spaces instead of a blank space
    website_length = len(website.strip(" "))

    new_data = {
        website: {
            "email": username,
            "password": password,
        }
    }

    if password_length == 0 or website_length == 0:
        messagebox.showerror(message="You cannot leave the fields empty", title="Error!!")
    else:
        with open("data.json", mode="r") as json_file:  # mode (a) will append the file
            # json.dump(new_data, json_file,indent=4)
            # data = json.load(json_file)


        # Clearing the fields after each use
        pyperclip.copy(password)
        website_textfield.delete(0, END)
        password_textfield.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=20, padx=20)

# Canvas
canvas = Canvas(width=200, height=200)
mypass_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=mypass_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:", font=("Arial", 10, "bold"))
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username:", font=("Arial", 10, "bold"))
username_label.grid(row=2, column=0)

password_label = Label(text="Password:", font=("Arial", 10, "bold"))
password_label.grid(row=3, column=0)

# Input fields

website_textfield = Entry(width=52)
website_textfield.grid(row=1, column=1, columnspan=2)
website_textfield.insert(0, ".com")
website_textfield.focus()

username_textfield = Entry(width=52)
username_textfield.grid(row=2, column=1, columnspan=2)
username_textfield.insert(0, "@gmail.com")

password_textfield = Entry(width=33)
password_textfield.grid(row=3, column=1)

# Buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=44, command=add_info)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
