import random
from tkinter import *
from tkinter import messagebox
import pandas
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Times New Roman", 40)
WORD_FONT = ("Times New Roman", 60, "bold")
current_word_dict = {}
new_word_list = []

# convert csv file using pandas
try:
    word_list = pd.read_csv(
        "/Users/amber_xin/Documents/自学/udemy/100 _codes_py/Day31_FlashCardProject/data/words_to_learn.csv")
except FileNotFoundError:
    word_list = pd.read_csv(
        "/Users/amber_xin/Documents/自学/udemy/100 _codes_py/Day31_FlashCardProject/data/wordlist1.csv")
finally:
    word_dict_list = word_list.to_dict(orient="records")


# generate new word
def generate_word():
    global current_word_dict, flip_timer
    if len(word_dict_list) == 0:
        messagebox.showinfo(message="Great! You have finished all words")
        window.destroy()
    else:
        window.after_cancel(flip_timer)
        current_word_dict = random.choice(word_dict_list)
        canvas.itemconfig(language_text, text="English", fill="black", font=LANGUAGE_FONT)
        canvas.itemconfig(word_text, text=current_word_dict["English"], fill="black", font=WORD_FONT)
        canvas.itemconfig(canvas_bg, image=font_pic)
        flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_bg, image=back_pic)
    canvas.itemconfig(language_text, text="中文", fill="white")
    canvas.itemconfig(word_text, text=current_word_dict["Chinese"], fill="white")


def remove_word():
    word_dict_list.remove(current_word_dict)
    unknown_word = pandas.DataFrame(word_dict_list)
    unknown_word.to_csv(
        "/Users/amber_xin/Documents/自学/udemy/100 _codes_py/Day31_FlashCardProject/data/words_to_learn.csv", index=False)
    generate_word()


# set up gui interface
window = Tk()
window.title("Flash Card")
window.minsize(width=800, height=726)
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# set up a font canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
font_pic = PhotoImage(
    file="/Users/amber_xin/Documents/自学/udemy/100 _codes_py/Day31_FlashCardProject/images/card_front.png")
back_pic = PhotoImage(
    file="/Users/amber_xin/Documents/自学/udemy/100 _codes_py/Day31_FlashCardProject/images/card_back.png")
canvas_bg = canvas.create_image(400, 263, image=font_pic)
canvas.grid(row=0, column=0, columnspan=2)

# set up text in canvas
language_text = canvas.create_text(400, 150, text="Language", font=LANGUAGE_FONT)
word_text = canvas.create_text(400, 263, text="word", font=WORD_FONT)

# set up button
wrong_img = PhotoImage(file="/Users/amber_xin/Documents/自学/udemy/100 _codes_py/Day31_FlashCardProject/images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=generate_word)
wrong_btn.grid(row=1, column=0)
right_img = PhotoImage(file="/Users/amber_xin/Documents/自学/udemy/100 _codes_py/Day31_FlashCardProject/images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=remove_word)
right_btn.grid(row=1, column=1)

generate_word()

window.mainloop()
