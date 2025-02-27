from turtle import Turtle

ALIGNMENT="center"
FONT=("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.score_board()

    def score_board(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score:{self.score}",align=ALIGNMENT,font=FONT )

    def game_over(self):
        self.goto(0,10)
        self.write(arg="Game over", align=ALIGNMENT, font=FONT)
        self.goto(0,-10)
        self.write(arg=f"Score:{self.score}", align=ALIGNMENT, font=FONT)