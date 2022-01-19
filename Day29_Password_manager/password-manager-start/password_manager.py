from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # list comprehension
    letter_list = [random.choice(letters) for _ in range(nr_letters)]
    symbol_list = [random.choice(symbols) for _ in range(nr_symbols)]
    numbers_list = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = letter_list + symbol_list + numbers_list

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website_info = web_entry.get()
    email_info = email_entry.get()
    password_info = password_entry.get()

    if not len(website_info) == 0 and len(email_info) == 0:

        is_ok = messagebox.askokcancel(title=website_info,
                                       message=f"There are the details of {website_info}:\n"
                                               f"Email:{email_info}\n"
                                               f"Password:{password_info}\n"
                                               f"Is it ok to save?")
        if is_ok:
            # create data.txt
            with open("data.txt", "a") as data_file:
                format_string = f"{website_info} | {email_info} | {password_info}\n"
                data_file.write(format_string)

                # clear the entry box
                web_entry.delete(0, END)
                password_entry.delete(0, END)

    else:
        messagebox.showinfo(title="Warning", message="Please don't leave any thing empty")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=20, pady=20)

# set image
canvas = Canvas(width=200, height=200)
bg_pic = PhotoImage(
    file="/Users/amber_xin/Documents/自学/udemy/100 _codes_py/Day29_Password_manager/password-manager-start/logo.png")
canvas.create_image(100, 100, image=bg_pic)
canvas.grid(row=0, column=1)

# set labels
web_label = Label(text="Website:")
web_label.grid(row=1, column=0)

email_label = Label(text='Email/username:')
email_label.grid(row=2, column=0)

password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

# set entry
web_entry = Entry(width=35)
web_entry.grid(row=1, column=1, columnspan=2, sticky="w")
web_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="w")
email_entry.insert(0, "gxin1201@163.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="w")

# set buttons
generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(row=3, column=2, sticky="e")

add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(row=4, column=1, columnspan=2, sticky="w")

window.mainloop()
