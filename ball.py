from turtle import Turtle


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__(shape="circle")
        self.color("white")
        self.penup()
        # self.goto(0, 0)
        # self.speed(3)
        # self.setheading(angle)

    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)
