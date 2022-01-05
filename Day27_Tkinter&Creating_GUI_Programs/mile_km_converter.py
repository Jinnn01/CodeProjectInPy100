import tkinter

# set up a window
window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=150, height=100)
window.config(padx=20,pady=20)

def calculater():
    result = 1.609344 * float(user_input.get())
    output_label.config(text="{0:.2f}".format(result))

# set up text

mile_label = tkinter.Label(text="Miles")
mile_label.grid(column=2, row=0)

km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)

equal_label = tkinter.Label(text="is equal to")
equal_label.grid(column=0, row=1)

# set up output text
output_label = tkinter.Label(text=0)
output_label.grid(column=1, row=1)


# set up button
calculate_button = tkinter.Button(text="Calculate",command=calculater)
calculate_button.grid(column=1,row=2)

# set up entry
user_input = tkinter.Entry(width=5)
user_input.grid(column=1,row=0)



window.mainloop()
