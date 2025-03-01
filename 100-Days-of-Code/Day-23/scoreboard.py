from turtle import Turtle

FONT = ("Courier", 22, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        self.level=1
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280,260)
        self.score_board()

    def score_board(self):
        self.clear()
        self.write(arg=f"Level:{self.level}",font=FONT)

    def increase_level(self):
        self.level+=1
        self.score_board()

    def game_over(self):
        self.goto(0,0)
        self.write(arg="Game Over",align="center",font=FONT)
