import turtle
import pandas as pd

# screen set up
screen = turtle.Screen()
screen.title("U.S States Game")
image = "/Users/amber_xin/Desktop/自学/udemy/100 _codes_py/Day25_WorkingwithCSVDataandPandasLibrary/us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# csv file set up
file_path = "/Users/amber_xin/Desktop/自学/udemy/100 _codes_py/Day25_WorkingwithCSVDataandPandasLibrary/us-states-game-start/50_states.csv"
state_data = pd.read_csv(file_path)

times = 0
score = 0
while times <= 50:
    # ask user input
    answer_state = screen.textinput(title=f"{score}/50 Guess the states", prompt="What's another state's name ?")
    # get state data
    state_input = answer_state.capitalize()
    state_column = state_data["state"]
    state_row = state_data[state_column == state_input]
    # check does input state exit?
    if state_row.empty:
        pass
    else:
        score += 1
        # get state pos
        x_pos = int(state_row["x"])
        y_pos = int(state_row["y"])

        # set a turtle go to that pos
        state_answer = turtle.Turtle()
        state_answer.penup()
        state_answer.hideturtle()
        state_answer.goto(x_pos, y_pos)
        state_answer.write(arg=f"{state_input}", font=("Courier", 12, "normal"))

    times += 1

screen.exitonclick()
