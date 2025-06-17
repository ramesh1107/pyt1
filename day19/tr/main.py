import turtle as t
import random


screen= t.Screen()
screen.setup(width=700, height=700)
is_race_on = False
user_bet= screen.textinput(title= "Make your bet", prompt="Enter your color: ")

print(user_bet)
all_turtles = []
colors = ["red", "green", "blue", "black", "purple", "brown", "purple"]
y_positions = [-100,-50,0,50,100,150,200]

for i in range(0,6):
    new_turtle =t.Turtle()
    new_turtle.penup()
    new_turtle.shape("turtle")
    new_turtle.color(colors[i])
    new_turtle.goto(x=-300,y=y_positions[i])
    all_turtles.append(new_turtle)
if user_bet:
    is_race_on= True

while is_race_on:
    
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on = False
            win_color =turtle.pencolor()
            if win_color == user_bet:
                print(f"You've won! The {win_color} turtle is the winner!")

            else:
                print(f"You've lost! The {win_color} turtle is the winner!")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
screen.exitonclick()