from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.turtlesize(5, 1)
        self.color("white")
        self.shape("square")
        self.penup()
        self.setposition(position)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 20)

