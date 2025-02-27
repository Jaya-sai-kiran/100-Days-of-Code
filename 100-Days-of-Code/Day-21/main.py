#Snake game-->Final Part
from snake import Snake,My_screen
from scoreboard import Scoreboard
from food import Food

BGCOLOR="black"
SCREEN_WIDTH=600
SCREEN_HEIGHT=600

My_screen.setup(width=SCREEN_WIDTH,height=SCREEN_HEIGHT)
My_screen.bgcolor(BGCOLOR)
My_screen.title("My Snake Game")
My_screen.tracer(0)

snake=Snake()
food=Food()
score=Scoreboard()

My_screen.listen()
My_screen.onkey(snake.up,"Up")
My_screen.onkey(snake.down,"Down")
My_screen.onkey(snake.left,"Left")
My_screen.onkey(snake.right,"Right")

points=0
game_is_on=True
while game_is_on:
    if -SCREEN_WIDTH/2<snake.head.xcor()<SCREEN_WIDTH/2 and -SCREEN_HEIGHT/2<snake.head.ycor()<SCREEN_HEIGHT/2:
        snake.move_forward()
        if snake.head.distance(food) < 15:
            food.refresh()
            My_screen.update()
            score.score_board()
            snake.create_snake()
    else:
        game_is_on = False
        My_screen.clear()
        My_screen.bgcolor(BGCOLOR)
        score.game_over()

    for i in snake.snakes[1:]:
        if snake.head.distance(i) < 10:
            game_is_on = False
            My_screen.clear()
            My_screen.bgcolor(BGCOLOR)
            score.game_over()

My_screen.exitonclick()
