from turtle import Screen
from timmy import Timmy
from car import CarManager
from scoreboard import Scoreboard
import time

CAR_FREQUENCY = 6

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Cross")
screen.tracer(0)

timmy = Timmy()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(timmy.move_up, "Up")

turns = 0
game_running = True
while game_running:
    turns += 1
    time.sleep(0.1)
    screen.update()
    if turns % CAR_FREQUENCY == 0:
        car.create_car()
        turns -= CAR_FREQUENCY
    car.move_car()

    # Remove cars that passed off of visible screen from all_cars list
    for any_car in car.all_cars:
        if any_car.xcor() < -300:
            any_car.hideturtle()
            car.all_cars.remove(any_car)

    # Detect collision with car
    for any_car in car.all_cars:
        if any_car.distance(timmy) < 20:
            scoreboard.game_over()
            game_running = False

    # Detect turtle passed across successfully
    if timmy.success():
        timmy.startup()
        car.levelup_car()
        scoreboard.update_score()

screen.exitonclick()
