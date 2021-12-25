from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.score = 0
        self.penup()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-220, 260)
        self.write(f"Level: {self.score}", align='center', font=FONT)

    def get_score(self):
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", align='center', font=FONT)
