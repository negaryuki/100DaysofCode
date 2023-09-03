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
			self.xmove = 10
			self.ymove = 10
			
		def movement(self):
			new_x = self.xcor() + self.xmove
			new_y = self.ycor() + self.ymove
			self.goto(new_x,new_y)
		
		def bounce_y (self):
			self.ymove*= -1
	
		def bounce_x (self):
			self.xmove*= -1
