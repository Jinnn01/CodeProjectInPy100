'''
W - forwards
S - Backwards
A - Counter - Clockwise
D - Clockwise
C - Clean the drawing
'''
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def counter_clock_wise():
    tim.left(15)


def clock_wise():
    tim.right(15)


def clean_drawing():
    tim.clear()
    tim.penup()
    tim.home()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=counter_clock_wise)
screen.onkey(key="d", fun=clock_wise)
screen.onkey(key="c", fun=clean_drawing)
screen.exitonclick()
