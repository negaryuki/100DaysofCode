from turtle import Turtle
from random import Random

# Ball definition:
	
# width = 20
# height = 20
# starting x_pos = 0
# starting y_pos = 0

class Ball(Turtle):
		def __init__(self,position):
			super().__init__()
			self.shape = "circle"
			self.color("white")
			self.penup()
			
			
		def movement(self):
			new_x = self.xcor() + 10
			new_y = self.ycor() + 10
			self.goto(new_x,new_y)
