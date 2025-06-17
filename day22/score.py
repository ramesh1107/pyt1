from turtle import Turtle
ALIGN="center"
FONT=("comicsans",24,"bold")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()  
        self.l_score = 0
        self.r_score= 0
        self.up_score()
        
    
    def up_score(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score, align= ALIGN, font= FONT)
        self.goto(100,200)
        self.write(self.r_score, align= ALIGN, font= FONT)

    def l_point(self):
        self.l_score +=1
        self.up_score()
    
    def r_point(self):
        self.r_score +=1
        self.up_score()