from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.goto(0,0)

    def setpos(self,angle):
        self.left(angle)

    def move(self):
        self.forward(10)

    def down_bouncing(self):
        self.right(90)

    def up_bouncing(self):
        self.left(90)




