from turtle import Turtle, Screen

# import random

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


def create_turtle(colors):
    turtle_list = []
    for i in range(5):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[i])
        turtle_list.append(new_turtle)
    return turtle_list


turtle_list = create_turtle(colors)
for i in range(len(turtle_list)):
    turtle_list[i].penup()
    turtle_list[i].goto(x=-230, y=-100 + i * 50)

screen.exitonclick()
