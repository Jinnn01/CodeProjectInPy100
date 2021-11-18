def turn_right():
    turn_left()
    turn_left()
    turn_left()


while True:
    if at_goal():
        break
    else:
        if front_is_clear() and wall_on_right():
            move()
        elif wall_in_front() and wall_on_right():
            turn_left()
        else:
            turn_right()
            move()

# sol with bug

