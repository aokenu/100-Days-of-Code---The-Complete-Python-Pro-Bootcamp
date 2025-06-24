import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)
screen.listen()

turtle_player = Player()
score = Scoreboard()

screen.onkey(turtle_player.move_turtle, "Up")

car_list = []  # To store all car instances
game_is_on = True
loop_count = 0  # New counter variable

while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Move all cars
    for car in car_list:
        car.moving_cars()

    loop_count += 1
    if loop_count % 12 == 0:
        new_car = CarManager()
        car_list.append(new_car)

    for car in car_list:
        if turtle_player.distance(car) < 20:
            game_is_on = False
            score.game_over()

    if turtle_player.distance(0, 300) < 20:
        score.current_level += 1
        turtle_player.clear()
        score.display_counter()
        turtle_player.return_to_start()
        print("Reached finish line")


screen.exitonclick()