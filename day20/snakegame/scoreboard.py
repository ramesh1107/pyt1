from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open ('/Users/Ramesh/Pgms/python/day20/snakegame/data.txt') as file:
           self.high_score = int(file.read())
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        #with open ('/Users/Ramesh/Pgms/python/day20/snakegame/data.txt') as file:
        #    self.high_score = int(file.read()) 
        self.write(f"Score: {self.score} High score {self.high_score}", align=ALIGNMENT, font=FONT)

    '''def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)'''
   
    def reset (self):
        if self.score > self.high_score:
            self.high_score= self.score
            with open ('/Users/Ramesh/Pgms/python/day20/snakegame/data.txt', mode ="w") as file:
                file.write(f"{self.high_score}")
        self.score =0
        self.update_scoreboard()
          
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
