from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("#021513")
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

is_game_on = True
while is_game_on:
    screen.update()


screen.exitonclick()
