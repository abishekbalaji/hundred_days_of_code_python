import math


def five_percent(num):
    return math.ceil(num + (num * 0.05))


while True:
    print(five_percent(int(input("num: "))))
