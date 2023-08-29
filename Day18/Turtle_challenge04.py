import turtle
from turtle import Turtle, Screen
import random

walk = Turtle()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


directions = [0, 90, 180, 270]
walk.pensize(18)
walk.speed("fast")

for loop in range(200):
    walk.forward(30)
    walk.setheading(random.choice(directions))
    walk.color(random_color())

screen = Screen()
screen.exitonclick()
