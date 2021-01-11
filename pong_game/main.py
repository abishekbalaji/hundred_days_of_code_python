from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if scoreboard.l_score == 10:
        game_is_on = False
        print("Left player wins!")

    elif scoreboard.r_score == 10:
        game_is_on = False
        print("Right player wins!")

    else:
        # Detect collision with top and bottom walls
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # Detect collisions with paddle
        if ball.xcor() > 325 and ball.distance(r_paddle) < 50 or ball.xcor() < -325 and ball.distance(l_paddle) < 50:
            ball.bounce_x()

        if ball.xcor() > 400:
            ball.reset_position()
            scoreboard.increase_l_score()

        if ball.xcor() < -400:
            ball.reset_position()
            scoreboard.increase_r_score()

screen.exitonclick()
