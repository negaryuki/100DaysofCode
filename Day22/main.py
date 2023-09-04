from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# setup Screen:

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)  # controls animation, by setting 0 it removes the animation

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()

game_on = True

screen.listen()

# r_paddle movement control:

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

# l_paddle movement control:

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

while game_on:

    time.sleep(ball.move_speed)  # defines speed of game
    screen.update()
    ball.movement()

    # Detect Ball collision with wall:

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with r_paddle:
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    # Point for left:
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Point for right:
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
