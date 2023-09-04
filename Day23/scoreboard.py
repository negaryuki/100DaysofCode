from turtle import Turtle
# define constants:
ALIGNMENT = "left"	
FONT =("Courier", 24, "normal")

	
class Scoreboard(Turtle):
		def __init__(self,position):
			super().__init__()
			self.level = 1
			self.hideturtle()
			self.penup()
			self.goto(-280,250)
			self.update_scorecoard()
		
		def update_scoreboard(self)
			self.clear()
			self.write(f"Level:{self.level}",alignment = ALIGNMENT, font=FONT)
		
		def increase_level(self):
			self.level+= 1
			self.update_scoreboard()
			
		def game_over(self):
			self.goto(0,0)
			self.color("red")
			self.write("GAME OVER", False,"center", FONT)
			
	
