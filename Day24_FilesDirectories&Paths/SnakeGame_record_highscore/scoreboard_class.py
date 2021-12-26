# lecture solution
from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt","r") as open_file:
            self.high_score = int(open_file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(arg=f"Score:{self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt","w") as open_file:
                open_file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
