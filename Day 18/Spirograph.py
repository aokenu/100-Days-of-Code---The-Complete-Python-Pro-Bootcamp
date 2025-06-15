from turtle import Turtle, Screen
import random
import turtle

turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    r_color = (r, g, b)
    return r_color


tim = Turtle()
tim.shape("turtle")
tim.speed(15)
tim.turtlesize(1)
tim.pensize(5)


for i in range(18):
    tim.circle(100)
    tim.pencolor(random_color())
    tim.left(20)