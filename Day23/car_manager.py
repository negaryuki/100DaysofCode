from turtle import Turtle
import random
# Define Constants:
	
COLOR = ["red","orange","yellow","green","blue","purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
	
	
class CarManager:
	
	def __init__(self):
		self.all_cars= []

	def create_car(self):
		random_chance = random.randint(1,6)
		
		if random_chance ==1:         # every 6 times the while loop runs, a car will be generated. 
		
			new_car = Turtle("square")
			new_car.shapesize(stretch_wid=1 , stretch_len=2). #20 x 400
			new_car.penup()
			new_car.color(random.choice(COLOR))
			random_y = randint(-250,250)
			new_car.goto(300,random_y)
			self.all_cars.append(new_car)
		
	def move_cars(self):
		
		for car self.all_cars:
			car.backward(STARTING_MOVE_DISTANCE)
		
