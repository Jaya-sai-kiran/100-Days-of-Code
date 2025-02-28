from turtle import Turtle

ALIGNMENT="center"
FONT=("Courier", 20, "normal")

class Scoreboard():
    def __init__(self):
        self.start_game()

    def start_game(self):
        self.start_tom=Turtle()
        self.start_tom.color("white")
        self.start_tom.penup()
        self.start_tom.hideturtle()
        self.start_tom.write(arg=f"Press SPACE to start game", align=ALIGNMENT, font=FONT)

    def game_over(self,i):
        self.start_tom.write(arg="Game Over", align=ALIGNMENT, font=("Courier", 40, "normal"))
        self.start_tom.goto(0,60)
        self.start_tom.write(arg=f"Player {i} Won", align=ALIGNMENT, font=FONT)