from turtle import Turtle , Screen


screen = Screen()

screen.setup(width=500, height=400)

user_bet = screen.textinput("Make Your Bet", " Which Turtle will win? Choose a color")

colors =["red", "orange","yellow","green","blue", "purple"]

y_position = [-70,-40, -10,20 ,50, 80]
	
for i in range(0,6)
	tim = Turtle(shape="turtle")
	tim.penup()
	tim.color(colors[i])
	tim.goto(x= -230 ,y= y_position[i])
	

screen.exitonclick()

