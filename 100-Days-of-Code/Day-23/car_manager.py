import random as r
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager:
    def __init__(self):
        self.all_cars=[]
        self.car_speed=STARTING_MOVE_DISTANCE

    def create_car(self):
        if r.randint(1,6) == 1:
            new_car=Turtle("square")
            new_car.penup()
            new_car.shapesize(1,2)
            new_car.color(r.choice(COLORS))
            random_y=r.randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed+=MOVE_INCREMENT
