import time
from turtle import Screen
from player import Player
from car_manager_sol import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

score_board = Scoreboard()
player = Player()
cars_manager = CarManager()

# up key to move forward
screen.listen()
screen.onkey(player.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(cars_manager.move_speed)
    screen.update()
    cars_manager.create_car()
    cars_manager.move_cars()

    # reach the finish line
    if player.ycor() == player.finish_line:
        score_board.get_score()
        score_board.update_score()
        cars_manager.speed_up()
        player.reset_pos()

    # collision with cars
    for car in cars_manager.all_cars:
        if player.distance(car) < 20:
            score_board.game_over()
            game_is_on = False
