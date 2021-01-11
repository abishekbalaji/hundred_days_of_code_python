import turtle as t
import random

# colors = ["blue", "CadetBlue", "gray0", "DeepSkyBlue4", "firebrick", "DodgerBlue", "red", "gold",
#           "orange", "green", "orchid", "salmon"]

turtwig = t.Turtle()
t.colormode(255)
turtwig.shape("turtle")


# Square
# for _ in range(4):
#     turtwig.fd(100)
#     turtwig.right(90)

# Dashed line
# for _ in range(50):
#     turtwig.fd(5)
#     turtwig.pu()
#     turtwig.fd(5)
#     turtwig.pd()

# Shapes

# def angle(sides):
#     return 360 / sides
#
#
# def choose_color():
#     # color_choice = choice(colors)
#     # colors.remove(color_choice)
#     turtwig.color(choice(colors))


# def triangle():
#     choose_color()
#     for _ in range(3):
#         turtwig.right(angle(3))
#         turtwig.fd(100)
#
#
# def square():
#     choose_color()
#     for _ in range(4):
#         turtwig.right(angle(4))
#         turtwig.fd(100)
#
#
# def pentagon():
#     choose_color()
#     for _ in range(5):
#         turtwig.right(angle(5))
#         turtwig.fd(100)
#
#
# def hexagon():
#     choose_color()
#     for _ in range(6):
#         turtwig.right(angle(6))
#         turtwig.fd(100)
#
#
# def heptagon():
#     choose_color()
#     for _ in range(7):
#         turtwig.right(angle(7))
#         turtwig.fd(100)
#
#
# def octagon():
#     choose_color()
#     for _ in range(8):
#         turtwig.right(angle(8))
#         turtwig.fd(100)
#
#
# def nonagon():
#     choose_color()
#     for _ in range(9):
#         turtwig.right(angle(9))
#         turtwig.fd(100)
#
#
# def decagon():
#     choose_color()
#     for _ in range(10):
#         turtwig.right(angle(10))
#         turtwig.fd(100)
#
#
# triangle()
# square()
# pentagon()
# hexagon()
# heptagon()
# octagon()
# nonagon()
# decagon()

# OR------------------------------

# def draw_shape(sides):
#     choose_color()
#     for _ in range(sides):
#         turtwig.right(angle(sides))
#         turtwig.fd(100)
#
#
# for num_of_sides in range(3, 11):
#     draw_shape(num_of_sides)


# Random Walk

# def forward():
#     turtwig.fd(30)
#
#
# def backward():
#     turtwig.bk(30)
#
#
# def left():
#     turtwig.left(90)
#     turtwig.fd(30)
#
#
# def right():
#     turtwig.right(90)
#     turtwig.fd(30)
#
#
# def direction():
#     directions = [forward, backward, left, right]
#     choice(directions)()

def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


# directions = [0, 90, 180, 270]
#
# turtwig.pensize(10)
# turtwig.speed(1)
#
# for _ in range(100):
#     turtwig.color(random_color())
#     turtwig.fd(30)
#     turtwig.setheading(random.choice(directions))

# Spirograph


turtwig.speed("fastest")


def draw_spirograph(size):
    for _ in range(int(360 / size)):
        turtwig.color(random_color())
        turtwig.circle(100)
        turtwig.setheading(turtwig.heading() + size)


draw_spirograph(10)


screen = t.Screen()
screen.exitonclick()
