import turtle
from turtle import Turtle, Screen
import colorgram

colors = colorgram.extract('images.jpeg', 6)
rgb = []


for i in colors:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    new_color = (r ,g ,b)
    rgb.append(new_color)

print(rgb)

screen = Screen()
screen.exitonclick()
