from tkinter import *
from tkinter import messagebox
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate():
    import random
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
    #   password_list.append(random.choice(letters)

    [password_list.append(random.choice(letters)) for char in range(nr_letters)]

    [password_list.append(random.choice(symbols)) for symbol in range(nr_symbols)]

    [password_list.append(random.choice(numbers)) for number in range(nr_numbers)]

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": email,
        "password": password
    }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please do not leave any fields empty")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            password_entry.delete(0, END)
            website_entry.delete(0, END)


def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Search Not Found", message="No Data Found")
    else:
        for key in data.keys():
            if website == key:
                email = data[key]["email"]
                password = data[key]["password"]
                messagebox.showinfo(title="Search",
                                    message=f"Email:{email}\n Password:{password}")
        if website not in data.keys():
            messagebox.showinfo(title="Search Not Found",
                                message="No details of website found")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=("Arial", 10, "normal"))
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_label = Label(text="Email/Username:", font=("Arial", 10, "normal"))
email_label.grid(column=0, row=2)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "kbrako.asante@gmail.com")

password_label = Label(text="Password:", font=("Arial", 10, "normal"))
password_label.grid(column=0, row=3)

password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, columnspan=2)

generateButton = Button(text="✔", height=1, command=generate)
generateButton.grid(row=3, column=2)

add = Button(text="Add", width=30, command=save)
add.grid(row=4, column=1, columnspan=2)

searchButton = Button(text="search", command=find_password)
searchButton.grid(row=1, column=2)

window.mainloop()
