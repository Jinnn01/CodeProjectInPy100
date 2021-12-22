from turtle import Turtle


class Score_board(Turtle):
    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(position)
        self.score = 0
        self.write(arg=f"{self.score}", move=False, align='center', font=('Arial', 20, 'normal'))

    def get_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"{self.score}", move=False, align='center', font=('Arial', 20, 'normal'))
