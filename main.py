import turtle
import pandas as pd

from src.state import State

screen = turtle.Screen()
screen.title("U.S States Game")
screen.setup(width=725, height=491)


image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("./data/50_states.csv")
correct_guesses = []

while True:

    user_answer = screen.textinput("Name the state", "What's another state name?").title()

    state_data = data[data.state == user_answer]
    state_name = state_data["state"].item()
    state_x_coor = state_data["x"].item()
    state_y_coor = state_data["y"].item()

    
    state = State(state_name, state_x_coor, state_y_coor)
    state.place()
    
    # state_turtle = turtle.Turtle()
    # state_turtle.penup()
    # state_turtle.hideturtle()
    # x_coor = state_data["x"].item()
    # y_coor = state_data["y"].item()

    # state_turtle.goto(x=x_coor, y=y_coor)
    # state_turtle.write(arg=state_data["state"].item()) 


screen.mainloop()