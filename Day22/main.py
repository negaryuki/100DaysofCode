from turtle import Turtle, Screen
from paddle import Paddle


# setup Screen:

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0). # controls animation, by setting 0 it removes the animation

paddle = Paddle()
game_on = True

screen.listen()
screen.onkey(paddle.up, "Up")

while game_on:
	screen.update() 



screen.exitonclick()






screen.exitonclick()
