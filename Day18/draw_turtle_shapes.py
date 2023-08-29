from turtle import Turtle, Screen

shape = Turtle()


def draw_shape(sides):
    angle = 360 / sides
    for i in range(sides):
        shape.forward(100)
        shape.right(angle)


for no_sides in range(3, 10):
    draw_shape(no_sides)

screen = Screen()
screen.exitonclick()
