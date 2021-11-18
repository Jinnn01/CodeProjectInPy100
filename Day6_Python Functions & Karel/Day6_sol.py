def turn_right():
    turn_left()
    turn_left()
    turn_left()

# check whether the front is clear
while front_is_clear():
    # seek for a wall, go forward until it reaches a wall
    move()
# once reach the wall let the robot turn left, make the wall on its right side
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
    elif front_is_clear():
        move()
    else:
        turn_left()