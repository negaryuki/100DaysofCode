from turtle import Turtle , Screen

tim = Turtle()

screen = Screen()

def move_forward():
	tim.forward(10)
	
def move_backwards():
	tim.backward(10)
	
def move_left():
	tim.left(10)
	
def move_right():
	tim.right(10)
	
def clear():
	tim.clear()
	tim.penup()
	tim.home()
	tim.pendown()
	
	
screen.listen()
screen.onkey("w" , move_forward)
screen.onkey("s" , move_backwards)
screen.onkey("a" , move_left)
screen.onkey("d" , move_right)
clear()
