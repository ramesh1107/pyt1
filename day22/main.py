from turtle import Screen, Turtle
import time
from paddle import Paddle
from ball import Ball
from score import Score

screen = Screen()
#paddle =Paddle() 
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My pingpong game")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball ()
score= Score()
game_on = True

screen.listen()


screen.onkey(r_paddle.g_up ,"Up")
screen.onkey(r_paddle.g_down,"Down")
screen.onkey(l_paddle.g_up ,"s")
screen.onkey(l_paddle.g_down,"w")


while game_on:
    time.sleep(ball.mv_speed)
    screen.update()
    ball.move()
   
    # detect collision with wall

    if ball.ycor() > 280 or ball.ycor() <-280:
        ball.bounce_y()
          
    # detect collision with both paddle

    if ball.distance(r_paddle) <50 and ball.xcor() >320 or ball.distance(l_paddle) <50 and ball.xcor() >-320:
        ball.bounce_x()
    
    # detect collision with right paddle
    if ball.xcor() >380:
        ball.reset_post()
        score.l_point()
     
     # detect collision with left paddle
    if ball.xcor() < -380:
        ball.reset_post()
        score.r_point()

screen.exitonclick()