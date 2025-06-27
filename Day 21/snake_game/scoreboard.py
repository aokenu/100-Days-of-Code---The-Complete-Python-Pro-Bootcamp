from turtle import Turtle
from food import Food
from snake import Snake

ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")

class ScoreBoard(Food, Turtle):

    def __init__(self):
        super().__init__()
        self.live_score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.shape("square")
        self.color("white")
        self.hideturtle()
        self.penup()
        self.pencolor("white")

    def new_score(self):
        self.live_score += 1

    def display_score(self):
        self.goto(0, 280)
        self.clear()
        self.write(f"Score: {self.live_score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.live_score > self.high_score:
            self.high_score = self.live_score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)