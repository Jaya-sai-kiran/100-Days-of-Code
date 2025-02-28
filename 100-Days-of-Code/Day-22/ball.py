from turtle import Turtle
import random as r

BALL_MOVE=10

class Ball(Turtle):
    def __init__(self):
        self.angles=[10,20,30,40,50,60,120,130,140,150,160,170,190,200,210,220,230,240,300,310,320,330,340,350]
        self.ang=r.choice(self.angles)
        super().__init__("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("white")
        self.speed("fastest")

    def move_ball(self):
        self.forward(BALL_MOVE)

    def start_ball(self):
        self.setheading(self.ang)
        self.forward(BALL_MOVE)

    def reflect_ball(self):
        self.ang=360-self.ang
        self.setheading(self.ang)

    def paddle_hit(self):
        self.ang=180-self.ang
        self.setheading(self.ang)