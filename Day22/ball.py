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
			self.move_speed = 0.1
			
		def movement(self):
			new_x = self.xcor() + self.xmove
			new_y = self.ycor() + self.ymove
			self.goto(new_x,new_y)
		
		def bounce_y (self):
			self.ymove*= -1
			self.move_speed *= 0.5. # increases speed whenever ball hits paddle
	
		def bounce_x (self):
			self.xmove*= -1
			self.move_speed *= 0.5
			
			
		def reset_position(self):
			self.goto(0,0)
			self.move_speed = 0.1
			self.bounce_x()
