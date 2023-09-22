from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("#021513")
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball(36.87)

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

is_game_on = True
while is_game_on:
    ball.move()
    screen.update()


screen.exitonclick()
