from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("black")
        self.penup()
        self.current_level = 1
        self.clear()
        self.write(f"Level: {self.current_level}", align="left", font=("Courier", 14, "normal"))
        self.display_counter()

    def increase_level(self):
        self.current_level += 1

    def display_counter(self):
        self.goto(-300, 270)
        self.clear() # Clear previous level display
        self.write(f"Level: {self.current_level}", align="left", font=("Courier", 14, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=FONT)


