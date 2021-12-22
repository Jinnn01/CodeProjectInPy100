from turtle import Screen, Turtle
from Paddle_sol import Paddle
from Ball_sol import Ball
import time
from Score_board_sol import Score_board

# Set up the screen
game_screen = Screen()
game_screen.bgcolor("black")
game_screen.setup(width=800, height=600)
game_screen.title("Pong")
game_screen.tracer(0)

# create paddle
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
score_board = Score_board()

# respond to key presses
game_screen.listen()
game_screen.onkey(right_paddle.go_up, "Up")
game_screen.onkey(right_paddle.go_down, "Down")

game_screen.onkey(left_paddle.go_up, "w")
game_screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    game_screen.update()
    ball.move()

    # Detect wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # need to bounce
        ball.bounce_y()
    # Detect collision with paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or\
            ball.distance(left_paddle)<50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when paddle misses
    if ball.xcor() > 380:
        ball.reset_pos()
        score_board.l_point()

    if ball.xcor() < -380:
        ball.reset_pos()
        score_board.r_point()








game_screen.exitonclick()
