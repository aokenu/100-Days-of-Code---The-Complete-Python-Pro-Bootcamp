from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()
        self.shapesize(1, 2)
        self.goto(270, random.choice(range(-260, 260)))
        self.setheading(180)

    def moving_cars(self):
        self.forward(STARTING_MOVE_DISTANCE)

