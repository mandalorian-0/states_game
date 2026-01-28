import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
screen.setup(width=725, height=491)


image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("./data/50_states.csv")

while True:

    user_answer = screen.textinput("Name the state", "What's another state name?").title()


    state_data = data[data.state == user_answer]

    state_turtle = turtle.Turtle()
    state_turtle.penup()
    state_turtle.hideturtle()
    x_coor = state_data["x"].values[0]
    y_coor = state_data["y"].values[0]

    state_turtle.goto(x=x_coor, y=y_coor)
    state_turtle.write(arg=state_data["state"].values[0])



screen.mainloop()