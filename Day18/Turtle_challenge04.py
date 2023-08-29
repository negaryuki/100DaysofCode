from turtle import Turtle, Screen
import random

walk = Turtle()

color = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple",
         "navy", "blue", "skyblue","turquoise", "lightgreen",
          "green", "darkgreen", "chocolate", "brown", "black", "gray"
]

directions = [0, 90, 180, 270]

for loop in range(200):
    walk.forward(30)
    walk.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()