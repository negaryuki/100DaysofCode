import time
from turtle import Turtle, Screen

# setup Screen:

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Turns off the animation, however, in order to see anything, we need to use the update method later

# Step 1: Create a snake:

segment_distance = [(0, 0), (-20, 0), (-40, 0)]  # create a tuple to define snake segments location
snake = []  # create an empty list to hold the segments later on

for position in segment_distance:
    segment = Turtle("square")
    segment.color("white")
    segment.penup()
    segment.goto(position)
    snake.append(segment)

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)

    for seg in range(len(snake) - 1, 0, -1):
        new_x = snake[seg - 1].xcor()
        new_y = snake[seg - 1].ycor()
        snake[seg].goto(new_x, new_y)
    snake[0].forward(10)



screen.exitonclick()
