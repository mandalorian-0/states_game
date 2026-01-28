from turtle import Turtle

class State(Turtle):
    def __init__(self, name, x_coor, y_coor):
        super().__init__()
        self.name = name
        self.x_coor = x_coor
        self.y_coor = y_coor

        self.penup()
        self.hideturtle()

    def place(self):
        self.goto(x=self.x_coor, y=self.y_coor)
        self.write(arg=self.name) 