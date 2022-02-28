from tkinter import *

THEME_COLOR = "#375362"
FONT = ("Ariel", 20, "italic")


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR)
        # SCORE BROAD
        self.score = 0
        self.score_broad = Label(text=f"Score:{self.score}")
        self.score_broad.config(pady=20, background=THEME_COLOR, foreground="white")
        self.score_broad.grid(row=0, column=1)

        # canvas for
        self.Canvas = Canvas(width=300, height=250)
        self.Canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        self.question = self.Canvas.create_text(150, 125, text="Here is a question", font=FONT)

        # BUTTONS
        self.truepic = PhotoImage(
            file="/Users/amber_xin/Documents/自学/udemy/100 _codes_py/Day34_API_Practice_CreatingAGUI_Quiz/images/true.png")
        self.falsepic = PhotoImage(
            file="/Users/amber_xin/Documents/自学/udemy/100 _codes_py/Day34_API_Practice_CreatingAGUI_Quiz/images/false.png")
        self.known_button = Button(image=self.truepic, highlightthickness=0, highlightbackground=THEME_COLOR)
        self.known_button.grid(row=2, column=0, pady=20)
        self.unknown_button = Button(image=self.falsepic, highlightthickness=0, highlightbackground=THEME_COLOR)
        self.unknown_button.grid(row=2, column=1, pady=20)

        self.window.mainloop()  # set program to run
