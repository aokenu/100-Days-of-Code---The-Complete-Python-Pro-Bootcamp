from turtle import Turtle, Screen
import turtle
import random

turtle.colormode(255)

"""First possible solution"""

# Define possible colors
colors = ['black', 'blue', 'red', 'brown', 'green', 'pink', 'cyan', 'indigo']
direction = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


# Setup turtle
ninja_turtle = Turtle()
ninja_turtle.shape("turtle")
turtle.speed(0)
ninja_turtle.turtlesize(5)
ninja_turtle.pensize(30)


for i in range(200):
    ninja_turtle.forward(100)
    ninja_turtle.setheading(random.choice(direction))
    # ninja_turtle.color(random.choice(colors))
    color_pick = random_color()
    ninja_turtle.color(color_pick)




"""Second possible solution"""
# # Define possible directions as lambdas
# directions = [
#     lambda t: t.left(90),
#     lambda t: t.right(90),
#     lambda t: t.forward(100),
#     lambda t: t.backward(100)
# ]
#
#
#
# # Class to control turtle movement
# class TurtleMove:
#     def __init__(self, turtle):
#         self.turtle = turtle
#
#     def make_move(self):
#         move_func = random.choice(directions)
#         color_choice = random.choice(colors)
#         self.turtle.color(color_choice)
#         move_func(self.turtle)
#
# # Create a turtle mover
# tim = TurtleMove(ninja_turtle)
#
# is_on = True
# # Move the turtle a few times
# while is_on:
#     tim.make_move()


# Keep the screen open
screen = Screen()
screen.exitonclick()
