from turtle import Turtle
from food import Food
from snake import Snake

ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")

class ScoreBoard(Food):

    def __init__(self):
        super().__init__()
        self.live_score = 0
        self.sb = Turtle("square")
        self.sb.color("white")
        self.sb.hideturtle()
        self.sb.penup()
        self.sb.pencolor("white")

    def new_score(self):
        self.live_score += 1

    def display_score(self):
        self.sb.goto(0, 280)
        self.sb.clear()
        self.sb.write(f"Score : {self.live_score} ", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.sb.goto(0, 0)
        self.sb.write("GAME OVER!", align=ALIGNMENT, font=FONT)