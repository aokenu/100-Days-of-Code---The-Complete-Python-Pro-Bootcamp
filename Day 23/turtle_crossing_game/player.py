from turtle import Turtle
from car_manager import CarManager

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.shapesize(1, 1)
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_turtle(self):
        self.forward(MOVE_DISTANCE)

    def return_to_start(self):
        self.goto(STARTING_POSITION)
