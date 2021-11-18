# Reeborg maze

Reeborg was exploring a dark maze and the battery in its flashlight ran out.

- Write a program using an if/elif/else statement so Reeborg can find the exit. The secret is to have Reeborg follow along the right edge of the maze, turning right if it can, going straight ahead if it can’t turn right, or turning left as a last resort.

- What you need to know:

    The functions `move()` and `turn_left()`.
Either the test `front_is_clear()` or `wall_in_front()`, `right_is_clear()` or `wall_on_right()`, and `at_goal()`.
How to use a while loop and if/elif/else statements.
It might be useful to know how to use the negation of a test (not in Python).

## Idea:
- along the right wall
### Three situations:
1. front is clear and wall on right:

    action: *move*
2. wall in front and wall on right:

    action: *turn left*
    
3. other:

    action: *turn right and move*
## BUG problem
when the robot's right side is clear,code tells to turn the direction and move forward and check whether it is at goal
depending on the facing, there might not be a wall on the right side of the robot(key)
### To solve the question
get the robot a start position, where the wall is right side of the robot
