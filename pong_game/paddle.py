from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.pu()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def up(self):
        self.goto(self.xcor(), self.ycor() + 30)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 30)
