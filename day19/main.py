import turtle as t
import random

tim =t.Turtle()
screen= t.Screen()

def movef():
     tim.forward(100)
     
def moveb():
     tim.back(100)

def movel():
     tim.left(90)
     tim.forward(100)
     
def mover():
     tim.right(90)
     tim.forward(100)

def movec():
     tim.clear()

screen.listen()
screen.onkey(movef,"w")
screen.onkey(moveb, 's')
screen.onkey(movel, 'a')
screen.onkey(mover, 'd')
screen.onkey(key = "c", fun= movec)

screen.exitonclick()    