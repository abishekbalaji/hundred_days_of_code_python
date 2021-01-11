# from turtle import Turtle, Screen
#
# turtwig = Turtle()
# turtwig.shape("turtle")
# turtwig.color("DeepSkyBlue4")
# turtwig.forward(100)
# turtwig.left(90)
# turtwig.goto(200, 300)
#
# new_screen = Screen()
#
# print(new_screen.canvwidth)
# new_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["Pokemon Name", "Type"]
table.add_rows([
    ["Lucario", "Fighting / Steel"],
    ["Gengar", "Ghost"],
    ["Darkrai", "Dark"],
    ["Absol", "Dark"],
    ["Dragonite", "Dragon / Flying"]
])

table.align = "l"

print(table)
