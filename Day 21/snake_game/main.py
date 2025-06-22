import time
from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
import turtle
from scoreboard import ScoreBoard

import turtle

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


snake = Snake()
food = Food()
score = ScoreBoard()


screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

snake.create_snake()
score.display_score()


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        score.new_score()
        score.display_score()




screen.exitonclick()