from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        self.__x_move = 10
        self.__y_move = 10
        self.move_speed = 0.1

    def bounce_y(self):
        self.__y_move *= -1

    def bounce_x(self):
        self.__x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.__x_move, self.ycor() + self.__y_move)
