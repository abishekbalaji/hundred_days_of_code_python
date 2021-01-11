from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.move_speed = MOVE_INCREMENT

    def create_car(self):
        if random.randint(1, 6) == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.pu()
            new_car.color(random.choice(COLORS))
            y_cor = random.randint(-240, 240)
            new_car.goto(300, y_cor)
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.backward(self.move_speed)

    def increase_difficulty(self):
        self.move_speed += MOVE_INCREMENT
