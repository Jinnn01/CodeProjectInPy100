import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "/Users/amber_xin/Desktop/自学/udemy/100 _codes_py/Day25_WorkingwithCSVDataandPandasLibrary/us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv(
    "/Users/amber_xin/Desktop/自学/udemy/100 _codes_py/Day25_WorkingwithCSVDataandPandasLibrary/us-states-game-start/50_states.csv")
all_state = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the states",
                                    prompt="What's another state's name ?").title()

    if answer_state == "Exit":
        missing_state = []
        for state in all_state:
            if state not in guessed_states:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("StatesToLearn.csv")
        break

    #  if answer_state is one of the states in all the states of the csv file
    if answer_state in all_state:
        guessed_states.append(answer_state)
        # if they got it right
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data["x"]), int(state_data["y"]))
        t.write(answer_state)

# group unknown states into a csv
# get states which are not be inputted

# my solution for create a unlearnt states csv file
# remain_state = set(all_state) - set(guessed_states)
# remain_state = list(remain_state)
#
# state_x = []
# state_y = []
# for state in remain_state:
#     # get one state data - row
#     state_row = data[data.state == state]
#
#     !!!!bug!!!!!
#     state_x = state_x.append(int(state_row["x"]))
#     state_y = state_y.append(int(state_row["y"]))
#
# data_dict = {
#     "State": remain_state,
#     "X": state_x,
#     "Y": state_y
# }
#
# df = pandas.DataFrame(data_dict)
# df.to_csv("Remain_State.csv")




screen.exitonclick()
