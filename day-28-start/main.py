import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
marker = turtle.Turtle()
marker.penup()
marker.hideturtle()

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state name?")
    title_state = answer_state.title()
    if title_state == "Exit":
        break
    if title_state in states:
        guessed_states.append(title_state)
        state_data = data[data.state == title_state]
        marker.goto(int(state_data.x), int(state_data.y))
        marker.write(title_state)

with open("missed_states.csv", "w") as file:
    for state in states:
        if state not in guessed_states:
            file.write(f"{state}\n")
screen.exitonclick()
