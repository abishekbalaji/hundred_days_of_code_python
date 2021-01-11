from turtle import Turtle, Screen

turtwig = Turtle()


def move_forwards():
    turtwig.fd(10)


def move_backwards():
    turtwig.bk(10)


def turn_left():
    turtwig.left(10)


def turn_right():
    turtwig.right(10)


def clear():
    turtwig.clear()
    turtwig.pu()
    turtwig.home()
    turtwig.pd()


screen = Screen()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
