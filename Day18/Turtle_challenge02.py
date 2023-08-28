from turtle import Turtle, Screen

dashed_line = Turtle()

# use penup() and pendown() method

for i in range(5):
    dashed_line.forward(10)
    dashed_line.penup()
    dashed_line.forward(10)
    dashed_line.pendown()

screen = Screen()
screen.exitonclick()

# using color method

# for i in range(5):
#     dashed_line.forward(10)
#     dashed_line.pencolor("red")
#     dashed_line.forward(10)
#     dashed_line.pencolor("white")
