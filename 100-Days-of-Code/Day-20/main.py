#Snake game--->Initial Part
from snake import Snake,My_screen

My_screen.setup(width=600,height=600)
My_screen.bgcolor("black")
My_screen.title("My Snake Game")
My_screen.tracer(0)

sn=Snake()
My_screen.listen()
My_screen.onkey(sn.up,"Up")
My_screen.onkey(sn.down,"Down")
My_screen.onkey(sn.left,"Left")
My_screen.onkey(sn.right,"Right")


game_is_on=True
while game_is_on:
    sn.move_forward()

My_screen.exitonclick()
