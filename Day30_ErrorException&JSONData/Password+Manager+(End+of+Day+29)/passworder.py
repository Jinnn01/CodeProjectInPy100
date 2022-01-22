from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get().lower()
    email = email_entry.get()
    password = password_entry.get()
    new_dict = {
        website: {
            "email": email,
            'password': password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            try:
                with open(
                        "/Users/amber_xin/Documents/自学/udemy/100 _codes_py/Day30_ErrorException&JSONData/Password+Manager+(End+of+Day+29)/data.json",
                        "r") as data_file:
                    # json.dump(new_dict,data_file,indent=4)
                    # data_file.write(f"{website} | {email} | {password}\n")
                    data_container = json.load(data_file)

            except FileNotFoundError:
                with open(
                        "/Users/amber_xin/Documents/自学/udemy/100 _codes_py/Day30_ErrorException&JSONData/Password+Manager+(End+of+Day+29)/data.json",
                        "w") as data_file:
                    json.dump(new_dict, data_file, indent=4)

            else:
                data_container.update(new_dict)
                with open(
                        "/Users/amber_xin/Documents/自学/udemy/100 _codes_py/Day30_ErrorException&JSONData/Password+Manager+(End+of+Day+29)/data.json",
                        "w") as data_file:
                    json.dump(data_container, data_file, indent=4)

            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ----------------------------Find PASSWORD ------------------------------- #
def search_web():
    web_name = website_entry.get().lower()
    if not web_name:
        messagebox.showinfo(message="You can not look for an empty website")
    else:
        try:
            # reading data
            with open(
                    "/Users/amber_xin/Documents/自学/udemy/100 _codes_py/Day30_ErrorException&JSONData/Password+Manager+(End+of+Day+29)/data.json",
                    "r") as exist_data:
                whole_data = json.load(exist_data)
        except FileNotFoundError:
            messagebox.showinfo(message="No data files found")
        else:

            # check data whether in that
            if web_name in whole_data:
                # if so : show the data
                web_info = whole_data[web_name]
                messagebox.showinfo(title=web_name,
                                    message=f"WebName:{web_name}\nEmail:{web_info['email']}\nPassword:{web_info['password']}")
            else:
                # if not : warning
                messagebox.showinfo(title="Oops", message=f"No details for {web_name} ")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(
    file="/Users/amber_xin/Documents/自学/udemy/100 _codes_py/Day30_ErrorException&JSONData/Password+Manager+(End+of+Day+29)/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, sticky="w")
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="w")
email_entry.insert(0, "username@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="w")

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_web_btn = Button(text="Search", width=13, command=search_web)
search_web_btn.grid(row=1, column=2)

window.mainloop()
