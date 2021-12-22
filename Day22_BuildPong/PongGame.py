from turtle import Screen, Turtle
from Ball import Ball
from Paddle import Paddle

# Set up the screen
game_screen = Screen()
game_screen.bgcolor("black")
game_screen.setup(width=800, height=600)
game_screen.title("Pong")
game_screen.tracer(0)

ball = Ball()
ball.start_move()

# creat paddle and respond to key presses
paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350, 0)


def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


# respond to key presses
game_screen.listen()
game_screen.onkey(go_up, "Up")
game_screen.onkey(go_down, "Down")

game_is_on = True
while game_is_on:
    game_screen.update()

game_screen.exitonclick()
