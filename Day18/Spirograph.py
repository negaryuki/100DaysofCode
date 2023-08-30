import turtle
from turtle import Turtle, Screen
import random

spirograph = Turtle()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


spirograph.speed("fastest")


def draw_spirograph(gap_size):
    for i in range(int(360 / gap_size)):
        spirograph.circle(100)
        spirograph.color(random_color())
        spirograph.setheading(spirograph.heading() + gap_size)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()
