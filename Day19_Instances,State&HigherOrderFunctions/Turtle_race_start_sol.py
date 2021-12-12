from turtle import Turtle, Screen

# import random

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


for turtle_index in range(0,6):
    tim = Turtle(shape ="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230, y=-125 + turtle_index * 50)

screen.exitonclick()
