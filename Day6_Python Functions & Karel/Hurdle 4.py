def turn_right():
    turn_left()
    turn_left()
    turn_left()


def climb():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()


'''for i in range(6):
    climb()
    turn_left()
'''


def climb2():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


'''   
while not at_goal():
    if wall_in_front():
        climb2()
    else:
        move()
'''
# hurdle 4

while True:
    if at_goal():
        break
    else:
        if wall_in_front() and wall_on_right():
            turn_left()
        if front_is_clear() and wall_on_right():
            move()
        if not wall_on_right():
            turn_right()
            move()
            turn_right()
            move()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
