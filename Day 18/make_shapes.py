from turtle import Turtle, Screen

timmy_the_turtle = Turtle()

class DrawSquare:

    def __init__(self):
        self.turns = range(0, 4)

    def draw_square(self):
            timmy_the_turtle.color("blue")
            timmy_the_turtle.right(120)
            for i in range(4):
                timmy_the_turtle.forward(100)
                timmy_the_turtle.right(90)


    def draw_triangle(self):
            timmy_the_turtle.color("black")
            for i in range(2):
                timmy_the_turtle.forward(100)
                timmy_the_turtle.right(120)
            timmy_the_turtle.forward(100)


    def draw_pentagom(self):
            timmy_the_turtle.color("red")
            for i in range(5):
                timmy_the_turtle.forward(100)
                timmy_the_turtle.right(72)

    def draw_hexagon(self):
            timmy_the_turtle.color("brown")
            for i in range(6):
                timmy_the_turtle.forward(100)
                timmy_the_turtle.right(60)

    def draw_heptagon(self):
            timmy_the_turtle.color("green")
            for i in range(7):
                timmy_the_turtle.forward(100)
                timmy_the_turtle.right(51.4)

    def draw_octagon(self):
            timmy_the_turtle.color("indigo")
            for i in range(8):
                timmy_the_turtle.forward(100)
                timmy_the_turtle.right(45)

    def draw_nonagon(self):
            timmy_the_turtle.color("purple")
            for i in range(9):
                timmy_the_turtle.forward(100)
                timmy_the_turtle.right(40)

    def draw_decagon(self):
            timmy_the_turtle.color("cyan")
            for i in range(10):
                timmy_the_turtle.forward(100)
                timmy_the_turtle.right(36)