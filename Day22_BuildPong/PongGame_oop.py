from turtle import Screen, Turtle
from Paddle import Paddle
from Ball import Ball
import time

# Set up the screen
game_screen = Screen()
game_screen.bgcolor("black")
game_screen.setup(width=800, height=600)
game_screen.title("Pong")
game_screen.tracer(0)

# create paddle
right_paddle = Paddle()
right_paddle.goto((350, 0))
left_paddle = Paddle()
left_paddle.goto((-350, 0))

ball = Ball()
ball.setpos(135)
# respond to key presses
game_screen.listen()
game_screen.onkey(right_paddle.go_up, "Up")
game_screen.onkey(right_paddle.go_down, "Down")

game_screen.onkey(left_paddle.go_up, "w")
game_screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    game_screen.update()
    time.sleep(0.1)
    if ball.ycor() < 280:
        ball.move()
    else:
        ball.up_bouncing()
        ball.move()

    if ball.ycor() > -280:
        ball.move()
    else:
        ball.down_bouncing()
        ball.move()

game_screen.exitonclick()
