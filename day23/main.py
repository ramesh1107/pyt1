import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
player = Player()
score=Scoreboard()
car_manager= CarManager()

screen.listen()
screen.onkey(player.g_up ,"Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    #Detect Turtle collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.gm_ovr()

    #Detect Turtle sucessfull cross 
        if player.is_finish():
            player.go_to_start()
            car_manager.level_up()
            score.inc_lvl()


screen.exitonclick()
