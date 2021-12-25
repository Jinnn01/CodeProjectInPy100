from turtle import Turtle
from random import randint,choice
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.y_pos = randint(-250,250)
        self.create_car()

    def create_car(self):
        self.shape("square")
        self.shapesize(stretch_wid=1,stretch_len=2)
        self.penup()
        self.color(choice(COLORS))
        self.goto((280,self.y_pos))
        self.all_cars.append(self.pos())

    def car_move(self):
        for cars_pos in self.all_cars:
            new_pos = cars_pos - (STARTING_MOVE_DISTANCE,0)
            self.goto(new_pos)

    def restart(self):
        self.all_cars=[]


