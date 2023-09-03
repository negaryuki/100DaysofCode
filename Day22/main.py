from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

# setup Screen:

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0). # controls animation, by setting 0 it removes the animation

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball = Ball()

game_on = True
screen.listen()

# r_paddle movement control:
	
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

#l_paddle movement control:
	
screen.onkey(l_paddle.up, "w")
screen.onkey(_paddle.down, "s")

while game_on:
	time.sleep(0.1)
	screen.update() 
	ball.movement() 



screen.exitonclick()