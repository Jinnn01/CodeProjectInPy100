from tkinter import *
import requests


def get_quote():
    kanye_response = requests.get(url="https://api.kanye.rest")
    quote_data = kanye_response.json()
    quote = quote_data["quote"]
    canvas.itemconfig(quote_text,text=quote)



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(
    file="/Users/amber_xin/Documents/自学/udemy/100 _codes_py/Day33_API_Endpoints & API_Parameters/kanye-quotes-start/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"),
                                fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(
    file="/Users/amber_xin/Documents/自学/udemy/100 _codes_py/Day33_API_Endpoints & API_Parameters/kanye-quotes-start/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()
