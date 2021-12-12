from turtle import Turtle, Screen

import random

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
user_bet = screen.textinput(title="Make your bet", prompt="Which tutrle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


def create_turtle(colors):
    turtles = []
    for i in range(5):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[i])
        turtles.append(new_turtle)
    return turtles


turtle_list = create_turtle(colors)
for i in range(len(turtle_list)):
    turtle_list[i].penup()
    turtle_list[i].goto(x=-230, y=-100 + i * 50)

while True:
    for i in range(len(turtle_list)):
        if turtle_list[i].xcor() < 220:
            random_distance = random.randint(0, 10)
            turtle_list[i].forward(random_distance)
        else:
            winner_color = turtle_list[i].pencolor()
            if user_bet == winner_color:
                print(f"You've won! The {winner_color} turtle is the winner")
            else:
                print(f"You've lost! The {winner_color} turtle is the winner")

        break

screen.exitonclick()
