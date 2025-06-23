from turtle import Turtle
import turtle


class Paddle:
    def __init__(self, x_axis, y_axis):
        self.pad = Turtle("square")
        self.pad.color("white")
        self.pad.turtlesize(stretch_len=1, stretch_wid=5)
        self.pad.penup()
        self.pad.goto(x_axis, y_axis)


    def move_up(self):
        y = self.pad.ycor()
        self.pad.sety(y + 20)

    def move_down(self):
        y = self.pad.ycor()
        self.pad.sety(y - 20)

