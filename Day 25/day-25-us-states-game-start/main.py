import turtle
from statemap import StateMap
from turtle import Screen
import pandas as pd

screen = turtle.Screen()
screen.title("US State Game")
image = "blank_states_img.gif"
screen.addshape(image)
state_data = "50_states.csv"

turtle.shape(image)
state_map = StateMap()

state_data = pd.read_csv(state_data)
correct_answer = []

is_game_on = True

while is_game_on:
    response = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
    # Filter the row where state matches the user's input
    matched_row = state_data[state_data["state"] == response]

    if response == "Exit":
        break

    if not matched_row.empty and response not in correct_answer:
        answered = len(correct_answer) + 1

        matched_state = matched_row["state"].item()
        matched_xcor = int(matched_row["x"].item())
        matched_ycor = int(matched_row["y"].item())

        correct_answer.append(matched_state)
        total_state = len(state_data["state"])
        scoreboard = f"{answered}/{total_state}"

        turtle.color("black")
        turtle.write(f"{scoreboard}", align="left", font=("Arial", 12, "normal"))
        print(scoreboard)

        state_map.goto(matched_xcor, matched_ycor)
        state_map.write(matched_state, align="center", font=("Arial", 12, "normal"))

        if len(correct_answer) == 50:
            is_game_on = False

    else:
        print(f"No match found for '{response}'")



screen.exitonclick()
