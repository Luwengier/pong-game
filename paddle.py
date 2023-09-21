from turtle import Turtle


MOVE_DISTANCE = 30


class Paddle(Turtle):
    def __init__(self, position) -> None:
        super().__init__(shape="square")
        self.speed("fastest")
        self.color("white")
        self.penup()
        self.goto(position)
        self.setheading(90)
        self.shapesize(stretch_len=5, stretch_wid=1)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.backward(MOVE_DISTANCE)
