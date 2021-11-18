def turn_right():
    turn_left()
    turn_left()
    turn_left()

# initial the start direction
while not is_facing_north():
    turn_left()
    if front_is_clear() and right_is_clear():
        move()

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


# sol
'''
while not at_goal():
    if right_is_clear():
       turn_right()
    elif front_is_clear():
       move()
    else:
       turn_left()
'''