from turtle import Turtle

# Step 1: Create a snake:

# These are constants and are reachable throughout the class
SEGMENT_DISTANCE = [(0, 0), (-20, 0), (-40, 0)]  # create a tuple to define snake segments location
MOVE_DISTANCE = 20  # we create constants so that in case we want to make chages in the games option,


# we merely access it through the start of the code rather than the whole code body

class Snake:

    def __init__(self):
        self.snake = []  # create an empty list to hold the segments later on
        self.create_snake()  # method to create a snake
        self.move()

    def create_snake(self):
        for position in SEGMENT_DISTANCE:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.snake.append(segment)

    def move(self):
        for seg in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg - 1].xcor()
            new_y = self.snake[seg - 1].ycor()
            self.snake[seg].goto(new_x, new_y)
        self.snake[0].forward(MOVE_DISTANCE)

    # Define methods to control the snake with arrow keys
    def up(self):
        self.snake[0].setheading(90) # Set the snake's heading to 90 degrees (upward)
        self.move()

    def down(self):
        self.snake[0].setheading(270) # Set the snake's heading to 270 degrees (downward)
        self.move()
        self.move()

    def left(self):
        self.snake[0].setheading(180)  # Set the snake's heading to 180 degrees (leftward)
        self.move()

    def right(self):
        self.snake[0].setheading(0) # Set the snake's heading to 0 degrees (rightward)
        self.move()