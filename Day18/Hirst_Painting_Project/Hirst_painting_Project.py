import random
import turtle
from turtle import Turtle, Screen

color_list = [(28, 161, 195), (198, 159, 48), (176, 180, 184), (127, 198, 154), (163, 125, 184),
              (243, 153, 191), (159, 24, 34), (109, 115, 120), (35, 177, 81), (5, 6, 8), (245, 238, 37), (223, 26, 119),
              (237, 30, 40), (75, 64, 34), (241, 210, 223), (210, 236, 219), (196, 213, 218), (188, 160, 25),
              (181, 0, 0)]

turtle.colormode(255)
painting = Turtle()
painting.penup()
painting.speed("fast")
painting.setheading(225)
painting.forward(300)
painting.setheading(0)
painting.hideturtle()

dot_numbers = 100

for i in range(1, dot_numbers + 1):

    painting.dot(20, random.choice(color_list))
    painting.forward(50)

    if i % 10 == 0:
        painting.setheading(90)
        painting.forward(50)
        painting.setheading(180)
        painting.forward(500)
        painting.setheading(0)

screen = Screen()
screen.exitonclick()
