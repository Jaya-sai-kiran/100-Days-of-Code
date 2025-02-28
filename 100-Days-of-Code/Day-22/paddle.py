from turtle import Turtle, Screen

PADDLE_MOVE=20
COLOR="white"

My_screen=Screen()

class Paddle:
    def __init__(self):
        self.paddles=[]
        self.center_line()
        self.create_bars()

    def create_bars(self,):
        for i in [180,0]:
            bar=Turtle("square")
            bar.color(COLOR)
            bar.penup()
            bar.shapesize(0.5,3)
            bar.setheading(i)
            bar.forward(480)
            if i == 180:
                bar.forward(8)
            bar.setheading(90)
            self.paddles.append(bar)

    def center_line(self):
        pen1 = Turtle("arrow")
        pen2 = Turtle("arrow")
        pen1.color(COLOR)
        pen2.color(COLOR)
        pen1.setheading(90)
        pen2.setheading(270)
        self.dashed_line(pen1)
        self.dashed_line(pen2)

    @staticmethod
    def dashed_line(pen):
        for _ in range(15):
            pen.forward(10)
            pen.penup()
            pen.forward(10)
            pen.pendown()

    #Paddles moving functions
    def up_right(self):
        if self.paddles[1].ycor() < 255:
            self.paddles[1].forward(PADDLE_MOVE)

    def down_right(self):
        if self.paddles[1].ycor() > -250:
            self.paddles[1].backward(PADDLE_MOVE)

    def up_left(self):
        if self.paddles[0].ycor() < 250:
            self.paddles[0].forward(PADDLE_MOVE)

    def down_left(self):
        if self.paddles[0].ycor() > -250:
            self.paddles[0].backward(PADDLE_MOVE)