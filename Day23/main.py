import time
from turtle import Screen
from player import Player
from car_manager import CarManager 
from scoreboard import Scoreboard


# setup screen:
	
screen = Screen()
screen.setup(width-600, height=600)
screen.tracer(0).  # remove animation


player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.go_up,"Up")	
game_on = True

while game_on:
	time.sleep(0.1)
	screen.update()	
	
	car_manager.create_car(_)
	car_manager.move_cars()
	
	# Detect collisionn with car:
		
	for car in car_manager.all_cars:
		if car.distance(player) < 20:
			game_on = False
			
	# Detect successful crossing:
		
	if is_at_finishline():
		player.go_to_start()
		car_manager.level_up()

			 
		
		
screen.exitonclick()		
