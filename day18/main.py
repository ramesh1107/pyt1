import random
import turtle as t
screen= t.Screen()

tim = t.Turtle()
tim.shape("turtle")
t.colormode(255)
tim.speed("fastest")

'''colors = ["red", "green", "blue", "black", "purple", "brown", "purple"]
def draw_shape(n):
    angle = 360/n
    for _ in range(n):
        tim.forward(100)
        tim.right(angle)
    
  
for n in range(3,11):
    tim.color(random.choice(colors))
    draw_shape(n)
    n+=1'''

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

def draw_spirograph(size):
    
    for _ in range(int(360/size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+size)

draw_spirograph(7)
 
'''def random_walk():
    tim.pensize(5)
    tim.speed("fast")
    for _ in range(200):
        tim.color(random_color())
        tim.forward(30)
        tim.setheading(random.choice([0,90,180,270]))

 
random_walk()'''
    


screen.exitonclick()
