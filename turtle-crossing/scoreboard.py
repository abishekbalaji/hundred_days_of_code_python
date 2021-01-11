from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")
FONT_GAME_OVER = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.pu()
        self.hideturtle()
        self.goto(-250, 270)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", move=False, align=ALIGNMENT, font=FONT)

    def level_up(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT_GAME_OVER)
