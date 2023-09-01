from turtle import Turtle, Screen

# setup Screen:

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")

# Step 1: Create a snake:

segment_distance = [(0, 0), (-20, 0), (-40, 0)]  # create a tuple to define snake segments location
snake = []   # create an empty list to hold the segments later on

for position in segment_distance:
    segment = Turtle("square")
    segment.color("white")
    segment.penup()
    segment.goto(position)
    snake.append(segment)


screen.exitonclick()
