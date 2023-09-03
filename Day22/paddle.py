from turtle import Turtle


# Paddle description:

# width = 20
# height = 100
# x_pos = 350
# y_pos = 0


# Define constants:	


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)  # turtle size start at 20 x 20
        # in order to 100 --> 20x(5
        self.color("white")
        self.penup()
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
