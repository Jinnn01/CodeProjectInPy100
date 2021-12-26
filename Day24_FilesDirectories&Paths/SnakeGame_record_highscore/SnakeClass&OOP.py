from turtle import Screen
import time
from snake_class import Snake
from Day21_food import Food
from scoreboard_class import Scoreboard

# set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with  food
    if snake.head.distance(food) < 15:
        score_board.increase_score()
        # print("nom nom nom")
        food.refresh()
        snake.extend()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 \
            or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.reset()
        snake.reset()


    # detect collision with tail
    # if head collides with any segment in the tail
        # trigger game over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            score_board.reset()
            snake.reset()


screen.exitonclick()
