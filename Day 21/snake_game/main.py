import time
from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
import turtle
from scoreboard import ScoreBoard

import turtle

ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")

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
score.pencolor("white")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.new_score()
        score.display_score()

    # Detect collision with wall.
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        game_is_on = False
        score.game_over()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()