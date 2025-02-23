#Turtle race
import turtle as t
import random as r

My_screen=t.Screen()
My_screen.setup(width=500,height=400)
user_choice=My_screen.textinput(title="Turtle selection",prompt="Which turtle win's?")
is_race_on=True
colours=["red","blue","green","yellow","orange","purple"]
y_positions=-70
list_turtles=[]
for i in range(6):
    tim=t.Turtle(shape="turtle")
    tim.penup()
    tim.color(colours[i])
    tim.goto(x=-230, y=y_positions)
    y_positions+=30
    list_turtles.append(tim)

while is_race_on:
    for turtle in list_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winner=turtle.pencolor()
            if winner==user_choice:
                print(f"You Won")
            else:
                print(f"You lost, The winner is {winner} turtle")
        move = r.randint(0, 10)
        turtle.forward(move)


My_screen.exitonclick()