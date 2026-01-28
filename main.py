import turtle
import pandas as pd

from src.state import State
from src.score import Score

screen = turtle.Screen()
screen.title("U.S States Game")
screen.setup(width=725, height=491)

image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("./data/50_states.csv")
correct_guesses = []

score = Score()

while score.has_guessed_all():

    user_answer = screen.textinput(f"{score.show_score()}/{len(data)} States Correct", "What's another state name?").title()
    
    state_data = data[data.state == user_answer]

    if state_data.empty:
        turtle.TK.messagebox.showerror(title="Result", message=f"No state name '{user_answer}'")
        continue
    
    if state_data["state"].item() in correct_guesses:
        turtle.TK.messagebox.showinfo(title="Info", message=f"'{user_answer}' already guessed")
        continue

    state_data = data[data.state == user_answer]
    state_name = state_data["state"].item()
    state_x_coor = state_data["x"].item()
    state_y_coor = state_data["y"].item()

    
    state = State(state_name, state_x_coor, state_y_coor)
    state.place()
    score.increase_score()

    correct_guesses.append(state_data["state"].item())

screen.mainloop()