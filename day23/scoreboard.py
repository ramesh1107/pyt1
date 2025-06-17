from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
     def __init__(self):
          super().__init__()
          self.color("white")
          self.level =1
          self.penup()
          self.goto(-280,250)
          self.hideturtle()
          self.upd_score()

     def upd_score(self):
         self.clear()
         self.write(f"Level {self.level}", align ="left", font=FONT)  

     def inc_lvl(self):
        self.level +=1
        self.upd_score()
     
     def gm_ovr(self):
        self.goto(0,0)
        self.write(f"Game Over Bittu",align="center",font=FONT)
