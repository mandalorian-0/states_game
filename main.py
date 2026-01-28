import turtle

screen = turtle.Screen()
screen.title("U.S States Game")
screen.setup(width=725, height=491)


image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


user_answer = screen.textinput("Name the state", "What's another state name?")

screen.mainloop()