# import colorgram
import turtle as t
import random

t.colormode(255)
# colors = colorgram.extract('h-painting.jpg', 20)
turtwig = t.Turtle()
turtwig.shape("turtle")
turtwig.speed("fastest")
colors_list = [(236, 35, 108), (222, 231, 237), (145, 28, 65), (239, 74, 34), (6, 148, 93), (231, 238, 234),
               (232, 168, 40), (184, 158, 46), (44, 191, 233), (27, 127, 195), (126, 193, 74), (253, 223, 0),
               (85, 28, 93), (172, 36, 98), (246, 219, 44), (42, 172, 112), (216, 130, 165), (216, 58, 26)]
# for color in colors:
#     colors_list.append((color.rgb.r, color.rgb.g, color.rgb.b))
#
# print(colors_list)
x = 0

# for _ in range(10):
#     for __ in range(10):
#         turtwig.dot(20, random.choice(colors_list))
#         turtwig.pu()
#         turtwig.fd(50)
#         turtwig.pd()
#     turtwig.pu()
#     x += 50
#     turtwig.sety(x)
#     turtwig.setx(0)
#
#     turtwig.pd()

turtwig.pu()
turtwig.hideturtle()
turtwig.setheading(225)
turtwig.forward(300)
turtwig.setheading(0)

num_of_dots = 100

for dot_count in range(1, num_of_dots + 1):
    turtwig.dot(20, random.choice(colors_list))
    turtwig.fd(50)
    if dot_count % 10 == 0:
        turtwig.sety(turtwig.ycor() + 50)
        turtwig.setx(turtwig.xcor() - 500)

screen = t.Screen()
screen.exitonclick()
