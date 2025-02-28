#Pong Game
import time
from ball import Ball
from paddle import Paddle, My_screen
from scoreboard import Scoreboard

BG_COLOR="black"
SCREEN_WIDTH=1000
SCREEN_HEIGHT=600

My_screen.setup(width=SCREEN_WIDTH,height=SCREEN_HEIGHT)
My_screen.bgcolor(BG_COLOR)

paddle=Paddle()
ball=Ball()
scoreboard=Scoreboard()

My_screen.listen()
My_screen.onkeypress(paddle.up_right,"Up")
My_screen.onkeypress(paddle.down_right,"Down")
My_screen.onkeypress(paddle.up_left,"w")
My_screen.onkeypress(paddle.down_left,"s")

def game_started():
    game_is_on = True
    scoreboard.start_tom.clear()
    ball.start_ball()
    while game_is_on:
        time.sleep(0.05)
        if -500<ball.xcor()<500 and -300<ball.ycor()<300:
            if -285<ball.ycor()<289:
                if paddle.paddles[0].distance(ball) < 30 and ball.xcor()<-480:
                    ball.paddle_hit()
                elif paddle.paddles[1].distance(ball) < 30 and ball.xcor()>470:
                    ball.paddle_hit()
                ball.move_ball()
            else:
                ball.reflect_ball()
                ball.move_ball()
        else:
            game_is_on=False

    My_screen.clear()
    My_screen.bgcolor(BG_COLOR)
    if ball.xcor() > 0:
        scoreboard.game_over(1)
    else:
        scoreboard.game_over(2)

My_screen.onkey(game_started,"space")

My_screen.exitonclick()