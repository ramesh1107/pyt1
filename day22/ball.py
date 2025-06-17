from turtle import Turtle 


class Ball(Turtle):
 def __init__(self):
    super().__init__()
     
    self.color("white") 
    self.shape("circle")
    self.penup()
    self.x_move = 10
    self.y_move = 10
    self.mv_speed= 0.1
 
 def move(self):
   n_x=self.xcor() + self.x_move
   n_y=self.ycor() + self.y_move
   self.goto(n_x, n_y) 

 def bounce_y(self):
   self.y_move *=-1
   self.mv_speed *= 0.9
   
 def bounce_x(self):
   self.x_move *=-1
   self.mv_speed *= 0.9
  
 def reset_post(self):
   self.goto(0,0)
   self.mv_speed = 0.1
   self.bounce_x

