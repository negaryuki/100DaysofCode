from turtle import Turtle , Screen
import random

race_on = False

screen = Screen()

screen.setup(width=500, height=400)

user_bet = screen.textinput("Make Your Bet", " Which Turtle will win? Choose a color")

colors =["red", "orange","yellow","green","blue", "purple"]

y_position = [-70,-40, -10,20 ,50, 80]

all_turtles = []
	
for i in range(0,6):
	new_turtle = Turtle(shape="turtle")
	new_turtle.penup()
	new_turtle.color(colors[i])
	new_turtle.goto(x= -230 ,y= y_position[i])
	all_turtles.append(new_turtle)

if user_bet:
	race_on = True
	
while race_on:
	
	for i in all_turtles:
		
		if i.xcor() > 230:
			race_on = False
			winner = i.pencolor()
			
			if winner == user_bet:
				print(f'You have won! the {winner} turtle is the winner')
				
			else:
				print(f'You loose! the {winner} turtle is the winner')
										
		rand_distance = random.randint(0,10)
		i.forward(rand_distance)
	

		

screen.exitonclick()
