from turtle import Turtle
import random

colours = ["red", "orange", "yellow", "green", "blue", "purple", "violet"]
INITIAL_SPEED = 5
SPEED_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.move_speed = INITIAL_SPEED

    def create_car(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.color(random.choice(colours))
        new_car.resizemode("user")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.setheading(180)
        random_ycor = random.randint(-250, 250)
        new_car.goto(300, random_ycor)
        self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.forward(self.move_speed)

    def levelup_car(self):
        self.move_speed += SPEED_INCREMENT
