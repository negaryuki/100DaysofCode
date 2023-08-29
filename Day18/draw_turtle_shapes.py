from turtle import Turtle, Screen
import random

shape = Turtle()

color = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple",
         "navy", "blue", "skyblue","turquoise", "lightgreen",
          "green", "darkgreen", "chocolate", "brown", "black", "gray"
]

def draw_shape(sides):
    angle = 360 / sides
    for i in range(sides):
        shape.forward(100)
        shape.right(angle)


for no_sides in range(3, 10):
    shape.color(random.choice(color))
    draw_shape(no_sides)

screen = Screen()
screen.exitonclick()
