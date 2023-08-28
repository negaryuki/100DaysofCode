from turtle import Turtle, Screen

triangle = Turtle()
square = Turtle()
pentagon = Turtle()
hexagon = Turtle()
heptagon = Turtle()
octagon = Turtle()
nonagon = Turtle()
decagon = Turtle()

for i in range(3):
    triangle.forward(100)
    triangle.right(360/3)

for i in range(4):
    square.forward(100)
    square.right(360/4)

for i in range(5):
    pentagon.forward(100)
    pentagon.right(72)

for i in range(6):
    hexagon.forward(100)
    hexagon.right(365/6)

for i in range(7):
    heptagon.forward(100)
    heptagon.right(360/7)

for i in range(8):
    octagon.forward(100)
    octagon.right(360/8)

for i in range(9):
    nonagon.forward(100)
    nonagon.right(360/9)

for i in range(10):
    decagon.forward(100)
    decagon.right(360/10)

screen = Screen()
screen.exitonclick()
