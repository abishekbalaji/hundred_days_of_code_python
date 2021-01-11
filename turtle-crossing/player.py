from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.shape("turtle")
        self.start_over()
        self.setheading(90)

    def move(self):
        self.forward(20)

    def start_over(self):
        self.goto(0, -260)
