from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.write(arg=f"Score: {self.score}", move=False, align='center', font=('Arial', 16, 'normal'))

    def get_food(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align='center', font=('Arial', 16, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write(arg="Game Over", move=False, align="center", font=('Arial', 16, 'normal'))
