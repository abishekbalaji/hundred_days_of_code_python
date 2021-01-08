from random import choice
from os import system

from data import data
from art import logo, vs


def pick_from_list(data):
    if len(data) == 0:
        return (None, data)
    option = choice(data)
    data.remove(option)
    return (option, data)


def higher(a, b):
    return ("A", "B")[a['follower_count'] < b['follower_count']]


def statement(a, b):
    print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}")
    print(vs)
    print(f"Against B: {b['name']}, {b['description']}, from {b['country']}")
    answer = input("Who has more followers? Type 'A' or 'B': ")
    return answer


game = True
score = 0
(a, data) = pick_from_list(data)

print(logo)

while game:
    (b, data) = pick_from_list(data)
    if b == None:
        print("Awesome! You got everything right!")
        print(
            f"{a['name']}, {a['description']}, from {a['country']}, has {a['follower_count']}M followers on Instagram!")
        game = False
        break
    print(f"Correct answer: {higher(a,b)}")
    answer = statement(a, b)
    if answer == higher(a, b):
        score += 1
        system("clear")
        print(logo)
        print(f"You are right! Current score: {score}")
        if answer == "B":
            a = b
    else:
        game = False
        print(f"Sorry that's wrong. Final score: {score}")
