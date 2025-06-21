import time
from turtle import Turtle, Screen
import time

# Create a new screen
screen = Screen()

#Set up the screen to a defined size
screen.setup(width=600, height=600)

# Set up the screen background color
screen.bgcolor("black")

# Set up the title of the screen that shows up
screen.title("My Snake Game")

# Turn off tracer
screen.tracer(0)

segments = []
starting_position = [(0, 0), (-20, 0), (-40, 0)]



for segment in range(0, 3):
    snake = Turtle()
    snake.shape("square")
    snake.color("white")
    snake.penup()
    snake.goto(starting_position[segment])
    segments.append(snake)


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.5)

    for seg_num in range(len(segments) -1, 0, -1):
        new_x = segments[seg_num -1].xcor()
        new_y = segments[seg_num -1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
    segments[0].left(90)









screen.exitonclick()