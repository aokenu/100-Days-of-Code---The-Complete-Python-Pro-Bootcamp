from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard
import turtle


# Create a new screen
screen = Screen()

#Set up the screen to a defined size
screen.setup(width=800, height=600)

# Set up the screen background color
screen.bgcolor("black")

# Set up the title of the screen that shows up
screen.title("Pong Game")
screen.listen()
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
score = ScoreBoard()

is_game_on = True


screen.onkey(l_paddle.move_up, "w" )
screen.onkey(l_paddle.move_down, "s" )
screen.onkey(r_paddle.move_up, "Up" )
screen.onkey(r_paddle.move_down, "Down" )

ball_speed = 0.05

while is_game_on:
    screen.update()
    time.sleep(ball_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Detect collision with r_paddle
    if ball.distance(r_paddle.pad) < 50 and ball.xcor() > 320:
        ball_speed -= 0.001
        ball.bounce_x()

    if ball.distance(l_paddle.pad) < 50 and ball.xcor() < -320:
        ball_speed -= 0.001
        ball.bounce_x()

    # Detect when r_paddle misses the ball
    if ball.xcor() > 400:
        ball.reset_position()
        ball.bounce_x()
        score.clear()
        score.l_point()

    # Detect when l_paddle misses the ball
    if ball.xcor() < -400:
        ball.reset_position()
        ball.bounce_x()
        score.clear()
        score.r_point()

screen.exitonclick()