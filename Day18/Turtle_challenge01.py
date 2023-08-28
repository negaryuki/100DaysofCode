from turtle import Turtle, Screen

square = Turtle()

# use the loop for each side:
for i in range(4):
    square.forward(100)
    square.right(90)

screen = Screen()
screen.exitonclick()
