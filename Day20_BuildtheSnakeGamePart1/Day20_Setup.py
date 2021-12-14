from turtle import Screen, Turtle
import time
# set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# body list
snake_body = []

# create three turtles
for i in range(3):
    # set up the snake body
    square_body = Turtle()
    square_body.penup()
    square_body.shape("square")
    square_body.color("white")
    square_body.goto(-i * 20, 0)
    snake_body.append(square_body)

while True:
    screen.update()
    time.sleep(0.1)
    # make the snake keep moving,from last one to the head
    for body_pos in range(len(snake_body) - 1, 0, -1):
        new_pos = snake_body[body_pos - 1].pos()
        snake_body[body_pos].goto(new_pos)
    snake_body[0].forward(20)




    

screen.exitonclick()
