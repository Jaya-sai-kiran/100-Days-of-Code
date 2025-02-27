from turtle import Turtle,Screen
import time

My_screen=Screen()
DISTANCE=20
SLEEP_TIME=0.2
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.snakes = []
        x = 0
        for i in range(3):
            self.create_snake()
            self.snakes[i].goto(x=x, y=0)
            x+=-20
            My_screen.update()
        self.head = self.snakes[0]

    def create_snake(self):
        tim = Turtle("square")
        tim.penup()
        tim.color("white")
        self.snakes.append(tim)

    def body_move(self):
        for i in range(len(self.snakes) - 1, 0, -1):
            x = self.snakes[i - 1].xcor()
            y = self.snakes[i - 1].ycor()
            self.snakes[i].goto(x=x, y=y)

    def move_forward(self):
        self.body_move()
        self.head.forward(DISTANCE)
        My_screen.update()
        time.sleep(SLEEP_TIME)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

