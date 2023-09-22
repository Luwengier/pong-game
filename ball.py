from turtle import Turtle


class Ball(Turtle):
    def __init__(self, angle) -> None:
        super().__init__(shape="circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.speed(3)
        self.setheading(angle)

    def move(self):
        self.forward(10)
