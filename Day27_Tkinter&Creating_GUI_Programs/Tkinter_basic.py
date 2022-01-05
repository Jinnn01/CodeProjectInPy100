import tkinter

window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


def button_click():
    input_text = input.get()
    my_label["text"] = input_text
    # print("I have been clicked")


# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label["text"] = "New text"
# 2nd way
my_label.config(text="New text by config")
my_label.grid(column=0, row=0)

# Button
my_button = tkinter.Button(text="Click me", command=button_click)
my_button.grid(column=1, row=1)

# challenge - new button
new_button = tkinter.Button(text="New button")
new_button.grid(column=2, row=0)

# Entry
input = tkinter.Entry(width=10)
input.grid(column=3, row=2)

# input.get()# get input


window.mainloop()
