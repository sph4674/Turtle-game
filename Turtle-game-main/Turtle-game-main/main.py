import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
car_manager=CarManager()
scoreboard=Scoreboard()

screen.setup(width=600, height=600)
screen.title("Turtle crossing the road")
screen.tracer(0)

screen.listen()
screen.onkey(player.move_forward,"Up")
screen.onkey(player.move_backward, "Down")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()


    #detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player)<20:
            game_is_on=False
            scoreboard.game_over()

    #detect successfull crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increse_level()
        scoreboard.update_scoreboard()

screen.exitonclick()
